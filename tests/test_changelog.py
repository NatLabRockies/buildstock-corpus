"""`bsc changelog`: release notes computed from two manifests.

The diff is exercised on hand-built manifests with the body-hash lookups injected, so
every bucket (added, removed, source changed, overlay changed, re-rendered, unchanged,
gaps, exclusions, tooling) is pinned without a corpus. The git-backed reader is then
exercised against a real repository with a tagged commit, because that path -- reading a
manifest and an artifact body out of a ref -- is what the first changelog (v1 → v2) rests
on, v1 having recorded no body hash.
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

import pytest

import buildstock_corpus.changelog as C
from buildstock_corpus.provenance import body_sha256, body_sha256_file

RELEASE = "comstock_amy2018_2025_release_3"
PUB = "https://www.nlr.gov/docs/fy26osti/99999.pdf"


def row(
    source_path: str,
    *,
    input_sha: str = "in-1",
    body: str = "body-1",
    version: str = "v1",
    overlay: dict | None = None,
    status: str = "osti_pdf",
    title: str = "Some Report",
    record_body: bool = True,
) -> dict:
    """One manifest artifact row; output hash folds in the version, as a real header would."""
    r = {
        "source_path": source_path,
        "source_type": "pdf",
        "status": status,
        "source_url": f"https://example.org/{source_path}",
        "publication_url": PUB,
        "corpus_version": version,
        "title": title,
        "input_sha256": input_sha,
        "output_path": f"upgrade_measures/{source_path}".replace(".pdf", ".md"),
        "output_sha256": f"out-{version}-{body}",
    }
    if record_body:
        r["body_sha256"] = body
    if overlay:
        r["overlay"] = overlay
    return r


def manifest(rows: list[dict], *, version: str, gaps=(), excluded=(), tooling=None, chunks=10) -> dict:
    return {
        "product": "comstock",
        "release": RELEASE,
        "corpus_version": version,
        "generated_utc": "2026-10-20T12:00:00+00:00",
        "tooling": tooling or {"pipeline": "0.1.0", "pandoc": "3.9"},
        "sources": [{"id": "upgrade_measures", "type": "measures", "artifacts": rows}],
        "counts": {"documents": len(rows), "chunks": chunks},
        "crosswalk": {"counts": {"measures": 65, "covered": 65 - len(gaps), "gaps": len(gaps)}},
        "gaps": {"measures": list(gaps), "excluded_by_registry": list(excluded)},
    }


def recorded(_sid: str, r: dict) -> str | None:
    """A resolver that trusts the row; None for a row without the field (the v1 case)."""
    return r.get("body_sha256")


# --------------------------------------------------------------------------- the diff


def test_every_bucket_is_classified():
    old = manifest(
        [
            row("measure_pdfs/1.pdf"),  # unchanged body, new header -> unchanged
            row("measure_pdfs/2.pdf", input_sha="in-2"),  # upstream revises it
            row("measure_pdfs/3.pdf", overlay={"path": "o3.yaml", "sha256": "ov-a"}),
            row("measure_pdfs/4.pdf"),  # overlay gets added
            row("measure_pdfs/5.pdf"),  # re-rendered by a tooling change
            row("measure_pdfs/6.pdf"),  # removed
        ],
        version="v1",
        gaps=["dr_0004", "dr_0007"],
        excluded=[{"source_id": "upgrade_measures", "path": "measure_pdfs/85853.pdf", "url": "u"}],
    )
    new = manifest(
        [
            row("measure_pdfs/1.pdf", version="v2"),
            row("measure_pdfs/2.pdf", input_sha="in-2b", version="v2", body="body-2b"),
            row("measure_pdfs/3.pdf", version="v2", overlay={"path": "o3.yaml", "sha256": "ov-b"}),
            row("measure_pdfs/4.pdf", version="v2", overlay={"path": "o4.yaml", "sha256": "ov-c"}),
            row("measure_pdfs/5.pdf", version="v2", body="body-5-rerendered"),
            row("measure_pdfs/7.pdf", version="v2", title="Known Issues"),  # added
        ],
        version="v2",
        gaps=["dr_0007", "pkg_0099"],
        tooling={"pipeline": "0.1.0", "pandoc": "3.10"},
        chunks=12,
    )

    log = C.diff_manifests(old, new, recorded, recorded)

    paths = lambda items: [r["source_path"] for _, r, *_ in items]  # noqa: E731
    assert paths(log.added) == ["measure_pdfs/7.pdf"]
    assert paths(log.removed) == ["measure_pdfs/6.pdf"]
    assert paths(log.source_changed) == ["measure_pdfs/2.pdf"]
    assert [(r["source_path"], what) for _, r, what in log.overlay_changed] == [
        ("measure_pdfs/3.pdf", "overlay changed"),
        ("measure_pdfs/4.pdf", "overlay added"),
    ]
    assert paths(log.rerendered) == ["measure_pdfs/5.pdf"]
    assert log.unchanged == 1
    assert log.document_changes == 6
    assert log.gaps_closed == ["dr_0004"] and log.gaps_opened == ["pkg_0099"]
    assert [e["path"] for e in log.no_longer_excluded] == ["measure_pdfs/85853.pdf"]
    assert log.tooling == [("pandoc", "3.9", "3.10")]
    assert log.old_version == "v1" and log.new_version == "v2" and log.new_date == "2026-10-20"


def test_source_change_outranks_overlay_and_body():
    """A revised source is reported once, as such, whatever else moved with it."""
    old = manifest([row("a.pdf", overlay={"path": "o", "sha256": "x"})], version="v1")
    new = manifest(
        [row("a.pdf", input_sha="in-9", body="b9", version="v2", overlay={"path": "o", "sha256": "y"})],
        version="v2",
    )
    log = C.diff_manifests(old, new, recorded, recorded)
    assert len(log.source_changed) == 1 and not log.overlay_changed and not log.rerendered


def test_identical_output_hash_never_consults_the_body():
    """A byte-identical artifact (same corpus_version, e.g. --to a sibling ref) is unchanged."""
    old = manifest([row("a.pdf", record_body=False)], version="v1")
    new = manifest([row("a.pdf", record_body=False)], version="v1")

    def boom(_sid, _row):
        raise AssertionError("body resolver must not be called")

    log = C.diff_manifests(old, new, boom, boom)
    assert log.unchanged == 1 and log.document_changes == 0


def test_unreadable_body_is_an_error_not_a_guess():
    old = manifest([row("a.pdf", record_body=False)], version="v1")
    new = manifest([row("a.pdf", version="v2")], version="v2")
    with pytest.raises(C.ChangelogError, match="old side"):
        C.diff_manifests(old, new, recorded, recorded)


# --------------------------------------------------------------------------- rendering


def test_render_lists_an_added_document_by_path_with_its_link():
    """The plan's acceptance check: a release body names the added known-issues doc by path."""
    old = manifest([row("measure_pdfs/1.pdf")], version="v1")
    new = manifest(
        [row("measure_pdfs/1.pdf", version="v2"), row("known_issues/ki.pdf", version="v2", title="Known Issues")],
        version="v2",
    )
    text = C.render(C.diff_manifests(old, new, recorded, recorded), from_ref="tag-v1")

    assert text.startswith("## v2 — 2026-10-20\n")
    assert "Changes since `tag-v1` (corpus_version `v1`): 2 documents (+1)" in text
    assert "### Added" in text
    assert "- `upgrade_measures/known_issues/ki.pdf` → `upgrade_measures/known_issues/ki.md` (osti_pdf): Known Issues — " + PUB in text
    assert "### Changed" not in text and "### Removed" not in text


def test_render_collapses_many_rerendered_documents_to_a_count():
    n = C.LIST_RERENDERED_UP_TO + 5
    old = manifest([row(f"m/{i}.pdf") for i in range(n)], version="v1")
    new = manifest([row(f"m/{i}.pdf", version="v2", body=f"b{i}") for i in range(n)], version="v2")
    text = C.render(C.diff_manifests(old, new, recorded, recorded), from_ref="v1")

    assert f"- {n} documents re-rendered from unchanged sources and overlays (tooling change; upgrade_measures {n})." in text
    assert "m/0.pdf" not in text  # not listed one by one


def test_render_lists_few_rerendered_documents_individually():
    old = manifest([row("m/1.pdf"), row("m/2.pdf")], version="v1")
    new = manifest([row("m/1.pdf", version="v2", body="x"), row("m/2.pdf", version="v2")], version="v2")
    text = C.render(C.diff_manifests(old, new, recorded, recorded), from_ref="v1")
    assert "- `upgrade_measures/m/1.pdf` → `upgrade_measures/m/1.md` (osti_pdf): Some Report — re-rendered from an unchanged source." in text
    assert "m/2.pdf" not in text


def test_render_with_nothing_changed_says_so():
    old = manifest([row("m/1.pdf")], version="v1")
    new = manifest([row("m/1.pdf", version="v2")], version="v2")
    text = C.render(C.diff_manifests(old, new, recorded, recorded), from_ref="v1")
    assert "No document-level changes." in text


# --------------------------------------------------------------------------- appending


PREAMBLE = "# Changelog\n\nOne entry per tagged build.\n\n"
V1_ENTRY = "## v1 — 2026-10-08\n\nFirst tagged build.\n"


def test_append_inserts_above_the_newest_entry(tmp_path):
    path = tmp_path / "CHANGELOG.md"
    path.write_text(PREAMBLE + V1_ENTRY, encoding="utf-8")
    entry = "## v2 — 2026-10-20\n\nSecond build.\n"

    C.append_entry(entry, path)

    assert path.read_text(encoding="utf-8") == PREAMBLE + entry + "\n" + V1_ENTRY


def test_append_refuses_a_duplicate_heading(tmp_path):
    path = tmp_path / "CHANGELOG.md"
    path.write_text(PREAMBLE + V1_ENTRY, encoding="utf-8")
    with pytest.raises(C.ChangelogError, match="already has an entry"):
        C.append_entry("## v1 — 2026-10-08\n\nagain\n", path)
    assert path.read_text(encoding="utf-8") == PREAMBLE + V1_ENTRY


def test_append_to_a_file_with_no_entries_yet(tmp_path):
    path = tmp_path / "CHANGELOG.md"
    path.write_text("# Changelog\n", encoding="utf-8")
    C.append_entry("## v1 — d\n\nx\n", path)
    assert path.read_text(encoding="utf-8") == "# Changelog\n\n## v1 — d\n\nx\n"


# --------------------------------------------------------------------------- body hashes


def test_body_hash_ignores_only_the_header_line(tmp_path):
    a = tmp_path / "a.md"
    b = tmp_path / "b.md"
    a.write_text("<!-- header v1 -->\n# T\n\nbody\n", encoding="utf-8", newline="\n")
    b.write_text("<!-- header v2 -->\n# T\n\nbody\n", encoding="utf-8", newline="\n")
    assert body_sha256_file(a) == body_sha256_file(b)
    assert body_sha256_file(a) != body_sha256(b"<!-- header v1 -->\n# T\n\nbody changed\n")
    assert body_sha256(b"<!-- header only, no newline -->") == body_sha256(b"\n")


# --------------------------------------------------------------------------- git-backed


def git(repo: Path, *args: str) -> None:
    env = {
        **os.environ,
        "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org",
        "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.org",
    }
    subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True, env=env)


def test_manifest_and_bodies_are_read_from_the_tagged_ref(tmp_path, monkeypatch):
    """v1 recorded no body hash, so its side is hashed from the files git has at the tag."""
    repo = tmp_path / "repo"
    rel = Path("processed") / "comstock" / RELEASE
    (repo / rel / "upgrade_measures" / "m").mkdir(parents=True)
    doc = repo / rel / "upgrade_measures" / "m" / "1.md"
    doc.write_text("<!-- comstock x | upgrade_measures | m/1.pdf | corpus_version: v1 -->\n# T\n\nold body\n", encoding="utf-8", newline="\n")
    old = manifest([row("m/1.pdf", record_body=False)], version="v1")
    (repo / rel / "manifest.json").write_text(json.dumps(old), encoding="utf-8", newline="\n")
    git(repo, "init", "-q")
    git(repo, "add", ".")
    git(repo, "commit", "-q", "-m", "v1")
    git(repo, "tag", "tag-v1")

    # The working tree moves on: same source, body re-rendered, manifest now records it.
    doc.write_text("<!-- comstock x | upgrade_measures | m/1.pdf | corpus_version: v2 -->\n# T\n\nnew body\n", encoding="utf-8", newline="\n")
    new = manifest([row("m/1.pdf", version="v2", body=body_sha256_file(doc))], version="v2")
    (repo / rel / "manifest.json").write_text(json.dumps(new), encoding="utf-8", newline="\n")

    monkeypatch.setattr(C, "PROJECT_ROOT", repo)
    monkeypatch.setattr(C, "PROCESSED_DIR", repo / "processed")
    monkeypatch.setattr(C, "processed_root", lambda p, r: repo / rel)
    monkeypatch.setattr(C, "manifest_file", lambda p, r: repo / rel / "manifest.json")

    assert C.load_manifest_at("tag-v1", "comstock", RELEASE, repo)["corpus_version"] == "v1"
    log, text = C.changelog("comstock", RELEASE, "tag-v1", root=repo)
    assert [r["source_path"] for _, r in log.rerendered] == ["m/1.pdf"]
    assert "re-rendered from an unchanged source" in text

    # A header-only change leaves the body hash alone: unchanged, even across versions.
    doc.write_text("<!-- comstock x | upgrade_measures | m/1.pdf | corpus_version: v2 -->\n# T\n\nold body\n", encoding="utf-8", newline="\n")
    new = manifest([row("m/1.pdf", version="v2", body=body_sha256_file(doc))], version="v2")
    (repo / rel / "manifest.json").write_text(json.dumps(new), encoding="utf-8", newline="\n")
    log, _ = C.changelog("comstock", RELEASE, "tag-v1", root=repo)
    assert log.unchanged == 1 and not log.rerendered

    with pytest.raises(C.ChangelogError, match="no processed/"):
        C.load_manifest_at("no-such-ref", "comstock", RELEASE, repo)


# --------------------------------------------------------------------------- --show


def test_entry_for_returns_the_body_of_one_entry(tmp_path):
    path = tmp_path / "CHANGELOG.md"
    path.write_text(
        PREAMBLE + "## v2 — 2026-10-20\n\nSecond build.\n\n### Added\n\n- a doc\n\n" + V1_ENTRY,
        encoding="utf-8",
    )
    assert C.entry_for("v2", path) == "Second build.\n\n### Added\n\n- a doc\n"
    assert C.entry_for("v1", path) == "First tagged build.\n"  # the last entry runs to EOF


def test_entry_for_refuses_a_version_without_notes(tmp_path):
    path = tmp_path / "CHANGELOG.md"
    path.write_text(PREAMBLE + V1_ENTRY, encoding="utf-8")
    with pytest.raises(C.ChangelogError, match="no entry for 'v2'"):
        C.entry_for("v2", path)
    # A version that is a prefix of another is not a match.
    with pytest.raises(C.ChangelogError):
        C.entry_for("v", path)
