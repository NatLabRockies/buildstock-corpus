"""Derive the graded columns for round 1, arm A (the before-link baseline) -> runs_graded.csv.

`reached_corpus` and `corpus_in_search_results` are computed from the recorded URLs.
`correct` was judged by reading each answer against questions.json on 2026-11-13. Rule:
1 = every fact the question asks for is right; 0.5 = one asked-for fact missing or wrong;
0 = the main facts wrong or not found. A fact the key lists but the question does not ask
for is not required.

Corrected the same day: the first grading took half a point off four answers (Q10 runs 1-3,
Q12 run 2) for omitting facts the key lists but the questions do not ask for (that
timeseries analysis needs more samples; the EIA housing-unit definition). That broke the
rule above, and the Copilot sets were graded by the rule, so those four are now 1 and the
omissions are kept as notes. Every run scores 1: 39 of 39 (first recorded as 37).
"""

import csv
import pathlib

HERE = pathlib.Path(__file__).parent
CORPUS = "buildstock-corpus"
NOT_FULL = {  # (score, note); the notes are omissions of facts the questions do not ask for
    ("Q10", "1"): (1, "not asked, not given: timeseries analysis needs more samples"),
    ("Q10", "2"): (1, "not asked, not given: timeseries analysis needs more samples"),
    ("Q10", "3"): (1, "not asked, not given: timeseries analysis needs more samples"),
    ("Q12", "2"): (1, "not asked, not given: ResStock follows the EIA housing-unit definition"),
}

rows = list(csv.DictReader((HERE / "runs.csv").open(encoding="utf-8")))
out = []
for r in rows:
    if (r["round"], r["arm"]) != ("1", "A"):
        continue
    opened, shown = r["urls_opened"].split(), r["search_result_urls"].split()
    reached = any(CORPUS in u for u in opened)
    score, why = NOT_FULL.get((r["question_id"], r["run"]), (1, ""))
    out.append({
        **{k: r[k] for k in ("round", "arm", "question_id", "run", "model_requested", "reasoning_effort",
                             "searches_total", "opens_total", "tokens_total", "seconds")},
        "reached_corpus": "yes" if reached else "no",
        "corpus_in_search_results": "yes" if any(CORPUS in u for u in shown) else "no",
        "route_to_corpus": "none",
        "fetches_before_corpus": "",
        "correct": score,
        "citation": "publication URL only",
        "grading_note": why,
    })
with (HERE / "runs_graded.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0]))
    w.writeheader()
    w.writerows(out)
total = sum(float(o["correct"]) for o in out)
print(f"{len(out)} runs graded; reached corpus {sum(o['reached_corpus'] == 'yes' for o in out)}; "
      f"corpus in search results {sum(o['corpus_in_search_results'] == 'yes' for o in out)}; "
      f"correct {total} of {len(out)}")
