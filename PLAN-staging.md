# buildstock-corpus: staged work list

Companion to [PLAN.md](PLAN.md). Same tasks, ordered so each step has what it needs from the
one before. Tick the status column as steps land. Written 2026-10-06.

Two places this list departs from the order in PLAN.md:

- W2.2 (manifest fields) comes before W2.1 (provenance line), so the header is rendered from
  manifest fields rather than computed a second time.
- W5.2 (chunk line ranges) comes before W5.1 (section files), because section files are
  easier to emit once chunks already know their line ranges.

## Stage 0 · Decisions, no code

| # | Task | What it settles | Size | Status |
|---|------|-----------------|------|--------|
| 1 | Open question | Status of the six site-page measures: check the live URLs, decide `site_page` or not | S | Done 2026-10-06. Pages are live, but left as they are for now. Draft PDFs stay `draft_pdf`, untracked. |
| 2 | Open question | Tag naming: calendar `vYYYY.MM.N` as proposed, or a scheme naming the data release | S | Done 2026-10-06. `<release id>-v<N>`, full id, from `v1`. |
| 3 | Record | Write both answers into PLAN.md, marked confirmed with the date | S | Done 2026-10-06. |

## Stage 1 · A version and a status exist as data

| # | Task | What it does | Size | Status |
|---|------|--------------|------|--------|
| 4 | W1.4 | Write `corpus_version` into manifest, map, and each file header; commit hash until tags exist | S | Done 2026-10-06 on branch `corpus-version` (code `76f3d84`, rebuild commit follows). `bsc build --corpus-version` added; validate checks headers. |
| 5 | W3.1 | Define the status vocabulary (`osti_pdf`, `site_page`, `missing`); declared per source in the YAML, derived per document for measures; in manifest, crosswalk, chunks | S | Done 2026-10-06 on branch `status-field` (code `bc1a784`, rebuild commit follows). |
| 6 | W3.2 | Fold `draft_publications/` into `unpublished_docs/upgrade_measures/`; folder name kept by owner | S | Done 2026-10-06 with step 5. |

## Stage 2 · Every artifact links to its publication

| # | Task | What it does | Size | Status |
|---|------|--------------|------|--------|
| 7 | W2.2 | Add `source_url`, `publication_url`, `status`, `corpus_version` to every manifest row | S | Done 2026-10-07 on `status-field` (code `60076ab`, rebuild commit follows). All 167 links return 200. |
| 8 | W2.1 | Extend the line-1 provenance comment with the fields from step 7; validate fails without `source_url` | S | Done 2026-10-07 on `status-field` (code `4e1f08c`, rebuild commit follows). One line, owner decision. |
| 9 | W2.3 | Crosswalk rows gain `corpus_path` and absolute `doc_url`; keep `doc_target` one release | S | Done 2026-10-07 on `status-field` (code `7ab693f`, rebuild committed). 92504 canonical URL; four webinar decks excluded, 114 docs. |
| 10 | W2.4 | Overlay YAML files carry `source_url` and `publication_url` as fields | S | Done 2026-10-07 on `status-field` (code `8785426`, rebuild committed). All 57 sidecars stamped by script. |
| 11 | W2.5 | CORPUS_MAP.md shows a publication-link column in document and measure tables | S | Done 2026-10-07 on `status-field`. Short status-word labels, owner decision. Map regenerated, no rebuild. |

## Stage 3 · Findable without a clone

| # | Task | What it does | Size | Status |
|---|------|--------------|------|--------|
| 12 | W4.2 | `index.json` + `sections.json` per release, validated against JSON Schemas in `schemas/` | M | Done 2026-10-08 on `status-field`. Two files (owner decision); 30 KB target amended. |
| 13 | W4.1 | "Reading without a clone" section in README and CLAUDE.md: raw URL pattern, pin to a tag, two-fetch recipe | S | Done 2026-10-08 on `status-field`. Raw URL checked unauthenticated. |
| 14 | W4.3 + W3.3 | `AGENTS.md` as canonical, CLAUDE.md as pointer, `llms.txt` at root; citation guidance per status folded in | S | Done 2026-10-08 on `status-field`. GEMINI.md pointer too; README has a one-line pointer to Citing. |
| 15 | W7.1 | `LICENSE`, `CITATION.cff`, `CHANGELOG.md` | S | Done 2026-10-08 on `status-field`. BSD-3 whole repo, sole author, no DOI. Copyright holder to confirm. |

## Stage 4 · First tag

| # | Task | What it does | Size | Status |
|---|------|--------------|------|--------|
| 16 | W1.1 | Rebuild, validate, tag `comstock_amy2018_2025_release_3-v1`, cut the GitHub Release. W1.2 (new build, new tag, `-v2`) becomes the operating rule from here | S | Done 2026-10-08. PR #24 merged (`54f5c05`), tag pushed, release cut, raw URL at tag verified. |

## Stage 5 · Granularity, after the tag or in the same build if time allows

| # | Task | What it does | Size | Status |
|---|------|--------------|------|--------|
| 17 | W5.2 | Chunk metadata: `line_start`, `line_end`, `corpus_version` (heading path stays in `section`) | S | Done 2026-10-08 on `chunk-provenance` (code `8c4556e`, rebuild commit follows). |
| 18 | W5.1 | Section files per H2 for every document, whole file kept as canonical | M | Done 2026-10-08 on `section-files` (code `67479ea` + `267e3ea` flat layout, rebuild commit follows). 2,076 files. |
| 19 | W5.3 | Per-document chunk files beside the single `chunks.jsonl` | S | Done 2026-10-08 on `chunk-files` (code `fadc83e`, rebuild commit follows). 114 files. |
| 20 | W5.4 | Table wrappers carry `data-source` naming the LaTeX table file | S | Done 2026-10-08 on `table-source` (code `43ae2d4`, rebuild committed). 78 wrappers stamped. |
| 21 | W5.5 | Pandoc cleanup: cross-references as quoted titles, heading levels normalized | S | Done 2026-10-08 on `cleanup` (code `0a2f61f`, rebuild commit follows). Shares the branch with step 22. |
| 22 | W6.1 | Omit the undescribed cover-art and wordmark refs of every measure PDF (98); other undescribed figures left visible | S | Done 2026-10-08 on `cleanup` (code `b5faf42`, rebuild commit follows). Narrowed by owner, option 1. |

## Stage 6 · Release tooling

| # | Task | What it does | Size | Status |
|---|------|--------------|------|--------|
| 23 | W1.3 | `bsc changelog --from <tag>` once two tagged manifests exist to diff | M | Done 2026-10-08 on `changelog` (rebuild commit follows). Rows gain `body_sha256`; v1 is diffed by reading bodies from git. Against v1: 65 re-rendered, 49 unchanged. |
| 24 | W7.2 | CI: validate and tests on every push, block a tag unless both pass | — | Done 2026-10-08 on `ci`. `ci.yml` (Ubuntu + Windows) and `release.yml` (tag → checks → GitHub Release from the CHANGELOG entry). Rejecting the tag push itself needs a ruleset: org admin request recorded in PLAN.md. |

Not scheduled: W6.2 (data-dense figure descriptions, marked maybe) and W8 (ResStock, to be
determined).
