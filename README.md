# buildstock-corpus

Level 1 **AI-ready content pipeline** for the BuildStock domain-knowledge corpus.

Ingests a single dataset release (starting with **ComStock 2025-3**) and emits clean,
machine-readable, **release-tagged** artifacts plus a provenance **manifest** and a
queryable local **RAG index** — so retrieval options can be tested without locking in a
vector store. Every artifact is tied to its source hash and dataset release; nothing is
published without provenance.

## Requirements

- [`uv`](https://docs.astral.sh/uv/) (manages Python 3.12 and all deps)
- `git` (sources are fetched by cloning tagged repos)

## Usage

```bash
uv run bsc fetch     --release 2025-3   # download + hash raw sources -> raw/
uv run bsc build     --release 2025-3   # extract -> normalize -> chunks + manifest -> processed/
uv run bsc index     --release 2025-3   # embed chunks -> index/
uv run bsc query "How does ComStock determine HVAC system type?" --release 2025-3
uv run bsc validate  --release 2025-3   # enforce provenance invariants
```

### Smoke test

To check the pipeline end to end without building the whole corpus, cap the documents per
category and send the output to a sandbox root:

```bash
uv run bsc build --release 2025-3 --sample 1 --work-dir .smoketest   # 1 doc per category
uv run bsc validate --release 2025-3 --work-dir .smoketest
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
- `index/<product>-<release>/` — persistent Chroma store (gitignored)
