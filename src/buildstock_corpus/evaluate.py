"""Does the index actually beat asking Claude directly?

The baseline is deliberately the thing a user would otherwise do: paste the question
into a Claude chat. So the comparison holds the model and generation config fixed and
varies only one thing — whether the retrieved ComStock passages are in the prompt.

Three layers, cheapest first, each usable on its own:

1. Retrieval (no API key, always runs) — for each gold question, is the expected source
   in the top-k, at what rank, and do the gold answer points appear *verbatim* in the
   retrieved text? Point coverage in context is the honest ceiling on what retrieval can
   contribute: if the number isn't in the passages, no amount of prompting recovers it.
2. Head-to-head answers (`--answer`) — same model twice, once with the passages and once
   with nothing, so the two answers can be read side by side.
3. LLM judge (`--judge`) — grades each answer point per side as supported / missing /
   contradicted. `contradicted` on the bare-Claude side is the metric that matters most:
   a confidently wrong release-specific number is worse than a refusal.

Questions marked `known_gap: true` in the gold set are excluded from recall@k and
reported separately. They exist so the summary can't quietly credit the index for
coverage it doesn't have.

Without an API key, layers 2 and 3 are skipped and `eval/baseline_prompts.md` is written
instead, so the same comparison can be run by hand in claude.ai.
"""

from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .paths import PROJECT_ROOT

MODEL = "claude-opus-5"
EVAL_DIR = PROJECT_ROOT / "eval"
DEFAULT_GOLD = EVAL_DIR / "gold_set.yaml"
DEFAULT_RESULTS = EVAL_DIR / "results.json"
DEFAULT_PROMPTS = EVAL_DIR / "baseline_prompts.md"


# --------------------------------------------------------------------------- gold set


@dataclass
class GoldQuestion:
    id: str
    question: str
    category: str = "uncategorized"
    expected_sources: list[str] = field(default_factory=list)
    # Each point is a list of accepted variants; any one variant counts as present.
    points: list[list[str]] = field(default_factory=list)
    known_gap: bool = False
    note: str = ""

    @property
    def point_labels(self) -> list[str]:
        """First variant of each point — what the judge and the reports display."""
        return [variants[0] for variants in self.points]


def load_gold_set(path: Path = DEFAULT_GOLD) -> tuple[str, str, list[GoldQuestion]]:
    """Parse the gold set; returns (product, release, questions)."""
    import yaml

    if not path.exists():
        raise FileNotFoundError(f"no gold set at {path}")
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}

    questions: list[GoldQuestion] = []
    seen: set[str] = set()
    for entry in raw.get("questions", []):
        qid = entry.get("id")
        if not qid:
            raise ValueError(f"gold question missing 'id': {entry}")
        if qid in seen:
            raise ValueError(f"duplicate gold question id: {qid}")
        seen.add(qid)

        sources = entry.get("expected_sources") or []
        if isinstance(sources, str):
            sources = [sources]
        points: list[list[str]] = []
        for point in entry.get("expected_answer_points") or []:
            points.append([str(point)] if isinstance(point, str) else [str(v) for v in point])

        questions.append(
            GoldQuestion(
                id=qid,
                question=" ".join(str(entry["question"]).split()),
                category=entry.get("category", "uncategorized"),
                expected_sources=[str(s) for s in sources],
                points=points,
                known_gap=bool(entry.get("known_gap", False)),
                note=" ".join(str(entry.get("note", "")).split()),
            )
        )
    if not questions:
        raise ValueError(f"gold set at {path} has no questions")
    return raw.get("product", "comstock"), str(raw.get("release", "2025-3")), questions


# ------------------------------------------------------------------- matching helpers

_WS = re.compile(r"\s+")


def _tighten(text: str) -> str:
    """Normalize for substring matching: NFKC, unify dashes, drop all whitespace.

    Whitespace-insensitive matching is what makes "-1°C" match "- 1 °C" and "1 hour"
    match "1  hour" across PDF-extracted text. It is a proxy, not a grader — use
    --judge when the wording of an answer matters.
    """
    out = unicodedata.normalize("NFKC", text).lower()
    for dash in ("−", "–", "—"):
        out = out.replace(dash, "-")
    return _WS.sub("", out)


def _point_present(variants: list[str], haystack_tight: str) -> bool:
    return any(_tighten(v) in haystack_tight for v in variants)


def _citation(meta: dict) -> str:
    return f"{meta.get('source_id', '')}/{meta.get('source_path', '')}"


def _source_rank(q: GoldQuestion, hits: list[dict]) -> int | None:
    """1-based rank of the first hit matching any expected source, else None."""
    for rank, hit in enumerate(hits, 1):
        cite = _citation(hit["metadata"])
        if any(expected in cite for expected in q.expected_sources):
            return rank
    return None


# ------------------------------------------------------------------------ LLM helpers

RAG_INSTRUCTION = (
    "Answer the question using ONLY the passages below, which come from the ComStock "
    "{release} documentation. Cite the passages you use as [n]. If the passages do not "
    "cover the question, say so explicitly rather than guessing."
)


def _anthropic_client():
    """Return an Anthropic client, or None if the key or SDK is missing."""
    import os

    if not os.environ.get("ANTHROPIC_API_KEY"):
        return None
    try:
        import anthropic
    except ImportError:
        return None
    return anthropic.Anthropic()


def _complete(client, prompt: str, max_tokens: int = 2048, schema: dict | None = None) -> str:
    """One streamed message. Streaming keeps long-context calls off the request timeout."""
    kwargs: dict[str, Any] = {
        "model": MODEL,
        "max_tokens": max_tokens,
        "thinking": {"type": "adaptive"},
        "messages": [{"role": "user", "content": prompt}],
    }
    if schema is not None:
        kwargs["output_config"] = {"format": {"type": "json_schema", "schema": schema}}
    with client.messages.stream(**kwargs) as stream:
        msg = stream.get_final_message()
    return "".join(b.text for b in msg.content if b.type == "text").strip()


def _render_passages(hits: list[dict]) -> str:
    """The exact passage block the model is given — citation line included.

    Context coverage is scored against this, not against chunk text alone: the citation
    line is part of what the model can see, so a report number that only appears in a
    source path (e.g. measure_pdfs/89340.pdf) is legitimately available to it.
    """
    return "\n\n".join(
        f"[{i}] {_citation(h['metadata'])}"
        + (f" § {h['metadata']['section']}" if h["metadata"].get("section") else "")
        + f"\n{h['text']}"
        for i, h in enumerate(hits, 1)
    )


def _rag_prompt(q: GoldQuestion, hits: list[dict], release: str) -> str:
    passages = _render_passages(hits)
    return (
        f"{RAG_INSTRUCTION.format(release=release)}\n\n"
        f"Passages:\n{passages}\n\nQuestion: {q.question}"
    )


_VERDICT = {
    "type": "object",
    "properties": {
        "point": {"type": "string"},
        "verdict": {"type": "string", "enum": ["supported", "missing", "contradicted"]},
    },
    "required": ["point", "verdict"],
    "additionalProperties": False,
}

_JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "rag": {"type": "array", "items": _VERDICT},
        "baseline": {"type": "array", "items": _VERDICT},
        "rag_cites_sources": {"type": "boolean"},
        "baseline_hedges": {"type": "boolean"},
        "notes": {"type": "string"},
    },
    "required": ["rag", "baseline", "rag_cites_sources", "baseline_hedges", "notes"],
    "additionalProperties": False,
}


def _judge(client, q: GoldQuestion, rag_answer: str, baseline_answer: str) -> dict:
    """Grade both answers against the gold points. One point per verdict entry, in order."""
    points = "\n".join(f"{i}. {label}" for i, label in enumerate(q.point_labels, 1))
    prompt = (
        "You are grading two answers to the same question about the ComStock commercial "
        "building stock dataset. Grade each answer independently against the list of facts "
        "a correct answer must contain.\n\n"
        "For every fact, return one verdict per answer:\n"
        "- supported: the answer states this fact (equivalent units or wording is fine)\n"
        "- missing: the answer does not state it, or explicitly declines to\n"
        "- contradicted: the answer asserts something incompatible with it\n\n"
        "Return the verdicts in the same order as the fact list, one entry per fact. "
        "Judge only against the facts given; do not use your own knowledge of ComStock. "
        "Set baseline_hedges to true if answer B disclaims knowledge of this dataset "
        "release or warns that its information may be outdated.\n\n"
        f"Question: {q.question}\n\n"
        f"Facts a correct answer must contain:\n{points}\n\n"
        f"Answer A (retrieval-augmented):\n{rag_answer}\n\n"
        f"Answer B (no retrieval):\n{baseline_answer}"
    )
    return json.loads(_complete(client, prompt, max_tokens=4096, schema=_JUDGE_SCHEMA))


def _verdict_counts(verdicts: list[dict], n_points: int) -> dict:
    counts = {"supported": 0, "missing": 0, "contradicted": 0}
    for v in verdicts:
        if v.get("verdict") in counts:
            counts[v["verdict"]] += 1
    # A judge that returns fewer verdicts than facts is treated as "missing", never as a pass.
    counts["missing"] += max(0, n_points - sum(counts.values()))
    counts["score"] = round(counts["supported"] / n_points, 3) if n_points else 0.0
    return counts


# ------------------------------------------------------------------------------ report


def _mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 3) if values else 0.0


def _summarize(rows: list[dict], k: int) -> dict:
    scored = [r for r in rows if not r["known_gap"]]
    gaps = [r for r in rows if r["known_gap"]]

    ranks = [r["retrieval"]["rank"] for r in scored if r["retrieval"]["rank"]]
    summary: dict[str, Any] = {
        "questions_total": len(rows),
        "questions_scored": len(scored),
        "known_gaps": len(gaps),
        f"recall_at_{k}": _mean([1.0 if r["retrieval"]["rank"] else 0.0 for r in scored]),
        "mrr": _mean([1.0 / rank for rank in ranks] + [0.0] * (len(scored) - len(ranks))),
        "context_point_coverage": _mean([r["retrieval"]["context_coverage"] for r in scored]),
        "known_gap_ids": [r["id"] for r in gaps],
        "retrieval_misses": [r["id"] for r in scored if not r["retrieval"]["rank"]],
    }

    judged = [r for r in scored if r.get("judge")]
    if judged:
        summary["judged"] = {
            "n": len(judged),
            "rag_point_score": _mean([r["judge"]["rag"]["score"] for r in judged]),
            "baseline_point_score": _mean([r["judge"]["baseline"]["score"] for r in judged]),
            "rag_contradictions": sum(r["judge"]["rag"]["contradicted"] for r in judged),
            "baseline_contradictions": sum(r["judge"]["baseline"]["contradicted"] for r in judged),
            "rag_cited_sources": sum(1 for r in judged if r["judge"]["rag_cites_sources"]),
            "baseline_hedged": sum(1 for r in judged if r["judge"]["baseline_hedges"]),
        }
    answered = [r for r in scored if r.get("answers")]
    if answered:
        summary["answer_substring_coverage"] = {
            "n": len(answered),
            "rag": _mean([r["answers"]["rag_coverage"] for r in answered]),
            "baseline": _mean([r["answers"]["baseline_coverage"] for r in answered]),
        }
    return summary


def _print_report(rows: list[dict], summary: dict, k: int) -> None:
    print(f"\n{'id':<38} {'cat':<20} {'rank':>5} {'ctx':>6}  judged rag/base")
    print("-" * 88)
    for r in rows:
        rank = r["retrieval"]["rank"]
        rank_s = str(rank) if rank else ("gap" if r["known_gap"] else "MISS")
        judged = ""
        if r.get("judge"):
            j = r["judge"]
            judged = f"{j['rag']['score']:.2f}/{j['baseline']['score']:.2f}"
            if j["baseline"]["contradicted"]:
                judged += f"  (base contradicted x{j['baseline']['contradicted']})"
        print(
            f"{r['id']:<38} {r['category']:<20} {rank_s:>5} "
            f"{r['retrieval']['context_coverage']:>6.2f}  {judged}"
        )

    print(f"\nscored {summary['questions_scored']} questions ({summary['known_gaps']} known gaps excluded)")
    print(f"  recall@{k}                {summary[f'recall_at_{k}']:.2f}")
    print(f"  MRR                     {summary['mrr']:.2f}")
    print(f"  gold points in context  {summary['context_point_coverage']:.2f}")
    if summary["retrieval_misses"]:
        print(f"  retrieval misses        {', '.join(summary['retrieval_misses'])}")
    if summary["known_gap_ids"]:
        print(f"  known gaps (excluded)   {', '.join(summary['known_gap_ids'])}")

    j = summary.get("judged")
    if j:
        print(f"\njudged head-to-head on {j['n']} questions (model {MODEL}, identical config):")
        print(f"  gold points supported   index {j['rag_point_score']:.2f}  vs  bare {j['baseline_point_score']:.2f}")
        print(f"  contradicted facts      index {j['rag_contradictions']}     vs  bare {j['baseline_contradictions']}")
        print(f"  cited a source          index {j['rag_cited_sources']}/{j['n']}")
        print(f"  hedged on the release   bare  {j['baseline_hedged']}/{j['n']}")


def _write_baseline_prompts(path: Path, questions: list[GoldQuestion], release: str) -> None:
    """Copy-pasteable prompts for running the bare-Claude side by hand in claude.ai."""
    lines = [
        f"# Bare-Claude baseline prompts — ComStock {release}",
        "",
        "Paste each question into a fresh Claude chat with no attachments and no project "
        "context, then grade the reply against the facts listed under it. This is the same "
        "baseline `bsc eval --answer --judge` automates; it exists so the comparison can be "
        "run without an API key.",
        "",
    ]
    for q in questions:
        lines += [f"## {q.id}  ({q.category})", "", "```text", q.question, "```", ""]
        lines.append("A correct answer must contain:")
        lines += [f"- {label}" for label in q.point_labels]
        if q.known_gap:
            lines += ["", f"> Known corpus gap — the index cannot answer this either. {q.note}"]
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


# -------------------------------------------------------------------------- entrypoint


def evaluate_release(
    product: str | None = None,
    release: str | None = None,
    gold_path: Path = DEFAULT_GOLD,
    k: int = 5,
    answer: bool = False,
    judge: bool = False,
    out_path: Path = DEFAULT_RESULTS,
    prompts_path: Path | None = DEFAULT_PROMPTS,
) -> dict:
    """Run the gold set against the index; write results.json and return the payload."""
    from .query import search

    gold_product, gold_release, questions = load_gold_set(gold_path)
    product = product or gold_product
    release = release or gold_release

    client = _anthropic_client() if (answer or judge) else None
    if (answer or judge) and client is None:
        print(
            "[no ANTHROPIC_API_KEY or anthropic SDK — running retrieval only.\n"
            f" the bare-Claude side can still be done by hand from {prompts_path}]"
        )
    if judge and not answer:
        answer = True  # nothing to judge otherwise

    rows: list[dict] = []
    for i, q in enumerate(questions, 1):
        print(f"[{i}/{len(questions)}] {q.id}", flush=True)
        hits = search(product, release, q.question, k=k)
        context_tight = _tighten(_render_passages(hits))
        present = [_point_present(variants, context_tight) for variants in q.points]

        row: dict[str, Any] = {
            "id": q.id,
            "category": q.category,
            "question": q.question,
            "known_gap": q.known_gap,
            "note": q.note,
            "retrieval": {
                "rank": _source_rank(q, hits),
                "expected_sources": q.expected_sources,
                "context_coverage": round(sum(present) / len(present), 3) if present else 0.0,
                "points_in_context": [
                    {"point": label, "present": ok} for label, ok in zip(q.point_labels, present)
                ],
                "hits": [
                    {
                        "rank": r,
                        "score": h["score"],
                        "source": _citation(h["metadata"]),
                        "section": h["metadata"].get("section", ""),
                    }
                    for r, h in enumerate(hits, 1)
                ],
            },
        }

        if client is not None:
            rag_answer = _complete(client, _rag_prompt(q, hits, release))
            # The baseline gets the bare question and nothing else — same model, same
            # config, no system prompt. That is the chat a user would otherwise have.
            baseline_answer = _complete(client, q.question)
            rag_tight, base_tight = _tighten(rag_answer), _tighten(baseline_answer)
            row["answers"] = {
                "rag": rag_answer,
                "baseline": baseline_answer,
                "rag_coverage": round(
                    sum(_point_present(v, rag_tight) for v in q.points) / len(q.points), 3
                )
                if q.points
                else 0.0,
                "baseline_coverage": round(
                    sum(_point_present(v, base_tight) for v in q.points) / len(q.points), 3
                )
                if q.points
                else 0.0,
            }
            if judge:
                verdicts = _judge(client, q, rag_answer, baseline_answer)
                n = len(q.points)
                row["judge"] = {
                    "rag": _verdict_counts(verdicts.get("rag", []), n),
                    "baseline": _verdict_counts(verdicts.get("baseline", []), n),
                    "rag_cites_sources": bool(verdicts.get("rag_cites_sources")),
                    "baseline_hedges": bool(verdicts.get("baseline_hedges")),
                    "notes": verdicts.get("notes", ""),
                    "verdicts": verdicts,
                }
        rows.append(row)

    summary = _summarize(rows, k)
    payload = {
        "product": product,
        "release": release,
        "k": k,
        "model": MODEL if client is not None else None,
        "gold_set": str(gold_path.relative_to(PROJECT_ROOT)) if gold_path.is_relative_to(PROJECT_ROOT) else str(gold_path),
        "answers_generated": client is not None,
        "judged": bool(judge and client is not None),
        "summary": summary,
        "questions": rows,
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    if prompts_path is not None:
        prompts_path.parent.mkdir(parents=True, exist_ok=True)
        _write_baseline_prompts(prompts_path, questions, release)

    _print_report(rows, summary, k)
    print(f"\nwrote {out_path}")
    if prompts_path is not None:
        print(f"wrote {prompts_path}")
    return payload
