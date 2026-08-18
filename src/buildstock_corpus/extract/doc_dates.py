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
