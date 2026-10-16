# buildstock-corpus — for agents (Claude Code, Codex, Gemini CLI, and any other)

This repo holds the **AI-ready BuildStock corpus**: clean, release-tagged markdown
extracted from ComStock's documentation, with a provenance manifest.

## Start here

Two start orders, one per kind of reader:

- **With a clone, read `processed/<product>/<release>/CORPUS_MAP.md` first**, currently
  [processed/comstock/comstock_amy2018_2025_release_3/CORPUS_MAP.md](processed/comstock/comstock_amy2018_2025_release_3/CORPUS_MAP.md).
- **Fetching URLs without a clone, fetch `index.json` first**, at a release tag; see
  "Reading without a clone" below. `CORPUS_MAP.md` is the same contents as readable prose.

The map lists every document with its title, path, sections and last-updated date, plus a
measure → upgrade-id → document routing table and the corpus's known gaps. One read there
tells you which file to open; without it you are grepping 118 files blind.

## Reading without a clone

If you can fetch URLs but have no checkout, every file under `processed/` is served raw:

```
https://raw.githubusercontent.com/NatLabRockies/buildstock-corpus/<ref>/processed/<product>/<release>/<path>
```

- **Pin `<ref>` to a release tag** (`<release id>-v<N>`). The current tag is
  `comstock_amy2018_2025_release_3-v3`; the newest is always the top entry of `CHANGELOG.md`
  and the "Current" line of `llms.txt`. `main` moves on every rebuild.
- **Fetch `index.json` first** (~155 KB raw, ~20 KB gzip-compressed over the wire): every
  document and measure with its `corpus_path`, `status`, `source_url`, `publication_url`,
  `bytes`, and the document's section files (`sections_dir` + `section_files`, one per H2,
  the slug being the heading). Then fetch the one section you need,
  `<sections_dir>/<name>`, a few KB with its own citable line-1 header that also names the
  parent `corpus_path` and `lines`; or the whole document. `sections.json` adds every
  heading's level and line range, and is only needed for those.
- **Check `bytes` before fetching a whole document.** 41 documents are over 100 KB;
  Appendix A is 437 KB. Fetch the section file instead, or read a line range.
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
- **The corpus is one dataset release.** Do not mix facts across releases; the release tag
  is part of every claim.

## Citing

Every document's line 1 names its publication `status`, both URLs and the `corpus_version`.
How to cite depends on the status:

- **`osti_pdf`** — a report with an OSTI number. Cite the `publication_url` (the OSTI URL);
  it is the publication of record and does not depend on this corpus.
- **`site_page`** — a page or PDF the ComStock site publishes without an OSTI number. Cite
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

If you changed something and need to regenerate:

```bash
uv run bsc map      --release comstock_amy2018_2025_release_3   # seconds, needs no raw/
uv run bsc validate --release comstock_amy2018_2025_release_3   # provenance invariants
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
