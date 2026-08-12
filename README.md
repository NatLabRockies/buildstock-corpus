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
uv run bsc eval                         # score the index against eval/gold_set.yaml
```

The heavy extractors (LaTeX via pandoc, PDF via docling) live in an optional extra:

```bash
uv sync --extra extract
```

## Evaluation

`bsc eval` answers one question: **does the index beat just asking Claude?** The baseline is
what a user would otherwise do — paste the question into a Claude chat — so the comparison
holds the model and generation config fixed and varies only whether the retrieved ComStock
passages are in the prompt.

It runs in three layers, cheapest first:

```bash
uv run bsc eval                    # retrieval only: recall@k, MRR, gold points in context
uv run bsc eval --answer           # + index-backed and bare-Claude answers side by side
uv run bsc eval --judge            # + an LLM judge grading each gold fact per side
```

Layers 2 and 3 need `ANTHROPIC_API_KEY` and `uv sync --extra llm`. Without a key the run
falls back to retrieval only and writes `eval/baseline_prompts.md`, so the bare-Claude side
can be done by hand in claude.ai.

The headline retrieval metric is **gold points in context**: the share of required facts that
appear verbatim in the retrieved passages. It is the ceiling on what retrieval can contribute
— if a number isn't in the passages, no prompting recovers it. The judge's
`baseline_contradictions` count is the sharper argument for retrieval: a confidently wrong
release-specific number is worse than a refusal.

`eval/gold_set.yaml` deliberately keeps questions marked `known_gap: true` — places the corpus
is known *not* to cover (image-only tables, structured artifacts that aren't chunked). They are
excluded from recall@k and reported separately so the summary can't credit the index for
coverage it doesn't have. Results land in `eval/results.json` (tracked, so scores are
comparable across releases).

## Layout

- `sources/<product>_<release>.yaml` — source registry (repos, tag, measure URLs)
- `raw/<product>/<release>/` — downloaded originals (gitignored)
- `processed/<product>/<release>/` — clean markdown, referenced image assets, `crosswalk.json`, `chunks.jsonl`, `manifest.json`
- `index/<product>-<release>/` — persistent Chroma store (gitignored)
