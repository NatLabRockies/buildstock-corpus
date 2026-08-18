"""Retrieval: hits carry full provenance, and reading does not leave the store locked.

Embedders are faked via conftest, so these cover retrieval's plumbing rather than
embedding quality. The store itself is real Chroma — the locking behavior only shows up
against the actual segment files.
"""

from __future__ import annotations

import shutil

import pytest

import buildstock_corpus.index as I
import buildstock_corpus.query as Q
from buildstock_corpus.paths import chunks_file, index_root, use_workspace

RELEASE = "comstock_amy2018_2025_release_3"


def test_search_returns_k_hits_with_provenance(indexed):
    hits = Q.search("comstock", RELEASE, "hvac system type", k=2)

    assert len(hits) == 2
    for h in hits:
        assert h["metadata"]["source_id"] == "technical_reference"
        assert isinstance(h["score"], float)
        assert h["text"]


def test_search_does_not_leave_the_store_locked(indexed):
    """A leaked client keeps the segment files mmapped, so the next `bsc index` for this
    release cannot replace the store — on Windows the rmtree fails outright."""
    Q.search("comstock", RELEASE, "hvac system type", k=1)

    idx_dir = index_root("comstock", RELEASE)
    shutil.rmtree(idx_dir)  # stands in for the rmtree at the top of build_index
    assert not idx_dir.exists()


def test_index_can_replace_a_store_that_was_just_queried(indexed, write_chunks):
    """The end-to-end version of the above: query, then re-index, in one process."""
    Q.search("comstock", RELEASE, "hvac system type", k=1)

    write_chunks("comstock", RELEASE, 2)
    result = I.build_index("comstock", RELEASE, batch_size=2)

    assert result["chunks"] == 2
    assert Q.search("comstock", RELEASE, "hvac system type", k=2)


def test_search_requires_an_index(tmp_path):
    use_workspace(tmp_path)
    try:
        with pytest.raises(FileNotFoundError, match="bsc index"):
            Q.search("comstock", RELEASE, "anything")
    finally:
        use_workspace(None)


def test_format_hits_cites_source_and_section(indexed):
    hits = Q.search("comstock", RELEASE, "hvac system type", k=1)
    hits[0]["metadata"].update(
        {
            "source_path": "measure_pdfs/89040.pdf",
            "section": "2  Baseline",
            "product": "comstock",
            "release": RELEASE,
        }
    )

    out = Q.format_hits(hits)

    assert "technical_reference/measure_pdfs/89040.pdf § 2  Baseline" in out
    assert f"(comstock {RELEASE})" in out


def test_chunks_file_is_untouched_by_search(indexed):
    """Guard against retrieval ever writing into processed/ — it is read-only by design."""
    before = chunks_file("comstock", RELEASE).read_bytes()
    Q.search("comstock", RELEASE, "hvac system type", k=1)
    assert chunks_file("comstock", RELEASE).read_bytes() == before
