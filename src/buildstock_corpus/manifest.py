"""Provenance manifest — the record that makes the corpus release-tagged and auditable.

`build_manifest()` runs at the end of a build and writes manifest.json: for every
processed artifact it records the hashed source input it came from, the hashed output,
the clone commit SHAs, the version of every tool in the chain, and the tracked gaps.

`validate_release()` enforces the invariants FY26 governance rests on:
  * release tag present and matching,
  * every output artifact traces to a hashed source input (no orphan outputs),
  * every recorded output still exists on disk with the recorded hash, and
  * every crosswalk measure is either covered by a doc or listed as a tracked gap.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from .index import EMBED_MODEL
from .paths import manifest_file, output_rel, processed_root

PIPELINE_VERSION = "0.1.0"
_COVERED_KINDS = {"internal_md", "external_pdf", "local_pdf"}


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def _tooling() -> dict:
    """Versions of every tool in the extraction chain, for reproducibility."""
    tooling: dict = {"pipeline": PIPELINE_VERSION, "embedding_model": EMBED_MODEL}
    try:
        import pypandoc

        tooling["pandoc"] = pypandoc.get_pandoc_version()
    except Exception:
        tooling["pandoc"] = None
    try:
        from importlib.metadata import version

        tooling["docling"] = version("docling")
    except Exception:
        tooling["docling"] = None
    return tooling


def _input_hashes(src_state: dict) -> dict[str, str]:
    """Every hashed input for a source, keyed by path (unions all input lists)."""
    hashes: dict[str, str] = {}
    for key in ("inputs", "internal_pages", "external_pdfs", "local_pdfs"):
        for item in src_state.get(key) or []:
            hashes[item["path"]] = item["sha256"]
    for key in ("crosswalk", "index_page"):
        item = src_state.get(key)
        if item:
            hashes[item["path"]] = item["sha256"]
    return hashes


def _by_type(docs) -> dict[str, int]:
    out: dict[str, int] = {}
    for d in docs:
        out[d.source_type] = out.get(d.source_type, 0) + 1
    return out


def build_manifest(
    product: str,
    release: str,
    docs,
    crosswalk: dict | None,
    warnings: list[str],
    excluded: dict[str, list[str]],
    state: dict,
    n_chunks: int,
    remaps: dict[str, tuple[str, str]] | None = None,
) -> dict:
    """Assemble and write manifest.json from the just-built documents + fetch state.

    `remaps` mirrors the output-dir remapping build applied when writing the files, so
    recorded output_paths point at where the artifacts actually landed. source_path
    stays as-is — it is the upstream citation anchor.
    """
    proot = processed_root(product, release)
    remaps = remaps or {}
    src_hashes = {sid: _input_hashes(st) for sid, st in state.get("sources", {}).items()}

    sources_out: dict[str, dict] = {}
    for doc in docs:
        out_rel = output_rel(doc.source_id, doc.source_path, remaps.get(doc.source_id))
        out_abs = proot / out_rel
        grp = sources_out.setdefault(
            doc.source_id,
            {
                "id": doc.source_id,
                "type": state.get("sources", {}).get(doc.source_id, {}).get("type"),
                "clone": state.get("sources", {}).get(doc.source_id, {}).get("clone"),
                "artifacts": [],
            },
        )
        grp["artifacts"].append(
            {
                "source_path": doc.source_path,
                "source_type": doc.source_type,
                "title": doc.title,
                "input_sha256": src_hashes.get(doc.source_id, {}).get(doc.source_path),
                "output_path": out_rel,
                "output_sha256": _sha256_file(out_abs) if out_abs.is_file() else None,
            }
        )

    unreachable_pdfs = [
        {"source_id": sid, **m}
        for sid, st in state.get("sources", {}).items()
        for m in (st.get("missing") or [])
    ]

    manifest = {
        "product": product,
        "release": release,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "tooling": _tooling(),
        "clones": state.get("clones", []),
        "sources": list(sources_out.values()),
        "counts": {
            "documents": len(docs),
            "chunks": n_chunks,
            "by_type": _by_type(docs),
        },
        "crosswalk": {
            "file": "crosswalk.json",
            "counts": crosswalk["counts"] if crosswalk else None,
        },
        "gaps": {
            "measures": [g["measure_id"] for g in crosswalk["gaps"]] if crosswalk else [],
            "unreachable_pdfs": unreachable_pdfs,
            "excluded_unpublished": excluded,
        },
        "warnings": warnings,
    }

    mf = manifest_file(product, release)
    mf.parent.mkdir(parents=True, exist_ok=True)
    mf.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


def validate_manifest(product: str, release: str, manifest: dict) -> list[str]:
    """Return a list of invariant violations ([] means valid). Pure — no printing."""
    proot = processed_root(product, release)
    errors: list[str] = []

    if manifest.get("product") != product or manifest.get("release") != release:
        errors.append(
            f"release tag mismatch: manifest is "
            f"{manifest.get('product')}/{manifest.get('release')}, expected {product}/{release}"
        )

    n_art = 0
    for src in manifest.get("sources", []):
        for a in src.get("artifacts", []):
            n_art += 1
            where = f"{src.get('id')}: {a.get('output_path')}"
            if not a.get("input_sha256"):
                errors.append(f"{where}: output has no hashed source input")
            recorded = a.get("output_sha256")
            out_abs = proot / a.get("output_path", "")
            if not recorded:
                errors.append(f"{where}: no recorded output hash")
            elif not out_abs.is_file():
                errors.append(f"{where}: output file missing on disk")
            elif _sha256_file(out_abs) != recorded:
                errors.append(f"{where}: output hash mismatch (file changed since build)")
    if n_art == 0:
        errors.append("manifest records zero artifacts")

    cw_file = proot / "crosswalk.json"
    if cw_file.is_file():
        cw = json.loads(cw_file.read_text(encoding="utf-8"))
        gap_ids = {g["measure_id"] for g in cw.get("gaps", [])}
        for m in cw.get("measures", []):
            if m["doc_kind"] not in _COVERED_KINDS and m["measure_id"] not in gap_ids:
                errors.append(
                    f"crosswalk: measure {m['measure_id']} is neither covered nor a tracked gap"
                )

    return errors


def validate_release(product: str, release: str) -> bool:
    """Load manifest.json, check invariants, print a report; return True if valid."""
    mf = manifest_file(product, release)
    if not mf.is_file():
        print(f"validate: no manifest at {mf}; run `bsc build` first")
        return False
    manifest = json.loads(mf.read_text(encoding="utf-8"))
    errors = validate_manifest(product, release, manifest)

    n_art = sum(len(s.get("artifacts", [])) for s in manifest.get("sources", []))
    if errors:
        print(f"validate: FAILED for {product} {release} ({len(errors)} violation(s)):")
        for e in errors[:25]:
            print(f"  - {e}")
        if len(errors) > 25:
            print(f"  ... and {len(errors) - 25} more")
        return False

    print(f"validate: OK - {product} {release}")
    print(f"  {n_art} artifacts, all traced to hashed inputs and present on disk with matching hashes")
    gaps = manifest.get("gaps", {})
    gm = gaps.get("measures", [])
    if gm:
        print(f"  {len(gm)} tracked measure gap(s): {', '.join(gm)}")
    up = gaps.get("unreachable_pdfs", [])
    if up:
        print(f"  {len(up)} unreachable PDF(s) recorded as gaps")
    return True
