"""Indexing rebuilds the store in place: a rebuild must not strand the previous build's
vectors on disk, and the resulting collection must hold exactly what chunks.jsonl holds.

The embedder is faked via conftest — this covers the store's lifecycle, not embedding
quality.
"""

from __future__ import annotations

import pytest

import buildstock_corpus.index as I
from buildstock_corpus.paths import index_root


def _segment_dirs(idx_dir) -> list[str]:
    """Chroma's per-collection HNSW segment dirs (UUID-named), which used to accumulate."""
    return sorted(p.name for p in idx_dir.iterdir() if p.is_dir())


def test_index_reports_every_chunk(workspace, write_chunks):
    write_chunks("comstock", "2025-3", 5)

    result = I.build_index("comstock", "2025-3", batch_size=2)

    assert result["chunks"] == 5
    assert result["collection"] == "comstock_2025-3"
    assert result["index_dir"] == str(index_root("comstock", "2025-3"))


def test_rebuild_discards_the_previous_store(workspace, write_chunks):
    """The bug this guards: delete_collection left the old segment dir (and its vectors)
    behind, so every rebuild added another copy of the release to disk."""
    write_chunks("comstock", "2025-3", 4)
    I.build_index("comstock", "2025-3", batch_size=2)

    idx_dir = index_root("comstock", "2025-3")
    first = _segment_dirs(idx_dir)
    assert first, "expected the first build to write a segment dir"
    stale_marker = idx_dir / first[0] / "data_level0.bin"
    assert stale_marker.exists()

    I.build_index("comstock", "2025-3", batch_size=2)

    second = _segment_dirs(idx_dir)
    assert len(second) == len(first), f"segment dirs accumulated: {first} -> {second}"
    assert not stale_marker.exists(), "the previous build's vectors survived the rebuild"


def test_rebuild_drops_chunks_that_are_gone(workspace, write_chunks):
    """A shrinking chunks.jsonl must shrink the collection — no orphaned ids left behind."""
    import chromadb

    write_chunks("comstock", "2025-3", 6)
    I.build_index("comstock", "2025-3", batch_size=4)
    write_chunks("comstock", "2025-3", 2)
    I.build_index("comstock", "2025-3", batch_size=4)

    client = chromadb.PersistentClient(path=str(index_root("comstock", "2025-3")))
    try:
        coll = client.get_collection("comstock_2025-3")
        assert coll.count() == 2
        assert sorted(coll.get()["ids"]) == ["chunk-0", "chunk-1"]
    finally:
        # Leaving it open would keep the segment files mmapped, and pytest's later cleanup
        # of this tmp_path would fail on Windows.
        client.close()


def test_index_refuses_an_empty_chunks_file(workspace, write_chunks):
    write_chunks("comstock", "2025-3", 0)
    with pytest.raises(ValueError, match="empty"):
        I.build_index("comstock", "2025-3")


def test_index_requires_a_build_first(workspace):
    with pytest.raises(FileNotFoundError, match="bsc build"):
        I.build_index("comstock", "2025-3")
