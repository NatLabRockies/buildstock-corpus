"""When was each measure document last updated? (the crosswalk's currency signal)

A measure's documentation is one of two things, and each can prove its own date a
different way:

  * a published PDF, which carries a revision date in its own metadata     -> pdf_moddate
  * a markdown page in the site repo, whose last change is a commit there  -> git_commit

Both answer the same question — when did this document last change at its source — so the
date is recorded with the source that established it rather than on its own. An undated
date is a claim; a dated one with its provenance is evidence, and a measure whose
documentation does not exist yet gets no date at all rather than a stand-in.

Deliberately NOT used as sources:

  * the HTTP Last-Modified of a downloaded PDF — that is when the web host last touched
    its copy, which moves when a site is migrated (these URLs moved to nlr.gov in 2026)
    without the document itself being revised.
  * filesystem mtime under raw/ — that is when *we* fetched, not when upstream published.

Reproducibility note: git dates need real commit history. fetch clones blobless but with
full history for exactly this reason; against a `--depth 1` clone every file would report
the clone tip's own commit date, which looks like an answer and is not one.
"""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

from ..paths import long_path

# 'D:20230714122936-06'00'' -> the date as the producer stated it, no timezone shifting:
# the document's own claim about its revision day is the thing being recorded.
_PDF_DATE = re.compile(r"^D:(?P<y>\d{4})(?P<m>\d{2})(?P<d>\d{2})")

# Mirrors extract.latex._INPUT_RE: a LaTeX chapter pulls its dense tables with
# \input{tables/...}, and those files are inlined into the document before pandoc sees it.
# Dating a chapter therefore has to walk the same \input set, or a chapter whose prose is
# old but whose tables were refreshed would report a stale date (6_AppendixA is exactly
# that case). Keep this pattern in step with latex._INPUT_RE.
_INPUT_RE = re.compile(r"\\input\{([^}]+)\}")


@dataclass(frozen=True)
class DocDate:
    """A document's last-updated date (ISO 8601 'YYYY-MM-DD') and how it was established."""

    date: str
    source: str  # "pdf_moddate" | "git_commit"


def _pdf_date(path: Path) -> str | None:
    """The revision date a PDF states in its own metadata, preferring ModDate.

    ModDate is when the file was last written, CreationDate when it was first produced;
    for an unrevised document they are the same, and for a revised one ModDate is the
    answer to the question being asked.
    """
    try:
        import pypdfium2 as pdfium
    except ImportError:  # pragma: no cover - the extract extra provides it
        return None

    try:
        doc = pdfium.PdfDocument(long_path(path))
    except Exception:  # noqa: BLE001 - an unreadable PDF is undated, not fatal
        return None
    try:
        meta = doc.get_metadata_dict() or {}
    except Exception:  # noqa: BLE001
        return None
    finally:
        doc.close()

    for key in ("ModDate", "CreationDate"):
        m = _PDF_DATE.match(str(meta.get(key) or ""))
        if m:
            return f"{m['y']}-{m['m']}-{m['d']}"
    return None


def _is_shallow(repo: Path) -> bool:
    """Is `repo` a shallow clone? Then git dating is a lie waiting to happen.

    Against a shallow clone `git log -- <path>` reports the clone tip for every file, so
    every document collapses onto one date that looks like an answer and is not (see the
    module docstring). Callers use this to refuse to date rather than emit that fake
    uniform date. A missing git is not shallow — it is simply undatable, handled downstream.
    """
    try:
        out = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "--is-shallow-repository"],
            capture_output=True,
            text=True,
            check=False,
        ).stdout.strip()
    except OSError:  # pragma: no cover - git missing
        return False
    return out == "true"


def _git_date(repo: Path, rel_path: str) -> str | None:
    """The commit date of the last commit to touch `rel_path` in `repo`.

    Committer date, not author date: the question is when the file last changed at the
    host, and a rebased or cherry-picked page changed there when it landed.
    """
    try:
        out = subprocess.run(
            ["git", "-C", str(repo), "log", "-1", "--format=%cI", "--", rel_path],
            capture_output=True,
            text=True,
            check=False,
        ).stdout.strip()
    except OSError:  # pragma: no cover - git missing
        return None
    return out[:10] or None


def resolve_doc_dates(src_state: dict, raw_root: Path, clone_dir: Path) -> dict[str, DocDate]:
    """Map each measure document (by the target the index page links to) to its date.

    Keys match `MeasureRef.target`, so the crosswalk can look a measure's date up by the
    same string it already records as `doc_target`: an absolute URL for an external PDF, a
    repo-relative path for a local PDF or an internal markdown page.
    """
    dates: dict[str, DocDate] = {}

    # External PDFs: downloaded under raw/. Mirror URLs that served byte-identical content
    # share one file, so each URL is keyed separately onto that file's date.
    for entry in src_state.get("external_pdfs", []):
        if entry.get("status") != "ok":
            continue
        date = _pdf_date(raw_root / entry["path"])
        if date:
            dates[entry["url"]] = DocDate(date, "pdf_moddate")

    # Local PDFs: published documents that happen to be committed to the site repo. Their
    # own metadata still describes the document; the commit only says when it was posted.
    for entry in src_state.get("local_pdfs", []):
        rel = entry["path"]
        date = _pdf_date(clone_dir / rel)
        if date:
            dates[rel] = DocDate(date, "pdf_moddate")
        else:
            git = _git_date(clone_dir, rel)
            if git:
                dates[rel] = DocDate(git, "git_commit")

    # Internal markdown pages: no document metadata to consult, so the repo is the record.
    for entry in src_state.get("internal_pages", []):
        rel = entry["path"]
        git = _git_date(clone_dir, rel)
        if git:
            dates[rel] = DocDate(git, "git_commit")

    return dates


def git_doc_date(clone_dir: Path, rel_path: str) -> DocDate | None:
    """Last-updated date of a single repo file, from its last commit (git_commit).

    The github.io how-to/methodology pages carry no document metadata of their own, so the
    repo is the record — the same rule already applied to internal measure pages in
    resolve_doc_dates. Caller is responsible for the shallow-clone check (_is_shallow).
    """
    git = _git_date(clone_dir, rel_path)
    return DocDate(git, "git_commit") if git else None


def _latex_input_closure(chapter: Path, proj_dir: Path, seen: set[Path], _depth: int = 0) -> None:
    """Collect `chapter` and every .tex it transitively \\input's that exists on disk.

    Mirrors extract.latex._expand_inputs' file resolution (append '.tex' when absent, drop
    missing targets, depth cap) so the date covers exactly the text pandoc converts. Results
    accumulate into `seen`; `\\input` paths are resolved relative to `proj_dir` (the project
    root), matching how latex.py reads them.
    """
    if _depth > 10 or chapter in seen or not chapter.is_file():
        return
    seen.add(chapter)
    text = chapter.read_text(encoding="utf-8", errors="replace")
    for rel in _INPUT_RE.findall(text):
        rel = rel.strip()
        fp = proj_dir / (rel if rel.endswith(".tex") else f"{rel}.tex")
        _latex_input_closure(fp, proj_dir, seen, _depth + 1)


def latex_doc_date(clone_dir: Path, chapter_rel: str) -> DocDate | None:
    """Last-updated date of a LaTeX chapter, over the chapter file and its \\input'd tables.

    A chapter is not one file: it inlines its dense tables from tables/*.tex, and those can
    be revised long after the surrounding prose. So the date is the latest commit across the
    whole \\input closure, not the chapter file alone — otherwise a refreshed table sitting
    under stale prose would be reported as stale. Source stays 'git_commit'; the closure rule
    is an implementation detail of how that commit date is established.

    Caller is responsible for the shallow-clone check (_is_shallow); on a shallow clone every
    path in the closure collapses to the tip commit and this would return a fake uniform date.
    """
    chapter = clone_dir / chapter_rel
    closure: set[Path] = set()
    _latex_input_closure(chapter, chapter.parent, closure)
    dates = [
        d
        for p in closure
        if (d := _git_date(clone_dir, p.relative_to(clone_dir).as_posix()))
    ]
    return DocDate(max(dates), "git_commit") if dates else None
