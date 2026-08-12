"""Shared in-memory document model and format-agnostic text cleanup.

Every extractor (markdown now; latex/pdf later) produces `Document` objects with a
cleaned markdown `body` plus the provenance fields the chunker and manifest need.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

_BLANK_RUN_RE = re.compile(r"\n{3,}")
_SLUG_RE = re.compile(r"[^a-z0-9]+")


@dataclass
class Document:
    product: str
    release: str
    source_id: str
    source_type: str  # markdown | measures | latex | pdf
    source_path: str  # repo-relative path or url-derived id (the citation anchor)
    title: str
    body: str  # cleaned markdown
    extra: dict = field(default_factory=dict)  # extra provenance folded into chunk metadata
                                               # (e.g. measure_id, measure_initial_release, url)


def collapse_blank_lines(text: str) -> str:
    """Trim trailing whitespace per line and collapse blank runs to a single blank."""
    text = "\n".join(line.rstrip() for line in text.splitlines())
    text = _BLANK_RUN_RE.sub("\n\n", text)
    return text.strip() + "\n"


def first_heading(body: str) -> str | None:
    for line in body.splitlines():
        if line.startswith("#"):
            return line.lstrip("#").strip() or None
    return None


def slug(text: str) -> str:
    return _SLUG_RE.sub("-", text.lower()).strip("-") or "untitled"
