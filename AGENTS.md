# buildstock-corpus — for agents (Claude Code, Codex, Gemini CLI, and any other)

This repo holds the **AI-ready BuildStock corpus**: clean, release-tagged markdown
extracted from the documentation of two products, ComStock and ResStock, with a provenance
manifest. Each product has its own folder, release id and release tag:

| Product | Covers | Folder under `processed/` | Current tag |
|---|---|---|---|
| ComStock | commercial buildings | `comstock/comstock_amy2018_2025_release_3/` (118 documents, 65 measures) | `comstock_amy2018_2025_release_3-v3` |
| ResStock | housing | `resstock/resstock_amy2018_2025_release_1/` (62 documents, 32 measures) | `resstock_amy2018_2025_release_1-v1` |

## Start here

**Pick the product first.** Then two start orders, one per kind of reader:

- **With a clone, read `processed/<product>/<release>/CORPUS_MAP.md` first**:
  [ComStock's map](processed/comstock/comstock_amy2018_2025_release_3/CORPUS_MAP.md) or
  [ResStock's map](processed/resstock/resstock_amy2018_2025_release_1/CORPUS_MAP.md).
- **Fetching URLs without a clone, fetch that product's `index.json` first**, at its release
  tag; see "Reading without a clone" below. `CORPUS_MAP.md` is the same contents as readable
  prose.

The map lists every document with its title, path, sections and last-updated date, plus a
measure → upgrade-id → document routing table and the corpus's known gaps. One read there
tells you which file to open; without it you are grepping 118 files (ComStock) or 62
(ResStock) blind.

## Reading without a clone

If you can fetch URLs but have no checkout, every file under `processed/` is served raw:

```
https://raw.githubusercontent.com/NatLabRockies/buildstock-corpus/<ref>/processed/<product>/<release>/<path>
```

- **Pin `<ref>` to the product's release tag** (`<release id>-v<N>`), from the table
  above; a product's newest tag is its topmost entry in `CHANGELOG.md` and its "Current"
  line in `llms.txt`. A product's folder exists only at its own tags and on `main`: the
  ComStock tag has no ResStock folder. `main` moves on every rebuild.
- **Fetch `index.json` first**, at
  `processed/<product>/<release>/index.json` (ComStock's is ~155 KB raw, ~20 KB
  gzip-compressed over the wire; ResStock's ~85 KB and ~11 KB): every
  document and measure with its `corpus_path`, `status`, `source_url`, `publication_url`,
  `bytes`, and the document's section files (`sections_dir` + `section_files`, one per H2,
  the slug being the heading). Then fetch the one section you need,
  `<sections_dir>/<name>`, usually a few KB, with its own citable line-1 header that also
  names the parent `corpus_path` and `lines`; or the whole document. `sections.json` adds
  every heading's level and line range, H3 and below included; fetch it when the section
  file is large and you need one table's lines (in ResStock's guide chapter 3a, the
  Geometry and Envelope sections are about 60 KB each and hold many housing characteristics,
  one H4 apiece).
- **Check `bytes` before fetching a whole document.** 41 of ComStock's documents and 14 of
  ResStock's are over 100 KB; ComStock's Appendix A is 450 KB and ResStock's largest, the
  report 95032, is 291 KB. Fetch the section file instead, or read a line range.
- Both JSON files validate against `schemas/` in this repo.

## Reading the corpus

- **These are plain markdown files — read and grep them directly.** You do not need the
  vector index. `bsc query` exists for consumers *without* filesystem access, and it
  requires a ~1 hour `bsc index` build first.
- **Cite as `source_id/source_path`.** Every processed file opens with a one-line HTML
  comment recording the product, release, source id and upstream path it came from, plus
  its publication `status`, the `source_url` of the upstream file at its pinned commit, the
  `publication_url` a reader should be sent to, and the `corpus_version` of the build. Line
  1 alone is enough to cite the file. Quote the source id and path, not the path under
  `processed/`, so a citation survives a re-layout.
- **Images are absent from a clone.** `processed/**/*.png` is gitignored (~250 MB,
  regenerable), so image references point at files that are not there. Tables and figures
  marked *hand-authored* in the map were transcribed from those images, so their content is
  present as text even when the picture is not.
- **Each folder is one dataset release of one product.** Do not mix facts across products
  or releases; the release tag is part of every claim. Tables of similar name can sit close
  together (ResStock's Geometry Stories, Geometry Story Bin and Geometry Building Type
  Height): cite the one whose heading matches the question, with its line range.

## Citing

Every document's line 1 names its publication `status`, both URLs and the `corpus_version`.
How to cite depends on the status:

- **`osti_pdf`** — a report with an OSTI number. Cite the `publication_url` (the OSTI URL);
  it is the publication of record and does not depend on this corpus.
- **`site_page`** — a page or PDF the product's site publishes without an OSTI number (ResStock's technical reference guide is one). Cite
  the `publication_url` **and the `corpus_version`**, and say the document has no OSTI
  number. It can be revised in place upstream; the corpus version is what pins the text
  you read.
- **`missing`** — a measure listed in the crosswalk with no documentation. There is nothing
  to cite; say so rather than citing the nearest document.

In every case also name `source_id/source_path` and the `corpus_version`, so the claim
traces to the exact file and build it came from. When quoting a passage from a long
document, add a line range: a section's from `sections.json`, or a retrieved chunk's own
`line_start`–`line_end` (every chunk in `chunks.jsonl` carries them, with its heading path
in `section` and its `corpus_version`).

## Do not run `bsc fetch`

It re-downloads every source PDF, moves every source clone to its ref (a branch ref such
as the site's `main` to the remote tip), and can invalidate the hand-authored overlay hash
pins in `overlays/`, which is how transcribed tables prove they match their source.
Everything under `processed/` is already committed — you do not need to fetch or build to
read it.

If you changed something and need to regenerate, name the product and its release (with two
products registered, `bsc` no longer guesses):

```bash
uv run bsc map      --product comstock --release comstock_amy2018_2025_release_3   # seconds, needs no raw/
uv run bsc validate --product comstock --release comstock_amy2018_2025_release_3   # provenance invariants
uv run bsc map      --product resstock --release resstock_amy2018_2025_release_1
uv run bsc validate --product resstock --release resstock_amy2018_2025_release_1
```

## Provenance is load-bearing

`manifest.json` records the sha256 of every artifact's bytes and `bsc validate` recomputes
them, so **editing anything under `processed/` by hand turns validation red**. Those files
are build output. Change the extractor or an overlay in `overlays/`, then rebuild.

`CORPUS_MAP.md` is likewise generated — it stamps the manifest hash it came from, and
`bsc validate` reports it stale if the manifest has moved on. Regenerate with `bsc map`.

The Chroma index under `index/` (gitignored) is not part of the release record, so a stale
one is a **warning**, not a failure: `bsc validate` says so when the store is older than
`chunks.jsonl` or holds a different number of records. Re-run `bsc index` after any build
that changed `chunks.jsonl`.
