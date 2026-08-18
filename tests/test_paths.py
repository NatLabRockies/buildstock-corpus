"""Output-path mapping: processed/ layout mirrors source paths unless a source remaps a dir.

Also covers the --work-dir sandbox: derived outputs move, inputs and caches do not.
"""

import pytest

from buildstock_corpus.paths import (
    INDEX_DIR,
    PROCESSED_DIR,
    index_root,
    output_rel,
    processed_root,
    raw_root,
    remap_dir,
    sources_file,
    use_workspace,
)

RELEASE = "comstock_amy2018_2025_release_3"

REMAP = {
    "docs/upgrade_measures": "unpublished_docs/upgrade_measures",
    "assets": "draft_publications",
}


def test_output_mirrors_source_path_without_remap():
    assert (
        output_rel("github_site", "docs/upgrades/hvac.md")
        == "github_site/docs/upgrades/hvac.md"
    )


def test_source_extension_is_replaced_with_md():
    assert output_rel("upgrade_measures", "measure_pdfs/89040.pdf") == (
        "upgrade_measures/measure_pdfs/89040.md"
    )


def test_remap_rewrites_nested_source_dir():
    assert output_rel("upgrade_measures", "docs/upgrade_measures/env_window_film.md", REMAP) == (
        "upgrade_measures/unpublished_docs/upgrade_measures/env_window_film.md"
    )


def test_remap_rewrites_single_segment_source_dir():
    assert output_rel("upgrade_measures", "assets/files/ComStock Measure Doc.pdf", REMAP) == (
        "upgrade_measures/draft_publications/files/ComStock Measure Doc.md"
    )


def test_remap_leaves_paths_outside_every_remapped_dir_alone():
    assert output_rel("upgrade_measures", "measure_pdfs/89040.pdf", REMAP) == (
        "upgrade_measures/measure_pdfs/89040.md"
    )


def test_remap_respects_path_segment_boundary():
    """"docs/upgrade_measures_notes/" must not match the "docs/upgrade_measures" prefix."""
    assert output_rel("upgrade_measures", "docs/upgrade_measures_notes/x.md", REMAP) == (
        "upgrade_measures/docs/upgrade_measures_notes/x.md"
    )
    assert remap_dir("assets_archive/files", REMAP) == "assets_archive/files"


def test_longest_matching_prefix_wins():
    """A dir remap must not be shadowed by a shorter prefix that also matches."""
    remap = {"assets": "draft_publications", "assets/files": "draft_publications/pdfs"}
    assert remap_dir("assets/files/doc.pdf", remap) == "draft_publications/pdfs/doc.pdf"
    assert remap_dir("assets/images/fig.png", remap) == "draft_publications/images/fig.png"


def test_remap_applies_to_image_dirs_not_just_docs():
    """Image dirs travel with their .md file, so relative refs keep resolving."""
    assert remap_dir("assets/files/ComStock_Measure_Doc_images", REMAP) == (
        "draft_publications/files/ComStock_Measure_Doc_images"
    )
    assert remap_dir("docs/upgrade_measures/media", REMAP) == (
        "unpublished_docs/upgrade_measures/media"
    )


def test_remap_tolerates_trailing_slashes():
    remap = {"docs/upgrade_measures/": "unpublished_docs/upgrade_measures/"}
    assert output_rel("upgrade_measures", "docs/upgrade_measures/env_window_film.md", remap) == (
        "upgrade_measures/unpublished_docs/upgrade_measures/env_window_film.md"
    )


@pytest.fixture
def workspace(tmp_path):
    """Activate a sandbox root, always restoring the project defaults afterwards."""
    use_workspace(tmp_path)
    yield tmp_path
    use_workspace(None)


def test_workspace_redirects_derived_outputs(workspace):
    assert processed_root("comstock", RELEASE) == workspace / "processed" / "comstock" / RELEASE
    assert index_root("comstock", RELEASE) == workspace / "index" / f"comstock-{RELEASE}"


def test_workspace_leaves_inputs_alone(workspace):
    """raw/ and sources/ are inputs — a sandbox reuses them instead of re-fetching."""
    assert raw_root("comstock", RELEASE) == PROCESSED_DIR.parent / "raw" / "comstock" / RELEASE
    assert sources_file("comstock", RELEASE).parent == PROCESSED_DIR.parent / "sources"


def test_workspace_can_be_cleared(workspace):
    use_workspace(None)
    assert processed_root("comstock", RELEASE) == PROCESSED_DIR / "comstock" / RELEASE
    assert index_root("comstock", RELEASE) == INDEX_DIR / f"comstock-{RELEASE}"
