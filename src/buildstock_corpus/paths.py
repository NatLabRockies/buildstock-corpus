"""Filesystem layout for the corpus pipeline.

Everything is addressed by (product, release) so artifacts stay release-tagged
end to end. The project root is resolved from this file's location, so the CLI
works regardless of the caller's working directory.
"""

from __future__ import annotations

from pathlib import Path

# src/buildstock_corpus/paths.py -> project root is three parents up.
PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DIR = PROJECT_ROOT / "raw"
PROCESSED_DIR = PROJECT_ROOT / "processed"
INDEX_DIR = PROJECT_ROOT / "index"
SOURCES_DIR = PROJECT_ROOT / "sources"


def raw_root(product: str, release: str) -> Path:
    return RAW_DIR / product / release


def processed_root(product: str, release: str) -> Path:
    return PROCESSED_DIR / product / release


def index_root(product: str, release: str) -> Path:
    # Chroma dislikes ':' and other separators; keep the dir name filesystem-safe.
    return INDEX_DIR / f"{product}-{release}"


def sources_file(product: str, release: str) -> Path:
    return SOURCES_DIR / f"{product}_{release}.yaml"


def manifest_file(product: str, release: str) -> Path:
    return processed_root(product, release) / "manifest.json"


def chunks_file(product: str, release: str) -> Path:
    return processed_root(product, release) / "chunks.jsonl"


def remap_dir(rel: str, remap: dict[str, str] | None = None) -> str:
    """Rewrite the leading directory of a source-relative path per `output_remap`.

    Output normally mirrors the repo-relative source path, which keeps the relative
    image/link refs inside each page resolvable. A source may remap a leading directory
    when the corpus must not reuse upstream's name for it (see `output_remap` in the
    source registry): given {"docs/x": "unpublished_docs/x"}, "docs/x/page.md" becomes
    "unpublished_docs/x/page.md".

    Matching is on whole path segments, so "docs/x_notes/" never matches "docs/x". When
    several prefixes match, the longest (most specific) one wins. Paths outside every
    remapped directory are returned unchanged.
    """
    if not remap:
        return rel
    for key in sorted(remap, key=len, reverse=True):
        src_dir = key.strip("/")
        if rel == src_dir or rel.startswith(f"{src_dir}/"):
            return remap[key].strip("/") + rel[len(src_dir):]
    return rel


def output_rel(source_id: str, source_path: str, remap: dict[str, str] | None = None) -> str:
    """processed/-relative output path for one document: <source_id>/<source_path>.md."""
    rel = Path(source_path).with_suffix(".md").as_posix()
    return f"{source_id}/{remap_dir(rel, remap)}"
