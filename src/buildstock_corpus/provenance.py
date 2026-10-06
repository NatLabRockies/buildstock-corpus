"""The corpus version and the per-file provenance header that carries it.

A *corpus version* names one build of everything under processed/. It is distinct from the
dataset release id (`comstock_amy2018_2025_release_3`), which names the ComStock data the
corpus documents: a rebuild with a better extractor changes bytes under the same release
path, and the corpus version is what tells those two builds apart.

Release builds are given the tag they will be published under
(`bsc build --corpus-version comstock_amy2018_2025_release_3-v1`), because the value is
written into every artifact and so has to be known before the commit the tag points at
exists. Any other build falls back to the short hash of the current commit, suffixed
`-dirty` when the working tree has uncommitted changes, so a stray build can never pass
for a release.

Both build (which writes the header) and manifest (which validates it) import from here;
keeping the format in one place is what lets validate check the header against the
manifest byte for byte.
"""

from __future__ import annotations

import re
import subprocess

from .paths import PROJECT_ROOT

# The header is one HTML comment on line 1, so every consumer that already skips a leading
# comment keeps working. Field order is fixed; `corpus_version:` is the only labelled
# segment so a later extension (source_url, status, ...) can add more labelled segments
# without moving the positional ones in front of it.
_HEADER_RE = re.compile(
    r"^<!--\s*(?P<product>\S+)\s+(?P<release>\S+)\s*\|\s*(?P<source_id>[^|]+?)\s*\|\s*"
    r"(?P<source_path>[^|]+?)\s*(?:\|\s*corpus_version:\s*(?P<corpus_version>\S+)\s*)?-->\s*$"
)

UNKNOWN_VERSION = "unknown"


def default_corpus_version(root=PROJECT_ROOT) -> str:
    """Short hash of the checked-out commit, `-dirty` if the tree has local changes.

    Returns "unknown" when git is unavailable or `root` is not a repository, rather than
    raising: a build should still run from a tarball, it just cannot name its commit.
    """
    try:
        sha = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=root, capture_output=True, text=True, check=True,
        ).stdout.strip()
        status = subprocess.run(
            ["git", "status", "--porcelain", "--untracked-files=no"],
            cwd=root, capture_output=True, text=True, check=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return UNKNOWN_VERSION
    if not sha:
        return UNKNOWN_VERSION
    return f"{sha}-dirty" if status.strip() else sha


def render_header(
    product: str, release: str, source_id: str, source_path: str, corpus_version: str
) -> str:
    """Line 1 of every processed .md file, newline included."""
    return (
        f"<!-- {product} {release} | {source_id} | {source_path}"
        f" | corpus_version: {corpus_version} -->\n"
    )


def parse_header(first_line: str) -> dict[str, str | None] | None:
    """Fields of a provenance header, or None if the line is not one.

    `corpus_version` is None for a header written before the field existed, which lets
    validate report "no version" separately from "wrong version".
    """
    m = _HEADER_RE.match(first_line.rstrip("\r\n"))
    return m.groupdict() if m else None


def read_header(path) -> dict[str, str | None] | None:
    """parse_header applied to the first line of a file on disk."""
    with open(path, encoding="utf-8") as f:
        return parse_header(f.readline())
