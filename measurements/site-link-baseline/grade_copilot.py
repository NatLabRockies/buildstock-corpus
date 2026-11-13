"""Derive the graded sheet for the Copilot runs of round 1, arm A -> runs_copilot_graded.csv.

Corpus reach is computed from each run's event log: `reached_corpus` when a tool call
named the corpus repository (a GitHub search scoped to it, or a file read from it), and
`corpus_in_tool_results` when the repository only appeared in what a tool returned.
Correctness comes from grades_copilot.json: each answer was read in full against the
answer key on 2026-11-13 by a grader given one written rule, and a sample was re-read.
Rule: 1 = every fact the question asks for is present and agrees with the key; 0.5 = one
asked-for fact missing or wrong; 0 = the main facts wrong or not found. A fact the key
lists but the question does not ask for is not required.
"""

import csv
import gzip
import json
import pathlib

HERE = pathlib.Path(__file__).parent
CORPUS = "buildstock-corpus"

grades = {(g["model"], g["question_id"], str(g["run"])): g
          for g in json.loads((HERE / "grades_copilot.json").read_text(encoding="utf-8"))}
out = []
for r in csv.DictReader((HERE / "runs_copilot.csv").open(encoding="utf-8")):
    if (r["round"], r["arm"]) != ("1", "A"):
        continue
    called, seen, ids = False, False, {}
    for line in gzip.open(HERE / "logs" / r["raw_file"], "rt", encoding="utf-8"):
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        data = ev.get("data") or {}
        if ev.get("type") == "tool.execution_start" and CORPUS in json.dumps(data.get("arguments") or {}):
            called = True
        elif ev.get("type") == "tool.execution_complete" and CORPUS in json.dumps(data.get("result") or {}):
            seen = True
    g = grades[(r["model_requested"], r["question_id"], r["run"])]
    out.append({
        **{k: r[k] for k in ("round", "arm", "question_id", "run", "model_requested", "reasoning_effort",
                             "fetches_total", "github_calls_total", "tokens_total", "seconds")},
        "reached_corpus": "yes" if called else "no",
        "corpus_in_tool_results": "yes" if (seen or called) else "no",
        "route_to_corpus": "GitHub code search" if called else "none",
        "answer_names_corpus": "yes" if CORPUS in r["answer_text"] else "no",
        "correct": g["score"],
        "grade_kind": g["kind"],
        "grading_note": g["reason"],
    })
with (HERE / "runs_copilot_graded.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0]))
    w.writeheader()
    w.writerows(out)
for model in sorted({o["model_requested"] for o in out}):
    rows = [o for o in out if o["model_requested"] == model]
    hit = [o for o in rows if o["reached_corpus"] == "yes"]
    miss = [o for o in rows if o["reached_corpus"] == "no"]
    mean = lambda xs: round(sum(float(x["correct"]) for x in xs) / len(xs), 3) if xs else None
    print(f"{model}: {len(rows)} runs; reached corpus {len(hit)}; in tool results {sum(o['corpus_in_tool_results'] == 'yes' for o in rows)}; "
          f"correct {sum(float(o['correct']) for o in rows)} of {len(rows)}; "
          f"mean score when corpus reached {mean(hit)}, when not {mean(miss)}")
