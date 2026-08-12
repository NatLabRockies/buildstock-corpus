"""Crosswalk CSV + index map -> crosswalk.json (the per-measure versioning anchor).

The CSV maps each universal measure id to its per-release upgrade id/name; the index
page maps it to its documentation and the release it first appeared in. Joined by
measure id, this yields, for every measure: its doc (or a tracked gap), its initial
release, and its upgrade id within *this* dataset release — so a downstream answer can
say which measure a passage documents and whether it is even present in this release.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

from .measures_index import MeasureRef

_COVERED_KINDS = {"internal_md", "external_pdf", "local_pdf"}


def _release_columns(fieldnames: list[str], release: str) -> tuple[str | None, str | None]:
    """Find the upgrade_id/upgrade_name CSV columns for this release (e.g. 2025-3 ->
    '2025_comstock_amy2018_release_3_upgrade_{id,name}'), tolerant of the exact prefix."""
    year, _, num = release.partition("-")
    id_pat = re.compile(rf"{re.escape(year)}.*release_{re.escape(num)}_upgrade_id$")
    name_pat = re.compile(rf"{re.escape(year)}.*release_{re.escape(num)}_upgrade_name$")
    id_col = next((f for f in fieldnames if id_pat.search(f)), None)
    name_col = next((f for f in fieldnames if name_pat.search(f)), None)
    return id_col, name_col


def build_crosswalk(csv_path: Path, refs: list[MeasureRef], release: str) -> dict:
    """Join the crosswalk CSV with the parsed index refs into a crosswalk document."""
    ref_by_id = {r.measure_id: r for r in refs}
    measures: list[dict] = []
    gaps: list[dict] = []

    with csv_path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        id_col, name_col = _release_columns(reader.fieldnames or [], release)
        for row in reader:
            mid = (row.get("measure_id") or "").strip()
            if not mid:
                continue
            ref = ref_by_id.get(mid)
            upgrade_id = (row.get(id_col) or "").strip() if id_col else ""
            entry = {
                "measure_id": mid,
                "documentation_name": (row.get("measure_documentation_name") or "").strip(),
                "repo_folder": (row.get("public_repo_measure_folder_name") or "").strip(),
                "initial_release": ref.initial_release if ref else None,
                "doc_kind": ref.kind if ref else "unknown",
                "doc_target": ref.target if ref else None,
                "in_release": bool(upgrade_id),
                "upgrade_id": upgrade_id or None,
                "upgrade_name": ((row.get(name_col) or "").strip() or None) if name_col else None,
            }
            measures.append(entry)
            if ref is None:
                gaps.append({"measure_id": mid, "reason": "not listed in index page"})
            elif ref.kind not in _COVERED_KINDS:
                gaps.append({"measure_id": mid, "reason": "documentation expected soon"})

    # Index measures with no CSV row (rare, but track it rather than lose it).
    csv_ids = {m["measure_id"] for m in measures}
    for r in refs:
        if r.measure_id not in csv_ids:
            measures.append({
                "measure_id": r.measure_id,
                "documentation_name": r.name,
                "repo_folder": None,
                "initial_release": r.initial_release,
                "doc_kind": r.kind,
                "doc_target": r.target,
                "in_release": None,
                "upgrade_id": None,
                "upgrade_name": None,
            })
            if r.kind not in _COVERED_KINDS:
                gaps.append({"measure_id": r.measure_id, "reason": "documentation expected soon"})

    covered = sum(1 for m in measures if m["doc_kind"] in _COVERED_KINDS)
    return {
        "release": release,
        "counts": {"measures": len(measures), "covered": covered, "gaps": len(gaps)},
        "measures": sorted(measures, key=lambda m: m["measure_id"]),
        "gaps": sorted(gaps, key=lambda g: g["measure_id"]),
    }
