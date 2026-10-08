# buildstock-corpus: plan for AI consumers

Drafted 2026-09-24 from a review of commit `887025c6` (main, 2026-08-24). Decisions marked
**confirmed** were made by the corpus's product owner on 2026-09-24; the rest are proposals.
Each task names the module it lands in, the check that proves it done, and a size (S under a
day, M a few days, L more). Nothing here changes what the corpus contains; it changes how an
agent finds, pins, and cites it.

## Principles

1. **One build, one immutable name.** Anything a skill or a test case cites must resolve to the
   same bytes next year. Today only a commit hash does that.
2. **Metadata travels with the file.** A consumer that fetched one Markdown file over HTTPS has
   no clone, no manifest, and no map. Whatever it needs to cite the file has to be in the file.
3. **The URL-only path is the primary path.** A clean-room agent, a hosted assistant, and a
   future MCP server all read this corpus one HTTPS fetch at a time. Design for them first;
   the clone user already has everything.
4. **Status is data, not a folder name.** Folder names get renamed and do not travel with a
   fetched file. A field does.

## Decisions taken

- **Tag the corpus with GitHub release tags, starting with the December 2026 release.**
  (confirmed)
- **Every Markdown and YAML artifact carries the link to its publication.** (confirmed)
- **Add the corpus path and an absolute publication URL to every crosswalk row.** (confirmed)
- **Publish a machine index per release.** (confirmed)
- **Split large documents in whatever form is easiest for an agent while staying organized.**
  (confirmed; proposal in W5)
- **Image cleanup only where it needs no new information.** (confirmed as "maybe"; W6 splits
  it accordingly)
- **CI is future work.** (confirmed; listed in W7 as a proposal, not scheduled)
- **ResStock is to be determined.** (confirmed; W8 is a placeholder)
- **The six site-page measures and the two site-served measure PDFs are one class.** Status
  `site_page`: published on the ComStock site without an OSTI number, whether as a rendered
  page or a PDF file. All eight live in `unpublished_docs/upgrade_measures/`, a folder name
  the owner keeps ("no OSTI publication yet"); `draft_publications/` is gone. No live-URL or
  version tracking for the PDFs; they are replaced when an OSTI publication appears.
  (confirmed 2026-10-06)
- **Status vocabulary is three values:** `osti_pdf`, `site_page`, `missing`. The technical
  reference chapters are `site_page` (no OSTI number). (confirmed 2026-10-06)
- **Tags are named after the dataset release:** `<release id>-v<N>`, full release id, counter
  starting at `v1`. First tag: `comstock_amy2018_2025_release_3-v1`. (confirmed 2026-10-06)

## Open questions settled 2026-10-06

- **What is the status of the six site-page measures?** All six resolve on
  natlabrockies.github.io and are linked from the live upgrade-measures index, so the YAML
  comment "pages absent from the live ComStock site" is out of date. The owner chose to leave
  them as they are for now; see the decision above. W3.1 gives them, and the two site-served
  PDFs, status `site_page`.
- **Tag naming.** Decided: name the tag after the dataset release, not the calendar. See the
  decision above and W1.1.

## W1 · Versioning and the release process

**W1.1 · Tag each build after its dataset release and cut a GitHub Release.** *Done
2026-10-08.* First tag `comstock_amy2018_2025_release_3-v1` on merge commit `54f5c05` of
PR #24 (branches `corpus-version` + `status-field`, 21 commits), annotated, pushed; GitHub
Release cut from it with the CHANGELOG entry. Check passed: the raw URL at the tag serves
`index.json`, which names the tag as its `corpus_version`. Release step as run: finalize
CHANGELOG/CITATION/llms.txt → `bsc build --corpus-version <tag>` → validate + network link
test → `bsc changelog --from <previous tag> --append` and add the hand-written tooling
bullets (W1.3) → commit → PR → merge commit → `git tag -a` on the merge commit → push tag →
`gh release create --verify-tag --notes-file` with that entry. *Size:* S.

**W1.2 · Mid-release updates get a new build and a new tag.** *Operating rule from 2026-10-08.*
When a known-issues document is added or a measure PDF is revised inside a data release,
rebuild, validate, and tag `comstock_amy2018_2025_release_3-v2`. Consumers stay on the tag
they pinned until they choose to move. Never edit a tagged snapshot in place. `main` remains
the moving pointer for people who want the newest build and accept drift. README states the
policy ("Reading without a clone"). *Size:* S.

**W1.3 · Release notes generated from the manifest.** *Done 2026-10-08.* The manifest hashes
every input and output, so the difference between two builds is computable: documents added,
removed, revised upstream (input hash moved), with a changed overlay, or re-rendered from an
unchanged source, plus measure gaps opened or closed, registry exclusions and tooling
versions. `bsc changelog --from <tag> [--to <ref>] [--append]` prints that list in the
CHANGELOG's shape; `--append` inserts it at the top of `CHANGELOG.md`. Two things the plan
assumed turned out otherwise: `date_last_updated` is not in the manifest (it is document
metadata the map reads), and `output_sha256` moves on every build because line 1 names the
corpus version. So each row now also records `body_sha256` (the file without line 1), which
`bsc validate` checks; for a manifest that predates it (v1) the bodies are read out of git at
the ref. First run against v1: 65 documents re-rendered (steps 21 and 22), 49 unchanged.
*Where:* `changelog.py`, `cli.py`, `provenance.body_sha256`, `manifest.py`. *Check:* the
rendered entry lists an added document by `source_id/source_path` with its publication URL
(pinned in `tests/test_changelog.py`). *Size:* M.

**W1.4 · Record the corpus version inside the artifacts.** Write `corpus_version` into
`manifest.json`, the `CORPUS_MAP.md` provenance block, the index (W4), and each file's header
line (W2.1), so a fetched file says which build it belongs to. Until tags exist, use the
commit hash. *Where:* `manifest.py build_manifest`, `corpus_map.py _render`, `build.py
_write_processed`. *Check:* line 1 of any file names the tag. *Size:* S.

## W2 · Every artifact links to its publication

**W2.1 · Extend the provenance line.** Today line 1 is
`<!-- comstock <release> | <source_id> | <upstream path> -->`. Add the publication URL, the
upstream URL at its pinned ref, the publication status (W3), and the corpus version:

```
<!-- buildstock-corpus | comstock | comstock_amy2018_2025_release_3 | technical_reference
     | source: documentation/reference_doc/4_4_geometry.tex
     | source_url: https://github.com/NatLabRockies/ComStock/blob/2025-3/documentation/reference_doc/4_4_geometry.tex
     | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf
     | status: osti_pdf | corpus_version: comstock_amy2018_2025_release_3-v1 -->
```

*Done 2026-10-07, branch `status-field`.* Landed as **one line**, not wrapped (owner
decision): the three positional segments are unchanged and `status`, `source_url`,
`publication_url`, `corpus_version` follow as labelled segments in a fixed order, so a parser
that skips the first comment or reads only `head -1` still works. For an OSTI PDF both URLs
are the OSTI URL; for a site page or site-served PDF `publication_url` is the live site URL;
for a reference chapter it is the release's reference-documentation PDF. Build resolves the
values once per document and both the header and the manifest row read them from there;
`bsc validate` compares every header field to its row. Longest header is 535 characters (a
site-served PDF, whose two percent-encoded URLs are the bulk of it). *Size:* S.

**W2.2 · Same fields in the manifest.** *Done 2026-10-07, branch `status-field`.* Every
artifact row carries `source_url` (the upstream file at the clone's commit sha, or the OSTI
URL), `publication_url`, `status` (from W3.1) and `corpus_version`. The registry supplies the
facts: a site-backed source names its `site_url`, the latex source names the one
`publication_url` all 19 chapters belong to (the release's reference-documentation PDF,
listed in the References table of the site's Resources page; owner chose to record the PDF
only, not the listing page). `links.py` builds the URLs; `bsc validate` requires both links
as absolute https and the row version to match. `tests/test_links_network.py` fetched all
167 distinct URLs with 200 on 2026-10-07; it is deselected by default (`pytest -m network`).
*Size:* S.

**W2.3 · Crosswalk rows carry the corpus path and an absolute URL.** *Done 2026-10-07, branch
`status-field`.* Every measure row has `corpus_path` (the processed Markdown, null for a gap)
and `doc_url` (the document's own `publication_url`, so row and document agree). `doc_target`
is kept this release and flagged deprecated in the crosswalk's top level. `bsc validate`
checks a covered row points at a manifest artifact and at that artifact's publication; the
map's measures table reads `corpus_path` from the row instead of joining filenames. Two
owner decisions landed with it: OSTI report 92504, which documents dr_0005, dr_0006, pkg_0007
and pkg_0009, is recorded everywhere under the `docs.nlr.gov` spelling (registry
`canonical_urls`); and the four release-webinar slide decks (85853, 87746, 89653, 92766) the
index page links outside the measures table are excluded from the corpus (registry
`exclude_urls`), leaving 114 documents. The dispatch-schedule report (89343) stays. *Size:* S.

**W2.4 · Overlay files name their source.** *Done 2026-10-07, branch `status-field`.* Every
sidecar carries `source_url` and `publication_url` as top-level keys beside `source_id` and
`source_path`, stamped from the manifest by `scripts/stamp_overlay_links.py` (text insertion,
comment blocks untouched, idempotent). The four sidecars of the excluded webinar decks are
stamped from the fetch record. Build skips a sidecar whose links differ from its document's;
`bsc validate` reports an applied overlay whose links are absent or differ from its
artifact's. `overlays/README.md` documents the fields. *Size:* S.

**W2.5 · The map shows the links.** *Done 2026-10-07, branch `status-field`.* A Published
column in the document tables and the measures table: the status word (`osti_pdf`,
`site_page`) linking the publication URL, a dash for a gap. Short label, not the URL, by
owner decision, so the map stays readable. Rendering only; `bsc map` regenerated it without
a rebuild. *Size:* S.

## W3 · Publication status as a field

**W3.1 · One status vocabulary.** *Done 2026-10-06, branch `status-field`.* Three values
(see `src/buildstock_corpus/status.py`): `osti_pdf` (a report with an OSTI number, recognised
from its URL), `site_page` (published on the ComStock site without one, page or PDF alike),
`missing` (documented nowhere; crosswalk rows only). Latex/markdown sources declare it in
`sources/*.yaml`; the measures source derives it per document from the index page's link
kind. Landed in the manifest (per artifact), the crosswalk (per measure) and chunk metadata;
`bsc validate` rejects a missing or unknown value. Still to carry it: the provenance line
(W2.1), the map (W2.5) and the index (W4.2). *Size:* S.

**W3.2 · Folder names that say what the status is.** *Done 2026-10-06 in the same change.*
`draft_publications/` is folded into `unpublished_docs/upgrade_measures/`, so the two
site-served PDFs sit beside the six site-served pages: one class, one folder. The folder
keeps its name at the owner's request; the registry comment now says what "unpublished"
means there. No further rename is planned. *Size:* S.

**W3.3 · Citation guidance per status.** *Done 2026-10-08 with W4.3.* A "Citing" section in
`AGENTS.md`: `osti_pdf` by its OSTI URL; `site_page` by its ComStock-site URL and the corpus
version, noting no OSTI number; `missing` has nothing to cite; always name
`source_id/source_path` and `corpus_version`. README carries a one-line pointer (owner
decision). *Size:* S.

## W4 · Findable without a clone

**W4.1 · "Reading without a clone" in README.md and CLAUDE.md.** *Done 2026-10-08, branch
`status-field`.* Raw URL pattern, pin to a tag (commit hash until then; `main` moves), the
recipe (index.json, sections.json only for headings, then one document), the citation rule,
and a size warning with real numbers. The pattern was fetched unauthenticated from
raw.githubusercontent.com. *Size:* S.

**W4.2 · `index.json` per release, generated beside the map.** *Done 2026-10-08, branch
`status-field`.* Two files, by owner decision: 114 documents' headings cannot fit the 30 KB
target, and a consumer that only needs titles and links should not pay for them.
`index.json` (67 KB raw, 6 KB gzipped): per document `title`, `source_id`, `corpus_path`,
`source_path`, `source_url`, `publication_url`, `status`, `bytes`, `sections` (count); per
measure `measure_id`, `upgrade_id`, `upgrade_name`, `corpus_path`, `doc_url`, `status`; plus
`corpus_version` and `manifest_sha256`. `sections.json` (194 KB raw, 25 KB gzipped): every
heading with `level`, `line_start`, `line_end` (1-based, line 1 is the header), keyed by
corpus path; W5.1 adds each section's file path here. Links are explicit, not derivable.
Both validate against `schemas/*.schema.json` at generation and in `bsc validate`, which
also flags a stale one. Amended target: index under 70 KB raw / 10 KB gzipped; sections under
30 KB gzipped. The acceptance walk becomes four fetches when headings are needed. Growth: ~550
B per document in the index, ~1.7 KB in sections; a shorter site host shrinks both. *Size:* M.

**W4.3 · `AGENTS.md` and `llms.txt`.** *Done 2026-10-08, branch `status-field`.* `AGENTS.md` is
canonical; `CLAUDE.md` and `GEMINI.md` are one-line `@AGENTS.md` imports (Claude Code and
Gemini CLI both support the syntax; Codex reads AGENTS.md by default). `llms.txt` at the root
links AGENTS.md, index.json, sections.json, the map, README, manifest, crosswalk and schemas,
using `main` and stating the tag pattern for pinning. *Size:* S.

## W5 · Granularity and chunk provenance

**W5.1 · Section files for every document, whole files kept.** *Done 2026-10-08, branch
`section-files`.* `sections/<source_id>/<document stem>/<NN>-<slug>.md` for every H2 (with its
H3+ beneath it) plus `00-<title slug>` for text before the first H2; 2,076 files, ~7.4 MB,
tiling each document from line 2. Line 1 is the document's header plus `corpus_path`,
`section`, `lines`. Flat by source, not a mirror of the document tree: the mirror reached
268-char paths and git refused them on Windows (owner switched layouts); flat is 234 chars.
Slugs capped at 40. Not hashed into the manifest: `bsc validate`
regenerates and compares (absent dir = derived, not a violation; `bsc map` regenerates the
tree). `sections.json` names the file for every H2 and preamble. *Size:* M.

**W5.2 · Chunk metadata that locates the chunk.** *Done 2026-10-08, branch `chunk-provenance`.*
Every chunk carries `line_start`, `line_end` (1-based lines of the processed file, the whole
paragraphs the chunk draws from; the overlap tail is not counted) and `corpus_version`. The
heading path stays in `section` as a string, since Chroma metadata holds only scalars. Chunk
ids and texts are unchanged. Check over all 7,731 chunks: each chunk's last paragraph lies
within its range and every range sits inside one `sections.json` section. *Size:* S.

**W5.3 · Per-document chunk files.** *Done 2026-10-08, branch `chunk-files`.*
`chunks/<source_id>/<document stem>.jsonl`, one per document (empty when it has no chunks),
byte-exact slices of `chunks.jsonl` that reproduce it when concatenated in manifest order;
`index.json` names each document's `chunks_file` and `chunks` count. Not hashed into the
manifest: `bsc validate` splits `chunks.jsonl` and compares; `bsc map` regenerates. Median
77 KB, largest 711 KB; the README says a chunk file is larger than its document and points
readers at section files for text. *Size:* S.

**W5.4 · Tables carry their source file name.** *Done 2026-10-08, branch `table-source`.*
Every `<div id="tab:...">` wrapper in the 19 chapters carries `data-source="tables/<file>.tex"`
(or the chapter file for the one inline table): 78 stamped, 46 where label == file name. The
extractor records which inlined file defined each label. Overlay counts unchanged. Side
effect: Appendix A repacks into 3 more chunks, so its chunk ordinals shift; `bsc index` is due.
*Size:* S.

**W5.5 · Pandoc artefact cleanup.** *Done 2026-10-08, branch `cleanup`.* The 253 cross-reference
anchors are rendered as the target's title in quotes (Table “Window Property Data Sources”,
Section “ComStock Data Access”), resolved from every `\label` in the LaTeX project; equation
labels keep plain text. Owner chose titles over reconstructed numbering (pandoc's numbers
were per-file and wrong for the split chapter 4). Heading levels normalized so no heading
sits more than one level below the previous. `bsc validate` fails on any surviving
`data-reference-type`. *Size:* S.

## W6 · Images

**W6.1 · Drop or mark image references that have no overlay entry.** *Done 2026-10-08, branch
`cleanup`, narrowed.* The premise did not hold: the endorsed figure standard skips decorative
images entirely (no entry), so the overlays do not list them. What is mechanical: the first
two docling images of every measure PDF are the cover grid and the NREL wordmark (14 overlay
headers say so; all 49 PDFs match), and build replaces their undescribed `![Image](...)` refs
with a one-line comment -- 98 refs. The 176 undescribed real figures (six measure pages, two
site PDFs, 000002+ in ~16 OSTI reports) stay visible as the gap they are (owner decision,
option 1). `bsc validate` flags a surviving cover/wordmark ref in a PDF. *Size:* S.

**W6.2 · Descriptions for data-dense figures.** Proposal only, marked maybe by the owner: some
figures carry more data than prose can hold. Leave them as the description standard the
rollout settled on; do not expand scope here.

## W7 · Repository hygiene

**W7.1 · Now:** *Done 2026-10-08, branch `status-field`.* `LICENSE` (BSD-3 for the whole repo,
owner decision; copyright holder copied from upstream ComStock's license, to confirm with the
lab), `CITATION.cff` (sole author, NLR, type dataset, no DOI, version = the tag read),
`CHANGELOG.md` (convention + an Unreleased entry for the two branches). `AGENTS.md` and
`llms.txt` landed in W4.3. *Size:* S.

**W7.2 · Future work, proposed:** a CI workflow that runs `bsc validate` and the test suite on
every push, blocks a release tag unless both pass, and runs `bsc changelog` to draft the
release notes. Until it exists, the release step in W1 is a checklist a person runs.

## W8 · ResStock

To be determined. The layout `processed/<product>/<release>/` needs no change; a ResStock entry
in `sources/` and the same status and link fields are all that is required when its
documentation is in scope.

## Sequencing

**Before the December build, so paths and names change once:** W3.1, W2.1 to W2.5, W1.4,
W4.2, then W1.1 as the first tag. W4.1, W4.3, W7.1 can land any time before the tag. (W3.2 is
deferred; see above.) The step-by-step order actually being worked is in `PLAN-staging.md`.

**In the December build or the one after:** W5.1 to W5.5, W6.1, W1.3.

**Any time after the first tag:** W1.2 becomes the operating rule; W7.2 when there is time.

## Acceptance for the whole plan

Give an agent nothing but the repository URL and the question "what floor-to-floor height does
ComStock assume for a medium office, with a citation". It should fetch `llms.txt` or the
README, then `index.json`, then one section file, and answer with the value, the section, the
upstream file at its tag, the publication URL, and the corpus version, in three fetches and
under 40 KB transferred. Every one of those facts should have come from the fetched files, not
from the agent's memory.
