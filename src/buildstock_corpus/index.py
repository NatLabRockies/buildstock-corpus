"""Embed chunks.jsonl into a persistent Chroma collection (one per product+release).

Embeddings are local/offline via fastembed (bge-small-en-v1.5, ONNX, no torch). The
collection is rebuilt from scratch each run so the index always matches chunks.jsonl.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from .paths import PROJECT_ROOT, chunks_file, index_root

EMBED_MODEL = "BAAI/bge-small-en-v1.5"
_EMBED_CACHE = PROJECT_ROOT / ".cache" / "fastembed"


def collection_name(product: str, release: str) -> str:
    return f"{product}_{release}"


def _embedder():
    from fastembed import TextEmbedding

    _EMBED_CACHE.mkdir(parents=True, exist_ok=True)
    return TextEmbedding(model_name=EMBED_MODEL, cache_dir=str(_EMBED_CACHE))


def _read_chunks(product: str, release: str) -> list[dict]:
    cf = chunks_file(product, release)
    if not cf.exists():
        raise FileNotFoundError(f"no chunks at {cf}; run `bsc build` first")
    with cf.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def build_index(product: str, release: str, batch_size: int = 256) -> dict:
    chunks = _read_chunks(product, release)
    if not chunks:
        raise ValueError("chunks.jsonl is empty; nothing to index")

    import chromadb

    idx_dir: Path = index_root(product, release)
    idx_dir.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(idx_dir))
    name = collection_name(product, release)
    try:
        client.delete_collection(name)  # rebuild from scratch
    except Exception:
        pass
    coll = client.create_collection(name=name, metadata={"hnsw:space": "cosine"})

    embedder = _embedder()
    total = len(chunks)
    # Embed and write one batch at a time (rather than embedding all up front): bounds
    # memory and, on a slow CPU, gives a live progress/ETA line instead of a black box.
    t0 = time.perf_counter()
    for i in range(0, total, batch_size):
        part = chunks[i : i + batch_size]
        vecs = [vec.tolist() for vec in embedder.embed([c["text"] for c in part], batch_size=batch_size)]
        coll.add(
            ids=[c["id"] for c in part],
            embeddings=vecs,
            documents=[c["text"] for c in part],
            metadatas=[c["metadata"] for c in part],
        )
        done = min(i + batch_size, total)
        elapsed = time.perf_counter() - t0
        rate = done / elapsed if elapsed else 0.0
        eta_min = (total - done) / rate / 60 if rate else 0.0
        print(f"index: {done}/{total} chunks ({rate:.1f}/s, eta {eta_min:.1f} min)", flush=True)

    print(f"index: {total} chunks -> {idx_dir} (collection '{name}')")
    return {"chunks": total, "index_dir": str(idx_dir), "collection": name}
