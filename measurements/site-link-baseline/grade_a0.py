"""Derive the graded columns for round 1, arm A (the before-link baseline) -> runs_graded.csv.

`reached_corpus` and `corpus_in_search_results` are computed from the recorded URLs.
`correct` was judged by reading each answer against questions.json on 2026-11-13 and is
entered below; every run not listed scored 1. Rule: 1 = every fact the question asks for is
right; 0.5 = right as far as it goes, one asked-for fact missing. An upgrade number the key
lists but the question did not ask for (Q03, Q04, Q05) is not required.
"""

import csv
import pathlib

HERE = pathlib.Path(__file__).parent
CORPUS = "buildstock-corpus"
NOT_FULL = {
    ("Q10", "1"): (0.5, "gives 1,000 or more; does not say timeseries analysis needs more samples"),
    ("Q10", "2"): (0.5, "gives 1,000 or more; does not say timeseries analysis needs more samples"),
    ("Q10", "3"): (0.5, "gives 1,000 or more; does not say timeseries analysis needs more samples"),
    ("Q12", "2"): (0.5, "inclusions right; does not say ResStock follows the EIA housing-unit definition"),
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
