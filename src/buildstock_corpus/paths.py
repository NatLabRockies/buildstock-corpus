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
