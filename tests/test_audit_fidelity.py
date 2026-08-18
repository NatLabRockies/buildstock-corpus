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


def orphans(tmp_path: Path, body: str) -> tuple[list[int], list[int]]:
    """Run the real audit over one document; return orphaned (table, figure) line numbers.

    The leading newline of each triple-quoted body is kept, so reported line numbers line up
    with the literal as written: the first line of content is line 2.
    """
    (tmp_path / "doc.md").write_text(body.rstrip("\n") + "\n", encoding="utf-8")
    findings, _ = A.audit(tmp_path, {})
    if not findings:
        return [], []
    f = findings[0]
    return (
        [o["line"] for o in f["orphan_tables"]],
        [o["line"] for o in f["orphan_figures"]],
    )


# --- the shapes that must be reported -----------------------------------------------------

def test_caption_followed_by_bitmap_is_orphaned_despite_a_sibling_table_above(tmp_path):
    """92618.md:272 / 95005.md:429 — the case that motivated the fix.

    The previous caption's table ends 2 lines above and the dropped table's own content is a
    bitmap below. Both an undirected window and a prose-tolerant backward scan accept this.
    """
    tables, _ = orphans(
        tmp_path,
        """
Table 1. Fuels Modeled

| Fuel | Modeled |
|---|---|
| Natural gas | yes |

Table 2. On-Site Fossil-Fuel Emissions Factors

![Image](doc_images/image_000004.png)

## 3.4 Utility Bills
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
     overlay: comstock_2025-3/upgrade_measures/measure_pdfs/86103.yaml
     method: vision-transcription -->

| manufacturer | Daikin |
|---|---|
| model | VRV |
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
