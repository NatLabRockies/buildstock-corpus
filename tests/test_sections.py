"""Section files are what a consumer fetches instead of a 437 KB document, so the contract
is pinned here: one file per H2 plus a 00- preamble, tiling the document from line 2 so the
concatenation reproduces it; a citable line-1 header naming the parent and the line range;
short, predictable names; and validate regenerating them to catch a missing, changed or
extra one.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from buildstock_corpus import sections as S
from buildstock_corpus.provenance import parse_header, render_header

RELEASE = "comstock_amy2018_2025_release_3"
HEADER = render_header(
    "comstock", RELEASE, "technical_reference", "documentation/reference_doc/4_4_geometry.tex",
    status="site_page", source_url="https://github.com/x/y/blob/abc/4_4_geometry.tex",
    publication_url="https://example.org/ref.pdf", corpus_version=f"{RELEASE}-v1",
)
DOC = HEADER + (
    "# Geometry\n\nIntro paragraph.\n\n## Floor Height\n\nFour metres.\n\n### Detail | note\n\nMore.\n\n"
    "## Rotation\n\nText.\n\n## References\n\n[1] a\n"
)
PATH = "technical_reference/documentation/reference_doc/4_4_geometry.md"


def test_plan_one_file_per_h2_plus_preamble_with_short_predictable_names():
    plans = S.plan_sections(PATH, DOC)
    assert [(p.name, p.level, p.line_start, p.line_end) for p in plans] == [
        ("00-geometry", 1, 2, 5),
        ("01-floor-height", 2, 6, 13),  # the H3 "Detail" rides inside its H2
        ("02-rotation", 2, 14, 17),
        ("03-references", 2, 18, 20),
    ]
    assert plans[1].file == "sections/technical_reference/documentation/reference_doc/4_4_geometry/01-floor-height.md"


def test_sections_tile_the_document_from_line_two():
    rendered = S.render_sections(PATH, DOC)
    bodies = [content.split("\n", 1)[1] for content in rendered.values()]  # drop each header
    assert "".join(bodies) == DOC.split("\n", 1)[1]  # the document minus its own header


def test_section_header_carries_the_documents_provenance_plus_its_place():
    rendered = S.render_sections(PATH, DOC)
    content = rendered["sections/technical_reference/documentation/reference_doc/4_4_geometry/01-floor-height.md"]
    first, rest = content.split("\n", 1)
    h = parse_header(first)
    assert h["source_path"] == "documentation/reference_doc/4_4_geometry.tex"
    assert h["status"] == "site_page" and h["corpus_version"] == f"{RELEASE}-v1"
    assert h["publication_url"] == "https://example.org/ref.pdf"
    assert h["corpus_path"] == PATH and h["section"] == "Floor Height" and h["lines"] == "6-13"
    assert rest.startswith("## Floor Height\n") and "### Detail | note" in rest


def test_a_pipe_in_a_heading_cannot_break_the_header():
    doc = HEADER + "# T\n\n## A | B --> C\n\nx\n"
    rendered = S.render_sections("t/x.md", doc)
    assert list(rendered) == ["sections/t/x/01-a-b-c.md"]  # a bare title line yields no 00- file
    content = rendered["sections/t/x/01-a-b-c.md"]
    assert parse_header(content.split("\n", 1)[0])["section"] == "A / B -- C"


def test_document_without_h2_yields_only_the_preamble_file():
    doc = HEADER + "# Only Title\n\nSome prose.\n\n### Deep\n\nMore.\n"
    plans = S.plan_sections("t/x.md", doc)
    assert [(p.name, p.line_start, p.line_end) for p in plans] == [("00-only-title", 2, 8)]


def test_slug_is_capped_and_never_empty():
    assert len(S.slugify("x" * 100)) == S.MAX_SLUG
    assert S.slugify("!!!") == "section"
    assert S.slugify("Window-to-Wall Ratio (WWR)") == "window-to-wall-ratio-wwr"


def test_write_then_check_is_clean_and_tampering_is_caught(tmp_path):
    proot = tmp_path
    assert S.check_sections(proot, PATH, DOC, "w") == ([], 0, False)  # nothing written yet
    plans = S.write_sections(proot, PATH, DOC)
    assert len(plans) == 4
    assert S.check_sections(proot, PATH, DOC, "w") == ([], 4, True)

    target = proot / plans[2].file
    target.write_text(target.read_text(encoding="utf-8") + "tampered\n", encoding="utf-8")
    (proot / S.sections_dir(PATH) / "99-extra.md").write_text("x\n", encoding="utf-8")
    (proot / plans[0].file).unlink()
    errors, n, present = S.check_sections(proot, PATH, DOC, "w")
    assert n == 4 and present
    assert sorted(e.split(": ", 1)[1].split(":")[0] for e in errors) == [
        "section file differs from its document", "section file missing",
        "section file not produced by its document",
    ]


def test_rewriting_replaces_stale_files_and_orphans_are_found(tmp_path):
    proot = tmp_path
    S.write_sections(proot, PATH, DOC)
    S.write_sections(proot, PATH, HEADER + "# Geometry\n\n## Only One\n\nx\n")  # headings changed
    assert sorted(p.name for p in Path(proot / S.sections_dir(PATH)).glob("*.md")) == ["01-only-one.md"]

    other = "github_site/docs/gone.md"
    S.write_sections(proot, other, HEADER + "# Gone\n\n## A\n\nx\n")
    assert S.orphan_section_files(proot, [PATH]) == [
        "sections/github_site/docs/gone/01-a.md",
    ]
    assert S.orphan_section_files(proot, [PATH, other]) == []


def test_render_refuses_a_document_without_a_header():
    with pytest.raises(ValueError, match="not a provenance header"):
        S.render_sections("t/x.md", "# No header\n\n## A\n\nx\n")
