"""Run the 13 questions of RUNNER.md through the GitHub Copilot CLI.

The same measurement as run_arm_codex.py, for GitHub Copilot: `copilot -p` (prompt mode,
exits after one answer), signed in with the GitHub account that has Copilot. One fresh
session per run, started in a new empty folder, custom instructions off, memory off (the
prompt-mode default), shell and file writes denied. Each run writes one row to
runs_copilot.csv and its whole event stream to logs/.

What Copilot can reach is not what Codex can: as installed (1.0.111) it has a page-fetch
tool and GitHub's own tools (the built-in GitHub MCP server) and **no web search**. So a
run can only open addresses the model already knows or finds through GitHub. The sheet
records each kind of step separately.

Needs this file, RUNNER.md beside it, Python 3.10+ (standard library only) and the Copilot
CLI installed and signed in (run `copilot` once in a terminal).

    python run_arm_copilot.py --dry-run
    python run_arm_copilot.py --round 1 --only Q01 --runs 1
    python run_arm_copilot.py --round 1

Each run uses one Copilot premium request. Re-running skips runs already in the sheet.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time

HERE = pathlib.Path(__file__).parent
FIELDS = [
    "round", "arm", "question_id", "run", "tool", "tool_version", "model_requested", "model_served",
    "reasoning_effort", "date_utc", "exit_code", "fetches_total", "urls_fetched", "fetch_failures",
    "github_calls_total", "github_calls", "other_tools", "answer_text", "answer_urls", "tokens_in",
    "tokens_cache_read", "tokens_cache_write", "tokens_out", "tokens_reasoning", "tokens_total",
    "premium_requests", "seconds", "raw_file", "notes",
]
ARM_SUFFIX = {
    "A": "",
    "B": (" Use only pages and files under natlabrockies.github.io/ResStock.github.io and docs.nlr.gov."
          " Cite the page or report you used."),
}
_URL_RE = re.compile(r"https?://[^\s\"'<>)\]\\]+")


def questions(runner: pathlib.Path) -> dict[str, str]:
    """Question id -> text, read from RUNNER.md so the two can never drift apart."""
    text = runner.read_text(encoding="utf-8")
    body = text.split("## The questions", 1)[1].split("## When you are done", 1)[0]
    out = {}
    for m in re.finditer(r"^### (Q\d+)\s*\n(.*?)(?=^### Q\d+|\Z)", body, re.M | re.S):
        out[m.group(1)] = " ".join(m.group(2).split())
    if not out:
        raise SystemExit(f"no questions found in {runner}")
    return out


def find_copilot() -> str | None:
    """The real copilot.exe. VS Code puts a launcher on PATH; either works once the CLI is installed."""
    return shutil.which("copilot")


def command(copilot: str, prompt: str, model: str, effort: str, usage_file: str) -> list[str]:
    return [
        copilot, "-p", prompt, "--output-format", "json",
        "--no-custom-instructions",  # no AGENTS.md or instruction files, whatever the folder holds
        "--no-auto-update",
        "--model", model, "--reasoning-effort", effort,
        # Prompt mode cannot ask, so every tool is allowed, except the two that could change
        # this machine. Deny rules win over allow-all.
        "--allow-all-tools", "--allow-all-urls", "--deny-tool", "shell", "--deny-tool", "write",
        "--usage-output-file", usage_file,
    ]


def _unique(seq):
    seen, out = set(), []
    for x in seq:
        if x and x not in seen:
            seen.add(x)
            out.append(x)
    return out


def summarize(lines: list[str]) -> dict:
    """Read Copilot's JSON Lines event stream (shape as emitted by Copilot CLI 1.0.111).

    Every tool step is a `tool.execution_start` (toolName, arguments) answered by a
    `tool.execution_complete` (success). `web_fetch` carries the URL; anything else is a
    GitHub tool or another built-in. The answer is the text of the assistant messages.
    """
    fetched, failed, github, other, answer, notes = [], [], [], [], [], []
    by_id, model = {}, ""
    for line in lines:
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        kind, data = ev.get("type", ""), ev.get("data") or {}
        if kind == "tool.execution_start":
            name, args = str(data.get("toolName", "")), data.get("arguments") or {}
            by_id[data.get("toolCallId")] = (name, args)
            if name == "web_fetch":
                fetched.append(str(args.get("url", "")))
            elif "github" in name.lower() or data.get("mcpServerName"):
                github.append(f"{name}({json.dumps(args, sort_keys=True)[:200]})")
            else:
                other.append(name)
        elif kind == "tool.execution_complete" and data.get("success") is False:
            name, args = by_id.get(data.get("toolCallId"), ("?", {}))
            failed.append(f"{name}:{args.get('url') or json.dumps(args)[:120]}")
        elif kind == "assistant.message":
            model = data.get("model") or model
            if data.get("content"):
                answer.append(data["content"])
        elif kind in ("session.error", "error"):
            notes.append(f"{kind}: {json.dumps(data)[:300]}")
    text = "\n\n".join(answer).strip()
    return {
        "model_served": model,
        "fetches_total": len(fetched),
        "urls_fetched": " ".join(fetched),
        "fetch_failures": " | ".join(failed),
        "github_calls_total": len(github),
        "github_calls": " | ".join(github),
        "other_tools": " ".join(_unique(other)),
        "answer_text": text,
        "answer_urls": " ".join(_unique(_URL_RE.findall(text))),
        "notes": "; ".join(notes),
    }


def usage(path: pathlib.Path) -> dict:
    """Token counts from the file Copilot writes at the end of a session."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    t = {"inputTokens": 0, "outputTokens": 0, "cacheReadTokens": 0, "cacheWriteTokens": 0, "reasoningTokens": 0}
    for metrics in (data.get("modelMetrics") or {}).values():
        for key in t:
            t[key] += (metrics.get("usage") or {}).get(key) or 0
    return {
        "tokens_in": t["inputTokens"], "tokens_cache_read": t["cacheReadTokens"],
        "tokens_cache_write": t["cacheWriteTokens"], "tokens_out": t["outputTokens"],
        "tokens_reasoning": t["reasoningTokens"],
        # inputTokens already includes what was read from or written to the cache
        "tokens_total": t["inputTokens"] + t["outputTokens"],
        "premium_requests": data.get("totalPremiumRequestCost", ""),
    }


def done_runs(path: pathlib.Path) -> set[tuple[str, str, str, str, str]]:
    if not path.is_file():
        return set()
    with path.open(encoding="utf-8", newline="") as f:
        return {(r["round"], r["arm"], r["question_id"], r["run"], r["model_requested"]) for r in csv.DictReader(f)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--round", default="1")
    ap.add_argument("--arm", default="A", choices=sorted(ARM_SUFFIX))
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--model", default="claude-sonnet-5.5", help="default: what Copilot CLI 1.0.111 picked unconfigured")
    ap.add_argument("--effort", default="medium", choices=["none", "minimal", "low", "medium", "high", "xhigh", "max"])
    ap.add_argument("--timeout", type=int, default=1200)
    ap.add_argument("--runner", type=pathlib.Path, default=HERE / "RUNNER.md")
    ap.add_argument("--out", type=pathlib.Path, default=HERE / "runs_copilot.csv")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    qs = questions(args.runner)
    wanted = [q for q in qs if not args.only or q in args.only]
    have = done_runs(args.out)
    plan = [(q, r) for q in wanted for r in range(1, args.runs + 1)
            if (args.round, args.arm, q, str(r), args.model) not in have]
    copilot = find_copilot()
    print(f"{len(qs)} questions in {args.runner.name}; {len(plan)} runs to do "
          f"(arm {args.arm}, round {args.round}, model {args.model}, reasoning {args.effort})")
    if args.dry_run:
        for q, r in plan[:2]:
            print(f"  {q} run {r}: {qs[q] + ARM_SUFFIX[args.arm]}")
        print("  command:", " ".join(command(copilot or "copilot", "<question>", args.model, args.effort, "usage.json")))
        print("  Copilot CLI:", copilot or "NOT FOUND on PATH: run `copilot` once in a terminal to install and sign in")
        return 0
    if not copilot:
        raise SystemExit("the Copilot CLI is not on PATH: run `copilot` once in a terminal to install and sign in")
    version = subprocess.run([copilot, "--version"], capture_output=True, text=True).stdout.strip().splitlines()[0]

    log_dir = args.out.parent / "logs"
    log_dir.mkdir(exist_ok=True)
    new_file = not args.out.is_file()
    with args.out.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        for n, (qid, run) in enumerate(plan, 1):
            prompt = qs[qid] + ARM_SUFFIX[args.arm]
            row = dict.fromkeys(FIELDS, "")
            row.update(round=args.round, arm=args.arm, question_id=qid, run=run, tool="copilot -p",
                       tool_version=version, model_requested=args.model, reasoning_effort=args.effort,
                       date_utc=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"))
            started = time.monotonic()
            with tempfile.TemporaryDirectory(prefix="blank_") as empty, \
                    tempfile.TemporaryDirectory(prefix="usage_") as side:
                usage_file = pathlib.Path(side) / "usage.json"
                try:
                    proc = subprocess.run(command(copilot, prompt, args.model, args.effort, str(usage_file)),
                                          capture_output=True, text=True, encoding="utf-8", errors="replace",
                                          cwd=empty, timeout=args.timeout, stdin=subprocess.DEVNULL)
                    out, err, code = proc.stdout, proc.stderr, proc.returncode
                except subprocess.TimeoutExpired as e:
                    out = e.stdout.decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
                    err, code = f"abandoned after {args.timeout}s", "timeout"
                row.update(usage(usage_file))
            tag = "" if args.model == "claude-sonnet-5.5" else "." + re.sub(r"[^A-Za-z0-9.-]+", "-", args.model)
            raw_file = log_dir / f"r{args.round}_{args.arm}_{qid}_{run}.copilot{tag}.jsonl"
            raw_file.write_text(out, encoding="utf-8")
            row.update(summarize(out.splitlines()))
            row.update(exit_code=code, raw_file=raw_file.name, seconds=round(time.monotonic() - started, 1))
            if code != 0:
                row["notes"] = "; ".join(x for x in (row["notes"], f"exit {code}: {err.strip()[-300:]}") if x)
            writer.writerow(row)
            f.flush()
            print(f"  [{n}/{len(plan)}] {qid} run {run}: {row['fetches_total']} fetches, "
                  f"{row['github_calls_total']} GitHub calls, {row['tokens_total']} tokens, {row['seconds']}s "
                  f"{row['notes'][:120]}")
            if code != 0 and not row["answer_text"] and n == 1:
                raise SystemExit(f"the first run produced no answer; fix that before running the rest (see {raw_file.name})")
    print(f"done: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
