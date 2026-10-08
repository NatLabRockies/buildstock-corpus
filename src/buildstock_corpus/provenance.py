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

The header is line 1 of every processed .md file: one HTML comment, one line, so a parser
that skips a leading comment keeps working and `head -1` shows everything. Three
positional segments (product + release, source id, upstream path) are followed by
labelled `key: value` segments -- status, source_url, publication_url, corpus_version
today -- in a fixed order, so a consumer that fetched one file with no clone and no
manifest still has what it needs to cite it (see links.py and status.py for the fields).

Both build (which writes the header) and manifest (which validates it) import from here;
keeping the format in one place is what lets validate check the header against the
manifest row field by field.
"""

from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path

from .paths import PROJECT_ROOT

# Labelled segments, in the order they are written. Values never contain " | " or "-->":
# URLs are percent-encoded, status is a bare word, the version is a tag or hash. The last
# three appear only on section files (see sections.py): the parent document's corpus_path,
# the section heading, and the lines it spans in the parent.
HEADER_FIELDS = (
    "status", "source_url", "publication_url", "corpus_version",
    "corpus_path", "section", "lines",
)

_POSITIONAL_RE = re.compile(
    r"^<!--\s*(?P<product>\S+)\s+(?P<release>\S+)\s*\|\s*(?P<source_id>[^|]+?)\s*\|\s*"
    r"(?P<source_path>[^|]+?)\s*(?P<rest>(?:\|.*?)?)-->\s*$"
)
_LABELLED_RE = re.compile(r"^(?P<key>[a-z_]+):\s*(?P<value>.*)$")

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
    product: str, release: str, source_id: str, source_path: str, **fields: str | None
) -> str:
    """Line 1 of a processed .md file, newline included.

    `fields` are the labelled segments (see HEADER_FIELDS); they are written in that fixed
    order and a None is omitted rather than written as "None". An unknown key is an error,
    so a typo cannot silently produce a header validate will reject.
    """
    unknown = set(fields) - set(HEADER_FIELDS)
    if unknown:
        raise ValueError(f"render_header: unknown header field(s) {sorted(unknown)}")
    for key, value in fields.items():
        if value is not None and (" | " in str(value) or "-->" in str(value)):
            raise ValueError(f"render_header: {key} value cannot contain ' | ' or '-->': {value!r}")
    parts = [f"{product} {release}", source_id, source_path]
    parts += [f"{k}: {fields[k]}" for k in HEADER_FIELDS if fields.get(k) is not None]
    return "<!-- " + " | ".join(parts) + " -->\n"


def parse_header(first_line: str) -> dict[str, str | None] | None:
    """Fields of a provenance header, or None if the line is not one.

    Every key in HEADER_FIELDS is present in the result; one the header does not carry is
    None, which lets validate report "no value" separately from "wrong value" and lets a
    header written before a field existed still parse.
    """
    m = _POSITIONAL_RE.match(first_line.rstrip("\r\n"))
    if not m:
        return None
    out: dict[str, str | None] = {
        "product": m.group("product"),
        "release": m.group("release"),
        "source_id": m.group("source_id"),
        "source_path": m.group("source_path"),
        **{k: None for k in HEADER_FIELDS},
    }
    rest = m.group("rest").strip()
    for seg in (s.strip() for s in rest.lstrip("|").split(" | ") if s.strip()):
        lm = _LABELLED_RE.match(seg)
        if not lm:
            return None  # a stray unlabelled segment: not a header this module wrote
        out[lm.group("key")] = lm.group("value").strip()
    return out


def read_header(path) -> dict[str, str | None] | None:
    """parse_header applied to the first line of a file on disk."""
    with open(path, encoding="utf-8") as f:
        return parse_header(f.readline())


def body_sha256(data: bytes) -> str:
    """sha256 of a processed file's bytes after its line-1 header.

    `output_sha256` covers the whole file, and line 1 names the corpus version, so every
    build moves every output hash: comparing two builds by it says only that they are two
    builds. The body hash leaves the header out, so it moves only when the extracted
    content did -- which is what `bsc changelog` needs to tell a re-rendered document from
    one merely re-stamped. A file with no newline is all header and has an empty body.
    """
    nl = data.find(b"\n")
    return hashlib.sha256(data[nl + 1 :] if nl >= 0 else b"").hexdigest()


def body_sha256_file(path) -> str:
    """body_sha256 of a file on disk."""
    return body_sha256(Path(path).read_bytes())
