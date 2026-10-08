"""Per-section files: every H2 of every document as its own small, citable markdown file.

Forty documents are over 100 KB and the largest is 437 KB; no agent reads those whole. A
section file is how it reads them: `sections.json` names the file for a heading, and one
fetch returns just that section with everything a citation needs on its line 1.

Layout, beside the documents under processed/<product>/<release>/:

    sections/<source_id>/<document stem>/<NN>-<slug>.md

`00-<title slug>` holds what sits between the H1 and the first H2 when there is any text
there (a document with no H2 at all gets only that file, which is the document again under
a predictable path; a bare title line followed by its H2 gets no 00- file); `NN-<slug>`
holds the NN-th H2 with every H3+ beneath it, down to the next H2. Files tile the document
from line 2 onward -- or from the first H2 when only the title line precedes it -- so
concatenating a document's sections in order reproduces its content.

Line 1 of a section file is the document's own provenance header plus three labelled
fields: the parent `corpus_path`, the `section` heading, and the `lines` it spans in the
parent. The rest is the parent's lines, byte for byte.

Section files are a pure function of the document, so they are not hashed into the
manifest: `bsc validate` regenerates them from the document on disk and compares. The same
function plans, writes and checks, so the three cannot disagree.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

from .chunk import _HEADING_RE
from .paths import long_path
from .provenance import parse_header, render_header

SECTIONS_DIRNAME = "sections"
MAX_SLUG = 40
_SLUG_RE = re.compile(r"[^a-z0-9]+")


def document_sections(text: str) -> list[dict]:
    """Every heading in a processed file, with its level and 1-based line range.

    A section runs from its heading line to the line before the next heading of any
    level (or the last line of the file), so ranges tile the file after the first heading
    and `lines[line_start-1:line_end]` is exactly the section's text.
    """
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()  # the trailing newline is not a line
    heads = [(i + 1, m) for i, line in enumerate(lines) if (m := _HEADING_RE.match(line))]
    out: list[dict] = []
    for k, (ln, m) in enumerate(heads):
        end = heads[k + 1][0] - 1 if k + 1 < len(heads) else len(lines)
        out.append({
            "heading": m.group(2).strip(),
            "level": len(m.group(1)),
            "line_start": ln,
            "line_end": end,
        })
    return out


def slugify(text: str, max_len: int = MAX_SLUG) -> str:
    """Lower-case ASCII slug, capped so section paths stay short (Windows MAX_PATH)."""
    s = _SLUG_RE.sub("-", text.lower()).strip("-")[:max_len].rstrip("-")
    return s or "section"


@dataclass
class SectionPlan:
    name: str  # file stem: 00-<title slug> or NN-<heading slug>
    heading: str
    level: int  # 1 for the preamble (the document's H1), 2 for an H2
    line_start: int  # 1-based, in the parent document
    line_end: int
    file: str  # processed/-relative path of the section file


def sections_dir(corpus_path: str) -> str:
    """processed/-relative directory a document's section files live in.

    Flat by source: `sections/<source_id>/<document stem>/`, not a mirror of the document's
    directory tree. The mirror reached 268-character absolute paths on a typical Windows
    checkout, where git refuses to add them and plain file access fails without long-path
    opt-in; this form stays under the 260 limit. `sections.json` names the exact file for
    every heading, so no consumer derives the path by hand.
    """
    source_id, stem = doc_slot(corpus_path)
    return f"{SECTIONS_DIRNAME}/{source_id}/{stem}"


def doc_slot(corpus_path: str) -> tuple[str, str]:
    """(source_id, document stem): the short, flat address every derived tree keys on."""
    base = corpus_path[:-3] if corpus_path.endswith(".md") else corpus_path
    source_id, _, rest = base.partition("/")
    stem = rest.rsplit("/", 1)[-1] if rest else source_id
    return source_id, stem


def check_unique_section_dirs(corpus_paths: list[str]) -> None:
    """Refuse two documents that would share a section dir (same source id and stem)."""
    seen: dict[str, str] = {}
    for cp in corpus_paths:
        d = sections_dir(cp)
        if d in seen:
            raise ValueError(
                f"section dir collision: {cp!r} and {seen[d]!r} both map to {d}; "
                f"rename one upstream or extend sections_dir"
            )
        seen[d] = cp


def plan_sections(corpus_path: str, text: str) -> list[SectionPlan]:
    """Which section files a document yields, and the lines each covers."""
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    heads = document_sections(text)
    h2 = [h for h in heads if h["level"] == 2]
    title = next((h["heading"] for h in heads if h["level"] == 1 and h["line_start"] == 2), None)
    d = sections_dir(corpus_path)
    plans: list[SectionPlan] = []
    first_h2 = h2[0]["line_start"] if h2 else len(lines) + 1
    # A preamble file only when there is text between the title line and the first H2; a
    # bare title followed by its H2 has nothing a reader would fetch on its own.
    if first_h2 > 2 and any(line.strip() for line in lines[2 : first_h2 - 1]):
        name = "00-" + slugify(title or "preamble")
        plans.append(SectionPlan(name, title or "", 1, 2, first_h2 - 1, f"{d}/{name}.md"))
    width = max(2, len(str(len(h2))))
    for k, h in enumerate(h2, start=1):
        end = h2[k]["line_start"] - 1 if k < len(h2) else len(lines)
        name = f"{k:0{width}d}-{slugify(h['heading'])}"
        plans.append(SectionPlan(name, h["heading"], 2, h["line_start"], end, f"{d}/{name}.md"))
    return plans


def _safe(value: str) -> str:
    # A heading cannot be allowed to break the one-line header comment.
    return value.replace(" | ", " / ").replace("-->", "--").strip()


def render_sections(corpus_path: str, text: str) -> dict[str, str]:
    """{section file path: its full content} for a document, from the document alone.

    The document's own line-1 header supplies the provenance fields, so a section file
    says exactly what its parent says, plus where in the parent it came from.
    """
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    header = parse_header(lines[0]) if lines else None
    if header is None:
        raise ValueError(f"{corpus_path}: line 1 is not a provenance header; cannot cut sections")
    out: dict[str, str] = {}
    for p in plan_sections(corpus_path, text):
        front = render_header(
            header["product"], header["release"], header["source_id"], header["source_path"],
            status=header.get("status"), source_url=header.get("source_url"),
            publication_url=header.get("publication_url"),
            corpus_version=header.get("corpus_version"),
            corpus_path=corpus_path, section=_safe(p.heading) or None,
            lines=f"{p.line_start}-{p.line_end}",
        )
        out[p.file] = front + "\n".join(lines[p.line_start - 1 : p.line_end]) + "\n"
    return out


def _read(path: str) -> str:
    with open(long_path(path), encoding="utf-8", newline="") as f:
        return f.read()


def _write(path: str, content: str) -> None:
    os.makedirs(long_path(os.path.dirname(path)), exist_ok=True)
    with open(long_path(path), "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def _listdir_files(dirpath: str) -> list[str]:
    try:
        return sorted(n for n in os.listdir(long_path(dirpath)) if n.endswith(".md"))
    except FileNotFoundError:
        return []


def write_sections(proot: Path, corpus_path: str, text: str) -> list[SectionPlan]:
    """Write a document's section files, replacing whatever that document's dir held."""
    d = str(proot / sections_dir(corpus_path))
    for stale in _listdir_files(d):
        os.remove(long_path(os.path.join(d, stale)))
    for rel, content in render_sections(corpus_path, text).items():
        _write(str(proot / rel), content)
    return plan_sections(corpus_path, text)


def check_sections(
    proot: Path, corpus_path: str, text: str, where: str
) -> tuple[list[str], int, bool]:
    """(violations, files checked, present) for one document's section files on disk.

    Regenerates from the document and compares byte for byte: a missing, changed or extra
    file under the document's section dir is a violation, since the files are committed
    output a consumer fetches on their own. A document with no section dir at all is not
    a violation -- like an absent map, the files are derived and `bsc map` regenerates
    them -- so `present` is False and nothing is checked; validate reports the count.
    """
    expected = render_sections(corpus_path, text)
    errors: list[str] = []
    d = str(proot / sections_dir(corpus_path))
    if not os.path.isdir(long_path(d)):
        return [], 0, False
    on_disk = {os.path.join(sections_dir(corpus_path), n).replace("\\", "/") for n in _listdir_files(d)}
    for rel, content in expected.items():
        path = str(proot / rel)
        if rel not in on_disk:
            errors.append(f"{where}: section file missing: {rel}")
        elif _read(path) != content:
            errors.append(f"{where}: section file differs from its document: {rel}")
    for rel in sorted(on_disk - set(expected)):
        errors.append(f"{where}: section file not produced by its document: {rel}")
    return errors, len(expected), True


def write_all_sections(proot: Path, corpus_paths: list[str]) -> int:
    """Replace the whole sections/ tree from the documents on disk; returns files written.

    Used by `bsc map`, so section files can be regenerated in seconds without raw/, and
    by build after it writes the documents.
    """
    import shutil

    check_unique_section_dirs(corpus_paths)
    tree = proot / SECTIONS_DIRNAME
    if tree.exists():
        shutil.rmtree(long_path(tree))
    n = 0
    for rel in corpus_paths:
        n += len(write_sections(proot, rel, _read(str(proot / rel))))
    return n


def orphan_section_files(proot: Path, documents: list[str]) -> list[str]:
    """Section files under sections/ that belong to no document in `documents`."""
    root = proot / SECTIONS_DIRNAME
    if not root.exists():
        return []
    expected = {sections_dir(c) for c in documents}
    orphans: list[str] = []
    for dirpath, _dirs, files in os.walk(long_path(root)):
        rel_dir = os.path.relpath(dirpath, long_path(proot)).replace("\\", "/")
        if rel_dir in expected:
            continue
        orphans += [f"{rel_dir}/{f}" for f in files if f.endswith(".md")]
    return sorted(orphans)
