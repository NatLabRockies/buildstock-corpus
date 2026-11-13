"""Write a corrected, graded copy of the hand-filled Cowork sheet. The original is left as it is."""
import csv, pathlib, statistics, sys

csv.field_size_limit(10**9)
d = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).parent
rows = list(csv.DictReader((d / "runs_cowork.csv").read_bytes().decode("cp1252").splitlines(keepends=True)))
G = {
    "Q01": (1, ""), "Q02": (1, ""), "Q03": (1, "35 F, from the report PDF"), "Q04": (1, ""),
    "Q05": (1, "from two package reports; the standalone report was refused by the fetch allowlist"),
    "Q06": (1, "from the guide"),
    "Q07": (0.5, "gives both 49% (guide) and 53% (online docs), reports the conflict, leans to 53%; key is 49%"),
    "Q08": (1, "1,200 stations and the county rule, from the guide"), "Q09": (1, "from the guide"),
    "Q10": (1, ""), "Q11": (1, ""), "Q12": (1, ""), "Q13": (1, ""),
}
for r in rows:
    r["model"] = "sonnet 5.5"          # the sheet counted up from 5.5 to 5.16: a spreadsheet fill-down
    r["date"] = "2026-11-13"           # likewise 11/13 to 11/24; the notes' timestamps are all 13 November
    if r["minutes"].strip() and not r["notes"].strip():
        r["notes"], r["minutes"] = r["minutes"], ""   # Q02: the notes were pasted one column to the left
    # Reported by the model inside the task when asked, not read from a usage meter: an estimate only.
    r["tokens_model_estimate_unverified"] = r.pop("tokens").replace(",", "").strip()
    r["correct"], r["grading_note"] = G[r["question_id"]]
    text = r["answer_text"] + r["urls_opened"] + r["notes"] + r["tools_seen"]
    r["corpus_mentioned"] = "yes" if "buildstock-corpus" in text else "no"
    r["personal_context_visible"] = "yes" if any(w in text for w in ("your preference", "you prefer", "product owner", "Stored context")) else "no"
with (d / "runs_cowork_checked.csv").open("w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
tok = [int(r["tokens_model_estimate_unverified"]) for r in rows]
print("score", sum(r["correct"] for r in rows), "of", len(rows), "| tokens total", sum(tok), "median", int(statistics.median(tok)),
      "| corpus mentioned", sum(r["corpus_mentioned"] == "yes" for r in rows),
      "| personal context visible in", [r["question_id"] for r in rows if r["personal_context_visible"] == "yes"])
