# Changelog

One entry per corpus build that is tagged. Tags are named `<release id>-v<N>` after the
dataset release the build documents, and never move. Two products share this file
(ComStock and ResStock), each with its own tags; a product's newest tag is its topmost
entry, and a product's folder exists only at its own tags and on `main`. Entries list documents added, removed
or changed (by input hash), overlays changed, and tooling changes that alter output.
`bsc changelog --from <tag>` computes the document-level part from two manifests, telling a
document re-rendered by a tooling change (body hash moved) from one merely re-stamped with
the new version, and `--append` inserts it here; the bullets saying *why* documents were
re-rendered are written by hand above it.

## resstock_amy2018_2025_release_1-v1 — 2026-11-12

First tagged ResStock build, and the corpus's second product. Documents ResStock dataset
release `resstock_amy2018_2025_release_1` (the AMY2012 dataset of the same release shares
this documentation and is not built twice): 62 documents, 32 measures (all 32 documented,
no tracked gap), 4,183 chunks, 1,147 section files. There is no earlier ResStock tag to
diff against, so this entry is the document list and the notes below. The plan and every
step's record are in `PLAN-resstock.md`. ComStock's files are unchanged by this tag; its
current tag is still `comstock_amy2018_2025_release_3-v3`.

### Sources

- **Technical reference guide**, 7 chapters, from LaTeX in `NatLabRockies/resstock` at tag
  `2025_Release_1_upgrades_29_to_32` (commit `3888e2f`), status `site_page`: the guide has
  no OSTI number, and its publication URL is the PDF the ResStock site serves. That PDF
  (October 2025) was built from a later, untagged state of the same source, so the two can
  differ in places; the map says so under "About this release". Chapters the main file
  comments out, and the appendix of option tables that chapter 3 already inlines, are not
  converted.
- **ResStock site**, 27 pages, from `NatLabRockies/ResStock.github.io` (commit `696c020`),
  status `site_page`.
- **Upgrade-measure reports**, 28 PDFs covering all 32 measures (measures 24 to 28 share
  report 93846), status `osti_pdf`. The eight links the site spells `www.nlr.gov` are
  recorded under `docs.nlr.gov`, so every OSTI URL has one spelling. Upgrade names come from
  OEDI's `upgrades_lookup.json`; measure ids are the numbers `1` to `32`.

### Tables and figures

Every table and figure in the 28 reports was compared with its PDF page before this tag.

- **105 tables hand-authored** in overlay sidecars: 63 transcribed or corrected because the
  extracted grid was wrong (merged or displaced rows, lost rows, a grid under the wrong
  caption, a URL or identifier broken by a line-wrap space), and 42 number grids that the
  reports show as pictures (heat pump performance maps in 95032, 95034, 95036 and 96826,
  6,457 values), read from the embedded images and checked by arithmetic and by surface fit.
- **136 extracted tables recorded correct** (`checked:` entries, each pinned to the PDF and
  to the table's fingerprint).
- **467 figures described** from the picture: 453 in the reports, 14 in the guide.
- **9 text repairs** to extracted text.
- `bsc validate` re-verifies all of the above from the files in a clone. The fidelity audit
  finds no orphaned table or figure caption in the reports. A second reader compared ten
  tables drawn at random with their pages; all matched.

### Extractor changes that also reach ComStock at its next build

None of these changes a ComStock file at this tag; ComStock's PDFs are re-converted when it
is next built.

- docling's table mode is chosen per source; ResStock uses ACCURATE, and ComStock moves to
  it at its next build.
- Page footnotes that sit under a table or figure are no longer dropped (22 restored in the
  ResStock reports; none was missing in ComStock).
- A hyphen printed at a line end is kept: 'Post-' / 'Retrofit' no longer becomes
  'PostRetrofit', and URLs broken after a hyphen resolve again (311 restored in the ResStock
  reports).
- Caption labels of appendix tables and figures (`Table A-2`) are recognized.
- The product must be named on the command line (`--product`), since two are registered.

### Known gaps and limits

- Two Jupyter notebook how-to guides on the site are not converted; the map lists them.
- 95032 Figure 2, a scanned manufacturer performance sheet, is described and not
  transcribed: its digits cannot be read reliably.
- Where a page prints an en dash between two numbers, the markdown can have a space before
  the dash and none after ('3 -5' for '3–5'); a search for '3-5' misses these.
- Inconsistencies inside the published documents are kept as printed; the sidecars and
  `PLAN-resstock.md` name them.

### Documents

- `technical_reference/docs/technical_reference_guide/1_Introduction.tex` — Introduction
- `technical_reference/docs/technical_reference_guide/2_ResStockStructureAndSampling.tex` — ResStock Workflow, Input Structure and Sampling
- `technical_reference/docs/technical_reference_guide/3a_ResStockInputs.tex` — Housing Characteristics and Inputs
- `technical_reference/docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex` — HVAC
- `technical_reference/docs/technical_reference_guide/3c_ResStockInputs.tex` — Water Heating, Appliances, Lighting, Plug Loads, Electric Vehicles, Electrical Panels, Household Characteristics
- `technical_reference/docs/technical_reference_guide/5_ResStockOutputs.tex` — ResStock Outputs
- `technical_reference/docs/technical_reference_guide/6_PublicDataAccess.tex` — Public Data Access
- `github_site/docs/citation_data_attribution.md` — Citation and Data Attribution
- `github_site/docs/contact.md` — Contact
- `github_site/docs/data.md` — Data
- `github_site/docs/developers.md` — For Developers
- `github_site/docs/FAQ.md` — FAQ
- `github_site/docs/resources/explanations/Building_Types.md` — Building Types Not Included In ResStock
- `github_site/docs/resources/explanations/Considerations_for_ResStock_Calibration_and_Validation.md` — Considerations for ResStock Calibration and Validation
- `github_site/docs/resources/explanations/Geographic_Fields_and_Codes.md` — Geographic Fields and Codes
- `github_site/docs/resources/explanations/Individual_Measures_Not_Combined.md` — Why Individual ResStock Measures Should Not Be Combined
- `github_site/docs/resources/explanations/Issue_2024_2_Electricity_and_Energy_Bills.md` — ResStock 2024 Release 2 Electricity and Energy Bills
- `github_site/docs/resources/explanations/Issue_2024_2_Measure_Applicability.md` — ResStock 2024 Release 2 Measure Applicability
- `github_site/docs/resources/explanations/Issue_2025_1_Column_Applicability.md` — ResStock 2025 Release 1 Column Applicability
- `github_site/docs/resources/explanations/Issue_2025_1_Electric_Panel_Capacity.md` — ResStock 2025 Release 1 Electric Panel Capacity
- `github_site/docs/resources/explanations/Issue_Wall_Type_Especially_Maine.md` — Wall Type Issue, Especially in Maine
- `github_site/docs/resources/explanations/Monthly_Net_Electricity_Comparisons.md` — Monthly Net Electricity Comparisons between ResStock 2024 Release 2 data and 2018 861M data
- `github_site/docs/resources/explanations/Number_of_samples.md` — How Many Samples are Required for this Analysis?
- `github_site/docs/resources/explanations/One_Row_Data_House.md` — One Row of Data Is Not One Real House
- `github_site/docs/resources/explanations/PV_System_Assignment_and_Distributions.md` — PV System Assignment and Distributions
- `github_site/docs/resources/explanations/Quota_Based_Sampling.md` — Quota-Based Sampling and Implications
- `github_site/docs/resources/explanations/Summer_Peaking_CCHP.md` — Summer Peak Increase from Cold Climate Heat Pump in ResStock 2025 Release 1
- `github_site/docs/resources/explanations/Unmet_load_hours.md` — Unmet Load Hours
- `github_site/docs/resources/explanations/Wood_Stud_Depth.md` — Wood Stud Depth and Wall R-Value Calculations
- `github_site/docs/resources/how-to-guides/Analyze_housing_stock_programmatically.md` — Analyze Housing Stock Programmatically
- `github_site/docs/resources/how-to-guides/aws_athena_queries.md` — AWS Athena Queries
- `github_site/docs/resources/how-to-guides/Housing_Stock_Excel_Questions.md` — Analyze Your Housing Stock and Different What if Scenarios Using Excel
- `github_site/docs/resources/resources.md` — Resources
- `github_site/docs/resources/tutorials/Enough_Samples_Data_Viewer.md` — How To Use The Data Viewer With Enough Samples
- `upgrade_measures/measure_pdfs/93846.pdf` — HVAC Demand Flexibility with On-Peak Load Shedding of 2F offset
- `upgrade_measures/measure_pdfs/94459.pdf` — Electric Vehicle Adoption with Level 1 Charging
- `upgrade_measures/measure_pdfs/94460.pdf` — Electric Vehicle Adoption with Level 2 Charging
- `upgrade_measures/measure_pdfs/94461.pdf` — Efficient Electric Vehicle Adoption with Level 2 Charging
- `upgrade_measures/measure_pdfs/94463.pdf` — Electric Vehicle Adoption with Level 2 Charging and Demand Flexibility
- `upgrade_measures/measure_pdfs/94464.pdf` — Efficient Electric Vehicle Adoption with Level 2 Charging and Demand Flexibility
- `upgrade_measures/measure_pdfs/95035.pdf` — Residential Two-Stage Geothermal Heat Pump (4.0 COP, 20.5 EER) With Envelope Improvements and Advanced Air Sealing
- `upgrade_measures/measure_pdfs/96281.pdf` — Advanced Air Sealing with Drill-and-Fill Wall Insulation
- `upgrade_measures/measure_pdfs/96344.pdf` — Duct Sealing and Insulation
- `upgrade_measures/measure_pdfs/96347.pdf` — Advanced Air Sealing, Attic Floor Insulation, and Duct Sealing and Insulation
- `upgrade_measures/measure_pdfs/96349.pdf` — Advanced Air Sealing, Drill-and-Fill Wall Insulation, Attic Floor Insulation, and Duct Sealing and Insulation
- `upgrade_measures/measure_pdfs/96405.pdf` — EnergyStar Windows
- `upgrade_measures/measure_pdfs/96413.pdf` — Cold Climate Air-Source Heat Pump
- `upgrade_measures/measure_pdfs/96414.pdf` — Dual Fuel Heat Pump
- `upgrade_measures/measure_pdfs/96634.pdf` — Natural Gas Furnace 95% AFUE
- `upgrade_measures/measure_pdfs/96635.pdf` — Propane Furnace 95% AFUE and Fuel Oil Furnace 88% AFUE
- `upgrade_measures/measure_pdfs/96636.pdf` — Reference Space Heating and Air Conditioning Upgrade Circa 2025
- `upgrade_measures/measure_pdfs/96739.pdf` — Attic Floor Insulation
- `upgrade_measures/measure_pdfs/96826.pdf` — Heat Pump Water Heater
- `upgrade_measures/measure_pdfs/96827.pdf` — Natural Gas Water Heater
- `upgrade_measures/measure_pdfs/96738.pdf` — Advanced Air Sealing
- `upgrade_measures/measure_pdfs/95032.pdf` — Residential Single-Stage Geothermal Heat Pump (3.8 COP, 18.6 EER)
- `upgrade_measures/measure_pdfs/95034.pdf` — Residential Two-Stage Geothermal Heat Pump (4.0 COP, 20.5 EER)
- `upgrade_measures/measure_pdfs/95036.pdf` — Residential Variable-Speed Geothermal Heat Pump (4.4 COP, 30.9 EER)
- `upgrade_measures/measure_pdfs/99816.pdf` — Light Air Sealing
- `upgrade_measures/measure_pdfs/99818.pdf` — Light Air Sealing, Attic Floor Insulation, and Duct Sealing and Insulation
- `upgrade_measures/measure_pdfs/99819.pdf` — Residential Two-Stage Geothermal Heat Pump (4.0 COP, 20.5 EER) With Light Envelope Improvements
- `upgrade_measures/measure_pdfs/99820.pdf` — Residential Variable-Speed Geothermal Heat Pump (4.4 COP, 30.9 EER) with Light Envelope Improvements

## comstock_amy2018_2025_release_3-v3 — 2026-10-16

Changes since `comstock_amy2018_2025_release_3-v2` (corpus_version `comstock_amy2018_2025_release_3-v2`): 118 documents (+1), 65 measures (61 documented, 4 tracked gaps), 8,022 chunks (+74). 11 documents changed, 107 unchanged in content.

Branch `release-v3` (the release PR), after PRs #39 and #40 merged past the v2 tag. Documents
ComStock dataset release `comstock_amy2018_2025_release_3`: 118 documents, 65 measures
(61 documented, 4 tracked gaps), 8,022 chunks.

### Tooling and corpus changes, by hand

- **Why a v3 so soon after v2.** An acceptance test run from the ComStock website (the site
  now links agents to this corpus and tells them to pin the current tag) found that
  `llms.txt` promised every `index.json` row names its section files, but those fields were
  added to `index.json` by PR #40 (`index-sections`) after v2 was tagged. At v2 the "fetch
  `index.json`, then one section file" route was true on `main` and false at the tag. This
  build puts `sections_dir` and `section_files` in `index.json` at a tag.
- **One new measure document.** pkg_0012 (Photovoltaics With 40% Rooftop Coverage With Roof
  Insulation), posted to the ComStock site as a pre-publication PDF (status `site_page`,
  site PRs #205 and #206), with a new overlay sidecar: its six figures described to the W6
  standard, and its tables checked cell for cell against the PDF. Tables 4, 6, 7, 8 and 9
  extracted correctly; three did not and are superseded by transcriptions: Table 1 was split
  at a page break (rows lost, cell text shifted), Table 2's grid was emitted under the Table 3
  caption, and Table 5 lost its climate-zone-1 column (R-21). One text repair demotes the
  `## Applicability` heading docling made of a Table 1 row label.
- **`replaces.under_caption`** in overlay sidecars: when a pinned table fingerprint matches
  more than one extracted table (an executive summary repeating a results table value for
  value, as every measure report does; pkg_0012's Table 2 equals Table 8), the entry names the
  caption the misplaced grid sits under and the first table below it is the one replaced.
  Three tests; documented in `overlays/README.md`.
- **The site pin moved** from `3b69dec` to `2036a73` (site PR #208), which is why every
  github.io document's header and manifest row names the new commit, and why the nine
  overlay sidecars under `upgrade_measures/` were re-stamped with the new `source_url`
  (`scripts/stamp_overlay_links.py`): the "overlay changed" lines below are that re-stamp,
  not new transcriptions. `bsc fetch` does not advance a clone that is already on disk; the
  site clone was pulled forward by hand before the fetch (see PLAN-buildstock-corpus-handoff.md,
  Finding 4).
- **For Developers page** re-rendered from a revised upstream source (site PRs #207 and #208 added a
  section on the corpus).
- **One start order per reader type**, stated in the same words in `AGENTS.md` and `llms.txt`:
  with a clone, read `CORPUS_MAP.md` first; fetching URLs, fetch `index.json` first at a tag.
  Earlier `AGENTS.md` said the map and both `llms.txt` files said `index.json`.
- **PR #39 (`acceptance-34`)**, merged after v2: named the current tag in `AGENTS.md` and
  `README.md` and recorded the first acceptance run; no document output changed.
- **PR #40 (`index-sections`)**, merged after v2: `index.json` rows carry `sections_dir` and
  `section_files`; `index.json` grew from 78 KB to 157 KB raw (7 KB to 20 KB gzip-compressed).
  `llms.txt` and `AGENTS.md` give the new size.

### Documents, computed

<!-- Generated by `bsc changelog`. Document lines cite `source_id/source_path`; add the tooling notes (why documents were re-rendered) by hand above the list. -->

### Added

- `upgrade_measures/assets/files/ComStock Measure Doc_PV with Roof Insulation.pdf` → `upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_PV with Roof Insulation.md` (site_page): Photovoltaics With 40% Rooftop Coverage With Roof Insulation — https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_PV%20with%20Roof%20Insulation.pdf
- Measure `pkg_0012` is now documented (tracked gap closed).

### Changed

- `github_site/docs/for_developers/for_developers.md` → `github_site/docs/for_developers/for_developers.md` (site_page): For Developers — upstream source revised.
- `upgrade_measures/assets/files/ComStock Measure Doc_Dim Lighting During Peak Hours.pdf` → `upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_Dim Lighting During Peak Hours.md` (site_page): Dim Lighting During Peak Hours — overlay changed.
- `upgrade_measures/assets/files/ComStock Measure Doc_HP RTU Higher Compressor Lockout.pdf` → `upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_HP RTU Higher Compressor Lockout.md` (site_page): Heat Pump Rooftop Units With Higher Compressor Lockout Temperature for Heating — overlay changed.
- `upgrade_measures/assets/files/ComStock Measure Doc_Lighting Control for Emission Reduction.pdf` → `upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_Lighting Control for Emission Reduction.md` (site_page): Lighting Control for Emission Reduction — overlay changed.
- `upgrade_measures/assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.pdf` → `upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.md` (site_page): Low Priority Device Switching During Peak Hours — overlay changed.
- `upgrade_measures/docs/upgrade_measures/env_ext_secondary_window.md` → `upgrade_measures/unpublished_docs/upgrade_measures/env_ext_secondary_window.md` (site_page): Secondary Window System — overlay changed.
- `upgrade_measures/docs/upgrade_measures/env_ext_wall_insulation.md` → `upgrade_measures/unpublished_docs/upgrade_measures/env_ext_wall_insulation.md` (site_page): Exterior Wall Insulation — overlay changed.
- `upgrade_measures/docs/upgrade_measures/env_ext_window_replacement.md` → `upgrade_measures/unpublished_docs/upgrade_measures/env_ext_window_replacement.md` (site_page): Window Replacement — overlay changed.
- `upgrade_measures/docs/upgrade_measures/env_roof_insulation.md` → `upgrade_measures/unpublished_docs/upgrade_measures/env_roof_insulation.md` (site_page): Roof Insulation — overlay changed.
- `upgrade_measures/docs/upgrade_measures/env_window_film.md` → `upgrade_measures/unpublished_docs/upgrade_measures/env_window_film.md` (site_page): Window Film — overlay changed.

## comstock_amy2018_2025_release_3-v2 — 2026-10-16

Changes since `comstock_amy2018_2025_release_3-v1` (corpus_version `comstock_amy2018_2025_release_3-v1`): 117 documents (+3), 65 measures (60 documented, 5 tracked gaps), 7,948 chunks (+217). 74 documents changed, 43 unchanged in content.

Branches `stage-7-fetch`, `site-pdf-wordmark` and `stage-7-finish`, plus the eight tooling
branches merged between the two tags (PRs #25–#32, #34, #35 and the release PR). Documents
ComStock dataset release `comstock_amy2018_2025_release_3`: 117 documents, 65 measures
(60 documented, 5 tracked gaps), 7,948 chunks.

### Tooling and corpus changes, by hand

- **Three new measure documents.** dr_0004 (Lighting Control for Emission Reduction), dr_0007
  (Low Priority Device Switching During Peak Hours) and dr_0008 (Dim Lighting During Peak
  Hours), posted to the ComStock site as pre-publication PDFs (status `site_page`); 35 figure
  descriptions hand-authored for them to the W6 standard. Tracked gaps 8 → 5.
- **The ComStock site is read at `main`.** Its `2025_3` branch froze in July 2026; the commit
  fetched (`3b69dec`) is recorded in every github.io document's header and manifest row, so
  every one of those documents is re-stamped.
- **Section files per H2** (`sections/<source_id>/<document stem>/NN-slug.md`, 2,154 of them)
  and **per-document chunk files** (`chunks/<source_id>/<stem>.jsonl`) beside `chunks.jsonl`;
  `sections.json` names each section file. Every chunk carries `line_start`, `line_end` and
  `corpus_version`.
- **Table wrappers carry `data-source`** naming the LaTeX table file they were converted from.
- **Pandoc cross-references render as the target's quoted title** instead of an anchor, and
  heading levels are normalized; `bsc validate` fails on a surviving anchor.
- **Decorative leading images are omitted.** An OSTI report's cover grid and NREL wordmark,
  and a site-served PDF's ComStock wordmark and PRE-PUBLICATION stamp, are replaced by a
  one-line comment (W6.1; `decorative.py`, shared by build and validate). Figure 1 of the HP
  RTU Higher Compressor Lockout document, hidden by the first version of this rule, is
  visible again.
- **`body_sha256` on every manifest row** (the file minus its line-1 header), which is what
  lets `bsc changelog --from <tag>` tell a re-rendered document from a re-stamped one. The
  "64 documents re-rendered" line below is those two tooling changes (cross-references,
  decorative refs) and the section cut; no source text changed.
- **Crosswalk rows drop `doc_target`** and the top-level `deprecated` block; `corpus_path` and
  `doc_url` are the row's locations.
- **Overlays.** The seven sidecars whose `source_url` named the July commit are re-stamped
  (they had been skipped for one build). The four webinar-deck sidecars (85853, 87746, 89653,
  92766), unused since the registry excluded those decks at -v1, are deleted.
- **`bsc validate`** re-verifies overlay bitmaps past Windows MAX_PATH (35 images were reported
  unverifiable on Windows), and warns, without failing, when the Chroma index under `index/`
  is older than `chunks.jsonl` or holds a different record count.
- **`bsc changelog --from <tag> [--to <ref>] [--append] [--show <tag>]`** computes the
  document-level part of this entry from two manifests.
- **CI.** `ci.yml` runs tests and validate on Ubuntu and Windows on every push; `release.yml`
  cuts the GitHub Release from this entry when a `*_release_*-v*` tag passes both.

### Documents, computed

<!-- Generated by `bsc changelog`. Document lines cite `source_id/source_path`; add the tooling notes (why documents were re-rendered) by hand above the list. -->

### Added

- `upgrade_measures/assets/files/ComStock Measure Doc_Dim Lighting During Peak Hours.pdf` → `upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_Dim Lighting During Peak Hours.md` (site_page): Dim Lighting During Peak Hours — https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_Dim%20Lighting%20During%20Peak%20Hours.pdf
- `upgrade_measures/assets/files/ComStock Measure Doc_Lighting Control for Emission Reduction.pdf` → `upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_Lighting Control for Emission Reduction.md` (site_page): Lighting Control for Emission Reduction — https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_Lighting%20Control%20for%20Emission%20Reduction.pdf
- `upgrade_measures/assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.pdf` → `upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.md` (site_page): Low Priority Device Switching During Peak Hours — https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_Low%20Priority%20Device%20Switching%20During%20Peak%20Hours.pdf
- Measure `dr_0004` is now documented (tracked gap closed).
- Measure `dr_0007` is now documented (tracked gap closed).
- Measure `dr_0008` is now documented (tracked gap closed).

### Changed

- `github_site/docs/resources/resources.md` → `github_site/docs/resources/resources.md` (site_page): Resources — upstream source revised.
- `upgrade_measures/assets/files/ComStock Measure Doc_HP RTU Higher Compressor Lockout.pdf` → `upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_HP RTU Higher Compressor Lockout.md` (site_page): Heat Pump Rooftop Units With Higher Compressor Lockout Temperature for Heating — overlay changed.
- `upgrade_measures/docs/upgrade_measures/env_ext_secondary_window.md` → `upgrade_measures/unpublished_docs/upgrade_measures/env_ext_secondary_window.md` (site_page): Secondary Window System — overlay changed.
- `upgrade_measures/docs/upgrade_measures/env_ext_wall_insulation.md` → `upgrade_measures/unpublished_docs/upgrade_measures/env_ext_wall_insulation.md` (site_page): Exterior Wall Insulation — overlay changed.
- `upgrade_measures/docs/upgrade_measures/env_ext_window_replacement.md` → `upgrade_measures/unpublished_docs/upgrade_measures/env_ext_window_replacement.md` (site_page): Window Replacement — overlay changed.
- `upgrade_measures/docs/upgrade_measures/env_roof_insulation.md` → `upgrade_measures/unpublished_docs/upgrade_measures/env_roof_insulation.md` (site_page): Roof Insulation — overlay changed.
- `upgrade_measures/docs/upgrade_measures/env_window_film.md` → `upgrade_measures/unpublished_docs/upgrade_measures/env_window_film.md` (site_page): Window Film — overlay changed.
- 64 documents re-rendered from unchanged sources and overlays (tooling change; technical_reference 16, upgrade_measures 48).

## comstock_amy2018_2025_release_3-v1 — 2026-10-08

First tagged build. Branches `corpus-version` and `status-field`, stacked on `main` at
`887025c`. Documents ComStock dataset release `comstock_amy2018_2025_release_3`: 114
documents, 65 measures (57 documented, 8 tracked gaps), 7,731 chunks.

### Added

- `corpus_version` in every file's line-1 header, the manifest and the map; `bsc build
  --corpus-version <tag>` names a release build, otherwise the commit hash.
- Publication `status` (`osti_pdf`, `site_page`, `missing`) on every document, crosswalk
  row and chunk; declared per source in the registry, derived per document for measures.
- `source_url` and `publication_url` on every manifest row, in every file's header, in
  every overlay sidecar, and as `corpus_path` / `doc_url` on every crosswalk row.
- `index.json` and `sections.json` beside the map, validated against `schemas/`.
- A Published column in the map's tables; "Reading without a clone" in README and
  AGENTS.md; `AGENTS.md` as the canonical agent file with `CLAUDE.md` and `GEMINI.md`
  importing it; `llms.txt`; `LICENSE` (BSD-3), `CITATION.cff`, this file.

### Changed

- The two site-served measure PDFs moved from `upgrade_measures/draft_publications/files/`
  to `upgrade_measures/unpublished_docs/upgrade_measures/`, beside the six site-served
  measure pages: one class, status `site_page`.
- OSTI report 92504 is recorded under one canonical URL (`docs.nlr.gov`) in all four
  measure rows that share it, its header and its manifest row.
- `bsc validate` checks header fields against manifest rows, overlay links against
  artifacts, crosswalk locations against the manifest, and the index files' schema and
  freshness.

### Removed

- The four release-webinar slide decks (OSTI 85853, 87746, 89653, 92766) the upgrade-measures
  index page links outside the measures table: not measure documentation. 118 documents
  become 114. Their overlay sidecars remain in `overlays/`, unused.

### Deprecated

- `crosswalk.json` `doc_target` (the index page's literal link): use `doc_url` and
  `corpus_path`. Removed after this release.
