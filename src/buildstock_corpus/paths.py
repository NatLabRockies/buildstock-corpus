"""Filesystem layout for the corpus pipeline.

Everything is addressed by (product, release) so artifacts stay release-tagged
end to end. The project root is resolved from this file's location, so the CLI
works regardless of the caller's working directory.
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path

# src/buildstock_corpus/paths.py -> project root is three parents up.
PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DIR = PROJECT_ROOT / "raw"
PROCESSED_DIR = PROJECT_ROOT / "processed"
INDEX_DIR = PROJECT_ROOT / "index"
SOURCES_DIR = PROJECT_ROOT / "sources"
OVERLAYS_DIR = PROJECT_ROOT / "overlays"

# Sandbox root for derived outputs, set by `--work-dir` (see use_workspace).
_WORKSPACE: Path | None = None


def use_workspace(root: str | Path | None) -> None:
    """Redirect derived outputs (processed/, index/) under `root`, or back to the defaults.

    Inputs and caches — raw/, sources/, .cache/ — are deliberately left alone, so a
    sandbox run reuses the already-fetched sources and the warm docling/fastembed caches
    instead of re-downloading and re-converting. This is what makes a throwaway build
    (`bsc build --sample 1 --work-dir .smoketest`) both cheap and unable to overwrite the
    release-tagged artifacts in processed/.
    """
    global _WORKSPACE
    _WORKSPACE = Path(root).resolve() if root else None


def _derived_base(name: str, default: Path) -> Path:
    """Base dir for a derived output tree, honoring an active workspace override."""
    return (_WORKSPACE / name) if _WORKSPACE else default


def long_path(path: str | Path) -> str:
    """A form of `path` that Win32 will accept even past the 260-character MAX_PATH limit.

    docling names each extracted image `image_NNNNNN_<sha256>.png`, an 81-character
    filename. Copied under processed/<product>/<release>/<source_id>/<upstream dirs>/, a
    few of those land at ~267 characters, and Windows without LongPathsEnabled cannot
    reach them at all: os.stat reports ERROR_PATH_NOT_FOUND for a file that is really
    there, so shutil.rmtree fails to clear a stale output tree and copytree fails to write
    a new one. Prefixing with \\\\?\\ opts that call out of path normalization and the
    limit.

    Returns str, not Path, because pathlib re-normalizes the prefix away. Off Windows this
    is just str(path).
    """
    if os.name != "nt":
        return str(path)
    text = str(Path(path).resolve())
    return text if text.startswith("\\\\?\\") else f"\\\\?\\{text}"


def sha256_file(path: Path) -> str:
    """sha256 of a file's bytes, read in blocks so a large artifact never lands in memory.

    Lives here rather than in manifest.py because two modules that must not import each
    other both need it: manifest.py hashes every artifact it records, and corpus_map.py
    hashes manifest.json to stamp which manifest a map was derived from. manifest.py then
    imports the map's reader to check that stamp, so the dependency runs one way only.
    """
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def raw_root(product: str, release: str) -> Path:
    return RAW_DIR / product / release


def processed_root(product: str, release: str) -> Path:
    return _derived_base("processed", PROCESSED_DIR) / product / release


def index_root(product: str, release: str) -> Path:
    # Chroma dislikes ':' and other separators; keep the dir name filesystem-safe.
    return _derived_base("index", INDEX_DIR) / f"{product}-{release}"


def sources_file(product: str, release: str) -> Path:
    return SOURCES_DIR / f"{product}_{release}.yaml"


def overlay_file(product: str, release: str, source_id: str, source_path: str) -> Path:
    """Sidecar overlay for one document: overlays/<product>_<release>/<source_id>/<path>.yaml.

    Overlays carry content that no extractor can recover from the source — tables the
    upstream document embeds as a bitmap, transcribed by hand. They are *inputs* to the
    build, not derived outputs, so like sources_file() they live at the project root and
    ignore the `--work-dir` sandbox: a sandboxed smoke build should read the same overlays
    as a release build, and must never write to them.

    The <source_id>/<source_path> layout mirrors output_rel(), so an overlay sits at the
    same relative position as the artifact it patches.
    """
    rel = Path(source_path).with_suffix(".yaml").as_posix()
    return OVERLAYS_DIR / f"{product}_{release}" / source_id / rel


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
