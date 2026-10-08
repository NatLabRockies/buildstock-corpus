"""Chunk provenance — every chunk must carry release-aware metadata and a stable id,
so retrieval can filter by release and citations can point at a doc + section."""

from __future__ import annotations

from buildstock_corpus.chunk import chunk_document
from buildstock_corpus.normalize import Document

RELEASE = "comstock_amy2018_2025_release_3"

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
        release=RELEASE,
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
        assert c.metadata["release"] == RELEASE
        assert c.metadata["source_type"] == "latex"
        assert c.metadata["source_path"] == "documentation/reference_doc/4_9_hvac.tex"
        assert c.metadata["doc_title"] == "HVAC Systems"

    # deepest section keeps its heading text in the chunk body for retrieval context
    assert "Heat Pumps" in chunks[2].text
    assert "heating and cooling" in chunks[2].text


def test_chunk_carries_the_documents_status_and_omits_it_when_unset():
    """Retrieval filters and citation guidance key on status, so every chunk carries it;
    None is omitted rather than written, because Chroma metadata cannot hold it."""
    for c in chunk_document(_doc(status="site_page")):
        assert c.metadata["status"] == "site_page"
    for c in chunk_document(_doc()):
        assert "status" not in c.metadata


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
    assert chunks[0].metadata["release"] == RELEASE


# --- where a chunk sits: line range and build ----------------------------------------------


def _slice(body: str, c, line_offset: int = 1) -> str:
    lines = body.split("\n")
    return "\n".join(lines[c.metadata["line_start"] - line_offset : c.metadata["line_end"] - line_offset + 1])


def test_chunk_line_ranges_slice_back_to_the_chunks_own_paragraphs():
    """line_start/line_end name the whole paragraphs a chunk draws from, in file lines
    (default offset: body index 0 is line 1), so `sed -n a,bp` re-reads exactly them."""
    chunks = chunk_document(_doc())
    for c in chunks:
        core = c.text.split("\n\n", 1)[1]  # drop the "title — breadcrumb" header line
        assert _slice(BODY, c) == core
    assert [(c.metadata["line_start"], c.metadata["line_end"]) for c in chunks] == [(3, 3), (7, 7), (11, 11)]


def test_overlap_tail_and_hard_split_do_not_stretch_the_range():
    long_para = "x" * 50
    body = "# T\n\n## A\n\n" + "\n\n".join(f"p{i} " + long_para for i in range(6)) + "\n"
    chunks = chunk_document(_doc(body=body), max_chars=130, overlap_chars=20)
    lines = body.split("\n")
    assert len(chunks) > 1
    for c in chunks:
        covered = "\n".join(lines[c.metadata["line_start"] - 1 : c.metadata["line_end"]])
        core = c.text.split("\n\n", 1)[1]
        # the chunk's last paragraph is never overlap; it must lie within the range
        assert core.split("\n\n")[-1] in covered
        # the range holds only whole paragraphs that the chunk's text actually contains
        for para in covered.split("\n\n"):
            assert para in core
    # a paragraph longer than max_chars is split, and every piece keeps the paragraph's lines
    big = chunk_document(_doc(body="# T\n\n" + "y" * 300 + "\n"), max_chars=100, overlap_chars=0)
    assert len(big) == 3 and {(c.metadata["line_start"], c.metadata["line_end"]) for c in big} == {(3, 3)}


def test_line_offset_shifts_every_range_and_corpus_version_is_carried():
    plain = chunk_document(_doc())
    shifted = chunk_document(_doc(), corpus_version="comstock_amy2018_2025_release_3-v1", line_offset=4)
    for a, b in zip(plain, shifted):
        assert b.metadata["line_start"] == a.metadata["line_start"] + 3
        assert b.metadata["line_end"] == a.metadata["line_end"] + 3
        assert b.metadata["corpus_version"] == "comstock_amy2018_2025_release_3-v1"
        assert "corpus_version" not in a.metadata
        assert a.id == b.id and a.text == b.text  # ids and texts are untouched by either
