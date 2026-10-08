"""index.json and sections.json are what a consumer without a clone codes against, so the
contract is pinned here: both validate against their schemas, every document and measure is
listed, section line ranges slice back to exactly the heading's text, and a file generated
from a manifest that has since moved on is reported stale by validate.
"""

from __future__ import annotations

import json

import pytest

import buildstock_corpus.corpus_index as X
from buildstock_corpus.manifest import validate_manifest
from buildstock_corpus.paths import manifest_file, processed_root

RELEASE = "comstock_amy2018_2025_release_3"
SITE = "https://natlabrockies.github.io/ComStock.github.io"

DOC_A = (
    f"<!-- comstock {RELEASE} | technical_reference | doc/a.tex | status: site_page"
    f" | source_url: https://github.com/x/y/blob/abc/doc/a.tex | publication_url: {SITE}/ref.pdf"
    " | corpus_version: test-v1 -->\n"
    "# Geometry\n\nIntro.\n\n## Floor Height\n\nFloor-to-floor height is 4 m.\n\n"
    "### Detail\n\nMore.\n\n## Rotation\n\nText.\n"
)
DOC_B = (
    f"<!-- comstock {RELEASE} | upgrade_measures | measure_pdfs/89340.pdf | status: osti_pdf"
    " | source_url: https://www.nlr.gov/docs/fy24osti/89340.pdf"
    " | publication_url: https://www.nlr.gov/docs/fy24osti/89340.pdf | corpus_version: test-v1 -->\n"
    "# Load Shed\n\nNo further headings.\n"
)


def _artifact(src_id, source_path, title, out, status, url):
    return {
        "source_path": source_path, "source_type": "x", "status": status, "source_url": url,
        "publication_url": url if status == "osti_pdf" else f"{SITE}/ref.pdf",
        "corpus_version": "test-v1", "title": title, "input_sha256": "a" * 64,
        "output_path": out, "output_sha256": "b" * 64,
    }


@pytest.fixture
def built(workspace):
    """A two-document release with a crosswalk, written where a build would put it."""
    proot = processed_root("comstock", RELEASE)
    for rel, text in (("technical_reference/doc/a.md", DOC_A), ("upgrade_measures/measure_pdfs/89340.md", DOC_B)):
        p = proot / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8", newline="\n")
    manifest = {
        "product": "comstock", "release": RELEASE, "corpus_version": "test-v1",
        "generated_utc": "2026-01-01T00:00:00+00:00",
        "counts": {"documents": 2, "chunks": 0, "by_type": {}},
        "crosswalk": {"file": "crosswalk.json", "counts": None},
        "sources": [
            {"id": "technical_reference", "type": "latex", "artifacts": [
                _artifact("technical_reference", "doc/a.tex", "Geometry", "technical_reference/doc/a.md",
                          "site_page", "https://github.com/x/y/blob/abc/doc/a.tex")]},
            {"id": "upgrade_measures", "type": "measures", "artifacts": [
                _artifact("upgrade_measures", "measure_pdfs/89340.pdf", "Load Shed",
                          "upgrade_measures/measure_pdfs/89340.md", "osti_pdf",
                          "https://www.nlr.gov/docs/fy24osti/89340.pdf")]},
        ],
        "gaps": {"measures": ["dr_0004"], "unreachable_pdfs": [], "excluded_unpublished": {}},
        "warnings": [],
    }
    manifest_file("comstock", RELEASE).write_text(json.dumps(manifest, indent=2), encoding="utf-8", newline="\n")
    (proot / "crosswalk.json").write_text(json.dumps({
        "release": RELEASE, "counts": {"measures": 2, "covered": 1, "gaps": 1},
        "measures": [
            {"measure_id": "dr_0001", "documentation_name": "Load Shed", "doc_kind": "external_pdf",
             "doc_target": "https://www.nlr.gov/docs/fy24osti/89340.pdf",
             "corpus_path": "upgrade_measures/measure_pdfs/89340.md",
             "doc_url": "https://www.nlr.gov/docs/fy24osti/89340.pdf", "status": "osti_pdf",
             "upgrade_id": "32", "upgrade_name": "Demand Flexibility", "in_release": True},
            {"measure_id": "dr_0004", "documentation_name": "Undocumented", "doc_kind": "none",
             "doc_target": None, "corpus_path": None, "doc_url": None, "status": "missing",
             "upgrade_id": "35", "upgrade_name": "Lighting Control", "in_release": True},
        ],
        "gaps": [{"measure_id": "dr_0004", "reason": "documentation expected soon"}],
    }), encoding="utf-8", newline="\n")
    return proot, manifest


def _load(proot, name):
    return json.loads((proot / name).read_text(encoding="utf-8"))


def test_index_lists_every_document_and_measure_and_validates(built):
    proot, _ = built
    result = X.build_index("comstock", RELEASE)

    index = _load(proot, X.INDEX_FILENAME)
    assert X.check_schema(index, X.INDEX_SCHEMA) == []
    assert index["counts"] == {"documents": 2, "measures": 2}
    assert index["corpus_version"] == "test-v1"
    assert index["manifest_sha256"] == result["manifest_sha256"]
    by_path = {d["corpus_path"]: d for d in index["documents"]}
    a = by_path["technical_reference/doc/a.md"]
    assert a["title"] == "Geometry" and a["status"] == "site_page"
    assert a["sections"] == 4  # H1 + two H2 + one H3
    assert a["bytes"] == (proot / "technical_reference/doc/a.md").stat().st_size
    assert a["publication_url"] == f"{SITE}/ref.pdf"
    by_id = {m["measure_id"]: m for m in index["measures"]}
    assert by_id["dr_0001"]["corpus_path"] == "upgrade_measures/measure_pdfs/89340.md"
    assert by_id["dr_0001"]["upgrade_id"] == "32"
    assert by_id["dr_0004"] == {"measure_id": "dr_0004", "upgrade_id": "35", "upgrade_name": "Lighting Control",
                                "corpus_path": None, "doc_url": None, "status": "missing"}
    assert set(by_id["dr_0001"]) == set(X._MEASURE_FIELDS)  # nothing extra leaks in


def test_section_line_ranges_slice_back_to_the_heading_and_tile_the_file(built):
    proot, _ = built
    X.build_index("comstock", RELEASE)

    sections = _load(proot, X.SECTIONS_FILENAME)
    assert X.check_schema(sections, X.SECTIONS_SCHEMA) == []
    secs = sections["documents"]["technical_reference/doc/a.md"]
    lines = (proot / "technical_reference/doc/a.md").read_text(encoding="utf-8").split("\n")
    assert [(s["heading"], s["level"]) for s in secs] == [
        ("Geometry", 1), ("Floor Height", 2), ("Detail", 3), ("Rotation", 2)]
    for s in secs:
        assert lines[s["line_start"] - 1].lstrip("#").strip() == s["heading"]
        assert s["line_end"] >= s["line_start"]
    # consecutive sections tile the file: each ends right before the next begins
    assert all(secs[i]["line_end"] + 1 == secs[i + 1]["line_start"] for i in range(len(secs) - 1))
    assert secs[-1]["line_end"] == len(lines) - 1  # last real line, not the trailing newline
    floor = next(s for s in secs if s["heading"] == "Floor Height")
    assert "Floor-to-floor height is 4 m." in "\n".join(lines[floor["line_start"] - 1:floor["line_end"]])
    assert sections["documents"]["upgrade_measures/measure_pdfs/89340.md"] == [
        {"heading": "Load Shed", "level": 1, "line_start": 2, "line_end": 4,
         "file": "sections/upgrade_measures/measure_pdfs/89340/00-load-shed.md"}]


def test_index_is_compact_and_lf(built):
    proot, _ = built
    X.build_index("comstock", RELEASE)
    raw = (proot / X.INDEX_FILENAME).read_bytes()
    assert b"\r\n" not in raw and raw.endswith(b"\n")
    assert b"\n" not in raw[:-1]  # one line: compact JSON, every byte is on the wire


def test_validate_accepts_fresh_index_files_and_flags_stale_ones(built):
    proot, manifest = built
    X.build_index("comstock", RELEASE)
    assert [e for e in validate_manifest("comstock", RELEASE, manifest) if "index.json" in e or "sections.json" in e] == []

    # the manifest moves on (a rebuild) and the index files do not
    manifest["warnings"] = ["something changed"]
    manifest_file("comstock", RELEASE).write_text(json.dumps(manifest, indent=2), encoding="utf-8", newline="\n")
    errors = validate_manifest("comstock", RELEASE, manifest)
    stale = [e for e in errors if "stale" in e and ("index.json" in e or "sections.json" in e)]
    assert len(stale) == 2 and all("bsc map" in e for e in stale)


def test_validate_flags_an_off_schema_index(built):
    proot, manifest = built
    X.build_index("comstock", RELEASE)
    index = _load(proot, X.INDEX_FILENAME)
    index["documents"][0]["status"] = "draft_pdf"  # not in the vocabulary
    del index["documents"][1]["bytes"]
    (proot / X.INDEX_FILENAME).write_text(json.dumps(index), encoding="utf-8")

    errors = [e for e in validate_manifest("comstock", RELEASE, manifest) if "index.json" in e]
    assert len(errors) == 1 and "index.schema.json" in errors[0]
    assert "documents/0/status" in errors[0] and "documents/1" in errors[0]


def test_absent_index_files_are_not_a_violation(built):
    proot, manifest = built
    assert [e for e in validate_manifest("comstock", RELEASE, manifest) if "index" in e or "sections" in e] == []


def test_document_sections_handles_headings_without_body_and_trailing_hashes():
    text = "# T\n## A ##\n## B\nx\n"
    assert X.document_sections(text) == [
        {"heading": "T", "level": 1, "line_start": 1, "line_end": 1},
        {"heading": "A", "level": 2, "line_start": 2, "line_end": 2},
        {"heading": "B", "level": 2, "line_start": 3, "line_end": 4},
    ]
    assert X.document_sections("no headings\n") == []


def test_sections_json_names_a_file_for_every_h2_and_the_preamble(built):
    proot, _ = built
    X.build_index("comstock", RELEASE)

    sections = _load(proot, X.SECTIONS_FILENAME)
    assert X.check_schema(sections, X.SECTIONS_SCHEMA) == []
    secs = sections["documents"]["technical_reference/doc/a.md"]
    files = {s["heading"]: s.get("file") for s in secs}
    assert files["Geometry"] == "sections/technical_reference/doc/a/00-geometry.md"  # preamble: "Intro."
    assert files["Floor Height"] == "sections/technical_reference/doc/a/01-floor-height.md"
    assert files["Rotation"] == "sections/technical_reference/doc/a/02-rotation.md"
    assert files["Detail"] is None  # an H3 is read inside its H2's file
    # a document with no H2 gets only the preamble file, which is the whole document
    only = sections["documents"]["upgrade_measures/measure_pdfs/89340.md"]
    assert [s.get("file") for s in only] == ["sections/upgrade_measures/measure_pdfs/89340/00-load-shed.md"]
