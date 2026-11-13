"""Run the 13 questions of RUNNER.md through Claude Code, signed in with a Claude account.

The same measurement as run_arm_codex.py and run_arm_copilot.py, for Claude: `claude -p`
(print mode, exits after one answer) uses the sign-in saved by `claude` + `/login`, so a
Claude subscription is enough and no API key is needed. One fresh, unsaved session per run,
started in a new empty folder, with every customization off (instruction files, memory,
skills, plugins, hooks, connectors) and web search and web fetch the only tools. Each run
writes one row to runs_claude.csv and its whole event stream to logs/.

Needs this file, RUNNER.md beside it, Python 3.10+ (standard library only) and Claude Code
installed and signed in (run `claude` once in a terminal and type /login).

    python run_arm_claude.py --dry-run
    python run_arm_claude.py --model MODEL --only Q01 --runs 1
    python run_arm_claude.py --model MODEL

Re-running skips runs already in the sheet, so an interrupted pass can be resumed.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import glob
import gzip
import json
import os
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
    "reasoning_effort", "date_utc", "exit_code", "searches_total", "search_queries", "search_result_urls",
    "fetches_total", "urls_fetched", "fetch_failures", "other_tools", "tools_offered", "answer_text",
    "answer_urls", "tokens_in", "tokens_cache_read", "tokens_cache_write", "tokens_out", "tokens_total",
    "turns", "cost_usd", "seconds", "raw_file", "notes",
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


def find_claude() -> str | None:
    """`claude` on PATH, or the copy the Claude desktop app keeps for itself on Windows."""
    found = shutil.which("claude")
    if found:
        return found
    local = os.environ.get("LOCALAPPDATA")
    if local:
        bundled = sorted(glob.glob(os.path.join(local, "Claude-Data", "*", "claude-code", "*", "*", "claude.exe")))
        if bundled:
            return bundled[-1]
    return None


def command(claude: str, model: str, effort: str) -> list[str]:
    return [
        claude, "-p", "--output-format", "stream-json", "--verbose",
        "--model", model, "--effort", effort,
        # Everything a person may have set up is off: CLAUDE.md, memory, skills, plugins, hooks,
        # connectors, custom agents. Sign-in and the built-in tools are unaffected.
        "--safe-mode", "--strict-mcp-config", "--disable-slash-commands", "--no-session-persistence",
        # The two web tools are the only tools that exist in the session, and both are pre-approved.
        "--tools", "WebSearch,WebFetch", "--allowedTools", "WebSearch,WebFetch",
        # Print mode cannot ask; anything else that would prompt is refused.
        "--permission-prompts", "none",
    ]


def _unique(seq):
    seen, out = set(), []
    for x in seq:
        if x and x not in seen:
            seen.add(x)
            out.append(x)
    return out


def _text(content) -> str:
    """A tool result's content as text, whether it arrived as a string or as blocks."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(b.get("text", "") if isinstance(b, dict) else str(b) for b in content)
    return "" if content is None else json.dumps(content)


def summarize(lines: list[str]) -> dict:
    """Read Claude Code's stream-json events (shape as emitted by Claude Code 2.1.321).

    `system`/init names the model and the tools on offer. Each `assistant` event carries
    message content blocks: `text`, or `tool_use` (name, input). Each `user` event carries the
    matching `tool_result` (is_error, content). The last event, `result`, has the final
    answer, the turn count, the token usage and the cost.
    """
    queries, results, fetched, failed, other, texts, notes = [], [], [], [], [], [], []
    by_id, model, offered, final = {}, "", "", {}
    for line in lines:
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        kind = ev.get("type", "")
        if kind == "system" and ev.get("subtype") == "init":
            model = ev.get("model") or model
            offered = " ".join(ev.get("tools") or [])
            if ev.get("mcp_servers"):
                notes.append(f"connectors present: {json.dumps(ev['mcp_servers'])[:200]}")
        elif kind == "assistant":
            msg = ev.get("message") or {}
            if not ev.get("parent_tool_use_id"):
                model = msg.get("model") or model
            for block in msg.get("content") or []:
                if block.get("type") == "text" and block.get("text") and not ev.get("parent_tool_use_id"):
                    texts.append(block["text"])
                elif block.get("type") == "tool_use":
                    name, args = block.get("name", ""), block.get("input") or {}
                    by_id[block.get("id")] = (name, args)
                    if name == "WebSearch":
                        queries.append(str(args.get("query", "")))
                    elif name == "WebFetch":
                        fetched.append(str(args.get("url", "")))
                    else:
                        other.append(name)
        elif kind == "user":
            content = (ev.get("message") or {}).get("content")
            for block in content if isinstance(content, list) else []:
                if not isinstance(block, dict) or block.get("type") != "tool_result":
                    continue
                name, args = by_id.get(block.get("tool_use_id"), ("?", {}))
                if block.get("is_error"):
                    failed.append(f"{name}:{args.get('url') or args.get('query') or ''}")
                elif name == "WebSearch":
                    results.extend(_URL_RE.findall(_text(block.get("content"))))
        elif kind == "result":
            final = ev
    if final.get("is_error"):
        notes.append(f"result error: {str(final.get('result') or final.get('subtype'))[:300]}")
    # The final answer is the last stretch of text; `result` holds it when the run ended normally.
    answer = (final.get("result") if isinstance(final.get("result"), str) and not final.get("is_error") else "") \
        or "\n\n".join(texts)
    t = {"in": 0, "read": 0, "write": 0, "out": 0}
    per_model = final.get("modelUsage") or {}
    if per_model:  # includes the small model WebFetch uses to read pages, which `usage` leaves out
        for u in per_model.values():
            t["in"] += u.get("inputTokens") or 0
            t["read"] += u.get("cacheReadInputTokens") or 0
            t["write"] += u.get("cacheCreationInputTokens") or 0
            t["out"] += u.get("outputTokens") or 0
    else:
        u = final.get("usage") or {}
        t = {"in": u.get("input_tokens") or 0, "read": u.get("cache_read_input_tokens") or 0,
             "write": u.get("cache_creation_input_tokens") or 0, "out": u.get("output_tokens") or 0}
    return {
        "model_served": " ".join(per_model) or model,
        "searches_total": len(queries),
        "search_queries": " | ".join(queries),
        "search_result_urls": " ".join(_unique(results)),
        "fetches_total": len(fetched),
        "urls_fetched": " ".join(fetched),
        "fetch_failures": " | ".join(failed),
        "other_tools": " ".join(_unique(other)),
        "tools_offered": offered,
        "answer_text": answer.strip(),
        "answer_urls": " ".join(_unique(_URL_RE.findall(answer))),
        # Claude counts cached input apart from fresh input, so the total is the sum of all four.
        "tokens_in": t["in"], "tokens_cache_read": t["read"], "tokens_cache_write": t["write"],
        "tokens_out": t["out"], "tokens_total": sum(t.values()) if final else "",
        "turns": final.get("num_turns", ""),
        "cost_usd": final.get("total_cost_usd", ""),
        "notes": "; ".join(notes),
    }


def done_runs(path: pathlib.Path) -> set[tuple[str, str, str, str, str]]:
    if not path.is_file():
        return set()
    with path.open(encoding="utf-8", newline="") as f:
        return {(r["round"], r["arm"], r["question_id"], r["run"], r["model_requested"]) for r in csv.DictReader(f)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--round", default="1", help="1 for the first pass; the number you are given for a repeat")
    ap.add_argument("--arm", default="A", choices=sorted(ARM_SUFFIX), help="A: question alone (default). B: site only")
    ap.add_argument("--runs", type=int, default=3, help="runs per question (default 3)")
    ap.add_argument("--only", nargs="*", help="question ids to run, e.g. Q01 Q07 (default: all)")
    ap.add_argument("--model", default="sonnet", help="a full model name, or an alias such as sonnet or opus (default sonnet)")
    ap.add_argument("--effort", default="medium", choices=["low", "medium", "high", "xhigh", "max"])
    ap.add_argument("--timeout", type=int, default=1200, help="seconds before a run is abandoned (default 1200)")
    ap.add_argument("--runner", type=pathlib.Path, default=HERE / "RUNNER.md")
    ap.add_argument("--out", type=pathlib.Path, default=HERE / "runs_claude.csv")
    ap.add_argument("--dry-run", action="store_true", help="print the plan and the command; start nothing")
    args = ap.parse_args()

    qs = questions(args.runner)
    wanted = [q for q in qs if not args.only or q in args.only]
    have = done_runs(args.out)
    plan = [(q, r) for q in wanted for r in range(1, args.runs + 1)
            if (args.round, args.arm, q, str(r), args.model) not in have]
    claude = find_claude()
    print(f"{len(qs)} questions in {args.runner.name}; {len(plan)} runs to do "
          f"(arm {args.arm}, round {args.round}, model {args.model}, effort {args.effort})")
    if args.dry_run:
        for q, r in plan[:2]:
            print(f"  {q} run {r}: {qs[q] + ARM_SUFFIX[args.arm]}")
        print("  command:", " ".join(command(claude or "claude", args.model, args.effort)),
              " (question on stdin, in a new empty folder)")
        print("  Claude Code:", claude or "NOT FOUND: install it, then run `claude` once and type /login")
        return 0
    if not claude:
        raise SystemExit("Claude Code was not found: install it, then run `claude` once and type /login")
    version = subprocess.run([claude, "--version"], capture_output=True, text=True).stdout.strip().splitlines()[0]

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
            row.update(round=args.round, arm=args.arm, question_id=qid, run=run, tool="claude -p",
                       tool_version=version, model_requested=args.model, reasoning_effort=args.effort,
                       date_utc=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"))
            started = time.monotonic()
            with tempfile.TemporaryDirectory(prefix="blank_") as empty:
                try:
                    proc = subprocess.run(command(claude, args.model, args.effort), input=prompt,
                                          capture_output=True, text=True, encoding="utf-8", errors="replace",
                                          cwd=empty, timeout=args.timeout)
                    out, err, code = proc.stdout, proc.stderr, proc.returncode
                except subprocess.TimeoutExpired as e:
                    out = e.stdout.decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
                    err, code = f"abandoned after {args.timeout}s", "timeout"
            tag = re.sub(r"[^A-Za-z0-9.-]+", "-", args.model)
            raw_file = log_dir / f"r{args.round}_{args.arm}_{qid}_{run}.claude.{tag}.jsonl.gz"
            with gzip.open(raw_file, "wt", encoding="utf-8") as z:
                z.write(out)
            row.update(summarize(out.splitlines()))
            row.update(exit_code=code, raw_file=raw_file.name, seconds=round(time.monotonic() - started, 1))
            if code != 0:
                tail = (err.strip() or out.strip())[-300:]
                row["notes"] = "; ".join(x for x in (row["notes"], f"exit {code}: {tail}") if x)
            broken = code != 0 or not row["answer_text"] or "result error" in row["notes"]
            if broken and n == 1:
                # Not recorded, so the same command starts from this run again once it is fixed.
                raise SystemExit(f"the first run failed, nothing was recorded: {row['notes'][:300]}\n"
                                 f"(full output in logs/{raw_file.name}; if it says you are not logged in, "
                                 f"run `claude` in a terminal and type /login)")
            writer.writerow(row)
            f.flush()
            print(f"  [{n}/{len(plan)}] {qid} run {run}: {row['searches_total']} searches, "
                  f"{row['fetches_total']} fetches, {row['tokens_total']} tokens, {row['seconds']}s "
                  f"{row['notes'][:160]}")
    print(f"done: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
