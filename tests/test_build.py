"""Smoke-test sampling: `--sample N` caps documents per category deterministically, and
pushes the cap down into the expensive extractors rather than filtering after the work.
"""

from __future__ import annotations

import os
import subprocess

import pytest

import buildstock_corpus.build as B
import buildstock_corpus.extract.latex as L
from buildstock_corpus.build import (
    _assign_status,
    _cap,
    _date_docs,
    _measure_extra,
    _write_processed,
)
from buildstock_corpus.extract.doc_dates import DocDate, git_doc_date
from buildstock_corpus.extract.measures_index import MeasureRef
from buildstock_corpus.normalize import Document
from buildstock_corpus.provenance import parse_header
from buildstock_corpus.registry import Source

RELEASE = "comstock_amy2018_2025_release_3"


def _doc(source_id: str, source_type: str, source_path: str) -> Document:
    return Document(
        product="comstock", release=RELEASE, source_id=source_id, source_type=source_type,
        source_path=source_path, title=source_path, body="# t\n\nbody\n",
    )


def test_declared_source_status_is_stamped_on_every_document():
    src = Source(id="github_site", type="markdown", repo="r", git_ref="x",
                 doc_glob="docs/**/*.md", status="site_page")
    docs = [_doc("github_site", "markdown", "docs/a.md"), _doc("github_site", "markdown", "docs/b.md")]

    _assign_status(docs, src, {})

    assert [d.status for d in docs] == ["site_page", "site_page"]


MEASURES_SRC = Source(
    id="upgrade_measures", type="measures", repo="r", git_ref="x",
    index_page="docs/upgrade_measures/upgrade_measures.md",
    internal_dir="docs/upgrade_measures", crosswalk_csv="assets/files/c.csv",
)
MEASURES_STATE = {
    "internal_pages": [{"path": "docs/upgrade_measures/env_window_film.md", "sha256": "a"}],
    "local_pdfs": [{"path": "assets/files/ComStock Measure Doc_PV.pdf", "sha256": "b"}],
    "external_pdfs": [
        {"url": "https://docs.nlr.gov/docs/fy25osti/95002.pdf", "path": "measure_pdfs/95002.pdf",
         "sha256": "c", "status": "ok"},
    ],
}


def test_measure_documents_are_classified_by_how_the_site_links_them():
    """A page and a PDF the site serves itself are one class; an OSTI report is another."""
    docs = [
        _doc("upgrade_measures", "measures", "docs/upgrade_measures/env_window_film.md"),
        _doc("upgrade_measures", "pdf", "assets/files/ComStock Measure Doc_PV.pdf"),
        _doc("upgrade_measures", "pdf", "measure_pdfs/95002.pdf"),
    ]

    _assign_status(docs, MEASURES_SRC, MEASURES_STATE)

    assert [d.status for d in docs] == ["site_page", "site_page", "osti_pdf"]


def test_measure_document_outside_the_fetch_state_is_an_error():
    docs = [_doc("upgrade_measures", "pdf", "measure_pdfs/00000.pdf")]
    with pytest.raises(ValueError, match="no publication status for measure_pdfs/00000.pdf"):
        _assign_status(docs, MEASURES_SRC, MEASURES_STATE)


def test_written_file_opens_with_the_full_provenance_header(tmp_path, monkeypatch):
    """Line 1 is all a consumer who fetched one file has; it must carry everything a
    citation needs, taken from the same Document fields the manifest row is built from."""
    monkeypatch.setattr(B, "processed_root", lambda p, r: tmp_path)
    doc = Document(
        product="comstock",
        release=RELEASE,
        source_id="technical_reference",
        source_type="latex",
        source_path="documentation/reference_doc/4_9_hvac.tex",
        title="HVAC Systems",
        body="# HVAC Systems\n\nbody\n",
        status="site_page",
        source_url="https://github.com/NatLabRockies/ComStock/blob/b77c60d/documentation/reference_doc/4_9_hvac.tex",
        publication_url="https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf",
    )

    _write_processed("comstock", RELEASE, [doc], {}, f"{RELEASE}-v1")

    out = tmp_path / "technical_reference/documentation/reference_doc/4_9_hvac.md"
    first, second, *_ = out.read_text(encoding="utf-8").splitlines()
    assert parse_header(first) == {
        "product": "comstock",
        "release": RELEASE,
        "source_id": "technical_reference",
        "source_path": "documentation/reference_doc/4_9_hvac.tex",
        "status": "site_page",
        "source_url": doc.source_url,
        "publication_url": doc.publication_url,
        "corpus_version": f"{RELEASE}-v1",
    }
    assert second == "# HVAC Systems"
    assert b"\r\n" not in out.read_bytes()


def test_assign_provenance_resolves_status_and_both_links_once():
    """One resolution feeds both the header and the manifest row."""
    clones = [{"repo": "https://github.com/NatLabRockies/ComStock.github.io.git", "sha": "bacf551",
               "dest": "repos/ComStock.github.io@2025_3"}]
    state = {**MEASURES_STATE, "clone": "ComStock.github.io@2025_3"}
    src = Source(id="upgrade_measures", type="measures", repo=clones[0]["repo"], git_ref="2025_3",
                 index_page="i.md", internal_dir="d", crosswalk_csv="c.csv",
                 site_url="https://natlabrockies.github.io/ComStock.github.io")
    page = _doc("upgrade_measures", "measures", "docs/upgrade_measures/env_window_film.md")
    osti = _doc("upgrade_measures", "pdf", "measure_pdfs/95002.pdf")

    B._assign_provenance([page, osti], src, state, clones)

    assert page.status == "site_page"
    assert page.source_url == "https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551/docs/upgrade_measures/env_window_film.md"
    assert page.publication_url == "https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_window_film.html"
    assert osti.status == "osti_pdf"
    assert osti.source_url == osti.publication_url == "https://docs.nlr.gov/docs/fy25osti/95002.pdf"


def test_cap_none_keeps_everything():
    assert _cap([1, 2, 3], None) == [1, 2, 3]


def test_cap_takes_a_deterministic_prefix():
    """Sampling must be the first N in source order, so runs are reproducible."""
    assert _cap([1, 2, 3], 1) == [1]
    assert _cap([1, 2, 3], 2) == [1, 2]


def test_cap_tolerates_fewer_items_than_the_cap():
    assert _cap([1], 5) == [1]
    assert _cap([], 1) == []


def _tex_project(tmp_path):
    """Minimal LaTeX project: main.tex \\include-ing three chapters."""
    proj = tmp_path / "documentation" / "reference_doc"
    proj.mkdir(parents=True)
    (proj / "main.tex").write_text(
        "\\include{ch1}\n\\include{ch2}\n\\include{ch3}\n", encoding="utf-8"
    )
    for stem in ("ch1", "ch2", "ch3"):
        (proj / f"{stem}.tex").write_text(f"\\section{{{stem}}}\n", encoding="utf-8")
    return tmp_path


def _count_conversions(monkeypatch) -> list[str]:
    """Replace the pandoc call with a counter, so we can assert it stops early."""
    converted: list[str] = []

    def fake_convert(tex_path, cwd):
        converted.append(tex_path.name)
        return f"# {tex_path.stem}\n\nbody\n", ""

    monkeypatch.setattr(L, "_convert", fake_convert)
    return converted


def test_latex_limit_stops_converting_after_n_chapters(tmp_path, monkeypatch):
    """The saving must be real: chapter 2 and 3 never reach pandoc."""
    clone = _tex_project(tmp_path)
    converted = _count_conversions(monkeypatch)

    docs, warnings = L.load_latex_docs(
        clone, "documentation/reference_doc/main.tex", "comstock", RELEASE, "tr", limit=1
    )

    assert len(docs) == 1
    assert converted == ["ch1.tex"]
    assert docs[0].source_type == "latex"
    assert docs[0].source_path == "documentation/reference_doc/ch1.tex"
    assert warnings == []


def test_latex_without_limit_converts_every_chapter(tmp_path, monkeypatch):
    clone = _tex_project(tmp_path)
    converted = _count_conversions(monkeypatch)

    docs, _ = L.load_latex_docs(
        clone, "documentation/reference_doc/main.tex", "comstock", RELEASE, "tr"
    )

    assert len(docs) == 3
    assert converted == ["ch1.tex", "ch2.tex", "ch3.tex"]


# --- _date_docs: the shallow-clone guard on the non-measure sources -------------------


def _git_repo(root):
    root.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "-C", str(root), "init", "-q"], check=True)
    return root


def _commit(repo, rel, text, when):
    p = repo / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    subprocess.run(["git", "-C", str(repo), "add", rel], check=True)
    subprocess.run(
        ["git", "-C", str(repo), "-c", "user.name=T", "-c", "user.email=t@e",
         "commit", "-q", "-m", rel],
        check=True,
        env={**os.environ, "GIT_AUTHOR_DATE": when, "GIT_COMMITTER_DATE": when},
    )


def _md_doc(source_path):
    return Document(
        product="comstock", release=RELEASE, source_id="github_site",
        source_type="markdown", source_path=source_path, title="t", body="body\n",
    )


def test_date_docs_stamps_dates_on_full_clone(tmp_path):
    repo = _git_repo(tmp_path / "repo")
    _commit(repo, "docs/data.md", "page", "2026-06-24T10:00:00+00:00")
    doc = _md_doc("docs/data.md")

    warnings = _date_docs([doc], repo, "github_site", git_doc_date)

    assert warnings == []
    assert doc.extra["date_last_updated"] == "2026-06-24"
    assert doc.extra["date_last_updated_source"] == "git_commit"


def test_date_docs_warns_and_leaves_undated_on_shallow_clone(tmp_path):
    """A shallow clone dates every file to the tip commit, so refuse and say so once."""
    origin = _git_repo(tmp_path / "origin")
    _commit(origin, "docs/a.md", "a", "2024-01-01T10:00:00+00:00")
    _commit(origin, "docs/b.md", "b", "2024-02-01T10:00:00+00:00")
    shallow = tmp_path / "shallow"
    subprocess.run(
        ["git", "clone", "-q", "--depth", "1", origin.as_uri(), str(shallow)], check=True
    )
    doc = _md_doc("docs/b.md")

    warnings = _date_docs([doc], shallow, "github_site", git_doc_date)

    assert len(warnings) == 1 and "shallow" in warnings[0]
    assert "date_last_updated" not in doc.extra


# --- _measure_extra: the per-measure date carried into chunk metadata -----------------


def _ref(measure_id, target, kind="external_pdf"):
    return MeasureRef(
        measure_id=measure_id, name="Env: Roof", initial_release="2024_1",
        kind=kind, target=target,
    )


def test_measure_extra_carries_the_documents_date(tmp_path):
    ref = _ref("env_roof", "https://docs.nlr.gov/docs/fy25osti/95002.pdf")
    dates = {"https://docs.nlr.gov/docs/fy25osti/95002.pdf": DocDate("2025-09-09", "pdf_moddate")}

    extra = _measure_extra([ref], dates)

    assert extra["date_last_updated"] == "2025-09-09"
    assert extra["date_last_updated_source"] == "pdf_moddate"


def test_measure_extra_omits_date_keys_when_undated(tmp_path):
    """No date is a missing key, not None: Chroma cannot hold None and chunks drop it."""
    ref = _ref("env_roof", "https://docs.nlr.gov/docs/fy25osti/95002.pdf")

    extra_no_dates = _measure_extra([ref], None)
    extra_unknown_target = _measure_extra([ref], {"other": DocDate("2025-01-01", "git_commit")})

    for extra in (extra_no_dates, extra_unknown_target):
        assert "date_last_updated" not in extra
        assert "date_last_updated_source" not in extra
        assert extra["measure_id"] == "env_roof"  # identity still present


def test_measure_extra_and_crosswalk_agree_on_the_same_measure(tmp_path):
    """The invariant the hoist protects: one date resolution feeds both, so they cannot drift."""
    from buildstock_corpus.extract.crosswalk import build_crosswalk

    ref = _ref("env_roof", "https://docs.nlr.gov/docs/fy25osti/95002.pdf")
    dates = {"https://docs.nlr.gov/docs/fy25osti/95002.pdf": DocDate("2025-09-09", "pdf_moddate")}

    csv_path = tmp_path / "cw.csv"
    csv_path.write_text(
        "measure_id,measure_documentation_name,public_repo_measure_folder_name,"
        "2025_comstock_amy2018_release_3_upgrade_id\n"
        "env_roof,Env Roof,env_roof,1\n",
        encoding="utf-8",
    )
    cw = build_crosswalk(csv_path, [ref], RELEASE, dates)
    cw_measure = next(m for m in cw["measures"] if m["measure_id"] == "env_roof")
    extra = _measure_extra([ref], dates)

    assert extra["date_last_updated"] == cw_measure["date_last_updated"] == "2025-09-09"
    assert extra["date_last_updated_source"] == cw_measure["date_last_updated_source"]


def test_registry_excluded_pdfs_are_skipped_and_recorded(tmp_path):
    """A fetched PDF the registry excludes yields no spec, and the skip is recorded so the
    manifest can say it was left out on purpose."""
    state = {
        "external_pdfs": [
            {"url": "https://www.nlr.gov/docs/fy23osti/85853.pdf", "path": "measure_pdfs/85853.pdf", "sha256": "a", "status": "ok"},
            {"url": "https://docs.nlr.gov/docs/fy25osti/95002.pdf", "path": "measure_pdfs/95002.pdf", "sha256": "b", "status": "ok"},
        ],
        "local_pdfs": [],
    }
    specs, skipped = B._pdf_specs(
        "comstock", RELEASE, tmp_path, state, [],
        exclude_urls=frozenset({"https://www.nlr.gov/docs/fy23osti/85853.pdf"}),
    )
    assert [s.source_path for s in specs] == ["measure_pdfs/95002.pdf"]
    assert skipped == [{"path": "measure_pdfs/85853.pdf", "url": "https://www.nlr.gov/docs/fy23osti/85853.pdf",
                        "reason": "excluded by source registry"}]


def test_measure_doc_index_keys_every_url_spelling_to_one_document():
    src = Source(id="upgrade_measures", type="measures", repo="r", git_ref="x",
                 index_page="i.md", internal_dir="d", crosswalk_csv="c.csv",
                 output_remap={"docs/upgrade_measures": "unpublished_docs/upgrade_measures"})
    state = {"external_pdfs": [
        {"url": "https://www.nlr.gov/docs/fy26osti/92504.pdf", "path": "measure_pdfs/92504.pdf", "sha256": "x"},
        {"url": "https://docs.nlr.gov/docs/fy26osti/92504.pdf", "path": "measure_pdfs/92504.pdf", "sha256": "x"},
    ]}
    pdf = _doc("upgrade_measures", "pdf", "measure_pdfs/92504.pdf")
    pdf.publication_url = "https://docs.nlr.gov/docs/fy26osti/92504.pdf"
    page = _doc("upgrade_measures", "measures", "docs/upgrade_measures/env_window_film.md")
    page.publication_url = "https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_window_film.html"

    index = B._measure_doc_index([pdf, page], src, state)

    one = {"corpus_path": "upgrade_measures/measure_pdfs/92504.md", "doc_url": pdf.publication_url}
    assert index["https://www.nlr.gov/docs/fy26osti/92504.pdf"] == one
    assert index["https://docs.nlr.gov/docs/fy26osti/92504.pdf"] == one
    assert index["measure_pdfs/92504.pdf"] == one
    assert index["docs/upgrade_measures/env_window_film.md"] == {
        "corpus_path": "upgrade_measures/unpublished_docs/upgrade_measures/env_window_film.md",
        "doc_url": page.publication_url,
    }
