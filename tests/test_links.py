"""source_url and publication_url are pure string building from facts the build holds, and
they are written into every artifact as-is, so their shape is pinned here: GitHub file URLs
carry the commit sha (never a branch or tag), site pages swap .md for .html, repo paths
with spaces are percent-encoded, and an OSTI PDF is its own source and publication.
"""

from __future__ import annotations

import pytest

from buildstock_corpus import links as L
from buildstock_corpus.manifest import artifact_urls
from buildstock_corpus.registry import Source

SHA = "b77c60d341c9b68c58c5d51e51b06f08f293d3cb"
SITE = "https://natlabrockies.github.io/ComStock.github.io"


@pytest.mark.parametrize(
    "repo",
    [
        "https://github.com/NatLabRockies/ComStock.git",
        "https://github.com/NatLabRockies/ComStock",
        "https://github.com/NatLabRockies/ComStock/",
        "git@github.com:NatLabRockies/ComStock.git",
        "NatLabRockies/ComStock",
    ],
)
def test_repo_web_url_normalises_every_clone_spelling(repo):
    assert L.repo_web_url(repo) == "https://github.com/NatLabRockies/ComStock"


def test_repo_file_url_pins_the_commit_sha():
    url = L.repo_file_url(
        "https://github.com/NatLabRockies/ComStock.git", SHA, "documentation/reference_doc/4_4_geometry.tex"
    )
    assert url == (
        f"https://github.com/NatLabRockies/ComStock/blob/{SHA}/documentation/reference_doc/4_4_geometry.tex"
    )


def test_repo_file_url_without_a_sha_is_an_error():
    """A branch-named URL would move under the citation; refuse rather than fall back."""
    with pytest.raises(ValueError, match="no commit sha"):
        L.repo_file_url("https://github.com/NatLabRockies/ComStock.git", "", "docs/a.md")


def test_paths_with_spaces_are_percent_encoded_but_slashes_kept():
    url = L.site_file_url(SITE, "assets/files/ComStock Measure Doc_PV with Battery Storage.pdf")
    assert url == f"{SITE}/assets/files/ComStock%20Measure%20Doc_PV%20with%20Battery%20Storage.pdf"


def test_site_page_url_swaps_md_for_html():
    assert L.site_page_url(SITE, "docs/citation.md") == f"{SITE}/docs/citation.html"
    assert L.site_page_url(SITE + "/", "/docs/upgrade_measures/hvac_doas_mshp.md") == (
        f"{SITE}/docs/upgrade_measures/hvac_doas_mshp.html"
    )


@pytest.mark.parametrize("url,ok", [
    ("https://example.org/a.pdf", True),
    ("http://example.org/a.pdf", False),
    ("docs/a.html", False),
    ("https://", False),
    (None, False),
])
def test_is_absolute_https(url, ok):
    assert L.is_absolute_https(url) is ok


# --- artifact_urls: the per-document resolution the manifest uses -------------------------

CLONE = {"repo": "https://github.com/NatLabRockies/ComStock.github.io.git", "sha": SHA,
         "dest": "repos/ComStock.github.io@2025_3"}
MEASURES = Source(id="upgrade_measures", type="measures", repo=CLONE["repo"], git_ref="2025_3",
                  index_page="i.md", internal_dir="d", crosswalk_csv="c.csv", site_url=SITE)
LATEX = Source(id="technical_reference", type="latex", repo="https://github.com/NatLabRockies/ComStock.git",
               git_ref="2025-3", doc_glob="**/*.tex", latex_main="main.tex", status="site_page",
               publication_url=f"{SITE}/assets/files/comstock_reference_documentation_2025_3.pdf")
STATE = {"external_pdfs": [{"url": "https://docs.nlr.gov/docs/fy25osti/95002.pdf",
                            "path": "measure_pdfs/95002.pdf", "sha256": "x", "status": "ok"}]}


def test_osti_pdf_is_its_own_source_and_publication():
    src, pub = artifact_urls("measure_pdfs/95002.pdf", MEASURES, STATE, CLONE)
    assert src == pub == "https://docs.nlr.gov/docs/fy25osti/95002.pdf"


def test_site_page_source_is_the_file_at_the_commit_and_publication_the_live_page():
    src, pub = artifact_urls("docs/upgrade_measures/env_window_film.md", MEASURES, STATE, CLONE)
    assert src == f"https://github.com/NatLabRockies/ComStock.github.io/blob/{SHA}/docs/upgrade_measures/env_window_film.md"
    assert pub == f"{SITE}/docs/upgrade_measures/env_window_film.html"


def test_site_served_pdf_publication_is_the_file_the_site_serves():
    path = "assets/files/ComStock Measure Doc_PV with Battery Storage.pdf"
    src, pub = artifact_urls(path, MEASURES, STATE, CLONE)
    assert src.endswith(f"/blob/{SHA}/assets/files/ComStock%20Measure%20Doc_PV%20with%20Battery%20Storage.pdf")
    assert pub == f"{SITE}/assets/files/ComStock%20Measure%20Doc_PV%20with%20Battery%20Storage.pdf"


def test_latex_chapters_all_point_at_the_one_reference_pdf():
    clone = {"repo": LATEX.repo, "sha": SHA, "dest": "repos/ComStock@2025-3"}
    for chapter in ("documentation/reference_doc/4_4_geometry.tex", "documentation/reference_doc/4_9_hvac.tex"):
        src, pub = artifact_urls(chapter, LATEX, {}, clone)
        assert src == f"https://github.com/NatLabRockies/ComStock/blob/{SHA}/{chapter}"
        assert pub == LATEX.publication_url


def test_clone_sourced_document_without_a_clone_record_is_an_error():
    with pytest.raises(ValueError, match="no clone record"):
        artifact_urls("docs/a.md", MEASURES, STATE, None)
