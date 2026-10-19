"""The measures side of a ResStock-shaped source (R1.3 of PLAN-resstock.md).

ResStock numbers its measures 1 to 32 instead of naming them hvac_0001, documents every
one as an external OSTI report (several sharing one), and publishes its per-release
upgrade map as OEDI's upgrades_lookup.json rather than a crosswalk CSV. The parser takes
its id pattern from the registry, fetch downloads and hashes the lookup, and the crosswalk
join reads it; the ComStock CSV path keeps working unchanged (see test_crosswalk.py).
"""

from __future__ import annotations

import hashlib
import json

import pytest

import buildstock_corpus.fetch as F
from buildstock_corpus.extract.crosswalk import build_crosswalk
from buildstock_corpus.extract.measures_index import parse_index
from buildstock_corpus.registry import DEFAULT_MEASURE_ID_PATTERN

RELEASE = "resstock_amy2018_2025_release_1"
INDEX_PATH = "docs/upgrade_measures.md"
NUMERIC = r"^\d+$"

# The ResStock page's shape: numeric ids, every link an OSTI PDF, one report shared by
# several measures (24 and 25 here), and a footnoted row with no documentation yet.
INDEX_MD = """\
# Upgrade Measures

| **Measure Number** | **Measure Name and Documentation Link** | **Initial Dataset Release** |
| :---: | --- | --- |
| 1 | [Natural Gas Furnace 95% AFUE](https://docs.nlr.gov/docs/fy26osti/96634.pdf)      | ResStock 2025 Release 1 |
| 6 | [Residential Single-Stage Geothermal Heat Pump (3.8 COP, 18.6 EER)](https://www.nlr.gov/docs/fy26osti/95032.pdf) | ResStock 2025 Release 1 |
| 11 | Advanced Air Sealing*                                                            | ResStock 2025 Release 1 |
| 24 | [HVAC Demand Flexibility with On-Peak Load Shedding of 2F offset](https://docs.nlr.gov/docs/fy26osti/93846.pdf) | ResStock 2025 Release 1 |
| 25 | [HVAC Demand Flexibility with 4 hour Pre-peak Load Shifting of 2F offset](https://docs.nlr.gov/docs/fy26osti/93846.pdf) | ResStock 2025 Release 1 |

*Measure documentation will be available in the future.
"""

LOOKUP = {
    "0": "Baseline",
    "1": "Natural Gas Furnace 95% AFUE for All Dwellings with Ducts",
    "6": "Single-Speed Geothermal Heat Pump with Thermally Enhanced Grout and Pipes",
    "11": "Air Sealing",
    "24": "HVAC Demand Flexibility - On-peak Load Shedding, 2F Offset",
    "25": "HVAC Demand Flexibility - Pre-peak Load Shifting, 2F Offset, 4hr Pre-peak Duration",
    "29": "General Air Sealing",
}


def test_numeric_ids_parse_with_the_registry_pattern_and_not_with_the_default():
    refs = parse_index(INDEX_MD, INDEX_PATH, NUMERIC)
    assert [r.measure_id for r in refs] == ["1", "6", "11", "24", "25"]
    by_id = {r.measure_id: r for r in refs}
    assert by_id["1"].kind == "external_pdf"
    assert by_id["1"].target == "https://docs.nlr.gov/docs/fy26osti/96634.pdf"
    assert by_id["1"].initial_release == "ResStock 2025 Release 1"
    assert by_id["11"].kind == "none" and by_id["11"].name == "Advanced Air Sealing"
    assert by_id["24"].target == by_id["25"].target  # one report, two measures
    # the header row's "Measure Number" cell is not an id
    assert parse_index(INDEX_MD, INDEX_PATH, DEFAULT_MEASURE_ID_PATTERN) == []


def test_lookup_join_counts_names_and_gaps(tmp_path):
    lookup_path = tmp_path / "upgrades_lookup.json"
    lookup_path.write_text(json.dumps(LOOKUP), encoding="utf-8")
    refs = parse_index(INDEX_MD, INDEX_PATH, NUMERIC)

    cw = build_crosswalk(None, refs, RELEASE, lookup_path=lookup_path)

    # six lookup measures (baseline excluded); 4 documented, 11 undocumented, 29 not on the page
    assert cw["counts"] == {"measures": 6, "covered": 4, "gaps": 2}
    assert [m["measure_id"] for m in cw["measures"]] == ["1", "11", "24", "25", "29", "6"]
    assert cw["gaps"] == [
        {"measure_id": "11", "reason": "documentation expected soon"},
        {"measure_id": "29", "reason": "not listed in index page"},
    ]
    m1 = next(m for m in cw["measures"] if m["measure_id"] == "1")
    assert m1["documentation_name"] == "Natural Gas Furnace 95% AFUE"  # the page's title
    assert m1["upgrade_name"] == LOOKUP["1"]  # the dataset's name for the same upgrade
    assert (m1["upgrade_id"], m1["in_release"], m1["status"]) == ("1", True, "osti_pdf")
    m29 = next(m for m in cw["measures"] if m["measure_id"] == "29")
    assert (m29["documentation_name"], m29["status"], m29["doc_kind"]) == (None, "missing", "unknown")
    assert all(m["repo_folder"] is None for m in cw["measures"])


def test_lookup_must_be_a_json_object_and_one_map_is_required(tmp_path):
    bad = tmp_path / "lookup.json"
    bad.write_text("[1, 2]", encoding="utf-8")
    with pytest.raises(ValueError, match="JSON object"):
        build_crosswalk(None, [], RELEASE, lookup_path=bad)
    with pytest.raises(ValueError, match="crosswalk CSV or an upgrades lookup"):
        build_crosswalk(None, [], RELEASE)


class _FakeResponse:
    def __init__(self, content: bytes, fail: bool = False):
        self.content = content
        self._fail = fail

    def raise_for_status(self):
        if self._fail:
            raise RuntimeError("404 Not Found")


class _FakeClient:
    responses: dict[str, _FakeResponse] = {}

    def __init__(self, **kwargs):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def get(self, url):
        return self.responses[url]


def test_fetch_downloads_and_hashes_the_lookup(tmp_path, monkeypatch):
    body = json.dumps(LOOKUP).encode("utf-8")
    _FakeClient.responses = {"https://example.org/oedi/upgrades_lookup.json": _FakeResponse(body)}
    monkeypatch.setattr(F.httpx, "Client", _FakeClient)

    entry, gap = F._download_lookup(
        "https://example.org/oedi/upgrades_lookup.json", tmp_path / "um_upgrades_lookup.json", tmp_path
    )

    assert gap is None
    assert entry == {
        "url": "https://example.org/oedi/upgrades_lookup.json",
        "path": "um_upgrades_lookup.json",
        "sha256": hashlib.sha256(body).hexdigest(),
    }
    assert (tmp_path / "um_upgrades_lookup.json").read_bytes() == body


def test_unreachable_or_malformed_lookup_is_a_gap_not_a_crash(tmp_path, monkeypatch):
    _FakeClient.responses = {
        "https://example.org/missing.json": _FakeResponse(b"", fail=True),
        "https://example.org/list.json": _FakeResponse(b"[1]"),
    }
    monkeypatch.setattr(F.httpx, "Client", _FakeClient)

    entry, gap = F._download_lookup("https://example.org/missing.json", tmp_path / "a.json", tmp_path)
    assert entry is None and gap["status"] == "error" and "404" in gap["note"]
    entry, gap = F._download_lookup("https://example.org/list.json", tmp_path / "b.json", tmp_path)
    assert entry is None and "JSON object" in gap["note"]
    assert not (tmp_path / "a.json").exists() and not (tmp_path / "b.json").exists()
