"""Manifest provenance invariants — the governance guarantee the whole corpus rests on:
no output artifact without a hashed source input + matching release tag, every recorded
output present on disk with its recorded hash, every crosswalk measure covered or a gap.

processed_root / manifest_file are monkeypatched to a tmp dir so these run hermetically.
"""

from __future__ import annotations

import hashlib
import json

import pytest

import buildstock_corpus.manifest as M
from buildstock_corpus.normalize import Document

RELEASE = "comstock_amy2018_2025_release_3"

REF_PDF = "https://example.org/site/assets/files/comstock_reference_documentation_2025_3.pdf"
SOURCE_URL = "https://github.com/NatLabRockies/ComStock/blob/abc123/documentation/reference_doc/4_9_hvac.tex"

OUT_REL = "technical_reference/documentation/reference_doc/4_9_hvac.md"
VERSION = "test-v1"
OUT_CONTENT = (
    f"<!-- comstock {RELEASE} | technical_reference"
    f" | documentation/reference_doc/4_9_hvac.tex | status: site_page"
    f" | source_url: {SOURCE_URL} | publication_url: {REF_PDF}"
    f" | corpus_version: {VERSION} -->\n"
    "# HVAC Systems\n\nbody\n"
)
# A header from before any labelled field existed: valid shape, nothing to check against.
OUT_CONTENT_UNVERSIONED = (
    f"<!-- comstock {RELEASE} | technical_reference"
    " | documentation/reference_doc/4_9_hvac.tex -->\n"
    "# HVAC Systems\n\nbody\n"
)


def _doc() -> Document:
    return Document(
        product="comstock",
        release=RELEASE,
        source_id="technical_reference",
        source_type="latex",
        source_path="documentation/reference_doc/4_9_hvac.tex",
        title="HVAC Systems",
        body="# HVAC Systems\n\nbody\n",
        status="site_page",
        source_url=SOURCE_URL,
        publication_url=REF_PDF,
    )


def _state(sha: str = "deadbeef", input_path: str = "documentation/reference_doc/4_9_hvac.tex") -> dict:
    return {
        "clones": [
            {
                "repo": "https://github.com/NatLabRockies/ComStock.git",
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
    # Pin the default so these never shell out to git, and so the fixture header above
    # matches what build_manifest records when no version is passed.
    monkeypatch.setattr(M, "default_corpus_version", lambda: VERSION)
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

    manifest = M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)

    assert manifest["product"] == "comstock" and manifest["release"] == RELEASE
    art = manifest["sources"][0]["artifacts"][0]
    assert art["input_sha256"] == "deadbeef"  # traced to the hashed source input
    assert art["output_sha256"]  # output hashed at build time
    assert art["output_path"] == OUT_REL
    assert manifest["clones"][0]["sha"] == "abc123"  # commit provenance recorded
    assert manifest["counts"]["chunks"] == 1
    assert manifest["corpus_version"] == VERSION  # defaulted, and agrees with the header

    assert M.validate_manifest("comstock", RELEASE, manifest) == []
    assert M.validate_release("comstock", RELEASE) is True


def test_explicit_corpus_version_is_recorded(tmp_path, monkeypatch):
    """A release build names its tag up front; the manifest must carry exactly that."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot, OUT_CONTENT.replace(VERSION, f"{RELEASE}-v1"))

    manifest = M.build_manifest(
        "comstock", RELEASE, [_doc()], None, [], {}, _state(), 1,
        corpus_version=f"{RELEASE}-v1",
    )

    assert manifest["corpus_version"] == f"{RELEASE}-v1"
    assert M.validate_manifest("comstock", RELEASE, manifest) == []


def test_validate_fails_when_header_names_another_version(tmp_path, monkeypatch):
    """Hash agreement is not enough: the header must name the manifest's own build."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot, OUT_CONTENT.replace(VERSION, "other-v9"))

    manifest = M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)

    errors = M.validate_manifest("comstock", RELEASE, manifest)
    assert len(errors) == 1
    assert "other-v9" in errors[0] and VERSION in errors[0]


def test_validate_fails_when_header_has_no_fields(tmp_path, monkeypatch):
    """A file from a pre-field build is a provenance gap, reported field by field."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot, OUT_CONTENT_UNVERSIONED)

    manifest = M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)

    errors = M.validate_manifest("comstock", RELEASE, manifest)
    assert sorted(e.rsplit("names no ", 1)[1] for e in errors) == [
        "corpus_version", "publication_url", "source_url", "status",
    ]


def test_validate_fails_when_a_header_field_differs_from_its_row(tmp_path, monkeypatch):
    """Hash agreement is not enough: each header field must say what the row says."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot, OUT_CONTENT.replace(f"publication_url: {REF_PDF}", "publication_url: https://example.org/other.pdf"))

    manifest = M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)

    errors = M.validate_manifest("comstock", RELEASE, manifest)
    assert len(errors) == 1
    assert "header publication_url 'https://example.org/other.pdf'" in errors[0]
    assert REF_PDF in errors[0]


def test_manifest_refuses_a_document_without_links(tmp_path, monkeypatch):
    """Links are resolved by build onto the Document; a row with blanks is never written."""
    _patch(tmp_path, monkeypatch)
    doc = _doc()
    doc.source_url = None
    with pytest.raises(ValueError, match="no source_url/publication_url"):
        M.build_manifest("comstock", RELEASE, [doc], None, [], {}, _state(), 1)


def test_artifact_status_is_recorded(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)

    manifest = M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)

    assert manifest["sources"][0]["artifacts"][0]["status"] == "site_page"
    assert M.validate_manifest("comstock", RELEASE, manifest) == []


def test_validate_fails_on_missing_or_unknown_status(tmp_path, monkeypatch):
    """Citation guidance keys on status, so an artifact without a valid one cannot be cited."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    manifest = M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)
    art = manifest["sources"][0]["artifacts"][0]

    art["status"] = None
    errors = M.validate_manifest("comstock", RELEASE, manifest)
    assert len(errors) == 1 and "status None" in errors[0]

    art["status"] = "draft_pdf"  # a value the vocabulary no longer has
    errors = M.validate_manifest("comstock", RELEASE, manifest)
    # the row is wrong, and the (correct) header now disagrees with it
    assert len(errors) == 2
    assert any("'draft_pdf' is not one of" in e for e in errors)
    assert any("header status 'site_page' != manifest 'draft_pdf'" in e for e in errors)


def test_artifact_links_and_version_are_recorded(tmp_path, monkeypatch):
    """A row copied out of the manifest must say where its source and publication live,
    and which build it belongs to, without the rest of the manifest."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)

    manifest = M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)

    art = manifest["sources"][0]["artifacts"][0]
    assert art["source_url"] == SOURCE_URL  # verbatim from the Document build resolved
    assert art["publication_url"] == REF_PDF
    assert art["corpus_version"] == manifest["corpus_version"] == VERSION
    assert M.validate_manifest("comstock", RELEASE, manifest) == []


def test_validate_fails_on_a_missing_or_relative_link(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    manifest = M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)
    art = manifest["sources"][0]["artifacts"][0]

    art["publication_url"] = "assets/files/ref.pdf"
    errors = M.validate_manifest("comstock", RELEASE, manifest)
    # the row is wrong, and the (correct) header disagrees with it
    assert len(errors) == 2 and all("publication_url" in e for e in errors)

    art["publication_url"] = REF_PDF
    del art["source_url"]
    errors = M.validate_manifest("comstock", RELEASE, manifest)
    assert len(errors) == 1 and "source_url" in errors[0]


def test_validate_fails_when_a_row_names_another_build(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    manifest = M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)
    manifest["sources"][0]["artifacts"][0]["corpus_version"] = "other-v9"

    errors = M.validate_manifest("comstock", RELEASE, manifest)
    assert len(errors) == 1 and "row corpus_version 'other-v9'" in errors[0]


def test_validate_fails_when_manifest_has_no_version(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)

    manifest = M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)
    del manifest["corpus_version"]

    errors = M.validate_manifest("comstock", RELEASE, manifest)
    assert errors == ["manifest has no corpus_version"]


def test_sampled_build_is_stamped_partial(tmp_path, monkeypatch):
    """A capped smoke-test build must never read as the record for this release tag."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)

    manifest = M.build_manifest(
        "comstock", RELEASE, [_doc()], None, [], {}, _state(), 1, None, 1
    )

    assert manifest["sample"] == {"per_category": 1, "partial": True}
    # still a valid, fully traced manifest — just an explicitly partial one
    assert M.validate_manifest("comstock", RELEASE, manifest) == []
    assert M.validate_release("comstock", RELEASE) is True


def test_full_build_has_no_sample_key(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)

    manifest = M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)

    assert "sample" not in manifest


def test_validate_fails_when_output_deleted(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    out = _write_output(proot)
    M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)

    out.unlink()  # artifact vanishes after build
    errors = M.validate_manifest("comstock", RELEASE, _load(proot))
    assert any("missing on disk" in e for e in errors)
    assert M.validate_release("comstock", RELEASE) is False


def test_validate_fails_when_output_tampered(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    out = _write_output(proot)
    M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)

    out.write_text(OUT_CONTENT + "\nEDITED AFTER BUILD\n", encoding="utf-8")
    errors = M.validate_manifest("comstock", RELEASE, _load(proot))
    assert any("hash mismatch" in e for e in errors)


def test_validate_fails_on_orphan_output(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    # fetch hashed a different input, so this doc's output traces to nothing
    state = _state(input_path="documentation/reference_doc/other_chapter.tex")
    M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, state, 1)

    errors = M.validate_manifest("comstock", RELEASE, _load(proot))
    assert any("no hashed source input" in e for e in errors)


def test_validate_fails_on_release_mismatch(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)

    errors = M.validate_manifest("comstock", "2025-4", _load(proot))
    assert any("release tag mismatch" in e for e in errors)


def test_validate_fails_on_zero_artifacts(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    M.build_manifest("comstock", RELEASE, [], None, [], {}, _state(), 0)

    errors = M.validate_manifest("comstock", RELEASE, _load(proot))
    assert any("zero artifacts" in e for e in errors)


def test_validate_fails_on_untracked_crosswalk_measure(tmp_path, monkeypatch):
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)

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
    errors = M.validate_manifest("comstock", RELEASE, _load(proot))
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

    manifest = M.build_manifest("comstock", RELEASE, [_doc()], crosswalk, [], {}, state, 1)

    assert manifest["gaps"]["measures"] == ["dr_0005"]
    assert manifest["gaps"]["unreachable_pdfs"][0]["url"].endswith("gone.pdf")
    # crosswalk.json on disk would let validate confirm dr_0005 is a tracked gap
    (proot / "crosswalk.json").write_text(json.dumps(crosswalk), encoding="utf-8")
    assert M.validate_manifest("comstock", RELEASE, _load(proot)) == []


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
        f"source_url: {SOURCE_URL}\n"
        f"publication_url: {REF_PDF}\n"
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
        "comstock", RELEASE, [_doc()], None, [], {}, _state(), 1, None, None,
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
    assert M.validate_manifest("comstock", RELEASE, manifest, stats) == []
    assert stats == {"overlay_checked": 1, "overlay_checked_pdf": 0, "overlay_unverifiable": 0,
                     "sections_checked": 0, "docs_without_sections": 1}


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
    assert M.validate_manifest("comstock", RELEASE, manifest, stats) == []
    assert stats == {"overlay_checked": 0, "overlay_checked_pdf": 0, "overlay_unverifiable": 1,
                     "sections_checked": 0, "docs_without_sections": 1}


def test_redrawn_source_image_is_a_violation(tmp_path, monkeypatch):
    """Image present but changed = the transcription no longer describes it. That is a break."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    overlay = _overlay_fixture(tmp_path, monkeypatch, proot, png=PNG_BYTES + b"redrawn")

    errors = M.validate_manifest("comstock", RELEASE, _manifest_with_overlay(proot, overlay))

    assert len(errors) == 1
    assert "source image changed since transcription" in errors[0]


def test_edited_sidecar_is_a_violation(tmp_path, monkeypatch):
    """The shipped table came from the sidecar; if it changed after the build, say so."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    overlay = _overlay_fixture(tmp_path, monkeypatch, proot)
    manifest = _manifest_with_overlay(proot, overlay)
    (tmp_path / "overlays" / OV_REL).write_text("tables: []\n", encoding="utf-8", newline="\n")

    errors = M.validate_manifest("comstock", RELEASE, manifest)

    assert len(errors) == 1
    assert "overlay hash mismatch" in errors[0]


# --- caption-anchored overlays: pinned to the source document, not to a bitmap -------------


def _pdf_overlay_fixture(tmp_path, monkeypatch, *, pinned_sha: str = "deadbeef") -> dict:
    """An artifact whose overlay table is pinned to the source document's own hash.

    No image is written: that is the point of this anchor. The table was read from a page
    render of a source with no extractable bitmap, so the only thing that can be re-verified
    is that the source revision transcribed is the one this artifact was built from.
    """
    ov_root = tmp_path / "overlays"
    monkeypatch.setattr(M, "OVERLAYS_DIR", ov_root)
    ov_abs = ov_root / OV_REL
    ov_abs.parent.mkdir(parents=True, exist_ok=True)
    ov_abs.write_text(
        f"source_url: {SOURCE_URL}\n"
        f"publication_url: {REF_PDF}\n"
        "tables:\n"
        '  - label: "Table 1"\n'
        '    caption: "Sizing results"\n'
        "    source_pdf: documentation/reference_doc/4_9_hvac.tex\n"
        f'    source_pdf_sha256: "{pinned_sha}"\n'
        "    page: 12\n",
        encoding="utf-8",
        newline="\n",
    )
    return {
        "path": OV_REL,
        "sha256": hashlib.sha256(ov_abs.read_bytes()).hexdigest(),
        "tables_applied": ["Table 1"],
    }


def test_caption_anchored_overlay_verified_against_the_artifacts_input_hash(tmp_path, monkeypatch):
    """Counted separately from image-anchored: it is a different claim, always verifiable."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    overlay = _pdf_overlay_fixture(tmp_path, monkeypatch)

    manifest = _manifest_with_overlay(proot, overlay)

    stats: dict = {}
    assert M.validate_manifest("comstock", RELEASE, manifest, stats) == []
    assert stats == {"overlay_checked": 0, "overlay_checked_pdf": 1, "overlay_unverifiable": 0,
                     "sections_checked": 0, "docs_without_sections": 1}


def test_caption_anchored_overlay_pinned_to_another_revision_is_a_violation(tmp_path, monkeypatch):
    """Upstream reissued the document: the transcription describes a page that may be gone."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    overlay = _pdf_overlay_fixture(tmp_path, monkeypatch, pinned_sha="0ldrevision")

    errors = M.validate_manifest("comstock", RELEASE, _manifest_with_overlay(proot, overlay))

    assert len(errors) == 1
    assert "transcribed from a different revision" in errors[0]


def _write_crosswalk(proot, measures: list[dict], gaps: list[dict] | None = None) -> None:
    (proot / "crosswalk.json").write_text(
        json.dumps({"counts": {}, "measures": measures, "gaps": gaps or []}), encoding="utf-8"
    )


def test_crosswalk_rows_must_point_at_a_manifest_document_and_its_publication(tmp_path, monkeypatch):
    """A covered row's corpus_path has to be a file this manifest records, and its doc_url
    has to be that file's own publication_url; a gap must point nowhere."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    manifest = M.build_manifest("comstock", RELEASE, [_doc()], None, [], {}, _state(), 1)

    _write_crosswalk(proot, [
        {"measure_id": "ok_0001", "doc_kind": "external_pdf", "corpus_path": OUT_REL, "doc_url": REF_PDF},
        {"measure_id": "gap_0002", "doc_kind": "none", "corpus_path": None, "doc_url": None},
    ], gaps=[{"measure_id": "gap_0002"}])
    assert M.validate_manifest("comstock", RELEASE, manifest) == []

    _write_crosswalk(proot, [
        {"measure_id": "lost_0003", "doc_kind": "external_pdf", "corpus_path": "upgrade_measures/nope.md", "doc_url": REF_PDF},
        {"measure_id": "wrong_0004", "doc_kind": "internal_md", "corpus_path": OUT_REL, "doc_url": "https://example.org/elsewhere.pdf"},
        {"measure_id": "gap_0005", "doc_kind": "none", "corpus_path": OUT_REL, "doc_url": None},
    ], gaps=[{"measure_id": "gap_0005"}])
    errors = M.validate_manifest("comstock", RELEASE, manifest)
    assert len(errors) == 3
    assert any("lost_0003" in e and "not a manifest artifact" in e for e in errors)
    assert any("wrong_0004" in e and "publication_url" in e for e in errors)
    assert any("gap_0005" in e and "must not carry" in e for e in errors)


def test_overlay_naming_another_source_is_a_violation(tmp_path, monkeypatch):
    """A sidecar's links must be the artifact's own: a transcription made from a different
    file or revision cannot back the table it injected."""
    proot = _patch(tmp_path, monkeypatch)
    _write_output(proot)
    overlay = _overlay_fixture(tmp_path, monkeypatch, proot)
    ov_abs = M.OVERLAYS_DIR / OV_REL
    ov_abs.write_text(
        ov_abs.read_text(encoding="utf-8").replace(f"source_url: {SOURCE_URL}",
                                                   "source_url: https://github.com/x/y/blob/other/z.tex"),
        encoding="utf-8", newline="\n",
    )
    overlay["sha256"] = hashlib.sha256(ov_abs.read_bytes()).hexdigest()  # as a build would record
    manifest = _manifest_with_overlay(proot, overlay)

    errors = M.validate_manifest("comstock", RELEASE, manifest)
    assert len(errors) == 1
    assert "overlay source_url 'https://github.com/x/y/blob/other/z.tex'" in errors[0]
    assert SOURCE_URL in errors[0]
