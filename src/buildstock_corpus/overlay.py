"""Sidecar overlays — hand-authored content that no extractor can recover from the source.

Some upstream documents carry their dense tables as pixels rather than text. The extracted
markdown keeps the `Table N.` caption but not the numbers, so they survive only inside a
picture: invisible to retrieval, while the surrounding prose keeps cross-referencing the
table. No extractor change fixes that — the text is not in the input.

An overlay is a YAML sidecar (see paths.overlay_file) holding a markdown transcription of
each such table, keyed by caption label and pinned to the sha256 of whatever it was read
from. `apply_overlays()` injects them into Document.body during the build, before the
processed .md files and chunks.jsonl are written, so both the readable artifact and the
retrieval path get the table.

There are two anchor modes, because the same loss shows up in two shapes:

  * **image-anchored** (`source_image` + `source_image_sha256`) — the extractor emitted an
    `![](media/*.png)` ref for the table. The transcription *replaces* that ref, and pins
    the bitmap's hash. This is the measure-markdown case.
  * **caption-anchored** (`source_pdf` + `source_pdf_sha256` + `page`) — nothing at all
    followed the caption. In the measure PDFs these tables are rasterized regions whose
    text layer is empty, and with OCR disabled docling emits neither a table nor a picture,
    so there is no ref to replace. The transcription is *inserted* below the caption and
    pins the source PDF's own hash — the same sha256 fetch recorded and the manifest stores
    as the artifact's `input_sha256`, so `bsc validate` can re-verify it from a fresh clone
    where raw/ (gitignored) is absent.

A caption-anchored entry may additionally carry `replaces:`, which supersedes a table the
extractor *did* emit but got wrong. The gap and the error are different failures and want
different remedies: a missing table is closed by adding text, whereas a wrong table has to
be taken out, or the artifact ends up holding two contradictory copies of the same numbers.
The case that forced this is 96598, where docling shifted a page's reading order by one
caption — every grid landed under the *next* table's caption — and dropped the Roof/Wall
Type column that the captions name. The numbers were all present and all mislabelled, which
is worse than absent: a retrieval hit reads confidently off the wrong row.

Because this is the one place hand-authored text overrides extracted text, it is pinned from
both ends. `replaces.table_sha256` is the fingerprint of the extracted table being removed
(see _table_fingerprint), so if a later docling emits anything different — including a
correct table — the fingerprint stops matching and the build says so instead of silently
discarding better output. `replaces.why` is required, and lands in the artifact next to the
transcription, so the reason is reviewable where the consequence is visible.

`text_repairs:` is the same bargain for a single line of non-table text: an exact-match
find/replace, also with a required `why`. It exists for extractor artifacts that corrupt
document *structure* rather than content — in 96598 a one-line source note ("Data from
[11], [23]") was promoted to an H2, which silently refiled 30 chunks of section 3.2.4 under
a section named after a citation. It is not for editing prose, and a `find` that does not
match exactly once is refused.

Two governance rules shape this module:

  * Hand-authored text is never mistaken for extracted text. Each injection leaves an HTML
    comment naming what it was transcribed from and the method, and the manifest records the
    overlay file's hash next to the artifact it patched. A replacement or a repair says so in
    that comment too, because "this supplements the extractor" and "this overrules the
    extractor" are claims a reviewer has to be able to tell apart.
  * A transcription is only trustworthy for the thing it was made from. Every entry pins a
    hash; if upstream repoints the picture or ships a new PDF the hash stops matching and
    the build reports it instead of shipping a stale table.

Nothing here raises on bad input. A malformed or stale overlay degrades to a warning and
leaves the body untouched, matching how load_pdf_docs reports docling failures — a build
should surface the problem, not abort a 118-document run over one sidecar.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import yaml

# The same splitter the chunker uses, so the size check below measures exactly what
# chunk._pack will treat as an unbreakable unit — not an approximation of it.
from .chunk import _paragraphs
from .normalize import Document
from .paths import OVERLAYS_DIR, overlay_file

# Line-anchored so prose mentions ("as shown in Table 5") never match — same semantics as
# CAPTION in scripts/audit_md_fidelity.py, which is what verifies this work landed.
# Leading bold/italic markers are allowed because pandoc and docling both emit them.
_CAPTION = re.compile(
    r"^\s*(?:\*\*|__|\*|_)?\s*(Table|Figure|Fig\.?)\s*([0-9]+[A-Za-z]?)\s*[.:)]",
    re.IGNORECASE,
)
_MD_IMAGE_TARGET = re.compile(r"!\[[^\]]*\]\(\s*([^)\s]+)")
_MD_TABLE_DELIM = re.compile(r"^\s*\|[\s:|\-]+\|\s*$")
_MD_HEADING = re.compile(r"^#{1,6}\s+\S")
# A table's own printed title, which docling emits between the caption and the table — e.g.
# "**TABLE 6.5.1.1.3A High-Limit Shutoff Control Options...**". It matches _CAPTION but is not
# the next caption, and multi-level numbering is what separates the two. Same regex and same
# reason as SUBNUMBERED in scripts/audit_md_fidelity.py, which verifies this work landed.
_SUBNUMBERED = re.compile(
    r"^\s*(?:\*\*|__|\*|_)?\s*(?:Table|Figure|Fig\.?)\s*[0-9]+(?:\.[0-9]+)+", re.IGNORECASE
)

_MD_TABLE_LINE = re.compile(r"^\s*\|")

_MARKER = "<!-- table recovered from"  # our own injection, for idempotency
_REPAIR_MARKER = "<!-- text repaired by overlay:"

# How far below a caption to look for the image it labels. The observed shape is caption,
# blank, image — a small window keeps us from stealing the next section's figure.
_IMAGE_WINDOW = 5

# chunk.chunk_document packs to max_chars=1400; a *paragraph* larger than that gets
# hard-split mid-row, stranding the data from its header. Blank-line-separated sub-tables
# each stay intact however long the group runs in total, so overlays decompose wide tables
# rather than flattening them — and anything still over the limit gets flagged.
_CHUNK_MAX_CHARS = 1400


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def _label(kind: str, number: str) -> str:
    """Normalize a caption label so 'Fig. 3', 'FIGURE 3' and 'Figure 3' all compare equal."""
    kind = "Figure" if kind.lower().startswith("f") else "Table"
    return f"{kind} {number.upper()}"


def _find_caption(lines: list[str], label: str) -> int | None:
    want = label.strip()
    m = _CAPTION.match(want if want.endswith((".", ":", ")")) else want + ".")
    want_norm = _label(m.group(1), m.group(2)) if m else want
    for i, line in enumerate(lines):
        m = _CAPTION.match(line)
        if m and _label(m.group(1), m.group(2)) == want_norm:
            return i
    return None


def _locate_image(image_dir: Path, target: str) -> Path | None:
    """Resolve an image ref against the directory that document's refs come from.

    Two layouts have to work. A clone-sourced page keeps its bitmaps in a subdirectory
    (`media/x.png`) so the ref resolves as written. A PDF's bitmaps come from the docling
    cache, which is flat: the body says `86103_images/x.png`, but during the build that
    directory does not exist yet — the images are still sitting under their own names in the
    cache. So fall back to the basename, which is what _find_image already matched on.
    """
    for cand in (image_dir / target, image_dir / Path(target).name):
        if cand.is_file():
            return cand
    return None


def _find_image(lines: list[str], start: int, source_image: str) -> tuple[int, str] | None:
    """Locate the image ref below a caption, matching on basename.

    Basename rather than full target because the same page mixes `media/x.png` and
    `./media/x.png` spellings for the same file.
    """
    want = Path(source_image).name
    for i in range(start + 1, min(start + 1 + _IMAGE_WINDOW, len(lines))):
        for m in _MD_IMAGE_TARGET.finditer(lines[i]):
            if Path(m.group(1)).name == want:
                return i, m.group(1)
    return None


def _has_table_below(lines: list[str], start: int) -> bool:
    """Whether a real markdown table (confirmed by its delimiter row) already labels `start`.

    Directional and bounded by the next caption or heading, for the same reason
    scripts/audit_md_fidelity.py binds captions directionally: where captions are dense, a plain
    proximity window reaches past the next caption into the table that belongs to *it*. In
    96598.md the Table 10 caption is followed by a citation stub, then the Table 11 caption, then
    Table 11's table four lines further down — close enough for an undirected window to read
    Table 10 as already recovered and refuse its overlay as redundant.

    A sub-numbered bold line is the table's own printed title, not the next caption, so it does
    not stop the scan; otherwise 89128-shaped documents would look table-less and get a second,
    duplicate injection.
    """
    for line in lines[start + 1 : start + 1 + _IMAGE_WINDOW + 3]:
        if _MD_TABLE_DELIM.match(line):
            return True
        if _MD_HEADING.match(line) or (_CAPTION.match(line) and not _SUBNUMBERED.match(line)):
            return False
    return False


def _table_blocks(lines: list[str]) -> list[tuple[int, int]]:
    """Half-open [start, end) spans of every contiguous run of markdown table lines."""
    blocks: list[tuple[int, int]] = []
    i = 0
    while i < len(lines):
        if _MD_TABLE_LINE.match(lines[i]):
            j = i
            while j < len(lines) and _MD_TABLE_LINE.match(lines[j]):
                j += 1
            blocks.append((i, j))
            i = j
        else:
            i += 1
    return blocks


def _table_fingerprint(block: list[str]) -> str:
    """sha256 of a table's *values* — column padding and delimiter width normalized away.

    A pin has to be stable against everything that is not a change in content, or it turns
    into a tripwire that fires on reformatting and trains readers to re-pin without looking.
    Cells are stripped and the delimiter row is flattened to one dash per column, so what the
    hash actually commits to is: this many columns, these cell texts, in this order. A dropped
    column, a merged row or a shifted value all change it, which is exactly the set of
    extractor changes a replacement entry must not survive.
    """
    norm = []
    for line in block:
        cells = line.strip().strip("|").split("|")
        if _MD_TABLE_DELIM.match(line):
            norm.append("|".join("-" for _ in cells))
        else:
            norm.append("|".join(c.strip() for c in cells))
    return hashlib.sha256("\n".join(norm).encode("utf-8")).hexdigest()


def _remove_block(lines: list[str], start: int, end: int) -> None:
    """Delete [start, end) and the blank line the deletion would otherwise double up."""
    del lines[start:end]
    if 0 < start < len(lines) and not lines[start - 1].strip() and not lines[start].strip():
        del lines[start]


def entry_kind(entry: dict) -> str:
    """Which anchor mode this entry uses: 'image', 'pdf', or 'unknown' (see module docstring).

    Public because manifest._validate_overlay re-verifies these pins at `bsc validate` time
    and has to check the same field per kind that the build did.
    """
    if entry.get("source_image"):
        return "image"
    if entry.get("source_pdf") or entry.get("source_pdf_sha256"):
        return "pdf"
    return "unknown"


def _origin(entry: dict) -> str:
    """Human-readable description of what a transcription was read from."""
    if entry_kind(entry) == "image":
        return str(entry["source_image"])
    page = entry.get("page")
    return f"{entry.get('source_pdf')} p.{page}" if page else str(entry.get("source_pdf"))


def _comment_lines(text: str, indent: str) -> list[str]:
    """A free-text field as comment body lines, indented and stripped of blanks."""
    return [f"{indent}{ln.strip()}" for ln in str(text).strip().split("\n") if ln.strip()]


def _injection(entry: dict, overlay_rel: str, replaced_sha: str | None = None) -> str:
    """The injected block: provenance comment, then the transcribed table.

    `replaced_sha` is set when this entry superseded an extracted table, and turns the comment
    from "here is text the extractor could not reach" into "here is text that overruled the
    extractor, and this is why" — a stronger claim, so it is stated where it applies rather
    than only in the sidecar a reader may never open.
    """
    markdown = entry["markdown"].strip("\n")
    method = entry.get("method", "unspecified")
    head = [
        f"{_MARKER} {_origin(entry)}",
        f"     overlay: {overlay_rel}",
        f"     method: {method}",
    ]
    if replaced_sha:
        head.append(f"     supersedes the extractor's own table here (values {replaced_sha[:12]}…):")
        head += _comment_lines((entry.get("replaces") or {}).get("why", ""), "       ")
    return "\n".join(head) + " -->\n\n" + markdown


def _resolve_image_anchor(
    lines: list[str], i: int, entry: dict, image_dir: Path | None, out: list[str]
) -> int | None:
    """Line index of the verified image ref below caption line `i`, or None (reason -> `out`)."""
    found = _find_image(lines, i, str(entry["source_image"]))
    if found is None:
        # No ref to replace. If a real table is there now the overlay has been superseded;
        # otherwise the pinned picture has moved or gone.
        out.append(
            "caption already has a markdown table and no matching image ref; the extractor "
            "may now handle this table, so the overlay is redundant"
            if _has_table_below(lines, i)
            else f"no image ref matching {Path(str(entry['source_image'])).name} within "
            f"{_IMAGE_WINDOW} lines of the caption"
        )
        return None
    j, target = found

    expect = entry.get("source_image_sha256")
    if not expect:
        out.append("overlay entry has no source_image_sha256 to verify against")
        return None
    if image_dir is None:
        out.append("source image root unknown; cannot verify source_image_sha256")
        return None
    img = _locate_image(image_dir, target)
    if img is None:
        out.append(f"source image not found at {image_dir / target}")
        return None
    actual = _sha256_file(img)
    if actual != expect:
        out.append(
            f"source image changed since transcription ({target}: recorded "
            f"{expect[:12]}…, on disk {actual[:12]}…); transcription may be stale"
        )
        return None
    return j


def _resolve_replacement(
    lines: list[str], i: int, replaces: dict, out: list[str]
) -> tuple[int, int] | None:
    """Span of the extracted table this entry supersedes, or None (reason -> `out`).

    Located by fingerprint rather than by position, because position is the thing that is
    wrong: in 96598 the grid belonging to a caption is not below it. The fingerprint has to
    match exactly one table in the document — zero means the extracted body changed and the
    replacement must not be applied blind, more than one means the pin does not identify a
    single table and could remove the wrong one.
    """
    for field in ("table_sha256", "why"):
        if not replaces.get(field):
            out.append(f"overlay entry's 'replaces' is missing required field '{field}'")
            return None
    if "-->" in str(replaces["why"]):
        out.append("'replaces.why' contains '-->', which would truncate the provenance comment")
        return None

    want = str(replaces["table_sha256"]).strip().lower()
    hits = [(s, e) for s, e in _table_blocks(lines) if _table_fingerprint(lines[s:e]) == want]
    if len(hits) == 1:
        return hits[0]
    if not hits:
        # Two very different situations, and the difference decides what a maintainer does next.
        out.append(
            f"no extracted table matches the pinned fingerprint {want[:12]}…, and this caption "
            f"now has a table of its own; the extractor may have fixed this, so re-check the "
            f"output before re-pinning"
            if _has_table_below(lines, i)
            else f"no extracted table matches the pinned fingerprint {want[:12]}…; the extracted "
            f"body changed, so the table to supersede cannot be identified"
        )
    else:
        out.append(
            f"pinned fingerprint {want[:12]}… matches {len(hits)} extracted tables; it does not "
            f"identify one table, so nothing was replaced"
        )
    return None


def _insert_below_caption(lines: list[str], i: int, block: str) -> None:
    """Insert `block` as its own paragraph after caption line `i`.

    The extractor usually already leaves a blank line under the caption; reuse it rather than
    adding a second one, so the caption and its table read as one unit.
    """
    if i + 1 < len(lines) and not lines[i + 1].strip():
        lines.insert(i + 2, f"{block}\n")
    else:
        lines.insert(i + 1, f"\n{block}\n")


def _apply_entry(
    lines: list[str],
    entry: dict,
    image_dir: Path | None,
    overlay_rel: str,
    where: str,
    input_sha: str | None = None,
) -> tuple[bool, list[str]]:
    """Inject one table entry into `lines` in place. Returns (applied, warnings).

    `input_sha` is the sha256 of the input file this document was extracted from, used to
    verify a caption-anchored entry's `source_pdf_sha256`. Comparing against the hash fetch
    recorded (rather than re-hashing the PDF) is both cheaper and what `bsc validate` can
    repeat from a fresh clone, where raw/ is absent.
    """
    label = str(entry.get("label", "")).strip()
    warn = lambda msg: [f"{where}: {label or '<no label>'}: {msg}"]  # noqa: E731

    kind = entry_kind(entry)
    if kind == "unknown":
        return False, warn(
            "overlay entry names neither 'source_image' nor 'source_pdf'; cannot tell what "
            "it was transcribed from"
        )
    required = ("label", "markdown") + (
        ("source_image",) if kind == "image" else ("source_pdf", "source_pdf_sha256", "page")
    )
    for field in required:
        if not entry.get(field):
            return False, warn(f"overlay entry missing required field '{field}'")

    i = _find_caption(lines, label)
    if i is None:
        return False, warn("caption not found in the extracted body; overlay is stale")

    if any(_MARKER in line for line in lines[i + 1 : i + 4 + _IMAGE_WINDOW]):
        return False, []  # already injected — idempotent, not a problem

    if kind == "image":
        reasons: list[str] = []
        j = _resolve_image_anchor(lines, i, entry, image_dir, reasons)
        if j is None:
            return False, warn(reasons[0])
        lines[j] = _injection(entry, overlay_rel)
    else:
        replaces = entry.get("replaces") or {}
        # A replacement's anchor is the pinned fingerprint, not "is this caption bare", so the
        # redundancy check is skipped for it: the caption having a table is the premise here,
        # not a reason to back off. Correctness comes from the fingerprint instead.
        if not replaces and _has_table_below(lines, i):
            return False, warn(
                "caption already has a markdown table; the extractor may now handle this "
                "table, so the overlay is redundant"
            )
        expect = str(entry["source_pdf_sha256"])
        if input_sha is None:
            return False, warn(
                "source input hash unknown for this document; cannot verify source_pdf_sha256"
            )
        if expect != input_sha:
            return False, warn(
                f"source PDF changed since transcription (recorded {expect[:12]}…, build "
                f"input {input_sha[:12]}…); transcription may be stale"
            )
        replaced_sha = None
        if replaces:
            reasons = []
            span = _resolve_replacement(lines, i, replaces, reasons)
            if span is None:
                return False, warn(reasons[0])
            replaced_sha = str(replaces["table_sha256"]).lower()
            _remove_block(lines, *span)
            # Re-find rather than adjust: the removed block can sit either side of the caption,
            # and sequential entries each shift what follows. Re-finding cannot drift.
            i = _find_caption(lines, label)
            if i is None:  # unreachable — removal only deletes table lines
                return False, warn("caption vanished while replacing the extracted table")
        _insert_below_caption(lines, i, _injection(entry, overlay_rel, replaced_sha))

    # chunk._pack splits on blank lines, so what matters is the largest single paragraph,
    # not the size of the whole injected block: a table decomposed into blank-line-separated
    # sub-tables survives intact however long the group runs in total.
    longest = max((len(p) for p in _paragraphs(str(entry["markdown"]).split("\n"))), default=0)
    if longest > _CHUNK_MAX_CHARS:
        return True, warn(
            f"largest table paragraph is {longest} chars, over the {_CHUNK_MAX_CHARS}-char "
            f"chunk limit; decompose it into sub-tables or it will be split mid-row"
        )
    return True, []


def _repaired_above(lines: list[str], n: int) -> bool:
    """Whether line `n` is the replacement text of an already-applied repair.

    Walks the comment block immediately above `n` rather than scanning a fixed window, so a
    long multi-line `why` cannot push the marker out of range and make an applied repair look
    unapplied — which would re-warn on every build about work that already landed.
    """
    k = n - 1
    while k >= 0 and not lines[k].strip():
        k -= 1
    if k < 0 or not lines[k].rstrip().endswith("-->"):
        return False
    while k >= 0 and "<!--" not in lines[k]:
        k -= 1
    return k >= 0 and lines[k].lstrip().startswith(_REPAIR_MARKER)


def _apply_repair(lines: list[str], repair: dict, overlay_rel: str) -> tuple[bool, list[str]]:
    """Apply one exact-match text repair in place. Returns (applied, warnings).

    Whole-line matching, and the match must be unique. A substring find/replace over a
    100-page document is a blunt instrument — `find: "Data from [11], [23]"` would also hit
    the three legitimate copies of that note elsewhere in 96598 — so the pin is the whole line
    and the uniqueness requirement is what makes it a pin rather than a sweep.
    """
    where = f"{overlay_rel}: text_repairs"
    find = str(repair.get("find", ""))
    warn = lambda msg: [f"{where}: {find[:60]!r}: {msg}"]  # noqa: E731

    for field in ("find", "replace", "why"):
        if not str(repair.get(field, "")).strip():
            return False, [f"{where}: repair is missing required field '{field}'"]
    replace = str(repair["replace"])
    if "-->" in str(repair["why"]):
        return False, warn("'why' contains '-->', which would truncate the provenance comment")

    hits = [n for n, line in enumerate(lines) if line.strip() == find.strip()]
    if len(hits) != 1:
        already = any(
            line.strip() == replace.strip() and _repaired_above(lines, n)
            for n, line in enumerate(lines)
        )
        if not hits and already:
            return False, []  # already repaired — idempotent, not a problem
        return False, warn(
            f"matches {len(hits)} lines in the extracted body; a repair must identify exactly "
            f"one line, so nothing was changed"
        )

    n = hits[0]
    comment = "\n".join(
        [f"{_REPAIR_MARKER} {overlay_rel}", *_comment_lines(repair["why"], "     ")]
    )
    indent = lines[n][: len(lines[n]) - len(lines[n].lstrip())]
    lines[n] = f"{comment} -->\n\n{indent}{replace.strip()}"
    return True, []


def apply_overlays(
    docs: list[Document],
    product: str,
    release: str,
    image_dirs: dict[tuple[str, str], Path] | None = None,
    input_shas: dict[str, dict[str, str]] | None = None,
) -> tuple[dict[str, dict], list[str]]:
    """Inject every overlay that matches a document in `docs`.

    `image_dirs` maps (source_id, source_path) -> the directory that document's image refs
    resolve against, so a pinned bitmap can be hashed from wherever it actually lives at
    build time. The caller owns that layout question, which differs by source type: a
    clone-sourced page's images sit beside it in the clone, a PDF's under the docling cache.

    `input_shas` maps source_id -> source_path -> sha256 of the input file, taken from the
    same fetch state the manifest's `input_sha256` comes from. Caption-anchored entries are
    verified against it (see _apply_entry).

    Returns ({source_id: {source_path: {...record...}}}, warnings). The record is what the
    manifest stores next to the artifact: the overlay's path, its hash, and the labels
    actually applied.
    """
    image_dirs = image_dirs or {}
    input_shas = input_shas or {}
    applied: dict[str, dict] = {}
    warnings: list[str] = []

    for doc in docs:
        path = overlay_file(product, release, doc.source_id, doc.source_path)
        if not path.is_file():
            continue
        overlay_rel = path.relative_to(OVERLAYS_DIR).as_posix()

        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            warnings.append(f"{overlay_rel}: unreadable overlay: {str(exc)[:200]}")
            continue

        for field, expect in (("product", product), ("release", release)):
            if str(data.get(field, expect)) != expect:
                warnings.append(
                    f"{overlay_rel}: overlay is tagged {field}={data.get(field)!r}, "
                    f"but this build is {expect!r}; skipped"
                )
                break
        else:
            entries = data.get("tables") or []
            repairs = data.get("text_repairs") or []
            if not entries and not repairs:
                warnings.append(f"{overlay_rel}: overlay has no table entries or text repairs")
                continue

            image_dir = image_dirs.get((doc.source_id, doc.source_path))
            input_sha = input_shas.get(doc.source_id, {}).get(doc.source_path)

            lines = doc.body.split("\n")
            # Repairs run first: they fix document structure (a note mis-parsed as a heading),
            # and the table entries below are located relative to headings and captions.
            n_repairs = 0
            for repair in repairs:
                ok, warns = _apply_repair(lines, repair, overlay_rel)
                warnings += warns
                n_repairs += ok

            labels: list[str] = []
            for entry in entries:
                ok, warns = _apply_entry(
                    lines, entry, image_dir, overlay_rel, overlay_rel, input_sha
                )
                warnings += warns
                if ok:
                    labels.append(str(entry["label"]).strip())
            if labels or n_repairs:
                doc.body = "\n".join(lines)
                record = {
                    "path": overlay_rel,
                    "sha256": _sha256_file(path),
                    "tables_applied": labels,
                }
                if n_repairs:
                    # Recorded so a reader of the manifest can see this artifact carries a
                    # hand-authored correction to extracted text, not only additions to it.
                    record["text_repairs_applied"] = n_repairs
                applied.setdefault(doc.source_id, {})[doc.source_path] = record

    return applied, warnings
