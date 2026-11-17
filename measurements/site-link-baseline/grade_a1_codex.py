"""Derive the graded columns for round 2, arm A, Codex (the first after-link pass) -> runs_r2_graded.csv.

Round 2 was run on 2026-11-13, a few hours after the ResStock site began linking the corpus
(ResStock.github.io#102), with the settings of round 1. Same columns and the same rule as
grade_a0.py: 1 = every fact the question asks for is right; 0.5 = one asked-for fact missing
or wrong; 0 = the main facts wrong or not found. A fact the key lists but the question does
not ask for is not required. Judged by reading each answer against questions.json, one
grader, one read. Every run scores 1.

Two columns are new: whether the run opened the site's llms.txt, and whether it opened any
ResStock site page that carries a route to the corpus (the home-page callout or a footer link).
"""

import csv
import pathlib

HERE = pathlib.Path(__file__).parent
CORPUS = "buildstock-corpus"
SITE = "natlabrockies.github.io/ResStock.github.io"
NOTES = {  # (score, note)
    ("Q05", "1"): (1, "gives 'approximately 92%' for the key's 92.2%, as round 1 did"),
    ("Q05", "2"): (1, "gives 'about 92%' for the key's 92.2%, as round 1 did"),
    ("Q05", "3"): (1, "gives 'approximately 92%' for the key's 92.2%, as round 1 did"),
    ("Q13", "2"): (1, "says Arkansas: read the notebook after the site fix of 2026-11-13"),
    ("Q13", "3"): (1, "says Arkansas: read the notebook after the site fix of 2026-11-13"),
}

rows = list(csv.DictReader((HERE / "runs.csv").open(encoding="utf-8")))
out = []
for r in rows:
    if (r["round"], r["arm"], r["tool"]) != ("2", "A", "codex exec"):
        continue
    opened, shown = r["urls_opened"].split(), r["search_result_urls"].split()
    reached = any(CORPUS in u for u in opened)
    site_pages = [u for u in opened if SITE in u and u.rstrip("/").endswith((".html", "ResStock.github.io"))]
    score, why = NOTES.get((r["question_id"], r["run"]), (1, ""))
    out.append({
        **{k: r[k] for k in ("round", "arm", "question_id", "run", "model_requested", "reasoning_effort",
                             "searches_total", "opens_total", "tokens_total", "seconds")},
        "reached_corpus": "yes" if reached else "no",
        "corpus_in_search_results": "yes" if any(CORPUS in u for u in shown) else "no",
        "route_to_corpus": "none",
        "fetches_before_corpus": "",
        "opened_site_llms_txt": "yes" if any(SITE + "/llms.txt" in u for u in opened) else "no",
        "site_pages_opened": len(site_pages),
        "read_this_folder": "yes" if any("site-link-baseline" in u for u in opened + shown) else "no",
        "correct": score,
        "citation": "publication URL only",
        "grading_note": why,
    })
with (HERE / "runs_r2_graded.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0]))
    w.writeheader()
    w.writerows(out)
total = sum(float(o["correct"]) for o in out)
print(f"{len(out)} runs graded; reached corpus {sum(o['reached_corpus'] == 'yes' for o in out)}; "
      f"corpus in search results {sum(o['corpus_in_search_results'] == 'yes' for o in out)}; "
      f"opened site llms.txt {sum(o['opened_site_llms_txt'] == 'yes' for o in out)}; "
      f"runs that opened a site page {sum(o['site_pages_opened'] > 0 for o in out)}; "
      f"read this folder {sum(o['read_this_folder'] == 'yes' for o in out)}; "
      f"correct {total} of {len(out)}")
