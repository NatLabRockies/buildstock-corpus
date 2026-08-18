"""Audit the .md generator's fidelity on tables and figures.

The extractors keep a `Table N.` / `Figure N.` caption line even when the thing the
caption describes never made it into the markdown. That is the failure mode worth
finding: the surrounding prose still says "as shown in Table 5", so a reader (or an
LLM) is promised a table that isn't there and has to either hallucinate it or give up.

For every processed .md file this script pairs each caption against the artifact it
actually binds to:

  table caption   satisfied by a markdown table block, or a raw <table> (unconverted)
  figure caption  satisfied by a markdown image ![...], a raw <img>, or a fenced code
                  block (some "figures" are listings, e.g. an EnergyPlus object)

The binding is *directional*: scan forward from the caption to the first decisive line
(an artifact of any kind, the next caption, or the next heading) and let that line decide.
Only if nothing forward decides it do we scan a short way backward, for the docs that put
the caption underneath its artifact. An undirected "is there a table within N lines"
window is not enough — where captions are dense it lets a caption whose own table is
missing be satisfied by its *neighbour's* table, which is exactly how 13 dropped tables
in measure_pdfs/ hid behind a clean report.

A caption that binds to nothing, or to the wrong kind of artifact, is reported as
ORPHANED — the content is gone.

Image references are also resolved against the filesystem: a ref pointing at a file that
was never copied into processed/ is reported as DANGLING. Raw <table>/<img> HTML that
survived is reported as UNCONVERTED — it still carries the content, but it is not clean
markdown. (In the LaTeX reference the <table>s use rowspan/colspan, which GFM pipe tables
cannot express, so those are expected to remain HTML.)

Duplicated H1 headings are reported too: the write step injects `# {title}` above a body
that may already start with the same heading.

Separately from the caption/artifact audit, each file is scored for CHARACTER HYGIENE: soft
hyphens, non-breaking spaces and digit-flanked en dashes. There the content is present but
spelled with a character that defeats retrieval — a converter rendering a typesetting hint
literally. Those are invisible in a rendered view, so they need a counted scoreboard.

Results are grouped by extractor (latex / markdown / measures / pdf) so it is clear
which path is losing content.

Usage:  uv run python scripts/audit_md_fidelity.py [--release 2025-3] [--product comstock]
"""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

REPO = Path(__file__).resolve().parent.parent

# Anchored at line start so prose mentions ("as shown in Table 5") are not counted as
# captions. Allows leading bold/italic markers, which pandoc and docling both emit.
CAPTION = re.compile(
    r"^\s*(?:\*\*|__|\*|_)?\s*(Table|Figure|Fig\.?)\s*([0-9]+[A-Za-z]?)\s*[.:)]",
    re.IGNORECASE,
)
MD_TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
MD_TABLE_DELIM = re.compile(r"^\s*\|[\s:|\-]+\|\s*$")
MD_IMAGE = re.compile(r"!\[[^\]]*\]\(")
HTML_TABLE = re.compile(r"<table\b", re.IGNORECASE)
HTML_IMG = re.compile(r"<img\b", re.IGNORECASE)
CODE_FENCE = re.compile(r"^\s*(?:```|~~~)")

# Targets, for resolving refs against disk. Skips external URLs and data: URIs.
MD_IMAGE_TARGET = re.compile(r"!\[[^\]]*\]\(\s*([^)\s]+)")
HTML_IMG_TARGET = re.compile(r"<img\b[^>]*?\bsrc\s*=\s*[\"']([^\"']+)[\"']", re.IGNORECASE)
H1 = re.compile(r"^#\s+(.+?)\s*$")
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*$")
# "List of Figures" / "List of Tables" / "Table of Contents" sections legitimately repeat
# every caption with no artifact beside them; counting those as orphans is a false positive.
TOC_HEADING = re.compile(r"^(?:list of (?:figures|tables)|(?:table of )?contents)\b", re.IGNORECASE)

# A section-numbered title reproduced *inside* a table ("**TABLE 6.5.1.1.3A High-Limit
# Shutoff...**", lifted from ASHRAE 90.1) matches CAPTION but is not one of our captions.
# Multi-level dotted numbering is the tell: a real caption reads "Table 6. Something".
# Treating these as "the next caption" ends the forward scan one line early and reports a
# recovered table as dropped (89128.md:521).
SUBNUMBERED = re.compile(
    r"^\s*(?:\*\*|__|\*|_)?\s*(?:Table|Figure|Fig\.?)\s*[0-9]+(?:\.[0-9]+)+", re.IGNORECASE
)
# Sub-figure labels between a multi-panel image and its caption: "- (a) Three-pipe system".
# Requires the parenthesised single letter, so ordinary bullets are not swallowed.
SUBFIGURE = re.compile(r"^\s*(?:[-*+]\s*)?(?:\*\*|__|\*|_)?\(?[A-Za-z]\)")
COMMENT_OPEN = re.compile(r"<!--")
COMMENT_CLOSE = re.compile(r"-->")

# How far a caption may reach for its artifact, counted in *content* lines: blank lines, HTML
# comments and in-table titles are walked for free (see skippable / _reach). Only a backstop for
# pathological input — what actually keeps a caption from claiming its neighbour's table is
# boundary(), and _bind_below_strict stops at the first non-skippable line regardless. Measured
# corpus-wide, orphan counts are flat from 12 all the way out to 60, which is the evidence that
# this number is not the operative bound; 16 leaves headroom without pretending otherwise.
#
# Counting content rather than raw lines is what makes the budget mean something stable. An
# overlay's provenance comment is as long as its justification needs to be — 96598's replacement
# entries carry a paragraph explaining what they superseded and why, ten comment lines before
# the table starts — and under a raw line budget, writing a fuller explanation would push a
# recovered table out of reach and report it as still missing. Distance between a caption and its
# table is a property of the document, not of how much we had to say about it.
WINDOW = 16
BACK_WINDOW = 6  # content lines above a caption, for docs that put the caption under the artifact
# Absolute line cap on either reach, so an unterminated comment cannot run a scan away.
SCAN_CAP = 200

# Character hygiene. Separate from the caption/artifact audit: the content is present, but
# spelled with characters that defeat retrieval. All three come from a converter rendering a
# *typesetting hint* as a literal character, and all three are invisible or near-invisible in
# a rendered view, which is why they need a counted scoreboard rather than a reader's eye.
#
#   soft hyphen (U+00AD)  pandoc's rendering of TeX's `\-`. Sits *inside* identifiers —
#                         `HPA<AD>CCOOL<AD>PLFFPLR`, `FullService<AD>Restaurant`, `EIA<AD>861` —
#                         so a lexical or hybrid search for the real spelling misses the doc.
#   nbsp (U+00A0)         from `~`. Not a space to anything that tokenizes on whitespace.
#   range en dash         a digit-flanked U+2013: `1980–2004`, `132–220`. The corpus spells the
#                         same vintage bin both ways, so one entity has two spellings and a
#                         search for either misses the other.
#
# Only digit-flanked en dashes are counted. An en dash standing alone in a table cell is an
# empty-value placeholder meaning "no value" — folding those to ASCII would read as a value or
# a minus sign, so they are left alone by design and are not a finding. ° ® ™ · smart quotes,
# em dashes and U+2212 minus are all legitimate and deliberately unmeasured.
SOFT_HYPHEN = "\u00ad"
NBSP = "\u00a0"
RANGE_EN_DASH = re.compile(r"(?<=\d)\u2013(?=\d)")
CHAR_CLASSES = ("soft_hyphens", "nbsp", "range_en_dashes")


def _reach(lines: list[str], i: int, comments: set[int], step: int, budget: int):
    """Line indices out from caption `i`, spending `budget` only on non-skippable lines."""
    for n in range(1, SCAN_CAP + 1):
        j = i + step * n
        if not 0 <= j < len(lines):
            return
        yield j
        if not skippable(lines, j, comments):
            budget -= 1
            if budget <= 0:
                return


def toc_lines(lines: list[str]) -> set[int]:
    """Line numbers inside a list-of-figures/tables or contents section."""
    out: set[int] = set()
    in_toc = False
    for i, line in enumerate(lines):
        m = HEADING.match(line)
        if m:
            in_toc = bool(TOC_HEADING.match(m.group(1)))
        elif in_toc:
            out.add(i)
    return out


def image_targets(lines: list[str]) -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        for pat in (MD_IMAGE_TARGET, HTML_IMG_TARGET):
            for m in pat.finditer(line):
                out.append((i, m.group(1)))
    return out


def _is_file(path: Path) -> bool:
    """MAX_PATH-tolerant is_file().

    Win32 rejects paths over 260 chars unless they carry the \\\\?\\ prefix, so a plain
    is_file() reports "missing" for files that are really there. Docling's hash-suffixed
    image names put some corpus paths right at that boundary, and reporting those as
    DANGLING would be a false positive about lost content. Probe the long-path form
    before believing the miss.
    """
    if path.is_file():
        return True
    if os.name == "nt":
        resolved = str(path.resolve())
        if not resolved.startswith("\\\\"):
            return Path(f"\\\\?\\{resolved}").is_file()
    return False


def dangling_refs(md_path: Path, lines: list[str]) -> list[dict]:
    """Image refs whose target file is not present next to the .md file."""
    out: list[dict] = []
    for line_no, target in image_targets(lines):
        if re.match(r"^(?:[a-z][a-z0-9+.-]*:|//|#)", target, re.IGNORECASE):
            continue  # http(s), data:, protocol-relative, in-page anchor
        clean = unquote(target.split("#")[0].split("?")[0])
        if not clean:
            continue
        if not _is_file(md_path.parent / clean):
            out.append({"line": line_no + 1, "target": target[:120]})
    return out


def duplicate_h1(lines: list[str]) -> list[dict]:
    """The injected `# {title}` followed (ignoring blanks) by the same H1 from the body."""
    heads = [(i, m.group(1)) for i, line in enumerate(lines) if (m := H1.match(line))]
    out: list[dict] = []
    for (i, a), (j, b) in zip(heads, heads[1:]):
        if a == b and not any(ln.strip() for ln in lines[i + 1 : j]):
            out.append({"line": j + 1, "heading": a[:100]})
    return out


def character_hygiene(text: str) -> dict[str, int]:
    """Counts of the retrieval-defeating characters, by class. Zero is the target for all."""
    return {
        "soft_hyphens": text.count(SOFT_HYPHEN),
        "nbsp": text.count(NBSP),
        "range_en_dashes": len(RANGE_EN_DASH.findall(text)),
    }


def table_block_lines(lines: list[str]) -> set[int]:
    """Line numbers (0-based) belonging to a real markdown table block.

    A block is 2+ consecutive pipe rows; a delimiter row alone is enough to confirm.
    """
    out: set[int] = set()
    run: list[int] = []
    for i, line in enumerate(lines):
        if MD_TABLE_ROW.match(line):
            run.append(i)
            continue
        if len(run) >= 2 or any(MD_TABLE_DELIM.match(lines[j]) for j in run):
            out.update(run)
        run = []
    if len(run) >= 2 or any(MD_TABLE_DELIM.match(lines[j]) for j in run):
        out.update(run)
    return out


def marker_lines(lines: list[str], pattern: re.Pattern) -> set[int]:
    return {i for i, line in enumerate(lines) if pattern.search(line)}


def comment_lines(lines: list[str]) -> set[int]:
    """Line numbers inside an HTML comment span.

    Every chunk-1/chunk-2 overlay recovery puts a multi-line `<!-- table recovered from
    ... -->` provenance block between the caption and the table, so the scan has to step
    over comments rather than treat them as content.
    """
    out: set[int] = set()
    depth = 0
    for i, line in enumerate(lines):
        opens = len(COMMENT_OPEN.findall(line))
        closes = len(COMMENT_CLOSE.findall(line))
        if depth or opens:
            out.add(i)
        depth = max(0, depth + opens - closes)
    return out


def artifact_at(i: int, tables: set[int], images: set[int], fences: set[int]) -> str | None:
    """Which kind of artifact, if any, line `i` is evidence of."""
    if i in tables:
        return "table"
    if i in images:
        return "image"
    if i in fences:
        return "fence"
    return None


def block_start(
    i: int, kind: str, tables: set[int], images: set[int], fences: set[int]
) -> int:
    """First line of the artifact that line `i` belongs to.

    Consecutive lines of the same kind are one artifact: a caption binds to a table, not to
    one of its rows, so the question "whose table is this?" is asked of the whole block.
    """
    while i > 0 and artifact_at(i - 1, tables, images, fences) == kind:
        i -= 1
    return i


SATISFIES = {"table": {"table"}, "figure": {"image", "fence"}}


def skippable(lines: list[str], i: int, comments: set[int]) -> bool:
    """Lines that may sit between a caption and its artifact without severing them."""
    return (
        not lines[i].strip()
        or i in comments
        or bool(SUBNUMBERED.match(lines[i]))
        or bool(SUBFIGURE.match(lines[i]))
    )


def boundary(line: str) -> bool:
    """A line that ends the caption's claim on what follows."""
    return bool(HEADING.match(line)) or (bool(CAPTION.match(line)) and not SUBNUMBERED.match(line))


def _bind_adjacent(
    lines: list[str],
    i: int,
    accept: set[str],
    tables: set[int],
    images: set[int],
    fences: set[int],
    comments: set[int],
) -> int | None:
    """The artifact immediately below caption `i`, else the one immediately above it.

    "Immediately" meaning nothing but blank lines, comments, sub-figure labels or an
    in-table title in between. Below wins ties: captioning above the artifact is the
    common convention, and the measure pages that caption underneath are consistent about
    it. This runs before the prose-tolerant reach below so that a caption cannot claim the
    *next* figure's image while its own sits right above it.
    """
    for probe in (_bind_below_strict, _bind_backward):
        j = probe(lines, i, accept, tables, images, fences, comments)
        if j is not None:
            return j
    return None


def _bind_below_strict(
    lines: list[str],
    i: int,
    accept: set[str],
    tables: set[int],
    images: set[int],
    fences: set[int],
    comments: set[int],
) -> int | None:
    """Artifact directly below caption `i`, nothing but skippables in between."""
    for j in _reach(lines, i, comments, 1, WINDOW):
        found = artifact_at(j, tables, images, fences)
        if found:
            return j if found in accept else None
        if not skippable(lines, j, comments):
            return None
    return None


def _bind_forward(
    lines: list[str],
    i: int,
    accept: set[str],
    tables: set[int],
    images: set[int],
    fences: set[int],
    comments: set[int],
) -> int | None:
    """First artifact line below caption `i`, if it is one this caption accepts.

    Prose between a caption and its artifact is tolerated — the PDF docs routinely put a
    sentence of setup under a caption, and forbidding it costs 32 false positives — but the
    next caption or heading ends the search, so a caption cannot borrow its neighbour's
    table.
    """
    for j in _reach(lines, i, comments, 1, WINDOW):
        found = artifact_at(j, tables, images, fences)
        if found:
            return j if found in accept else None
        if skippable(lines, j, comments):
            continue
        if boundary(lines[j]):
            break
    return None


def _bind_backward(
    lines: list[str],
    i: int,
    accept: set[str],
    tables: set[int],
    images: set[int],
    fences: set[int],
    comments: set[int],
) -> int | None:
    """Artifact directly above caption `i`, for the docs that caption underneath it.

    Strict: only blank lines, comments, sub-figure labels and in-table titles may
    intervene. A prose-tolerant version re-borrows the previous caption's table.

    For a *table* found above, refused if that table already carries a caption of its own
    directly above it — which is what separates the two shapes that look identical from
    this caption's line. In 92618.md:272 docling emitted Table 2's rows above its caption
    (with a picture of the same table below) and prose, not a caption, sits above those
    rows, so the content is present. At 95005.md:429 the table above is captioned Table 3
    from above, so Table 4 really is gone and must not be excused by its neighbour's table.

    The same inference does not hold for images, so it is not applied to them: tables in
    this corpus are captioned above without exception, but figures are captioned above in
    some documents and below in others, and several caption *every* figure underneath. In
    those, every image has a caption above it — the previous figure's — and reading that as
    ownership orphans 8 correctly-captioned figures (measured corpus-wide).
    """
    for j in _reach(lines, i, comments, -1, BACK_WINDOW):
        found = artifact_at(j, tables, images, fences)
        if found:
            if found not in accept:
                return None
            if found == "table" and _captioned_from_above(
                lines, j, found, tables, images, fences, comments
            ):
                return None
            return j
        if not skippable(lines, j, comments):
            break
    return None


def _captioned_from_above(
    lines: list[str],
    j: int,
    kind: str,
    tables: set[int],
    images: set[int],
    fences: set[int],
    comments: set[int],
) -> bool:
    """Whether the artifact containing line `j` is already labelled by the caption above it."""
    for k in range(block_start(j, kind, tables, images, fences) - 1, -1, -1):
        if skippable(lines, k, comments):
            continue
        return bool(CAPTION.match(lines[k])) and not SUBNUMBERED.match(lines[k])
    return False


def bind_captions(
    lines: list[str],
    captions: list[tuple[int, str]],
    tables: set[int],
    images: set[int],
    fences: set[int],
    comments: set[int],
) -> dict[int, bool]:
    """Bind every caption in a document to its artifact. Returns {caption line: bound}.

    Two probes, the confident one first:

    1. **Adjacent** — the artifact directly below the caption, else directly above it.
    2. **Prose-tolerant forward** — for the captions adjacency left unbound.

    Adjacency has to come first. Reaching across prose earlier lets a caption in a
    caption-below-image document bind to the *next* figure's image while its own sits right
    above it: the count stays the same but the binding is wrong, and any later use of these
    pairings inherits the error.
    """
    bound: dict[int, bool] = {}
    for i, want in captions:
        accept = SATISFIES[want]
        bound[i] = any(
            probe(lines, i, accept, tables, images, fences, comments) is not None
            for probe in (_bind_adjacent, _bind_forward)
        )
    return bound


def classify_sources(manifest: dict) -> dict[str, str]:
    """output_path -> source_type, so gaps can be attributed to an extractor."""
    kinds: dict[str, str] = {}
    for src in manifest.get("sources", []):
        for art in src.get("artifacts", []):
            out = art.get("output_path")
            if out:
                # PDF-derived docs land under measure_pdfs/ but share the "measures"
                # source; separate them so docling is judged on its own.
                kind = art.get("source_type", src.get("type", "unknown"))
                if "measure_pdfs/" in out:
                    kind = "pdf"
                kinds[out.replace("\\", "/")] = kind
    return kinds


def audit(processed: Path, kinds: dict[str, str]) -> tuple[list[dict], dict]:
    findings: list[dict] = []
    totals: dict = defaultdict(
        lambda: {
            "files": 0,
            "table_captions": 0,
            "orphan_tables": 0,
            "figure_captions": 0,
            "orphan_figures": 0,
            "md_tables": 0,
            "html_tables": 0,
            "html_imgs": 0,
            "md_images": 0,
            "dangling_refs": 0,
            "duplicate_h1": 0,
            "soft_hyphens": 0,
            "nbsp": 0,
            "range_en_dashes": 0,
        }
    )

    for path in sorted(processed.rglob("*.md")):
        rel = path.relative_to(processed).as_posix()
        kind = kinds.get(rel, "unknown")
        raw = path.read_text(encoding="utf-8")
        lines = raw.split("\n")

        tbl = table_block_lines(lines)
        html_tbl = marker_lines(lines, HTML_TABLE)
        img = marker_lines(lines, MD_IMAGE)
        html_img = marker_lines(lines, HTML_IMG)
        fence = marker_lines(lines, CODE_FENCE)

        t = totals[kind]
        t["files"] += 1
        # Count blocks, not rows, for a readable "how many tables converted" number.
        t["md_tables"] += len([1 for i in sorted(tbl) if (i - 1) not in tbl])
        t["html_tables"] += len(html_tbl)
        t["html_imgs"] += len(html_img)
        t["md_images"] += len(img)

        dangling = dangling_refs(path, lines)
        dup_h1 = duplicate_h1(lines)
        t["dangling_refs"] += len(dangling)
        t["duplicate_h1"] += len(dup_h1)

        chars = character_hygiene(raw)
        for cls, n in chars.items():
            t[cls] += n

        in_toc = toc_lines(lines)
        comments = comment_lines(lines)
        tables = tbl | html_tbl
        images = img | html_img

        captions: list[tuple[int, str, str, str]] = []
        for i, line in enumerate(lines):
            m = CAPTION.match(line)
            if not m or i in in_toc:
                continue
            want = "table" if m.group(1).lower().startswith("t") else "figure"
            captions.append((i, want, f"{m.group(1).title()} {m.group(2)}", " ".join(line.split())[:130]))
        bound = bind_captions(
            lines, [(i, want) for i, want, _, _ in captions], tables, images, fence, comments
        )

        orphan_t: list[dict] = []
        orphan_f: list[dict] = []
        for i, want, label, caption in captions:
            if want == "table":
                t["table_captions"] += 1
                if not bound[i]:
                    t["orphan_tables"] += 1
                    orphan_t.append({"line": i + 1, "label": label, "caption": caption})
            else:
                t["figure_captions"] += 1
                if not bound[i]:
                    t["orphan_figures"] += 1
                    orphan_f.append({"line": i + 1, "label": label, "caption": caption})

        if orphan_t or orphan_f or dangling or dup_h1 or html_tbl or any(chars.values()):
            findings.append(
                {
                    "file": rel,
                    "extractor": kind,
                    "orphan_tables": orphan_t,
                    "orphan_figures": orphan_f,
                    "dangling_refs": dangling,
                    "duplicate_h1": dup_h1,
                    "unconverted_html_tables": sorted(n + 1 for n in html_tbl),
                    "unconverted_html_imgs": sorted(n + 1 for n in html_img),
                    "characters": {k: v for k, v in chars.items() if v},
                }
            )
    return findings, dict(totals)


def write_report(path: Path, findings: list[dict], totals: dict, product: str, release: str) -> None:
    lines = [
        f"# .md generator fidelity — tables and figures ({product} {release})",
        "",
        "Generated by `scripts/audit_md_fidelity.py`.",
        "",
        "**ORPHANED** = a `Table N.`/`Figure N.` caption survived but the table or image did",
        "not convert. The prose around it still cross-references the artifact, so the content",
        "is silently missing. **DANGLING** = an image reference whose target file is not present",
        "in `processed/`. **DUP H1** = the injected title heading repeated by the body's own H1.",
        "Raw `<table>`/`<img>` counts are reported for visibility: in the LaTeX reference the",
        "tables use rowspan/colspan, which GFM cannot express, so those stay as HTML by design.",
        "",
        "## Summary by extractor",
        "",
        "| extractor | files | table captions | orphaned | figure captions | orphaned | md tables | images | dangling | dup H1 | raw &lt;table&gt; | raw &lt;img&gt; |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    order = ["latex", "markdown", "measures", "pdf", "unknown"]
    for kind in [k for k in order if k in totals] + [k for k in totals if k not in order]:
        t = totals[kind]
        lines.append(
            f"| {kind} | {t['files']} | {t['table_captions']} | **{t['orphan_tables']}** | "
            f"{t['figure_captions']} | **{t['orphan_figures']}** | {t['md_tables']} | "
            f"{t['md_images'] + t['html_imgs']} | **{t['dangling_refs']}** | "
            f"**{t['duplicate_h1']}** | {t['html_tables']} | {t['html_imgs']} |"
        )
    agg = {
        k: sum(t[k] for t in totals.values())
        for k in (
            "table_captions", "orphan_tables", "figure_captions", "orphan_figures",
            "md_tables", "md_images", "html_imgs", "dangling_refs", "duplicate_h1",
            *CHAR_CLASSES,
        )
    }
    lines += [
        "",
        f"**Totals.** {agg['orphan_tables']}/{agg['table_captions']} table captions orphaned; "
        f"{agg['orphan_figures']}/{agg['figure_captions']} figure captions orphaned; "
        f"{agg['md_tables']} tables converted to markdown; "
        f"{agg['md_images'] + agg['html_imgs']} image refs present with "
        f"{agg['dangling_refs']} dangling; {agg['duplicate_h1']} duplicated H1 heading(s).",
        "",
        "## Character hygiene by extractor",
        "",
        "The content is present but spelled with characters that defeat retrieval, all of them",
        "a converter rendering a *typesetting hint* literally. **SOFT HYPHEN** (U+00AD, pandoc's",
        "`\\-`) is the worst of the three because it lands inside identifiers invisibly, so a",
        "search for the real spelling misses. **NBSP** (U+00A0, from `~`) is not a space to a",
        "whitespace tokenizer. **RANGE EN DASH** is a digit-flanked U+2013 (`1980–2004`), and the",
        "corpus spells the same vintage bin both ways, so one entity has two spellings. Zero is",
        "the target for all three. An en dash standing alone in a table cell is an empty-value",
        "placeholder, not a defect, and is deliberately not counted here.",
        "",
        "| extractor | files | soft hyphen | nbsp | range en dash |",
        "|---|---:|---:|---:|---:|",
    ]
    for kind in [k for k in order if k in totals] + [k for k in totals if k not in order]:
        t = totals[kind]
        lines.append(
            f"| {kind} | {t['files']} | **{t['soft_hyphens']}** | **{t['nbsp']}** | "
            f"**{t['range_en_dashes']}** |"
        )
    lines += [
        "",
        f"**Totals.** {agg['soft_hyphens']} soft hyphen(s); {agg['nbsp']} nbsp; "
        f"{agg['range_en_dashes']} range en dash(es).",
        "",
        "## Gaps by file",
        "",
    ]
    def severity(f: dict) -> int:
        return -(
            len(f["orphan_tables"])
            + len(f["orphan_figures"])
            + len(f["dangling_refs"])
            + len(f["duplicate_h1"])
        )

    for f in sorted(findings, key=severity):
        n = -severity(f)
        lines.append(f"### `{f['file']}`")
        lines.append("")
        lines.append(f"extractor: **{f['extractor']}** — {n} issue(s)")
        lines.append("")
        for o in f["orphan_tables"]:
            lines.append(f"- L{o['line']} **ORPHANED TABLE** — {o['caption']}")
        for o in f["orphan_figures"]:
            lines.append(f"- L{o['line']} **ORPHANED FIGURE** — {o['caption']}")
        for o in f["duplicate_h1"]:
            lines.append(f"- L{o['line']} **DUPLICATE H1** — {o['heading']}")
        for o in f["dangling_refs"][:20]:
            lines.append(f"- L{o['line']} **DANGLING REF** — {o['target']}")
        if len(f["dangling_refs"]) > 20:
            lines.append(f"- ... and {len(f['dangling_refs']) - 20} more dangling ref(s)")
        if f["unconverted_html_tables"]:
            lines.append(
                f"- unconverted raw `<table>` at line(s): {', '.join(map(str, f['unconverted_html_tables']))}"
            )
        if f["unconverted_html_imgs"]:
            lines.append(
                f"- unconverted raw `<img>` at line(s): {', '.join(map(str, f['unconverted_html_imgs']))}"
            )
        if f["characters"]:
            detail = ", ".join(
                f"{v} {cls.replace('_', ' ')}" for cls, v in f["characters"].items()
            )
            lines.append(f"- **CHARACTER HYGIENE** — {detail}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--product", default="comstock")
    ap.add_argument("--release", default="2025-3")
    args = ap.parse_args()

    processed = REPO / "processed" / args.product / args.release
    manifest = json.loads((processed / "manifest.json").read_text(encoding="utf-8"))
    kinds = classify_sources(manifest)

    findings, totals = audit(processed, kinds)

    out_md = REPO / "md_fidelity_report.md"
    out_json = REPO / "md_fidelity_report.json"
    write_report(out_md, findings, totals, args.product, args.release)
    out_json.write_text(
        json.dumps(
            {"product": args.product, "release": args.release, "totals": totals, "findings": findings},
            indent=2,
        ),
        encoding="utf-8",
        newline="\n",
    )

    print(
        f"{'extractor':<12}{'files':>6}{'tblCap':>8}{'orphan':>8}{'figCap':>8}{'orphan':>8}"
        f"{'mdTbl':>7}{'imgs':>7}{'dangle':>8}{'dupH1':>7}{'<table>':>9}"
    )
    print("-" * 87)
    for kind, t in totals.items():
        print(
            f"{kind:<12}{t['files']:>6}{t['table_captions']:>8}{t['orphan_tables']:>8}"
            f"{t['figure_captions']:>8}{t['orphan_figures']:>8}{t['md_tables']:>7}"
            f"{t['md_images'] + t['html_imgs']:>7}{t['dangling_refs']:>8}"
            f"{t['duplicate_h1']:>7}{t['html_tables']:>9}"
        )
    print(
        f"\n{'extractor':<12}{'files':>6}{'softHyp':>9}{'nbsp':>7}{'rangeEn':>9}"
    )
    print("-" * 43)
    for kind, t in totals.items():
        print(
            f"{kind:<12}{t['files']:>6}{t['soft_hyphens']:>9}{t['nbsp']:>7}"
            f"{t['range_en_dashes']:>9}"
        )

    print(f"\nfiles with gaps: {len(findings)}")
    print(f"wrote {out_md.relative_to(REPO)}")
    print(f"wrote {out_json.relative_to(REPO)}")


if __name__ == "__main__":
    main()
