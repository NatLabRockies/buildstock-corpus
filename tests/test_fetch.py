"""`bsc fetch` clone handling: an existing clone must follow its ref.

Exercised against a real local bare repository rather than a mocked `git`, because the
behaviour under test is git's: a branch ref must land on the remote tip when the clone
already exists on disk, a tag ref must resolve to the same commit as before, and the
blobless filter and the sparse-checkout set must survive the move. The v3 release
(2026-10-16) had to `git pull --ff-only` the site clone by hand before fetching; these
tests pin that this is no longer needed.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

from buildstock_corpus.fetch import Clone, _ensure_clone

WHEN = "2026-01-01T00:00:00+00:00"


def git(repo: Path, *args: str) -> str:
    out = subprocess.run(
        ["git", "-C", str(repo), "-c", "user.name=T", "-c", "user.email=t@e", *args],
        check=True,
        capture_output=True,
        text=True,
        env={**os.environ, "GIT_AUTHOR_DATE": WHEN, "GIT_COMMITTER_DATE": WHEN},
    )
    return out.stdout.strip()


def commit(work: Path, rel: str, text: str) -> str:
    """Write `rel`, commit it on the current branch, push, and return the new commit sha."""
    path = work / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    git(work, "add", rel)
    git(work, "commit", "-q", "-m", rel)
    git(work, "push", "-q", "origin", "HEAD")
    return git(work, "rev-parse", "HEAD")


def remote_with_tag(tmp_path: Path) -> tuple[Path, Path, str]:
    """A bare 'origin' holding `main` with two commits, the first tagged `2025-3`.

    Mirrors the registry's two kinds of ref: the ComStock code repo pinned at a tag and
    the ComStock.github.io site read at a moving branch. Returns the bare repo, the work
    tree that pushes to it, and the tagged commit.
    """
    origin = tmp_path / "origin.git"
    origin.mkdir()
    git(origin, "init", "-q", "--bare", "--initial-branch=main")
    # Partial-clone filters are a server-side opt-in; GitHub allows them, a local bare
    # repo has to be told to.
    git(origin, "config", "uploadpack.allowFilter", "true")

    work = tmp_path / "work"
    work.mkdir()
    git(work, "init", "-q", "--initial-branch=main")
    git(work, "remote", "add", "origin", str(origin))
    first = commit(work, "docs/page.md", "v1")
    commit(work, "other/skip.md", "not in the sparse set")
    git(work, "tag", "2025-3", first)
    git(work, "push", "-q", "origin", "2025-3")
    return origin, work, first


def site_clone(origin: Path, ref: str) -> Clone:
    return Clone(repo=str(origin), git_ref=ref, sparse=["docs"], name=f"origin@{ref}")


def assert_blobless_and_sparse(dest: Path) -> None:
    assert git(dest, "config", "remote.origin.partialclonefilter") == "blob:none"
    assert git(dest, "config", "remote.origin.promisor") == "true"
    assert git(dest, "sparse-checkout", "list").splitlines() == ["docs"]
    assert (dest / "docs" / "page.md").is_file()
    assert not (dest / "other").exists()


def test_fresh_clone_of_a_branch_is_blobless_sparse_and_at_the_tip(tmp_path):
    origin, work, _ = remote_with_tag(tmp_path)
    tip = git(work, "rev-parse", "HEAD")
    repos = tmp_path / "repos"
    repos.mkdir()

    clone = site_clone(origin, "main")
    _ensure_clone(clone, repos)

    assert clone.sha == tip
    assert_blobless_and_sparse(repos / clone.name)


def test_existing_branch_clone_advances_to_the_remote_tip(tmp_path):
    """Finding 4: a clone left from an earlier fetch must not pin yesterday's `main`."""
    origin, work, _ = remote_with_tag(tmp_path)
    repos = tmp_path / "repos"
    repos.mkdir()
    first_run = site_clone(origin, "main")
    _ensure_clone(first_run, repos)
    dest = repos / first_run.name

    commit(work, "docs/new_page.md", "posted after the first fetch")
    new_tip = commit(work, "other/also_skip.md", "still outside the sparse set")

    second_run = site_clone(origin, "main")
    _ensure_clone(second_run, repos)

    assert first_run.sha != new_tip
    assert second_run.sha == new_tip
    assert (dest / "docs" / "new_page.md").read_text(encoding="utf-8") == (
        "posted after the first fetch"
    )
    assert_blobless_and_sparse(dest)


def test_existing_tag_clone_stays_on_the_tagged_commit(tmp_path):
    """A tag ref is a fixed pin: moving `main` underneath it must change nothing."""
    origin, work, tagged = remote_with_tag(tmp_path)
    repos = tmp_path / "repos"
    repos.mkdir()
    first_run = site_clone(origin, "2025-3")
    _ensure_clone(first_run, repos)
    assert first_run.sha == tagged

    commit(work, "docs/later.md", "on main, not under the tag")

    second_run = site_clone(origin, "2025-3")
    _ensure_clone(second_run, repos)

    assert second_run.sha == tagged
    dest = repos / second_run.name
    assert not (dest / "docs" / "later.md").exists()
    assert_blobless_and_sparse(dest)


def test_sparse_set_widened_by_the_registry_is_applied_to_an_existing_clone(tmp_path):
    origin, _, _ = remote_with_tag(tmp_path)
    repos = tmp_path / "repos"
    repos.mkdir()
    _ensure_clone(site_clone(origin, "main"), repos)

    wider = Clone(
        repo=str(origin), git_ref="main", sparse=["docs", "other"], name="origin@main"
    )
    _ensure_clone(wider, repos)

    dest = repos / wider.name
    assert sorted(git(dest, "sparse-checkout", "list").splitlines()) == ["docs", "other"]
    assert (dest / "other" / "skip.md").is_file()


def test_shallow_clone_left_by_an_old_fetch_is_deepened_and_moved(tmp_path):
    """Both repairs at once: full history for doc dates, and the remote tip."""
    origin, work, _ = remote_with_tag(tmp_path)
    repos = tmp_path / "repos"
    repos.mkdir()
    dest = repos / "origin@main"
    # `--depth` is ignored for a plain-path local clone; a file:// URL goes through the
    # transport and honours it, which is what a clone of GitHub did.
    subprocess.run(
        [
            "git", "clone", "-q", "--depth", "1", "--branch", "main",
            "--filter=blob:none", origin.as_uri(), str(dest),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    assert git(dest, "rev-parse", "--is-shallow-repository") == "true"
    new_tip = commit(work, "docs/new_page.md", "after the shallow clone")

    clone = site_clone(origin, "main")
    _ensure_clone(clone, repos)

    assert clone.sha == new_tip
    assert git(dest, "rev-parse", "--is-shallow-repository") == "false"
    assert git(dest, "sparse-checkout", "list").splitlines() == ["docs"]
