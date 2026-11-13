"""Grades for the Claude Code runs of round 1, arm A -> runs_claude_graded.csv.

Each answer was read in full against the answer key on 2026-11-13 by one grader, once; no
second read. Rule, the same as for the other agents: 1 = every fact the question asks for
is present and agrees with the key; 0.5 = one asked-for fact missing or wrong; 0 = the main
facts wrong or not found. A fact the key lists but the question does not ask for is not
required. A right fact stated with a caution ("not confirmed") counts as present.
"""

import csv
import pathlib
import statistics

csv.field_size_limit(10**9)
HERE = pathlib.Path(__file__).parent
CORPUS = "buildstock-corpus"
G = {  # question -> (score, note) for runs 1, 2, 3
    "Q01": [(1, ""), (1, "names report 96413 as the likely one, says not certain"), (1, "")],
    "Q02": [(1, ""), (1, ""), (1, "")],
    "Q03": [(0, "report PDF unreadable; no temperature given"),
            (0, "report PDF unreadable; no temperature given"),
            (0, "report PDF unreadable; mentions 30 F from an older release, unconfirmed")],
    "Q04": [(1, "from search summaries of the report"),
            (0, "240V only confirmed; efficiency and first hour rating not found"),
            (0, "nothing confirmed; 240V only called likely")],
    "Q05": [(1, "92% given as likely"), (0.5, "share given as 97.9%, from a package report"),
            (0, "no cutoff, no target; 92% unconfirmed")],
    "Q06": [(1, "from the latest docs page, not the guide"), (1, "same"), (1, "same")],
    "Q07": [(0, "53% from the latest docs page (key 49%); basements: says the docs do not say"),
            (0.5, "53% (key 49%)"), (0.5, "53% (key 49%)")],
    "Q08": [(0, "by county only; no station rule, no count"),
            (0.5, "county file and nearest-to-population-centroid rule; no station count"),
            (0, "county file inferred; station rule vague; no count")],
    "Q09": [(1, "from the pull request, not the guide"), (1, "same"),
            (1, "same; unsure which season is which but assumes correctly")],
    "Q10": [(1, ""), (1, ""), (1, "")],
    "Q11": [(1, ""), (0, "found no Maine issue"), (1, "")],
    "Q12": [(1, "no tools used; from the model's own knowledge"), (1, "same"), (1, "same")],
    "Q13": [(1, ""), (1, ""), (1, "")],
}
rows = list(csv.DictReader((HERE / "runs_claude.csv").open(encoding="utf-8")))
out = []
for r in rows:
    score, note = G[r["question_id"]][int(r["run"]) - 1]
    fails = [x for x in r["fetch_failures"].split(" | ") if x]
    out.append({
        **{k: r[k] for k in ("round", "arm", "question_id", "run", "tool_version", "model_requested", "model_served",
                             "reasoning_effort", "searches_total", "fetches_total", "tokens_total", "cost_usd", "seconds")},
        "fetch_failures_total": len(fails),
        "reached_corpus": "yes" if CORPUS in r["urls_fetched"] else "no",
        "corpus_in_search_results": "yes" if CORPUS in r["search_result_urls"] else "no",
        "answer_names_corpus": "yes" if CORPUS in r["answer_text"] else "no",
        "correct": score,
        "grading_note": note,
    })
with (HERE / "runs_claude_graded.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0]))
    w.writeheader()
    w.writerows(out)
tok = [int(o["tokens_total"]) for o in out]
print(f"{len(out)} runs; reached corpus {sum(o['reached_corpus'] == 'yes' for o in out)}; "
      f"in search results {sum(o['corpus_in_search_results'] == 'yes' for o in out)}; "
      f"correct {sum(o['correct'] for o in out)} of {len(out)}; "
      f"questions fully right {sum(all(s == 1 for s, _ in v) for v in G.values())} of {len(G)}")
print(f"tokens {sum(tok)} median {int(statistics.median(tok))}; seconds {round(sum(float(o['seconds']) for o in out))}; "
      f"cost {round(sum(float(o['cost_usd']) for o in out), 2)}; fetches {sum(int(o['fetches_total']) for o in out)} "
      f"failed {sum(o['fetch_failures_total'] for o in out)}; searches {sum(int(o['searches_total']) for o in out)}")
for q, v in G.items():
    print(q, sum(s for s, _ in v))
