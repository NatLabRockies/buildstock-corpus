"""Header-aware chunking: split each Document on markdown headings, pack paragraphs
into ~max_chars chunks, and carry provenance metadata so retrieval stays release-aware
and citations point at a document + section.
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


def _split_sections(body: str) -> list[_Section]:
    """Walk lines, tracking the heading stack, and group body text under each heading."""
    stack: list[tuple[int, str]] = []  # (level, text)
    sections: list[_Section] = []
    current: list[str] = []

    def breadcrumb() -> str:
        return " > ".join(text for _, text in stack)

    def flush() -> None:
        if current and any(line.strip() for line in current):
            sections.append(_Section(breadcrumb(), current.copy()))
        current.clear()

    for line in body.splitlines():
        m = _HEADING_RE.match(line)
        if m:
            flush()
            level = len(m.group(1))
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, m.group(2).strip()))
        else:
            current.append(line)
    flush()

    if not sections:  # body with no headings at all
        sections.append(_Section("", body.splitlines()))
    return sections


def _paragraphs(lines: list[str]) -> list[str]:
    paras: list[str] = []
    buf: list[str] = []
    for line in lines:
        if line.strip():
            buf.append(line)
        elif buf:
            paras.append("\n".join(buf))
            buf = []
    if buf:
        paras.append("\n".join(buf))
    return paras


def _hard_split(text: str, max_chars: int) -> list[str]:
    return [text[i : i + max_chars] for i in range(0, len(text), max_chars)]


def _pack(paras: list[str], max_chars: int, overlap_chars: int) -> list[str]:
    """Greedily fill chunks up to max_chars on paragraph boundaries, with small overlap."""
    chunks: list[str] = []
    buf = ""
    for para in paras:
        for piece in (_hard_split(para, max_chars) if len(para) > max_chars else [para]):
            if buf and len(buf) + len(piece) + 2 > max_chars:
                chunks.append(buf)
                tail = buf[-overlap_chars:] if overlap_chars else ""
                if tail:  # don't begin the overlap mid-word
                    space = tail.find(" ")
                    tail = tail[space + 1 :] if space != -1 else ""
                buf = (tail + "\n\n" + piece) if tail else piece
            else:
                buf = (buf + "\n\n" + piece) if buf else piece
    if buf.strip():
        chunks.append(buf)
    return chunks


def chunk_document(doc: Document, max_chars: int = 1400, overlap_chars: int = 200) -> list[Chunk]:
    chunks: list[Chunk] = []
    ordinal = 0
    for section in _split_sections(doc.body):
        paras = _paragraphs(section.lines)
        if not paras:
            continue
        for body_text in _pack(paras, max_chars, overlap_chars):
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
            }
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


def chunk_documents(docs: list[Document], **kw) -> list[Chunk]:
    out: list[Chunk] = []
    for doc in docs:
        out.extend(chunk_document(doc, **kw))
    return out
