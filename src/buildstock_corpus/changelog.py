"""Release notes computed from two builds' manifests (`bsc changelog --from <tag>`).

Every manifest row carries three hashes: the source input, the whole output file, and
the output body without its line-1 header (see provenance.body_sha256). Diffing two
manifests row by row, keyed on `source_id/source_path` (the citation anchor), gives the
document-level part of a release's notes without anyone re-reading the corpus:

  * added / removed       -- the key is in one manifest only;
  * source changed        -- `input_sha256` moved: upstream revised the document;
  * overlay changed       -- the hand-authored sidecar moved, was added or removed;
  * re-rendered           -- input and overlay unchanged, body changed: a tooling change;
  * unchanged             -- body identical, even though the header (and so
                             `output_sha256`) names a new build.

Manifests from before `body_sha256` existed (the v1 tag) are diffed by reading the files
themselves out of git at that ref, so the first changelog does not have to wait for a
second tagged build that records the hash.

The old side is always read from git (`git show <ref>:<path>`); the new side is the
working tree by default, which is where a freshly built release sits when its notes are
written, or a second ref. What the manifest cannot know -- *why* 65 documents were
re-rendered -- is left for a hand-written bullet above the generated list.
"""

from __future__ import annotations

import json
import subprocess
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path

from .paths import PROCESSED_DIR, PROJECT_ROOT, manifest_file, processed_root
from .provenance import body_sha256, body_sha256_file

Key = tuple[str, str]  # (source_id, source_path)
# Resolves a row's body hash on one side of the diff; None when the artifact cannot be read.
BodyHashFn = Callable[[str, dict], str | None]

CHANGELOG_FILENAME = "CHANGELOG.md"
# Above this many, re-rendered documents are summarized per source rather than listed:
# a tooling change touches most of the corpus, and 65 identical bullets say nothing.
LIST_RERENDERED_UP_TO = 10


class ChangelogError(RuntimeError):
    """A manifest or artifact needed for the diff could not be read."""


@dataclass
class Changelog:
    """The computed difference between two builds, in the order the notes render it."""

    old_version: str
    new_version: str
    new_date: str  # YYYY-MM-DD of the new build, from its manifest's generated_utc
    added: list[tuple[str, dict]] = field(default_factory=list)
    removed: list[tuple[str, dict]] = field(default_factory=list)
    source_changed: list[tuple[str, dict]] = field(default_factory=list)
    overlay_changed: list[tuple[str, dict, str]] = field(default_factory=list)  # + what moved
    rerendered: list[tuple[str, dict]] = field(default_factory=list)
    unchanged: int = 0
    gaps_closed: list[str] = field(default_factory=list)
    gaps_opened: list[str] = field(default_factory=list)
    newly_excluded: list[dict] = field(default_factory=list)
    no_longer_excluded: list[dict] = field(default_factory=list)
    tooling: list[tuple[str, str | None, str | None]] = field(default_factory=list)
    old_counts: dict = field(default_factory=dict)
    new_counts: dict = field(default_factory=dict)
    new_measures: dict | None = None

    @property
    def document_changes(self) -> int:
        return (
            len(self.added)
            + len(self.removed)
            + len(self.source_changed)
            + len(self.overlay_changed)
            + len(self.rerendered)
        )


# --------------------------------------------------------------------------- reading


def _repo_rel(product: str, release: str) -> str:
    """processed/<product>/<release>, as git names it -- never the --work-dir sandbox."""
    return (PROCESSED_DIR.relative_to(PROJECT_ROOT) / product / release).as_posix()


def git_show(ref: str, repo_path: str, root: Path = PROJECT_ROOT) -> bytes | None:
    """Bytes of `repo_path` at `ref`, or None if the ref has no such file."""
    proc = subprocess.run(["git", "show", f"{ref}:{repo_path}"], cwd=root, capture_output=True)
    return proc.stdout if proc.returncode == 0 else None


def load_manifest_at(ref: str, product: str, release: str, root: Path = PROJECT_ROOT) -> dict:
    """manifest.json as committed at `ref`."""
    path = f"{_repo_rel(product, release)}/manifest.json"
    data = git_show(ref, path, root)
    if data is None:
        raise ChangelogError(f"no {path} at git ref {ref!r}")
    return json.loads(data.decode("utf-8"))


def load_manifest_working(product: str, release: str) -> dict:
    """manifest.json of the working tree (honors --work-dir)."""
    mf = manifest_file(product, release)
    if not mf.is_file():
        raise ChangelogError(f"no manifest at {mf}; run `bsc build` first")
    return json.loads(mf.read_text(encoding="utf-8"))


def body_hash_resolver(
    product: str, release: str, ref: str | None, root: Path = PROJECT_ROOT
) -> BodyHashFn:
    """A BodyHashFn for one side: the row's recorded hash, else the artifact's bytes.

    `ref=None` means the working tree. Rows from a build that recorded `body_sha256` never
    touch disk or git; older rows are hashed from the file, which for a ref costs one
    `git show` per document that needs it.
    """
    rel = _repo_rel(product, release)
    proot = processed_root(product, release)

    def resolve(source_id: str, row: dict) -> str | None:
        if row.get("body_sha256"):
            return row["body_sha256"]
        out = row.get("output_path")
        if not out:
            return None
        if ref is None:
            path = proot / out
            return body_sha256_file(path) if path.is_file() else None
        data = git_show(ref, f"{rel}/{out}", root)
        return body_sha256(data) if data is not None else None

    return resolve


# --------------------------------------------------------------------------- diffing


def artifact_rows(manifest: dict) -> dict[Key, dict]:
    return {
        (src["id"], a["source_path"]): a
        for src in manifest.get("sources", [])
        for a in src.get("artifacts", [])
    }


def _overlay_delta(old: dict | None, new: dict | None) -> str | None:
    if old is None and new is None:
        return None
    if old is None:
        return "overlay added"
    if new is None:
        return "overlay removed"
    if old.get("sha256") != new.get("sha256"):
        return "overlay changed"
    return None


def _excluded_key(entry: dict) -> tuple:
    return (entry.get("source_id"), entry.get("path"), entry.get("url"))


def diff_manifests(old: dict, new: dict, old_body: BodyHashFn, new_body: BodyHashFn) -> Changelog:
    """Compute the Changelog between two manifests. Pure apart from the two resolvers."""
    log = Changelog(
        old_version=old.get("corpus_version") or "unknown",
        new_version=new.get("corpus_version") or "unknown",
        new_date=(new.get("generated_utc") or "")[:10],
        old_counts=old.get("counts") or {},
        new_counts=new.get("counts") or {},
        new_measures=(new.get("crosswalk") or {}).get("counts"),
    )
    o_rows, n_rows = artifact_rows(old), artifact_rows(new)

    for key in sorted(n_rows.keys() - o_rows.keys()):
        log.added.append((key[0], n_rows[key]))
    for key in sorted(o_rows.keys() - n_rows.keys()):
        log.removed.append((key[0], o_rows[key]))
    for key in sorted(o_rows.keys() & n_rows.keys()):
        sid, o, n = key[0], o_rows[key], n_rows[key]
        if o.get("input_sha256") != n.get("input_sha256"):
            log.source_changed.append((sid, n))
            continue
        delta = _overlay_delta(o.get("overlay"), n.get("overlay"))
        if delta:
            log.overlay_changed.append((sid, n, delta))
            continue
        if o.get("output_sha256") == n.get("output_sha256"):
            log.unchanged += 1  # byte-identical: not even the header moved
            continue
        ob, nb = old_body(sid, o), new_body(sid, n)
        if ob is None or nb is None:
            side = "old" if ob is None else "new"
            raise ChangelogError(
                f"{sid}/{key[1]}: cannot read the artifact body on the {side} side; "
                f"is the processed tree present there?"
            )
        if ob != nb:
            log.rerendered.append((sid, n))
        else:
            log.unchanged += 1

    o_gaps = set((old.get("gaps") or {}).get("measures") or [])
    n_gaps = set((new.get("gaps") or {}).get("measures") or [])
    log.gaps_closed = sorted(o_gaps - n_gaps)
    log.gaps_opened = sorted(n_gaps - o_gaps)

    o_ex = {_excluded_key(e): e for e in (old.get("gaps") or {}).get("excluded_by_registry") or []}
    n_ex = {_excluded_key(e): e for e in (new.get("gaps") or {}).get("excluded_by_registry") or []}
    log.newly_excluded = [n_ex[k] for k in sorted(n_ex.keys() - o_ex.keys(), key=str)]
    log.no_longer_excluded = [o_ex[k] for k in sorted(o_ex.keys() - n_ex.keys(), key=str)]

    o_tool, n_tool = old.get("tooling") or {}, new.get("tooling") or {}
    for name in sorted(o_tool.keys() | n_tool.keys()):
        if o_tool.get(name) != n_tool.get(name):
            log.tooling.append((name, o_tool.get(name), n_tool.get(name)))
    return log


# --------------------------------------------------------------------------- rendering


def _doc_line(source_id: str, row: dict, *, with_url: bool = False) -> str:
    cite = f"`{source_id}/{row.get('source_path')}`"
    line = f"- {cite} → `{row.get('output_path')}` ({row.get('status')}): {row.get('title')}"
    if with_url and row.get("publication_url"):
        line += f" — {row['publication_url']}"
    return line


def _plural(n: int, noun: str) -> str:
    return f"{n:,} {noun}{'' if n == 1 else 's'}"


def _delta(old: int | None, new: int | None) -> str:
    if old is None or new is None or old == new:
        return ""
    d = new - old
    return f" ({'+' if d > 0 else '−'}{abs(d):,})"


def render(log: Changelog, *, from_ref: str) -> str:
    """The generated entry, in the shape CHANGELOG.md already uses."""
    out: list[str] = [f"## {log.new_version} — {log.new_date or 'unreleased'}", ""]

    n_docs, o_docs = log.new_counts.get("documents"), log.old_counts.get("documents")
    n_chunks, o_chunks = log.new_counts.get("chunks"), log.old_counts.get("chunks")
    parts = []
    if n_docs is not None:
        parts.append(f"{_plural(n_docs, 'document')}{_delta(o_docs, n_docs)}")
    if log.new_measures:
        m = log.new_measures
        parts.append(
            f"{_plural(m.get('measures', 0), 'measure')} "
            f"({m.get('covered', 0)} documented, {_plural(m.get('gaps', 0), 'tracked gap')})"
        )
    if n_chunks is not None:
        parts.append(f"{_plural(n_chunks, 'chunk')}{_delta(o_chunks, n_chunks)}")
    out.append(
        f"Changes since `{from_ref}` (corpus_version `{log.old_version}`): "
        + ", ".join(parts)
        + f". {_plural(log.document_changes, 'document')} changed, "
        f"{log.unchanged} unchanged in content."
    )
    out.append("")
    out.append(
        "<!-- Generated by `bsc changelog`. Document lines cite `source_id/source_path`; "
        "add the tooling notes (why documents were re-rendered) by hand above the list. -->"
    )

    added = [_doc_line(s, r, with_url=True) for s, r in log.added]
    for g in log.gaps_closed:
        added.append(f"- Measure `{g}` is now documented (tracked gap closed).")
    if added:
        out += ["", "### Added", "", *added]

    changed: list[str] = []
    for s, r in log.source_changed:
        changed.append(_doc_line(s, r) + " — upstream source revised.")
    for s, r, what in log.overlay_changed:
        changed.append(_doc_line(s, r) + f" — {what}.")
    if log.rerendered:
        if len(log.rerendered) <= LIST_RERENDERED_UP_TO:
            for s, r in log.rerendered:
                changed.append(_doc_line(s, r) + " — re-rendered from an unchanged source.")
        else:
            by_src: dict[str, int] = {}
            for s, _ in log.rerendered:
                by_src[s] = by_src.get(s, 0) + 1
            detail = ", ".join(f"{s} {n}" for s, n in sorted(by_src.items()))
            changed.append(
                f"- {_plural(len(log.rerendered), 'document')} re-rendered from unchanged "
                f"sources and overlays (tooling change; {detail})."
            )
    for name, o, n in log.tooling:
        changed.append(f"- Tooling: {name} {o or 'absent'} → {n or 'absent'}.")
    if changed:
        out += ["", "### Changed", "", *changed]

    removed = [_doc_line(s, r) for s, r in log.removed]
    for e in log.newly_excluded:
        removed.append(
            f"- `{e.get('source_id')}/{e.get('path')}` excluded by the source registry"
            + (f" ({e['url']})" if e.get("url") else "")
            + "."
        )
    for e in log.no_longer_excluded:
        removed.append(
            f"- `{e.get('source_id')}/{e.get('path')}` is no longer excluded by the source registry."
        )
    for g in log.gaps_opened:
        removed.append(f"- Measure `{g}` has no documentation (tracked gap opened).")
    if removed:
        out += ["", "### Removed", "", *removed]

    if not (added or changed or removed):
        out += ["", "No document-level changes."]
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- appending


def append_entry(entry: str, path: Path) -> None:
    """Insert `entry` above the newest `## ` entry of CHANGELOG.md, keeping the preamble.

    Refuses to add a second entry under the same heading, so re-running the command after
    a paste does not duplicate the notes.
    """
    text = path.read_text(encoding="utf-8") if path.is_file() else ""
    heading = entry.splitlines()[0]
    if heading in text.splitlines():
        raise ChangelogError(f"{path.name} already has an entry {heading!r}")
    lines = text.splitlines(keepends=True)
    at = next((i for i, line in enumerate(lines) if line.startswith("## ")), len(lines))
    before = "".join(lines[:at])
    if before and not before.endswith("\n\n"):
        before = before.rstrip("\n") + "\n\n"
    after = "".join(lines[at:])
    path.write_text(before + entry + ("\n" + after if after else ""), encoding="utf-8", newline="\n")


def entry_for(version: str, path: Path) -> str:
    """The body of CHANGELOG.md's `## <version> — <date>` entry: a GitHub Release's notes.

    The heading is left out, as the v1 Release was written, because the Release page
    already shows the tag. Raises if the file has no entry for `version`, which is how the
    release workflow refuses to publish a tag nobody wrote notes for.
    """
    if not path.is_file():
        raise ChangelogError(f"no {path.name}")
    lines = path.read_text(encoding="utf-8").splitlines()
    start = next(
        (i for i, line in enumerate(lines) if line.startswith(f"## {version} ") or line == f"## {version}"),
        None,
    )
    if start is None:
        raise ChangelogError(f"{path.name} has no entry for {version!r}")
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    return "\n".join(lines[start + 1 : end]).strip("\n") + "\n"


# --------------------------------------------------------------------------- entry point


def changelog(
    product: str,
    release: str,
    from_ref: str,
    to_ref: str | None = None,
    root: Path = PROJECT_ROOT,
) -> tuple[Changelog, str]:
    """Diff the build at `from_ref` against `to_ref` (None: the working tree); render it."""
    old = load_manifest_at(from_ref, product, release, root)
    if to_ref:
        new = load_manifest_at(to_ref, product, release, root)
    else:
        new = load_manifest_working(product, release)
    log = diff_manifests(
        old,
        new,
        body_hash_resolver(product, release, from_ref, root),
        body_hash_resolver(product, release, to_ref, root),
    )
    return log, render(log, from_ref=from_ref)
