# buildstock-corpus — for agents

This repo holds the **AI-ready BuildStock corpus**: clean, release-tagged markdown
extracted from ComStock's documentation, with a provenance manifest.

## Start here

**Read `processed/<product>/<release>/CORPUS_MAP.md` first**, currently
[processed/comstock/comstock_amy2018_2025_release_3/CORPUS_MAP.md](processed/comstock/comstock_amy2018_2025_release_3/CORPUS_MAP.md).

It lists every document with its title, path, sections and last-updated date, plus a
measure → upgrade-id → document routing table and the corpus's known gaps. One read there
tells you which file to open; without it you are grepping 118 files blind.

## Reading the corpus

- **These are plain markdown files — read and grep them directly.** You do not need the
  vector index. `bsc query` exists for consumers *without* filesystem access, and it
  requires a ~1 hour `bsc index` build first.
- **Cite as `source_id/source_path`.** Every processed file opens with an HTML comment
  recording the product, release, source id and upstream path it came from. Quote that,
  not the path under `processed/`, so a citation survives a re-layout.
- **Images are absent from a clone.** `processed/**/*.png` is gitignored (~250 MB,
  regenerable), so image references point at files that are not there. Tables and figures
  marked *hand-authored* in the map were transcribed from those images, so their content is
  present as text even when the picture is not.
- **The corpus is one dataset release.** Do not mix facts across releases; the release tag
  is part of every claim.

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
