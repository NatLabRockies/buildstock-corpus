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

## Stage 7 · The `-v2` release

Written 2026-10-08, after steps 1–24 merged (main `e487c6e`, eight merges past the v1 tag).
W1.2 is the operating rule: every change to this dataset release's corpus lands in a new
build and a new tag. Steps 28, 29 and 35 need nothing upstream and can go first, in one PR,
while the drafts are being posted; 26, 27, 30, 31, 32 run in order once they are live.

| # | Task | What it does | Size | Status |
|---|------|--------------|------|--------|
| 25 | Owner | Post the DR_0004, DR_0007 and DR_0008 drafts to the ComStock site so the upgrade-measures index links them. Outside the repo. | — | |
| 26 | Fetch + build | The one sanctioned `bsc fetch` (AGENTS.md says not to, for this reason: it can move overlay hash pins), then `bsc build`. Gaps 8 → 5. `bsc validate` says whether any refetched PDF moved under a pin. | S | |
| 27 | Overlays | If the three new reports embed tables or figures as bitmaps, transcribe them to the W6 standard. Unknown until 26: nothing, or up to three M items. | ? | |
| 28 | Crosswalk | Drop the deprecated `doc_target` field and the crosswalk's `deprecated` block ("kept for this release only"), and `corpus_map.py`'s fallback to it. | S | |
| 29 | Owner decision | The four webinar-deck overlays (85853, 87746, 89653, 92766; 187 figure descriptions) sit unused in `overlays/`. Delete, or keep with a note saying why. Not deleted without the owner's word. | S | |
| 30 | Index | `bsc index` (~1 h, local, gitignored). The current index is from 2026-08-24 and predates every rebuild since. | S | |
| 31 | Release files | `bsc changelog --from comstock_amy2018_2025_release_3-v1 --append`, then the hand-written tooling bullets for steps 17–24 (section files, chunk files, `data-source`, cross-refs as titles, decorative refs, body hash, changelog, CI). `CITATION.cff` `version` and the `llms.txt` "Current" line → v2. | S | |
| 32 | Tag v2 | W1.1 recipe: `bsc build --corpus-version comstock_amy2018_2025_release_3-v2`, validate, `pytest -m network`, PR, merge commit, `git tag -a` on it, push the tag. First real run of `release.yml`: watch it. Check the raw URL at the tag serves `index.json` naming v2. | S | |

## Stage 8 · Governance and acceptance

| # | Task | What it does | Size | Status |
|---|------|--------------|------|--------|
| 33 | Owner | Org admin request from PLAN.md W7.2: branch ruleset on `main` requiring both `ci` checks (`ubuntu-latest`, `windows-latest`); tag ruleset on `*_release_*-v*` restricting creation and deletion. Outside the repo. | — | |
| 34 | Acceptance | The whole-plan test at the end of PLAN.md: a fresh agent, the repo URL only, the medium-office floor-to-floor question. Pass is three fetches, under 40 KB, every fact from the fetched files. Record the result in PLAN.md. | S | after 32 |
| 35 | Validate | Warn (not fail) when the Chroma index under `index/` is older than `chunks.jsonl` or holds a different chunk count; AGENTS.md notes the gap today. | S | |

Not scheduled, owner decisions pending: the five remaining gaps (dr_0009–dr_0011, hvac_0021,
pkg_0012) wait on upstream documentation; W6.2 (data-dense figure descriptions, marked maybe);
W8 (ResStock, to be determined); onboarding the next ComStock dataset release (new `sources/`
entry, registry, fetch, crosswalk, overlays for its PDFs, first tag `<new release>-v1`), a stage
of its own and not yet sized.
