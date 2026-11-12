"""Jekyll/Kramdown markdown cleanup for the github.io site + internal measure pages.

Strips front matter (capturing the title), HTML comments, Liquid tags, and Kramdown
attribute lists, leaving portable markdown. HTML comments are removed deliberately:
the source pages use them to withhold draft/unreleased content (e.g. greenhouse-gas
tables), which must not leak into the release-tagged corpus.

Collapsible `<details>` blocks are unfolded (see _unfold_details): the site hides an answer
behind its `<summary>`, which is a heading in everything but markup, so the summary becomes
one. ResStock's FAQ page is 48 such blocks and had no question a reader could be sent to.
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

# <details> ... </details> and the <summary> that titles each one (it may span lines).
_DETAILS_TOKEN_RE = re.compile(
    r"<details\b[^>]*>|</details\s*>|<summary\b[^>]*>(.*?)</summary\s*>", re.DOTALL | re.I
)
_ANY_TAG_RE = re.compile(r"<[^>]+>")
_MD_HEADING_LINE_RE = re.compile(r"^(#{1,6})\s")
_BLOCK_TAG_INDENT_RE = re.compile(r"(?m)^[ \t]+(?=</?(?:p|ul|li)\b)", re.I)
_ANCHOR_RE = re.compile(r'<a\s+[^>]*?href="([^"]*)"[^>]*>(.*?)</a\s*>', re.DOTALL | re.I)
_UL_RE = re.compile(r"<ul\b[^>]*>(.*?)</ul\s*>", re.DOTALL | re.I)
_LI_RE = re.compile(r"<li\b[^>]*>\s*(.*?)\s*</li\s*>", re.DOTALL | re.I)
_P_OPEN_RE = re.compile(r"<p\b[^>]*>\s*", re.I)
_P_CLOSE_RE = re.compile(r"\s*</p\s*>", re.I)
_BOLD_RE = re.compile(r"<(b|strong)>(.*?)</\1>", re.DOTALL | re.I)
_ITALIC_RE = re.compile(r"<(i|em)>(.*?)</\1>", re.DOTALL | re.I)


def _last_heading_level(text: str) -> int:
    """Level of the last markdown heading in `text`, fenced code aside; 1 if there is none
    (the document's title is its H1 even when the body never repeats it)."""
    level = 1
    in_fence = False
    for line in text.split("\n"):
        if line.startswith("```"):
            in_fence = not in_fence
        elif not in_fence and (m := _MD_HEADING_LINE_RE.match(line)):
            level = len(m.group(1))
    return level


def _dedent_block(segment: str) -> str:
    """Remove the indentation a <details> body shares, so it is not read as a code block.

    The body of a collapsible block is written indented under its tag (four spaces on the
    ResStock FAQ). Once the tags are gone, a paragraph that still starts with four spaces
    after a blank line is an indented code block to any markdown reader. Only the
    indentation every line has in common is removed, so a nested list keeps its shape, and
    the contents of a fenced or <pre> block are neither measured nor moved.
    """
    lines = segment.split("\n")
    movable: list[int] = []
    in_fence = in_pre = False
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        opened_pre = "<pre" in line.lower()
        if not in_fence and not in_pre and stripped and i > 0:  # line 0 is the tag line's tail
            movable.append(i)
        if opened_pre:
            in_pre = True
        if "</pre" in line.lower():
            in_pre = False
    if not movable:
        return segment
    common = min(len(lines[i]) - len(lines[i].lstrip()) for i in movable)
    if not common:
        return segment
    for i in movable:
        lines[i] = lines[i][common:]
    return "\n".join(lines)


def _details_html_to_markdown(segment: str) -> str:
    """The simple HTML a <details> body is written in, as markdown: paragraphs, links,
    bullet lists, bold and italic. Anything else (a <pre> block, a table) is left as it is.
    The body's shared indentation is removed first (see _dedent_block), then whatever is
    left in front of a line that opens with one of the block tags handled here."""
    segment = _BLOCK_TAG_INDENT_RE.sub("", _dedent_block(segment))
    segment = _ANCHOR_RE.sub(lambda m: f"[{' '.join(m.group(2).split())}]({m.group(1)})", segment)
    segment = _UL_RE.sub(lambda m: "\n" + _LI_RE.sub(r"- \1", m.group(1)) + "\n", segment)
    segment = _P_CLOSE_RE.sub("\n", _P_OPEN_RE.sub("", segment))
    segment = _BOLD_RE.sub(r"**\2**", segment)
    return _ITALIC_RE.sub(r"*\2*", segment)


def _unfold_details(md: str) -> str:
    """Turn each collapsible block into a heading plus its content.

    `<summary>` becomes a heading one level below the heading the block sits under (two
    below for a block nested in another, and so on, to H6 at most), so every question on an
    FAQ page is a section a reader can be sent to and a chunk is filed under its own
    question. The `<details>` tags themselves carry nothing and are dropped. A page with no
    such block is returned untouched.
    """
    if "<details" not in md.lower():
        return md
    out: list[str] = []
    outside: list[str] = []  # the page's own text between blocks: where its headings are
    pos = 0
    depth = 0
    base = 1
    for m in _DETAILS_TOKEN_RE.finditer(md):
        segment = md[pos : m.start()]
        out.append(_details_html_to_markdown(segment) if depth else segment)
        if not depth:
            outside.append(segment)
        pos = m.end()
        token = m.group(0).lower()
        if token.startswith("<details"):
            if depth == 0:
                base = _last_heading_level("".join(outside))
            depth += 1
        elif token.startswith("</details"):
            depth = max(0, depth - 1)
            out.append("\n")
        else:
            title = " ".join(_ANY_TAG_RE.sub("", m.group(1)).split())
            if depth and title:
                out.append(f"\n\n{'#' * min(6, base + depth)} {title}\n\n")
            else:  # a <summary> outside any <details>, or an empty one: not ours to rewrite
                out.append(m.group(0))
    tail = md[pos:]
    out.append(_details_html_to_markdown(tail) if depth else tail)
    return "".join(out)


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
    raw = _unfold_details(raw)

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
