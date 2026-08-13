"""Manifest provenance invariants — the governance guarantee the whole corpus rests on:
no output artifact without a hashed source input + matching release tag, every recorded
output present on disk with its recorded hash, every crosswalk measure covered or a gap.

processed_root / manifest_file are monkeypatched to a tmp dir so these run hermetically.
"""

from __future__ import annotations

import hashlib
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


def test_sampled_build_is_stamped_partial(tmp_path, monkeypatch):
    """A capped smoke-test build must never read as the record for this release tag."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)

    manifest = M.build_manifest(
        "comstock", "2025-3", [_doc()], None, [], {}, _state(), 1, None, 1
    )

    assert manifest["sample"] == {"per_category": 1, "partial": True}
    # still a valid, fully traced manifest — just an explicitly partial one
    assert M.validate_manifest("comstock", "2025-3", manifest) == []
    assert M.validate_release("comstock", "2025-3") is True


def test_full_build_has_no_sample_key(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)

    manifest = M.build_manifest("comstock", "2025-3", [_doc()], None, [], {}, _state(), 1)

    assert "sample" not in manifest


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


# --- overlay provenance: a hand-authored table must trace to the bitmap it was read from --

OV_REL = "upgrade_measures/docs/upgrade_measures/env_roof_insulation.yaml"
PNG_BYTES = b"\x89PNG\r\n\x1a\nnot-a-real-png-just-stable-bytes"


def _overlay_fixture(tmp_path, monkeypatch, proot, *, png: bytes | None = PNG_BYTES):
    """An artifact with one applied overlay table, plus the sidecar and image on disk.

    `png=None` leaves the image absent, which is the state of a fresh clone:
    .gitignore excludes processed/**/*.png, so the pictures are simply not there.
    """
    ov_root = tmp_path / "overlays"
    monkeypatch.setattr(M, "OVERLAYS_DIR", ov_root)
    ov_abs = ov_root / OV_REL
    ov_abs.parent.mkdir(parents=True, exist_ok=True)
    ov_abs.write_text(
        "tables:\n"
        '  - label: "Table 1"\n'
        "    source_image: media/roof.png\n"
        f'    source_image_sha256: "{hashlib.sha256(PNG_BYTES).hexdigest()}"\n',
        encoding="utf-8",
        newline="\n",
    )
    if png is not None:
        img = (proot / OUT_REL).parent / "media" / "roof.png"
        img.parent.mkdir(parents=True, exist_ok=True)
        img.write_bytes(png)
    return {
        "path": OV_REL,
        "sha256": hashlib.sha256(ov_abs.read_bytes()).hexdigest(),
        "tables_applied": ["Table 1"],
    }


def _manifest_with_overlay(proot, overlay: dict) -> dict:
    manifest = M.build_manifest(
        "comstock", "2025-3", [_doc()], None, [], {}, _state(), 1, None, None,
        {"technical_reference": {"documentation/reference_doc/4_9_hvac.tex": overlay}},
    )
    return manifest


def test_overlay_recorded_and_verified_against_its_source_image(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    overlay = _overlay_fixture(tmp_path, monkeypatch, proot)

    manifest = _manifest_with_overlay(proot, overlay)

    art = manifest["sources"][0]["artifacts"][0]
    assert art["overlay"]["tables_applied"] == ["Table 1"]
    assert manifest["counts"]["overlay_tables"] == 1
    stats: dict = {}
    assert M.validate_manifest("comstock", "2025-3", manifest, stats) == []
    assert stats == {"overlay_checked": 1, "overlay_unverifiable": 0}


def test_absent_source_image_is_unverifiable_not_a_violation(tmp_path, monkeypatch):
    """A fresh clone has the transcription and the manifest but none of the pictures.

    processed/**/*.png is gitignored on purpose (~250 MB, regenerable), so failing here
    would report a provenance break on every clone where there is none.
    """
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    overlay = _overlay_fixture(tmp_path, monkeypatch, proot, png=None)

    manifest = _manifest_with_overlay(proot, overlay)

    stats: dict = {}
    assert M.validate_manifest("comstock", "2025-3", manifest, stats) == []
    assert stats == {"overlay_checked": 0, "overlay_unverifiable": 1}


def test_redrawn_source_image_is_a_violation(tmp_path, monkeypatch):
    """Image present but changed = the transcription no longer describes it. That is a break."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    overlay = _overlay_fixture(tmp_path, monkeypatch, proot, png=PNG_BYTES + b"redrawn")

    errors = M.validate_manifest("comstock", "2025-3", _manifest_with_overlay(proot, overlay))

    assert len(errors) == 1
    assert "source image changed since transcription" in errors[0]


def test_edited_sidecar_is_a_violation(tmp_path, monkeypatch):
    """The shipped table came from the sidecar; if it changed after the build, say so."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    overlay = _overlay_fixture(tmp_path, monkeypatch, proot)
    manifest = _manifest_with_overlay(proot, overlay)
    (tmp_path / "overlays" / OV_REL).write_text("tables: []\n", encoding="utf-8", newline="\n")

    errors = M.validate_manifest("comstock", "2025-3", manifest)

    assert len(errors) == 1
    assert "overlay hash mismatch" in errors[0]
