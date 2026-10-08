# buildstock-corpus

Level 1 **AI-ready content pipeline** for the BuildStock domain-knowledge corpus.

Ingests a single dataset release (starting with **ComStock 2025 release 3**) and emits clean,
machine-readable, **release-tagged** artifacts plus a provenance **manifest** and a
queryable local **RAG index** — so retrieval options can be tested without locking in a
vector store. Every artifact is tied to its source hash and dataset release; nothing is
published without provenance.

## Requirements

- [`uv`](https://docs.astral.sh/uv/) (manages Python 3.12 and all deps)
- `git` (sources are fetched by cloning tagged repos)

## Usage

Releases are named for the OEDI data lake convention,
`<dataset type>_<weather data>_<year of publication>_release_<release number>`, so a corpus
artifact names the same release the published data does. Upstream git tags and branches do
not follow it (`2025-3`, `2025_3`) and are pinned separately in the source registry.

```bash
REL=comstock_amy2018_2025_release_3

uv run bsc fetch     --release $REL   # download + hash raw sources -> raw/
uv run bsc build     --release $REL   # extract -> normalize -> chunks + manifest + map -> processed/
uv run bsc map       --release $REL   # regenerate CORPUS_MAP.md on its own (seconds)
uv run bsc index     --release $REL   # embed chunks -> index/
uv run bsc query "How does ComStock determine HVAC system type?" --release $REL
uv run bsc validate  --release $REL   # enforce provenance invariants
```

That is the **authoring** pipeline, and it is not where a cloner starts. `processed/` is
committed, so a fresh clone already has the corpus — see below. Do not begin with
`bsc fetch`: it re-downloads every source PDF and can invalidate the hand-authored overlay
hash pins that let a transcribed table prove it matches its source.

## Reading the corpus

Start at **`processed/<product>/<release>/CORPUS_MAP.md`**. It lists every document with its
title, path, top-level sections and last-updated date, plus a measure → upgrade-id →
document routing table and the corpus's known gaps — so one read tells you which file to
open instead of grepping 114 of them. `bsc build` writes it, and `bsc map` regenerates it
from the built artifacts in a second or two without touching `raw/`.

Which consumer you are decides what you need:

- **An agent or human with the repo checked out** needs nothing but `processed/`. The
  markdown is committed and citable; read and grep it directly. No index, no API key.
- **A consumer that can fetch URLs but has no clone** (a hosted assistant, an MCP server,
  a clean-room agent) reads the same files over HTTPS: `index.json` first, then one
  document. See [Reading without a clone](#reading-without-a-clone). No index, no API key.
- **A consumer that wants semantic retrieval** needs the vector store: `bsc index` then
  `bsc query`. Budget for it — embedding all 7,731 chunks takes on the order of an hour on
  a laptop CPU, and `index/` is gitignored, so every clone builds its own.
  `bsc query --answer` additionally needs `ANTHROPIC_API_KEY` and the `llm` extra;
  retrieval alone does not.

How to cite a document depends on its publication status; the rules are in
[AGENTS.md § Citing](AGENTS.md#citing). `AGENTS.md` is the canonical instructions file for
agents; `CLAUDE.md` and `GEMINI.md` are one-line pointers that import it, and `llms.txt` at
the root is the discovery file for readers without a clone.

`bsc validate` checks the manifest, the overlays, and whether `CORPUS_MAP.md`, `index.json`
and `sections.json` are stale relative to `manifest.json`. It does **not** open the Chroma
store, so a stale index passes silently — re-run `bsc index` after any build that changed
`chunks.jsonl`.

### Reading without a clone

Every file under `processed/` is served raw by GitHub, unauthenticated:

```
https://raw.githubusercontent.com/NatLabRockies/buildstock-corpus/<ref>/processed/<product>/<release>/<path>
```

**Pin `<ref>` to a release tag**, `<release id>-v<N>` (the first will be
`comstock_amy2018_2025_release_3-v1`). A tag never moves, so a citation made against it
resolves to the same bytes next year. `main` is rewritten on every rebuild; use it only when
you want the newest build and accept that paths and content drift. Until the first tag
exists, pin a commit hash — the one in every file's `corpus_version` is the commit of the
tooling that built it.

The recipe is two fetches, three when you need headings:

1. **`index.json`** (~67 KB raw, ~6 KB over the wire). Every document with its `title`,
   `corpus_path`, `status`, `source_url`, `publication_url` and `bytes`, and every measure
   with its `upgrade_id`, `corpus_path` and `doc_url`. Pick the document; for a measure,
   start from its `upgrade_id` or `measure_id`.
2. **`sections.json`** (~194 KB raw, ~25 KB over the wire), only if you need to land on a
   heading: every heading of every document with `line_start` and `line_end` in the file.
3. **The document**, at `<corpus_path>`. Its line 1 is a provenance header carrying the
   release, upstream path, `status`, both URLs and the `corpus_version`, so the file alone
   is enough to cite. Quote `source_id/source_path` and the `corpus_version`, and send a
   reader to the `publication_url`, not to the markdown.

**Mind the size.** 40 of the 114 documents are over 100 KB and four are over 200 KB; the
largest, the reference documentation's Appendix A, is 437 KB. Check `bytes` in the index
before fetching, and use the line range from `sections.json` to read only the section you
need. Per-section files are planned so that a heading can be fetched on its own.

Both JSON files stamp the `manifest_sha256` they were generated from and validate against
[`schemas/`](schemas/) in this repo; code against the schema, not the example.

### Smoke test

To check the pipeline end to end without building the whole corpus, cap the documents per
category and send the output to a sandbox root:

```bash
uv run bsc build --release $REL --sample 1 --work-dir .smoketest   # 1 doc per category
uv run bsc validate --release $REL --work-dir .smoketest
```

`--sample N` keeps the first N documents of each category (latex, markdown, measures, pdf)
and stamps the manifest `sample: {partial: true}`, so a smoke-test manifest can never be
mistaken for the record of a release. `--work-dir` redirects `processed/` and `index/` only:
`raw/` and the conversion caches stay shared, so the sandbox run reuses fetched sources and
the warm docling cache and leaves the release artifacts untouched.

The heavy extractors (LaTeX via pandoc, PDF via docling) live in an optional extra:

```bash
uv sync --extra extract
```

## Layout

- `sources/<product>_<release>.yaml` — source registry (repos, tag, measure URLs)
- `raw/<product>/<release>/` — downloaded originals (gitignored)
- `processed/<product>/<release>/` — clean markdown, referenced image assets, `CORPUS_MAP.md`, `index.json`, `sections.json`, `crosswalk.json`, `chunks.jsonl`, `manifest.json`
  - `CORPUS_MAP.md` is the entry point for reading the corpus: every document's title,
    path, sections and date, the measure→upgrade-id→document routing table, and the known
    gaps. Generated (never hand-edited) and stamped with the sha256 of the manifest it was
    derived from, so `bsc validate` can tell a current map from a stale one.
  - `index.json` and `sections.json` are the same facts as data, for a consumer that
    fetches the corpus over HTTPS: every document and measure with paths, links, status and
    size; every heading with its line range. Generated beside the map, stamped the same
    way, and validated against `schemas/`.
  - `crosswalk.json` maps each measure to its documentation and its upgrade id in this
    release. Every measure also carries `date_last_updated` — when its document last
    changed at its source — alongside the `date_last_updated_source` that established it
    (`pdf_moddate` from the published PDF's own metadata, or `git_commit` from the site
    repo). A measure whose documentation does not exist yet is undated rather than given a
    stand-in.
- `index/<product>-<release>/` — persistent Chroma store (gitignored)
