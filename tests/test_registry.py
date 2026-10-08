"""The source registry is where a source declares the publication status all its documents
share. A latex/markdown source without one, or with a value outside the vocabulary, is a
registry error at load time, before any build; a measures source must not declare one,
because it derives status per document from the index page's links.
"""

from __future__ import annotations

import textwrap

import pytest

import buildstock_corpus.registry as R

RELEASE = "comstock_amy2018_2025_release_3"

BASE = textwrap.dedent(
    f"""\
    product: comstock
    release: "{RELEASE}"
    sources:
      - id: technical_reference
        type: latex
        repo: https://example.org/ComStock.git
        git_ref: "2025-3"
        doc_glob: "documentation/**/*.tex"
        latex_main: "documentation/reference_doc/main.tex"
        {{latex_status}}
        {{latex_link}}
      - id: upgrade_measures
        type: measures
        repo: https://example.org/ComStock.github.io.git
        git_ref: "2025_3"
        index_page: "docs/upgrade_measures/upgrade_measures.md"
        internal_dir: "docs/upgrade_measures"
        crosswalk_csv: "assets/files/crosswalk.csv"
        {{measures_status}}
        {{measures_link}}
    """
)


def _registry(
    tmp_path,
    monkeypatch,
    latex_status="status: site_page",
    measures_status="",
    latex_link="publication_url: https://example.org/site/assets/files/ref_2025_3.pdf",
    measures_link="site_url: https://example.org/site",
):
    path = tmp_path / "sources.yaml"
    path.write_text(
        BASE.format(
            latex_status=latex_status, measures_status=measures_status,
            latex_link=latex_link, measures_link=measures_link,
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(R, "sources_file", lambda p, r: path)
    return R.load_registry("comstock", RELEASE)


def test_publication_links_are_loaded(tmp_path, monkeypatch):
    reg = _registry(tmp_path, monkeypatch)
    assert reg.by_id("technical_reference").publication_url.endswith("ref_2025_3.pdf")
    assert reg.by_id("upgrade_measures").site_url == "https://example.org/site"


def test_latex_source_without_publication_url_is_rejected(tmp_path, monkeypatch):
    with pytest.raises(ValueError, match="technical_reference.*publication_url"):
        _registry(tmp_path, monkeypatch, latex_link="")


def test_site_source_without_site_url_is_rejected(tmp_path, monkeypatch):
    with pytest.raises(ValueError, match="upgrade_measures.*site_url"):
        _registry(tmp_path, monkeypatch, measures_link="")


def test_relative_or_http_links_are_rejected(tmp_path, monkeypatch):
    with pytest.raises(ValueError, match="absolute https"):
        _registry(tmp_path, monkeypatch, measures_link="site_url: http://example.org/site")
    with pytest.raises(ValueError, match="absolute https"):
        _registry(tmp_path, monkeypatch, latex_link="publication_url: assets/files/ref.pdf")


def test_source_status_is_loaded(tmp_path, monkeypatch):
    reg = _registry(tmp_path, monkeypatch)
    assert reg.by_id("technical_reference").status == "site_page"
    assert reg.by_id("upgrade_measures").status is None  # derived per document


def test_latex_source_without_status_is_rejected(tmp_path, monkeypatch):
    with pytest.raises(ValueError, match="technical_reference.*status"):
        _registry(tmp_path, monkeypatch, latex_status="")


def test_status_outside_the_vocabulary_is_rejected(tmp_path, monkeypatch):
    with pytest.raises(ValueError, match="'draft_pdf'"):
        _registry(tmp_path, monkeypatch, latex_status="status: draft_pdf")


def test_measures_source_must_not_declare_a_status(tmp_path, monkeypatch):
    with pytest.raises(ValueError, match="upgrade_measures.*must not set status"):
        _registry(tmp_path, monkeypatch, measures_status="status: site_page")


def test_the_real_registry_loads():
    """The checked-in registry for this release must satisfy its own rules."""
    reg = R.load_registry("comstock", RELEASE)
    assert reg.by_id("technical_reference").status == "site_page"
    assert reg.by_id("github_site").status == "site_page"
    assert reg.by_id("upgrade_measures").status is None
    # The two site-served measure PDFs land beside the site-served measure pages.
    remap = reg.by_id("upgrade_measures").output_remap
    assert remap["assets/files"] == remap["docs/upgrade_measures"]
    # Both site-backed sources name the same live site; the reference chapters name one PDF.
    site = reg.by_id("github_site").site_url
    assert site == reg.by_id("upgrade_measures").site_url == "https://natlabrockies.github.io/ComStock.github.io"
    assert reg.by_id("technical_reference").publication_url == (
        f"{site}/assets/files/comstock_reference_documentation_2025_3.pdf"
    )


def test_canonical_and_exclude_urls_are_loaded_and_checked(tmp_path, monkeypatch):
    reg = _registry(
        tmp_path, monkeypatch,
        measures_link=(
            "site_url: https://example.org/site\n"
            "    canonical_urls:\n"
            '      "https://www.example.org/a.pdf": "https://docs.example.org/a.pdf"\n'
            "    exclude_urls:\n"
            "      - https://www.example.org/slides.pdf"
        ),
    )
    um = reg.by_id("upgrade_measures")
    assert um.canonical_urls == {"https://www.example.org/a.pdf": "https://docs.example.org/a.pdf"}
    assert um.exclude_urls == ["https://www.example.org/slides.pdf"]


def test_canonical_url_chains_and_self_maps_are_rejected(tmp_path, monkeypatch):
    with pytest.raises(ValueError, match="not itself an alias"):
        _registry(tmp_path, monkeypatch, measures_link=(
            "site_url: https://example.org/site\n"
            "    canonical_urls:\n"
            '      "https://a.example.org/x.pdf": "https://b.example.org/x.pdf"\n'
            '      "https://b.example.org/x.pdf": "https://c.example.org/x.pdf"'
        ))


def test_exclude_urls_must_be_absolute_https(tmp_path, monkeypatch):
    with pytest.raises(ValueError, match="exclude_urls.*absolute https"):
        _registry(tmp_path, monkeypatch, measures_link=(
            "site_url: https://example.org/site\n"
            "    exclude_urls:\n"
            "      - assets/files/slides.pdf"
        ))


def test_the_real_registry_excludes_the_four_webinar_decks_and_canonicalises_92504():
    um = R.load_registry("comstock", RELEASE).by_id("upgrade_measures")
    assert sorted(u.rsplit("/", 1)[-1] for u in um.exclude_urls) == ["85853.pdf", "87746.pdf", "89653.pdf", "92766.pdf"]
    assert um.canonical_urls == {
        "https://www.nlr.gov/docs/fy26osti/92504.pdf": "https://docs.nlr.gov/docs/fy26osti/92504.pdf"
    }
