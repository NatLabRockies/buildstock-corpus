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

import yaml

from .index import EMBED_MODEL
from .paths import OVERLAYS_DIR, manifest_file, output_rel, processed_root

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
    sample: int | None = None,
    overlays: dict[str, dict] | None = None,
) -> dict:
    """Assemble and write manifest.json from the just-built documents + fetch state.

    `remaps` mirrors the output-dir remapping build applied when writing the files, so
    recorded output_paths point at where the artifacts actually landed. source_path
    stays as-is — it is the upstream citation anchor.

    `sample` records that the build was capped per category. It is stamped into the
    manifest as `sample.partial` because a manifest is the record of what a release
    contains: an unmarked 4-document manifest tagged 2025-3 would be a false record.

    `overlays` records which artifacts carry hand-authored content (see overlay.py),
    keyed source_id -> source_path. Without it a reader could not tell a transcribed table
    from an extracted one, which is the whole reason the transcriptions live in versioned
    sidecars rather than being edited into processed/.
    """
    proot = processed_root(product, release)
    remaps = remaps or {}
    overlays = overlays or {}
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
        artifact = {
            "source_path": doc.source_path,
            "source_type": doc.source_type,
            "title": doc.title,
            "input_sha256": src_hashes.get(doc.source_id, {}).get(doc.source_path),
            "output_path": out_rel,
            "output_sha256": _sha256_file(out_abs) if out_abs.is_file() else None,
        }
        ov = overlays.get(doc.source_id, {}).get(doc.source_path)
        if ov:
            artifact["overlay"] = ov
        grp["artifacts"].append(artifact)

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
            "overlay_documents": sum(len(v) for v in overlays.values()),
            "overlay_tables": sum(
                len(rec["tables_applied"]) for v in overlays.values() for rec in v.values()
            ),
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
    if sample is not None:
        manifest["sample"] = {"per_category": sample, "partial": True}

    mf = manifest_file(product, release)
    mf.parent.mkdir(parents=True, exist_ok=True)
    mf.write_text(json.dumps(manifest, indent=2), encoding="utf-8", newline="\n")
    return manifest


def _validate_overlay(proot: Path, artifact: dict, where: str) -> tuple[list[str], int, int]:
    """Check a hand-authored overlay is intact and still matches the images it transcribed.

    Returns (violations, tables_checked, tables_unverifiable).

    Two things can silently rot: the sidecar itself can be edited after the build (so the
    shipped table no longer matches the recorded source), or upstream can redraw the image
    a table was read from (so the transcription is stale). Both leave a plausible table in
    the corpus with nothing backing it, which is what the manifest exists to prevent, so
    both are violations.

    An *absent* image is not. .gitignore deliberately excludes processed/**/*.png (~250 MB
    of regenerable binaries), so a fresh clone has the transcriptions and the manifest but
    none of the pictures. Treating that as a violation would make `bsc validate` fail on
    every clone until someone re-ran fetch+build — reporting a provenance break where
    there is none. Those tables are counted as unverifiable here and surfaced by
    validate_release, so a clean run never overstates what it actually checked.
    """
    ov = artifact["overlay"]
    errors: list[str] = []

    ov_abs = OVERLAYS_DIR / ov.get("path", "")
    if not ov_abs.is_file():
        return [f"{where}: overlay file missing on disk: {ov.get('path')}"], 0, 0
    if _sha256_file(ov_abs) != ov.get("sha256"):
        return [f"{where}: overlay hash mismatch (sidecar changed since build): {ov['path']}"], 0, 0

    try:
        data = yaml.safe_load(ov_abs.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        return [f"{where}: overlay is not readable YAML: {str(exc)[:120]}"], 0, 0

    applied = set(ov.get("tables_applied") or [])
    page_dir = (proot / artifact.get("output_path", "")).parent
    checked = unverifiable = 0
    for entry in data.get("tables") or []:
        label = str(entry.get("label", "")).strip()
        if label not in applied:
            continue  # recorded as not applied; nothing was injected to back up
        img = page_dir / str(entry.get("source_image", ""))
        if not img.is_file():
            unverifiable += 1
        elif _sha256_file(img) != entry.get("source_image_sha256"):
            checked += 1
            errors.append(
                f"{where}: {label}: source image changed since transcription "
                f"({img.name}); the injected table may no longer match it"
            )
        else:
            checked += 1
    return errors, checked, unverifiable


def validate_manifest(
    product: str, release: str, manifest: dict, stats: dict | None = None
) -> list[str]:
    """Return a list of invariant violations ([] means valid). Pure — no printing.

    `stats`, if given, is filled with counts the caller may want to report but which are
    not violations: `overlay_checked` and `overlay_unverifiable` (see _validate_overlay).
    It is an out-parameter rather than part of the return value so the return stays a plain
    error list, which is what every caller and test asserts on.
    """
    proot = processed_root(product, release)
    errors: list[str] = []
    checked = unverifiable = 0

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
            if a.get("overlay"):
                ov_errors, n_ok, n_skip = _validate_overlay(proot, a, where)
                errors += ov_errors
                checked += n_ok
                unverifiable += n_skip
    if n_art == 0:
        errors.append("manifest records zero artifacts")
    if stats is not None:
        stats["overlay_checked"] = checked
        stats["overlay_unverifiable"] = unverifiable

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
    stats: dict = {}
    errors = validate_manifest(product, release, manifest, stats)

    n_art = sum(len(s.get("artifacts", [])) for s in manifest.get("sources", []))
    if errors:
        print(f"validate: FAILED for {product} {release} ({len(errors)} violation(s)):")
        for e in errors[:25]:
            print(f"  - {e}")
        if len(errors) > 25:
            print(f"  ... and {len(errors) - 25} more")
        return False

    print(f"validate: OK - {product} {release}")
    sample = manifest.get("sample")
    if sample:
        print(
            f"  SAMPLE (partial corpus - NOT a release record): "
            f"at most {sample.get('per_category')} document(s) per category"
        )
    print(f"  {n_art} artifacts, all traced to hashed inputs and present on disk with matching hashes")
    counts = manifest.get("counts", {})
    n_ov = counts.get("overlay_tables") or 0
    if n_ov:
        # State what was actually re-verified. On a fresh clone the source images are
        # absent by design (.gitignore drops processed/**/*.png), and claiming those
        # transcriptions were checked against their pictures would be a false record.
        skipped = stats.get("overlay_unverifiable", 0)
        detail = f"{stats.get('overlay_checked', 0)} re-verified against its source image"
        if skipped:
            detail += (
                f", {skipped} unverifiable here (source image not in the working tree; "
                f"run `bsc fetch && bsc build` to restore it)"
            )
        print(
            f"  {n_ov} hand-authored table(s) across "
            f"{counts.get('overlay_documents')} doc(s): {detail}"
        )
    gaps = manifest.get("gaps", {})
    gm = gaps.get("measures", [])
    if gm:
        print(f"  {len(gm)} tracked measure gap(s): {', '.join(gm)}")
    up = gaps.get("unreachable_pdfs", [])
    if up:
        print(f"  {len(up)} unreachable PDF(s) recorded as gaps")
    return True
