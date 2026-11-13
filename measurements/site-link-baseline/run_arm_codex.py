"""Run the 13 questions of RUNNER.md through the Codex CLI, signed in with a ChatGPT account.

The same measurement as run_arm.py, for an OpenAI model and with no API key: Codex's
non-interactive mode (`codex exec`) uses the login saved by `codex login`, so a ChatGPT
subscription is enough. One fresh, unsaved Codex session per run, started in a new empty
folder (so no AGENTS.md or project file can tell it anything), with the user's Codex
configuration ignored and live web search on. Each run writes one row to runs.csv and its
whole event stream to raw/, so anything else can be derived later without re-running.

Needs this file, RUNNER.md beside it, Python 3.10+ (standard library only) and the Codex
CLI, installed and signed in once:

    npm install -g @openai/codex
    codex login

Then:

    python run_arm_codex.py --dry-run                      # show what would run; starts nothing
    python run_arm_codex.py --round 1 --only Q01 --runs 1  # one real run, to check it works
    python run_arm_codex.py --round 1                      # all 13 questions x 3 runs

Re-running skips runs already in runs.csv, so an interrupted pass can be resumed. Use the
same --model for the repeat pass; it is recorded in every row with the Codex version.
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
    "round", "arm", "question_id", "run", "tool", "tool_version", "model_requested", "reasoning_effort",
    "date_utc", "exit_code", "searches_total", "search_queries", "search_result_urls", "opens_total",
    "urls_opened", "commands_run", "answer_text", "answer_urls", "tokens_in", "tokens_cached_in",
    "tokens_out", "tokens_reasoning", "tokens_total", "seconds", "raw_file", "notes",
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


def command(codex: str, model: str, effort: str) -> list[str]:
    """The Codex invocation. The prompt is piped on stdin ('-'), never put on the command line."""
    # Live web search: `--search` is a flag of the interactive `codex` only (0.169.0 rejects it
    # on `exec`); the setting it stands for is web_search = "live".
    cmd = [codex, "exec", "--json", "-c", 'web_search="live"', "--ephemeral", "--ignore-user-config",
           "--ignore-rules", "--skip-git-repo-check", "--sandbox", "read-only",
           # Both are stated, never left to a default: with the user's configuration ignored,
           # Codex 0.169.0 ran gpt-6.1-sol with reasoning effort "none", and a default can move.
           "--model", model, "-c", f'model_reasoning_effort="{effort}"']
    return cmd + ["-"]


def child_env() -> dict[str, str]:
    """The environment Codex runs in.

    Activating a conda environment sets SSL_CERT_FILE to conda's own public certificate
    list, and Codex uses that variable when CODEX_CA_CERTIFICATE is unset. On a network
    that inspects TLS with an organization's own root certificate, that list does not
    contain it and every request fails (seen at login on 2026-11-13: token_exchange_failed).
    Without the variable Codex trusts what the operating system trusts. So it is dropped
    for Codex, unless CODEX_CA_CERTIFICATE says which bundle to use.
    """
    import os

    env = dict(os.environ)
    if not env.get("CODEX_CA_CERTIFICATE") and env.pop("SSL_CERT_FILE", None):
        print("  note: SSL_CERT_FILE is not passed to Codex (set CODEX_CA_CERTIFICATE to choose a bundle)")
    return env


def _unique(seq):
    seen, out = set(), []
    for x in seq:
        if x and x not in seen:
            seen.add(x)
            out.append(x)
    return out


def summarize(lines: list[str]) -> dict:
    """Read Codex's JSON Lines event stream (shape as emitted by Codex 0.169.0).

    A `web_search` item is one of two things, told apart by `action.type`:
      * "search": a query was run; `results` are the search results (ref_id `turnNsearchM`);
      * anything else: a page was opened; `results` name the page (ref_id `turnNviewM`).
    So the pages a run actually opened are separate from the URLs it was merely shown. The
    raw stream is kept beside the sheet for anything this misses.
    """
    queries, result_urls, opened, commands, answer, notes = [], [], [], [], [], []
    usage = {"input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0, "reasoning_output_tokens": 0}
    for line in lines:
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        kind = ev.get("type", "")
        if kind == "turn.completed":
            for key in usage:
                usage[key] += (ev.get("usage") or {}).get(key) or 0
        elif kind in ("turn.failed", "error"):
            notes.append(f"{kind}: {json.dumps(ev.get('error') or ev.get('message') or ev)[:300]}")
        elif kind == "item.completed":
            item = ev.get("item") or {}
            itype = str(item.get("type", ""))
            if itype == "agent_message":
                answer.append(item.get("text", ""))
            elif itype == "web_search":
                action = item.get("action") if isinstance(item.get("action"), dict) else {}
                urls = [r.get("url", "") for r in item.get("results") or [] if isinstance(r, dict)]
                if action.get("type") == "search":
                    queries.append(str(action.get("query") or item.get("query") or ""))
                    result_urls += urls
                else:
                    opened += urls or _URL_RE.findall(json.dumps(action))
            elif itype == "command_execution":
                commands.append(str(item.get("command", "")))
                opened += _URL_RE.findall(str(item.get("command", "")))
    text = "\n\n".join(a for a in answer if a).strip()
    return {
        "searches_total": len(queries),
        "search_queries": " | ".join(queries),
        "search_result_urls": " ".join(_unique(result_urls)),
        "opens_total": len([u for u in opened if u]),
        "urls_opened": " ".join(u for u in opened if u),
        "commands_run": " | ".join(commands),
        "answer_text": text,
        "answer_urls": " ".join(_unique(_URL_RE.findall(text))),
        "tokens_in": usage["input_tokens"],
        "tokens_cached_in": usage["cached_input_tokens"],
        "tokens_out": usage["output_tokens"],
        "tokens_reasoning": usage["reasoning_output_tokens"],
        "tokens_total": usage["input_tokens"] + usage["output_tokens"],
        "notes": "; ".join(notes),
    }


def done_runs(path: pathlib.Path) -> set[tuple[str, str, str, str]]:
    if not path.is_file():
        return set()
    with path.open(encoding="utf-8", newline="") as f:
        return {(r["round"], r["arm"], r["question_id"], r["run"]) for r in csv.DictReader(f)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--round", default="1", help="1 for the first pass; the number you are given for a repeat")
    ap.add_argument("--arm", default="A", choices=sorted(ARM_SUFFIX), help="A: question alone (default). B: site only")
    ap.add_argument("--runs", type=int, default=3, help="runs per question (default 3)")
    ap.add_argument("--only", nargs="*", help="question ids to run, e.g. Q01 Q07 (default: all)")
    ap.add_argument("--model", default="gpt-6.1-sol", help="Codex model (default gpt-6.1-sol, what Codex 0.169.0 picked unconfigured)")
    ap.add_argument("--effort", default="medium", choices=["none", "minimal", "low", "medium", "high", "xhigh"],
                    help="reasoning effort (default medium)")
    ap.add_argument("--timeout", type=int, default=1200, help="seconds before a run is abandoned (default 1200)")
    ap.add_argument("--runner", type=pathlib.Path, default=HERE / "RUNNER.md")
    ap.add_argument("--out", type=pathlib.Path, default=HERE / "runs.csv")
    ap.add_argument("--dry-run", action="store_true", help="print the plan and the command; start nothing")
    args = ap.parse_args()

    qs = questions(args.runner)
    wanted = [q for q in qs if not args.only or q in args.only]
    have = done_runs(args.out)
    plan = [(q, r) for q in wanted for r in range(1, args.runs + 1)
            if (args.round, args.arm, q, str(r)) not in have]
    codex = shutil.which("codex")
    print(f"{len(qs)} questions in {args.runner.name}; {len(plan)} runs to do "
          f"(arm {args.arm}, round {args.round}, model {args.model}, reasoning {args.effort})")
    if args.dry_run:
        for q, r in plan[:3]:
            print(f"  {q} run {r}: {qs[q] + ARM_SUFFIX[args.arm]}")
        print("  command:", " ".join(command(codex or "codex", args.model, args.effort)), " (prompt on stdin, in a new empty folder)")
        print("  Codex CLI:", codex or "NOT FOUND on PATH: npm install -g @openai/codex, then codex login")
        return 0
    if not codex:
        raise SystemExit("the Codex CLI is not on PATH: npm install -g @openai/codex, then codex login")
    env = child_env()
    version = subprocess.run([codex, "--version"], capture_output=True, text=True, env=env).stdout.strip()

    raw_dir = args.out.parent / "raw"
    raw_dir.mkdir(exist_ok=True)
    new_file = not args.out.is_file()
    with args.out.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        for n, (qid, run) in enumerate(plan, 1):
            prompt = qs[qid] + ARM_SUFFIX[args.arm]
            row = dict.fromkeys(FIELDS, "")
            row.update(round=args.round, arm=args.arm, question_id=qid, run=run, tool="codex exec",
                       tool_version=version, model_requested=args.model, reasoning_effort=args.effort,
                       date_utc=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"))
            started = time.monotonic()
            with tempfile.TemporaryDirectory(prefix="blank_") as empty:
                try:
                    proc = subprocess.run(command(codex, args.model, args.effort), input=prompt, capture_output=True,
                                          text=True, encoding="utf-8", errors="replace", cwd=empty,
                                          timeout=args.timeout, env=env)
                    out, err, code = proc.stdout, proc.stderr, proc.returncode
                except subprocess.TimeoutExpired as e:
                    out = e.stdout.decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
                    err, code = f"abandoned after {args.timeout}s", "timeout"
            raw_file = raw_dir / f"r{args.round}_{args.arm}_{qid}_{run}.codex.jsonl"
            raw_file.write_text(out, encoding="utf-8")
            row.update(summarize(out.splitlines()))
            row.update(exit_code=code, raw_file=raw_file.name, seconds=round(time.monotonic() - started, 1))
            if code != 0:
                row["notes"] = "; ".join(x for x in (row["notes"], f"exit {code}: {err.strip()[-300:]}") if x)
            writer.writerow(row)
            f.flush()
            print(f"  [{n}/{len(plan)}] {qid} run {run}: {row['searches_total']} searches, {row['opens_total']} pages opened, "
                  f"{row['tokens_total']} tokens, {row['seconds']}s {row['notes'][:120]}")
            if code != 0 and not row["answer_text"] and n == 1:
                raise SystemExit("the first run produced no answer; fix that before running the rest "
                                 f"(see {raw_file.name} and the note in runs.csv)")
    print(f"done: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
