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
uv run bsc build     --release $REL   # extract -> normalize -> chunks + manifest -> processed/
uv run bsc index     --release $REL   # embed chunks -> index/
uv run bsc query "How does ComStock determine HVAC system type?" --release $REL
uv run bsc validate  --release $REL   # enforce provenance invariants
```

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
- `processed/<product>/<release>/` — clean markdown, referenced image assets, `crosswalk.json`, `chunks.jsonl`, `manifest.json`
  - `crosswalk.json` maps each measure to its documentation and its upgrade id in this
    release. Every measure also carries `date_last_updated` — when its document last
    changed at its source — alongside the `date_last_updated_source` that established it
    (`pdf_moddate` from the published PDF's own metadata, or `git_commit` from the site
    repo). A measure whose documentation does not exist yet is undated rather than given a
    stand-in.
- `index/<product>-<release>/` — persistent Chroma store (gitignored)
