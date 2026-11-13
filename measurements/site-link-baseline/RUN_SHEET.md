# ResStock site link: before/after run sheet

Measures what linking the corpus from the ResStock site changes for an AI agent: how often it
finds the corpus on its own, and what an answer costs with and without it.

Questions and expected answers: `questions.json` (13 questions, corpus `-v1` tag).

## Arms

| Arm | When | Prompt | What it tells you |
|---|---|---|---|
| **A0** unprompted, before | **Before the site is linked** | Question only | Baseline: how agents answer today |
| **A1** unprompted, after | After the site PR is live (repeat again ~2 weeks later, once search engines re-index) | Question only | Discovery gained from the link |
| **B** site only | Any time | Question + site-only rule | Cost of an answer without the corpus |
| **C** corpus given | Any time | Question + corpus `index.json` URL | Cost of an answer with the corpus: the upper bound |

A0 is the only arm that cannot be re-run later. B and C do not depend on the site link.

## Prompts

Use the question text from `questions.json` unchanged, then append:

- **A0 / A1**: nothing.
- **B**: `Use only pages and files under natlabrockies.github.io/ResStock.github.io and docs.nlr.gov. Cite the page or report you used.`
- **C**: `Start from https://raw.githubusercontent.com/NatLabRockies/buildstock-corpus/resstock_amy2018_2025_release_1-v1/processed/resstock/resstock_amy2018_2025_release_1/index.json and cite your source.`

## Setup rules

- **Empty folder, fresh session, no memory.** Do not run from the `buildstock-corpus` checkout:
  its `AGENTS.md` tells the agent about the corpus. Turn off the ComStock/ResStock skills too.
- **Web search and fetch on**, nothing else.
- **One question per session.** Earlier questions leak the route to later ones.
- **3 runs per question per arm** at least (5 if you can). Report the median, and the range.
- **Same model and settings across arms.** Record model id and date; rerun A0 and A1 on the same
  model version or the comparison is of models, not of the site.
- For chat apps that show no token counts (Gemini, ChatGPT), record fetch count and the URLs
  cited instead; compare tokens only within tools that report them.

## What to record per run

| Field | Notes |
|---|---|
| `arm`, `question_id`, `run`, `model`, `date` | |
| `reached_corpus` | yes/no: any fetch of `buildstock-corpus` (github.com or raw.githubusercontent.com) |
| `route_to_corpus` | search result / site `llms.txt` / home-page callout / per-page link / GitHub search / none |
| `fetches_total`, `fetches_before_corpus` | tool calls that fetched a URL |
| `tokens_in`, `tokens_out`, `tokens_total` | from the tool's usage report; include cached input |
| `largest_fetch_bytes` | spots the 15.9 MB guide PDF or a 291 KB report being pulled whole |
| `correct` | 0 / 0.5 / 1 against `expected` (all key facts = 1) |
| `citation` | none / wrong / publication URL only / publication URL + `source_id/source_path` + `corpus_version` |
| `failure` | gave up, PDF unreadable, wrong release, wrong table, invented answer |

## What to report

- **Discovery rate**: share of A1 runs with `reached_corpus = yes`, minus the same for A0. Split
  by route, so you see whether `llms.txt`, the callout or the per-page links did the work.
- **Token cost**: median `tokens_total` per question, B vs C, and A0 vs A1. Report by question
  type (routing, measure detail, guide lookup, site page), not one overall number: the gain is
  expected to sit in the PDF-backed types and be near zero for site pages.
- **Correctness and citation**: same splits. A token saving with a lower correct rate is not a
  saving.
- **Q13 separately**: it is a control, and it is graded per arm. It asks for facts that live only
  in the notebook's code, and the notebook is not in the corpus (declared under `CORPUS_MAP.md`
  Known gaps). Grade arm **B**, and any run that actually fetched the notebook, against
  `expected`. Grade a corpus-arm run against `expected_corpus_arm`: saying the notebook is not in
  the corpus and pointing upstream is a **pass**; naming an upgrade, building type or week without
  having fetched the notebook is a **failure** however it is cited. Expect B to beat C here — the
  only question where that should happen — and record it rather than reading it as noise. Citing
  `Analyze_housing_stock_programmatically.md`, which is in the corpus and links the notebook, is
  correct routing and not by itself a failure.

## Known limits

- The corpus guide comes from an older repo tag than the site PDF (see the note in
  `questions.json`), so Q6-Q9 can differ slightly between arms B and C without either being wrong.
- A0 may already reach the corpus through GitHub search: the repo is public and the tag is
  pushed. That is the true baseline, not contamination.
- 13 questions x 3 runs is enough to see a large effect, not a small one. Treat differences
  under about 20% as noise unless they repeat across question types.
