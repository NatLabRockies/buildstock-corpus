"""Smoke-test sampling: `--sample N` caps documents per category deterministically, and
pushes the cap down into the expensive extractors rather than filtering after the work.
"""

from __future__ import annotations

import buildstock_corpus.extract.latex as L
from buildstock_corpus.build import _cap


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
        clone, "documentation/reference_doc/main.tex", "comstock", "2025-3", "tr", limit=1
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
        clone, "documentation/reference_doc/main.tex", "comstock", "2025-3", "tr"
    )

    assert len(docs) == 3
    assert converted == ["ch1.tex", "ch2.tex", "ch3.tex"]
