"""Chunk provenance — every chunk must carry release-aware metadata and a stable id,
so retrieval can filter by release and citations can point at a doc + section."""

from __future__ import annotations

from buildstock_corpus.chunk import chunk_document
from buildstock_corpus.normalize import Document

BODY = """\
# HVAC Systems

Intro paragraph about HVAC in ComStock.

## System Types

RTU and heat pumps are the common baseline system types.

### Heat Pumps

Heat pumps provide both heating and cooling.
"""


def _doc(**over) -> Document:
    kw = dict(
        product="comstock",
        release="2025-3",
        source_id="technical_reference",
        source_type="latex",
        source_path="documentation/reference_doc/4_9_hvac.tex",
        title="HVAC Systems",
        body=BODY,
    )
    kw.update(over)
    return Document(**kw)


def test_chunk_metadata_and_breadcrumbs():
    chunks = chunk_document(_doc())

    # one chunk per (single-paragraph) heading section
    assert len(chunks) == 3
    assert [c.metadata["section"] for c in chunks] == [
        "HVAC Systems",
        "HVAC Systems > System Types",
        "HVAC Systems > System Types > Heat Pumps",
    ]

    # provenance carried on every chunk, tagged to the release
    for c in chunks:
        assert c.metadata["product"] == "comstock"
        assert c.metadata["release"] == "2025-3"
        assert c.metadata["source_type"] == "latex"
        assert c.metadata["source_path"] == "documentation/reference_doc/4_9_hvac.tex"
        assert c.metadata["doc_title"] == "HVAC Systems"

    # deepest section keeps its heading text in the chunk body for retrieval context
    assert "Heat Pumps" in chunks[2].text
    assert "heating and cooling" in chunks[2].text


def test_chunk_ids_unique_and_ordered():
    chunks = chunk_document(_doc())
    ids = [c.id for c in chunks]
    assert ids == [
        "technical_reference|documentation/reference_doc/4_9_hvac.tex|0",
        "technical_reference|documentation/reference_doc/4_9_hvac.tex|1",
        "technical_reference|documentation/reference_doc/4_9_hvac.tex|2",
    ]
    assert len(set(ids)) == len(ids)


def test_chunk_folds_measure_identity_and_drops_none_extra():
    doc = _doc(
        source_id="upgrade_measures",
        source_type="measures",
        extra={"measure_id": "env_0002", "measure_name": "Roof Insulation", "url": None},
    )
    chunks = chunk_document(doc)
    assert chunks, "expected at least one chunk"
    md = chunks[0].metadata
    # measure identity flows into chunk metadata so answers can cite the measure...
    assert md["measure_id"] == "env_0002"
    assert md["measure_name"] == "Roof Insulation"
    # ...but None-valued extras are dropped (Chroma metadata rejects null values)
    assert "url" not in md


def test_chunk_body_without_headings():
    doc = _doc(body="A flat document with no markdown headings at all.\n")
    chunks = chunk_document(doc)
    assert len(chunks) == 1
    assert chunks[0].metadata["section"] == ""
    assert chunks[0].metadata["release"] == "2025-3"
