"""Every table wrapper in a converted chapter names the LaTeX file the table came from, so a
reader who knows the reference's tables/ layout can map between the two. The label matches
the file name in only 46 of 78 cases upstream, which is why the attribute exists.
"""

from __future__ import annotations

import re
from types import SimpleNamespace

import buildstock_corpus.extract.latex as L

CHAPTER = """\\chapter{HVAC}
Intro.
\\input{tables/ashp_eff}
\\input{tables/chiller_curves.tex}
\\begin{table}
\\caption{Inline one}
\\label{tab:inline_table}
\\begin{tabular}{|l|}\\hline a \\\\ \\hline\\end{tabular}
\\end{table}
"""
ASHP = "\\begin{table}\\caption{ASHP}\\label{tab:ashp_eff}\\begin{tabular}{|l|}\\hline x \\\\ \\hline\\end{tabular}\\end{table}\n"
CHILLER = "\\begin{table}\\caption{Curves}\\label{tab:wcc_perf_curves}\\begin{tabular}{|l|}\\hline y \\\\ \\hline\\end{tabular}\\end{table}\n"


def _project(tmp_path):
    (tmp_path / "tables").mkdir()
    (tmp_path / "4_9_hvac.tex").write_text(CHAPTER, encoding="utf-8")
    (tmp_path / "tables" / "ashp_eff.tex").write_text(ASHP, encoding="utf-8")
    (tmp_path / "tables" / "chiller_curves.tex").write_text(CHILLER, encoding="utf-8")
    return tmp_path


def _fake_pandoc(text, cwd, citeproc):
    """Stand in for pandoc: one <div id="tab:..."> wrapper per table label, like the real one."""
    out = "# HVAC\n\n" + "\n".join(
        f'<div id="{lab}">\n\n| a |\n|---|\n\n</div>' for lab in re.findall(r"\\label\{(tab:[^}]+)\}", text)
    )
    return SimpleNamespace(returncode=0, stdout=out + "\n", stderr="")


def test_labels_are_collected_from_inlined_table_files(tmp_path):
    proj = _project(tmp_path)
    labels: dict[str, str] = {}
    L._expand_inputs((proj / "4_9_hvac.tex").read_text(encoding="utf-8"), proj, labels=labels)
    assert labels == {"tab:ashp_eff": "tables/ashp_eff.tex", "tab:wcc_perf_curves": "tables/chiller_curves.tex"}
    # the inline table's label is not an input file's, so it is not in the map


def test_wrappers_name_their_file_or_the_chapter(tmp_path, monkeypatch):
    proj = _project(tmp_path)
    monkeypatch.setattr(L, "_pandoc", _fake_pandoc)

    md, _ = L._convert(proj / "4_9_hvac.tex", proj)

    assert '<div id="tab:ashp_eff" data-source="tables/ashp_eff.tex">' in md  # label == file stem
    assert '<div id="tab:wcc_perf_curves" data-source="tables/chiller_curves.tex">' in md  # label != stem
    assert '<div id="tab:inline_table" data-source="4_9_hvac.tex">' in md  # written in the chapter
    assert md.count("data-source=") == 3


def test_stamp_is_idempotent_and_leaves_other_divs_alone():
    md = '<div id="tab:a">\n<div id="fig:b">\n<div id="tab:c" data-source="tables/c.tex">\n'
    once = L._stamp_table_sources(md, {"tab:a": "tables/a.tex"}, "ch.tex")
    assert once == (
        '<div id="tab:a" data-source="tables/a.tex">\n<div id="fig:b">\n'
        '<div id="tab:c" data-source="tables/c.tex">\n'
    )
    assert L._stamp_table_sources(once, {"tab:a": "tables/a.tex"}, "ch.tex") == once
