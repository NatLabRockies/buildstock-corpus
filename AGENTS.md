# buildstock-corpus — for agents (Claude Code, Codex, Gemini CLI, and any other)

This repo holds the **AI-ready BuildStock corpus**: clean, release-tagged markdown
extracted from ComStock's documentation, with a provenance manifest.

## Start here

**Read `processed/<product>/<release>/CORPUS_MAP.md` first**, currently
[processed/comstock/comstock_amy2018_2025_release_3/CORPUS_MAP.md](processed/comstock/comstock_amy2018_2025_release_3/CORPUS_MAP.md).

It lists every document with its title, path, sections and last-updated date, plus a
measure → upgrade-id → document routing table and the corpus's known gaps. One read there
tells you which file to open; without it you are grepping 114 files blind.

## Reading without a clone

If you can fetch URLs but have no checkout, every file under `processed/` is served raw:

```
https://raw.githubusercontent.com/NatLabRockies/buildstock-corpus/<ref>/processed/<product>/<release>/<path>
```

- **Pin `<ref>` to a release tag** (`<release id>-v<N>`, first one
  `comstock_amy2018_2025_release_3-v1`); until tags exist, to a commit hash. `main` moves
  on every rebuild.
- **Fetch `index.json` first** (~6 KB over the wire): every document and measure with its
  `corpus_path`, `status`, `source_url`, `publication_url` and `bytes`. Then the one
  document you need. Fetch `sections.json` only to land on a heading by line range.
- **Check `bytes` before fetching.** 40 documents are over 100 KB; Appendix A is 437 KB.
  Read a line range rather than the whole file.
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

It re-downloads every source PDF and can invalidate the hand-authored overlay hash pins in
`overlays/`, which is how transcribed tables prove they match their source. Everything
under `processed/` is already committed — you do not need to fetch or build to read it.

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

One thing validation does **not** cover: the Chroma index under `index/` (gitignored) is
never opened by `bsc validate`, so it can be silently out of date. Re-run `bsc index` after
any build that changed `chunks.jsonl`.
