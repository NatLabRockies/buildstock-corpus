"""Sidecar overlays — hand-authored content that no extractor can recover from the source.

Some upstream measure pages embed their dense tables as bitmaps. The extracted markdown
keeps the `Table N.` caption and an `![](media/*.png)` link, so the numbers survive only
inside the picture: invisible to retrieval, while the surrounding prose keeps
cross-referencing the table. No extractor change fixes that — the text is not in the input.

An overlay is a YAML sidecar (see paths.overlay_file) holding a markdown transcription of
each such table, keyed by caption label and pinned to the sha256 of the image it was read
from. `apply_overlays()` injects them into Document.body during the build, before the
processed .md files and chunks.jsonl are written, so both the readable artifact and the
retrieval path get the table.

Two governance rules shape this module:

  * Hand-authored text is never mistaken for extracted text. Each injection leaves an HTML
    comment naming the source image and the method, and the manifest records the overlay
    file's hash next to the artifact it patched.
  * A transcription is only trustworthy for the image it was made from. Every entry pins
    `source_image_sha256`; if upstream repoints or redraws the picture the hash stops
    matching and the build reports it instead of shipping a stale table.

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
    """A real markdown table (confirmed by its delimiter row) already sits below `start`."""
    window = lines[start + 1 : start + 1 + _IMAGE_WINDOW + 3]
    return any(_MD_TABLE_DELIM.match(line) for line in window)


def _injection(entry: dict, overlay_rel: str) -> str:
    """The replacement block: provenance comment, then the transcribed table."""
    markdown = entry["markdown"].strip("\n")
    method = entry.get("method", "unspecified")
    return (
        f"{_MARKER} {entry['source_image']}\n"
        f"     overlay: {overlay_rel}\n"
        f"     method: {method} -->\n"
        f"\n"
        f"{markdown}"
    )


def _apply_entry(
    lines: list[str], entry: dict, image_dir: Path | None, overlay_rel: str, where: str
) -> tuple[bool, list[str]]:
    """Inject one table entry into `lines` in place. Returns (applied, warnings)."""
    label = str(entry.get("label", "")).strip()
    warn = lambda msg: [f"{where}: {label or '<no label>'}: {msg}"]  # noqa: E731

    for field in ("label", "source_image", "markdown"):
        if not entry.get(field):
            return False, warn(f"overlay entry missing required field '{field}'")

    i = _find_caption(lines, label)
    if i is None:
        return False, warn("caption not found in the extracted body; overlay is stale")

    if any(_MARKER in line for line in lines[i + 1 : i + 4 + _IMAGE_WINDOW]):
        return False, []  # already injected — idempotent, not a problem

    found = _find_image(lines, i, str(entry["source_image"]))
    if found is None:
        if _has_table_below(lines, i):
            return False, warn(
                "caption already has a markdown table and no matching image ref; "
                "the extractor may now handle this table, so the overlay is redundant"
            )
        return False, warn(
            f"no image ref matching {Path(str(entry['source_image'])).name} within "
            f"{_IMAGE_WINDOW} lines of the caption"
        )
    j, target = found

    expect = entry.get("source_image_sha256")
    if not expect:
        return False, warn("overlay entry has no source_image_sha256 to verify against")
    if image_dir is None:
        return False, warn("source image root unknown; cannot verify source_image_sha256")
    img = image_dir / target
    if not img.is_file():
        return False, warn(f"source image not found at {img}")
    actual = _sha256_file(img)
    if actual != expect:
        return False, warn(
            f"source image changed since transcription ({target}: recorded "
            f"{expect[:12]}…, on disk {actual[:12]}…); transcription may be stale"
        )

    lines[j] = _injection(entry, overlay_rel)

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
    clone_dirs: dict[str, Path] | None = None,
) -> tuple[dict[str, dict], list[str]]:
    """Inject every overlay that matches a document in `docs`.

    `clone_dirs` maps source_id -> clone directory, so the pinned source images can be
    hashed from the same tree the markdown was extracted from. Image refs are relative to
    the page that carries them, which is how they resolve in processed/ too.

    Returns ({source_id: {source_path: {...record...}}}, warnings). The record is what the
    manifest stores next to the artifact: the overlay's path, its hash, and the labels
    actually applied.
    """
    clone_dirs = clone_dirs or {}
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

            clone = clone_dirs.get(doc.source_id)
            image_dir = (clone / doc.source_path).parent if clone else None

            lines = doc.body.split("\n")
            labels: list[str] = []
            for entry in entries:
                ok, warns = _apply_entry(lines, entry, image_dir, overlay_rel, overlay_rel)
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
