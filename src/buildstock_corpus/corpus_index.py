"""index.json and sections.json: the corpus for a consumer that has no clone.

A clean-room agent, a hosted assistant, or an MCP server reads this corpus one HTTPS fetch
at a time. CORPUS_MAP.md is written for a reader; these two files are written for a
program, and are the first thing such a consumer fetches:

  index.json     every document (title, corpus path, upstream path, both links, status,
                 size, how many sections) and every measure (ids, names, corpus path,
                 doc_url, status), plus the corpus_version and the manifest hash they
                 describe. ~60 KB raw, ~7 KB over the wire; fetched first.
  sections.json  every heading of every document with its level and the line range it
                 spans in the processed file, keyed by corpus path. ~200 KB raw, ~26 KB
                 over the wire; fetched only when a question needs headings. Line ranges
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

from .chunk import _HEADING_RE
from .paths import PROJECT_ROOT, manifest_file, processed_root, sha256_file

INDEX_FILENAME = "index.json"
SECTIONS_FILENAME = "sections.json"
SCHEMAS_DIR = PROJECT_ROOT / "schemas"
INDEX_SCHEMA = SCHEMAS_DIR / "index.schema.json"
SECTIONS_SCHEMA = SCHEMAS_DIR / "sections.schema.json"

_MEASURE_FIELDS = ("measure_id", "upgrade_id", "upgrade_name", "corpus_path", "doc_url", "status")


def document_sections(text: str) -> list[dict]:
    """Every heading in a processed file, with its level and 1-based line range.

    A section runs from its heading line to the line before the next heading of any
    level (or the last line of the file), so ranges tile the file after the first heading
    and `lines[line_start-1:line_end]` is exactly the section's text.
    """
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()  # the trailing newline is not a line
    heads = [(i + 1, m) for i, line in enumerate(lines) if (m := _HEADING_RE.match(line))]
    out: list[dict] = []
    for k, (ln, m) in enumerate(heads):
        end = heads[k + 1][0] - 1 if k + 1 < len(heads) else len(lines)
        out.append({
            "heading": m.group(2).strip(),
            "level": len(m.group(1)),
            "line_start": ln,
            "line_end": end,
        })
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

    documents: list[dict] = []
    sections: dict[str, list[dict]] = {}
    for src in manifest.get("sources") or []:
        for a in src.get("artifacts", []):
            path = proot / a["output_path"]
            text = path.read_text(encoding="utf-8")
            secs = document_sections(text)
            sections[a["output_path"]] = secs
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


def validate_index_files(product: str, release: str, manifest_sha: str) -> list[str]:
    """Violations for index.json / sections.json: unreadable, stale, or off-schema.

    Absent is fine (they are derived; `bsc map` regenerates them). Present but describing
    a different manifest is a violation for the same reason a stale map is: a consumer
    that fetched it would route questions by a corpus that no longer exists.
    """
    proot = processed_root(product, release)
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
