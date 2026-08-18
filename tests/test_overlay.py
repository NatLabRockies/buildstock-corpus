"""Sidecar overlay injection, in both anchor modes: an image-anchored transcription replaces
the bitmap ref it was read from, a caption-anchored one is inserted below a caption that the
extractor left with nothing under it. Every failure mode degrades to a warning that leaves
the body untouched.

The pinned hash is the point of most of these tests — an overlay that no longer matches the
image or the PDF revision it was transcribed from must not silently ship.
"""

from __future__ import annotations

import hashlib

import pytest
import yaml

import buildstock_corpus.overlay as O
import buildstock_corpus.paths as P
from buildstock_corpus.normalize import Document

RELEASE = "comstock_amy2018_2025_release_3"

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
        release=RELEASE,
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
        # (source_id, source_path) -> the dir that document's image refs resolve against.
        image_dirs = {
            ("upgrade_measures", f"docs/upgrade_measures/{name}.md"): clone
            / "docs"
            / "upgrade_measures"
            for name in ("env_roof", "env_walls")
        }
        input_shas = {"upgrade_measures": {}}
        image = png
        sha = hashlib.sha256(png.read_bytes()).hexdigest()

        def write(self, tables, source_path="docs/upgrade_measures/env_roof.md", **top):
            path = P.overlay_file("comstock", RELEASE, "upgrade_measures", source_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                yaml.safe_dump({"product": "comstock", "release": RELEASE, **top,
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
    return O.apply_overlays(docs, "comstock", RELEASE, env.image_dirs, env.input_shas)


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
    assert rec["path"] == (
        f"comstock_{RELEASE}/upgrade_measures/docs/upgrade_measures/env_roof.yaml"
    )


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


def test_flat_cache_image_is_found_by_basename(env):
    """A PDF's refs name a per-document subdir that does not exist yet at build time.

    docling writes `86103_images/x.png` into the body but keeps the bitmaps flat in the
    conversion cache, so the ref only resolves once the images are copied out — after
    overlays run. Falling back to the basename is what makes the pin verifiable.
    """
    flat = env.image.parent.parent  # docs/upgrade_measures — roof.png is one level down
    (flat / "roof.png").write_bytes(env.image.read_bytes())
    body = BODY.replace("![](media/roof.png)", "![](86103_images/roof.png)")
    env.write([env.entry(source_image="86103_images/roof.png")])
    doc = _doc(body)
    applied, warnings = _apply([doc], env)

    assert warnings == [] and applied
    assert TABLE in doc.body


# --- caption-anchored mode: nothing followed the caption, so there is no ref to replace ----

PDF_SHA = "a" * 64
PDF_PATH = "measure_pdfs/89040.pdf"
PDF_BODY = """## 3 Modeling Approach

Sizing results are given in Table 1.

Table 1. Roof Construction Types

## 4 Results

Energy savings are reported below.
"""


def _pdf_doc(body: str = PDF_BODY) -> Document:
    return Document(
        product="comstock",
        release=RELEASE,
        source_id="upgrade_measures",
        source_type="pdf",
        source_path=PDF_PATH,
        title="VRF Upsizing",
        body=body,
    )


@pytest.fixture
def pdf_env(env):
    """`env`, plus a caption-anchored entry writer and the fetch-recorded input hash."""
    env.input_shas["upgrade_measures"][PDF_PATH] = PDF_SHA

    def entry(**kw):
        base = {
            "label": "Table 1",
            "caption": "Roof Construction Types",
            "source_pdf": PDF_PATH,
            "source_pdf_sha256": PDF_SHA,
            "page": 25,
            "method": "vision-transcription",
            "markdown": TABLE,
        }
        return {**base, **kw}

    env.pdf_entry = entry
    return env


def test_caption_anchored_table_is_inserted_below_the_caption(pdf_env):
    pdf_env.write([pdf_env.pdf_entry()], source_path=PDF_PATH)
    doc = _pdf_doc()
    applied, warnings = _apply([doc], pdf_env)

    assert warnings == []
    assert TABLE in doc.body
    # provenance names the page, since there is no bitmap to name
    assert f"<!-- table recovered from {PDF_PATH} p.25" in doc.body
    lines = doc.body.split("\n")
    assert (
        lines.index("Table 1. Roof Construction Types")
        < lines.index("| Building Type | Construction |")
        < lines.index("## 4 Results")
    )
    rec = applied["upgrade_measures"][PDF_PATH]
    assert rec["tables_applied"] == ["Table 1"]


def test_caption_anchored_injection_is_idempotent(pdf_env):
    """Re-running the build must not stack a second copy under the same caption."""
    pdf_env.write([pdf_env.pdf_entry()], source_path=PDF_PATH)
    doc = _pdf_doc()
    _apply([doc], pdf_env)
    once = doc.body

    applied, warnings = _apply([doc], pdf_env)
    assert doc.body == once and once.count(TABLE) == 1
    assert applied == {} and warnings == []


def test_stale_source_pdf_hash_warns_and_changes_nothing(pdf_env):
    """Upstream reissued the PDF: the page the table was read from may not exist any more."""
    pdf_env.write([pdf_env.pdf_entry(source_pdf_sha256="b" * 64)], source_path=PDF_PATH)
    doc = _pdf_doc()
    applied, warnings = _apply([doc], pdf_env)

    assert applied == {} and doc.body == PDF_BODY
    assert "source PDF changed since transcription" in warnings[0]


def test_unknown_input_hash_is_refused(pdf_env):
    """No recorded input hash means the pin cannot be checked, so it is not trusted."""
    del pdf_env.input_shas["upgrade_measures"][PDF_PATH]
    pdf_env.write([pdf_env.pdf_entry()], source_path=PDF_PATH)
    doc = _pdf_doc()
    applied, warnings = _apply([doc], pdf_env)

    assert applied == {} and doc.body == PDF_BODY
    assert "cannot verify source_pdf_sha256" in warnings[0]


def test_caption_anchored_entry_must_pin_a_page(pdf_env):
    """Without the page there is no way to re-find what was transcribed."""
    entry = pdf_env.pdf_entry()
    del entry["page"]
    pdf_env.write([entry], source_path=PDF_PATH)
    applied, warnings = _apply([_pdf_doc()], pdf_env)

    assert applied == {}
    assert "missing required field 'page'" in warnings[0]


def test_caption_anchored_overlay_is_flagged_redundant_if_a_table_is_there(pdf_env):
    """A later docling can extract these; then the overlay should be retired, not stacked."""
    body = PDF_BODY.replace("## 4 Results", f"{TABLE}\n\n## 4 Results")
    pdf_env.write([pdf_env.pdf_entry()], source_path=PDF_PATH)
    doc = _pdf_doc(body)
    applied, warnings = _apply([doc], pdf_env)

    assert applied == {} and doc.body == body
    assert "overlay is redundant" in warnings[0]


def test_a_neighbours_table_does_not_make_our_overlay_look_redundant(pdf_env):
    """The 96598 shape: a dense caption pair where only the second one kept its table.

    Table 1's caption is followed by a citation stub, then Table 2's caption, then Table 2's
    table. An undirected proximity window reaches that table and refuses Table 1's overlay as
    redundant — silently leaving the gap the overlay exists to close. The scan is bounded by the
    next caption for exactly this case.
    """
    body = PDF_BODY.replace(
        "## 4 Results",
        f"Table from [11]\n\nTable 2. Wall Construction Types\n\n{TABLE}\n\n## 4 Results",
    )
    pdf_env.write([pdf_env.pdf_entry()], source_path=PDF_PATH)
    doc = _pdf_doc(body)
    applied, warnings = _apply([doc], pdf_env)

    assert warnings == [] and applied
    lines = doc.body.split("\n")
    assert (
        lines.index("Table 1. Roof Construction Types")
        < lines.index("| Building Type | Construction |")
        < lines.index("Table 2. Wall Construction Types")
    )


def test_a_sub_numbered_title_between_caption_and_table_still_reads_as_redundant(pdf_env):
    """The 89128 shape: the table's own printed title sits between caption and table.

    "**TABLE 6.5.1.1.3A ...**" matches the caption pattern but is not the next caption, so it
    must not stop the scan — otherwise the document looks table-less and gets a second,
    duplicate copy injected under the same caption.
    """
    body = PDF_BODY.replace(
        "## 4 Results",
        f"**TABLE 6.5.1.1.3A Roof Construction Options**\n\n{TABLE}\n\n## 4 Results",
    )
    pdf_env.write([pdf_env.pdf_entry()], source_path=PDF_PATH)
    doc = _pdf_doc(body)
    applied, warnings = _apply([doc], pdf_env)

    assert applied == {} and doc.body == body
    assert "overlay is redundant" in warnings[0]


def test_a_heading_between_caption_and_table_stops_the_scan(pdf_env):
    """A table under the *next section's* heading is not this caption's table."""
    body = PDF_BODY.replace("## 4 Results", f"## 4 Results\n\n{TABLE}")
    pdf_env.write([pdf_env.pdf_entry()], source_path=PDF_PATH)
    doc = _pdf_doc(body)
    applied, warnings = _apply([doc], pdf_env)

    assert warnings == [] and applied
    lines = doc.body.split("\n")
    assert lines.index("| Building Type | Construction |") < lines.index("## 4 Results")


def test_entry_naming_neither_anchor_is_refused(pdf_env):
    entry = pdf_env.pdf_entry()
    del entry["source_pdf"]
    del entry["source_pdf_sha256"]
    pdf_env.write([entry], source_path=PDF_PATH)
    applied, warnings = _apply([_pdf_doc()], pdf_env)

    assert applied == {}
    assert "neither 'source_image' nor 'source_pdf'" in warnings[0]


# --- replace mode: the extractor emitted a table, and got it wrong -------------------------
#
# The shape below is 96598's: docling shifted the reading order by one caption, so Table 1's
# caption has nothing under it while Table 1's grid sits under the Table 2 caption. Both grids
# are present and both are mislabelled, which no insert can fix.

GRID_A = "| Energy Code | 1A | 2A |\n|---|---|---|\n| Pre-1980 | 10 | 10 |"
GRID_B = "| Energy Code | 1 | 2 |\n|---|---|---|\n| DEER 2020 | 25 | 29 |"
FIXED_A = "| Roof Type | Energy Code | 1A | 2A |\n|---|---|---|---|\n| Attic | Pre-1980 | 10 | 10 |"
FIXED_B = "| Roof Type | Energy Code | 1 | 2 |\n|---|---|---|---|\n| IEAD | DEER 2020 | 25 | 29 |"

SHIFTED_BODY = f"""## 3 Modeling Approach

Table 1. Roof R-Value for Non-California Buildings

Table from [11]

Table 2. Roof R-Value for California Buildings

{GRID_A}

Table from [23]

{GRID_B}

## 4 Results
"""


def _fp(table: str) -> str:
    return O._table_fingerprint(table.split("\n"))


def _replacer(pdf_env, label, markdown, table_sha, why="docling put it under the next caption"):
    return pdf_env.pdf_entry(
        label=label,
        markdown=markdown,
        method="pdf-text-layer",
        replaces={"table_sha256": table_sha, "why": why},
    )


def test_replacement_removes_the_wrong_table_and_inserts_under_the_right_caption(pdf_env):
    pdf_env.write(
        [_replacer(pdf_env, "Table 1", FIXED_A, _fp(GRID_A))], source_path=PDF_PATH
    )
    doc = _pdf_doc(SHIFTED_BODY)
    applied, warnings = _apply([doc], pdf_env)

    assert warnings == []
    assert GRID_A not in doc.body  # the mislabelled grid is gone, not left alongside
    assert FIXED_A in doc.body
    lines = doc.body.split("\n")
    assert (
        lines.index("Table 1. Roof R-Value for Non-California Buildings")
        < lines.index("| Roof Type | Energy Code | 1A | 2A |")
        < lines.index("Table 2. Roof R-Value for California Buildings")
    )
    assert applied["upgrade_measures"][PDF_PATH]["tables_applied"] == ["Table 1"]


def test_replacement_says_in_the_artifact_that_it_overruled_the_extractor(pdf_env):
    """A reader who never opens the sidecar still sees that this overrode extracted text."""
    pdf_env.write(
        [_replacer(pdf_env, "Table 1", FIXED_A, _fp(GRID_A), why="dropped the Roof Type column")],
        source_path=PDF_PATH,
    )
    doc = _pdf_doc(SHIFTED_BODY)
    _apply([doc], pdf_env)

    assert "supersedes the extractor's own table here" in doc.body
    assert _fp(GRID_A)[:12] in doc.body
    assert "dropped the Roof Type column" in doc.body


def test_both_halves_of_a_shifted_pair_are_repaired_without_index_drift(pdf_env):
    """Sequential replacements each re-find their caption, so removals cannot shift the next."""
    pdf_env.write(
        [
            _replacer(pdf_env, "Table 1", FIXED_A, _fp(GRID_A)),
            _replacer(pdf_env, "Table 2", FIXED_B, _fp(GRID_B)),
        ],
        source_path=PDF_PATH,
    )
    doc = _pdf_doc(SHIFTED_BODY)
    applied, warnings = _apply([doc], pdf_env)

    assert warnings == []
    assert applied["upgrade_measures"][PDF_PATH]["tables_applied"] == ["Table 1", "Table 2"]
    lines = doc.body.split("\n")
    assert (
        lines.index("Table 1. Roof R-Value for Non-California Buildings")
        < lines.index("| Roof Type | Energy Code | 1A | 2A |")
        < lines.index("Table 2. Roof R-Value for California Buildings")
        < lines.index("| Roof Type | Energy Code | 1 | 2 |")
        < lines.index("## 4 Results")
    )
    # the prose between the two captions is left where the extractor put it
    assert doc.body.index("Table from [11]") < doc.body.index("Table from [23]")


def test_fingerprint_ignores_padding_and_delimiter_width(pdf_env):
    """The pin tracks values, not formatting, or reflowing a table alone would trip it."""
    padded = "|  Energy Code  |  1A  | 2A |\n|---------------|------|----|\n| Pre-1980 | 10 | 10 |"
    assert _fp(padded) == _fp(GRID_A)

    pdf_env.write([_replacer(pdf_env, "Table 1", FIXED_A, _fp(padded))], source_path=PDF_PATH)
    doc = _pdf_doc(SHIFTED_BODY)
    _, warnings = _apply([doc], pdf_env)
    assert warnings == [] and FIXED_A in doc.body


def test_fingerprint_changes_when_a_column_is_dropped():
    """The failure this pin exists to catch has to actually change the hash."""
    lost_column = "| Energy Code | 1A |\n|---|---|\n| Pre-1980 | 10 |"
    assert _fp(lost_column) != _fp(GRID_A)


def test_replacement_is_refused_when_the_extracted_table_changed(pdf_env):
    pdf_env.write([_replacer(pdf_env, "Table 1", FIXED_A, "b" * 64)], source_path=PDF_PATH)
    doc = _pdf_doc(SHIFTED_BODY)
    applied, warnings = _apply([doc], pdf_env)

    assert applied == {}
    assert doc.body == SHIFTED_BODY
    assert "the extracted body changed" in warnings[0]


def test_a_fingerprint_miss_under_a_now_populated_caption_reads_as_maybe_fixed(pdf_env):
    """Distinguishing this from the case above is what stops a better extraction being lost."""
    pdf_env.write([_replacer(pdf_env, "Table 1", FIXED_A, "b" * 64)], source_path=PDF_PATH)
    doc = _pdf_doc(PDF_BODY.replace("## 4 Results", f"{TABLE}\n\n## 4 Results"))
    applied, warnings = _apply([doc], pdf_env)

    assert applied == {}
    assert "the extractor may have fixed this" in warnings[0]


def test_an_ambiguous_fingerprint_replaces_nothing(pdf_env):
    """Two tables with the same values: the pin does not say which, so it removes neither."""
    pdf_env.write([_replacer(pdf_env, "Table 1", FIXED_A, _fp(GRID_A))], source_path=PDF_PATH)
    twice = SHIFTED_BODY.replace(GRID_B, GRID_A)
    doc = _pdf_doc(twice)
    applied, warnings = _apply([doc], pdf_env)

    assert applied == {}
    assert doc.body == twice
    assert "matches 2 extracted tables" in warnings[0]


def test_replacement_requires_a_stated_reason(pdf_env):
    entry = _replacer(pdf_env, "Table 1", FIXED_A, _fp(GRID_A))
    del entry["replaces"]["why"]
    pdf_env.write([entry], source_path=PDF_PATH)
    doc = _pdf_doc(SHIFTED_BODY)
    applied, warnings = _apply([doc], pdf_env)

    assert applied == {} and doc.body == SHIFTED_BODY
    assert "'replaces' is missing required field 'why'" in warnings[0]


def test_a_reason_cannot_truncate_the_provenance_comment(pdf_env):
    """`why` lands inside an HTML comment, so it must not be able to close it early."""
    pdf_env.write(
        [_replacer(pdf_env, "Table 1", FIXED_A, _fp(GRID_A), why="oops --> escaped")],
        source_path=PDF_PATH,
    )
    doc = _pdf_doc(SHIFTED_BODY)
    applied, warnings = _apply([doc], pdf_env)

    assert applied == {} and doc.body == SHIFTED_BODY
    assert "would truncate the provenance comment" in warnings[0]


def test_a_stale_pdf_hash_still_blocks_a_replacement(pdf_env):
    """The source pin gates replacements too — this is the mode that deletes text."""
    entry = _replacer(pdf_env, "Table 1", FIXED_A, _fp(GRID_A))
    entry["source_pdf_sha256"] = "c" * 64
    pdf_env.write([entry], source_path=PDF_PATH)
    doc = _pdf_doc(SHIFTED_BODY)
    applied, warnings = _apply([doc], pdf_env)

    assert applied == {} and doc.body == SHIFTED_BODY
    assert "source PDF changed since transcription" in warnings[0]


def test_replacement_is_idempotent(pdf_env):
    pdf_env.write([_replacer(pdf_env, "Table 1", FIXED_A, _fp(GRID_A))], source_path=PDF_PATH)
    doc = _pdf_doc(SHIFTED_BODY)
    _apply([doc], pdf_env)
    once = doc.body
    applied, warnings = _apply([doc], pdf_env)

    assert doc.body == once and warnings == [] and applied == {}
    assert once.count(FIXED_A) == 1


# --- text repairs: an extractor artifact that corrupts structure, not table content ---------


def _repair(**kw):
    base = {
        "find": "## Data from [11], [23]",
        "replace": "Data from [11], [23]",
        "why": "docling promoted a source note to a heading, refiling 30 chunks under it",
    }
    return {**base, **kw}


REPAIR_BODY = """## 3.2.4 Roof Insulation Methodology

Table 1. Roof R-Value

## Data from [11], [23]

Energy savings are reported below.
"""


def test_text_repair_demotes_a_mis_parsed_heading(pdf_env):
    pdf_env.write([], source_path=PDF_PATH, text_repairs=[_repair()])
    doc = _pdf_doc(REPAIR_BODY)
    applied, warnings = _apply([doc], pdf_env)

    assert warnings == []
    assert "## Data from [11], [23]" not in doc.body
    assert "\nData from [11], [23]\n" in doc.body
    rec = applied["upgrade_measures"][PDF_PATH]
    assert rec["text_repairs_applied"] == 1 and rec["tables_applied"] == []
    # the reason travels with the change, same rule as a table replacement
    assert f"<!-- text repaired by overlay: comstock_{RELEASE}/" in doc.body
    assert "refiling 30 chunks under it" in doc.body


def test_text_repair_matching_several_lines_is_refused(pdf_env):
    """A find that hits twice is a sweep, not a pin."""
    pdf_env.write([], source_path=PDF_PATH, text_repairs=[_repair()])
    doubled = REPAIR_BODY + "\n## Data from [11], [23]\n"
    doc = _pdf_doc(doubled)
    applied, warnings = _apply([doc], pdf_env)

    assert applied == {} and doc.body == doubled
    assert "matches 2 lines" in warnings[0]


def test_text_repair_matching_nothing_is_refused(pdf_env):
    pdf_env.write([], source_path=PDF_PATH, text_repairs=[_repair(find="## Not present")])
    doc = _pdf_doc(REPAIR_BODY)
    applied, warnings = _apply([doc], pdf_env)

    assert applied == {} and doc.body == REPAIR_BODY
    assert "matches 0 lines" in warnings[0]


def test_text_repair_is_idempotent(pdf_env):
    pdf_env.write([], source_path=PDF_PATH, text_repairs=[_repair()])
    doc = _pdf_doc(REPAIR_BODY)
    _apply([doc], pdf_env)
    once = doc.body
    applied, warnings = _apply([doc], pdf_env)

    assert doc.body == once and warnings == [] and applied == {}


def test_text_repair_survives_a_long_reason(pdf_env):
    """Idempotency walks the comment block, so a wordy `why` cannot re-warn every build."""
    pdf_env.write(
        [], source_path=PDF_PATH, text_repairs=[_repair(why="\n".join(f"line {n}" for n in range(30)))]
    )
    doc = _pdf_doc(REPAIR_BODY)
    _apply([doc], pdf_env)
    _, warnings = _apply([doc], pdf_env)
    assert warnings == []


def test_text_repair_requires_a_stated_reason(pdf_env):
    repair = _repair()
    del repair["why"]
    pdf_env.write([], source_path=PDF_PATH, text_repairs=[repair])
    doc = _pdf_doc(REPAIR_BODY)
    applied, warnings = _apply([doc], pdf_env)

    assert applied == {} and doc.body == REPAIR_BODY
    assert "missing required field 'why'" in warnings[0]


def test_an_overlay_with_neither_tables_nor_repairs_warns(pdf_env):
    pdf_env.write([], source_path=PDF_PATH)
    applied, warnings = _apply([_pdf_doc(REPAIR_BODY)], pdf_env)

    assert applied == {}
    assert "no table entries or text repairs" in warnings[0]


def test_repairs_and_table_entries_compose_in_one_overlay(pdf_env):
    """96598's real shape: a demoted heading and a superseded table in the same sidecar."""
    body = f"""## 3 Modeling Approach

Table 1. Roof R-Value

## Data from [11], [23]

{GRID_A}
"""
    pdf_env.write(
        [_replacer(pdf_env, "Table 1", FIXED_A, _fp(GRID_A))],
        source_path=PDF_PATH,
        text_repairs=[_repair()],
    )
    doc = _pdf_doc(body)
    applied, warnings = _apply([doc], pdf_env)

    assert warnings == []
    rec = applied["upgrade_measures"][PDF_PATH]
    assert rec["tables_applied"] == ["Table 1"] and rec["text_repairs_applied"] == 1
    lines = doc.body.split("\n")
    assert (
        lines.index("Table 1. Roof R-Value")
        < lines.index("| Roof Type | Energy Code | 1A | 2A |")
        < lines.index("Data from [11], [23]")
    )


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
    p = P.overlay_file("comstock", RELEASE, "upgrade_measures", "docs/x/env_roof.md")
    assert p.relative_to(P.OVERLAYS_DIR).as_posix() == (
        f"comstock_{RELEASE}/upgrade_measures/docs/x/env_roof.yaml"
    )


def test_overlay_file_ignores_the_work_dir_sandbox(tmp_path):
    """Overlays are inputs; a sandboxed smoke build must read the real ones."""
    before = P.overlay_file("comstock", RELEASE, "s", "a.md")
    P.use_workspace(tmp_path)
    try:
        assert P.overlay_file("comstock", RELEASE, "s", "a.md") == before
    finally:
        P.use_workspace(None)
