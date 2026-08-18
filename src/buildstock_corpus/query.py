"""Retrieve top-k release-tagged, cited passages for a query (retrieval-first).

The default output is the retrieved chunks with full provenance (source path, section,
release). `--answer` is optional and only synthesizes if an Anthropic API key is present,
keeping Level 1 true to "the user brings their own LLM".
"""

from __future__ import annotations

import os

from .index import EMBED_MODEL, collection_name, index_root
from .paths import PROJECT_ROOT

_EMBED_CACHE = PROJECT_ROOT / ".cache" / "fastembed"


def _embedder():
    from fastembed import TextEmbedding

    return TextEmbedding(model_name=EMBED_MODEL, cache_dir=str(_EMBED_CACHE))


def search(product: str, release: str, text: str, k: int = 5) -> list[dict]:
    import chromadb

    idx_dir = index_root(product, release)
    if not idx_dir.exists():
        raise FileNotFoundError(f"no index at {idx_dir}; run `bsc index` first")
    client = chromadb.PersistentClient(path=str(idx_dir))
    # Close before returning: reading mmaps the segment files and chroma caches the client
    # by path, so a leaked one keeps the store locked and a later `bsc index` in the same
    # process cannot replace it (WinError 32 on Windows). Every hit is copied out of `res`
    # below, so nothing here outlives the client.
    try:
        coll = client.get_collection(collection_name(product, release))

        qvec = next(iter(_embedder().query_embed([text]))).tolist()
        res = coll.query(query_embeddings=[qvec], n_results=k)

        hits: list[dict] = []
        for doc, meta, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0]):
            hits.append({"text": doc, "metadata": dict(meta), "score": round(1.0 - dist, 4)})
        return hits
    finally:
        client.close()


def format_hits(hits: list[dict]) -> str:
    lines: list[str] = []
    for i, h in enumerate(hits, 1):
        m = h["metadata"]
        cite = f"{m['source_id']}/{m['source_path']}"
        section = f" § {m['section']}" if m.get("section") else ""
        lines.append(
            f"[{i}] score={h['score']}  ({m['product']} {m['release']})  {cite}{section}\n"
            f"{h['text'].strip()}\n"
        )
    return "\n".join(lines)


def query_corpus(text: str, product: str, release: str, k: int = 5, answer: bool = False) -> None:
    """Retrieve, print cited passages, and optionally synthesize an answer."""
    hits = search(product, release, text, k=k)
    if not hits:
        print("no passages found")
        return
    print(format_hits(hits))
    if answer:
        synthesized = answer_from_hits(product, release, text, hits)
        if synthesized is None:
            print("\n[--answer skipped: set ANTHROPIC_API_KEY and `uv pip install anthropic`]")
        else:
            print("\n=== answer ===\n" + synthesized)


def answer_from_hits(product: str, release: str, text: str, hits: list[dict]) -> str | None:
    """Optional LLM synthesis over the retrieved passages; None if no API key/SDK."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return None
    try:
        import anthropic
    except ImportError:
        return None

    context = "\n\n".join(
        f"[{i}] {h['metadata']['source_id']}/{h['metadata']['source_path']}\n{h['text']}"
        for i, h in enumerate(hits, 1)
    )
    prompt = (
        f"Answer the question using ONLY the passages below (ComStock {release}). "
        f"Cite passages as [n]. If the passages don't cover it, say so.\n\n"
        f"Passages:\n{context}\n\nQuestion: {text}"
    )
    client = anthropic.Anthropic()
    msg = client.messages.create(
        model="claude-opus-5",
        max_tokens=2048,
        thinking={"type": "adaptive"},
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(block.text for block in msg.content if block.type == "text")
