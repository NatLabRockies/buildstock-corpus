"""The fidelity audit's caption -> artifact binding.

The binding has to be directional. An undirected "is there a table within N lines" window
reported 0/345 orphaned table captions corpus-wide while 13 tables in measure_pdfs/ had no
text at all: where captions are dense, a caption whose own table was dropped is satisfied by
its neighbour's table. Every case below is reduced from a real document, so a regression here
means the audit has started hiding lost content again.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("audit_md_fidelity", REPO / "scripts" / "audit_md_fidelity.py")
audit_md_fidelity = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(audit_md_fidelity)
A = audit_md_fidelity


def _audit_one(tmp_path: Path, body: str, entry_index: dict | None = None) -> dict:
    """Run the real audit over one document and return its finding (empty dict if clean).

    The leading newline of each triple-quoted body is kept, so reported line numbers line up
    with the literal as written: the first line of content is line 2.

    Every local image the body references is created on disk, as it would be in processed/, so
    a finding holds only what the case is about and not the fixture's own dangling refs.
    """
    body = body.rstrip("\n") + "\n"
    (tmp_path / "doc.md").write_text(body, encoding="utf-8")
    for _, target in A.image_targets(body.split("\n")):
        image = tmp_path / target
        image.parent.mkdir(parents=True, exist_ok=True)
        image.touch()
    findings, _ = A.audit(tmp_path, {}, entry_index or {})
    return findings[0] if findings else {}


def orphans(
    tmp_path: Path, body: str, entry_index: dict | None = None
) -> tuple[list[int], list[int]]:
    """Orphaned (table, figure) caption line numbers for one document."""
    f = _audit_one(tmp_path, body, entry_index)
    if not f:
        return [], []
    return (
        [o["line"] for o in f["orphan_tables"]],
        [o["line"] for o in f["orphan_figures"]],
    )


def figure_entry(source: str, description: str = "", **kw) -> dict:
    """One overlay figures: entry, and the index key the marker below will resolve to."""
    entry = {"source_image": source, "alt": f"alt for {source}", **kw}
    if description:
        entry["description"] = description
    return entry


def entry_index(*entries: dict, sidecar: str = "p_r/src/doc.yaml") -> dict:
    return {(sidecar, e["source_image"]): e for e in entries}


def marker(source: str, sidecar: str = "p_r/src/doc.yaml") -> str:
    """The provenance comment overlay._figure_injection writes above a ref it rewrote."""
    return (
        f"<!-- figure described by overlay: {sidecar}\n"
        f"     source: {source}\n"
        f"     method: vision-description\n"
        f"     described: 2026-08-19 -->"
    )


# --- the shapes that must be reported -----------------------------------------------------

def test_caption_followed_by_bitmap_is_orphaned_despite_a_sibling_table_above(tmp_path):
    """95005.md:429 — the case that motivated the fix.

    The previous caption's table ends 2 lines above and the dropped table's own content is a
    bitmap below. Both an undirected window and a prose-tolerant backward scan accept this.
    """
    tables, _ = orphans(
        tmp_path,
        """
Table 3. Wall Assembly Thermal Performance (Outside California)

| Wall Type | Energy Code | 1A |
|---|---|---|
| Mass | Pre-1980 | 4.3 |

Table 4. Wall Assembly Thermal Performance (Inside California)

![Image](doc_images/image_000002.png)

## 2.4 Roofs
""",
    )
    assert tables == [8]


def test_caption_cannot_borrow_the_next_captions_table(tmp_path):
    """96598.md:393 — Table 5's caption was satisfied by *Table 6's* table five lines down.

    The citation stub docling leaves where the table should be ("Table from [11]") is prose,
    not evidence, and prose must not stop the forward scan either — only the next caption does.
    """
    tables, _ = orphans(
        tmp_path,
        """
Table 5. Baseline Roof R-Value by Roof Type

Table from [11]

Table 6. Baseline Wall R-Value by Wall Type

| Wall Type | CZ1 | CZ2 |
|---|---|---|
| Mass | 5.0 | 5.7 |
""",
    )
    assert tables == [2]


def test_two_captions_sharing_one_image_orphans_the_unbound_one(tmp_path):
    """92502.md:549 — Figure 6 and Figure 7 in a row with a single image under them."""
    _, figures = orphans(
        tmp_path,
        """
Figure 6. Distributions of max daily peak load reduction

Figure 7. Distributions of median daily peak load reduction

![Image](doc_images/image_000007.png)
""",
    )
    assert figures == [2]


def test_figure_caption_with_only_a_table_below_is_orphaned(tmp_path):
    """The wrong kind of artifact is still a decision: a table is not a figure."""
    _, figures = orphans(
        tmp_path,
        """
Figure 3. Narrative description of the upsizing algorithm

| Step | Action |
|---|---|
| 1 | Size to load |
""",
    )
    assert figures == [2]


# --- the shapes that must NOT be reported -------------------------------------------------

def test_caption_above_and_below_its_artifact_both_bind(tmp_path):
    tables, figures = orphans(
        tmp_path,
        """
Table 1. Above its table

| a | b |
|---|---|
| 1 | 2 |

![Image](doc_images/image_000001.png)

Figure 1. Below its image
""",
    )
    assert (tables, figures) == ([], [])


def test_rows_detached_above_their_caption_are_not_a_dropped_table(tmp_path):
    """92618.md:272 — the same silhouette as 95005 above, and the opposite verdict.

    docling put Table 2's three rows *above* its caption and kept a picture of the same
    table below. From the caption's own line the two documents are indistinguishable: table
    above, bitmap below. What separates them is who owns the table above — here prose, so
    these rows are Table 2's and the numbers are in the text; in 95005 a Table 3 caption,
    so Table 4 is genuinely gone. Flagging this one would have us inject an overlay that
    duplicates body text.
    """
    tables, _ = orphans(
        tmp_path,
        """
## 3.3 Greenhouse Gas Emissions

Three electricity grid scenarios are presented to compare the emissions of the baseline.

| Natural gas | 147.3 lb/MMBtu (228.0 kg/MWh) a |
|---|---|
| Propane | 177.8 lb/MMBtu (182.3 kg/MWh) |

Table 2. On-Site Fossil-Fuel Emissions Factors

![Image](doc_images/image_000004.png)

## 3.4 Utility Bills
""",
    )
    assert tables == []


def test_a_chain_of_images_captioned_underneath_orphans_none_of_them(tmp_path):
    """env_roof_insulation.md:222 — why ownership is inferred for tables but not images.

    Every image in this document is captioned below, so every image also has the *previous*
    figure's caption above it. Reading that as ownership — the inference that is correct for
    tables, which this corpus captions above without exception — orphans 8 correctly
    captioned figures corpus-wide.
    """
    _, figures = orphans(
        tmp_path,
        """
![Image](media/f93fbe14.png)

Figure 3. Average roof assembly R-value for each energy code followed

![Image](media/6879600c.png)

Figure 4. Climate zone floor area percentage per energy code followed

# 4. Modeling Approach
""",
    )
    assert figures == []


def test_prose_between_a_caption_and_its_own_table_is_tolerated(tmp_path):
    """Common in the PDF docs — a sentence of setup sits under the caption.

    Forbidding this costs 32 false positives corpus-wide, so prose is not a boundary.
    """
    tables, _ = orphans(
        tmp_path,
        """
Table 4. Wall Assembly Thermal Performance

Values are area-weighted across the applicable floor area of the stock.

| Wall Type | R-Value |
|---|---|
| Mass | 5.0 |
""",
    )
    assert tables == []


def test_overlay_provenance_comment_does_not_sever_caption_from_table(tmp_path):
    """Tolerance 4 — every chunk-1/chunk-2 recovery puts this multi-line block in between."""
    tables, _ = orphans(
        tmp_path,
        """
Table 1. Specifications of Available VRF (HR) Systems

<!-- table recovered from measure_pdfs/86103.pdf p.14
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     method: vision-transcription -->

| manufacturer | Daikin |
|---|---|
| model | VRV |
""",
    )
    assert tables == []


def test_a_decomposed_overlay_injection_is_not_read_as_still_missing(tmp_path):
    """The widest gap an overlay puts between a caption and its first table row — 86599.md:284.

    A wide table is decomposed into bold-labelled sub-tables so chunk._pack cannot split it
    mid-row, and the table's own printed title lines are transcribed as bold lines rather than
    folded into the caption. Provenance comment, blanks, two title lines and a sub-table label
    put the delimiter row twelve lines below the caption, and a WINDOW of 10 reported all three
    of chunk 3's caption-anchored recoveries as still dropped right after applying them.
    """
    tables, _ = orphans(
        tmp_path,
        """
Table 2. Wall Assembly Thermal Performance (Outside California)

<!-- table recovered from measure_pdfs/86599.pdf p.13
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86599.yaml
     method: vision-transcription -->

**Whole Wall Assembly R-value by ASHRAE Climate Zone (ft^2*F*hr/Btu)**

**Includes interior and exterior air films**

**Mass**

| Energy Code | 1A | 2A |
|---|---|---|
| Pre-1980 | 4.3 | 4.3 |
""",
    )
    assert tables == []


def test_section_numbered_in_table_title_is_not_the_next_caption(tmp_path):
    """Tolerance 2 — 89128.md:521.

    docling emits the table's own ASHRAE title between the caption and the table. It matches
    the caption pattern, and reading it as "the next caption" reported a recovered table as
    dropped. Multi-level dotted numbering is what tells the two apart.
    """
    tables, _ = orphans(
        tmp_path,
        """
Table 5 . Economizer Configuration Suggestions in ASHRAE 90.1-2010

**TABLE 6.5.1.1.3A High-Limit Shutoff Control Options for Air Economizers**

| Climate Zones | Allowed Control Types |
|---|---|
| 1a | Fixed dry bulb |
""",
    )
    assert tables == []


def test_subfigure_labels_do_not_sever_image_from_caption(tmp_path):
    """Tolerance 3 — 86103.md:234, a two-panel figure captioned underneath."""
    _, figures = orphans(
        tmp_path,
        """
![Image](doc_images/image_000008.png)

- (a) Three-pipe system example
- (b) Two-pipe system example

Figure 2. Different piping layouts between two- and three-pipe systems
""",
    )
    assert figures == []


def test_list_of_figures_section_is_excluded_even_when_captions_wrap(tmp_path):
    """Tolerance 1 — 95013.md.

    A list-of-figures section repeats every caption with no artifact beside it. The captions
    wrap, so the leader dots land on the *following* line and a dots-on-this-line test misses
    all of them; exclusion has to be driven by the section heading.
    """
    tables, figures = orphans(
        tmp_path,
        """
## List of Figures

Figure 1. ComStock baseline in-force energy code followed as a percentage of
applicable floor area ....................................................... 9

Table 1. Fuels modeled in the ComStock baseline
............................................................................ 11

## 1 Introduction

Prose that mentions Table 1 and Figure 1 without being a caption.
""",
    )
    assert (tables, figures) == ([], [])


def test_fenced_listing_satisfies_a_figure_caption(tmp_path):
    """Some "figures" are code listings, e.g. an EnergyPlus IDF object."""
    _, figures = orphans(
        tmp_path,
        """
Figure 9. EnergyPlus object used to model the lockout

```
Coil:Cooling:DX:SingleSpeed,
```
""",
    )
    assert figures == []


# --- injected figure descriptions are ours, not the document's ----------------------------
#
# The figure-description sweep injects a description paragraph below each ref it rewrites, and
# those routinely *open* like a caption ("Table 2. On-Site Fossil Fuel Emissions Factors...")
# because naming the thing you describe is the natural way to start. Undistinguished, each one
# is counted as a source caption it is not, and each one severs a real caption from the image
# below it. Measured on the completed sweep, that was 425 phantom captions and 15 fabricated
# orphans. Both halves of the fix are needed and neither substitutes for the other: excluding
# descriptions from detection cleared the 8 table cases and none of the figure ones; making
# them walkable cleared the 7 figure cases and none of the table ones.

def test_description_opening_like_a_caption_is_not_counted_as_one(tmp_path):
    """95002.md:397 — docling dropped Table 2's real caption, so the description is the only
    `Table N.` line in the file. Counted, it is a caption for a table that was never there.
    """
    source = "doc_images/image_000003.png"
    description = (
        "Table 2. On-Site Fossil Fuel Emissions Factors, which survives in the extraction "
        "only as a bitmap. Rows: Natural gas 147.3 lb/MMBtu; Propane 177.8 lb/MMBtu."
    )
    f = _audit_one(
        tmp_path,
        f"""
## 3.4  Carbon Emissions Equivalent

Three electricity grid scenarios are presented to compare the emissions.

{marker(source)}

![Table 2 bitmap: on-site fossil fuel emissions factors]({source})

{description}

## 3.5  Limitations and Concerns
""",
        entry_index(figure_entry(source, description)),
    )
    assert f == {}  # neither counted nor orphaned, and no warning


def test_real_caption_severed_from_its_image_by_a_description_still_binds(tmp_path):
    """86105.md:229 — the source caption sits below its image, the description in between.

    The description here does *not* match CAPTION ("Figure 3 (Section 2) compares..." — `(` is
    not in `[.:)]`), so excluding descriptions from detection does nothing for this shape. It
    needs the walkable half: prose that is ours must not sever a caption from its artifact.
    """
    source = "doc_images/image_000009.png"
    description = "Figure 3 (Section 2) compares economizer coverage by building type."
    _, figures = orphans(
        tmp_path,
        f"""
{marker(source)}

![Two-panel stacked bar chart comparing economizer coverage]({source})

{description}

- (a) Coverage in ComStock for each building type

- (b) Coverage in CBECS 2018 for each building type

Figure 3. Economizer floor area coverage between ComStock and CBECS (2018)

## 3  Modeling Approach
""",
        entry_index(figure_entry(source, description)),
    )
    assert figures == []


def test_a_genuinely_dropped_figure_is_still_orphaned_in_a_described_document(tmp_path):
    """The guard against trading false positives for false negatives.

    86105 and 89040 both carry descriptions *and* a genuinely dropped figure. Walking over our
    own prose must not let a caption whose image is gone reach the *described* figure's image.
    """
    source = "doc_images/image_000009.png"
    description = "Figure 3 (Section 2) compares economizer coverage by building type."
    _, figures = orphans(
        tmp_path,
        f"""
{marker(source)}

![Two-panel stacked bar chart comparing economizer coverage]({source})

{description}

Figure 3. Economizer floor area coverage between ComStock and CBECS (2018)

Figure 5. Economizer control types in the baseline building stock

## 3  Modeling Approach
""",
        entry_index(figure_entry(source, description)),
    )
    assert figures == [13]  # Figure 3 binds upward; Figure 5's image was dropped


def test_decorative_entry_leaves_the_table_below_it_intact(tmp_path):
    """85853.md:1101 — the shape that rules out walking down from the marker.

    The engine appends a description only for non-decorative entries, so below a decorative
    ref the next paragraph is the *document's*. Here that is a real markdown table. Marking
    its rows as ours would excuse a caption whose own table is missing — a false negative,
    which is worse than the false positive it replaces.
    """
    decorative = "doc_images/image_000003.png"
    tables, figures = orphans(
        tmp_path,
        f"""
{marker(decorative)}

![Three line icons joined by plus signs]({decorative})

Table 4. Wall Assembly Thermal Performance

| Wall Type | Energy Code | 1A |
|---|---|---|
| Mass | Pre-1980 | 4.3 |

Table 5. Roof Assembly Thermal Performance

![Bitmap of the roof table](doc_images/image_000004.png)
""",
        entry_index(figure_entry(decorative, decorative=True)),
    )
    # Table 4 keeps the table the walk would have swallowed; Table 5's really is gone.
    assert (tables, figures) == ([15], [])


def test_multi_line_description_is_marked_to_its_own_length(tmp_path):
    """89341 / 95014 transcribe a bitmap table inside the description, so the block spans nine
    lines including two blanks. "Up to the next blank" would stop inside it and leave the
    transcribed rows looking like the document's own content.
    """
    source = "doc_images/image_000003.png"
    description = (
        "Table 1. On-Site Fossil Fuel Emissions Factors. Bitmap in the source PDF.\n"
        "\n"
        "| Fuel | Emissions factor |\n"
        "| --- | --- |\n"
        "| Natural gas | 147.3 lb/MMBtu |\n"
        "\n"
        "Footnote as printed: lb = pound; MMBtu = million British thermal units."
    )
    f = _audit_one(
        tmp_path,
        f"""
{marker(source)}

![Table 1 bitmap: on-site fossil fuel emissions factors]({source})

{description}

## 3.5  Limitations
""",
        entry_index(figure_entry(source, description)),
    )
    assert f == {}


def test_description_that_does_not_match_the_sidecar_warns_instead_of_marking(tmp_path):
    """A mismatch means the sidecar and processed/ have drifted, so the file needs a rebuild.

    Guessing which lines are ours from that point is how a false negative gets made, so the
    audit marks nothing and reports the drift as a finding of its own.
    """
    source = "doc_images/image_000003.png"
    f = _audit_one(
        tmp_path,
        f"""
{marker(source)}

![Table 2 bitmap]({source})

Table 2. On-Site Fossil Fuel Emissions Factors — an older wording, since revised.

## 3.5  Limitations
""",
        entry_index(figure_entry(source, "Table 2. On-Site Fossil Fuel Emissions Factors.")),
    )
    assert [w["line"] for w in f["overlay_desc_warnings"]] == [9]
    # Nothing was marked, so the stale line is still read as the document's own caption.
    assert [o["line"] for o in f["orphan_tables"]] == [9]


def test_marker_with_no_matching_overlay_entry_warns(tmp_path):
    """A marker naming a sidecar entry that no longer exists is drift too, not something to
    silently walk past."""
    source = "doc_images/image_000003.png"
    f = _audit_one(
        tmp_path,
        f"""
{marker(source)}

![Some figure]({source})

A paragraph that may or may not be ours.
""",
        entry_index(figure_entry("doc_images/some_other_image.png", "Unrelated.")),
    )
    assert len(f["overlay_desc_warnings"]) == 1


def test_overlay_entry_index_keys_on_the_path_the_marker_writes(tmp_path):
    """The marker writes its sidecar path relative to overlays/, so the index must key that way."""
    sidecar = tmp_path / "comstock_rel_1" / "upgrade_measures" / "measure_pdfs" / "85853.yaml"
    sidecar.parent.mkdir(parents=True)
    sidecar.write_text(
        "product: comstock\n"
        "figures:\n"
        "- source_image: 85853_images/image_000004.png\n"
        "  alt: A chart\n"
        "  description: A description.\n",
        encoding="utf-8",
    )
    index = A.overlay_entry_index(tmp_path, "comstock", "rel_1")
    key = ("comstock_rel_1/upgrade_measures/measure_pdfs/85853.yaml", "85853_images/image_000004.png")
    assert index[key]["description"] == "A description."


# --- the pieces the binding leans on ------------------------------------------------------

def test_comment_lines_covers_multi_line_spans():
    lines = ["a", "<!-- one", "two -->", "b", "<!-- inline -->", "c"]
    assert A.comment_lines(lines) == {1, 2, 4}


@pytest.mark.parametrize(
    "line, subnumbered",
    [
        ("**TABLE 6.5.1.1.3A High-Limit Shutoff**", True),
        ("Table 2.1 Something", True),
        ("Table 2. Specifications for Broilers", False),
        ("Figure 2. Different piping layouts", False),
    ],
)
def test_subnumbered_only_matches_multi_level_numbering(line, subnumbered):
    assert bool(A.SUBNUMBERED.match(line)) is subnumbered


@pytest.mark.parametrize(
    "line, is_label",
    [
        ("- (a) Three-pipe system example", True),
        ("(b) Two-pipe system example", True),
        ("- The system requires a branch controller", False),
        ("- [4] 'Photovoltaics and electricity'", False),
    ],
)
def test_subfigure_label_does_not_swallow_ordinary_bullets(line, is_label):
    assert bool(A.SUBFIGURE.match(line)) is is_label
