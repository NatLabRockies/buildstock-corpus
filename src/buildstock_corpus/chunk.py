"""Header-aware chunking: split each Document on markdown headings, pack paragraphs
into ~max_chars chunks, and carry provenance metadata so retrieval stays release-aware
and citations point at a document + section + line range.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from .normalize import Document

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")


@dataclass
class Chunk:
    id: str
    text: str
    metadata: dict = field(default_factory=dict)


@dataclass
class _Section:
    breadcrumb: str  # e.g. "3. ComStock Baseline Approach > 3.1 Applicability"
    lines: list[str]
    first_line: int = 0  # 0-based index in the body of lines[0]


@dataclass
class _Para:
    text: str
    start: int  # 0-based body index of the paragraph's first line
    end: int  # ... and of its last line (inclusive)


def _split_sections(body: str) -> list[_Section]:
    """Walk lines, tracking the heading stack, and group body text under each heading.

    Each section remembers the body index of its first line, so a chunk cut from it can
    say which lines it covers (see chunk_document's line_start / line_end).
    """
    stack: list[tuple[int, str]] = []  # (level, text)
    sections: list[_Section] = []
    current: list[str] = []
    current_start = 0

    def breadcrumb() -> str:
        return " > ".join(text for _, text in stack)

    def flush() -> None:
        if current and any(line.strip() for line in current):
            sections.append(_Section(breadcrumb(), current.copy(), current_start))
        current.clear()

    for i, line in enumerate(body.splitlines()):
        m = _HEADING_RE.match(line)
        if m:
            flush()
            level = len(m.group(1))
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, m.group(2).strip()))
        else:
            if not current:
                current_start = i
            current.append(line)
    flush()

    if not sections:  # body with no headings at all
        sections.append(_Section("", body.splitlines(), 0))
    return sections


def _paragraphs(lines: list[str], first_line: int = 0) -> list[_Para]:
    """Blank-line-separated paragraphs, each with the body indices of its lines."""
    paras: list[_Para] = []
    buf: list[str] = []
    start = 0
    for k, line in enumerate(lines):
        if line.strip():
            if not buf:
                start = first_line + k
            buf.append(line)
        elif buf:
            paras.append(_Para("\n".join(buf), start, first_line + k - 1))
            buf = []
    if buf:
        paras.append(_Para("\n".join(buf), start, first_line + len(lines) - 1))
    return paras


def _hard_split(text: str, max_chars: int) -> list[str]:
    return [text[i : i + max_chars] for i in range(0, len(text), max_chars)]


def _pack(paras: list[_Para], max_chars: int, overlap_chars: int) -> list[tuple[str, int, int]]:
    """Greedily fill chunks up to max_chars on paragraph boundaries, with small overlap.

    Returns (text, start, end) per chunk: the text exactly as before this function tracked
    lines (so chunk ids and texts are stable across that change), and the body indices of
    the whole paragraphs the chunk draws from. The overlap tail copied in from the previous
    chunk is not part of the range -- it belongs to that chunk's lines -- and a paragraph
    longer than max_chars is hard-split into pieces that all carry the paragraph's full
    range, since no piece boundary falls on a line.
    """
    chunks: list[tuple[str, int, int]] = []
    buf = ""
    span = [0, 0]
    for para in paras:
        pieces = _hard_split(para.text, max_chars) if len(para.text) > max_chars else [para.text]
        for piece in pieces:
            if buf and len(buf) + len(piece) + 2 > max_chars:
                chunks.append((buf, span[0], span[1]))
                tail = buf[-overlap_chars:] if overlap_chars else ""
                if tail:  # don't begin the overlap mid-word
                    space = tail.find(" ")
                    tail = tail[space + 1 :] if space != -1 else ""
                buf = (tail + "\n\n" + piece) if tail else piece
                span = [para.start, para.end]
            else:
                if buf:
                    span[1] = para.end
                else:
                    span = [para.start, para.end]
                buf = (buf + "\n\n" + piece) if buf else piece
    if buf.strip():
        chunks.append((buf, span[0], span[1]))
    return chunks


def chunk_document(
    doc: Document,
    max_chars: int = 1400,
    overlap_chars: int = 200,
    *,
    corpus_version: str | None = None,
    line_offset: int = 1,
) -> list[Chunk]:
    """Chunk one document; every chunk carries where it sits and which build it is from.

    `section` is the heading path (H1 > ... > Hn) the chunk sits under; `line_start` /
    `line_end` are the 1-based lines of the whole paragraphs it draws from, in the file the
    reader will open; `corpus_version` names the build. Together they let a retrieval hit
    be cited as "<corpus_path> lines a-b at <corpus_version>" and re-read with `sed -n`.

    Chunking runs on doc.body, which is not quite the processed file: build prepends a
    provenance header and a title line and may drop the body's own title line (see
    build._leading_heading_offset). `line_offset` is what maps a 0-based body index to a
    1-based file line; the default, 1, is right for a body written verbatim from line 1.
    Chroma metadata holds only scalars, so the heading path stays a string.
    """
    chunks: list[Chunk] = []
    ordinal = 0
    for section in _split_sections(doc.body):
        paras = _paragraphs(section.lines, section.first_line)
        if not paras:
            continue
        for body_text, start, end in _pack(paras, max_chars, overlap_chars):
            breadcrumb = section.breadcrumb
            header = f"{doc.title} — {breadcrumb}" if breadcrumb else doc.title
            metadata = {
                "product": doc.product,
                "release": doc.release,
                "source_id": doc.source_id,
                "source_type": doc.source_type,
                "source_path": doc.source_path,
                "doc_title": doc.title,
                "section": breadcrumb,
                "line_start": start + line_offset,
                "line_end": end + line_offset,
            }
            if corpus_version is not None:
                metadata["corpus_version"] = corpus_version
            if doc.status is not None:  # Chroma metadata cannot hold None
                metadata["status"] = doc.status
            metadata.update({k: v for k, v in doc.extra.items() if v is not None})
            chunks.append(
                Chunk(
                    id=f"{doc.source_id}|{doc.source_path}|{ordinal}",
                    text=f"{header}\n\n{body_text.strip()}",
                    metadata=metadata,
                )
            )
            ordinal += 1
    return chunks


def chunk_documents(
    docs: list[Document],
    line_offsets: dict[tuple[str, str], int] | None = None,
    **kw,
) -> list[Chunk]:
    """Chunk every document; `line_offsets` maps (source_id, source_path) to the file-line
    offset build computed for it (see chunk_document), defaulting to 1."""
    line_offsets = line_offsets or {}
    out: list[Chunk] = []
    for doc in docs:
        offset = line_offsets.get((doc.source_id, doc.source_path), 1)
        out.extend(chunk_document(doc, line_offset=offset, **kw))
    return out
