"""The latex extractor's character normalization, and the audit that scores it.

pandoc renders TeX's typesetting hints as literal Unicode: `\\-` becomes a soft hyphen, `~`
becomes a non-breaking space, `--` becomes an en dash. The soft hyphens are the reason this
exists — they landed *inside* identifiers, invisibly, so `HPACCOOLPLFFPLR` did not match the
document that contained it. Each case below is a real spelling taken from the technical
reference; a regression here silently un-fixes retrieval on those identifiers.

The normalization is deliberately per class rather than one ASCII fold, and the case that
proves it is the placeholder dash: an en dash alone in a table cell means "no value", so
folding it to `-` would put something that reads as a value into an empty cell.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

from buildstock_corpus.extract.latex import _normalize_characters

REPO = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "audit_md_fidelity", REPO / "scripts" / "audit_md_fidelity.py"
)
audit_md_fidelity = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(audit_md_fidelity)
A = audit_md_fidelity

SHY = "\u00ad"  # soft hyphen
NBSP = "\u00a0"  # non-breaking space
EN = "\u2013"  # en dash


# --- soft hyphens: deleted, because they hide inside identifiers ---------------------------

@pytest.mark.parametrize(
    "spelled,real",
    [
        (f"HPA{SHY}CCOOL{SHY}PLFFPLR", "HPACCOOLPLFFPLR"),  # an EnergyPlus curve name
        (f"FullService{SHY}Restaurant", "FullServiceRestaurant"),  # a ComStock building type
        (f"EIA{SHY}861", "EIA861"),
    ],
)
def test_soft_hyphen_is_deleted_so_the_identifier_is_searchable(spelled, real):
    assert _normalize_characters(spelled) == real


def test_soft_hyphen_deletion_does_not_join_across_a_real_hyphen():
    """Only the invisible character goes; an author's real hyphen is content."""
    assert _normalize_characters(f"Pre-1980{SHY}vintage") == "Pre-1980vintage"


# --- nbsp: a plain space, because nothing tokenizes on U+00A0 ------------------------------

def test_nbsp_becomes_a_plain_space():
    assert _normalize_characters(f"Table{NBSP}5") == "Table 5"


# --- en dashes: only the digit-flanked ones fold -------------------------------------------

@pytest.mark.parametrize(
    "spelled,real",
    [
        (f"1980{EN}2004", "1980-2004"),  # the vintage bin the corpus spells both ways
        (f"| Hospital | 120 | 132{EN}220 |", "| Hospital | 120 | 132-220 |"),
    ],
)
def test_range_en_dash_folds_to_ascii(spelled, real):
    assert _normalize_characters(spelled) == real


@pytest.mark.parametrize(
    "line",
    [
        f"| QuickServiceRestaurant | {EN} | {EN} | Corridor |",  # empty-cell placeholders
        f'<td style="text-align: center;">{EN}</td>',  # same, inside a rowspan table
    ],
)
def test_placeholder_en_dash_in_an_empty_cell_is_left_alone(line):
    """It means "no value". An ASCII `-` there reads as a value or a minus sign."""
    assert _normalize_characters(line) == line


@pytest.mark.parametrize(
    "text",
    [
        "23.5°C",  # degree
        "EnergyPlus® and DOE-2™",  # registered / trademark
        "kW·h",  # middot
        "the “baseline” model’s",  # smart quotes
        "one thing — then another",  # em dash
        "−5.0",  # U+2212 minus, not a range
    ],
)
def test_legitimate_characters_are_untouched(text):
    """None of these is a fidelity problem, and a blanket ASCII fold would damage them."""
    assert _normalize_characters(text) == text


def test_a_lone_en_dash_between_non_digits_is_not_a_range():
    assert _normalize_characters(f"gen1{EN}gen3") == f"gen1{EN}gen3"


# --- the audit has to score all three, or the fix has no scoreboard -----------------------

def test_audit_counts_each_character_class(tmp_path):
    body = f"# Doc\n\nHPA{SHY}CCOOL uses Table{NBSP}5 for 1980{EN}2004 and 132{EN}220.\n"
    (tmp_path / "doc.md").write_text(body, encoding="utf-8")
    findings, totals = A.audit(tmp_path, {})
    assert findings[0]["characters"] == {
        "soft_hyphens": 1,
        "nbsp": 1,
        "range_en_dashes": 2,
    }
    assert totals["unknown"]["soft_hyphens"] == 1
    assert totals["unknown"]["range_en_dashes"] == 2


def test_audit_does_not_count_a_placeholder_dash_as_a_defect(tmp_path):
    (tmp_path / "doc.md").write_text(
        f"# Doc\n\n| a | b |\n|---|---|\n| x | {EN} |\n", encoding="utf-8"
    )
    _, totals = A.audit(tmp_path, {})
    assert totals["unknown"]["range_en_dashes"] == 0


def test_audit_reports_a_clean_file_as_having_no_character_findings(tmp_path):
    (tmp_path / "doc.md").write_text("# Doc\n\nAll ASCII, 1980-2004.\n", encoding="utf-8")
    findings, totals = A.audit(tmp_path, {})
    assert findings == []
    assert totals["unknown"]["soft_hyphens"] == 0
