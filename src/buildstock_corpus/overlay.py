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

Two governance rules shape this module:

  * Hand-authored text is never mistaken for extracted text. Each injection leaves an HTML
    comment naming what it was transcribed from and the method, and the manifest records the
    overlay file's hash next to the artifact it patched.
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

_MARKER = "<!-- table recovered from"  # our own injection, for idempotency

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


def _injection(entry: dict, overlay_rel: str) -> str:
    """The injected block: provenance comment, then the transcribed table."""
    markdown = entry["markdown"].strip("\n")
    method = entry.get("method", "unspecified")
    return (
        f"{_MARKER} {_origin(entry)}\n"
        f"     overlay: {overlay_rel}\n"
        f"     method: {method} -->\n"
        f"\n"
        f"{markdown}"
    )


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
        if _has_table_below(lines, i):
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
        _insert_below_caption(lines, i, _injection(entry, overlay_rel))

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
            if not entries:
                warnings.append(f"{overlay_rel}: overlay has no table entries")
                continue

            image_dir = image_dirs.get((doc.source_id, doc.source_path))
            input_sha = input_shas.get(doc.source_id, {}).get(doc.source_path)

            lines = doc.body.split("\n")
            labels: list[str] = []
            for entry in entries:
                ok, warns = _apply_entry(
                    lines, entry, image_dir, overlay_rel, overlay_rel, input_sha
                )
                warnings += warns
                if ok:
                    labels.append(str(entry["label"]).strip())
            if labels:
                doc.body = "\n".join(lines)
                applied.setdefault(doc.source_id, {})[doc.source_path] = {
                    "path": overlay_rel,
                    "sha256": _sha256_file(path),
                    "tables_applied": labels,
                }

    return applied, warnings
