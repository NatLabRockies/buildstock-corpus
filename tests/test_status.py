"""The publication-status vocabulary is what citation guidance keys on, so its three values
and the rules that assign them are pinned here: OSTI reports are recognised by URL, anything
the ComStock site serves itself is site_page whether page or PDF, and a link kind with no
document behind it is missing. An external link that is not an OSTI report is a decision
for the owner, not a guess, so it raises.
"""

from __future__ import annotations

import pytest

from buildstock_corpus import status as S


def test_vocabulary_is_exactly_three_values():
    assert S.STATUSES == {"osti_pdf", "site_page", "missing"}


@pytest.mark.parametrize(
    "url",
    [
        "https://www.nlr.gov/docs/fy24osti/89340.pdf",
        "https://docs.nlr.gov/docs/fy25osti/95002.pdf",
        "HTTPS://WWW.NLR.GOV/DOCS/FY23OSTI/86103.PDF",
    ],
)
def test_osti_urls_are_recognised(url):
    assert S.is_osti_url(url)
    assert S.status_for_url(url) == S.OSTI_PDF


@pytest.mark.parametrize(
    "url",
    [
        "https://docs.nlr.gov/measures/hvac_0001.pdf",  # nlr.gov but not under fyNNosti
        "https://natlabrockies.github.io/ComStock.github.io/assets/files/x.pdf",
        "https://www.nlr.gov/docs/fy24osti/89340.html",
        "",
        None,
    ],
)
def test_non_osti_urls_are_not(url):
    assert not S.is_osti_url(url)


def test_non_osti_external_url_is_an_error_not_a_guess():
    with pytest.raises(ValueError, match="not an OSTI report"):
        S.status_for_url("https://example.org/report.pdf")


def test_site_served_kinds_are_site_page_whether_page_or_pdf():
    assert S.status_for_kind("internal_md", "docs/upgrade_measures/env_window_film.md") == S.SITE_PAGE
    assert S.status_for_kind("local_pdf", "assets/files/ComStock Measure Doc.pdf") == S.SITE_PAGE


def test_external_pdf_is_judged_by_its_url():
    assert S.status_for_kind("external_pdf", "https://www.nlr.gov/docs/fy24osti/89340.pdf") == S.OSTI_PDF


@pytest.mark.parametrize("kind", ["none", "external_other", "unknown"])
def test_kinds_without_a_document_are_missing(kind):
    assert S.status_for_kind(kind, None) == S.MISSING


def test_check_status_names_the_offender():
    assert S.check_status("site_page", "x") == "site_page"
    with pytest.raises(ValueError, match="technical_reference.*'draft_pdf'"):
        S.check_status("draft_pdf", "technical_reference")
