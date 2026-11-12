# PLAN: Fix the guidance mismatches the site-to-corpus acceptance test found

Written 2026-10-16 in the ComStock.github.io session and moved into this checkout the same day;
carried out here on branch `release-v3`.
Owner: Lauren Klun. Status: complete 2026-10-16. All of Phase A done; Phase B not needed. Amended 2026-10-16: v3 must re-fetch to pick up
the pkg_0012 draft posted after v2's site pin (see Finding 3 and step A.2).

## Goal

An agent that reaches the corpus from the ComStock website and pins to the current release tag,
as `llms.txt` tells it to, can follow every piece of advice in `llms.txt` and `AGENTS.md`
without hitting a field or file that does not exist at that tag.

## Where things stand (2026-10-16)

- The ComStock site now sends agents to the corpus: `llms.txt`, a home-page callout, a
  per-page "read this page as Markdown" link pinned to the corpus tag, and a schema.org
  Dataset block. The site's weekly `Sync corpus index` workflow copies `index.json` from the
  newest corpus release tag into the site's `_data/` and opens a PR when it changes.
- Acceptance test run 1 (recorded in the site's PLAN.md, Phase 3 step 5): a fresh agent given
  only the site URL answered the medium-office floor-to-floor question correctly (13 ft), cited
  tag `comstock_amy2018_2025_release_3-v2` the way `AGENTS.md` asks, in six fetches. Pass.
- Finding 1, confirmed against the raw files. `llms.txt` on `main`, line 24, says every
  `index.json` row carries `sections_dir` and `section_files` so a reader can fetch one H2
  instead of a whole document. `index.json` at tag v2 has no such fields. The v2 row for
  `4_4_geometry.md` holds only: `bytes`, `chunks`, `chunks_file`, `corpus_path`,
  `publication_url`, `sections`, `source_id`, `source_path`, `source_url`, `status`, `title`.
  The fields were added on `main` by PR #40 (`index-sections`) after v2 was tagged, so the
  "three-fetch route" exists on `main` but not at the tag agents are told to use.
- Finding 2, minor. `AGENTS.md` ("Start here") says read `CORPUS_MAP.md` first. Both the
  corpus `llms.txt` and the site's `llms.txt` say `index.json` first for readers without a
  clone. Harmless, but two orders for one audience is a small decision an agent should not
  have to make.
- Finding 3, found 2026-10-16 while reviewing this plan in the corpus checkout. The corpus's
  `fetch_state.json` pins the site clone at `3b69dec` (site PR #204). Since then site PRs #205
  and #206 posted `assets/files/ComStock Measure Doc_PV with Roof Insulation.pdf` and linked it
  from the measures index as pkg_0012 (`[13]+`), and `docs/for_developers/for_developers.md`
  changed. The corpus at `main` and at v2 lists pkg_0012 as `status: missing`, one of five
  gaps. A rebuild from the present `raw/` would not see any of this: v3 must re-fetch first,
  as v2 did when it picked up the three DR drafts.
- Finding 4, found 2026-10-16 at step A.2. `bsc fetch` does not move an existing clone:
  `_ensure_clone` in `src/buildstock_corpus/fetch.py` reads HEAD of a clone that is already
  on disk and only clones afresh when the directory is missing. v2 moved the site pin only
  because switching the registry from `2025_3` to `main` changed the clone directory name.
  For v3 the site clone was brought forward by hand with `git pull --ff-only` in
  `raw/.../repos/ComStock.github.io@main` (`3b69dec` to `2036a73`, site PR #208) before
  running `bsc fetch`. A fetch that updates a branch-ref clone to its remote tip is owed as a
  separate change; not part of this release PR. Done after v3 (branch `fetch-follow-ref`):
  `_ensure_clone` now fetches the ref and checks out `FETCH_HEAD` detached for an existing
  clone, with tests in `tests/test_fetch.py`.
- Not a bug. The agent reported the provenance header was not on line 1. The raw file at v2
  begins with the HTML comment on line 1; its fetch tool rendered a `---` line first. Do not
  change the header.

## Design rules (from the repo's own conventions)

- `AGENTS.md` is canonical; `CLAUDE.md` and `GEMINI.md` only import it; `llms.txt` is the
  discovery file for readers without a clone.
- Tags never move; `main` is rewritten on rebuilds. A release tag must equal the manifest's
  `corpus_version`, which only `bsc build` writes, and `CHANGELOG.md` must carry an entry for
  it before `release.yml` will create the GitHub Release.
- The "never run `bsc fetch`" rule in `AGENTS.md` and `README.md` is for readers; cutting a
  release does fetch, because the site is read at `main` and only a fetch moves the pin.
  `bsc fetch` brings an existing clone to its ref before reading its SHA, so a branch ref
  lands on the remote tip and a tag ref stays on its commit (added after v3; before it the
  clone had to be pulled by hand, see Finding 4). The cost it warns of is real: overlay
  sidecars pin the sha256 of their source image or PDF, so unchanged files keep their pins,
  but any sidecar whose `source_url` names the old commit is re-stamped (seven were at v2)
  and a changed source file makes its overlay stale, which the build reports. Never
  hand-edit anything under `processed/`.
- Work on a branch, PR to `main`.

## Decision to make first: a v3 tag, or wording only

| Option | What it is | Cost | Recommend when |
|--------|-----------|------|----------------|
| A. Tag v3 | Fetch, then rebuild at `--corpus-version comstock_amy2018_2025_release_3-v3`, so `index.json` at the tag carries `section_files` and the corpus picks up the pkg_0012 draft posted since v2; the advice in `llms.txt` becomes true at the tag and one tracked gap closes. | A `bsc fetch` (re-clones the site at `main`, re-hashes sources), a full `bsc build` (docling cache warm for everything but the one new PDF; expect tens of minutes), validate, changelog entry, four files that name the current tag, tag push. | The build and `bsc validate` run clean locally. This is the route the plan's own acceptance criterion (three fetches) asks for. |
| B. Wording only | Say in `llms.txt` and `AGENTS.md` that `section_files` appear in `index.json` from the next tag onward, and that at v2 the fallback is a line range from `sections.json` or the whole document. | One small PR, under an hour. | The build cannot be run now, or a content change is due soon and v3 should wait for it. |

Try A. Fall back to B if step A.2 or A.3 fails or takes longer than the session allows, and
leave a dated note saying why. Under B, pkg_0012 stays a tracked gap until the next tag.

## Phase A: tag v3

| # | Step | Files | Done when | Result |
|---|------|-------|-----------|--------|
| A.1 | Confirm the gap from this checkout: compare the `4_4_geometry.md` row of `index.json` at `main` with the same row fetched at `?ref=comstock_amy2018_2025_release_3-v2` via `gh api -H "Accept: application/vnd.github.raw"`. | none | `section_files` present on `main`, absent at v2, recorded in this table. | Done 2026-10-16. `main`: 13 keys incl. `sections_dir` (`sections/technical_reference/4_4_geometry`) and 9 `section_files`. v2 via `gh api`: 11 keys, no `section_files`. |
| A.2 | Re-fetch so the site pin moves past `3b69dec`: `uv run bsc fetch --release comstock_amy2018_2025_release_3`. Then confirm the new pin in `raw/comstock/comstock_amy2018_2025_release_3/fetch_state.json` (the ComStock.github.io clone's `sha` is the current site `main`; the ComStock code clone stays at `b77c60d` since `2025-3` is a tag) and that the PV with Roof Insulation PDF is in the fetched measures list. Any overlay whose source hash no longer matches must be dealt with before A.3, not after. | `raw/**` (gitignored), `fetch_state.json` | New site sha recorded; the new PDF hashed; no overlay reports a changed source. | Done 2026-10-16 (after the hand pull in Finding 4). Site clone `2036a73`, code clone `b77c60d` unchanged. upgrade_measures: 31 internal pages, 52 PDFs downloaded, 6 local PDFs (was 5), 0 unreachable; the PV with Roof Insulation PDF is in the state. Overlay check deferred to the build in A.3. |
| A.3 | Rebuild with the new version: `uv run bsc build --release comstock_amy2018_2025_release_3 --corpus-version comstock_amy2018_2025_release_3-v3`, then `uv run bsc validate --release comstock_amy2018_2025_release_3`. Expect every document re-stamped (new `corpus_version`, new site commit in `source_url`), one new document (pkg_0012, `unpublished_docs/upgrade_measures/ComStock Measure Doc_PV with Roof Insulation.md`, status `site_page`), one re-rendered from a changed source (`github_site/docs/for_developers/for_developers.md`), and otherwise no body changes; if many bodies change, stop and find out why before going on. Crosswalk counts should move from 60 covered / 5 gaps to 61 / 4. If pkg_0012 is still `missing`, the `[13]+` reference-style link on the index page was not parsed: fix the measures parser, do not hand-edit. | `processed/comstock/comstock_amy2018_2025_release_3/**` | Validate green; `index.json` and every line-1 header say `-v3`; `index.json` rows carry `sections_dir` and `section_files`; pkg_0012 has a `corpus_path` and the map's gap list names four measures. | First build 2026-10-16: 118 docs, 61 covered / 4 gaps, pkg_0012 rendered as `unpublished_docs/upgrade_measures/ComStock Measure Doc_PV with Roof Insulation.md` (65 KB, every table extracted as text, 5 figures + wordmark as bare image refs). But 9 overlay sidecars still named `3b69dec` in `source_url` and were skipped (tables 57 to 34, figure descriptions 855 to 820), the same side effect v2 saw. Ran `scripts/stamp_overlay_links.py` (9 stamped), rebuilt. Second build: 118 docs, 8,016 chunks, 2,182 section files, 57 tables + 855 figure descriptions in 56 docs, 61 covered / 4 gaps (dr_0009, dr_0010, dr_0011, hvac_0021), no extraction warnings. `bsc validate` OK (26 PDF-verified, 886 image-verified, 1 repair); only the two stale-index warnings. Bodies vs v2 (computed changelog): +1 added, 1 re-rendered from a revised source (for_developers), 9 with re-stamped overlays, 107 unchanged. **Owner decision 2026-10-16: describe the figures and check the tables before tagging.** New sidecar `overlays/.../assets/files/ComStock Measure Doc_PV with Roof Insulation.yaml`: 6 figure descriptions to the W6 standard (62-72 words each); tables checked cell for cell against 1.5x page renders and the PDF text layer. Tables 4, 6, 7, 8, 9 correct. Three repaired: Table 1 (split at the iv/v page break, rows lost, text shifted; replaced), Table 2 (grid emitted under the Table 3 caption; replaced), Table 5 (zone 1 / R-21 column dropped; replaced), plus one text repair demoting the stray `## Applicability` heading. Table 2 needed a small engine extension, `replaces.under_caption`, because its values equal Table 8's and the fingerprint alone matched both (overlay.py, 3 tests, README). Final build: 118 docs, 8,022 chunks, 2,181 section files (the demoted heading was one), 60 tables + 861 figure descriptions in 57 docs, 2 text repairs, 29 PDF-verified / 892 image-verified; validate OK, overlay and non-network tests green. Table 1 is decomposed into three sub-tables to stay under the 1400-char chunk limit. |
| A.4 | Changelog: `uv run bsc changelog --release comstock_amy2018_2025_release_3 --from comstock_amy2018_2025_release_3-v2 --append`, then write the hand bullets above the computed part: why v3 exists (section files in `index.json`, acceptance test from the website), that the site pin moved from `3b69dec` to the new commit, and anything PRs #39 and #40 changed in output. The computed part should itself list the new document and `Measure pkg_0012 is now documented (tracked gap closed)`, as the v2 entry did for dr_0004, dr_0007 and dr_0008; if it does not, the A.3 build did not pick the PDF up. | `CHANGELOG.md` | Top entry is `-v3` with today's date and names pkg_0012. | Done 2026-10-16. Computed part: +1 (pkg_0012, gap closed), 10 changed (for_developers revised upstream; 9 overlay re-stamps), 107 unchanged, 8,016 chunks (+68). Hand bullets: why v3, the new document and its undescribed figures, the pin move and re-stamp, PRs #39/#40, start order. `bsc changelog --show` reads it. |
| A.5 | Name the current tag everywhere it is named: the `Current:` line in `llms.txt`, the current-tag sentences in `AGENTS.md` and `README.md`, `version` in `CITATION.cff`. `grep -rn "release_3-v2"` across the repo, excluding `processed/` and `CHANGELOG.md`, should find nothing afterwards. | `llms.txt`, `AGENTS.md`, `README.md`, `CITATION.cff` | grep clean. | Done 2026-10-16. Also refreshed the counts those files carry: 118 documents, 41 over 100 KB, `index.json` ~155 KB raw / ~20 KB gzip (llms.txt had said ~6 KB, true only before PR #40). |
| A.6 | Finding 2 while these files are open: one canonical start order per reader type, worded the same in `AGENTS.md` and `llms.txt`. Clone readers start at `CORPUS_MAP.md`; URL-fetch readers start at `index.json`. | `AGENTS.md`, `llms.txt` | Both files state both orders identically. | Done 2026-10-16. Both open with "Two start orders, one per kind of reader": clone readers `CORPUS_MAP.md`, URL readers `index.json` at a tag. |
| A.7 | Record acceptance test run 2 under "Acceptance for the whole plan" in `PLAN.md`: source was the website URL only, pass, six fetches (site home, site `llms.txt`, corpus `llms.txt` + `AGENTS.md`, `index.json` at v2, the Geometry chapter), the two findings above and this fix. Mark the `-v3` row in `PLAN-staging.md` if that table tracks releases. | `PLAN.md`, `PLAN-staging.md` | Entry dated 2026-10-16 present. | Done 2026-10-16. Run-2 paragraph added under "Acceptance for the whole plan" in PLAN.md; PLAN-staging.md gained Stage 9 (steps 36-38) for the v3 release. |
| A.8 | Branch, commit, PR to `main`. CI (`ci.yml`) runs tests and validate on Ubuntu and Windows. Merge. | branch | PR merged, CI green. | Done 2026-10-16. Branch `release-v3` (commits `67342fc`, `419f772`, `7240f00`), PR #41, CI green on both runners, merged as `0de0a1b` with a merge commit. |
| A.9 | Tag the merge commit `comstock_amy2018_2025_release_3-v3` and push the tag. `release.yml` checks the tag equals the manifest's `corpus_version` and that `CHANGELOG.md` has the entry, then creates the GitHub Release. Note from the v2 record: the tag ruleset still needed a bypass actor; if the push is refused, that is why. | git tag | GitHub Release `-v3` exists. | Tag `comstock_amy2018_2025_release_3-v3` (annotated) on `0de0a1b`, pushed 2026-10-16; the tag ruleset accepted it, so step 33's bypass-actor item is resolved. `release.yml` run 38946978808. |
| A.10 | Prove the route at the new tag: fetch `index.json` at `?ref=...-v3`, read the `section_files` of `4_4_geometry.md`, fetch `<sections_dir>/<the floor-height file>` at the tag, confirm it carries its own line-1 header naming the parent `corpus_path` and `lines`. | none | Three fetches, the section file alone answers the question. | Done 2026-10-16. `index.json` at the tag: 21 KB on the wire, `corpus_version` v3, the Geometry row lists `sections_dir` and nine `section_files`. `06-floor-height.md` at the tag: 756 bytes, line 1 names the parent `4_4_geometry.tex`, status, both URLs and v3; it holds the 13 ft Medium Office row. Two corpus fetches after `llms.txt`. |
| A.11 | Back on the website: run the `Sync corpus index` workflow by hand from the ComStock.github.io Actions tab (or wait for Monday 12:00 UTC). It should open a PR replacing `_data/corpus_index.json` with the v3 file; merging it moves every per-page link and the Dataset block to v3, and the pkg_0012 page's "read as Markdown" link starts resolving to a real file. This is also the first live test of that workflow's PR-creation step. | ComStock.github.io repo | PR opened and merged; a page footer on the live site names `-v3`. | 2026-10-16: `Sync corpus index` dispatched by hand after `release.yml` finished (the workflow reads `releases/latest`, so the Release must exist first); run 38947127437 green and it opened site PR #209 replacing `_data/corpus_index.json` with the v3 file (`corpus_version` v3). First live run of the PR-creation step: works. Site PR #209 merged 2026-10-16 as `b159ac7` (owner's word); Pages deploy 38948362218 green. Live check: the For Developers page's "read this page as Markdown" link points at the `-v3` tag and that raw file returns 200 with a v3 header. The upgrade-measures index page carries no link, as expected: it is the measures index, not a corpus document. |

## Phase B: wording only (fallback)

| # | Step | Files | Done when | Result |
|---|------|-------|-----------|--------|
| B.1 | In `llms.txt` line 24 and the matching bullet of `AGENTS.md` ("Fetch `index.json` first"), state that `sections_dir` and `section_files` are present in `index.json` on `main` and from the next tag onward, and that at `comstock_amy2018_2025_release_3-v2` the way to read one heading is a line range from `sections.json` or the whole document after checking `bytes`. | `llms.txt`, `AGENTS.md` | An agent at v2 is not sent looking for fields that are not there. | |
| B.2 | Finding 2, as A.6. | `AGENTS.md`, `llms.txt` | Same as A.6. | |
| B.3 | Record acceptance run 2 as in A.7, plus a line that v3 is owed and why it was deferred. | `PLAN.md` | Entry present. | |
| B.4 | Branch, PR, merge. No tag. | branch | Merged. | |

## Evidence to carry over

- Site PLAN.md Phase 3 step 5 (in the ComStock.github.io checkout) holds the full run-1 record.
- Agent's fetch log, in order: `https://natlabrockies.github.io/ComStock.github.io/`,
  `.../llms.txt`, `raw.githubusercontent.com/.../main/llms.txt`, `.../main/AGENTS.md`,
  `.../comstock_amy2018_2025_release_3-v2/processed/comstock/comstock_amy2018_2025_release_3/index.json`
  (~6 KB), `.../technical_reference/documentation/reference_doc/4_4_geometry.md` (16 KB raw).
- Agent's answer: 13 ft, "Floor-to-Floor Heights by Building Type" table under "Floor Height",
  source `documentation/reference_doc/4_4_geometry.tex` at commit `b77c60d`, status `site_page`,
  no OSTI number, publication URL the 2025 Release 3 reference documentation PDF on the site.
