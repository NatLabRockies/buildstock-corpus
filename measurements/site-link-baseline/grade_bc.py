"""Derive the graded columns for round 1, arms B (site only) and C (corpus index.json given),
Codex runner -> runs_bc_graded.csv, and print the B/C/A0 comparison by question type.

`correct` was judged by reading each answer against questions.json on 2026-11-13, one
grader, one read, by the same rule as grade_a0.py: 1 = every fact the question asks for
is right; 0.5 = one asked-for fact missing or wrong; 0 = the main facts wrong or not found.
A fact the key lists but the question does not ask for is not required. Q13 follows
RUN_SHEET.md: a run that fetched the notebook is graded against `expected`, a corpus-arm
run that did not is graded against `expected_corpus_arm`. All six Q13 runs here are graded
against `expected`: the three C runs fetched the notebook (at the release's pinned site
commit), and B is always graded against it.

Everything else is computed from the recorded URLs:
  reached_corpus         any opened URL under buildstock-corpus (in arm C the prompt gives one,
                         so this is yes by construction there);
  read_corpus_document   an opened corpus URL other than index.json: the agent got past the index;
  index_opens            how often index.json was opened (Codex's browser shows the one-line
                         file as "Total lines: 1" and no readable content, so it retries);
  cited_corpus           the answer links a buildstock-corpus URL;
  off_site               arm B only: opened or cited hosts outside the two the prompt allows.
"""

import csv
import pathlib
import statistics as st
import urllib.parse as up

HERE = pathlib.Path(__file__).parent
CORPUS = "buildstock-corpus"
B_HOSTS = {"natlabrockies.github.io", "docs.nlr.gov"}
TYPES = {"routing": ["Q01", "Q02"], "measure_detail": ["Q03", "Q04", "Q05"],
         "guide_lookup": ["Q06", "Q07", "Q08", "Q09"], "site_page": ["Q10", "Q11", "Q12"], "control": ["Q13"]}
QTYPE = {q: t for t, qs in TYPES.items() for q in qs}
NOT_FULL = {  # (arm, question, run) -> (score, note); every other run scores 1
    ("C", "Q05", "1"): (1, "share given as 'about 92%' (key 92.2%); counted as right"),
    ("C", "Q05", "3"): (1, "share given as 'about 92%' (key 92.2%); counted as right"),
    ("B", "Q13", "1"): (0, "declined: the browser could not read the notebook on the site; no facts given"),
    ("B", "Q13", "2"): (0, "declined: the browser could not read the notebook on the site; no facts given"),
    ("B", "Q13", "3"): (0, "declined: the browser could not read the notebook on the site; no facts given"),
}

rows = [r for r in csv.DictReader((HERE / "runs.csv").open(encoding="utf-8")) if r["round"] == "1"]
out = []
for r in rows:
    if r["arm"] not in ("B", "C"):
        continue
    opened = r["urls_opened"].split()
    corpus = [u for u in opened if CORPUS in u]
    hosts = {up.urlparse(u).netloc for u in opened + r["answer_urls"].split()}
    score, why = NOT_FULL.get((r["arm"], r["question_id"], r["run"]), (1, ""))
    out.append({
        **{k: r[k] for k in ("round", "arm", "question_id", "run", "model_requested", "reasoning_effort",
                             "searches_total", "opens_total", "tokens_total", "seconds")},
        "question_type": QTYPE[r["question_id"]],
        "reached_corpus": "yes" if corpus else "no",
        "read_corpus_document": "yes" if any("index.json" not in u for u in corpus) else "no",
        "index_opens": sum("index.json" in u for u in corpus),
        "cited_corpus": "yes" if CORPUS in r["answer_urls"] else "no",
        "off_site": " ".join(sorted(hosts - B_HOSTS)) if r["arm"] == "B" else "",
        "correct": score,
        "grading_note": why,
    })
with (HERE / "runs_bc_graded.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0]))
    w.writeheader()
    w.writerows(out)

a0 = [r for r in rows if r["arm"] == "A"]
print(f"{len(out)} runs graded -> runs_bc_graded.csv\n")
for arm in ("B", "C"):
    g = [o for o in out if o["arm"] == arm]
    print(f"arm {arm}: correct {sum(float(o['correct']) for o in g)} of {len(g)}; "
          f"read a corpus document {sum(o['read_corpus_document'] == 'yes' for o in g)}; "
          f"cited the corpus {sum(o['cited_corpus'] == 'yes' for o in g)}; "
          f"off-site {sum(bool(o['off_site']) for o in g)}; "
          f"tokens {sum(int(o['tokens_total']) for o in g):,}")
print("\nmedian tokens a run by question type   A0       B        C")
for t, qs in TYPES.items():
    med = [st.median(int(r["tokens_total"]) for r in src if r["question_id"] in qs)
           for src in (a0, [o for o in out if o["arm"] == "B"], [o for o in out if o["arm"] == "C"])]
    print(f"  {t:<16}{'':20}" + "".join(f"{m:>9,.0f}" for m in med))
med = [st.median(int(r["tokens_total"]) for r in src)
       for src in (a0, [o for o in out if o["arm"] == "B"], [o for o in out if o["arm"] == "C"])]
print(f"  {'all':<16}{'':20}" + "".join(f"{m:>9,.0f}" for m in med))
