"""What a release leaves out on purpose, and what a reader must know about it, reach the map
(R3.3 of PLAN-resstock.md).

ResStock's first build raised three things the map could not say: two Jupyter notebook
how-to guides the markdown extractor skips (decision D4), a second dataset (AMY2012) that
shares the documentation (D2), and measure ids that are bare numbers, which sorted "10"
before "2". The registry now declares the first two, the manifest records them, the map
lists them, and measures sort the way a reader counts.
"""

from __future__ import annotations

import textwrap

import pytest

import buildstock_corpus.corpus_map as M
import buildstock_corpus.registry as R
from buildstock_corpus.extract.crosswalk import measure_sort_key

RELEASE = "resstock_amy2018_2025_release_1"

REGISTRY = textwrap.dedent(
    f"""\
    product: resstock
    release: "{RELEASE}"
    {{notes}}
    sources:
      - id: github_site
        type: markdown
        repo: https://example.org/ResStock.github.io.git
        git_ref: "main"
        status: site_page
        site_url: https://example.org/site
        doc_glob: "docs/**/*.md"
        {{not_converted}}
    """
)


def _load(tmp_path, monkeypatch, notes="", not_converted=""):
    path = tmp_path / "sources.yaml"
    path.write_text(REGISTRY.format(notes=notes, not_converted=not_converted), encoding="utf-8")
    monkeypatch.setattr(R, "sources_file", lambda p, r: path)
    return R.load_registry("resstock", RELEASE)


def test_numeric_measure_ids_sort_as_numbers_and_padded_ids_keep_their_order():
    assert sorted(["10", "2", "1", "32", "9"], key=measure_sort_key) == ["1", "2", "9", "10", "32"]
    padded = ["hvac_0010", "env_0002", "hvac_0002", "pkg_0012", "dr_0005"]
    assert sorted(padded, key=measure_sort_key) == sorted(padded)


def test_registry_carries_notes_and_not_converted_files(tmp_path, monkeypatch):
    reg = _load(
        tmp_path, monkeypatch,
        notes='notes:\n  - "Also documents the AMY2012 dataset."',
        not_converted=(
            "not_converted:\n"
            '          - path: "docs/how-to/annual.ipynb"\n'
            '            reason: "Jupyter notebook."'
        ),
    )
    assert reg.notes == ["Also documents the AMY2012 dataset."]
    assert reg.by_id("github_site").not_converted == [
        {"path": "docs/how-to/annual.ipynb", "reason": "Jupyter notebook."}
    ]


def test_a_registry_without_either_loads_with_nothing_to_say(tmp_path, monkeypatch):
    reg = _load(tmp_path, monkeypatch)
    assert reg.notes == [] and reg.by_id("github_site").not_converted == []


def test_the_checked_in_comstock_registry_declares_neither():
    real = R.load_registry("comstock", "comstock_amy2018_2025_release_3")
    assert real.notes == [] and all(not s.not_converted for s in real.sources)


def test_a_not_converted_entry_needs_a_path_and_a_reason(tmp_path, monkeypatch):
    with pytest.raises(ValueError, match="needs a path and a reason"):
        _load(
            tmp_path, monkeypatch,
            not_converted='not_converted:\n          - path: "docs/how-to/annual.ipynb"',
        )
    with pytest.raises(ValueError, match="notes must be a list"):
        _load(tmp_path, monkeypatch, notes='notes: "one sentence, not a list"')


def test_the_checked_in_resstock_registry_declares_the_notebooks_and_the_second_dataset():
    reg = R.load_registry("resstock", RELEASE)
    paths = [e["path"] for e in reg.by_id("github_site").not_converted]
    assert len(paths) == 2 and all(p.endswith(".ipynb") for p in paths)
    assert any("AMY2012" in n for n in reg.notes)
    assert any("2025_Release_1_upgrades_29_to_32" in n for n in reg.notes)


def test_map_lists_unconverted_files_as_known_gaps():
    manifest = {
        "gaps": {
            "measures": [],
            "not_converted": [
                {"source_id": "github_site", "path": "docs/how-to/annual.ipynb", "reason": "Jupyter notebook."}
            ],
        }
    }
    lines = M._gaps_section(manifest)
    assert lines[0] == "## Known gaps"
    assert any("1 upstream file(s) not converted" in ln for ln in lines)
    assert "  - `github_site/docs/how-to/annual.ipynb`: Jupyter notebook." in lines
    # a manifest written before the key existed still has no gaps section
    assert M._gaps_section({"gaps": {"measures": []}}) == []


def test_map_opens_with_the_release_notes_when_there_are_any():
    base = {"corpus_version": "x-v1", "generated_utc": "t", "sources": [], "counts": {}}
    with_notes = M._render("resstock", RELEASE, {**base, "notes": ["Also documents AMY2012."]}, "abc", {})
    assert "## About this release\n\n- Also documents AMY2012.\n" in with_notes
    assert with_notes.index("## About this release") < with_notes.index("## How to read this corpus")
    assert "## About this release" not in M._render("resstock", RELEASE, base, "abc", {})
