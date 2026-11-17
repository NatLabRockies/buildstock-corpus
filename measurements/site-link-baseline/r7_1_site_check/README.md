# R7.1 done-when check: from the ResStock site to the corpus

Run 2026-11-13, right after ResStock.github.io#102 went live. `site_check.py` runs Claude Code
(`claude -p`, model `sonnet`, served as `claude-sonnet-5-5`, effort `medium`) with the same
isolation as `../run_arm_claude.py` (`--safe-mode`, new empty folder, no session saved), except
that **WebFetch is the only tool**: there is no web search, so any route to the corpus has to go
through the site. The prompt names the site and never the corpus. Three runs; one log each in `logs/`.

Question: in ResStock 2025 Release 1, what fraction of dwelling units have 3 bedrooms, with a citation.
**This question has no published answer**: the guide's Bedrooms entry lists the options and gives no
share. So the runs measure the route, not correctness.

| Run | Fetches | First corpus fetch | Route |
|---|---|---|---|
| 1 | 10 | 4 | home → site `llms.txt` → guide PDF (too large) → `CORPUS_MAP.md` |
| 2 | 9 | 4 | home → guide PDF (too large) → site `llms.txt` → `CORPUS_MAP.md` |
| 3 | 10 | never | home → guide PDF → Data page → README → site pages → `Bedrooms.tsv` in the model repo |

Do not answer questions from these logs; they hold agents' answers.
