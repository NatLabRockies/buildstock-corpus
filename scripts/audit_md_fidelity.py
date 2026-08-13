"""Audit the .md generator's fidelity on tables and figures.

The extractors keep a `Table N.` / `Figure N.` caption line even when the thing the
caption describes never made it into the markdown. That is the failure mode worth
finding: the surrounding prose still says "as shown in Table 5", so a reader (or an
LLM) is promised a table that isn't there and has to either hallucinate it or give up.

For every processed .md file this script pairs each caption against nearby evidence
that the artifact actually converted:

  table caption   satisfied by a markdown table block, or a raw <table> (unconverted)
  figure caption  satisfied by a markdown image ![...], a raw <img>, or a fenced code
                  block (some "figures" are listings, e.g. an EnergyPlus object)

A caption with no evidence in its window is reported as ORPHANED — the content is gone.

Image references are also resolved against the filesystem: a ref pointing at a file that
was never copied into processed/ is reported as DANGLING. Raw <table>/<img> HTML that
survived is reported as UNCONVERTED — it still carries the content, but it is not clean
markdown. (In the LaTeX reference the <table>s use rowspan/colspan, which GFM pipe tables
cannot express, so those are expected to remain HTML.)

Duplicated H1 headings are reported too: the write step injects `# {title}` above a body
that may already start with the same heading.

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

WINDOW = 10  # lines either side of a caption to look for its artifact


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


def near(target: set[int], line_no: int, window: int = WINDOW) -> bool:
    return any(abs(t - line_no) <= window for t in target)


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
        }
    )

    for path in sorted(processed.rglob("*.md")):
        rel = path.relative_to(processed).as_posix()
        kind = kinds.get(rel, "unknown")
        lines = path.read_text(encoding="utf-8").split("\n")

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

        in_toc = toc_lines(lines)
        orphan_t: list[dict] = []
        orphan_f: list[dict] = []
        for i, line in enumerate(lines):
            m = CAPTION.match(line)
            if not m or i in in_toc:
                continue
            label = f"{m.group(1).title()} {m.group(2)}"
            caption = " ".join(line.split())[:130]
            if m.group(1).lower().startswith("t"):
                t["table_captions"] += 1
                if not (near(tbl, i) or near(html_tbl, i)):
                    t["orphan_tables"] += 1
                    orphan_t.append({"line": i + 1, "label": label, "caption": caption})
            else:
                t["figure_captions"] += 1
                if not (near(img, i) or near(html_img, i) or near(fence, i)):
                    t["orphan_figures"] += 1
                    orphan_f.append({"line": i + 1, "label": label, "caption": caption})

        if orphan_t or orphan_f or dangling or dup_h1 or html_tbl:
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
    print(f"\nfiles with gaps: {len(findings)}")
    print(f"wrote {out_md.relative_to(REPO)}")
    print(f"wrote {out_json.relative_to(REPO)}")


if __name__ == "__main__":
    main()
