"""The LaTeX loader's per-project behaviour (R1.2 of PLAN-resstock.md).

ResStock's technical reference guide differs from ComStock's in ways the first loader
assumed away: chapters are pulled with \\input and several are commented out, tables come
in a custom `customLongTable` environment with caption and label as arguments, longtables
keep their caption and sprinkle `\\noalign{}` on every rule, the bibliography and the
figure directory have other names, and six figures are PDF files. None of this needs
pandoc to test; the conversions here are the text rewrites that happen before pandoc runs.
"""

from __future__ import annotations

import struct
import sys
import types
from types import SimpleNamespace

import pypdfium2 as pdfium

import buildstock_corpus.extract.latex as L

# --- chapter list ---------------------------------------------------------------------------

MAIN = """\\documentclass[]{nlr}
\\begin{document}
\\input{1_Introduction.tex}
\\include{2_Structure}
% \\input{4_RunningResStock.tex}
% PRIORITY C \\input{7_Validation.tex}
%\\begin{appendices}
%  \\input{Appendix_ResStock-RTD}
%\\end{appendices}
\\end{document}
"""


def test_chapter_list_takes_input_and_include_and_skips_commented_ones(tmp_path):
    main = tmp_path / "main.tex"
    main.write_text(MAIN, encoding="utf-8")
    assert L._chapter_files(main) == ["1_Introduction.tex", "2_Structure"]


# --- \\input expansion ------------------------------------------------------------------------


def test_commented_input_is_not_inlined_and_an_escaped_percent_is_not_a_comment(tmp_path):
    (tmp_path / "live.tex").write_text("LIVE\n", encoding="utf-8")
    (tmp_path / "dead.tex").write_text("DEAD LINE 1\nDEAD LINE 2\n", encoding="utf-8")
    text = "A \\input{live}\n% \\input{dead} % TODO too big\n50\\% done \\input{live}\n"

    out = L._expand_inputs(text, tmp_path)

    assert out.count("LIVE") == 2
    assert "DEAD" not in out  # the retired table stays retired
    assert "% \\input{dead} % TODO too big" in out  # the comment itself is kept verbatim


# --- customLongTable --------------------------------------------------------------------------

CUSTOM = """Intro.
\\begin{customLongTable}{ |p{3.cm}|p{1.5cm}| }
{Bedrooms options} {table:hc_opt_bedrooms}
{Option name & Stock saturation}
1 & 10\\% \\\\ \\hline
2 & 30\\% \\\\ \\hline
\\end{customLongTable}
After.
"""


def test_custom_longtable_expands_to_the_plain_longtable_its_definition_means():
    out = L._expand_custom_longtables(CUSTOM)

    assert "customLongTable" not in out
    assert out.startswith("Intro.\n\\begin{longtable}{|p{3.cm}|p{1.5cm}|}\n")
    assert "\\caption{Bedrooms options} \\label{table:hc_opt_bedrooms} \\\\\n" in out
    assert "\\toprule\nOption name & Stock saturation \\\\\n\\midrule\n\\endhead\n" in out
    assert "\\endhead\n1 & 10\\% \\\\ \\hline\n2 & 30\\% \\\\ \\hline\n\\bottomrule\n\\end{longtable}\nAfter." in out


MULTILINE_ARGS = """\\begin{customLongTable}
{ |p{3.cm}|p{3cm}| }
{Neighbors options}
{table:hc_opt_neighbor}
{Option name & \\texttt{neighbor\\_left\\_distance}
}  \\hline
None & 90\\% \\\\ \\hline
\\end{customLongTable}
"""


def test_custom_longtable_arguments_may_span_lines_and_nest_braces():
    out = L._expand_custom_longtables(MULTILINE_ARGS)

    assert "\\caption{Neighbors options} \\label{table:hc_opt_neighbor} \\\\" in out
    assert "\\toprule\nOption name & \\texttt{neighbor\\_left\\_distance} \\\\\n\\midrule" in out
    # whatever followed the fourth argument is the body, here a leading \\hline
    assert "\\endhead\n\\hline\nNone & 90\\% \\\\ \\hline\n\\bottomrule" in out


def test_malformed_custom_longtable_is_left_for_pandoc():
    text = "\\begin{customLongTable}{a}{b}\nno fourth argument and no end"
    assert L._expand_custom_longtables(text) == text


def test_expand_inputs_runs_the_custom_longtable_rewrite_and_collects_its_label(tmp_path):
    (tmp_path / "characteristics").mkdir()
    (tmp_path / "characteristics" / "Bedrooms.tex").write_text(CUSTOM, encoding="utf-8")
    labels: dict[str, str] = {}

    out = L._expand_inputs("\\input{characteristics/Bedrooms}\n", tmp_path, labels=labels)

    assert "\\begin{longtable}" in out and "customLongTable" not in out
    assert labels == {"table:hc_opt_bedrooms": "characteristics/Bedrooms.tex"}


# --- longtable normalization ------------------------------------------------------------------

RESSTOCK_LT = """\\begin{longtable}[]{ |p{3cm}| }
\\caption{The State characteristic} \\label{table:hc_arg_def_state}  \\\\
\\toprule\\noalign{}
Name \\\\
\\midrule\\noalign{}
\\endhead
\\bottomrule\\noalign{}
\\endlastfoot
AL \\\\
\\end{longtable}"""


def test_longtable_keeps_its_caption_and_label_and_loses_noalign_and_page_machinery():
    out = L._normalize_longtable(RESSTOCK_LT)

    assert "\\caption{The State characteristic}" in out
    assert "\\label{table:hc_arg_def_state}" in out
    for gone in ("noalign", "\\endhead", "\\endlastfoot"):
        assert gone not in out
    assert "\\toprule\nName \\\\\n\\midrule\n\n\\bottomrule\n\nAL" in out


# --- cross-reference titles and table wrappers ------------------------------------------------


def test_label_titles_resolve_table_prefixes_and_custom_longtable_captions(tmp_path):
    (tmp_path / "ch.tex").write_text(
        "\\section{Inputs}\n" + CUSTOM
        + "\\begin{longtable}{|l|}\n\\caption{Plain one} \\label{Tab:plain} \\\\\n\\end{longtable}\n",
        encoding="utf-8",
    )
    titles = L._label_titles(tmp_path)
    assert titles["table:hc_opt_bedrooms"] == "Bedrooms options"  # from the environment's arguments
    assert titles["Tab:plain"] == "Plain one"  # case-insensitive prefix


def test_table_wrappers_with_resstock_labels_are_stamped():
    md = '<div id="table:hc_opt_bedrooms">\n| a |\n</div>\n<div id="Tab:plain">\n</div>'
    out = L._stamp_table_sources(md, {"table:hc_opt_bedrooms": "characteristics/Bedrooms.tex"}, "3a.tex")
    assert '<div id="table:hc_opt_bedrooms" data-source="characteristics/Bedrooms.tex">' in out
    assert '<div id="Tab:plain" data-source="3a.tex">' in out


# --- bibliography -----------------------------------------------------------------------------


def test_pandoc_is_told_the_registry_bibliography(tmp_path, monkeypatch):
    seen: dict = {}
    monkeypatch.setitem(sys.modules, "pypandoc", types.SimpleNamespace(get_pandoc_path=lambda: "pandoc"))

    def fake_run(args, **kwargs):
        seen["args"] = args
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    monkeypatch.setattr(L.subprocess, "run", fake_run)
    L._pandoc("x", tmp_path, True, "files/refs.bib")
    assert "--bibliography=files/refs.bib" in seen["args"]


def test_convert_resolves_citations_only_when_the_named_bibliography_exists(tmp_path, monkeypatch):
    (tmp_path / "ch.tex").write_text("\\chapter{X}\n", encoding="utf-8")
    calls: list[tuple[bool, str]] = []

    def fake_pandoc(text, cwd, citeproc, bibliography):
        calls.append((citeproc, bibliography))
        return SimpleNamespace(returncode=0, stdout="# X\n", stderr="")

    monkeypatch.setattr(L, "_pandoc", fake_pandoc)
    L._convert(tmp_path / "ch.tex", tmp_path, "files/refs.bib")
    assert calls == [(False, "files/refs.bib")]  # no such file: no citeproc attempt

    (tmp_path / "files").mkdir()
    (tmp_path / "files" / "refs.bib").write_text("", encoding="utf-8")
    calls.clear()
    L._convert(tmp_path / "ch.tex", tmp_path, "files/refs.bib")
    assert calls == [(True, "files/refs.bib")]


# --- PDF figures ------------------------------------------------------------------------------


def _blank_pdf(path, width=120, height=80):
    doc = pdfium.PdfDocument.new()
    doc.new_page(width, height)
    doc.save(str(path))
    doc.close()


def test_pdf_figures_are_rendered_to_png_and_the_reference_rewritten(tmp_path, monkeypatch):
    monkeypatch.setattr(L, "LATEX_PNG_CACHE", tmp_path / "cache")
    (tmp_path / "images").mkdir()
    _blank_pdf(tmp_path / "images" / "Figure 1.pdf")
    text = (
        "\\begin{figure}\n\\includegraphics[width=1\\linewidth]{images/Figure 1.pdf}\n"
        "\\caption{Flow}\n\\end{figure}\n"
        "\\includegraphics{images/missing.pdf}\n\\includegraphics{images/map.png}\n"
    )
    rasters: dict = {}

    out = L._rasterize_pdf_figures(text, tmp_path, rasters)

    assert "\\includegraphics[width=1\\linewidth]{images/Figure 1.png}" in out
    assert "{images/missing.pdf}" in out and "{images/map.png}" in out  # untouched
    assert list(rasters) == ["images/Figure 1.png"]
    png = rasters["images/Figure 1.png"].read_bytes()
    assert png[:8] == b"\x89PNG\r\n\x1a\n"
    assert struct.unpack(">II", png[16:24]) == (240, 160)  # page size at scale 2

    # the cache is keyed by the PDF's bytes, so a second pass renders nothing new
    before = rasters["images/Figure 1.png"].stat().st_mtime_ns
    L._rasterize_pdf_figures(text, tmp_path, {})
    assert rasters["images/Figure 1.png"].stat().st_mtime_ns == before


def test_load_latex_docs_threads_bibliography_and_rasters_to_convert(tmp_path, monkeypatch):
    proj = tmp_path / "docs" / "trg"
    proj.mkdir(parents=True)
    (proj / "main.tex").write_text("\\input{1_Intro.tex}\n", encoding="utf-8")
    (proj / "1_Intro.tex").write_text("\\chapter{Intro}\n", encoding="utf-8")
    seen: dict = {}

    def fake_convert(tex_path, cwd, bibliography, rasters):
        seen.update(bibliography=bibliography)
        rasters["images/Figure 1.png"] = tmp_path / "cache.png"
        return "# Intro\n\nbody\n", ""

    monkeypatch.setattr(L, "_convert", fake_convert)
    rasters: dict = {}
    docs, warnings = L.load_latex_docs(
        tmp_path, "docs/trg/main.tex", "resstock", "r", "tr", bibliography="files/refs.bib", rasters=rasters
    )
    assert [d.source_path for d in docs] == ["docs/trg/1_Intro.tex"]
    assert seen == {"bibliography": "files/refs.bib"}
    assert rasters == {"images/Figure 1.png": tmp_path / "cache.png"}
    assert warnings == []
