"""CORPUS_MAP.md is what an agent reads instead of opening 118 files, so the claims it
makes have to be true: every document listed, sections that say something the title does
not, measures routed to the file a reader can actually open, and a stale map called out
rather than trusted.

The map is derived from manifest.json + chunks.jsonl + crosswalk.json, so these tests
author those three by hand rather than running a build.
"""

from __future__ import annotations

import json

import buildstock_corpus.corpus_map as M
from buildstock_corpus.manifest import validate_manifest
from buildstock_corpus.paths import chunks_file, manifest_file, processed_root

RELEASE = "comstock_amy2018_2025_release_3"


def _write_manifest(artifacts: list[dict], **extra) -> dict:
    """A minimal manifest with one source, written where build_manifest would put it."""
    manifest = {
        "product": "comstock",
        "release": RELEASE,
        "generated_utc": "2026-01-01T00:00:00+00:00",
        "counts": {"documents": len(artifacts), "chunks": 0, "by_type": {}},
        "crosswalk": {"file": "crosswalk.json", "counts": None},
        "sources": [{"id": "technical_reference", "type": "latex", "artifacts": artifacts}],
        "gaps": {"measures": [], "unreachable_pdfs": [], "excluded_unpublished": {}},
        "warnings": [],
        **extra,
    }
    mf = manifest_file("comstock", RELEASE)
    mf.parent.mkdir(parents=True, exist_ok=True)
    mf.write_text(json.dumps(manifest, indent=2), encoding="utf-8", newline="\n")
    return manifest


def _artifact(source_path: str, title: str, output_path: str, **extra) -> dict:
    return {
        "source_path": source_path,
        "source_type": "latex",
        "title": title,
        "input_sha256": "a" * 64,
        "output_path": output_path,
        "output_sha256": "b" * 64,
        **extra,
    }


def _write_chunk_rows(rows: list[dict]) -> None:
    """chunks.jsonl carrying only the metadata the map reads."""
    cf = chunks_file("comstock", RELEASE)
    cf.parent.mkdir(parents=True, exist_ok=True)
    with cf.open("w", encoding="utf-8", newline="\n") as f:
        for i, meta in enumerate(rows):
            f.write(json.dumps({"id": f"c{i}", "text": "x", "metadata": meta}) + "\n")


def _meta(source_path: str, doc_title: str, section: str | None = None, **extra) -> dict:
    meta = {
        "product": "comstock",
        "release": RELEASE,
        "source_id": "technical_reference",
        "source_path": source_path,
        "source_type": "latex",
        "doc_title": doc_title,
        **extra,
    }
    if section is not None:
        meta["section"] = section
    return meta


def _map_text() -> str:
    return (processed_root("comstock", RELEASE) / M.MAP_FILENAME).read_text(encoding="utf-8")


def test_map_lists_every_document(workspace):
    _write_manifest(
        [
            _artifact("doc/a.tex", "Envelope", "technical_reference/doc/a.md"),
            _artifact("doc/b.tex", "Lighting", "technical_reference/doc/b.md"),
        ]
    )
    _write_chunk_rows(
        [
            _meta("doc/a.tex", "Envelope", "Envelope > Windows", date_last_updated="2025-09-04"),
            _meta("doc/b.tex", "Lighting", "Lighting > Fixtures"),
        ]
    )

    result = M.build_map("comstock", RELEASE)

    assert result["documents"] == 2
    text = _map_text()
    assert "technical_reference/doc/a.md" in text
    assert "technical_reference/doc/b.md" in text
    assert "2025-09-04" in text


def test_sections_skip_the_documents_own_title(workspace):
    """A LaTeX chapter's breadcrumbs all start with its title; repeating it says nothing."""
    _write_manifest([_artifact("doc/a.tex", "Envelope", "technical_reference/doc/a.md")])
    _write_chunk_rows(
        [
            _meta("doc/a.tex", "Envelope", "Envelope"),
            _meta("doc/a.tex", "Envelope", "Envelope > Windows"),
            _meta("doc/a.tex", "Envelope", "Envelope > Roofs > Insulation"),
        ]
    )

    M.build_map("comstock", RELEASE)

    row = next(ln for ln in _map_text().splitlines() if "doc/a.md" in ln)
    assert "Windows" in row
    assert "Roofs" in row
    # "Insulation" is a third-level heading -- the map routes to files, not within them.
    assert "Insulation" not in row


def test_document_without_sections_falls_back_to_its_title(workspace):
    """The two LaTeX appendices are flat data tables with no section metadata at all.

    An empty cell would read as "this document has no content", which is not what it means.
    """
    _write_manifest([_artifact("doc/appx.tex", "6_AppendixA", "technical_reference/doc/appx.md")])
    _write_chunk_rows([_meta("doc/appx.tex", "6_AppendixA")])

    M.build_map("comstock", RELEASE)

    row = next(ln for ln in _map_text().splitlines() if "doc/appx.md" in ln)
    cells = [c.strip() for c in row.split("|")]
    assert "6_AppendixA" in cells[3], f"sections cell was empty: {row}"


def test_map_is_written_with_lf_endings(workspace):
    """.gitattributes pins the checkout to LF; a CRLF map would differ by who generated it."""
    _write_manifest([_artifact("doc/a.tex", "Envelope", "technical_reference/doc/a.md")])
    _write_chunk_rows([_meta("doc/a.tex", "Envelope", "Envelope > Windows")])

    M.build_map("comstock", RELEASE)

    raw = (processed_root("comstock", RELEASE) / M.MAP_FILENAME).read_bytes()
    assert b"\r\n" not in raw


def test_pipe_in_a_title_does_not_break_the_table(workspace):
    _write_manifest([_artifact("doc/a.tex", "Cooling | Heating", "technical_reference/doc/a.md")])
    _write_chunk_rows([_meta("doc/a.tex", "Cooling | Heating", "Cooling | Heating > Chillers")])

    M.build_map("comstock", RELEASE)

    row = next(ln for ln in _map_text().splitlines() if "doc/a.md" in ln)
    assert "Cooling \\| Heating" in row
    # Count delimiters only: the escaped pipe inside the cell must not be one of them.
    assert row.replace("\\|", "").count("|") == 6, f"escaping changed the column count: {row}"


def test_sample_build_is_marked_as_partial(workspace):
    """A capped smoke-test map must not read as the record of a release."""
    _write_manifest(
        [_artifact("doc/a.tex", "Envelope", "technical_reference/doc/a.md")],
        sample={"per_category": 1, "partial": True},
    )
    _write_chunk_rows([_meta("doc/a.tex", "Envelope", "Envelope > Windows")])

    M.build_map("comstock", RELEASE)

    assert "SAMPLE" in _map_text()


def test_missing_manifest_is_an_error(workspace):
    import pytest

    with pytest.raises(FileNotFoundError, match="run `bsc build` first"):
        M.build_map("comstock", RELEASE)


# --- measure routing -------------------------------------------------------------------


def _write_crosswalk(measures: list[dict], gaps: list[dict] | None = None) -> None:
    cw = {
        "release": RELEASE,
        "counts": {"measures": len(measures), "covered": 0, "gaps": len(gaps or [])},
        "measures": measures,
        "gaps": gaps or [],
    }
    proot = processed_root("comstock", RELEASE)
    proot.mkdir(parents=True, exist_ok=True)
    (proot / "crosswalk.json").write_text(json.dumps(cw, indent=2), encoding="utf-8", newline="\n")


def test_external_pdf_measure_joins_on_filename(workspace):
    """A crosswalk target is a URL; the artifact records where fetch put the file."""
    _write_manifest(
        [_artifact("measure_pdfs/89340.pdf", "Load Shed", "upgrade_measures/measure_pdfs/89340.md")]
    )
    _write_chunk_rows([_meta("measure_pdfs/89340.pdf", "Load Shed", "Load Shed > Summary")])
    _write_crosswalk(
        [
            {
                "measure_id": "dr_0001",
                "documentation_name": "Thermostat Control for Load Shed",
                "doc_kind": "external_pdf",
                "doc_target": "https://www.nlr.gov/docs/fy24osti/89340.pdf",
                "upgrade_id": "32",
                "upgrade_name": "Demand Flexibility",
            }
        ]
    )

    M.build_map("comstock", RELEASE)

    row = next(ln for ln in _map_text().splitlines() if "dr_0001" in ln or "| 32 |" in ln)
    assert "upgrade_measures/measure_pdfs/89340.md" in row
    assert "not in corpus" not in row


def test_ambiguous_filename_is_not_linked(workspace):
    """Two upstream files sharing a name must not route a reader to an arbitrary one."""
    _write_manifest(
        [
            _artifact("a/report.pdf", "One", "upgrade_measures/a/report.md"),
            _artifact("b/report.pdf", "Two", "upgrade_measures/b/report.md"),
        ]
    )
    _write_chunk_rows([_meta("a/report.pdf", "One", "One > S")])
    _write_crosswalk(
        [
            {
                "measure_id": "dr_0002",
                "documentation_name": "Ambiguous",
                "doc_kind": "external_pdf",
                "doc_target": "https://example.gov/docs/report.pdf",
                "upgrade_id": "40",
                "upgrade_name": "Whatever",
            }
        ]
    )

    M.build_map("comstock", RELEASE)

    row = next(ln for ln in _map_text().splitlines() if "Ambiguous" in ln)
    assert "not in corpus" in row
    assert "upgrade_measures/a/report.md" not in row


def test_undocumented_measure_is_shown_as_a_gap(workspace):
    """Knowing a document was never written is an answer; silence sends an agent searching."""
    _write_manifest([_artifact("doc/a.tex", "Envelope", "technical_reference/doc/a.md")])
    _write_chunk_rows([_meta("doc/a.tex", "Envelope", "Envelope > Windows")])
    _write_crosswalk(
        [
            {
                "measure_id": "dr_0004",
                "documentation_name": "Undocumented Measure",
                "doc_kind": "none",
                "doc_target": None,
                "upgrade_id": "35",
                "upgrade_name": "Lighting Control",
            }
        ],
        gaps=[{"measure_id": "dr_0004"}],
    )

    M.build_map("comstock", RELEASE)

    row = next(ln for ln in _map_text().splitlines() if "Undocumented Measure" in ln)
    assert "gap" in row


# --- freshness -------------------------------------------------------------------------


def _map_errors(manifest: dict) -> list[str]:
    """Only the violations about the map; artifact hashes are covered by test_manifest."""
    errors = validate_manifest("comstock", RELEASE, manifest)
    return [e for e in errors if M.MAP_FILENAME in e]


def test_absent_map_is_not_a_violation(workspace):
    """The map is derived and regenerates in seconds; a clone without one is not broken."""
    manifest = _write_manifest([_artifact("doc/a.tex", "Envelope", "technical_reference/doc/a.md")])

    assert _map_errors(manifest) == []


def test_current_map_passes(workspace):
    manifest = _write_manifest([_artifact("doc/a.tex", "Envelope", "technical_reference/doc/a.md")])
    _write_chunk_rows([_meta("doc/a.tex", "Envelope", "Envelope > Windows")])
    M.build_map("comstock", RELEASE)

    assert _map_errors(manifest) == []


def test_stale_map_is_flagged(workspace):
    """Nothing else in validate would catch this: the map is not an artifact it walks."""
    manifest = _write_manifest([_artifact("doc/a.tex", "Envelope", "technical_reference/doc/a.md")])
    _write_chunk_rows([_meta("doc/a.tex", "Envelope", "Envelope > Windows")])
    M.build_map("comstock", RELEASE)

    # A rebuild that changes the corpus rewrites manifest.json; the map still describes the old one.
    manifest = _write_manifest(
        [
            _artifact("doc/a.tex", "Envelope", "technical_reference/doc/a.md"),
            _artifact("doc/new.tex", "Added Later", "technical_reference/doc/new.md"),
        ]
    )

    errors = _map_errors(manifest)
    assert len(errors) == 1
    assert "stale" in errors[0]
    assert "bsc map" in errors[0]


def test_map_without_a_stamp_is_flagged(workspace):
    """The header is the only thing making the map checkable; hand-editing it away is a break."""
    manifest = _write_manifest([_artifact("doc/a.tex", "Envelope", "technical_reference/doc/a.md")])
    proot = processed_root("comstock", RELEASE)
    proot.mkdir(parents=True, exist_ok=True)
    (proot / M.MAP_FILENAME).write_text("# hand-written map\n", encoding="utf-8", newline="\n")

    errors = _map_errors(manifest)
    assert len(errors) == 1
    assert "manifest_sha256" in errors[0]


def test_recorded_stamp_round_trips(workspace):
    _write_manifest([_artifact("doc/a.tex", "Envelope", "technical_reference/doc/a.md")])
    _write_chunk_rows([_meta("doc/a.tex", "Envelope", "Envelope > Windows")])

    result = M.build_map("comstock", RELEASE)

    assert M.recorded_manifest_sha256("comstock", RELEASE) == result["manifest_sha256"]
