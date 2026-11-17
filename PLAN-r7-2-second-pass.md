# R7.2 second pass: handoff plan

**Due 2026-11-27**, two weeks after the ResStock site began linking the corpus (2026-11-13).
This file is the whole handoff: a new session with no memory of the earlier work can start
from here. It belongs to step R7.2 of [PLAN-resstock.md](PLAN-resstock.md).

**To pick this up in a new session, say:** *"Read `PLAN-r7-2-second-pass.md` in
buildstock-corpus and start with 'Before any run'. Ask me the open decisions first."*

Written 2026-11-17. If anything below disagrees with the repository, the repository wins;
re-check the "State when this was written" section before acting on it.

## What this measures

Does linking the corpus from the ResStock site change what an AI agent does with a ResStock
question? Thirteen questions about ResStock 2025 Release 1, three runs each, one fresh session
per run, the agent told nothing about the corpus. The questions are in
`measurements/site-link-baseline/RUNNER.md`; the design is in `RUN_SHEET.md`; the folder's
`README.md` holds the results so far.

| Arm | Prompt | What it shows |
|---|---|---|
| A | The question alone | Whether the agent finds the corpus by itself. Before the link is A0, after is A1. |
| B | Question + "use only the ResStock site and docs.nlr.gov" | Cost and correctness from the published documentation alone |
| C | Question + the corpus `index.json` address at the `-v1` tag | Cost and correctness when the corpus is handed over |

## What has been done

### R7.0, the baseline (2026-11-13, before the link). Merged.

Arm A, round 1, four agents, 39 runs each, all at effort `medium`:

| Agent | Tools | Reached the corpus | Corpus seen in a result | Correct | Median tokens |
|---|---|---|---|---|---|
| Codex CLI 0.169.0, `gpt-6.1-sol` | web search | 0 | 0 | 39 of 39 | 71,000 |
| Claude Code 2.1.321, `sonnet` (`claude-sonnet-5-5`) | web search, page fetch | 0 | 2 | 27 of 39 | 165,000 |
| Copilot CLI 1.0.111, `claude-sonnet-5.5` | page fetch, GitHub search; no web search | 2 | 7 | 31 of 39 | 289,000 |
| Copilot CLI 1.0.111, `gemini-4-argon` | page fetch, GitHub search; no web search | 12 | 26 | 37.5 of 39 | 201,000 |

Arms B and C, round 1, **Codex only** (PR #79):

| Arm | Correct | Read a corpus file past `index.json` | Cited the corpus | Median tokens | Tokens in all |
|---|---|---|---|---|---|
| A0, question alone | 39 of 39 | 0 | 0 | 71,000 | 5.9 million |
| B, site only | 36 of 39 | 0 | 0 | 143,000 | 6.5 million |
| C, corpus given | 39 of 39 | 8 | 6 | 302,000 | 13.2 million |

What the baseline taught, in the order it matters for the repeat:

1. **Web search never surfaced the corpus; GitHub code search did.** Copilot's searches ran
   signed in as the corpus's owner, which may favour it; not tested.
2. **Codex answers correctly from the published documents without the corpus.** So no
   correctness gain is expected for Codex; its comparison rests on discovery, cost and citation.
3. **Claude Code cannot read the PDFs** (its fetch tool returns the reports as binary and
   refuses the 15.9 MB guide). Nearly all its lost points are that. Every one of those answers
   is in a corpus file it can fetch: this is the agent where reaching the corpus should raise
   correctness.
4. **Arm C did not measure the corpus.** Codex's browser cannot read the one-line `index.json`
   (85 KB, compact on purpose): it reports "Total lines: 1" and shows nothing. Only 8 of 39 C
   runs read any other corpus file, and C cost about twice B. It measured an unreadable
   starting point, not the upper bound the design meant.
5. **Q13, the control, went the other way from the design.** B scored 0 of 3 (the browser
   cannot read a notebook), C scored 3 of 3 (reached it as raw text through the link the
   corpus records).
6. **Q07 is a real upstream mismatch**: the guide says 49% one-story, the model repository's
   file and the readthedocs page say 53%. The key follows the guide.
7. A hand-run Cowork side note exists (`cowork/`); it is not comparable and is repeated only
   if it can be run cold.

### R7.1, the site link (2026-11-13). Live.

- **NatLabRockies/ResStock.github.io#102, merged `6ecd2103`**: `llms.txt`, `robots.txt`, a
  sitemap, `url:` corrected, a "For AI Assistants and Agents" callout on the home page, a
  "read this page as Markdown" link pinned to `resstock_amy2018_2025_release_1-v1` on 27 pages,
  a schema.org Dataset block, and a weekly sync job that looks only at `resstock_` tags. It also
  fixed the dead README link (`README_resstock_2025_1.pdf`) and the notebook's Arizona/Arkansas
  mix-up.
- **NatLabRockies/ComStock.github.io#216, merged `9da17c6b`**: ComStock's sync job read GitHub's
  "latest release", which had become the ResStock tag; it now takes `comstock_` tags only.
- **Live site checked in a browser the same day.** All of it present and correct.
- **Route check** (`measurements/site-link-baseline/r7_1_site_check/` on branch `r7-site-links`):
  Claude Code with page fetch as its only tool, given the site's address and no mention of the
  corpus, three runs. Two reached the corpus at fetch 4, through the site's `llms.txt` and then
  `CORPUS_MAP.md`. One never opened `llms.txt` and never reached it. The question used (3
  bedrooms) has no published answer, so correctness was not tested. The home-page callout and
  `llms.txt` did the work; no run used a per-page footer link. Both successful runs opened
  `CORPUS_MAP.md` and a whole 169 KB chapter on `main`, not `index.json` and a section file,
  and neither read `AGENTS.md`.

### R7.2 first pass (2026-11-13, a few hours after the link). Codex, arm A only.

Round 2, 39 of 39 runs, round 1's settings (branch `r7-2-pass-1`, PR #78):

| | Round 1 (before) | Round 2 (after) |
|---|---|---|
| Reached the corpus | 0 | 0 |
| Corpus in a search result | 0 | 0 |
| Opened the site's `llms.txt` | 0 | 0 |
| Correct | 39 of 39 | 39 of 39 |
| Median tokens a run | 71,000 | 70,000 |

Nothing changed, as expected that soon: search engines had not re-indexed the site. Seven runs
opened a ResStock site page (16 different pages, the home page with the callout once, the
Maine page with its footer link three times) and none went on to the corpus. Total tokens fell
from 5.9 to 4.6 million, nearly all on Q11; that is run-to-run variation. Two Q13 answers say
Arkansas, so the site fix was already visible. **The other three agents were not run in this
pass (owner's decision); the pass below is their first after the link.**

## State when this was written (2026-11-17). Re-check each line.

| Thing | State |
|---|---|
| `main` | at `4118458f`, PR #79 merged (arms B and C). `runs.csv` on `main` holds round 1 arms A, B, C: 117 rows. |
| PR #77, `r7-site-links` | **Open, conflicts with `main`.** Holds the R7.1 record in `PLAN-resstock.md` and `r7_1_site_check/`. |
| PR #78, `r7-2-pass-1` | **Open, conflicts with `main`.** Holds round 2: 39 rows in `runs.csv`, 39 logs, `grade_a1_codex.py`, `runs_r2_graded.csv`, a README section. |
| Why they conflict | #79 changed the same rows of `PLAN-resstock.md`, appended to `runs.csv` and edited the README. `runs.csv` needs the appended rows of both sides kept; the plan rows need both edits. |
| `PLAN-resstock.md` on `main` | Still says R7.1 "not started" and R7.2 "not started"; #77 corrects R7.1. The R7.2 row has not been written by anyone. |
| Worktrees | `lk-claude-local/bsc-r7-2` (`r7-2-pass-1`), `lk-claude-local/bsc-r7-2-plan` (this file's branch). Remove each once its PR merges. |
| Answer key | `.scratch/site-link-baseline/questions.json` in the main checkout. Gitignored, never committed until the last round is graded: the repository is public. |
| Reminder | Scheduled task `r7-2-second-pass-reminder`, one-time, 2026-11-27 09:00 Mountain. It alerts and asks; it runs nothing. |

## The work

### Before any run

1. **Get #77 and #78 merged**, resolving the conflicts as described above, so `main` holds
   rounds 1 and 2 and the R7.1 record. Do this first: every later step appends to `runs.csv`.
2. **Work in a new worktree on a new branch off `main`** (suggested `r7-2-pass-2`). Other
   sessions use the main checkout; on 2026-11-13 a commit landed on another session's branch
   because that session had switched the shared folder.
3. **Check each tool's version** against the table above (`codex --version`, `copilot --version`,
   `claude --version`). A changed version is a changed instrument: tell the owner before
   running, and record it. The model names must match too.
4. **Look at the live site** in the browser (`curl` to `natlabrockies.github.io` fails on this
   machine) to confirm the callout, `llms.txt` and footer links are still there.
5. **See whether search engines now know the corpus**: search for a distinctive phrase from the
   site's `llms.txt` and for `buildstock-corpus ResStock`. Record what comes back, with the date.
   If nothing does, the Codex and Claude Code A runs will most likely repeat round 2.
6. **Settle the open decisions** at the end of this file with the owner.

### The runs

All from `measurements/site-link-baseline/` in the new worktree. **Use `--round 3` everywhere**:
round 2 is the first after-link pass, round 3 is this one. Re-running a command resumes; runs
already recorded are skipped.

| # | Arm | Agent | Command | About | Compare with |
|---|---|---|---|---|---|
| 1 | A | Codex | `python run_arm_codex.py --round 3` | 16 min | rounds 1 and 2 |
| 2 | A | Claude Code | `python run_arm_claude.py --round 3 --model sonnet` | 30 min | round 1 |
| 3 | A | Copilot, Claude | `python run_arm_copilot.py --round 3` | 90 min, 39 premium requests | round 1 |
| 4 | A | Copilot, Gemini | `python run_arm_copilot.py --round 3 --model gemini-4-argon` | 95 min, 39 premium requests | round 1 |
| 5 | B | Codex | `python run_arm_codex.py --round 3 --arm B` | 20 min | round 1 arm B |
| 6 | C | Codex | `python run_arm_codex.py --round 3 --arm C` | 40 min | round 1 arm C |

Run one question first on each (`--only Q01 --runs 1`) and read the row before the rest.

**Arms B and C are included at the owner's request (2026-11-17).** Two things to know:

- **Arm B is not the same after the link.** The site now carries the callout and the footer
  links, but B's rule keeps the agent on the site and `docs.nlr.gov`, so it cannot follow them
  to the corpus (`raw.githubusercontent.com`). A changed B result would show the agent reading
  different site pages, not the corpus. Record whether any B run tries to leave for the corpus
  and is held back by the rule.
- **Arm C as built starts from a file Codex cannot read.** Repeating it unchanged gives a
  comparable number and the same flaw. See open decision 1.

Codex setup on this machine: the CLI is in the conda environment `codex`
(`AppData/Local/anaconda3/envs/codex`); put that folder on `PATH` and unset `SSL_CERT_FILE`
(the network inspects TLS and conda's certificate list lacks the organization's root).
`codex login status` should say "Logged in using ChatGPT".

### Grading and deriving

- **Rule, the same for every set:** 1 = every fact the question asks for is right; 0.5 = one
  asked-for fact missing or wrong; 0 = the main facts wrong or not found. A fact the key lists
  that the question does not ask for is not required. Q13 follows `RUN_SHEET.md`.
- Read every answer against `questions.json`. Model each grading script on the one for the
  same agent: `grade_a1_codex.py` (on #78) for Codex arm A, `grade_bc.py` for arms B and C,
  `grade_claude.py`, `grade_copilot.py` with `grades_copilot.json`.
- **Derive from the logs, not from the answer text:** reached the corpus (a corpus URL opened),
  corpus in a search or tool result, the route (site `llms.txt`, home-page callout, a per-page
  link, web search, GitHub search), fetches before the corpus, and whether a tag or `main` was
  read.
- **Exclude any run that opened `measurements/site-link-baseline/`** in this repository: it
  holds earlier answers. Count them and say so.
- Say for each set how it was graded (one grader, one read, or a second check).

### The report

The R7.2 row of `PLAN-resstock.md`, the folder's README, and a short write-up for colleagues
if the owner wants one (the round 1 summaries are Word files in
`.scratch/site-link-baseline/`). It should answer:

1. **Discovery**: runs that reached the corpus, round 3 minus round 1, per agent, split by
   route, so it is clear whether `llms.txt`, the callout, the per-page links or search did it.
2. **Cost**: tokens A before against A after, and B against C, by question type (measure
   report, guide, site page, the Q13 control), not one overall number.
3. **Correctness and citation** on the same splits. A token saving with fewer right answers is
   not a saving. Watch Claude Code's PDF questions (Q03, Q04, Q05, Q07, Q08).
4. **What an agent reads once it is in the corpus**: `index.json` and a section file as
   `AGENTS.md` asks, or `CORPUS_MAP.md` and whole chapters as the route check saw.
5. What was not measured, and what changed in the instrument (tool versions, search index).

### Done when

Round 3 recorded for arm A on all four agents and for arms B and C on Codex; every set graded
by the rule; the comparison written into `PLAN-resstock.md` and the README; the answer key
committed if the owner agrees no further round is coming; PRs merged; worktrees removed.

## Open decisions for the owner

1. **Arm C's starting point.** (a) Repeat it unchanged from `index.json`: comparable with round
   1, and known to be unreadable for Codex. (b) Add a second corpus arm that starts from a
   readable file, `CORPUS_MAP.md` or the corpus `llms.txt`, so the corpus's real cost is
   measured. (c) Both. Recommended: (c), with the new arm named separately (for example C2) so
   round 1's C stays comparable.
2. **Arms B and C on the other agents.** Round 1 ran them on Codex only. Claude Code is the
   agent the corpus should help most, so C on Claude Code (about 30 minutes) is the most
   informative addition; Copilot would cost 78 premium requests per arm and model.
3. **A cold site-only route check with one of the 13 questions**, replacing the 3-bedroom
   question that had no answer.
4. **Whether to act on what the route check saw** before the pass: agents take `CORPUS_MAP.md`
   and whole chapters from the site's `llms.txt` rather than `index.json` and section files.
   Changing the site's `llms.txt` now would change the thing being measured; recommended: leave
   it until this pass is recorded.
5. **Committing the answer key** once this pass is graded.

## Things that will trip you up on this machine

- **Bare commands do not resolve in PowerShell**: `PATHEXT` is stripped. In Git Bash, start
  with `export PATHEXT=".COM;.EXE;.BAT;.CMD"`.
- **Python's console is cp1252.** Printing an answer with `≥` or `≈` dies. Use `python -X utf8`
  and write to a file, or encode with `errors="replace"`.
- **Logs carry the Windows user name in paths.** Replace it before committing, as the Copilot
  and Claude Code logs already do (`USER`), and check for email addresses.
- **`runs.csv` is appended by every runner.** Two branches that both ran something will
  conflict there; keep both sets of rows.
- **A background command is cut off at ten minutes.** Long batches: run in the background and
  re-run to resume, or use the terminal.
- **Do not run `bsc fetch`**, and do not edit anything under `processed/` (see `AGENTS.md`).
  Nothing in this step touches the corpus itself.
- **The owner's working rules**: one step at a time, ask before starting; recommend a branch
  and wait for a yes; merge commits; tags never move; no files on OneDrive.
