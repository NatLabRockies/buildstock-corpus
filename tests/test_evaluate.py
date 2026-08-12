"""Gold-set parsing and eval scoring — the parts that must not silently flatter the index."""

from __future__ import annotations

import json

import pytest

from buildstock_corpus import evaluate as ev
from buildstock_corpus.evaluate import GoldQuestion

GOLD_YAML = """\
product: comstock
release: "2025-3"
questions:
  - id: numeric_point
    category: measure_parameters
    question: >-
      What is the default
      cooling offset?
    expected_sources: measure_pdfs/89341.pdf
    expected_answer_points:
      - ["-1°C", "1.8°F"]
      - "1 hour"
  - id: a_known_gap
    category: coverage
    known_gap: true
    question: Which measures lack documentation?
    expected_sources:
      - crosswalk.json
    expected_answer_points:
      - hvac_0021
    note: crosswalk.json is not chunked into the index.
"""


def _write_gold(tmp_path, body=GOLD_YAML):
    path = tmp_path / "gold_set.yaml"
    path.write_text(body, encoding="utf-8")
    return path


def test_load_gold_set_normalizes_shapes(tmp_path):
    product, release, questions = ev.load_gold_set(_write_gold(tmp_path))

    assert (product, release) == ("comstock", "2025-3")
    q = questions[0]
    # folded YAML scalar collapsed to a single line
    assert q.question == "What is the default cooling offset?"
    # scalar expected_sources coerced to a list; scalar point coerced to a 1-variant list
    assert q.expected_sources == ["measure_pdfs/89341.pdf"]
    assert q.points == [["-1°C", "1.8°F"], ["1 hour"]]
    assert q.point_labels == ["-1°C", "1 hour"]
    assert q.known_gap is False
    assert questions[1].known_gap is True


def test_load_gold_set_rejects_duplicate_ids(tmp_path):
    body = GOLD_YAML + "\n  - id: numeric_point\n    question: dup\n"
    with pytest.raises(ValueError, match="duplicate"):
        ev.load_gold_set(_write_gold(tmp_path, body))


def test_load_gold_set_rejects_empty(tmp_path):
    with pytest.raises(ValueError, match="no questions"):
        ev.load_gold_set(_write_gold(tmp_path, "questions: []\n"))


@pytest.mark.parametrize(
    "variants,haystack,expected",
    [
        # whitespace- and dash-insensitive: PDF extraction spaces numbers unpredictably
        (["-1°C"], "set to - 1 °C by default", True),
        (["-1°C"], "set to −1°C by default", True),  # unicode minus
        (["1 hour"], "duration of pre-cooling is 1  hour", True),
        # any-of variants
        (["-1°C", "1.8°F"], "an offset of 1.8°F", True),
        (["9.72%"], "roughly 9.7% of floor area", False),
    ],
)
def test_point_present_matching(variants, haystack, expected):
    assert ev._point_present(variants, ev._tighten(haystack)) is expected


def _hit(source_id, source_path, score=0.9):
    return {"text": "", "score": score, "metadata": {"source_id": source_id, "source_path": source_path}}


def test_source_rank_is_first_match_of_any_expected_source():
    q = GoldQuestion(id="q", question="?", expected_sources=["measure_pdfs/89341.pdf"])
    hits = [
        _hit("github_site", "docs/faq.md"),
        _hit("upgrade_measures", "measure_pdfs/89341.pdf"),
    ]
    assert ev._source_rank(q, hits) == 2
    assert ev._source_rank(q, hits[:1]) is None


def test_verdict_counts_treats_a_short_judge_reply_as_missing():
    # Three gold facts, one verdict returned: the two unaccounted facts must not pass.
    counts = ev._verdict_counts([{"point": "a", "verdict": "supported"}], n_points=3)
    assert counts == {"supported": 1, "missing": 2, "contradicted": 0, "score": pytest.approx(0.333)}


def test_summary_excludes_known_gaps_from_recall():
    rows = [
        {"id": "hit", "category": "c", "known_gap": False, "retrieval": {"rank": 1, "context_coverage": 1.0}},
        {"id": "miss", "category": "c", "known_gap": False, "retrieval": {"rank": None, "context_coverage": 0.0}},
        # a known gap that also misses must not drag recall down or count as scored
        {"id": "gap", "category": "c", "known_gap": True, "retrieval": {"rank": None, "context_coverage": 0.0}},
    ]
    summary = ev._summarize(rows, k=5)

    assert summary["questions_total"] == 3
    assert summary["questions_scored"] == 2
    assert summary["recall_at_5"] == 0.5
    assert summary["mrr"] == 0.5
    assert summary["context_point_coverage"] == 0.5
    assert summary["retrieval_misses"] == ["miss"]
    assert summary["known_gap_ids"] == ["gap"]


def test_shipped_gold_set_is_loadable_and_hits_the_expected_categories():
    product, release, questions = ev.load_gold_set(ev.DEFAULT_GOLD)

    assert (product, release) == ("comstock", "2025-3")
    assert len(questions) >= 8
    # every question is gradeable and points at something
    for q in questions:
        assert q.points, f"{q.id} has no expected answer points"
        assert q.expected_sources, f"{q.id} has no expected sources"
    # the gap questions are the honesty check — the set must keep at least one
    assert any(q.known_gap for q in questions)


def test_baseline_prompts_render_with_facts_and_gap_warning(tmp_path):
    _, release, questions = ev.load_gold_set(_write_gold(tmp_path))
    out = tmp_path / "baseline_prompts.md"

    ev._write_baseline_prompts(out, questions, release)
    text = out.read_text(encoding="utf-8")

    assert "What is the default cooling offset?" in text
    assert "- -1°C" in text  # gold facts listed for manual grading
    assert "Known corpus gap" in text  # gap questions flagged so they aren't miscounted


def test_evaluate_release_writes_results_without_an_api_key(tmp_path, monkeypatch):
    gold = _write_gold(tmp_path)
    # No API key path: retrieval only, no LLM calls.
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.setattr(
        "buildstock_corpus.query.search",
        lambda product, release, text, k=5: [_hit("upgrade_measures", "measure_pdfs/89341.pdf")],
    )
    out = tmp_path / "results.json"

    payload = ev.evaluate_release(
        gold_path=gold, k=1, answer=True, out_path=out, prompts_path=tmp_path / "prompts.md"
    )

    assert payload["answers_generated"] is False
    assert payload["judged"] is False
    written = json.loads(out.read_text(encoding="utf-8"))
    assert written["summary"]["questions_scored"] == 1
    assert written["summary"]["recall_at_1"] == 1.0
    assert "answers" not in written["questions"][0]
