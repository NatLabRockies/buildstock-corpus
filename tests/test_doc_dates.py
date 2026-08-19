"""Per-document 'last updated' dates — the crosswalk's currency signal.

Both sources are exercised for real rather than stubbed: a hand-built PDF whose Info dict
carries the dates, and an actual git repo with dated commits. The point of the field is
that the date is evidence, so a test that fakes the evidence would pin nothing.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

from buildstock_corpus.extract.doc_dates import (
    DocDate,
    _git_date,
    _is_shallow,
    _pdf_date,
    git_doc_date,
    latex_doc_date,
    resolve_doc_dates,
)

MOD = b"D:20250909162920-06'00'"
CREATED = b"D:20240101000000Z"


def minimal_pdf(moddate: bytes | None = None, createdate: bytes | None = None) -> bytes:
    """A one-page PDF with a real xref, so pdfium parses it the way it parses a report."""
    info = b"<<"
    if moddate:
        info += b"/ModDate(" + moddate + b")"
    if createdate:
        info += b"/CreationDate(" + createdate + b")"
    info += b">>"
    objs = [
        b"<</Type/Catalog/Pages 2 0 R>>",
        b"<</Type/Pages/Kids[3 0 R]/Count 1>>",
        b"<</Type/Page/Parent 2 0 R/MediaBox[0 0 200 200]>>",
        info,
    ]
    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for i, body in enumerate(objs, start=1):
        offsets.append(len(out))
        out += f"{i} 0 obj".encode() + body + b"endobj\n"
    xref = len(out)
    out += f"xref\n0 {len(objs) + 1}\n".encode()
    out += b"0000000000 65535 f \n"
    for off in offsets:
        out += f"{off:010d} 00000 n \n".encode()
    out += (
        f"trailer<</Size {len(objs) + 1}/Root 1 0 R/Info 4 0 R>>\n"
        f"startxref\n{xref}\n%%EOF\n"
    ).encode()
    return bytes(out)


def write_pdf(path: Path, **kwargs) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(minimal_pdf(**kwargs))
    return path


# --- PDF metadata ---------------------------------------------------------------------


def test_moddate_preferred_over_creationdate(tmp_path):
    """A revised document's ModDate is the answer; CreationDate is when it was first made."""
    pdf = write_pdf(tmp_path / "a.pdf", moddate=MOD, createdate=CREATED)
    assert _pdf_date(pdf) == "2025-09-09"


def test_creationdate_used_when_never_revised(tmp_path):
    pdf = write_pdf(tmp_path / "b.pdf", createdate=CREATED)
    assert _pdf_date(pdf) == "2024-01-01"


def test_pdf_without_dates_is_undated(tmp_path):
    """No date is a better answer than a guessed one."""
    assert _pdf_date(write_pdf(tmp_path / "c.pdf")) is None


def test_unreadable_pdf_is_undated_not_fatal(tmp_path):
    junk = tmp_path / "junk.pdf"
    junk.write_bytes(b"not a pdf at all")
    assert _pdf_date(junk) is None


def test_pdf_date_keeps_the_producers_stated_day(tmp_path):
    """No timezone shifting: 'D:20250101013000+09:00' is that document's 2025-01-01.

    Converting to UTC would move a late-evening or early-morning revision to the day
    before or after the one the document itself claims.
    """
    pdf = write_pdf(tmp_path / "tz.pdf", moddate=b"D:20250101013000+09'00'")
    assert _pdf_date(pdf) == "2025-01-01"


# --- git history ----------------------------------------------------------------------


def git_repo(root: Path) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    return root


def commit(repo: Path, rel: str, text: str | None, when: str) -> None:
    """Commit `rel` at date `when`; `text=None` commits whatever is already on disk.

    Passing None matters for the PDF cases — writing placeholder text over a PDF would
    leave nothing for the metadata reader to find, and the test would pass for the wrong
    reason (falling back to git because the file stopped being a PDF).
    """
    path = repo / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    if text is not None:
        path.write_text(text, encoding="utf-8")
    subprocess.run(["git", "add", rel], cwd=repo, check=True)
    subprocess.run(
        ["git", "-c", "user.name=T", "-c", "user.email=t@e", "commit", "-q", "-m", rel],
        cwd=repo,
        check=True,
        env={**os.environ, "GIT_AUTHOR_DATE": when, "GIT_COMMITTER_DATE": when},
    )


def test_git_date_is_per_file(tmp_path):
    repo = git_repo(tmp_path / "repo")
    commit(repo, "docs/old.md", "old", "2024-03-04T10:00:00+00:00")
    commit(repo, "docs/new.md", "new", "2026-01-15T10:00:00+00:00")

    assert _git_date(repo, "docs/old.md") == "2024-03-04"
    assert _git_date(repo, "docs/new.md") == "2026-01-15"


def test_git_date_follows_the_latest_change_not_the_first(tmp_path):
    repo = git_repo(tmp_path / "repo")
    commit(repo, "docs/page.md", "v1", "2024-03-04T10:00:00+00:00")
    commit(repo, "docs/page.md", "v2", "2025-07-08T10:00:00+00:00")

    assert _git_date(repo, "docs/page.md") == "2025-07-08"


def test_git_date_none_for_untracked_path(tmp_path):
    repo = git_repo(tmp_path / "repo")
    commit(repo, "docs/page.md", "v1", "2024-03-04T10:00:00+00:00")

    assert _git_date(repo, "docs/never_committed.md") is None


def test_shallow_clone_cannot_date_files_which_is_why_fetch_keeps_history(tmp_path):
    """The bug this field's plumbing exists to avoid.

    Against `git clone --depth 1` every path resolves to the single tip commit, so all
    documents report the same day and it looks like a real answer. fetch clones blobless
    with full history precisely so this test's `full` case is what production sees.
    """
    origin = git_repo(tmp_path / "origin")
    commit(origin, "docs/old.md", "old", "2024-03-04T10:00:00+00:00")
    commit(origin, "docs/new.md", "new", "2026-01-15T10:00:00+00:00")

    shallow = tmp_path / "shallow"
    subprocess.run(
        ["git", "clone", "-q", "--depth", "1", origin.as_uri(), str(shallow)], check=True
    )
    full = tmp_path / "full"
    subprocess.run(["git", "clone", "-q", origin.as_uri(), str(full)], check=True)

    # shallow: both files collapse onto the tip commit's date
    assert _git_date(shallow, "docs/old.md") == _git_date(shallow, "docs/new.md")
    # full history: each file keeps its own
    assert _git_date(full, "docs/old.md") == "2024-03-04"
    assert _git_date(full, "docs/new.md") == "2026-01-15"


# --- resolve_doc_dates ----------------------------------------------------------------


def test_resolve_dates_across_all_three_document_kinds(tmp_path):
    raw = tmp_path / "raw"
    clone = git_repo(tmp_path / "clone")
    write_pdf(raw / "measure_pdfs/95002.pdf", moddate=MOD)
    commit(clone, "docs/upgrade_measures/env_roof.md", "page", "2026-03-09T10:00:00+00:00")
    write_pdf(clone / "assets/files/doc.pdf", moddate=b"D:20260121090000Z")
    commit(clone, "assets/files/doc.pdf", None, "2026-01-28T10:00:00+00:00")

    state = {
        "external_pdfs": [
            {"url": "https://docs.example.gov/95002.pdf", "path": "measure_pdfs/95002.pdf",
             "sha256": "x", "status": "ok"},
        ],
        "local_pdfs": [{"path": "assets/files/doc.pdf", "sha256": "y"}],
        "internal_pages": [{"path": "docs/upgrade_measures/env_roof.md", "sha256": "z"}],
    }

    dates = resolve_doc_dates(state, raw, clone)

    # keyed by the same target string the index page links to, so crosswalk can join on it
    assert dates["https://docs.example.gov/95002.pdf"] == DocDate("2025-09-09", "pdf_moddate")
    assert dates["docs/upgrade_measures/env_roof.md"] == DocDate("2026-03-09", "git_commit")
    # a published PDF that happens to be committed is dated by the document, not the commit
    assert dates["assets/files/doc.pdf"] == DocDate("2026-01-21", "pdf_moddate")


def test_local_pdf_without_metadata_falls_back_to_its_commit(tmp_path):
    """Still answerable: the repo knows when the file last changed even if the PDF does not."""
    raw = tmp_path / "raw"
    clone = git_repo(tmp_path / "clone")
    write_pdf(clone / "assets/files/bare.pdf")  # a real PDF, just with no dates in its Info dict
    commit(clone, "assets/files/bare.pdf", None, "2025-05-06T10:00:00+00:00")

    dates = resolve_doc_dates({"local_pdfs": [{"path": "assets/files/bare.pdf"}]}, raw, clone)

    assert dates["assets/files/bare.pdf"] == DocDate("2025-05-06", "git_commit")


def test_mirror_urls_sharing_one_file_each_get_its_date(tmp_path):
    """fetch dedupes byte-identical mirrors onto one path; both URLs still need a date."""
    raw = tmp_path / "raw"
    write_pdf(raw / "measure_pdfs/95002.pdf", moddate=MOD)
    state = {
        "external_pdfs": [
            {"url": "https://a.example/95002.pdf", "path": "measure_pdfs/95002.pdf",
             "status": "ok"},
            {"url": "https://b.example/95002.pdf", "path": "measure_pdfs/95002.pdf",
             "status": "ok", "note": "duplicate content"},
        ]
    }

    dates = resolve_doc_dates(state, raw, git_repo(tmp_path / "clone"))

    assert dates["https://a.example/95002.pdf"].date == "2025-09-09"
    assert dates["https://b.example/95002.pdf"].date == "2025-09-09"


def test_undownloaded_pdf_is_absent_rather_than_dated(tmp_path):
    """An unreachable PDF is a tracked gap; inventing a date for it would hide that."""
    state = {
        "external_pdfs": [
            {"url": "https://gone.example/x.pdf", "path": "measure_pdfs/x.pdf",
             "status": "error"},
        ]
    }

    dates = resolve_doc_dates(state, tmp_path / "raw", git_repo(tmp_path / "clone"))

    assert dates == {}


def test_missing_file_on_disk_is_absent_rather_than_dated(tmp_path):
    state = {"external_pdfs": [{"url": "u", "path": "measure_pdfs/nope.pdf", "status": "ok"}]}

    assert resolve_doc_dates(state, tmp_path / "raw", git_repo(tmp_path / "clone")) == {}


# --- _is_shallow ----------------------------------------------------------------------


def test_is_shallow_true_for_depth1_clone_false_for_full(tmp_path):
    """The probe that lets the build refuse to date a shallow clone instead of faking it."""
    origin = git_repo(tmp_path / "origin")
    commit(origin, "a.txt", "a", "2024-01-01T10:00:00+00:00")
    commit(origin, "b.txt", "b", "2024-02-01T10:00:00+00:00")

    shallow = tmp_path / "shallow"
    subprocess.run(
        ["git", "clone", "-q", "--depth", "1", origin.as_uri(), str(shallow)], check=True
    )
    full = tmp_path / "full"
    subprocess.run(["git", "clone", "-q", origin.as_uri(), str(full)], check=True)

    assert _is_shallow(shallow) is True
    assert _is_shallow(full) is False


# --- git_doc_date (github_site pages) -------------------------------------------------


def test_git_doc_date_wraps_commit_and_is_none_for_untracked(tmp_path):
    repo = git_repo(tmp_path / "repo")
    commit(repo, "docs/data.md", "page", "2026-06-24T10:00:00+00:00")

    assert git_doc_date(repo, "docs/data.md") == DocDate("2026-06-24", "git_commit")
    assert git_doc_date(repo, "docs/never.md") is None


# --- latex_doc_date (chapter + its \input closure) ------------------------------------


def test_latex_doc_date_uses_latest_of_chapter_and_its_inputs(tmp_path):
    """The case chapter-file-only dating gets wrong: old prose, a freshly revised table.

    This mirrors 6_AppendixA in the real tech reference (chapter 2024-05, tables 2025-08).
    The document is the chapter plus everything it \\input's, so its date is the latest of
    the two, not the chapter file's own commit.
    """
    repo = git_repo(tmp_path / "repo")
    commit(
        repo,
        "documentation/reference_doc/appendix.tex",
        "\\section{Appendix}\n\\input{tables/big}\n",
        "2024-05-01T10:00:00+00:00",
    )
    commit(
        repo,
        "documentation/reference_doc/tables/big.tex",
        "| col |\n| --- |\n| v |\n",
        "2025-08-20T10:00:00+00:00",
    )

    dd = latex_doc_date(repo, "documentation/reference_doc/appendix.tex")

    assert dd == DocDate("2025-08-20", "git_commit")


def test_latex_doc_date_recurses_nested_inputs(tmp_path):
    """\\input can nest; the date must reach the deepest file, matching _expand_inputs."""
    repo = git_repo(tmp_path / "repo")
    commit(repo, "d/ch.tex", "\\input{a}\n", "2024-01-01T10:00:00+00:00")
    commit(repo, "d/a.tex", "\\input{b}\n", "2024-06-01T10:00:00+00:00")
    commit(repo, "d/b.tex", "deepest table\n", "2026-02-02T10:00:00+00:00")

    assert latex_doc_date(repo, "d/ch.tex") == DocDate("2026-02-02", "git_commit")


def test_latex_doc_date_ignores_missing_input(tmp_path):
    """A dropped \\input target (as _expand_inputs drops it) dates by the chapter alone."""
    repo = git_repo(tmp_path / "repo")
    commit(repo, "d/ch.tex", "\\input{tables/gone}\nbody\n", "2025-03-03T10:00:00+00:00")

    assert latex_doc_date(repo, "d/ch.tex") == DocDate("2025-03-03", "git_commit")
