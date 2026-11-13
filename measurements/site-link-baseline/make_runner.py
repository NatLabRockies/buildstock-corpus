"""Generate RUNNER.md (the blind brief) from questions.json (the grading key).

questions.json holds the expected answers and names corpus paths. It must NOT go to
anyone running the unprompted arms. This script copies only `id` and `question` out of
it, so the runner file can never drift from the key by hand-editing: regenerate instead.

    uv run --no-sync python -I make_runner.py

Deliberately absent from the output: the word for the thing being measured, the release
and corpus_version metadata, every `expected` / `source` / `trap` / `note` field, and the
run sheet's `reached_corpus` and `route_to_corpus` columns. Those two are derived from
`urls_fetched` during grading; asking a runner to fill them in would reveal the target.
"""

import json
import pathlib

HERE = pathlib.Path(__file__).parent

PREAMBLE = """# Answering 13 ResStock questions — instructions for the runner

Thanks for doing this. We are measuring how much work it takes an AI assistant to answer
real questions about the ResStock building stock model, and how good the answers are. You
do not need to know anything about ResStock, and you should not look anything up yourself.

**Please do not read ahead or research the questions.** Each one goes to the assistant cold.

## Setup

1. A **fresh chat for every question.** Earlier questions give away how to answer later
   ones, so 13 questions means 13 separate chats. Do not reuse a chat, and do not continue
   one after the answer arrives.
2. **No memory, no custom instructions, no project/workspace context, no uploaded files.**
   If the assistant has a memory or personalization feature, turn it off first.
3. **Web search and web fetch ON. Nothing else** — no code execution, no connectors, no
   local files.
4. **Same assistant and same settings for all 13**, and record which. If you can see a
   model version string, write it down exactly. We will ask you to repeat this run in a
   few weeks and it has to be the same model, or the comparison measures the model instead
   of what we are testing.
5. Run each question **3 times** (3 fresh chats), or 5 if you have the patience.

## What to do per chat

Paste the question text **exactly as written below** and add nothing to it — no "please
cite your sources", no extra context, no follow-up questions. Let the assistant finish,
then stop.

## What to record

Copy `runs-template.csv` to `runs.csv` and fill it in — it already has a row for every
question and run, so you only add the cells. Put `1` in the `round` column for this pass
(we will tell you the number for the repeat). The columns that matter most:

- `urls_fetched` — **every URL the assistant opened, in the order it opened them.** This is
  the single most important field. Most assistants show these as links, footnotes or a
  "sources" panel; copy them verbatim, separated by spaces. If you cannot see any URLs,
  write `not_shown`.
- `fetches_total` — how many pages it opened (count the URLs above).
- `answer_text` — paste the assistant's answer, or its key numbers if it is long.
- `citation_given` — what it offered as a source: nothing / a URL / a document name / a
  document name plus version. Verbatim is better than summarised.
- `tokens_in`, `tokens_out`, `tokens_total` — only if the tool reports them. Leave blank
  otherwise; do not estimate.
- `notes` — anything odd: it gave up, it could not open a PDF, it asked you a question, it
  contradicted itself, it took unusually long.

Do **not** grade the answers. Some are subtly wrong in ways that need the source documents
to see, and we have those here. Just record what it said.

If an assistant refuses or errors, record the row with `notes` saying so and run it again
as a new run number.

## The questions

"""

POSTAMBLE = """
## When you are done

Send back `runs.csv` and nothing else is needed. If you kept the chat transcripts, those
are useful too, but the CSV is the deliverable.
"""


def main() -> None:
    data = json.loads((HERE / "questions.json").read_text(encoding="utf-8"))
    questions = data["questions"]

    lines = [PREAMBLE]
    for q in questions:
        lines.append(f"### {q['id']}\n\n{q['question']}\n")
    lines.append(POSTAMBLE)

    out = "\n".join(lines)
    (HERE / "RUNNER.md").write_text(out, encoding="utf-8")

    # Prefilled collection template: one row per question per run, cells left blank.
    # No reached_corpus / route_to_corpus / correct columns — those are derived and
    # graded against the key, not filled in by the runner.
    cols = [
        "round",
        "question_id",
        "run",
        "model",
        "date",
        "fetches_total",
        "urls_fetched",
        "answer_text",
        "citation_given",
        "tokens_in",
        "tokens_out",
        "tokens_total",
        "notes",
    ]
    runs_per_question = 3
    rows = [",".join(cols)]
    for q in questions:
        for run in range(1, runs_per_question + 1):
            row = [""] * len(cols)
            row[cols.index("question_id")] = q["id"]
            row[cols.index("run")] = str(run)
            rows.append(",".join(row))
    (HERE / "runs-template.csv").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(
        f"wrote runs-template.csv: {len(rows) - 1} rows "
        f"({len(questions)} questions x {runs_per_question} runs), {len(cols)} columns"
    )

    # Leak check: nothing identifying the corpus may reach the runner.
    banned = [
        "buildstock-corpus",
        "corpus",
        "raw.githubusercontent",
        "index.json",
        "sections.json",
        "CORPUS_MAP",
        "expected",
        "resstock_amy2018_2025_release_1-v1",
        "osti_pdf",
        "site_page",
    ]
    hits = [w for w in banned if w.lower() in out.lower()]
    print(f"wrote RUNNER.md: {len(questions)} questions, {len(out)} chars")
    print("leak check:", "CLEAN" if not hits else f"LEAKED {hits}")
    if hits:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
