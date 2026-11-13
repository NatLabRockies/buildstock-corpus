"""Run the 13 questions of RUNNER.md against the Claude API and record what happened.

The automated form of the hand-run sheet: one fresh API conversation per run, no system
prompt, no memory, web search and web fetch the only tools. Each run writes one row to
runs.csv (every search, every URL fetched, the answer, exact token counts) and the full
response to logs/, so anything else can be derived later without re-running.

Needs only this file, RUNNER.md beside it, Python 3.10+ and `pip install anthropic`.
Credentials come from the environment (ANTHROPIC_API_KEY, or an `ant auth login` profile);
set ANTHROPIC_BASE_URL as well if you go through a gateway.

    python run_arm.py --dry-run                 # show what would be sent; no API call
    python run_arm.py --round 1 --only Q01 --runs 1   # one real run, to check it works
    python run_arm.py --round 1                 # all 13 questions x 3 runs

Re-running skips runs already in runs.csv, so an interrupted pass can be resumed.
Use the same --model and --effort for the repeat pass; both are recorded in every row.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import pathlib
import re
import sys
import time

HERE = pathlib.Path(__file__).parent
FIELDS = [
    "round", "arm", "question_id", "run", "model_requested", "model_served", "effort", "date_utc",
    "stop_reason", "searches_total", "search_queries", "search_result_urls", "fetches_total",
    "urls_fetched", "fetch_errors", "answer_text", "citation_urls", "tokens_in", "tokens_out",
    "tokens_cache_read", "tokens_cache_write", "tokens_total", "api_calls", "seconds", "request_ids",
    "raw_file", "notes",
]
# What each arm appends to the question. Arm A is the question alone.
ARM_SUFFIX = {
    "A": "",
    "B": (" Use only pages and files under natlabrockies.github.io/ResStock.github.io and docs.nlr.gov."
          " Cite the page or report you used."),
}
MAX_CONTINUATIONS = 8  # a long server-tool turn pauses and is resumed; this bounds it


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


def tools(basic: bool) -> list[dict]:
    """Web search and web fetch, run on Anthropic's servers. Nothing else."""
    if basic:  # older models, and platforms that only offer the first versions
        return [{"type": "web_search_20250305", "name": "web_search"},
                {"type": "web_fetch_20250910", "name": "web_fetch"}]
    return [{"type": "web_search_20260209", "name": "web_search"},
            {"type": "web_fetch_20260209", "name": "web_fetch"}]


def ask(client, model: str, effort: str, prompt: str, basic_tools: bool) -> tuple[list[dict], dict]:
    """One conversation. Returns every content block and the summed usage.

    A turn that uses server tools can stop with `pause_turn`; the assistant content is sent
    back unchanged and the server carries on, with no extra user message.
    """
    messages = [{"role": "user", "content": prompt}]
    blocks: list[dict] = []
    tally = {"input_tokens": 0, "output_tokens": 0, "cache_read_input_tokens": 0,
             "cache_creation_input_tokens": 0, "api_calls": 0, "request_ids": [],
             "stop_reason": None, "model": None, "stop_details": None}
    for _ in range(MAX_CONTINUATIONS + 1):
        with client.messages.stream(
            model=model,
            max_tokens=64000,
            output_config={"effort": effort},
            tools=tools(basic_tools),
            messages=messages,
        ) as stream:
            message = stream.get_final_message()
        data = message.to_dict()
        usage = data.get("usage") or {}
        for key in ("input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens"):
            tally[key] += usage.get(key) or 0
        tally["api_calls"] += 1
        tally["request_ids"].append(getattr(message, "_request_id", None) or "")
        tally["stop_reason"] = data.get("stop_reason")
        tally["stop_details"] = data.get("stop_details")
        tally["model"] = data.get("model")
        blocks.extend(data.get("content") or [])
        if data.get("stop_reason") != "pause_turn":
            break
        messages = [{"role": "user", "content": prompt}, {"role": "assistant", "content": blocks}]
    return blocks, tally


def summarize(blocks: list[dict]) -> dict:
    """Pull the searches, the fetched URLs (in order), the answer and its citations out."""
    queries, result_urls, fetched, fetch_errors, answer, cited = [], [], [], [], [], []
    fetch_url_by_id = {}
    for b in blocks:
        kind = b.get("type")
        if kind == "server_tool_use":
            args = b.get("input") or {}
            if b.get("name") == "web_search":
                queries.append(str(args.get("query", "")))
            elif b.get("name") == "web_fetch":
                url = str(args.get("url", ""))
                fetched.append(url)
                fetch_url_by_id[b.get("id")] = url
        elif kind == "web_search_tool_result":
            content = b.get("content")
            if isinstance(content, list):  # a list on success, a single error object otherwise
                result_urls += [r.get("url", "") for r in content if isinstance(r, dict)]
            elif isinstance(content, dict):
                fetch_errors.append(f"search:{content.get('error_code', 'error')}")
        elif kind == "web_fetch_tool_result":
            content = b.get("content") or {}
            if isinstance(content, dict) and "error" in str(content.get("type", "")):
                url = fetch_url_by_id.get(b.get("tool_use_id"), "?")
                fetch_errors.append(f"{url}:{content.get('error_code', 'error')}")
        elif kind == "text":
            answer.append(b.get("text", ""))
            for c in b.get("citations") or []:
                if c.get("url") and c["url"] not in cited:
                    cited.append(c["url"])
    return {
        "searches_total": len(queries),
        "search_queries": " | ".join(queries),
        "search_result_urls": " ".join(u for u in result_urls if u),
        "fetches_total": len(fetched),
        "urls_fetched": " ".join(fetched),
        "fetch_errors": " | ".join(fetch_errors),
        "answer_text": "".join(answer).strip(),
        "citation_urls": " ".join(cited),
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
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--effort", default="medium", choices=["low", "medium", "high", "xhigh", "max"])
    ap.add_argument("--basic-tools", action="store_true", help="use the first-version web tools (older models, some platforms)")
    ap.add_argument("--runner", type=pathlib.Path, default=HERE / "RUNNER.md")
    ap.add_argument("--out", type=pathlib.Path, default=HERE / "runs.csv")
    ap.add_argument("--dry-run", action="store_true", help="print the plan and the first prompt; call nothing")
    args = ap.parse_args()

    qs = questions(args.runner)
    wanted = [q for q in qs if not args.only or q in args.only]
    have = done_runs(args.out)
    plan = [(q, r) for q in wanted for r in range(1, args.runs + 1)
            if (args.round, args.arm, q, str(r)) not in have]
    print(f"{len(qs)} questions in {args.runner.name}; {len(plan)} runs to do "
          f"(arm {args.arm}, round {args.round}, model {args.model}, effort {args.effort})")
    if args.dry_run:
        for q, r in plan[:3]:
            print(f"  {q} run {r}: {qs[q] + ARM_SUFFIX[args.arm]}")
        print("  tools:", json.dumps(tools(args.basic_tools)))
        print("  no system prompt; one new conversation per run; nothing was sent")
        return 0

    import anthropic

    client = anthropic.Anthropic()  # credentials and any base URL come from the environment
    raw_dir = args.out.parent / "logs"
    raw_dir.mkdir(exist_ok=True)
    new_file = not args.out.is_file()
    with args.out.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        for n, (qid, run) in enumerate(plan, 1):
            prompt = qs[qid] + ARM_SUFFIX[args.arm]
            row = dict.fromkeys(FIELDS, "")
            row.update(round=args.round, arm=args.arm, question_id=qid, run=run, model_requested=args.model,
                       effort=args.effort, date_utc=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"))
            started = time.monotonic()
            try:
                blocks, tally = ask(client, args.model, args.effort, prompt, args.basic_tools)
            except anthropic.AuthenticationError:
                raise SystemExit("the API rejected the credentials; nothing more was run")
            except anthropic.NotFoundError as e:
                raise SystemExit(f"model or endpoint not found ({e.message}); nothing more was run")
            except anthropic.BadRequestError as e:
                # Usually a platform that does not offer these tools or this model: stop, do not fill
                # the sheet with 39 identical failures.
                raise SystemExit(f"the API refused the request ({e.message}); nothing more was run")
            except anthropic.RateLimitError as e:
                row["notes"] = f"rate limited after the SDK's retries: {e.message}"
            except anthropic.APIStatusError as e:
                row["notes"] = f"API error {e.status_code}: {e.message}"
            except anthropic.APIConnectionError as e:
                row["notes"] = f"network error: {e}"
            else:
                raw_file = raw_dir / f"r{args.round}_{args.arm}_{qid}_{run}.json"
                raw_file.write_text(json.dumps({"prompt": prompt, "content": blocks, "tally": tally}, indent=1),
                                    encoding="utf-8")
                row.update(summarize(blocks))
                total = (tally["input_tokens"] + tally["output_tokens"] + tally["cache_read_input_tokens"]
                         + tally["cache_creation_input_tokens"])
                notes = []
                if tally["stop_reason"] == "refusal":
                    notes.append(f"refused: {tally['stop_details']}")
                elif tally["stop_reason"] != "end_turn":
                    notes.append(f"did not finish normally (stop_reason {tally['stop_reason']})")
                row.update(model_served=tally["model"], stop_reason=tally["stop_reason"],
                           tokens_in=tally["input_tokens"], tokens_out=tally["output_tokens"],
                           tokens_cache_read=tally["cache_read_input_tokens"],
                           tokens_cache_write=tally["cache_creation_input_tokens"], tokens_total=total,
                           api_calls=tally["api_calls"], request_ids=" ".join(tally["request_ids"]),
                           raw_file=raw_file.name, notes="; ".join(notes))
            row["seconds"] = round(time.monotonic() - started, 1)
            writer.writerow(row)
            f.flush()
            print(f"  [{n}/{len(plan)}] {qid} run {run}: {row['fetches_total'] or 0} fetches, "
                  f"{row['tokens_total'] or '?'} tokens, {row['seconds']}s {row['notes']}")
    print(f"done: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
