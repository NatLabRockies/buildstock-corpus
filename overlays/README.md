# Overlays — hand-authored content the extractors cannot recover

Some upstream measure pages embed their dense tables as **pictures**. The extracted markdown
keeps the caption and an image link:

```
Table 1. Roof Construction Types

![](media/1d093dd8864b636f6dd02a3d70bcc1c1.png)
```

so the numbers survive only inside the bitmap — invisible to retrieval, while the
surrounding prose keeps cross-referencing the table. No extractor change fixes this,
because the text is not in the input.

An overlay is a YAML sidecar holding a markdown transcription of each such table.
`bsc build` injects it in place of the image ref (see
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

`label` is what locates the insertion point; `caption` is documentation for reviewers.

## Provenance

Two rules keep hand-authored text distinguishable from extracted text:

* **Every injection is labelled in the artifact.** The replacement carries an HTML comment
  naming the source image, the overlay file, and the method. The manifest records the
  overlay's path, its sha256, and the labels applied next to the artifact it patched, plus
  `counts.overlay_tables` at the top level.
* **A transcription is only trustworthy for the image it was made from.**
  `source_image_sha256` is checked at build time and again by `bsc validate`. If upstream
  redraws or repoints the picture, the hash stops matching and the build reports a stale
  overlay instead of shipping numbers that no longer match their source.

Nothing here aborts a build. A missing caption, a moved image, a stale hash, or a malformed
sidecar degrades to a warning and leaves the body untouched.

## Writing a transcription

1. **Composite the PNG onto white before reading it.** Several of these bitmaps are RGBA
   with transparent row fills that are white-intended. On a dark background whole rows
   disappear — roof Table 9 looks like 8 rows and is actually 17.
2. **Flatten what GFM cannot express.** Two-row headers become
   `Group: Column`; merged cells are repeated or the group is split.
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
   image are already in the document; repeating them in the overlay double-counts them.

## Reviewing

Diff the overlay against the source PNG at
`sources/<source_id>/…/media/<name>.png`, then:

```bash
uv run bsc build --product comstock --release 2025-3
uv run bsc validate --product comstock --release 2025-3
uv run python scripts/audit_md_fidelity.py
```

The audit's orphaned-caption count for the affected extractor should drop by the number of
tables applied, and `dangling` must stay at zero.
