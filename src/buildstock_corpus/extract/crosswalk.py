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

from .doc_dates import DocDate
from .measures_index import MeasureRef

_COVERED_KINDS = {"internal_md", "external_pdf", "local_pdf"}


# Release ids in OEDI form (comstock_amy2018_2025_release_3) and the older tag form
# (2025-3). Both are reduced to the (year, release number) pair the CSV columns key on;
# the dataset type and weather year in between are not part of that key.
_OEDI_RELEASE = re.compile(r"_(?P<year>\d{4})_release_(?P<num>\d+)$")
_TAG_RELEASE = re.compile(r"^(?P<year>\d{4})-(?P<num>\d+)$")


def _release_parts(release: str) -> tuple[str, str] | None:
    """(year, release number) for a release id, or None if it encodes neither."""
    for pattern in (_OEDI_RELEASE, _TAG_RELEASE):
        m = pattern.search(release)
        if m:
            return m.group("year"), m.group("num")
    return None


def _release_columns(fieldnames: list[str], release: str) -> tuple[str | None, str | None]:
    """Find the upgrade_id/upgrade_name CSV columns for this release.

    The CSV names them for the release in its own way — comstock_amy2018_2025_release_3 ->
    '2025_comstock_amy2018_release_3_upgrade_{id,name}', which orders the same parts
    differently — so match on the year and release number and stay tolerant of whatever
    sits between them.
    """
    parts = _release_parts(release)
    if parts is None:
        return None, None
    year, num = parts
    id_pat = re.compile(rf"{re.escape(year)}.*release_{re.escape(num)}_upgrade_id$")
    name_pat = re.compile(rf"{re.escape(year)}.*release_{re.escape(num)}_upgrade_name$")
    id_col = next((f for f in fieldnames if id_pat.search(f)), None)
    name_col = next((f for f in fieldnames if name_pat.search(f)), None)
    return id_col, name_col


def build_crosswalk(
    csv_path: Path,
    refs: list[MeasureRef],
    release: str,
    dates: dict[str, DocDate] | None = None,
) -> dict:
    """Join the crosswalk CSV with the parsed index refs into a crosswalk document.

    `dates` maps a doc target to when that document was last updated at its source (see
    doc_dates.resolve_doc_dates). Measures sharing one document share its date; a measure
    whose documentation does not exist yet is dated None rather than given a stand-in.
    """
    ref_by_id = {r.measure_id: r for r in refs}
    measures: list[dict] = []
    gaps: list[dict] = []

    def dated(ref: MeasureRef | None) -> tuple[str | None, str | None]:
        """(date, source) for a ref's document — both None together, never one alone."""
        d = dates.get(ref.target) if (dates and ref and ref.target) else None
        return (d.date, d.source) if d else (None, None)

    with csv_path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        id_col, name_col = _release_columns(reader.fieldnames or [], release)
        for row in reader:
            mid = (row.get("measure_id") or "").strip()
            if not mid:
                continue
            ref = ref_by_id.get(mid)
            upgrade_id = (row.get(id_col) or "").strip() if id_col else ""
            date, date_source = dated(ref)
            entry = {
                "measure_id": mid,
                "documentation_name": (row.get("measure_documentation_name") or "").strip(),
                "repo_folder": (row.get("public_repo_measure_folder_name") or "").strip(),
                "initial_release": ref.initial_release if ref else None,
                "doc_kind": ref.kind if ref else "unknown",
                "doc_target": ref.target if ref else None,
                "date_last_updated": date,
                "date_last_updated_source": date_source,
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
            date, date_source = dated(r)
            measures.append({
                "measure_id": r.measure_id,
                "documentation_name": r.name,
                "repo_folder": None,
                "initial_release": r.initial_release,
                "doc_kind": r.kind,
                "doc_target": r.target,
                "date_last_updated": date,
                "date_last_updated_source": date_source,
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
