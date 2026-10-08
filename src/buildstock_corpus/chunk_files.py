"""Per-document chunk files: one JSON Lines file per document beside the single chunks.jsonl.

chunks.jsonl is ~14 MB. A consumer building or checking a retrieval index for a handful of
documents should not have to fetch all of it, so every document's rows are also written to

    processed/<product>/<release>/chunks/<source_id>/<document stem>.jsonl

byte for byte and in the same order as in chunks.jsonl, under the same flat address the
section files use (see sections.doc_slot). Concatenating the files in manifest order
reproduces chunks.jsonl exactly. A document with no chunks gets an empty file, so the path
is predictable for every document and index.json can say `chunks: 0`.

These are a pure function of chunks.jsonl, so they are not hashed into the manifest:
`bsc validate` splits chunks.jsonl in memory and compares with the files on disk; `bsc map`
regenerates the tree. The chunks are rows of text with metadata, not reading matter -- a
document's chunk file is larger than the document, because chunks overlap and each carries
a header and metadata -- so a reader who wants the text fetches the section file instead.
"""

from __future__ import annotations

import json
import os
import shutil
from pathlib import Path

from .paths import long_path
from .sections import doc_slot

CHUNKS_DIRNAME = "chunks"


def chunks_file_for(corpus_path: str) -> str:
    """processed/-relative path of a document's chunk file."""
    source_id, stem = doc_slot(corpus_path)
    return f"{CHUNKS_DIRNAME}/{source_id}/{stem}.jsonl"


def _artifacts(manifest: dict) -> list[tuple[str, str, str]]:
    """(source_id, source_path, output_path) for every artifact, in manifest order."""
    return [
        (s["id"], a["source_path"], a["output_path"])
        for s in manifest.get("sources", [])
        for a in s.get("artifacts", [])
    ]


def split_chunks(chunks_text: str, manifest: dict) -> dict[str, str]:
    """{chunk file path: its content} for every document, from chunks.jsonl's text.

    Rows are routed by their metadata's (source_id, source_path) and kept verbatim, so each
    file is a byte-exact slice of chunks.jsonl. A row naming a document the manifest does
    not list is an error: chunks and manifest come from one build and cannot disagree.
    """
    by_key = {(sid, sp): chunks_file_for(out) for sid, sp, out in _artifacts(manifest)}
    files: dict[str, list[str]] = {rel: [] for rel in by_key.values()}
    for line in chunks_text.splitlines(keepends=True):
        if not line.strip():
            continue
        md = json.loads(line)["metadata"]
        key = (md.get("source_id"), md.get("source_path"))
        if key not in by_key:
            raise ValueError(f"chunk for {key} names a document the manifest does not list")
        files[by_key[key]].append(line if line.endswith("\n") else line + "\n")
    return {rel: "".join(rows) for rel, rows in files.items()}


def chunk_counts(chunks_text: str) -> dict[tuple[str, str], int]:
    """(source_id, source_path) -> number of chunks, for index.json."""
    counts: dict[tuple[str, str], int] = {}
    for line in chunks_text.splitlines():
        if line.strip():
            md = json.loads(line)["metadata"]
            key = (md.get("source_id"), md.get("source_path"))
            counts[key] = counts.get(key, 0) + 1
    return counts


def _read(path: str) -> str:
    with open(long_path(path), encoding="utf-8", newline="") as f:
        return f.read()


def write_chunk_files(proot: Path, manifest: dict, chunks_text: str) -> int:
    """Replace the whole chunks/ tree from chunks.jsonl; returns files written."""
    tree = proot / CHUNKS_DIRNAME
    if tree.exists():
        shutil.rmtree(long_path(tree))
    files = split_chunks(chunks_text, manifest)
    for rel, content in files.items():
        path = str(proot / rel)
        os.makedirs(long_path(os.path.dirname(path)), exist_ok=True)
        with open(long_path(path), "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
    return len(files)


def check_chunk_files(proot: Path, manifest: dict, chunks_text: str) -> tuple[list[str], int, bool]:
    """(violations, files checked, present) for the chunks/ tree against chunks.jsonl.

    An absent tree is derived output, not a violation (`bsc map` regenerates it); present,
    every document's file must match its slice byte for byte, and no file may exist that
    no document produced.
    """
    tree = proot / CHUNKS_DIRNAME
    if not tree.is_dir():
        return [], 0, False
    expected = split_chunks(chunks_text, manifest)
    errors: list[str] = []
    for rel, content in expected.items():
        path = str(proot / rel)
        if not os.path.isfile(long_path(path)):
            errors.append(f"chunks: file missing: {rel}")
        elif _read(path) != content:
            errors.append(f"chunks: file differs from its slice of chunks.jsonl: {rel}")
    on_disk = {
        os.path.relpath(os.path.join(d, f), long_path(proot)).replace("\\", "/")
        for d, _dirs, fs in os.walk(long_path(tree)) for f in fs if f.endswith(".jsonl")
    }
    for rel in sorted(on_disk - set(expected)):
        errors.append(f"chunks: file belongs to no document in this manifest: {rel}")
    return errors, len(expected), True
