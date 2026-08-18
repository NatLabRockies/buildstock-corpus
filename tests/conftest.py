"""Shared fixtures for the index/query tests: a tmp workspace with the embedder faked.

Loading bge-small would dominate the runtime of tests that are really about the store's
lifecycle and retrieval's plumbing, so both stages get a stub embedder here. The Chroma
store itself stays real — the file-locking behavior these tests pin only appears against
the actual segment files.
"""

from __future__ import annotations

import json

import pytest

import buildstock_corpus.index as I
import buildstock_corpus.query as Q
from buildstock_corpus.paths import chunks_file, use_workspace

RELEASE = "comstock_amy2018_2025_release_3"

DIM = 8


class _FakeVec(list):
    """Stands in for the ndarray fastembed yields; the callers only need .tolist()."""

    def tolist(self) -> list[float]:
        return list(self)


class FakeEmbedder:
    def embed(self, texts, batch_size=None):
        # Deterministic and text-dependent, so distinct chunks get distinct vectors.
        for text in texts:
            yield _FakeVec([float(len(text) % 7)] + [0.0] * (DIM - 1))

    def query_embed(self, texts, **kwargs):
        return self.embed(texts)


@pytest.fixture
def write_chunks():
    """Author a chunks.jsonl with `count` chunks in the active workspace."""

    def _write(product: str, release: str, count: int) -> None:
        cf = chunks_file(product, release)
        cf.parent.mkdir(parents=True, exist_ok=True)
        with cf.open("w", encoding="utf-8") as f:
            for i in range(count):
                f.write(
                    json.dumps(
                        {
                            "id": f"chunk-{i}",
                            "text": f"passage {i} " + "x" * i,
                            "metadata": {"source_id": "technical_reference", "ordinal": i},
                        }
                    )
                    + "\n"
                )

    return _write


@pytest.fixture
def workspace(tmp_path, monkeypatch):
    """Point derived outputs at a tmp dir and stub out the real embedding model."""
    monkeypatch.setattr(I, "_embedder", lambda: FakeEmbedder())
    monkeypatch.setattr(Q, "_embedder", lambda: FakeEmbedder())
    use_workspace(tmp_path)
    yield tmp_path
    use_workspace(None)


@pytest.fixture
def indexed(workspace, write_chunks):
    """A small real Chroma store, already built, in a tmp workspace."""
    write_chunks("comstock", RELEASE, 4)
    I.build_index("comstock", RELEASE, batch_size=2)
    return workspace
