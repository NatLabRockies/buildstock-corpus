"""Smoke-test sampling: `--sample N` caps documents per category deterministically, and
pushes the cap down into the expensive extractors rather than filtering after the work.
"""

from __future__ import annotations

import os
import subprocess

import buildstock_corpus.extract.latex as L
from buildstock_corpus.build import _cap, _date_docs, _measure_extra
from buildstock_corpus.extract.doc_dates import DocDate, git_doc_date
from buildstock_corpus.extract.measures_index import MeasureRef
from buildstock_corpus.normalize import Document

RELEASE = "comstock_amy2018_2025_release_3"


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
    ref = _ref("env_roof", "https://docs.example.gov/roof.pdf")
    dates = {"https://docs.example.gov/roof.pdf": DocDate("2025-09-09", "pdf_moddate")}

    extra = _measure_extra([ref], dates)

    assert extra["date_last_updated"] == "2025-09-09"
    assert extra["date_last_updated_source"] == "pdf_moddate"


def test_measure_extra_omits_date_keys_when_undated(tmp_path):
    """No date is a missing key, not None: Chroma cannot hold None and chunks drop it."""
    ref = _ref("env_roof", "https://docs.example.gov/roof.pdf")

    extra_no_dates = _measure_extra([ref], None)
    extra_unknown_target = _measure_extra([ref], {"other": DocDate("2025-01-01", "git_commit")})

    for extra in (extra_no_dates, extra_unknown_target):
        assert "date_last_updated" not in extra
        assert "date_last_updated_source" not in extra
        assert extra["measure_id"] == "env_roof"  # identity still present


def test_measure_extra_and_crosswalk_agree_on_the_same_measure(tmp_path):
    """The invariant the hoist protects: one date resolution feeds both, so they cannot drift."""
    from buildstock_corpus.extract.crosswalk import build_crosswalk

    ref = _ref("env_roof", "https://docs.example.gov/roof.pdf")
    dates = {"https://docs.example.gov/roof.pdf": DocDate("2025-09-09", "pdf_moddate")}

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
