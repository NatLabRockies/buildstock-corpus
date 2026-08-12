"""Manifest provenance invariants — the governance guarantee the whole corpus rests on:
no output artifact without a hashed source input + matching release tag, every recorded
output present on disk with its recorded hash, every crosswalk measure covered or a gap.

processed_root / manifest_file are monkeypatched to a tmp dir so these run hermetically.
"""

from __future__ import annotations

import json

import buildstock_corpus.manifest as M
from buildstock_corpus.normalize import Document

OUT_REL = "technical_reference/documentation/reference_doc/4_9_hvac.md"
OUT_CONTENT = (
    "<!-- comstock 2025-3 | technical_reference | documentation/reference_doc/4_9_hvac.tex -->\n"
    "# HVAC Systems\n\nbody\n"
)


def _doc() -> Document:
    return Document(
        product="comstock",
        release="2025-3",
        source_id="technical_reference",
        source_type="latex",
        source_path="documentation/reference_doc/4_9_hvac.tex",
        title="HVAC Systems",
        body="# HVAC Systems\n\nbody\n",
    )


def _state(sha: str = "deadbeef", input_path: str = "documentation/reference_doc/4_9_hvac.tex") -> dict:
    return {
        "clones": [
            {
                "repo": "NatLabRockies/ComStock",
                "git_ref": "2025-3",
                "sha": "abc123",
                "dest": "repos/ComStock@2025-3",
            }
        ],
        "sources": {
            "technical_reference": {
                "type": "latex",
                "clone": "ComStock@2025-3",
                "inputs": [{"path": input_path, "sha256": sha}],
            }
        },
    }


def _patch(tmp_path, monkeypatch):
    proot = tmp_path / "processed"
    proot.mkdir()
    monkeypatch.setattr(M, "processed_root", lambda p, r: proot)
    monkeypatch.setattr(M, "manifest_file", lambda p, r: proot / "manifest.json")
    return proot


def _write_output(proot, content: str = OUT_CONTENT):
    out = proot / OUT_REL
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    return out


def _load(proot) -> dict:
    return json.loads((proot / "manifest.json").read_text(encoding="utf-8"))


def test_manifest_roundtrip_valid(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)

    manifest = M.build_manifest("comstock", "2025-3", [_doc()], None, [], {}, _state(), 1)

    assert manifest["product"] == "comstock" and manifest["release"] == "2025-3"
    art = manifest["sources"][0]["artifacts"][0]
    assert art["input_sha256"] == "deadbeef"  # traced to the hashed source input
    assert art["output_sha256"]  # output hashed at build time
    assert art["output_path"] == OUT_REL
    assert manifest["clones"][0]["sha"] == "abc123"  # commit provenance recorded
    assert manifest["counts"]["chunks"] == 1

    assert M.validate_manifest("comstock", "2025-3", manifest) == []
    assert M.validate_release("comstock", "2025-3") is True


def test_validate_fails_when_output_deleted(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    out = _write_output(proot)
    M.build_manifest("comstock", "2025-3", [_doc()], None, [], {}, _state(), 1)

    out.unlink()  # artifact vanishes after build
    errors = M.validate_manifest("comstock", "2025-3", _load(proot))
    assert any("missing on disk" in e for e in errors)
    assert M.validate_release("comstock", "2025-3") is False


def test_validate_fails_when_output_tampered(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    out = _write_output(proot)
    M.build_manifest("comstock", "2025-3", [_doc()], None, [], {}, _state(), 1)

    out.write_text(OUT_CONTENT + "\nEDITED AFTER BUILD\n", encoding="utf-8")
    errors = M.validate_manifest("comstock", "2025-3", _load(proot))
    assert any("hash mismatch" in e for e in errors)


def test_validate_fails_on_orphan_output(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    # fetch hashed a different input, so this doc's output traces to nothing
    state = _state(input_path="documentation/reference_doc/other_chapter.tex")
    M.build_manifest("comstock", "2025-3", [_doc()], None, [], {}, state, 1)

    errors = M.validate_manifest("comstock", "2025-3", _load(proot))
    assert any("no hashed source input" in e for e in errors)


def test_validate_fails_on_release_mismatch(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    M.build_manifest("comstock", "2025-3", [_doc()], None, [], {}, _state(), 1)

    errors = M.validate_manifest("comstock", "2025-4", _load(proot))
    assert any("release tag mismatch" in e for e in errors)


def test_validate_fails_on_zero_artifacts(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    M.build_manifest("comstock", "2025-3", [], None, [], {}, _state(), 0)

    errors = M.validate_manifest("comstock", "2025-3", _load(proot))
    assert any("zero artifacts" in e for e in errors)


def test_validate_fails_on_untracked_crosswalk_measure(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    M.build_manifest("comstock", "2025-3", [_doc()], None, [], {}, _state(), 1)

    # an undocumented measure that is NOT listed as a tracked gap must fail validation
    (proot / "crosswalk.json").write_text(
        json.dumps(
            {
                "counts": {"measures": 2, "covered": 1, "gaps": 0},
                "measures": [
                    {"measure_id": "good_0001", "doc_kind": "external_pdf"},
                    {"measure_id": "bad_0002", "doc_kind": "none"},
                ],
                "gaps": [],
            }
        ),
        encoding="utf-8",
    )
    errors = M.validate_manifest("comstock", "2025-3", _load(proot))
    assert any("bad_0002" in e and "neither covered nor a tracked gap" in e for e in errors)


def test_gaps_and_unreachable_pdfs_recorded(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    state = _state()
    state["sources"]["upgrade_measures"] = {
        "type": "measures",
        "clone": "ComStock.github.io@HEAD",
        "missing": [{"url": "https://docs.nlr.gov/measures/gone.pdf", "reason": "404"}],
    }
    crosswalk = {
        "counts": {"measures": 1, "covered": 0, "gaps": 1},
        "measures": [{"measure_id": "dr_0005", "doc_kind": "none"}],
        "gaps": [{"measure_id": "dr_0005", "reason": "documentation expected soon"}],
    }

    manifest = M.build_manifest("comstock", "2025-3", [_doc()], crosswalk, [], {}, state, 1)

    assert manifest["gaps"]["measures"] == ["dr_0005"]
    assert manifest["gaps"]["unreachable_pdfs"][0]["url"].endswith("gone.pdf")
    # crosswalk.json on disk would let validate confirm dr_0005 is a tracked gap
    (proot / "crosswalk.json").write_text(json.dumps(crosswalk), encoding="utf-8")
    assert M.validate_manifest("comstock", "2025-3", _load(proot)) == []
