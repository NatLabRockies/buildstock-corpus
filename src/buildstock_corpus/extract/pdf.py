"""PDF -> markdown via docling (layout-aware), for the external + local measure docs.

docling is expensive (layout models, seconds per page), so conversions are cached by
content sha256 under .cache/pdf_md/ — rebuilds are then instant and the cache key is
provenance-sound (same bytes -> same markdown). One Document is produced per physical
PDF; when several measures cite the same file (mirror URLs, shared package docs) their
identities are aggregated into that one Document's extra metadata.

The cache stores one directory per PDF (keyed by sha256) containing the markdown and any
images docling extracted from embedded figures. Old single-file caches are detected and
re-converted automatically on the next build.
"""

from __future__ import annotations

import re
import shutil
import tempfile
from dataclasses import dataclass, field
from pathlib import Path, PureWindowsPath

from ..normalize import Document, collapse_blank_lines, first_heading
from ..paths import PROJECT_ROOT

PDF_CACHE = PROJECT_ROOT / ".cache" / "pdf_md"
CACHE_MD_NAME = "document.md"
CACHE_IMG_DIR = "images"
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)  # docling emits <!-- image --> placeholders
_MD_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]*)\)")
_UNSAFE_REF_RE = re.compile(r"[^A-Za-z0-9._-]+")  # chars needing escaping in a link target

_converter = None  # docling DocumentConverter is costly to build; make one and reuse it


@dataclass
class PdfSpec:
    source_path: str  # provenance anchor: raw- or repo-relative path of the PDF
    abs_path: Path  # where the bytes live on disk
    sha256: str  # cache key
    title: str | None = None  # preferred title (measure doc name); falls back to heading/stem
    extra: dict = field(default_factory=dict)  # measure identity folded into chunk metadata


def _get_converter():
    global _converter
    if _converter is None:
        from docling.datamodel.base_models import InputFormat
        from docling.datamodel.pipeline_options import (
            AcceleratorOptions,
            PdfPipelineOptions,
            TableFormerMode,
        )
        from docling.document_converter import DocumentConverter, PdfFormatOption

        # These measure docs are born-digital NREL reports with a real text layer, so OCR
        # (RapidOCR on CPU) is pure cost — it drove conversion to minutes/PDF. Disable it but
        # keep the layout + table-structure models, which are the point of a layout-aware reader.
        # TableFormer FAST (vs ACCURATE) and more CPU threads keep the one-time cache warm to
        # tens of minutes instead of hours; tables still get real structure, just less refinement.
        opts = PdfPipelineOptions()
        opts.do_ocr = False
        opts.do_table_structure = True
        opts.table_structure_options.mode = TableFormerMode.FAST
        opts.table_structure_options.do_cell_matching = True
        opts.accelerator_options = AcceleratorOptions(num_threads=12)
        # Without this docling only emits <!-- image --> placeholders; the figure bitmaps
        # are needed so the "as shown in Figure N" prose isn't left pointing at nothing.
        opts.generate_picture_images = True
        _converter = DocumentConverter(
            format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)}
        )
    return _converter


def _relativize_image_refs(md: str, img_dir: Path) -> str:
    """Rewrite docling's absolute image paths to `images/<file>` refs.

    save_as_markdown emits the artifacts_dir as an absolute path, which would bake this
    machine's temp directory into the cached markdown. Matching on the basename keeps the
    cache portable and independent of where the conversion happened to run.
    """

    def repl(m: re.Match) -> str:
        name = PureWindowsPath(m.group(2)).name  # handles both / and \ separators
        if name and (img_dir / name).is_file():
            return f"![{m.group(1)}]({CACHE_IMG_DIR}/{name})"
        return m.group(0)

    return _MD_IMAGE_RE.sub(repl, md)


def _convert_into(abs_path: Path, dest: Path) -> None:
    """Convert one PDF into dest/document.md plus dest/images/ for embedded figures.

    docling's save_as_markdown writes the image files itself and points the markdown at
    them; the refs are then relativized so the cache stays portable.
    """
    from docling_core.types.doc import ImageRefMode

    result = _get_converter().convert(str(abs_path))
    dest.mkdir(parents=True, exist_ok=True)
    md_path = dest / CACHE_MD_NAME
    result.document.save_as_markdown(
        md_path,
        image_mode=ImageRefMode.REFERENCED,
        artifacts_dir=dest / CACHE_IMG_DIR,
    )
    md = md_path.read_text(encoding="utf-8")
    md_path.write_text(_relativize_image_refs(md, dest / CACHE_IMG_DIR), encoding="utf-8")


def _cache_dir_for(spec: PdfSpec) -> Path:
    """Return the cache directory for this PDF, converting if not already cached.

    Writes to a temp sibling and renames, so an interrupted conversion can't leave a
    half-populated directory that later looks like a valid cache hit.
    """
    cached = PDF_CACHE / spec.sha256
    if (cached / CACHE_MD_NAME).is_file():
        return cached

    # Pre-image-extraction caches were a single <sha256>.md file; drop so we re-convert.
    legacy = PDF_CACHE / f"{spec.sha256}.md"
    if legacy.is_file():
        legacy.unlink()
    if cached.exists():
        shutil.rmtree(cached)

    PDF_CACHE.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(dir=PDF_CACHE, prefix=f".{spec.sha256[:12]}-"))
    try:
        _convert_into(spec.abs_path, staging)
        staging.replace(cached)
    except BaseException:
        shutil.rmtree(staging, ignore_errors=True)
        raise
    return cached


def _image_dir_name(source_path: str) -> str:
    """Per-PDF image directory, as a sibling of the output .md file.

    Namespaced by PDF stem because many PDFs share one output directory and docling's
    image filenames restart at image_000000 for every document. Runs of characters that
    would need escaping in a markdown link target (notably spaces, which several measure
    PDF filenames contain) collapse to underscores so the emitted refs stay parseable.
    """
    return f"{_UNSAFE_REF_RE.sub('_', Path(source_path).stem)}_images"


def load_pdf_docs(
    specs: list[PdfSpec], product: str, release: str, source_id: str
) -> tuple[list[Document], list[str], dict[str, Path]]:
    """Convert each PDF spec into a Document.

    Returns (docs, warnings, image_dirs), where image_dirs maps a path relative to
    processed/<source_id>/ to the cache directory holding that PDF's extracted images.
    """
    docs: list[Document] = []
    warnings: list[str] = []
    image_dirs: dict[str, Path] = {}
    for spec in specs:
        try:
            cache_dir = _cache_dir_for(spec)
            md = (cache_dir / CACHE_MD_NAME).read_text(encoding="utf-8")
        except Exception as exc:  # a bad PDF is a tracked gap, not a fatal build error
            warnings.append(f"{spec.source_path}: docling failed: {str(exc)[:200]}")
            continue

        img_name = _image_dir_name(spec.source_path)
        cache_imgs = cache_dir / CACHE_IMG_DIR
        if cache_imgs.is_dir() and any(cache_imgs.iterdir()):
            rel_dir = (Path(spec.source_path).parent / img_name).as_posix()
            image_dirs[rel_dir] = cache_imgs
            md = md.replace(f"]({CACHE_IMG_DIR}/", f"]({img_name}/")

        body = collapse_blank_lines(_HTML_COMMENT_RE.sub("", md))
        if not body.strip():
            warnings.append(f"{spec.source_path}: empty after conversion")
            continue
        title = spec.title or first_heading(body) or Path(spec.source_path).stem
        docs.append(
            Document(
                product=product,
                release=release,
                source_id=source_id,
                source_type="pdf",
                source_path=spec.source_path,
                title=title,
                body=body,
                extra=dict(spec.extra),
            )
        )
    return docs, warnings, image_dirs
