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

Round 1 was run on four agents, 39 runs each, all completed:

| Agent | Tools it had | Reached the corpus | Corpus seen in a result | Correct | Median tokens |
|---|---|---|---|---|---|
| Codex CLI, `gpt-6.1-sol` | web search | 0 | 0 | 39 of 39 | 71,000 |
| Claude Code, `claude-sonnet-5-5` | web search, page fetch | 0 | 2 | 27 of 39 | 165,000 |
| Copilot CLI, `claude-sonnet-5.5` | page fetch, GitHub search; no web search | 2 | 7 | 31 of 39 | 289,000 |
| Copilot CLI, `gemini-4-argon` | page fetch, GitHub search; no web search | 12 | 26 | 37.5 of 39 | 201,000 |

All at reasoning effort `medium`. Web search never surfaced the corpus; GitHub code search
did. Copilot's searches ran signed in as the corpus's owner, which may favour it. Claude
Code's two sightings were pull request pages of this repository in web search results, which
it did not open; its fetch tool could not read the report PDFs or the guide, and that is
where it lost its points.

**A side note, not a fifth agent: Claude Cowork, by hand.** The 13 questions were pasted
once each into new Cowork tasks (Claude Sonnet 5.5) on the same day. It is not comparable to
the four above: one run a question instead of three, the links and tools are the model's own
account and not a log, and it was not a cold start (memory and the user's saved preferences
were on, and show in at least 5 of the 13 answers). What it does show: the corpus appeared
in none of the 13 tasks; and Cowork's fetch tool read the report PDFs and the guide that
Claude Code's could not, scoring 12.5 of 13 on the same model. Token use was not measured.
Files in `cowork/`. Details
are in the R7.0 row of `PLAN-resstock.md`.

## Round 2: after the link, first pass (R7.2)

The ResStock site began linking the corpus on 2026-11-13 (ResStock.github.io#102: `llms.txt`,
a home-page callout, a per-page Markdown link on 27 pages). Round 2 repeats arm A with round 1's
settings. It is run agent by agent; this table grows as each is done.

| Agent | Run | Reached the corpus | Corpus seen in a result | Correct | Median tokens |
|---|---|---|---|---|---|
| Codex CLI, `gpt-6.1-sol` | 2026-11-13, a few hours after the link | 0 (round 1: 0) | 0 (0) | 39 of 39 (39) | 70,000 (71,000) |

Codex, first pass: nothing changed in discovery, as expected this soon. Codex finds pages through
web search, and no search result named the corpus or the site's `llms.txt`; search engines had
not re-indexed the site. Seven runs opened a ResStock site page (16 different pages across those runs, among
them the home page with the callout once and the Maine wall-type page with its footer link three
times) and none went on to the corpus. No run read this folder. Total tokens fell from 5.9 to
4.6 million, almost all of it Q11 (median 937,000 to 412,000), which is run-to-run variation in
how soon the agent found the issue page, not an effect of the link. Two Q13 answers say Arkansas:
they read the notebook after the same site change corrected it. Graded by `grade_a1_codex.py`
into `runs_r2_graded.csv`; logs are `logs/r2_A_*.codex.jsonl`.

The second pass is due about two weeks later, once search engines have re-indexed the site.

## Files

| File | What it is |
|---|---|
| `RUNNER.md` | The 13 questions and the hand-run instructions. The scripts read the questions from it. |
| `RUN_SHEET.md` | The design: the arms (A before and after, B site only, C corpus given) and what to report. |
| `run_arm_codex.py` | The runner used for round 1: OpenAI's Codex CLI, non-interactive, one new session per run. |
| `run_arm_copilot.py` | The runner for GitHub Copilot CLI; `--model` picks the model, one sheet for all. |
| `run_arm_claude.py` | The runner for Claude Code (`claude -p`), on a Claude sign-in with no API key. |
| `run_arm.py` | The same measurement against the Claude API. Written and tested offline; never run. |
| `runs.csv` | Codex: one row per run: searches, search-result URLs, pages opened, the answer, tokens. |
| `runs_copilot.csv` | Copilot: one row per run and model: pages fetched, GitHub calls, the answer, tokens. |
| `grades_copilot.json`, `grade_copilot.py`, `runs_copilot_graded.csv` | The Copilot grades, and the sheet derived from them and the logs. |
| `runs_claude.csv` | Claude Code: one row per run: searches, search-result URLs, pages fetched, the answer, tokens, cost. |
| `grade_claude.py`, `runs_claude_graded.csv` | The Claude Code grades (one grader, one read) and the graded sheet. |
| `logs/` | Each run's complete event log, so every derived column can be recomputed. Copilot's and Claude Code's are gzip-compressed (`.jsonl.gz`); the user folder name in their paths is replaced by `USER`. |
| `cowork/` | The hand-run Cowork side note: `COWORK-RUN.md` (the instructions), `runs_cowork.csv` (the sheet as filled in by hand), `check_cowork.py` and `runs_cowork_checked.csv` (fill-down errors in the model and date columns corrected, one misplaced cell moved, grades added). |
| `grade_a0.py` | Derives `runs_graded.csv`: corpus reach from the recorded URLs, and the correctness grades. |
| `runs_graded.csv` | Round 1 graded. |
| `grade_a1_codex.py`, `runs_r2_graded.csv` | Round 2 (after the link), Codex, graded. |
| `runs-template.csv` | The blank sheet for a hand run. |
| `make_runner.py` | Regenerates `RUNNER.md` from the answer key. |

## Settings to repeat exactly

Codex CLI 0.169.0, model `gpt-6.1-sol`, reasoning effort `medium`, live web search, read-only
sandbox, user configuration ignored, a new empty folder per run. Copilot CLI 1.0.111, models
`claude-sonnet-5.5` and `gemini-4-argon`, reasoning effort `medium`, custom instructions off,
all tools allowed except shell and file writes, a new empty folder per run. Claude Code
2.1.321, model `sonnet` (served as `claude-sonnet-5-5`), effort `medium`, safe mode, web
search and web fetch the only tools, a new empty unsaved session and folder per run:

    python run_arm_codex.py --round 2
    python run_arm_copilot.py --round 2
    python run_arm_copilot.py --round 2 --model gemini-4-argon
    python run_arm_claude.py --round 2 --model sonnet

The round number, model, effort and tool version are written in every row.

## What is not here, and why

- **The answer key (`questions.json`).** It states the expected answer to every question and
  names the corpus paths they come from. It is kept out of this public repository until the
  after-link rounds are finished, so that no run can find the answers here. `make_runner.py`
  needs it; the runners and `grade_a0.py` do not.
- **Arms B and C.** Not run yet.

A later round should check the pages each run opened for this folder: a run that read
`runs.csv` did not answer the question on its own, and is excluded.
