"""Stamp every overlay sidecar with the source_url and publication_url of its document.

An overlay is a hand transcription of one document, and its header already names that
document by product, release, source id and upstream path. Adding the two links lets a
reader check the transcription against its source with nothing but the sidecar in hand
(W2.4). The values are the ones the build resolved onto the document -- taken from the
release manifest, so they cannot be typed wrong -- and build/validate then require the
overlay and the document to agree.

Overlays for documents the registry excludes (no manifest row) are stamped from the fetch
record instead, so they stay self-describing while they sit unused.

Keys are inserted as text, right after the `source_path:` line (or after `release:` when a
sidecar lacks source_id/source_path, in which case those two are added as well), so the
long comment blocks the sidecars open with are untouched. Re-running updates values in
place and changes nothing when they already agree.

    uv run python scripts/stamp_overlay_links.py --release comstock_amy2018_2025_release_3
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from buildstock_corpus.links import artifact_urls, clone_for  # noqa: E402
from buildstock_corpus.paths import OVERLAYS_DIR, manifest_file, raw_root  # noqa: E402
from buildstock_corpus.registry import load_registry  # noqa: E402

_KEY_RE = re.compile(r"^(product|release|source_id|source_path|source_url|publication_url):")


def stamp(text: str, source_id: str, source_path: str, source_url: str, publication_url: str) -> str:
    """Return `text` with the four identity keys present and the two links set.

    Existing `source_url` / `publication_url` lines are replaced; missing ones are inserted
    after `source_path:`; missing `source_id` / `source_path` are inserted after `release:`.
    """
    lines = text.split("\n")
    idx = {m.group(1): i for i, l in enumerate(lines) if (m := _KEY_RE.match(l))}
    if "release" not in idx:
        raise ValueError("overlay has no top-level release: line; cannot place the links")

    for key in ("source_url", "publication_url"):
        if key in idx:
            del lines[idx[key]]
            idx = {m.group(1): i for i, l in enumerate(lines) if (m := _KEY_RE.match(l))}

    insert_at = idx["release"] + 1
    new: list[str] = []
    if "source_id" not in idx:
        new.append(f"source_id: {source_id}")
    if "source_path" not in idx:
        new.append(f"source_path: {source_path}")
    else:
        insert_at = idx["source_path"] + 1
    new += [f"source_url: {source_url}", f"publication_url: {publication_url}"]
    lines[insert_at:insert_at] = new
    return "\n".join(lines)


def _targets(product: str, release: str) -> dict[str, tuple[str, str, str, str]]:
    """overlay path (relative to overlays/) -> (source_id, source_path, source_url, publication_url)."""
    manifest = json.loads(manifest_file(product, release).read_text(encoding="utf-8"))
    out: dict[str, tuple[str, str, str, str]] = {}
    for s in manifest["sources"]:
        for a in s["artifacts"]:
            if a.get("overlay"):
                out[a["overlay"]["path"]] = (s["id"], a["source_path"], a["source_url"], a["publication_url"])

    # Overlays with no manifest row: documents the registry excluded. Resolve their links
    # the way build would have, from the fetch record and the registry.
    reg = load_registry(product, release)
    state = json.loads((raw_root(product, release) / "fetch_state.json").read_text(encoding="utf-8"))
    rel_root = OVERLAYS_DIR / f"{product}_{release}"
    for path in sorted(rel_root.rglob("*.yaml")):
        rel = path.relative_to(OVERLAYS_DIR).as_posix()
        if rel in out:
            continue
        inner = path.relative_to(rel_root).as_posix()  # <source_id>/<source_path minus ext>.yaml
        source_id, stem = inner.split("/", 1)
        src = reg.by_id(source_id)
        src_state = state["sources"][source_id]
        candidates = [e["path"] for e in src_state.get("external_pdfs", []) if e["path"].rsplit(".", 1)[0] == stem[:-5]]
        candidates += [p["path"] for p in src_state.get("internal_pages", []) + src_state.get("local_pdfs", [])
                       if p["path"].rsplit(".", 1)[0] == stem[:-5]]
        if not candidates:
            print(f"  skip {rel}: no fetched input matches it", file=sys.stderr)
            continue
        source_path = candidates[0]
        src_url, pub_url = artifact_urls(source_path, src, src_state, clone_for(src_state, state.get("clones", [])))
        out[rel] = (source_id, source_path, src_url, pub_url)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--product", default="comstock")
    ap.add_argument("--release", required=True)
    ap.add_argument("--check", action="store_true", help="report files that would change; write nothing")
    args = ap.parse_args()

    changed = 0
    for rel, (source_id, source_path, src_url, pub_url) in sorted(_targets(args.product, args.release).items()):
        path = OVERLAYS_DIR / rel
        before = path.read_text(encoding="utf-8")
        after = stamp(before, source_id, source_path, src_url, pub_url)
        if after != before:
            changed += 1
            print(f"{'would stamp' if args.check else 'stamped'} {rel}")
            if not args.check:
                path.write_text(after, encoding="utf-8", newline="\n")
    print(f"{changed} overlay(s) {'need stamping' if args.check else 'stamped'}")
    return 1 if (args.check and changed) else 0


if __name__ == "__main__":
    raise SystemExit(main())
