"""R7.1 done-when: does a fresh agent, starting from the ResStock site, reach the corpus in <= 6 fetches?

Same isolation as measurements/site-link-baseline/run_arm_claude.py (safe mode, new empty folder,
no session saved), but WebFetch is the ONLY tool: no web search, so any route to the corpus
must go through the site. The prompt names the site, never the corpus.
"""
import json, os, subprocess, sys, tempfile, time

sys.path.insert(0, sys.argv[1])  # measurements/site-link-baseline
from run_arm_claude import find_claude

OUT = sys.argv[2]
RUNS = int(sys.argv[3]) if len(sys.argv) > 3 else 3
PROMPT = (
    "The ResStock documentation site is https://natlabrockies.github.io/ResStock.github.io/ . "
    "Starting from that site, answer: in ResStock 2025 Release 1, what fraction of dwelling units "
    "have 3 bedrooms? Give a citation for the figure, precise enough that someone else can check it."
)

claude = find_claude()
os.makedirs(OUT, exist_ok=True)
for run in range(1, RUNS + 1):
    cmd = [claude, "-p", "--output-format", "stream-json", "--verbose", "--model", "sonnet", "--effort", "medium",
           "--safe-mode", "--strict-mcp-config", "--disable-slash-commands", "--no-session-persistence",
           "--tools", "WebFetch", "--allowedTools", "WebFetch", "--permission-prompts", "none"]
    env = {k: v for k, v in os.environ.items() if not k.startswith("CLAUDE_CODE_") and k != "CLAUDECODE"}
    t0 = time.time()
    with tempfile.TemporaryDirectory(prefix="blank_") as empty:
        p = subprocess.run(cmd, input=PROMPT, capture_output=True, text=True, encoding="utf-8", cwd=empty, env=env, timeout=1200)
    log = os.path.join(OUT, f"run{run}.jsonl")
    open(log, "w", encoding="utf-8").write(p.stdout)
    fetches, answer, model = [], "", ""
    for line in p.stdout.splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("type") == "assistant":
            model = model or e["message"].get("model", "")
            for c in e["message"].get("content", []):
                if c.get("type") == "tool_use" and c.get("name") == "WebFetch":
                    fetches.append(c["input"].get("url", ""))
        if e.get("type") == "result":
            answer = e.get("result", "")
    first = next((i + 1 for i, u in enumerate(fetches) if "buildstock-corpus" in u), None)
    print(json.dumps({"run": run, "model": model, "secs": round(time.time() - t0), "exit": p.returncode,
                      "n_fetches": len(fetches), "first_corpus_fetch": first, "fetches": fetches,
                      "answer": answer, "stderr": p.stderr[-400:]}, ensure_ascii=False), flush=True)
