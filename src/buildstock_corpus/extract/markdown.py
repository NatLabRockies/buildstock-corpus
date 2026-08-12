"""Jekyll/Kramdown markdown cleanup for the github.io site + internal measure pages.

Strips front matter (capturing the title), HTML comments, Liquid tags, and Kramdown
attribute lists, leaving portable markdown. HTML comments are removed deliberately:
the source pages use them to withhold draft/unreleased content (e.g. greenhouse-gas
tables), which must not leak into the release-tagged corpus.
"""

from __future__ import annotations

import re
from pathlib import Path

from ..normalize import Document, collapse_blank_lines, first_heading

_FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
_TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)
_PUBLISHED_FALSE_RE = re.compile(r"^published:\s*false\s*$", re.IGNORECASE | re.MULTILINE)
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
_LIQUID_LINK_RE = re.compile(r"\{%\s*link\s+(.*?)\s*%\}")
_LIQUID_VAR_RE = re.compile(r"\{\{.*?\}\}")  # {{ site.baseurl }} and friends
_LIQUID_TAG_RE = re.compile(r"\{%.*?%\}")  # any remaining {% ... %}
_KRAMDOWN_ATTR_RE = re.compile(r"\{:[^}]*\}")  # {:refdef}, {: .fw-500 }, {:width="700"}


def clean_markdown(raw: str) -> tuple[str | None, str, bool]:
    """Return (title, cleaned_body, published) for one Jekyll markdown source file.

    published is False only when front matter explicitly sets `published: false`
    (Jekyll's marker for pages excluded from the live site — drafts/superseded copies).
    """
    title: str | None = None
    published = True
    fm = _FRONT_MATTER_RE.match(raw)
    if fm:
        block = fm.group(1)
        tm = _TITLE_RE.search(block)
        if tm:
            title = tm.group(1).strip().strip("\"'")
        if _PUBLISHED_FALSE_RE.search(block):
            published = False
        raw = raw[fm.end():]

    raw = _HTML_COMMENT_RE.sub("", raw)
    raw = _LIQUID_LINK_RE.sub(lambda m: m.group(1), raw)  # {% link path %} -> path
    raw = _LIQUID_VAR_RE.sub("", raw)
    raw = _LIQUID_TAG_RE.sub("", raw)
    raw = _KRAMDOWN_ATTR_RE.sub("", raw)

    body = collapse_blank_lines(raw)
    if not title:
        title = first_heading(body)
    return title, body, published


def load_markdown_docs(
    clone_dir: Path,
    rel_paths: list[str],
    product: str,
    release: str,
    source_id: str,
    source_type: str,
) -> tuple[list[Document], list[str]]:
    """Clean each repo-relative markdown file into a Document.

    Returns (documents, excluded). Pages with `published: false` are excluded (drafts
    not on the live site; their canonical form is the external PDF) — returned in the
    excluded list rather than silently dropped. Pages that clean to empty are dropped.
    """
    docs: list[Document] = []
    excluded: list[str] = []
    for rel in rel_paths:
        path = clone_dir / rel
        if not path.is_file():
            continue
        title, body, published = clean_markdown(path.read_text(encoding="utf-8", errors="replace"))
        if not published:
            excluded.append(rel)
            continue
        if not body.strip():
            continue
        docs.append(
            Document(
                product=product,
                release=release,
                source_id=source_id,
                source_type=source_type,
                source_path=rel,
                title=title or Path(rel).stem,
                body=body,
            )
        )
    return docs, excluded
