"""Index-page parsing + crosswalk join — the measure->doc->release versioning anchor."""

from __future__ import annotations

from buildstock_corpus.extract.crosswalk import _release_columns, build_crosswalk
from buildstock_corpus.extract.measures_index import (
    local_pdf_paths,
    parse_index,
)

RELEASE = "comstock_amy2018_2025_release_3"

INDEX_PATH = "docs/upgrade_measures/upgrade_measures.md"

# Exercises all four link forms plus a combined "shares one doc" row.
INDEX_MD = """\
# Upgrade Measures

| Measure ID | Documentation | Initial Release |
|---|---|---|
| ltg_0003 | [LED Lighting]({{site.baseurl}}{% link docs/upgrade_measures/ltg_led.md %}) | 2024-1 |
| hvac_0001 | [Heat Pump](https://docs.nlr.gov/measures/hvac_0001.pdf) | 2025-1 |
| env_0002 | [Roof Insulation][8] | 2025-2 |
| dr_0005 / dr_0006 | Coming Soon** | 2025-3 |

[8]: ../../assets/files/env_roof.pdf
"""


def _by_id(refs):
    return {r.measure_id: r for r in refs}


def test_parse_index_all_link_forms():
    refs = parse_index(INDEX_MD, INDEX_PATH)
    by_id = _by_id(refs)

    # combined row yields one ref per id, sharing the (here empty) doc
    assert set(by_id) == {"ltg_0003", "hvac_0001", "env_0002", "dr_0005", "dr_0006"}

    assert by_id["ltg_0003"].kind == "internal_md"
    assert by_id["ltg_0003"].target == "docs/upgrade_measures/ltg_led.md"
    assert by_id["ltg_0003"].name == "LED Lighting"
    assert by_id["ltg_0003"].initial_release == "2024-1"

    assert by_id["hvac_0001"].kind == "external_pdf"
    assert by_id["hvac_0001"].target == "https://docs.nlr.gov/measures/hvac_0001.pdf"

    # reference-style relative link resolved against the index dir (.. collapsed)
    assert by_id["env_0002"].kind == "local_pdf"
    assert by_id["env_0002"].target == "assets/files/env_roof.pdf"

    # plain-text (no link) measures are tracked gaps
    assert by_id["dr_0005"].kind == "none" and by_id["dr_0005"].target is None
    assert by_id["dr_0006"].kind == "none"


def test_local_pdf_paths_deduped_sorted():
    refs = parse_index(INDEX_MD, INDEX_PATH)
    assert local_pdf_paths(refs) == ["assets/files/env_roof.pdf"]


CSV = """\
measure_id,measure_documentation_name,public_repo_measure_folder_name,2025_comstock_amy2018_release_3_upgrade_id,2025_comstock_amy2018_release_3_upgrade_name
hvac_0001,Heat Pump,upgrade_hvac_0001,15,Heat Pump RTU
env_0002,Roof Insulation,upgrade_env_0002,,
dr_0005,Demand Response,upgrade_dr_0005,,
xyz_0009,Orphan Measure,upgrade_xyz_0009,3,Orphan
"""


def test_build_crosswalk_join_counts_and_gaps(tmp_path):
    csv_path = tmp_path / "crosswalk.csv"
    csv_path.write_text(CSV, encoding="utf-8")
    refs = parse_index(INDEX_MD, INDEX_PATH)

    cw = build_crosswalk(csv_path, refs, RELEASE)

    # 4 CSV rows + 2 index-only measures (ltg_0003, dr_0006) = 6; covered/gaps partition them
    assert cw["counts"] == {"measures": 6, "covered": 3, "gaps": 3}

    by_id = {m["measure_id"]: m for m in cw["measures"]}
    # release-present measure carries its per-release upgrade id/name
    assert by_id["hvac_0001"]["in_release"] is True
    assert by_id["hvac_0001"]["upgrade_id"] == "15"
    assert by_id["hvac_0001"]["upgrade_name"] == "Heat Pump RTU"
    # covered but not present in this release
    assert by_id["env_0002"]["in_release"] is False
    assert by_id["env_0002"]["doc_kind"] == "local_pdf"
    # index-only measure with no CSV row is still tracked
    assert by_id["ltg_0003"]["doc_kind"] == "internal_md"

    gap_ids = {g["measure_id"] for g in cw["gaps"]}
    assert gap_ids == {"dr_0005", "dr_0006", "xyz_0009"}
    # a CSV measure absent from the index is a distinct gap reason
    xyz_gap = next(g for g in cw["gaps"] if g["measure_id"] == "xyz_0009")
    assert "index" in xyz_gap["reason"]


def test_release_columns_found_however_the_release_id_orders_its_parts():
    """The CSV names its columns 2025_comstock_amy2018_release_3; our id says
    comstock_amy2018_2025_release_3. Same release, different order — match on year + number."""
    fields = list(CSV.split("\n")[0].split(","))

    assert _release_columns(fields, "comstock_amy2018_2025_release_3") == (
        "2025_comstock_amy2018_release_3_upgrade_id",
        "2025_comstock_amy2018_release_3_upgrade_name",
    )
    # the pre-OEDI tag form still resolves, so an older release stays buildable
    assert _release_columns(fields, "2025-3") == (
        "2025_comstock_amy2018_release_3_upgrade_id",
        "2025_comstock_amy2018_release_3_upgrade_name",
    )


def test_release_id_without_a_year_and_number_matches_no_column():
    """No silent wrong column: an id that encodes neither yields nothing to join on."""
    fields = list(CSV.split("\n")[0].split(","))
    assert _release_columns(fields, "comstock_amy2018_latest") == (None, None)
