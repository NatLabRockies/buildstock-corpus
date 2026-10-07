"""The provenance header is the one piece of metadata that travels with a fetched file, so
its shape is pinned here: one HTML comment on one line, three positional segments, then
labelled fields in a fixed order; a header from before a field existed still parses with
that field None; and the fallback version a non-release build gets.
"""

from __future__ import annotations

import subprocess

import pytest

from buildstock_corpus import provenance as P

RELEASE = "comstock_amy2018_2025_release_3"
SITE = "https://natlabrockies.github.io/ComStock.github.io"
FIELDS = dict(
    status="site_page",
    source_url="https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551/assets/files/ComStock%20Measure%20Doc_PV%20with%20Battery%20Storage.pdf",
    publication_url=f"{SITE}/assets/files/ComStock%20Measure%20Doc_PV%20with%20Battery%20Storage.pdf",
    corpus_version=f"{RELEASE}-v1",
)


def test_header_round_trips_every_field():
    line = P.render_header(
        "comstock", RELEASE, "upgrade_measures",
        "assets/files/ComStock Measure Doc_PV with Battery Storage.pdf", **FIELDS,
    )
    assert line.startswith("<!-- ") and line.endswith(" -->\n")
    assert "\n" not in line[:-1]  # one comment, one line
    assert P.parse_header(line) == {
        "product": "comstock",
        "release": RELEASE,
        "source_id": "upgrade_measures",
        "source_path": "assets/files/ComStock Measure Doc_PV with Battery Storage.pdf",
        **FIELDS,
    }


def test_fields_are_written_in_a_fixed_order():
    line = P.render_header("comstock", RELEASE, "github_site", "docs/a.md", **FIELDS)
    body = line[len("<!-- "):-len(" -->\n")]
    assert body.split(" | ") == [
        f"comstock {RELEASE}", "github_site", "docs/a.md",
        f"status: {FIELDS['status']}", f"source_url: {FIELDS['source_url']}",
        f"publication_url: {FIELDS['publication_url']}", f"corpus_version: {FIELDS['corpus_version']}",
    ]


def test_none_fields_are_omitted_not_written_as_none():
    line = P.render_header("comstock", RELEASE, "github_site", "docs/a.md", corpus_version="abc1234")
    assert "None" not in line
    parsed = P.parse_header(line)
    assert parsed["corpus_version"] == "abc1234"
    assert parsed["status"] is parsed["source_url"] is parsed["publication_url"] is None


def test_unknown_field_and_unsafe_value_are_errors():
    with pytest.raises(ValueError, match="unknown header field"):
        P.render_header("comstock", RELEASE, "s", "p", licence="x")
    with pytest.raises(ValueError, match="cannot contain"):
        P.render_header("comstock", RELEASE, "s", "p", status="a | b")


def test_pre_field_headers_still_parse():
    """Files from builds before each field existed are headers too, just missing it."""
    oldest = f"<!-- comstock {RELEASE} | technical_reference | documentation/reference_doc/4_9_hvac.tex -->"
    parsed = P.parse_header(oldest)
    assert parsed["source_path"] == "documentation/reference_doc/4_9_hvac.tex"
    assert all(parsed[k] is None for k in P.HEADER_FIELDS)

    version_only = oldest[:-4] + " | corpus_version: 76f3d84 -->"
    parsed = P.parse_header(version_only)
    assert parsed["corpus_version"] == "76f3d84" and parsed["status"] is None


@pytest.mark.parametrize(
    "line",
    [
        "# HVAC Systems",
        "",
        "<!-- figure described by overlay: x -->",
        "<!-- comstock -->",
        f"<!-- comstock {RELEASE} | s | p | not-a-field -->",  # unlabelled trailing segment
    ],
)
def test_non_header_lines_are_rejected(line):
    assert P.parse_header(line) is None


def test_read_header_reads_only_the_first_line(tmp_path):
    f = tmp_path / "doc.md"
    f.write_text(
        P.render_header("comstock", RELEASE, "github_site", "docs/a.md", corpus_version="abc1234")
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
