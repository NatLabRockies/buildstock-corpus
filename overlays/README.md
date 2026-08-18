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
release: "2025-3"
source_id: upgrade_measures
source_path: docs/upgrade_measures/env_roof_insulation.md

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
release: "2025-3"
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

## Provenance

Two rules keep hand-authored text distinguishable from extracted text:

* **Every injection is labelled in the artifact.** The injected block carries an HTML comment
  naming what it was transcribed from (the image, or the PDF and page), the overlay file, and
  the method. The manifest records the overlay's path, its sha256, and the labels applied next
  to the artifact it patched, plus `counts.overlay_tables` at the top level.
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

## Reviewing

Diff the overlay against the source: the PNG at `sources/<source_id>/…/media/<name>.png` for
an image-anchored entry, or `page` of the PDF named by `source_pdf` for a caption-anchored
one. Then:

```bash
uv run bsc build --product comstock --release 2025-3
uv run bsc validate --product comstock --release 2025-3
uv run python scripts/audit_md_fidelity.py
```

The audit's orphaned-caption count for the affected extractor should drop by the number of
tables applied, and `dangling` must stay at zero.
