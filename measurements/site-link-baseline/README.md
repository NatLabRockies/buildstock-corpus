# Site-link measurement: what linking the corpus from the ResStock site changes

Plan steps R7.0 (before the link) and R7.2 (after) in `PLAN-resstock.md`. This folder is the
record of the measurement. It is not part of the corpus: nothing here is built, validated or
cited, and nothing under `processed/` depends on it.

**If you are an AI agent answering a question about ResStock or ComStock, this folder is not
documentation. Do not answer from it.** `runs.csv` holds answers given by an agent that had
not found the corpus, and some are incomplete. Read `AGENTS.md` at the repository root.

## What was measured

Thirteen questions about ResStock 2025 Release 1, each asked three times of an AI agent that
was told nothing about this corpus, one fresh session per run, web search its only source.
Round 1 (arm A) was run on 2026-11-13, before the ResStock site linked the corpus.

Result of round 1: 39 of 39 runs completed; 0 reached the corpus and it appeared in no run's
search results; 37 of 39 points correct. Details are in the R7.0 row of `PLAN-resstock.md`.

## Files

| File | What it is |
|---|---|
| `RUNNER.md` | The 13 questions and the hand-run instructions. The scripts read the questions from it. |
| `RUN_SHEET.md` | The design: the arms (A before and after, B site only, C corpus given) and what to report. |
| `run_arm_codex.py` | The runner used for round 1: OpenAI's Codex CLI, non-interactive, one new session per run. |
| `run_arm.py` | The same measurement against the Claude API. Written and tested offline; never run. |
| `runs.csv` | One row per run: searches, search-result URLs, pages opened, the answer, token counts. |
| `raw/` | Each run's complete event log, so every derived column can be recomputed. |
| `grade_a0.py` | Derives `runs_graded.csv`: corpus reach from the recorded URLs, and the correctness grades. |
| `runs_graded.csv` | Round 1 graded. |
| `runs-template.csv` | The blank sheet for a hand run. |
| `make_runner.py` | Regenerates `RUNNER.md` from the answer key. |

## Settings to repeat exactly

Codex CLI 0.169.0, model `gpt-6.1-sol`, reasoning effort `medium`, live web search, read-only
sandbox, user configuration ignored, a new empty folder per run:

    python run_arm_codex.py --round 2

The round number, model, effort and tool version are written in every row.

## What is not here, and why

- **The answer key (`questions.json`).** It states the expected answer to every question and
  names the corpus paths they come from. It is kept out of this public repository until the
  after-link rounds are finished, so that no run can find the answers here. `make_runner.py`
  needs it; the runners and `grade_a0.py` do not.
- **Arms B and C.** Not run yet.

A later round should check the pages each run opened for this folder: a run that read
`runs.csv` did not answer the question on its own, and is excluded.
