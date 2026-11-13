# buildstock-corpus

Level 1 **AI-ready content pipeline** for the BuildStock domain-knowledge corpus.

Ingests one dataset release of one product at a time and emits clean, machine-readable,
**release-tagged** artifacts plus a provenance **manifest** and a queryable local **RAG
index** — so retrieval options can be tested without locking in a vector store. Every
artifact is tied to its source hash and dataset release; nothing is published without
provenance.

Two products are in the corpus, each in its own folder with its own tag:

| Product | Dataset release | Folder | Documents | Measures | Current tag |
|---|---|---|---|---|---|
| ComStock (commercial buildings) | 2025 release 3 | `processed/comstock/comstock_amy2018_2025_release_3/` | 118 | 65 (61 documented) | `comstock_amy2018_2025_release_3-v3` |
| ResStock (housing) | 2025 release 1 | `processed/resstock/resstock_amy2018_2025_release_1/` | 62 | 32 (all documented) | `resstock_amy2018_2025_release_1-v1` |

## Requirements

- [`uv`](https://docs.astral.sh/uv/) (manages Python 3.12 and all deps)
- `git` (sources are fetched by cloning tagged repos). On Windows, keep the checkout
  near the drive root or set `git config --global core.longpaths true`: the deepest paths
  under `processed/` are about 235 characters, and the 260-character default limit
  leaves little room for a long parent directory.

## Usage

Releases are named for the OEDI data lake convention,
`<dataset type>_<weather data>_<year of publication>_release_<release number>`, so a corpus
artifact names the same release the published data does. Upstream git tags and branches do
not follow it (`2025-3`, `2025_3`) and are pinned separately in the source registry.

Every command names the product and its release; with two products registered, `bsc` does
not guess.

```bash
P=comstock; REL=comstock_amy2018_2025_release_3     # or: P=resstock; REL=resstock_amy2018_2025_release_1

uv run bsc fetch     --product $P --release $REL   # download + hash raw sources -> raw/ (moves an existing clone to its ref; a branch ref lands on its tip)
uv run bsc build     --product $P --release $REL   # extract -> normalize -> chunks + manifest + map -> processed/
uv run bsc map       --product $P --release $REL   # regenerate CORPUS_MAP.md on its own (seconds)
uv run bsc index     --product $P --release $REL   # embed chunks -> index/
uv run bsc query "How does ComStock determine HVAC system type?" --product $P --release $REL
uv run bsc validate  --product $P --release $REL   # enforce provenance invariants
uv run bsc changelog --product $P --release $REL --from $REL-v1   # release notes: diff this build against a tag
```

That is the **authoring** pipeline, and it is not where a cloner starts. `processed/` is
committed, so a fresh clone already has the corpus — see below. Do not begin with
`bsc fetch`: it re-downloads every source PDF and can invalidate the hand-authored overlay
hash pins that let a transcribed table prove it matches its source.

## Reading the corpus

Start at **`processed/<product>/<release>/CORPUS_MAP.md`**. It lists every document with its
title, path, top-level sections and last-updated date, plus a measure → upgrade-id →
document routing table and the corpus's known gaps — so one read tells you which file to
open instead of grepping all of them. `bsc build` writes it, and `bsc map` regenerates it
from the built artifacts in a second or two without touching `raw/`.

Which consumer you are decides what you need:

- **An agent or human with the repo checked out** needs nothing but `processed/`. The
  markdown is committed and citable; read and grep it directly. No index, no API key.
- **A consumer that can fetch URLs but has no clone** (a hosted assistant, an MCP server,
  a clean-room agent) reads the same files over HTTPS: `index.json` first, then one
  document. See [Reading without a clone](#reading-without-a-clone). No index, no API key.
- **A consumer that wants semantic retrieval** needs the vector store: `bsc index` then
  `bsc query`. Budget for it — embedding ComStock's 8,022 chunks takes on the order of an
  hour on a laptop CPU (ResStock's 4,183 took six minutes on a workstation), and `index/`
  is gitignored, so every clone builds its own, one store per product. Retrieval finds a
  table best when the question uses the document's own terms ("stock saturation",
  "applicability"); the map and `index.json` are the surer route to a known table.
  `bsc query --answer` additionally needs `ANTHROPIC_API_KEY` and the `llm` extra;
  retrieval alone does not.

How to cite a document depends on its publication status; the rules are in
[AGENTS.md § Citing](AGENTS.md#citing). To cite the corpus itself, as distinct from
ComStock's and ResStock's documents, use [CITATION.cff](CITATION.cff) and name the release
tag you read. The repository is under the BSD-3 [LICENSE](LICENSE); the underlying
documentation remains ComStock's and ResStock's and is attributed per each product's
citation page. `AGENTS.md` is the canonical instructions file for
agents; `CLAUDE.md` and `GEMINI.md` are one-line pointers that import it, and `llms.txt` at
the root is the discovery file for readers without a clone.

`bsc validate` checks the manifest, the overlays, and whether `CORPUS_MAP.md`, `index.json`
and `sections.json` are stale relative to `manifest.json`. It does **not** open the Chroma
store, so a stale index passes silently — re-run `bsc index` after any build that changed
`chunks.jsonl`.

### Reading without a clone

Every file under `processed/` is served raw by GitHub, unauthenticated:

```
https://raw.githubusercontent.com/NatLabRockies/buildstock-corpus/<ref>/processed/<product>/<release>/<path>
```

**Pin `<ref>` to the product's release tag**, `<release id>-v<N>` (currently
`comstock_amy2018_2025_release_3-v3` and `resstock_amy2018_2025_release_1-v1`; a product's
newest is its topmost entry in `CHANGELOG.md`). A tag never moves, so a citation made
against it resolves to the same bytes next year. A product's folder exists only at its own
tags and on `main`: the ComStock tag has no ResStock folder. `main` is rewritten on every rebuild; use it only when
you want the newest build and accept that paths and content drift. Every file's line-1
`corpus_version` names the tag (or, for an untagged build, the commit) it came from.

The recipe is two fetches:

1. **`index.json`** of the product (ComStock's is ~155 KB raw, ~20 KB gzip-compressed over
   the wire; ResStock's ~85 KB and ~11 KB). Every document
   with its `title`, `corpus_path`, `status`, `source_url`, `publication_url`, `bytes`, and
   its section files: `sections_dir` plus `section_files`, one `<NN>-<slug>.md` per H2 (and
   a `00-` preamble when text precedes the first H2), the slug being the heading. Every
   measure with its `upgrade_id`, `corpus_path` and `doc_url`. Pick the document; for a
   measure, start from its `upgrade_id` or `measure_id`.
2. **One section of it**, at `<sections_dir>/<name>`: the heading and everything beneath it
   down to the next H2, usually a few KB. Or **the whole document**, at `<corpus_path>`.
   Line 1 of either is a provenance header carrying the release, upstream path, `status`,
   both URLs and the `corpus_version` (a section file's also names its parent
   `corpus_path`, its `section` and the `lines` it spans), so the file alone is enough to
   cite. Quote `source_id/source_path` and the `corpus_version`, and send a reader to the
   `publication_url`, not to the markdown.

**`sections.json`** (ComStock's ~365 KB raw, ~43 KB over the wire; ResStock's ~275 KB and
~33 KB) adds every heading's level and `line_start`/`line_end`, including H3 and below;
fetch it only when you need those, for example to cite one table inside a large section.
A range there is the heading's own text, from the heading line to the line before the next
heading of any level, and does not include its sub-headings: to cite a table, take the range
of the innermost heading above it (in ResStock's chapter 3a, the "Options" H5 under
"Geometry Stories", lines 1019-1061, not the H4 itself, which is lines 1003-1004). A whole
H2's range is the `lines` field on line 1 of its section file.

**Mind the size.** In ComStock, 41 of the 118 documents are over 100 KB and four are over
200 KB; the largest, the reference documentation's Appendix A, is 450 KB. In ResStock, 14
of the 62 are over 100 KB and two over 200 KB; the largest is the report 95032 at 291 KB.
Check `bytes` in the index before fetching a whole document; fetch the section file
instead, or use the line range from `sections.json`. Most section files are a few KB (the
median is about 2 KB in both products), but a section is a whole H2: in ResStock's guide
chapter 3a the Geometry and Envelope sections are about 60 KB each.

Both JSON files stamp the `manifest_sha256` they were generated from and validate against
[`schemas/`](schemas/) in this repo; code against the schema, not the example.

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

### Continuous integration

`.github/workflows/ci.yml` runs the test suite and `bsc validate` for every release under
`sources/` on each push, on Ubuntu and Windows, from `uv sync --locked` alone: the tests
never import the extractors. `.github/workflows/release.yml` runs on a `<release id>-v<N>`
tag push, repeats those checks at the tag, requires the tag to be the manifest's
`corpus_version` and `CHANGELOG.md` to carry an entry for it, and then creates the GitHub
Release with that entry as its notes. A tag whose tree fails gets no Release.

## Layout

- `sources/<product>_<release>.yaml` — source registry (repos, tag, measure URLs)
- `raw/<product>/<release>/` — downloaded originals (gitignored)
- `processed/<product>/<release>/` — clean markdown, referenced image assets, `CORPUS_MAP.md`, `index.json`, `sections.json`, `sections/`, `chunks/`, `crosswalk.json`, `chunks.jsonl`, `manifest.json`
  - `sections/<source_id>/<document stem>/<NN>-<slug>.md` — every H2 of every document as its
    own file (plus `00-` for the text before the first H2), each with a citable line-1
    header naming its parent and line range. A pure function of the document: `bsc
    validate` regenerates them and compares, so they are not hashed into the manifest.
  - `chunks/<source_id>/<document stem>.jsonl` — each document's rows of `chunks.jsonl` as
    their own file, byte for byte, for a consumer indexing a subset of documents; named
    per document as `chunks_file` in `index.json`. Regenerated and compared by `bsc
    validate` like the section files. For reading text, fetch the section file instead:
    a document's chunk file is larger than the document, since chunks overlap and carry
    metadata.
  - `CORPUS_MAP.md` is the entry point for reading the corpus: every document's title,
    path, sections and date, the measure→upgrade-id→document routing table, and the known
    gaps. Generated (never hand-edited) and stamped with the sha256 of the manifest it was
    derived from, so `bsc validate` can tell a current map from a stale one.
  - `index.json` and `sections.json` are the same facts as data, for a consumer that
    fetches the corpus over HTTPS: every document and measure with paths, links, status and
    size; every heading with its line range. Generated beside the map, stamped the same
    way, and validated against `schemas/`.
  - `crosswalk.json` maps each measure to its documentation and its upgrade id in this
    release. Every measure also carries `date_last_updated` — when its document last
    changed at its source — alongside the `date_last_updated_source` that established it
    (`pdf_moddate` from the published PDF's own metadata, or `git_commit` from the site
    repo). A measure whose documentation does not exist yet is undated rather than given a
    stand-in.
- `index/<product>-<release>/` — persistent Chroma store (gitignored)
