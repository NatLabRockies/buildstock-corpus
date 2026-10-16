"""index.json and sections.json: the corpus for a consumer that has no clone.

A clean-room agent, a hosted assistant, or an MCP server reads this corpus one HTTPS fetch
at a time. CORPUS_MAP.md is written for a reader; these two files are written for a
program, and are the first thing such a consumer fetches:

  index.json     every document (title, corpus path, upstream path, both links, status,
                 size, its section files) and every measure (ids, names, corpus path,
                 doc_url, status), plus the corpus_version and the manifest hash they
                 describe. ~155 KB raw, ~20 KB gzip-compressed over the wire; fetched
                 first. The section file names are what make the three-fetch route real
                 (guidance -> index.json -> one section file): without them a consumer
                 had to fetch sections.json, several times this size, or guess a path.
                 The whole-plan acceptance test of 2026-10-16 (PLAN.md) did the latter.
  sections.json  every heading of every document with its level and the line range it
                 spans in the processed file, keyed by corpus path. ~360 KB raw, ~46 KB
                 over the wire; fetched only when a question needs levels or line ranges. Line ranges
                 are 1-based and count line 1, the provenance header, so a hit can be
                 cited as "<corpus_path> lines a-b" and re-read with `sed -n`.

Both are derived from the built artifacts (manifest, crosswalk, the processed files), so
`bsc map` regenerates them in seconds with no raw/, and both stamp the manifest hash so
`bsc validate` can call a stale one out exactly as it does the map. Each is checked
against its JSON Schema under schemas/ before it is written and again at validate time,
so the files cannot drift from the contract a consumer codes against.

Headings are found with the chunker's own regex, so a section here is the same section
retrieval cites.
"""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema

from .chunk_files import chunk_counts, chunks_file_for
from .paths import PROJECT_ROOT, manifest_file, processed_root, sha256_file
from .sections import document_sections, plan_sections  # noqa: F401  (re-exported)

INDEX_FILENAME = "index.json"
SECTIONS_FILENAME = "sections.json"
SCHEMAS_DIR = PROJECT_ROOT / "schemas"
INDEX_SCHEMA = SCHEMAS_DIR / "index.schema.json"
SECTIONS_SCHEMA = SCHEMAS_DIR / "sections.schema.json"

_MEASURE_FIELDS = ("measure_id", "upgrade_id", "upgrade_name", "corpus_path", "doc_url", "status")


def sections_with_files(corpus_path: str, text: str) -> list[dict]:
    """document_sections plus, where one exists, the section file that holds the heading.

    Every H2 has one; the H1 (line 2) has the `00-` preamble file when the document has
    text before its first H2 (or no H2 at all). H3+ entries name no file -- they are read
    inside their H2's file.
    """
    by_start = {p.line_start: p.file for p in plan_sections(corpus_path, text)}
    out = []
    for s in document_sections(text):
        entry = dict(s)
        if s["level"] == 2 and s["line_start"] in by_start:
            entry["file"] = by_start[s["line_start"]]
        elif s["level"] == 1 and s["line_start"] == 2 and 2 in by_start:
            entry["file"] = by_start[2]
        out.append(entry)
    return out


def _schema(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check_schema(instance: dict, schema_path: Path) -> list[str]:
    """Schema violations for `instance`, each as "<json path>: <message>"; [] if valid."""
    validator = jsonschema.Draft202012Validator(_schema(schema_path))
    return [
        f"{'/'.join(str(p) for p in e.absolute_path) or '<root>'}: {e.message}"
        for e in sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path))
    ]


def _dump(obj: dict) -> str:
    # Compact: these are fetched by programs, and every byte here is a byte on the wire for
    # a consumer that reads the corpus over HTTPS. One trailing newline keeps git quiet.
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"), sort_keys=False) + "\n"


def build_index(product: str, release: str) -> dict:
    """Write index.json and sections.json for a release from its already-built artifacts."""
    mf = manifest_file(product, release)
    if not mf.is_file():
        raise FileNotFoundError(f"no manifest at {mf}; run `bsc build` first")
    manifest = json.loads(mf.read_text(encoding="utf-8"))
    manifest_sha = sha256_file(mf)
    proot = processed_root(product, release)

    cf = proot / "chunks.jsonl"
    counts = chunk_counts(cf.read_text(encoding="utf-8")) if cf.is_file() else {}

    documents: list[dict] = []
    sections: dict[str, list[dict]] = {}
    for src in manifest.get("sources") or []:
        for a in src.get("artifacts", []):
            path = proot / a["output_path"]
            text = path.read_text(encoding="utf-8")
            secs = sections_with_files(a["output_path"], text)
            sections[a["output_path"]] = secs
            files = [s["file"] for s in secs if "file" in s]
            # Every document has at least the `00-` preamble file (see sections.py), and all
            # of a document's files share one directory: name it once, then the basenames,
            # which keeps ~2,000 entries at ~20 KB on the wire instead of ~25 KB.
            sections_dir = files[0].rsplit("/", 1)[0] if files else None
            documents.append({
                "title": a.get("title") or "",
                "source_id": src["id"],
                "corpus_path": a["output_path"],
                "source_path": a["source_path"],
                "source_url": a.get("source_url"),
                "publication_url": a.get("publication_url"),
                "status": a.get("status"),
                "bytes": path.stat().st_size,
                "sections": len(secs),
                "sections_dir": sections_dir,
                "section_files": [f.rsplit("/", 1)[1] for f in files],
                "chunks": counts.get((src["id"], a["source_path"]), 0),
                "chunks_file": chunks_file_for(a["output_path"]),
            })

    measures: list[dict] = []
    cw_file = proot / ((manifest.get("crosswalk") or {}).get("file") or "crosswalk.json")
    if cw_file.is_file():
        cw = json.loads(cw_file.read_text(encoding="utf-8"))
        measures = [{k: m.get(k) for k in _MEASURE_FIELDS} for m in cw.get("measures", [])]

    stamp = {
        "product": product,
        "release": release,
        "corpus_version": manifest.get("corpus_version"),
        "manifest_sha256": manifest_sha,
    }
    index = {
        **stamp,
        "sections_file": SECTIONS_FILENAME,
        "counts": {"documents": len(documents), "measures": len(measures)},
        "documents": documents,
        "measures": measures,
    }
    sections_doc = {**stamp, "documents": sections}

    for instance, schema, name in ((index, INDEX_SCHEMA, INDEX_FILENAME),
                                   (sections_doc, SECTIONS_SCHEMA, SECTIONS_FILENAME)):
        problems = check_schema(instance, schema)
        if problems:
            raise ValueError(f"{name} violates {schema.name}: " + "; ".join(problems[:5]))

    index_path = proot / INDEX_FILENAME
    sections_path = proot / SECTIONS_FILENAME
    index_path.write_text(_dump(index), encoding="utf-8", newline="\n")
    sections_path.write_text(_dump(sections_doc), encoding="utf-8", newline="\n")
    result = {
        "index_file": str(index_path),
        "sections_file": str(sections_path),
        "documents": len(documents),
        "measures": len(measures),
        "index_bytes": index_path.stat().st_size,
        "sections_bytes": sections_path.stat().st_size,
        "manifest_sha256": manifest_sha,
    }
    print(
        f"index: {len(documents)} docs, {len(measures)} measures -> {index_path} "
        f"({result['index_bytes'] // 1024} KB) + {SECTIONS_FILENAME} "
        f"({result['sections_bytes'] // 1024} KB)"
    )
    return result


def validate_index_files(proot: Path, manifest_sha: str) -> list[str]:
    """Violations for index.json / sections.json under `proot`: unreadable, stale, off-schema.

    Absent is fine (they are derived; `bsc map` regenerates them). Present but describing
    a different manifest is a violation for the same reason a stale map is: a consumer
    that fetched it would route questions by a corpus that no longer exists.

    Takes the processed root rather than (product, release) so the caller's notion of
    where the release lives -- including a test's redirected one -- is the one checked.
    """
    errors: list[str] = []
    for name, schema in ((INDEX_FILENAME, INDEX_SCHEMA), (SECTIONS_FILENAME, SECTIONS_SCHEMA)):
        path = proot / name
        if not path.is_file():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{name}: not readable JSON ({str(exc)[:80]}); run `bsc map`")
            continue
        if data.get("manifest_sha256") != manifest_sha:
            errors.append(
                f"{name} is stale: it was generated from a different manifest than the one "
                f"on disk; run `bsc map` to regenerate it"
            )
        problems = check_schema(data, schema)
        if problems:
            errors.append(f"{name} violates {schema.name}: " + "; ".join(problems[:3]))
    return errors
