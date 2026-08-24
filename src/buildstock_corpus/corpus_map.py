"""Generate CORPUS_MAP.md — the entry point an agent reads before opening any document.

The corpus is 118 markdown files across three sources. Without a map, an agent answering
"which document covers exterior wall insulation, and what upgrade id is it?" has to guess
paths or grep every file; with one it reads this file and then exactly the file it needs.
That routing cost, not file size, is what makes reading the corpus slow.

Everything here is derived from artifacts a clone already has -- manifest.json (titles,
output paths, overlay records), chunks.jsonl (section breadcrumbs, dates) and
crosswalk.json (measure -> upgrade id -> doc). Nothing is re-extracted and nothing reads
raw/, so `bsc map` runs in seconds in a fresh clone. That independence is deliberate:
`bsc build` needs fetch_state.json, and re-running `bsc fetch` re-downloads every PDF and
can invalidate the hand-authored overlay hash pins.

The header stamps the sha256 of the manifest this map was built from, which is what lets
`bsc validate` tell a current map from a stale one (see manifest.validate_manifest). The
map points at the manifest rather than the manifest pinning the map because the manifest is
written first -- a hash of a file that does not exist yet cannot go into it.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from .paths import chunks_file, manifest_file, processed_root, sha256_file

MAP_FILENAME = "CORPUS_MAP.md"

# `manifest_sha256: <hex>` on its own line in the provenance header. Parsed back out by
# recorded_manifest_sha256 rather than kept in a sidecar: the stamp belongs to the document
# a reader is holding, and one file cannot go stale against itself.
_SHA_LINE = re.compile(r"^-\s*`manifest_sha256`:\s*`([0-9a-f]{64})`\s*$", re.MULTILINE)

# Sections are stored as breadcrumbs ("2. Technology Summary > 2.1 Lab Testing"). The map
# lists top-level headings only -- the depth an agent needs to pick a file, not to navigate
# inside one, which it will do by reading the file.
_MAX_SECTIONS = 8


def recorded_manifest_sha256(product: str, release: str) -> str | None:
    """The manifest hash a written map claims it was derived from, or None if no map."""
    path = processed_root(product, release) / MAP_FILENAME
    if not path.is_file():
        return None
    match = _SHA_LINE.search(path.read_text(encoding="utf-8"))
    return match.group(1) if match else None


def _doc_facts(product: str, release: str) -> dict[tuple[str, str], dict]:
    """Per-document section list and date, keyed (source_id, source_path), from chunks.jsonl.

    Read from the chunks rather than by re-parsing the markdown so the map describes exactly
    what was indexed. Two LaTeX appendices carry no section metadata at all (they are data
    tables, not prose); they get an empty list here and the caller falls back to the title.
    """
    facts: dict[tuple[str, str], dict] = defaultdict(lambda: {"sections": [], "date": None})
    cf = chunks_file(product, release)
    if not cf.is_file():
        return {}
    with cf.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            meta = json.loads(line)["metadata"]
            rec = facts[(meta["source_id"], meta["source_path"])]
            section = _headline_section(meta.get("section"), meta.get("doc_title"))
            if section and section not in rec["sections"]:
                rec["sections"].append(section)
            rec["date"] = rec["date"] or meta.get("date_last_updated")
    return dict(facts)


def _headline_section(breadcrumb: str | None, doc_title: str | None) -> str:
    """The outermost heading of a breadcrumb that isn't just the document's own title.

    A LaTeX chapter's breadcrumbs all begin with the chapter title ("Envelope > Windows"),
    so taking the first component verbatim would fill the column with 19 rows that repeat
    what the Document cell already says. Dropping title-equal components surfaces the real
    subsections there, and leaves the measure and site docs -- whose headings sit at the top
    level already -- unchanged.
    """
    title = (doc_title or "").strip()
    parts = [p.strip() for p in (breadcrumb or "").split(" > ") if p.strip()]
    meaningful = [p for p in parts if p != title]
    return meaningful[0] if meaningful else ""


def _cell(text: str) -> str:
    """Escape a value for a markdown table cell; a stray pipe would split the row."""
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def _overlay_note(artifact: dict) -> str:
    """Flag hand-authored content, so a reader knows a table was transcribed, not extracted."""
    ov = artifact.get("overlay")
    if not ov:
        return ""
    parts = []
    n_tables = len(ov.get("tables_applied") or [])
    n_figures = len(ov.get("figures_applied") or [])
    if n_tables:
        parts.append(f"{n_tables} table(s)")
    if n_figures:
        parts.append(f"{n_figures} figure(s)")
    return ", ".join(parts)


def _source_section(src: dict, facts: dict[tuple[str, str], dict]) -> list[str]:
    lines = [
        f"### `{src['id']}` — {len(src.get('artifacts', []))} document(s)",
        "",
        "| Document | Path | Top-level sections | Updated | Hand-authored |",
        "| --- | --- | --- | --- | --- |",
    ]
    for a in src.get("artifacts", []):
        rec = facts.get((src["id"], a["source_path"]), {})
        sections = rec.get("sections") or []
        # Fall back to the title rather than leaving the cell blank: an empty cell reads as
        # "this document has no content", when it means "this one is a flat data table".
        shown = sections[:_MAX_SECTIONS] or [a.get("title") or "(no headings)"]
        more = f" … +{len(sections) - _MAX_SECTIONS} more" if len(sections) > _MAX_SECTIONS else ""
        lines.append(
            f"| {_cell(a.get('title') or '')} "
            f"| [`{a['output_path']}`]({a['output_path']}) "
            f"| {_cell('; '.join(shown))}{more} "
            f"| {rec.get('date') or '—'} "
            f"| {_overlay_note(a) or '—'} |"
        )
    lines.append("")
    return lines


def _resolve_doc(target: str, by_source_path: dict[str, str], by_basename: dict[str, list[str]]) -> str | None:
    """The processed markdown for a crosswalk target, or None if nothing in the corpus matches.

    Internal pages name a repo-relative path, which is the artifact's source_path verbatim.
    External PDFs name a URL, and the artifact records where fetch put the file
    (`measure_pdfs/89340.pdf` for `https://.../89340.pdf`) -- so those join on the filename.
    Only a basename that resolves to exactly one artifact is accepted: two upstream files
    sharing a name would otherwise route readers to an arbitrary one of them, which is worse
    than declining to link and is the kind of thing nobody would notice in a 65-row table.
    """
    if not target:
        return None
    if target in by_source_path:
        return by_source_path[target]
    candidates = by_basename.get(target.rsplit("/", 1)[-1], [])
    return candidates[0] if len(candidates) == 1 else None


def _measures_section(
    crosswalk: dict, by_source_path: dict[str, str], by_basename: dict[str, list[str]]
) -> list[str]:
    """Measure -> upgrade id -> document. The highest-value routing table in the map.

    upgrade_id is how a measure is named in the published data lake, so a question that
    starts from a results column ("what is upgrade 32?") lands here first. Measures with no
    documentation are listed too, marked as gaps, because knowing a doc is absent is a real
    answer -- otherwise an agent keeps searching for a file that was never written.
    """
    measures = crosswalk.get("measures") or []
    if not measures:
        return []
    gaps = {g["measure_id"] for g in crosswalk.get("gaps") or []}
    lines = [
        "## Measures",
        "",
        f"{len(measures)} measure(s) in this release; "
        f"{crosswalk.get('counts', {}).get('covered', 0)} documented, {len(gaps)} tracked gap(s).",
        "",
        "| Upgrade id | Measure | Upgrade name | Document |",
        "| --- | --- | --- | --- |",
    ]
    for m in measures:
        mid = m.get("measure_id", "")
        target = m.get("doc_target") or ""
        out = _resolve_doc(target, by_source_path, by_basename)
        if out:
            doc = f"[`{out}`]({out})"
        elif mid in gaps:
            doc = "**gap** — no documentation in this release"
        elif target.startswith("http"):
            # Documented upstream but not extracted into this corpus -- say so rather than
            # linking silently, or a reader takes the URL for a local file it can read.
            doc = f"not in corpus — [upstream PDF]({target})"
        else:
            doc = "—"
        lines.append(
            f"| {_cell(m.get('upgrade_id') or '—')} "
            f"| {_cell(m.get('documentation_name') or mid)} "
            f"| {_cell(m.get('upgrade_name') or '—')} "
            f"| {doc} |"
        )
    lines.append("")
    return lines


def _gaps_section(manifest: dict) -> list[str]:
    """What the corpus does not contain. Stated so absence is never inferred as coverage."""
    gaps = manifest.get("gaps") or {}
    excluded = gaps.get("excluded_unpublished") or {}
    unreachable = gaps.get("unreachable_pdfs") or []
    measures = gaps.get("measures") or []
    if not (excluded or unreachable or measures):
        return []
    lines = ["## Known gaps", ""]
    if measures:
        lines += [
            f"- **{len(measures)} measure(s) with no documentation** in this release: "
            + ", ".join(f"`{m}`" for m in measures),
        ]
    if unreachable:
        lines += [f"- **{len(unreachable)} source PDF(s) unreachable** at fetch time."]
    for src_id, paths in excluded.items():
        lines += [
            f"- **{len(paths)} unpublished `{src_id}` page(s)** excluded upstream "
            f"(`published: false`), so they are absent by intent, not by failure."
        ]
    lines.append("")
    return lines


def _render(product: str, release: str, manifest: dict, manifest_sha: str, facts: dict) -> str:
    counts = manifest.get("counts") or {}
    sources = manifest.get("sources") or []
    # source_path -> output_path, so the measures table can link a crosswalk target (which
    # names the upstream file) to the processed markdown a reader should actually open.
    by_source_path = {
        a["source_path"]: a["output_path"] for s in sources for a in s.get("artifacts", [])
    }
    by_basename: dict[str, list[str]] = defaultdict(list)
    for src_path, out_path in by_source_path.items():
        by_basename[src_path.rsplit("/", 1)[-1]].append(out_path)

    lines = [
        f"# {product} {release} — corpus map",
        "",
        "Generated by `bsc map`. **Do not edit by hand** — regenerate instead.",
        "",
        "## Provenance",
        "",
        f"- `product`: `{product}`",
        f"- `release`: `{release}`",
        f"- `manifest_sha256`: `{manifest_sha}`",
        f"- `map_generated_utc`: `{datetime.now(timezone.utc).isoformat()}`",
        f"- `build_generated_utc`: `{manifest.get('generated_utc')}`",
        "",
    ]
    if manifest.get("sample"):
        lines += [
            "> **SAMPLE BUILD — partial corpus, not a release record.** This map describes a "
            "capped smoke-test build, not everything in the release.",
            "",
        ]
    lines += [
        "## How to read this corpus",
        "",
        "- **Start here, then open one file.** The tables below give every document's title, "
        "path and top-level sections; pick the file and read it directly.",
        "- **No vector index needed.** These are plain markdown files — read and grep them. "
        "`bsc query` exists for consumers *without* filesystem access and needs a ~1 hour "
        "`bsc index` build first.",
        "- **Cite as `source_id/source_path`.** Every document opens with an HTML comment "
        "recording the product, release, source id and upstream path it came from.",
        "- **Images are not in the clone.** `processed/**/*.png` is gitignored (~250 MB, "
        "regenerable), so image references resolve to absent files. Tables and figure "
        "descriptions marked *hand-authored* were transcribed from those images, so the "
        "content is present as text even when the picture is not.",
        "",
        "## Contents",
        "",
        f"- **{counts.get('documents', 0)} documents** in {len(sources)} source(s), "
        f"**{counts.get('chunks', 0)} chunks**",
    ]
    by_type = counts.get("by_type") or {}
    if by_type:
        lines.append(
            "- By type: " + ", ".join(f"{n} {t}" for t, n in sorted(by_type.items()))
        )
    if counts.get("overlay_documents"):
        lines.append(
            f"- Hand-authored content in {counts['overlay_documents']} document(s): "
            f"{counts.get('overlay_tables', 0)} table(s), "
            f"{counts.get('overlay_figures', 0)} figure description(s)"
        )
    lines += ["", "## Documents", ""]
    for src in sources:
        lines += _source_section(src, facts)

    proot = processed_root(product, release)
    cw_file = proot / (manifest.get("crosswalk", {}) or {}).get("file", "crosswalk.json")
    if cw_file.is_file():
        crosswalk = json.loads(cw_file.read_text(encoding="utf-8"))
        lines += _measures_section(crosswalk, by_source_path, dict(by_basename))

    lines += _gaps_section(manifest)
    return "\n".join(lines).rstrip() + "\n"


def build_map(product: str, release: str) -> dict:
    """Write CORPUS_MAP.md for a release from its already-built artifacts."""
    mf = manifest_file(product, release)
    if not mf.is_file():
        raise FileNotFoundError(f"no manifest at {mf}; run `bsc build` first")
    manifest = json.loads(mf.read_text(encoding="utf-8"))
    manifest_sha = sha256_file(mf)
    facts = _doc_facts(product, release)

    out: Path = processed_root(product, release) / MAP_FILENAME
    text = _render(product, release, manifest, manifest_sha, facts)
    out.parent.mkdir(parents=True, exist_ok=True)
    # newline="\n" for the same reason the processed .md files use it (see build._write_processed):
    # .gitattributes pins the checkout to LF, so a CRLF map would differ by who generated it.
    out.write_text(text, encoding="utf-8", newline="\n")

    n_docs = sum(len(s.get("artifacts", [])) for s in manifest.get("sources") or [])
    print(f"map: {n_docs} docs across {len(manifest.get('sources') or [])} source(s) -> {out}")
    return {"file": str(out), "documents": n_docs, "manifest_sha256": manifest_sha}
