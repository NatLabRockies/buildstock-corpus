"""Sidecar overlay injection: transcribed tables replace the bitmap refs they were read
from, and every failure mode degrades to a warning that leaves the body untouched.

The pinned source_image_sha256 is the point of most of these tests — an overlay that no
longer matches the image it was transcribed from must not silently ship.
"""

from __future__ import annotations

import hashlib

import pytest
import yaml

import buildstock_corpus.overlay as O
import buildstock_corpus.paths as P
from buildstock_corpus.normalize import Document

TABLE = "| Building Type | Construction |\n|---|---|\n| Hospital | IEAD |"

BODY = """# 3.  ComStock Baseline Approach

As shown in Table 1, most buildings are assumed to use IEAD roofs.

Table 1. Roof Construction Types

![](media/roof.png)

\\*Except pre-1980, which assumes IEAD
"""


def _doc(body: str = BODY, source_path: str = "docs/upgrade_measures/env_roof.md") -> Document:
    return Document(
        product="comstock",
        release="2025-3",
        source_id="upgrade_measures",
        source_type="measures",
        source_path=source_path,
        title="Roof Insulation",
        body=body,
    )


@pytest.fixture
def env(tmp_path, monkeypatch):
    """An overlays/ root and a clone holding the source image, both redirected to tmp.

    Both module globals need patching: overlay_file() reads paths.OVERLAYS_DIR, while
    apply_overlays() uses its own imported reference to relativize the recorded path.
    """
    overlays = tmp_path / "overlays"
    monkeypatch.setattr(P, "OVERLAYS_DIR", overlays)
    monkeypatch.setattr(O, "OVERLAYS_DIR", overlays)

    clone = tmp_path / "clone"
    media = clone / "docs" / "upgrade_measures" / "media"
    media.mkdir(parents=True)
    png = media / "roof.png"
    png.write_bytes(b"\x89PNG pretend bitmap")

    class Env:
        root = overlays
        clone_dirs = {"upgrade_measures": clone}
        image = png
        sha = hashlib.sha256(png.read_bytes()).hexdigest()

        def write(self, tables, source_path="docs/upgrade_measures/env_roof.md", **top):
            path = P.overlay_file("comstock", "2025-3", "upgrade_measures", source_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                yaml.safe_dump({"product": "comstock", "release": "2025-3", **top,
                                "tables": tables}),
                encoding="utf-8",
            )
            return path

        def entry(self, **kw):
            base = {
                "label": "Table 1",
                "caption": "Roof Construction Types",
                "source_image": "media/roof.png",
                "source_image_sha256": self.sha,
                "method": "vision-transcription",
                "markdown": TABLE,
            }
            return {**base, **kw}

    return Env()


def _apply(docs, env):
    return O.apply_overlays(docs, "comstock", "2025-3", env.clone_dirs)


def test_injects_table_and_drops_the_image_ref(env):
    env.write([env.entry()])
    doc = _doc()
    applied, warnings = _apply([doc], env)

    assert warnings == []
    assert TABLE in doc.body
    assert "![](media/roof.png)" not in doc.body
    # provenance is visible in the artifact, not just the manifest
    assert "<!-- table recovered from media/roof.png" in doc.body
    assert "method: vision-transcription" in doc.body
    # the table lands under its caption, not somewhere else in the doc
    lines = doc.body.split("\n")
    assert lines.index("| Building Type | Construction |") > lines.index(
        "Table 1. Roof Construction Types"
    )


def test_records_what_was_applied_for_the_manifest(env):
    path = env.write([env.entry()])
    applied, _ = _apply([_doc()], env)

    rec = applied["upgrade_measures"]["docs/upgrade_measures/env_roof.md"]
    assert rec["tables_applied"] == ["Table 1"]
    assert rec["sha256"] == hashlib.sha256(path.read_bytes()).hexdigest()
    assert rec["path"] == "comstock_2025-3/upgrade_measures/docs/upgrade_measures/env_roof.yaml"


@pytest.mark.parametrize("ref", ["media/roof.png", "./media/roof.png"])
def test_matches_both_image_ref_spellings(env, ref):
    """The same page mixes `media/x.png` and `./media/x.png` for one file."""
    env.write([env.entry()])
    doc = _doc(BODY.replace("![](media/roof.png)", f"![]({ref})"))
    _apply([doc], env)
    assert TABLE in doc.body


def test_caption_label_matching_ignores_case_and_style(env):
    """Captions arrive as `**Table 1.**` or `TABLE 1:` depending on the converter."""
    env.write([env.entry()])
    doc = _doc(BODY.replace("Table 1. Roof", "**TABLE 1:** Roof"))
    _apply([doc], env)
    assert TABLE in doc.body


def test_prose_mention_of_a_table_is_not_treated_as_the_caption(env):
    """"As shown in Table 1, ..." precedes the real caption and must not be matched."""
    env.write([env.entry()])
    doc = _doc()
    _apply([doc], env)
    prose = "As shown in Table 1, most buildings are assumed to use IEAD roofs."
    assert prose in doc.body  # untouched
    assert doc.body.index(TABLE) > doc.body.index(prose)


def test_stale_source_image_warns_and_changes_nothing(env):
    """Upstream redrew the picture: the transcription is no longer known-good."""
    env.write([env.entry()])
    env.image.write_bytes(b"\x89PNG a different bitmap")
    doc = _doc()
    applied, warnings = _apply([doc], env)

    assert applied == {}
    assert doc.body == BODY
    assert len(warnings) == 1
    assert "source image changed since transcription" in warnings[0]


def test_missing_source_image_warns_and_changes_nothing(env):
    env.write([env.entry()])
    env.image.unlink()
    doc = _doc()
    applied, warnings = _apply([doc], env)

    assert applied == {} and doc.body == BODY
    assert "source image not found" in warnings[0]


def test_unpinned_entry_is_refused(env):
    """An entry with no hash cannot be verified, so it is not trusted."""
    entry = env.entry()
    del entry["source_image_sha256"]
    env.write([entry])
    doc = _doc()
    applied, warnings = _apply([doc], env)

    assert applied == {} and doc.body == BODY
    assert "no source_image_sha256" in warnings[0]


def test_missing_caption_warns_that_the_overlay_is_stale(env):
    env.write([env.entry(label="Table 7")])
    doc = _doc()
    applied, warnings = _apply([doc], env)

    assert applied == {} and doc.body == BODY
    assert "caption not found" in warnings[0]


def test_missing_required_field_warns(env):
    entry = env.entry()
    del entry["markdown"]
    env.write([entry])
    applied, warnings = _apply([_doc()], env)

    assert applied == {}
    assert "missing required field 'markdown'" in warnings[0]


def test_release_mismatch_is_skipped(env):
    """An overlay tagged for another release must not leak into this one."""
    env.write([env.entry()], release="2024-2")
    doc = _doc()
    applied, warnings = _apply([doc], env)

    assert applied == {} and doc.body == BODY
    assert "tagged release='2024-2'" in warnings[0]


def test_injection_is_idempotent(env):
    """Re-applying over an already-injected body is a no-op, not a duplicate table."""
    env.write([env.entry()])
    doc = _doc()
    _apply([doc], env)
    once = doc.body

    applied, warnings = _apply([doc], env)
    assert doc.body == once
    assert once.count(TABLE) == 1
    assert applied == {} and warnings == []


def test_extractor_now_handles_the_table_so_overlay_is_flagged_redundant(env):
    """If the caption already has a real table and no image, say so instead of guessing."""
    env.write([env.entry()])
    doc = _doc(BODY.replace("![](media/roof.png)", TABLE))
    applied, warnings = _apply([doc], env)

    assert applied == {}
    assert "overlay is redundant" in warnings[0]


def test_multiple_tables_in_one_document(env):
    body = BODY + "\nTable 2. DEER Roof R-Values\n\n![](media/deer.png)\n"
    (env.image.parent / "deer.png").write_bytes(b"\x89PNG second bitmap")
    sha2 = hashlib.sha256((env.image.parent / "deer.png").read_bytes()).hexdigest()
    second = "| Zone | R |\n|---|---|\n| 5A | 21 |"
    env.write([
        env.entry(),
        env.entry(label="Table 2", source_image="media/deer.png",
                  source_image_sha256=sha2, markdown=second),
    ])
    doc = _doc(body)
    applied, warnings = _apply([doc], env)

    assert warnings == []
    assert TABLE in doc.body and second in doc.body
    rec = applied["upgrade_measures"]["docs/upgrade_measures/env_roof.md"]
    assert rec["tables_applied"] == ["Table 1", "Table 2"]


def test_oversized_single_table_is_applied_but_flagged(env):
    """Wide tables are meant to be decomposed in the overlay; warn if one still runs over."""
    wide = "| a | b |\n|---|---|\n" + "\n".join(["| x | y |"] * 400)
    env.write([env.entry(markdown=wide)])
    doc = _doc()
    applied, warnings = _apply([doc], env)

    assert wide in doc.body  # applied — losing the table would be worse
    assert applied  # and recorded, so the manifest still traces it
    assert "over the 1400-char chunk limit" in warnings[0]


def test_decomposed_sub_tables_are_not_flagged_on_total_size(env):
    """The limit applies per paragraph: chunk._pack only hard-splits a single paragraph.

    A table decomposed into blank-line-separated sub-tables may exceed 1400 chars in total
    and still survive intact, so measuring the whole block would reject correct overlays.
    """
    sub = "| a | b |\n|---|---|\n" + "\n".join(["| x | y |"] * 60)
    decomposed = "\n\n".join(f"**Group {n}**\n\n{sub}" for n in range(1, 4))
    assert len(decomposed) > O._CHUNK_MAX_CHARS  # the whole block is over...
    env.write([env.entry(markdown=decomposed)])
    doc = _doc()
    applied, warnings = _apply([doc], env)

    assert applied and warnings == []  # ...but no single paragraph is
    # and the chunker agrees: every sub-table survives with its header attached
    from buildstock_corpus.chunk import chunk_document

    for text in (c.text for c in chunk_document(doc)):
        assert text.count("|---|---|") == text.count("| a | b |")


def test_documents_without_an_overlay_are_untouched(env):
    env.write([env.entry()])
    other = _doc(source_path="docs/upgrade_measures/env_walls.md")
    applied, warnings = _apply([other], env)

    assert applied == {} and warnings == []
    assert other.body == BODY


def test_no_overlay_root_at_all_is_not_an_error(env):
    """A release with no overlays builds exactly as before."""
    applied, warnings = _apply([_doc()], env)
    assert applied == {} and warnings == []


def test_overlay_file_path_mirrors_output_layout():
    """Overlays sit at the same relative position as the artifact they patch."""
    p = P.overlay_file("comstock", "2025-3", "upgrade_measures", "docs/x/env_roof.md")
    assert p.relative_to(P.OVERLAYS_DIR).as_posix() == (
        "comstock_2025-3/upgrade_measures/docs/x/env_roof.yaml"
    )


def test_overlay_file_ignores_the_work_dir_sandbox(tmp_path):
    """Overlays are inputs; a sandboxed smoke build must read the real ones."""
    before = P.overlay_file("comstock", "2025-3", "s", "a.md")
    P.use_workspace(tmp_path)
    try:
        assert P.overlay_file("comstock", "2025-3", "s", "a.md") == before
    finally:
        P.use_workspace(None)
