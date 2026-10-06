"""The provenance header is the one piece of metadata that travels with a fetched file, and
the corpus version is the one field in it that distinguishes two builds of the same release.
These pin the header's shape (so old parsers that skip a leading comment still work), its
round trip, and the fallback version a non-release build gets.
"""

from __future__ import annotations

import subprocess

import pytest

from buildstock_corpus import provenance as P

RELEASE = "comstock_amy2018_2025_release_3"


def test_header_round_trips():
    line = P.render_header(
        "comstock", RELEASE, "upgrade_measures",
        "assets/files/ComStock Measure Doc_PV with Battery Storage.pdf", f"{RELEASE}-v1",
    )
    assert line.startswith("<!-- ") and line.endswith(" -->\n")
    assert "\n" not in line[:-1]  # one comment, one line
    assert P.parse_header(line) == {
        "product": "comstock",
        "release": RELEASE,
        "source_id": "upgrade_measures",
        "source_path": "assets/files/ComStock Measure Doc_PV with Battery Storage.pdf",
        "corpus_version": f"{RELEASE}-v1",
    }


def test_pre_version_header_parses_with_no_version():
    """Files from builds before the field existed are headers too, just unversioned."""
    old = f"<!-- comstock {RELEASE} | technical_reference | documentation/reference_doc/4_9_hvac.tex -->"
    parsed = P.parse_header(old)
    assert parsed is not None
    assert parsed["source_path"] == "documentation/reference_doc/4_9_hvac.tex"
    assert parsed["corpus_version"] is None


@pytest.mark.parametrize(
    "line",
    ["# HVAC Systems", "", "<!-- figure described by overlay: x -->", "<!-- comstock -->"],
)
def test_non_header_lines_are_rejected(line):
    assert P.parse_header(line) is None


def test_read_header_reads_only_the_first_line(tmp_path):
    f = tmp_path / "doc.md"
    f.write_text(
        P.render_header("comstock", RELEASE, "github_site", "docs/a.md", "abc1234")
        + "# Title\n\n<!-- not a header -->\n",
        encoding="utf-8",
        newline="\n",
    )
    assert P.read_header(f)["corpus_version"] == "abc1234"


def _git(*args, cwd):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=True)


def test_default_version_outside_a_repo_is_unknown(tmp_path):
    assert P.default_corpus_version(root=tmp_path) == P.UNKNOWN_VERSION


def test_default_version_is_the_short_hash_and_marks_a_dirty_tree(tmp_path):
    try:
        _git("init", "-q", cwd=tmp_path)
    except (OSError, subprocess.CalledProcessError):
        pytest.skip("git not available")
    _git("config", "user.email", "t@example.com", cwd=tmp_path)
    _git("config", "user.name", "t", cwd=tmp_path)
    (tmp_path / "a.txt").write_text("a\n", encoding="utf-8")
    _git("add", "a.txt", cwd=tmp_path)
    _git("commit", "-q", "-m", "init", cwd=tmp_path)
    sha = _git("rev-parse", "--short", "HEAD", cwd=tmp_path).stdout.strip()

    assert P.default_corpus_version(root=tmp_path) == sha

    (tmp_path / "a.txt").write_text("b\n", encoding="utf-8")  # tracked file modified
    assert P.default_corpus_version(root=tmp_path) == f"{sha}-dirty"

    # An untracked file is not "dirty": it cannot change what the build reads from git.
    (tmp_path / "a.txt").write_text("a\n", encoding="utf-8")
    (tmp_path / "scratch.txt").write_text("x\n", encoding="utf-8")
    assert P.default_corpus_version(root=tmp_path) == sha
