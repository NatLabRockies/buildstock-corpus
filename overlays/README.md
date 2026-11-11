# Overlays — hand-authored content the extractors cannot recover

Some upstream documents carry their dense tables as **pixels** rather than text. The numbers
then survive only inside a raster region — invisible to retrieval, while the surrounding prose
keeps cross-referencing the table. No extractor change fixes this, because the text is not in
the input.

That loss shows up in two shapes, and there is one anchor mode for each.

**Image-anchored** — the measure markdown pages. The extractor keeps the caption and an image
link:

```
Table 1. Roof Construction Types

![](media/1d093dd8864b636f6dd02a3d70bcc1c1.png)
```

**Caption-anchored** — the measure PDFs. The table is a rasterized region with an empty text
layer, and with OCR disabled docling emits neither a table nor a picture, so nothing at all
follows the caption:

```
Table 4. Sizing Results Before and After Upsizing Allowance

## 4 Results
```

(OCR does read these, but it mis-associates merged cells — collapsing min/max capacity
columns, shifting Notes onto the wrong energy-code row — which trades a visible gap for
plausible wrong numbers. See `_pipeline_options()` in
[`extract/pdf.py`](../src/buildstock_corpus/extract/pdf.py).)

An overlay is a YAML sidecar holding a markdown transcription of each such table. `bsc build`
either replaces the image ref or inserts below the caption, depending on the mode (see
[`src/buildstock_corpus/overlay.py`](../src/buildstock_corpus/overlay.py)), so both
`processed/**.md` and `chunks.jsonl` carry the table. Overlays are **inputs**, versioned
alongside `sources.yml`, not edits to derived output: a rebuild reproduces the fix, and
`--no-overlays` reproduces the pre-overlay output for comparison.

## Layout

```
overlays/<product>_<release>/<source_id>/<source_path with .yaml>
```

mirroring the position of the artifact each one patches, so an overlay is always tied to a
specific dataset release. A release with no overlays builds exactly as before.

## Schema

Both modes share the top-level keys and `label` / `markdown`; they differ only in what the
entry is pinned to. An entry naming neither `source_image` nor `source_pdf` is refused.

**Image-anchored** — replaces the `![](…)` ref below the caption:

```yaml
product: comstock
release: "comstock_amy2018_2025_release_3"
source_id: upgrade_measures
source_path: docs/upgrade_measures/env_roof_insulation.md
source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551…/docs/upgrade_measures/env_roof_insulation.md
publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_roof_insulation.html

tables:
  - label: "Table 1"                 # matched against the caption line in the body
    caption: "Roof Construction Types"
    source_image: media/1d093dd8864b636f6dd02a3d70bcc1c1.png
    source_image_sha256: "de93e539…"  # the bitmap this was transcribed from
    method: vision-transcription
    transcribed_utc: "2026-08-13"
    markdown: |
      | Building Type | Construction Type |
      |---|---|
      | Hospital | IEAD |
```

**Caption-anchored** — inserted below the caption, since there is no ref to replace:

```yaml
product: comstock
release: "comstock_amy2018_2025_release_3"
source_id: upgrade_measures
source_path: measure_pdfs/89040.pdf

tables:
  - label: "Table 4"
    caption: "Sizing Results Before and After Upsizing Allowance"
    source_pdf: measure_pdfs/89040.pdf   # same value as source_path above
    source_pdf_sha256: "28cea1fe…"       # the PDF revision this was read from
    page: 25                             # 1-based, as printed by the PDF reader
    method: vision-transcription
    transcribed_utc: "2026-08-17"
    markdown: |
      | Coil Type | Design Capacity [W] |
      |---|---|
      | Indoor unit 1 VRF cooling coil | 5,251 |
```

`label` is what locates the insertion point; `caption` is documentation for reviewers. `page`
is required in caption-anchored mode — without it a reviewer cannot re-find what was read.
Both `source_pdf` and `page` also appear in the injected provenance comment.

### Superseding a table the extractor got wrong

The two modes above close *gaps*. A caption-anchored entry may instead carry `replaces:`, which
removes a table the extractor did emit and puts the transcription in its place. That is a
stronger act, and it is for a narrower problem: a table that is present, plausible, and wrong.

96598 is the case that forced it. Pages 20, 31 and 32 each carry two tables, and on all three
docling shifted the reading order by one caption — every grid landed under the *next* table's
caption — while dropping the Roof Type / Wall Type column that the captions name. Nothing was
missing; everything was mislabelled, which a reader has no way to notice. An insert cannot fix
that, because the damage is text that is already there.

```yaml
  - label: "Table 5"
    source_pdf: measure_pdfs/96598.pdf
    source_pdf_sha256: "61294545…"
    page: 20
    method: pdf-text-layer
    replaces:
      table_sha256: "52112627…"   # fingerprint of the extracted table to remove
      why: |
        docling emitted this grid under the Table 6 caption and dropped the Roof
        Type column, so three assemblies ran together as 17 undifferentiated rows.
    markdown: |
      …
```

`table_sha256` is a fingerprint of the extracted table's **values**: each cell stripped, the
delimiter row flattened to one dash per column, then sha256 over the result. Padding and column
width are normalized away so reformatting alone cannot trip it, while a dropped column, a merged
row or a shifted value all change it. Get it from the document you are patching:

```bash
uv run python -c "import sys; sys.path.insert(0,'src'); from pathlib import Path; from buildstock_corpus.overlay import _table_blocks, _table_fingerprint as fp; L=Path(sys.argv[1]).read_text(encoding='utf-8').split('\n'); [print(fp(L[s:e])[:16], f'L{s+1}-{e}', L[s][:60]) for s,e in _table_blocks(L)]" processed/comstock/comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/96598.md
```

The fingerprint locates the table, not its position — position is the thing that is wrong here,
so the entry for `Table 5` legitimately removes a block sitting under the Table 6 caption. It
must match **exactly one** table in the document. Zero matches or several, and nothing is
replaced and the build warns; on zero it distinguishes "this caption now has a table of its own,
so the extractor may have fixed it" from "the extracted body changed" — the first is a reason to
retire the entry, the second a reason to re-derive it. Either way a better extraction is never
silently thrown away.

When the fingerprint matches **more than one** table, the entry may add
`replaces.under_caption: "Table 3"`, naming the caption the misplaced grid sits under; the first
table block below that caption must then be one of the matches, and that one is removed. This is
the shape every measure report has: an executive summary that repeats a results table value for
value (pkg_0012's Table 2 is Table 8), so a shifted summary grid is indistinguishable from the
results grid by values alone. An `under_caption` that is not a caption in the document, or whose
first table below is not a match, replaces nothing and warns.

`why` is **required**, and lands in the artifact next to the table it justifies rather than only
in this sidecar. The redundancy refusal is skipped for these entries: a table under the caption
is the premise, not a reason to back off.

**A table that came out as several grids.** A table that runs over a page break reaches the
markdown as one grid per page. A transcription of the whole table has to supersede all of
them, so `replaces` may list the later grids' fingerprints:

```yaml
    replaces:
      table_sha256: "2c1a0437…"        # the first grid
      also_removes:                    # the continuation grid(s), in any order
        - "b2f5bdf4…"
      why: >-
        Row labels are displaced between rows in both grids; values are right.
```

Each `also_removes` fingerprint must match exactly one other table. If any does not, nothing
is replaced: a partial replacement would leave the transcription beside a stale half of the
table it supersedes.

**A table with no caption.** A measure report's summary table sits under a heading, not a
"Table N." line. Give the entry `uncaptioned: true` and a descriptive `label`:

```yaml
  - label: "Measure Summary"
    uncaptioned: true
    source_pdf: measure_pdfs/96827.pdf
    source_pdf_sha256: "df766d88…"
    page: 9
    replaces:
      table_sha256: "ac675955…"
      why: >-
        Two cells lost their opening sentence.
    markdown: |
      ...
```

The fingerprint alone says which table is meant, and the transcription goes exactly where
that table stood. `replaces:` is therefore required: with no caption and no table to
supersede there is nowhere to put the text. The `label` is written into the provenance
comment, since nothing else in the body names the table.

**Caption labels.** A label is a number (`Table 7`, `Table 7a`) or an appendix label: one or
two letters, an optional hyphen, a number (`Table A-2`, `Figure B1`).

### Repairing a line of extracted text

`text_repairs:` is a top-level list, for extractor artifacts that corrupt document *structure*
rather than table content:

```yaml
text_repairs:
  - find: "## Data from [11], [23]"
    replace: "Data from [11], [23]"
    why: |
      docling promoted this one-line source note to a level-2 heading. The chunker is
      heading-aware, so that filed 30 of this document's chunks under a section named
      "Data from [11], [23]" instead of "3.2.4 Roof Insulation Upgrade Methodology".
```

Whole-line, exact match, and it must match exactly once — `find: "Data from [11], [23]"` as a
substring would also hit the three legitimate copies of that note elsewhere in 96598. A match
count of anything but one is refused with a warning. `why` is required and lands in an HTML
comment above the repaired line. Repairs run before the table entries, since they fix the
headings those entries are located against.

A repair can also delete its line, with `remove: true` in place of `replace`:

```yaml
text_repairs:
  - find: "1.490"
    remove: true
    why: |
      The last value of a Table 4 row, which fell out of its cell and was left as a
      paragraph below the table. The hand-authored Table 4 carries it in its row.
```

This is for a fragment the extractor left outside a table whose transcription now carries
it: a value that fell out of a cell, a spanning header stranded below the grid. The removed
text stays readable in the comment, with the reason. It is not for deleting content that is
nowhere else in the document.

This is deliberately the narrowest tool here. It is not for editing prose, fixing typos (see
"transcribe, don't improve" below), or normalizing characters. Before writing one, scan the
corpus for the pattern: a defect in more than one document is an extractor problem, and belongs
in `extract/`, not in a per-document sidecar. The 96598 repair was written only after a
corpus-wide scan found it to be the release's single citation note promoted to a heading.

`method` is free text and lands verbatim in that comment, so it should name how the values
were actually obtained rather than defaulting to a house style. Three routes are in use:

* `vision-transcription` — read off a render or a bitmap by eye. The only option when the
  region has no text layer at all (86599/86602 Table 2, where the whole table is one
  embedded bitmap).
* `pdf-text-layer` — the region is *classified* as a picture by docling but still has a live
  text layer, so the cells can be recovered exactly with `pymupdf`'s word boxes clustered by
  line. Prefer this whenever it is available: it is not a reading, and a 479×321 cached
  thumbnail is often too coarse to read reliably anyway (95005 Table 4, 576 values).
* A compound like `pdf-text-layer (values) + vision-transcription (product names)` — part of
  the table has a text layer and part does not. 89130's tables are pasted retailer listings
  whose screenshots cover the product names while the specification rows below them stay
  selectable. Say which part came from which; a reviewer checking one number should know
  whether to trust it to the digit or to re-read the picture.

### Recording a table that was checked and found right

Most tables the extractor emits are right, and until now a right table left no trace: a
reviewer could not tell "compared with the PDF and correct" from "never looked at". A
`checked:` entry records the first. Nothing is injected and the artifact does not change.

```yaml
checked:
  - label: "Table 2"                    # the caption the table belongs to
    caption: "Rated Efficiency by Compressor Type"   # documentation for reviewers
    source_pdf: measure_pdfs/96634.pdf  # same value as source_path
    source_pdf_sha256: "77c22cdd…"      # the PDF revision the table was compared with
    page: 12                            # 1-based, where the table is in the PDF
    table_sha256: "63c2673f…"           # fingerprint of the extracted table that was compared
    verdict: correct                    # the only verdict there is; see below
    method: page-render-and-text-layer
    checked_utc: "2026-11-12"
```

* **Pinned from both ends**, as a replacement is. `source_pdf_sha256` must equal the
  artifact's `input_sha256`, and `table_sha256` must match a table in the document (the
  same fingerprint `replaces.table_sha256` uses: cell values, not column padding). A reissued
  PDF, or an extractor that later emits anything different for that table, makes the entry
  stale: the build warns and stops counting it, and `bsc validate` fails if a recorded
  verdict no longer holds. A verdict is about one table as extracted from one PDF revision.
* **`correct` is the only verdict.** A table found wrong is not noted, it is fixed: write a
  `tables:` entry with `replaces:` so the artifact carries the right numbers. A table cannot
  be both checked and hand-authored in the same sidecar.
* **`label` must be a caption in the document**, except for a grid that has none (an acronym
  list, an executive-summary table): give it a descriptive `label` and `uncaptioned: true`,
  and the fingerprint alone identifies it.
* **Get the fingerprint from the build, never by hand:**
  `uv run python scripts/list_tables.py <processed .md>` prints every table with its line,
  size, nearest caption and `table_sha256`, and lists the captions that have no table.

The manifest records the labels under the artifact's overlay as `tables_checked` and counts
them as `counts.overlay_tables_checked`; `bsc validate` reports them on their own line,
because "an extracted table was verified" and "a table was hand-authored" are different
claims.

## Provenance

Two rules keep hand-authored text distinguishable from extracted text:

* **Every injection is labelled in the artifact.** The injected block carries an HTML comment
  naming what it was transcribed from (the image, or the PDF and page), the overlay file, and
  the method. The manifest records the overlay's path, its sha256, and the labels applied next
  to the artifact it patched, plus `counts.overlay_tables` at the top level. An entry that
  *superseded* extracted text says so in that comment, quotes the fingerprint of the block it
  removed, and carries its `why` — "this supplements the extractor" and "this overrules the
  extractor" have to be tellable apart by a reader who never opens the sidecar. Repairs are
  counted separately, as `counts.overlay_text_repairs` and `text_repairs_applied` on the
  artifact, and `bsc validate` reports them on their own line for the same reason.
* **A sidecar names the document it transcribes.** The header's `source_url` (the upstream
  file at the commit the corpus was built from) and `publication_url` (where a reader is sent
  for the human-readable form) are the same two links the document's own line-1 header and
  manifest row carry. They are stamped from the manifest by
  `scripts/stamp_overlay_links.py`, never typed; build skips a sidecar whose links differ
  from its document's, and `bsc validate` reports it. A reader holding only the sidecar can
  therefore open the exact source it was transcribed from.
* **A transcription is only trustworthy for the thing it was made from.** Every entry pins a
  hash, checked at build time and again by `bsc validate`:
  * `source_image_sha256` is re-hashed from the bitmap on disk. If upstream redraws or
    repoints the picture the hash stops matching and the build reports a stale overlay
    instead of shipping numbers that no longer match their source.
  * `source_pdf_sha256` must equal the artifact's own `input_sha256` — the hash `bsc fetch`
    recorded for that PDF. Pinning the value the manifest already carries (rather than
    re-hashing the file) is what makes these verifiable in a fresh clone, where `raw/` is
    gitignored and holds no PDFs at all.

`bsc validate` reports the two counts separately, because they are not the same claim: one
says a bitmap on disk still hashes to what the transcriber saw, the other says the PDF this
artifact was built from is the revision that was transcribed. Absent images are reported as
*unverifiable* rather than as violations — `processed/**/*.png` is gitignored on purpose
(~250 MB, regenerable), so failing on a fresh clone would report a break where there is none.

Nothing here aborts a build. A missing caption, a moved image, a stale hash, a PDF reissued
upstream, or a malformed sidecar degrades to a warning and leaves the body untouched. If a
later docling can extract one of these tables, the build says the overlay is *redundant*
rather than stacking a second copy under the caption — that is the signal to retire the entry.

## Writing a transcription

1. **Composite the PNG onto white before reading it.** Several of these bitmaps are RGBA
   with transparent row fills that are white-intended. On a dark background whole rows
   disappear — roof Table 9 looks like 8 rows and is actually 17.
   For a caption-anchored table there is no bitmap to read: render the page from the PDF
   (`pypdfium2` at ~200 dpi, cropping to the table region for wide ones) and transcribe from
   that. Skip any "List of Tables" page — its entries match the caption pattern too.
2. **Flatten what GFM cannot express, and say what you dropped.** Two-row headers become
   `Group: Column`; merged cells are repeated or the group is split. Cell shading cannot be
   carried at all, so check whether it is load-bearing: a legend, or a colour that encodes
   something no cell value repeats, belongs in a note under the table; fills that merely
   restate a value already in the row, or mark column groups, are dropped — and the sidecar's
   comment block records that they were dropped and why. Same for bold/red emphasis on
   individual values.
3. **Decompose rather than let the chunker split.** `chunk.chunk_document` packs to 1400
   chars and hard-splits any single paragraph over that, stranding rows from their header.
   Blank-line-separated sub-tables each stay intact however long the group runs in total, so
   wide tables are broken into bold-labelled sub-tables along a seam the source already has
   (a column group, an energy-code family). The build warns if a paragraph is still over.
4. **Transcribe, don't improve.** Blank cells stay blank — in stock-average tables a blank
   means the combination is absent from the stock, which is not the same as a dash or a
   zero. Trailing zeros are kept (`2.70`, not `2.7`). Source typos are preserved; these
   files are the citation anchor.
5. **Don't duplicate body text.** Footnotes that survived extraction as prose below the
   image are already in the document; repeating them in the overlay double-counts them. Grep
   the processed `.md` for a distinctive phrase from the footnote before transcribing it.
6. **Record inferences as inferences.** Where a header is implicit — a lower grid whose
   columns are identified only by alignment with the grid above it — transcribe the reading,
   and note in the comment block that it is a reading rather than something printed.
7. **Two tables with the same caption are not necessarily the same table.** Several measure
   PDFs revise a predecessor's table under its original caption, with changed units, changed
   row labels, or changed values. Transcribe each from its own page.

## Checking every table and figure: the ResStock method

ComStock's overlays were written after its first release, for the tables an audit found
missing. ResStock's are written before its first tag, and for every table, missing or not:
the audit only finds captions with nothing under them, and the tables that did the damage in
ComStock were present and wrong. So each measure PDF is worked through whole, once.

For each PDF (`processed/resstock/<release>/upgrade_measures/measure_pdfs/<n>.md`):

1. **List what the extractor produced.** `scripts/list_tables.py` on the processed file:
   every table with its caption and fingerprint, and every table caption with no table.
   `scripts/audit_md_fidelity.py` gives the same for figures.
2. **Render each table's page** from the PDF at 1.5x (`pypdfium2`), and read the PDF's text
   layer for the same page. Skip the "List of Tables" page: its entries match the caption
   pattern too.
3. **Compare the extracted grid with the render and the text layer, cell by cell**: the
   number of rows and columns, every header, every value, and which caption the grid sits
   under. docling's commonest errors are a grid filed under the next table's caption, a
   merged header flattened onto the wrong columns, and a dropped first column.
4. **Record the outcome, one entry per table:**
   * right: a `checked:` entry (above);
   * wrong: a `tables:` entry with `replaces:`, `method: vision-transcription` (or
     `pdf-text-layer` when the text layer was the source), and a `why`;
   * missing (a caption with no table, usually a rasterized table): a caption-anchored
     `tables:` entry.
   A table that spans pages or was split into several grids gets one entry per grid.
   Three things count as wrong even when every value is in the right cell:
   * **a dropped table footnote.** A footnote is part of its table; a marker in a cell that
     points at nothing is a defect. Replace the table and carry the footnote below the grid.
   * **an identifier or URL broken by a line-wrap space** (`..._heating_cap acity`,
     `projec t_national`). A search for the real name, or a click on the link, misses it.
     Replace the table with the extractor's own grid and the name joined, and say so in
     `method`. An ordinary word broken the same way (`ground-to- air`) is left as it is and
     mentioned in the `checked:` note.
   * **a fragment left outside the grid** (a value that fell out of a cell, a spanning
     header stranded below the table). Carry it in the transcription and remove the stray
     line with a `text_repairs` entry (`remove: true`).
5. **Describe every figure that is not decorative**: `alt` plus a `description` to the
   figure standard in `FIGURE_DESCRIPTIONS_ROLLOUT.md` (60 to 70 words: what the figure
   shows and the values a reader would cite), drafted from the page render and edited by
   hand, `method: vision-description`. A caption whose plot docling dropped has no bitmap to
   pin; note it in the sidecar's comment block and list it in the PR.
6. **Stamp the links and rebuild**: `scripts/stamp_overlay_links.py`, then build, validate
   and audit as under Reviewing. Commit one document at a time.

**Not tables: the contents pages.** docling renders a report's Table of Contents, List of
Figures and List of Tables as grids of dot leaders and page numbers. They are navigation for
a paginated document, not content, and are left out of the sweep: no entry is written for
them. The List of Acronyms and the Upgrade Summary table are content and are checked like
any other table, as `uncaptioned` entries.

A PDF is done when every table has a `checked:` or `tables:` entry and every real figure a
description. The technical reference guide's tables come from LaTeX source, not from a
layout model, and are not part of this sweep; its 15 figures are described the same way.

## Reviewing

Diff the overlay against the source: the PNG at `sources/<source_id>/…/media/<name>.png` for
an image-anchored entry, or `page` of the PDF named by `source_pdf` for a caption-anchored
one. Then:

```bash
uv run bsc build --product comstock --release comstock_amy2018_2025_release_3
uv run bsc validate --product comstock --release comstock_amy2018_2025_release_3
uv run python scripts/audit_md_fidelity.py
```

The audit's orphaned-caption count for the affected extractor should drop by the number of
tables applied, and `dangling` must stay at zero.
