"""Per-document chunk files are byte-exact slices of chunks.jsonl under the same flat address
as the section files, one per document (empty when a document has no chunks), reproducing
chunks.jsonl when concatenated in manifest order; validate regenerates and compares."""

from __future__ import annotations

import json

import pytest

from buildstock_corpus import chunk_files as C

MANIFEST = {"sources": [
    {"id": "technical_reference", "artifacts": [
        {"source_path": "documentation/reference_doc/4_4_geometry.tex",
         "output_path": "technical_reference/documentation/reference_doc/4_4_geometry.md"},
        {"source_path": "documentation/reference_doc/0_3_acronyms.tex",
         "output_path": "technical_reference/documentation/reference_doc/0_3_acronyms.md"}]},
    {"id": "upgrade_measures", "artifacts": [
        {"source_path": "measure_pdfs/89340.pdf", "output_path": "upgrade_measures/measure_pdfs/89340.md"}]},
]}


def _row(sid, sp, n):
    return json.dumps({"id": f"{sid}|{sp}|{n}", "text": f"t{n}", "metadata": {"source_id": sid, "source_path": sp}}) + "\n"


CHUNKS = (
    _row("technical_reference", "documentation/reference_doc/4_4_geometry.tex", 0)
    + _row("upgrade_measures", "measure_pdfs/89340.pdf", 0)
    + _row("technical_reference", "documentation/reference_doc/4_4_geometry.tex", 1)
)


def test_files_are_flat_by_source_and_slices_are_byte_exact():
    files = C.split_chunks(CHUNKS, MANIFEST)
    assert set(files) == {
        "chunks/technical_reference/4_4_geometry.jsonl",
        "chunks/technical_reference/0_3_acronyms.jsonl",
        "chunks/upgrade_measures/89340.jsonl",
    }
    geo = files["chunks/technical_reference/4_4_geometry.jsonl"]
    assert geo == CHUNKS.splitlines(keepends=True)[0] + CHUNKS.splitlines(keepends=True)[2]
    assert files["chunks/technical_reference/0_3_acronyms.jsonl"] == ""  # no chunks: empty, but present
    # concatenating in manifest order reproduces chunks.jsonl up to row order within the file set
    assert sorted(("".join(files.values())).splitlines()) == sorted(CHUNKS.splitlines())


def test_a_chunk_for_an_unlisted_document_is_an_error():
    with pytest.raises(ValueError, match="does not list"):
        C.split_chunks(_row("github_site", "docs/x.md", 0), MANIFEST)


def test_counts_feed_the_index():
    assert C.chunk_counts(CHUNKS) == {
        ("technical_reference", "documentation/reference_doc/4_4_geometry.tex"): 2,
        ("upgrade_measures", "measure_pdfs/89340.pdf"): 1,
    }
    assert C.chunks_file_for("upgrade_measures/unpublished_docs/upgrade_measures/env_window_film.md") == (
        "chunks/upgrade_measures/env_window_film.jsonl"
    )


def test_write_then_check_is_clean_and_tampering_is_caught(tmp_path):
    assert C.check_chunk_files(tmp_path, MANIFEST, CHUNKS) == ([], 0, False)  # absent tree: derived
    assert C.write_chunk_files(tmp_path, MANIFEST, CHUNKS) == 3
    assert C.check_chunk_files(tmp_path, MANIFEST, CHUNKS) == ([], 3, True)

    (tmp_path / "chunks/upgrade_measures/89340.jsonl").write_text("{}\n", encoding="utf-8")
    (tmp_path / "chunks/technical_reference/0_3_acronyms.jsonl").unlink()
    (tmp_path / "chunks/github_site").mkdir()
    (tmp_path / "chunks/github_site/stale.jsonl").write_text("", encoding="utf-8")
    errors, n, present = C.check_chunk_files(tmp_path, MANIFEST, CHUNKS)
    assert n == 3 and present
    assert sorted(e.split(": ")[1] for e in errors) == [
        "file belongs to no document in this manifest",
        "file differs from its slice of chunks.jsonl",
        "file missing",
    ]
    # a rewrite replaces the whole tree, stale file included
    C.write_chunk_files(tmp_path, MANIFEST, CHUNKS)
    assert C.check_chunk_files(tmp_path, MANIFEST, CHUNKS) == ([], 3, True)
