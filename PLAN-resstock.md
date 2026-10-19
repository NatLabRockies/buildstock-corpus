# PLAN: ResStock corpus, first release (`resstock_amy2018_2025_release_1`)

Written 2026-10-19 from a survey of the two ResStock sources and of how the ComStock corpus
was built (PLAN.md, PLAN-staging.md, PLAN-buildstock-corpus-handoff.md). Owner: Lauren Klun.
Status: decisions D1 to D6 taken 2026-10-19; no step started. Steps run one at a time, each asked for before it starts, one
branch and PR per step unless a row says otherwise (the ComStock convention).

## Goal

A second folder, `processed/resstock/resstock_amy2018_2025_release_1/`, built by the same
`bsc` pipeline from the ResStock technical reference guide, the ResStock site pages and the 32
upgrade-measure reports, with the same provenance header, manifest, map, section files and
`index.json`, and tagged `resstock_amy2018_2025_release_1-v1`. Every measure PDF's tables and
figures are checked against the PDF before the tag, not after.

## What was found (2026-10-19)

**Upgrade measures page** (`docs/upgrade_measures.md` in `NatLabRockies/ResStock.github.io`,
`main`). One three-column table, 32 rows: measure number 1 to 32, name with link, initial
dataset release (all "ResStock 2025 Release 1"). Every link is an external OSTI PDF; no page
is rendered by the site itself and no PDF is committed in the repo. 27 unique PDFs: measures
24 to 28 share one report (93846). Measure 11 (Advanced Air Sealing) has no link and a footnote
saying documentation will come later: one tracked gap. Eight links use `www.nlr.gov`, which
301-redirects to `docs.nlr.gov`; the other 19 use `docs.nlr.gov` directly. There is no
crosswalk CSV. The per-release upgrade-number-to-name map is OEDI's `upgrades_lookup.json`
(`2025/resstock_amy2018_release_1/upgrades_lookup.json`, 0 = Baseline, 1 to 32), whose names
differ from the site table's (e.g. "Heat Pumps Water Heater" vs "Heat Pump Water Heater").
The site's data page links a `README_resstock_20251.pdf` on OEDI that returns 404 (upstream
issue, not ours).

**Technical reference guide** (`docs/technical_reference_guide/` in `NatLabRockies/resstock`).
A LaTeX project, main file `ResStockTechnicalReferenceGuide.tex`, chapters pulled with
`\input` (ComStock used `\include`), bibliography `files/refs.bib` via biblatex (ComStock:
`bibliography.bib`), figures in `images/` (ComStock: `figures/`), six of the figures are PDF
files, not bitmaps. A custom `customLongTable` environment wraps caption, label and header
row as arguments; pandoc does not know it. Chapters 4 (Running ResStock), 7, 8, 9 and the
917 KB appendix are commented out of the main file, so the published PDF does not contain
them. `develop` and the release tags differ a great deal:

| ref | TRG state | class | notes |
|-----|-----------|-------|-------|
| `2025_Release_1` (2025-08-26) and `2025_Release_1_upgrades_29_to_32` (2026-03-25) | identical TRG files; chapter 3 inlined (3a 173 KB, 3b 169 KB, 3c 234 KB); no `characteristics/` dir | `nrel.cls` | 15 figures, ~150 longtables + 80 customLongTables in the included chapters |
| `develop` (1,458 commits ahead) | chapter 3 refactored into 1,065 `\input` files under `characteristics/` (per-characteristic description, sources, dependencies, options, properties, assumptions); title "Active Development Version"; ~10,000 changed lines in chapter 3 | `nlr.cls` | 19 image files |

The site publishes `assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf` (15.9 MB, posted
2025-10-22), whose version-history row reads "Draft, ResStock 2025 Release 1, October 2025".
That date is after both the tag and before today's `develop`, so no ref reproduces the PDF
exactly. This is decision D1 below.

**Site pages** (same site repo). `docs/FAQ.md` (34 KB), `data.md`, `developers.md`,
`citation_data_attribution.md`, `contact.md`, `resources/resources.md`, 17 explanation pages
(known-issue reports, sampling notes, geographic codes), 3 how-to pages, 1 tutorial, and two
Jupyter notebooks (`.ipynb`, 465 KB and 155 KB) the markdown extractor cannot read. The site
has no `llms.txt` or corpus links yet.

**The pipeline is ComStock-shaped in these places** (everything else is already generic):
registry validation (a `measures` source must have `internal_dir` and `crosswalk_csv`);
measure ids must match `[a-z]+_\d+`; the crosswalk joins a CSV by column name; the LaTeX
loader lists chapters from `\include` only and does not strip `%` comments; the bibliography
and figure directory names are fixed; `decorative.py` assumes the first two docling images of
every measure PDF are ComStock cover art and the NREL wordmark; CLI defaults, `llms.txt`,
`README.md`, `AGENTS.md`, `CITATION.cff`, `status.py`, `corpus_map.py` and the `bsc query`
prompt say "ComStock" in prose.

## Decisions (all six decided 2026-10-19; stage R1 may start)

| # | Decision | Options | Recommendation |
|---|----------|---------|----------------|
| D1 | Which ref of the TRG documents dataset 2025 Release 1 | (a) `develop` pinned at the commit fetched, as the ComStock site is (`git_ref: develop`, sha recorded in `fetch_state.json` and every `source_url`); (b) tag `2025_Release_1_upgrades_29_to_32`, the code the dataset's last upgrades were run from; (c) the `develop` commit nearest the PDF's 2025-10-22 posting | **Decided 2026-10-19: (b), the ResStock repo's release tag.** The owner chose the frozen code snapshot the dataset was run from over the moving branch: the tag never changes, so a rebuild reproduces the same guide, and the ComStock precedent (code repo at `2025-3`) holds. Record in the registry comment that `develop` was considered (NLR branding, refactored chapter 3, closer to the published PDF) and why it was not used. When the next dataset release has its own tag, that tag's guide is the next corpus release's source. |
| D2 | Release id and measure id spelling | Release id `resstock_amy2018_2025_release_1` (OEDI convention, same as ComStock; the AMY2012 dataset shares this documentation and is named in the map, not built twice). Measure ids: the table's number as a string (`"1"` to `"32"`), with `upgrade_id` the same number in this release | **Decided 2026-10-19: as stated.** ResStock reuses numbering across releases from 2025 R1 on ("the same set of measures will be run with each dataset release"), so the number is the stable id. |
| D3 | Chapters commented out of the main file (4 Running ResStock, 7, 8, 9, the 917 KB appendix of option/saturation tables) | (a) follow the main file, convert only what the PDF contains; (b) also convert the appendix as unpublished material with its own status | **Decided 2026-10-19: (a)** for v1. At the tag, chapter 3 already inlines each characteristic's option and saturation tables, so the appendix mostly duplicates them. Statuses stay the three in the vocabulary. |
| D4 | The two `.ipynb` how-to notebooks | (a) skip, list in the map's known gaps; (b) add a notebook extractor (markdown cells + code cells as fenced blocks, outputs dropped) | **Decided 2026-10-19: (a)** for v1; (b) is a small, separable follow-up. |
| D5 | docling table mode for a fresh cache | FAST (what ComStock used, to keep a 52-PDF warm-up to tens of minutes) or ACCURATE (slower, better cell structure) | **Decided 2026-10-19: ACCURATE.** 27 PDFs, one-time cost, and the owner's stated priority is correct tables. The cache key includes the options, so ComStock's cache is unaffected. |
| D6 | Link host | Record the eight `www.nlr.gov` links as fetched, or canonicalize to `docs.nlr.gov` via `canonical_urls` | **Decided 2026-10-19: canonicalize**, as ComStock did for 92504, so every OSTI URL in the corpus has one spelling. |

## Changes from how ComStock was done

1. **Fidelity before the first tag.** ComStock's table and figure overlays were written in six
   batches after v1 (PRs #14 to #20) and its decorative-image rule was fixed at v2 and v3. Here
   step R4 runs the full per-PDF check before `-v1` is cut, so the first tag already says what
   it means by "the tables are right".
2. **A table check that compares, not just counts.** The fidelity audit only finds captions with
   no table beneath them. The pkg_0012 method (page render at 1.5x plus the PDF text layer,
   compared cell for cell) is what caught three plausible wrong tables there. R4 applies it to
   every table in every measure PDF, and records the verdict per table in the sidecar even when
   nothing is replaced, so a reviewer can see each table was looked at.
3. **Figure descriptions drafted by a vision pass, reviewed by hand.** The rollout file closed
   with "generated-overlay automation for ResStock" as the next piece. R4 drafts each
   description from the page render, then edits it to the W6 standard (60 to 70 words, what the
   figure shows and the values a reader would cite), keeping `method: vision-description`.
4. **Measure identity from a JSON lookup, not a CSV.** OEDI's `upgrades_lookup.json` replaces the
   crosswalk CSV as the per-release upgrade map; it is downloaded and hashed by `bsc fetch`
   like the measure PDFs. Both site-table name and OEDI name are kept in `crosswalk.json`.
5. **PDF figures rasterized at build.** Six TRG figures are PDF files. The build renders each to
   PNG (pypdfium2 is already a dependency) so the image reference resolves and the figure
   overlay has a bitmap to pin by sha256, as every other figure does.
6. **Prose and defaults made product-neutral once**, rather than a second copy of each file.
   `llms.txt` and `README.md` list both releases; `AGENTS.md` names both current tags; the CLI
   requires `--product` and `--release` (or reads them from a single `sources/` entry when only
   one exists) instead of defaulting to ComStock.
7. **Everything else stays the same**: layout, status vocabulary (`osti_pdf`, `site_page`,
   `missing`), line-1 header, section files, chunking, manifest and validate, changelog and
   `release.yml`, tag form `<release id>-v<N>`, one PR per step.

## Steps

Sizes: S under an hour, M a few hours, L a day or more. "Files" are the main ones touched.

### Stage R1 · Make the tooling product-neutral (no ResStock content yet)

| # | Step | Files | Done when | Size |
|---|------|-------|-----------|------|
| R1.1 | Registry: make `internal_dir` and `crosswalk_csv` optional for a `measures` source; add `upgrades_lookup_url` (an https URL to a JSON map), `measure_id_pattern` (regex, default the ComStock one), and for `latex` sources `bibliography` (path relative to the project dir, default `bibliography.bib`) and `images_dir` (default `figures`). Validation messages stop naming ComStock. | `registry.py`, `test_registry.py` | ComStock registry loads unchanged; a ResStock-shaped registry loads; a `measures` source with neither CSV nor lookup URL is refused with a clear message. | S |
| R1.2 | LaTeX loader: chapter list from `\input` and `\include`, after stripping `%` comments (a commented `\input` must not become a chapter); expand `customLongTable{fmt}{caption}{label}{header}` into a plain `longtable` with `\caption`, `\label` and the header row before the existing longtable normalization; read the bibliography path and images dir from the registry; rasterize `\includegraphics` targets ending in `.pdf` to PNG beside the chapter and rewrite the reference. Check how pandoc maps `\paragraph` (the TRG's fourth heading level) and extend `_normalize_heading_levels` if it comes out as bold text. | `extract/latex.py`, `build.py` (`_copy_source_images`), `test_latex_*.py` | Fixture snippets with a commented input, a `customLongTable`, a spaced file name (`characteristics/Census Region`) and a `.pdf` figure convert to the expected markdown; ComStock's 19 chapters rebuild byte-identical (compare `body_sha256`). **Done 2026-10-19, branch `r1-latex`.** 13 new tests (`test_latex_resstock.py`), 398 passing. Sandbox rebuild of ComStock: 15 chapters byte-identical, 4 changed on purpose. (1) The loader had stripped `\caption` and `\label` from every longtable, so all 8 ComStock longtables (in 3_sampling, 5_outputs, 6_AppendixA) had lost their titles; pandoc 3 carries both, so they now render with a `<div id="tab:…" data-source=…>` wrapper and the caption line. ResStock's ~150 longtables are all captioned, which is what forced the fix. (2) `\input` substitution ignored `%` comments, so the HVAC chapter carried a 48-line "HVAC System Type Prevalence" table the authors had commented out ("too big") and the published PDF does not contain; it is gone. Both changes reach ComStock's `processed/` at its next rebuild and belong in that changelog entry. Also found: PNG rendering is hand-rolled (zlib) because Pillow is not in the test dependency group; a sandbox under the scratchpad path exceeds Windows MAX_PATH, so use a short `--work-dir`. | M |
| R1.3 | Measures: `_MEASURE_ID_RE` becomes the registry pattern; `fetch` downloads and hashes the lookup JSON when `upgrades_lookup_url` is set; `build_crosswalk` gains a JSON join path (upgrade number → name) alongside the CSV one, and `crosswalk.json` rows carry both the index-page name and the lookup name. `canonical_urls` applied as today. | `extract/measures_index.py`, `extract/crosswalk.py`, `fetch.py`, tests | The ResStock index page parses to 32 refs (31 `external_pdf`, 1 `none`); the join yields 32 measures, 31 covered, 1 gap; ComStock crosswalk counts unchanged (65 / 61 / 4). | M |
| R1.4 | Product-neutral prose and defaults: CLI `--product`/`--release` required unless exactly one registry exists; `status.py`, `corpus_map.py`, `links.py`, `decorative.py` docstrings and the `bsc query` prompt say "the product's site" and take the product name from the registry; `decorative.py` rule keyed per product (ComStock's two leading images stay as they are; ResStock's rule is set in R3 after the first conversion is inspected). | `cli.py`, `status.py`, `corpus_map.py`, `query.py`, `decorative.py`, tests | `bsc validate --product comstock --release comstock_amy2018_2025_release_3` green; `bsc map` regenerates an identical `CORPUS_MAP.md` for ComStock apart from any wording change, which is listed in the PR. | S |

### Stage R2 · Register and fetch

| # | Step | Files | Done when | Size |
|---|------|-------|-----------|------|
| R2.1 | Write `sources/resstock_resstock_amy2018_2025_release_1.yaml`: `technical_reference` (latex; repo `NatLabRockies/resstock`, `git_ref` per D1, `sparse: [docs/technical_reference_guide]`, `latex_main`, `bibliography: files/refs.bib`, `images_dir: images`, status `site_page`, `publication_url` the site's `assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf`); `github_site` (markdown; `ResStock.github.io` at `main`, `doc_glob: docs/**/*.md`, exclude `docs/upgrade_measures.md`, `sparse: [docs, assets/images]`, `site_url: https://natlabrockies.github.io/ResStock.github.io`); `upgrade_measures` (measures; same repo, `index_page: docs/upgrade_measures.md`, `upgrades_lookup_url` the OEDI JSON, `measure_id_pattern: ^\d+$`, `canonical_urls` for the eight `www.nlr.gov` links per D6). Header comment records D1 to D6 with dates. | `sources/…yaml`, `test_registry.py` | Registry loads and validates. | S |
| R2.2 | `uv run bsc fetch --product resstock --release resstock_amy2018_2025_release_1`. This is the one time fetch runs for this release; it writes only under `raw/resstock/` and does not touch ComStock's `raw/` or overlays. Record the fetched shas (resstock, site) and the 27 PDF hashes; confirm the lookup JSON was hashed. | `raw/resstock/**` (gitignored), `fetch_state.json` | 27 PDFs downloaded, 0 unreachable, lookup JSON present, both clone shas recorded here in this table. | S |

### Stage R3 · First build, extractor fixes

| # | Step | Files | Done when | Size |
|---|------|-------|-----------|------|
| R3.1 | Smoke build in a sandbox: `uv run bsc build --product resstock --release … --work-dir <scratch> --sample 2`, then the full build with `--no-overlays`. Expect ~7 TRG chapters (1, 2, 3a, 3b, 3c, 5, 6), ~26 site pages, 27 PDFs. The docling warm-up at ACCURATE is a one-time cost of roughly an hour. Read every build warning. | none committed | Build completes; warnings list recorded here. | M |
| R3.2 | Run `scripts/audit_md_fidelity.py` on the sandbox output and fix the extractor for every class of defect that is systematic rather than per-document: longtables that lost their header or caption, `customLongTable` captions, heading levels, cross-references (`\ref{table:…}` to quoted titles), soft hyphens and NBSPs, dangling image refs. Inspect the first two docling images of three ResStock PDFs and set the product's decorative rule (R1.4). | `extract/latex.py`, `decorative.py`, tests | latex: 0 orphaned table or figure captions, 0 dangling refs; pdf: orphaned count known and every one traced to a rasterized table (overlay work for R4), not an extractor bug; character hygiene zero in latex and markdown. | M |
| R3.3 | Commit the first real build to `processed/resstock/…` with `--corpus-version resstock_amy2018_2025_release_1-v1-pre` or no version (the manifest's `corpus_version` only has to equal the tag at release time); `bsc map`, `bsc validate`. | `processed/resstock/**` | Validate green; `CORPUS_MAP.md` lists every document, the 32-measure routing table and the gap (measure 11, two notebooks). | S |

### Stage R4 · Table and figure fidelity, every measure PDF and the TRG figures

| # | Step | Files | Done when | Size |
|---|------|-------|-----------|------|
| R4.1 | Working method, written once in `overlays/README.md` under a ResStock heading: for each PDF, list its tables from the audit; render each table's page at 1.5x; compare docling's grid to the render and the text layer cell by cell; a correct table gets a `checked:` entry (label, page, `verdict: correct`, date) and an incorrect one a `replaces:` transcription (`method: vision-transcription`); a table missing entirely gets a caption-anchored insert. For figures, every non-decorative image gets `alt` plus a description to the W6 standard, drafted from the render and edited by hand. `checked:` is a new, minimal engine addition (validate confirms the label exists and the page pin; nothing is injected). | `overlay.py`, `overlays/README.md`, tests | Engine accepts `checked:` entries; `bsc validate` counts them. | S |
| R4.2 | Sidecars for measures 1 to 10 (HVAC and water heating reports: 96634, 96635, 96636, 96413, 96414, 95032, 95034, 95036, 96826, 96827). Commit per document, as the rollout did. | `overlays/resstock_…/upgrade_measures/measure_pdfs/<n>.yaml` | Every table in the ten PDFs has a `checked` or `replaces` entry; every real figure a description. | L |
| R4.3 | Measures 12 to 18 (envelope and packages: 96739, 96344, 96281, 96347, 96349, 96405, 95035). | same | same | L |
| R4.4 | Measures 19 to 32 (EV reports 94459 to 94464, the shared demand-flexibility report 93846, the four light-envelope reports 99816 to 99820). | same | same | L |
| R4.5 | TRG figures: the 15 images chapter 2 and 3a reference (maps, the workflow and flowchart PDFs, the dependency tree), described to the same standard; the six rasterized PDF figures pinned by the PNG the build wrote. | `overlays/resstock_…/technical_reference/…yaml` | All TRG figure refs carry alt text and a description. | M |
| R4.6 | Rebuild with overlays, re-run the audit: 0 orphaned captions in `pdf`; every `replaces` and `checked` entry verified by `bsc validate` against the PDF hash. Spot-check ten tables at random against the PDF a second time, by a different reader (a fresh agent or the owner). | `processed/resstock/**` | Audit and validate green; spot-check recorded here. | S |

### Stage R5 · Index and acceptance

| # | Step | Files | Done when | Size |
|---|------|-------|-----------|------|
| R5.1 | `bsc index --product resstock --release …` (ComStock's took ~13 minutes here), then three `bsc query` smoke questions, one per source: a stock saturation from chapter 3, a known-issue page, an applicability rule from a measure PDF. Answers must cite line-1 facts. | `index/` (gitignored) | Three answers with correct citations; validate's stale-index warning clear. | S |
| R5.2 | Acceptance run, as ComStock's step 34: a fresh agent given only the repository URL and "what fraction of ResStock dwelling units have 3 bedrooms, with a citation" (or another single-table question) answers from `index.json` and one section file at the tag, naming `source_id/source_path`, status, publication URL and corpus version. Findings recorded in PLAN.md. | `PLAN.md` | Pass recorded, or findings fixed and re-run. | S |

### Stage R6 · Documentation and release

| # | Step | Files | Done when | Size |
|---|------|-------|-----------|------|
| R6.1 | `README.md`, `AGENTS.md`, `llms.txt` describe two products and name both current tags; `CITATION.cff` lists both releases; `PLAN.md` W8 points at this file; `CHANGELOG.md` gains the `resstock_amy2018_2025_release_1-v1` entry (`bsc changelog` has no previous tag to diff from, so the entry is the document list and the hand bullets: sources, D1 to D6, overlay counts, the gap). | those files | `grep -rn ComStock-only wording` finds nothing that excludes ResStock; `bsc changelog --show resstock_amy2018_2025_release_1-v1` reads the entry. | S |
| R6.2 | Final build with `--corpus-version resstock_amy2018_2025_release_1-v1`, validate, PR, CI green on both runners, merge with a merge commit, annotated tag on the merge commit, push. `release.yml` cuts the Release (tag ruleset bypass actor already in place since 2026-10-16). Prove the route at the tag: `index.json`, one section file, three fetches. | `processed/**`, git tag | GitHub Release exists; raw `index.json` at the tag says `-v1`. | S |

### Stage R7 · Site discovery (separate repo, owner's call)

| # | Step | Where | Done when | Size |
|---|------|-------|-----------|------|
| R7.1 | Give the ResStock site what the ComStock site got on 2026-10-16: `llms.txt`, a home-page callout, per-page "read this page as Markdown" links pinned to the corpus tag, a schema.org Dataset block, and the weekly `Sync corpus index` workflow. Also report the dead `README_resstock_20251.pdf` link. | `NatLabRockies/ResStock.github.io` | Live site links the `-v1` tag; a fresh agent reaches the corpus from the site in six fetches or fewer. | M |

## Open risks

- **The tag's guide is older than the published PDF.** The site's PDF (October 2025) carries
  edits the tag (August 2025 code, March 2026 tag) does not. A reader comparing the corpus to
  the PDF will find differences; the registry comment and the map's source note say which
  commit the text comes from, and the `publication_url` still sends them to the PDF.
- **Chapter 3 size.** 3a, 3b and 3c are 173, 169 and 234 KB of LaTeX at the tag; the section-file
  layout keeps each H2 small, but the `bytes` warning in `AGENTS.md` ("check before fetching a
  whole document") matters more here.
- **Rasterized tables in the OSTI PDFs.** ComStock's measure reports had a minority of tables as
  pixels; the ResStock reports come from the same report template, so expect some. The audit
  in R3.2 counts them; each is an insert in R4.
- **Decorative-image rule.** If the ResStock reports' leading docling images are not cover art
  plus wordmark, the per-product rule in R1.4 is where it is set; do not let a real Figure 1 be
  hidden as happened with two ComStock site PDFs at v2.
