"""pandoc leaves two artefacts in the converted chapters: cross-reference anchors whose text
is a per-file count or a bracketed label, and heading levels that jump (H1 to H5). The
extractor renders a reference as the target's own title in quotes -- searchable in any
file -- and closes heading gaps without flattening real structure.
"""

from __future__ import annotations

import buildstock_corpus.extract.latex as L

CHAPTER = """\\label{chap:3_sampling}
\\chapter{Sampling}
\\section{Characteristic Estimation}\\label{Characteristic Estimation}
See Table~\\ref{tab:window_data_sources} and Figure \\ref{fig:comstock_workflow}.
\\subsection{Infiltration}\\label{sec:infil}
\\begin{equation}\\label{energyplus_infiltration_eqn} x = y \\end{equation}
\\begin{figure}\\caption{Flowchart of the \\gls{ComStock} workflow.}\\label{fig:comstock_workflow}\\end{figure}
"""
TABLE = "\\begin{table}\\caption[short]{Window Property \\textbf{Data} Sources}\\label{tab:window_data_sources}\\end{table}\n"


def _project(tmp_path):
    (tmp_path / "tables").mkdir()
    (tmp_path / "3_sampling.tex").write_text(CHAPTER, encoding="utf-8")
    (tmp_path / "tables" / "window_data_sources.tex").write_text(TABLE, encoding="utf-8")
    return tmp_path


def test_labels_resolve_to_captions_and_headings_and_skip_equations(tmp_path):
    titles = L._label_titles(_project(tmp_path))
    assert titles == {
        "chap:3_sampling": "Sampling",  # label written before its heading: looks forward
        "Characteristic Estimation": "Characteristic Estimation",
        "sec:infil": "Infiltration",
        "fig:comstock_workflow": "Flowchart of the ComStock workflow.",  # \gls unwrapped
        "tab:window_data_sources": "Window Property Data Sources",  # \textbf unwrapped
    }
    assert "energyplus_infiltration_eqn" not in titles  # equations have no title


def test_cross_references_become_quoted_titles_or_plain_text():
    md = (
        'Table <a href="#tab:window_data_sources" data-reference-type="ref" data-reference="tab:window_data_sources">1.3</a> '
        'and Section <a href="#chap:3_sampling" data-reference-type="ref" data-reference="chap:3_sampling">[chap:3_sampling]</a>; '
        'Equation <a href="#energyplus_infiltration_eqn" data-reference-type="ref" data-reference="energyplus_infiltration_eqn">[energyplus_infiltration_eqn]</a>.'
    )
    titles = {"tab:window_data_sources": "Window Property Data Sources", "chap:3_sampling": "Sampling"}
    out = L._render_cross_references(md, titles)
    assert out == (
        "Table “Window Property Data Sources” and Section “Sampling”; "
        "Equation energyplus_infiltration_eqn."
    )
    assert "data-reference-type" not in out


def test_heading_gaps_close_without_flattening_structure():
    md = "# Exec\n\n##### Motivation\n\ntext\n\n##### Approach\n\n# Meta\n\n## Code\n\n#### Adoption\n\n#### Compliance\n\n## Turnover\n\n### Envelope\n\n#### Windows\n"
    out = L._normalize_heading_levels(md)
    levels = [len(l) - len(l.lstrip("#")) for l in out.split("\n") if l.startswith("#")]
    assert levels == [1, 2, 2, 1, 2, 3, 3, 2, 3, 4]
    assert "## Motivation" in out and "### Adoption" in out and "#### Windows" in out


def test_heading_normalization_leaves_code_fences_alone():
    md = "# T\n\n```\n##### not a heading\n```\n\n##### real\n"
    out = L._normalize_heading_levels(md)
    assert "##### not a heading" in out and "\n## real" in out


def test_well_formed_headings_are_unchanged():
    md = "# A\n\n## B\n\n### C\n\n## D\n\n# E\n\n## F\n"
    assert L._normalize_heading_levels(md) == md
