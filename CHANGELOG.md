# Changelog

One entry per corpus build that is tagged. Tags are named `<release id>-v<N>` after the
dataset release the build documents, and never move. Entries list documents added, removed
or changed (by input hash), overlays changed, and tooling changes that alter output.
`bsc changelog --from <tag>` computes the document-level part from two manifests, telling a
document re-rendered by a tooling change (body hash moved) from one merely re-stamped with
the new version, and `--append` inserts it here; the bullets saying *why* documents were
re-rendered are written by hand above it.

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
