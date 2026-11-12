"""List every markdown table in a processed document, with the fingerprint an overlay pins.

A `checked:` entry (and a `replaces:` one) names the extracted table it is about by
`table_sha256`, the fingerprint of the table's cell values (overlay._table_fingerprint).
This prints that value for each table in a document, beside the caption it sits under, so
an entry is written from what the build actually emitted and never typed by hand.

    uv run python scripts/list_tables.py processed/resstock/<release>/upgrade_measures/measure_pdfs/96634.md

For each table: the line it starts on, its size, the nearest `Table N.` caption above it
(or below, when docling put the grid first), and the fingerprint. Captions with no table
are listed at the end: those are the ones that need a caption-anchored `tables:` entry.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from buildstock_corpus.overlay import (  # noqa: E402
    _CAPTION,
    _MD_TABLE_DELIM,
    _has_table_below,
    _label,
    _table_blocks,
    _table_fingerprint,
)


def table_rows(text: str) -> tuple[list[dict], list[dict]]:
    """(tables, bare table captions) for one document's text."""
    lines = text.split("\n")
    captions = [
        (i, _label(m.group(1), m.group(2)), lines[i].strip())
        for i, line in enumerate(lines)
        if (m := _CAPTION.match(line)) and _label(m.group(1), m.group(2)).startswith("Table")
    ]
    tables = []
    for start, end in _table_blocks(lines):
        block = lines[start:end]
        above = [c for c in captions if c[0] < start]
        below = [c for c in captions if c[0] >= end]
        nearest = above[-1] if above else (below[0] if below else None)
        position = "above" if above else ("below" if below else "")
        body_rows = sum(1 for ln in block if not _MD_TABLE_DELIM.match(ln)) - 1
        tables.append({
            "line": start + 1,
            "rows": max(body_rows, 0),
            "cols": len(block[0].strip().strip("|").split("|")),
            "label": nearest[1] if nearest else "",
            "caption_line": nearest[0] + 1 if nearest else None,
            "caption_is": position,
            "caption": nearest[2] if nearest else "",
            "table_sha256": _table_fingerprint(block),
        })
    bare = [
        {"line": i + 1, "label": label, "caption": text_}
        for i, label, text_ in captions
        if not _has_table_below(lines, i)
    ]
    return tables, bare


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("document", type=Path, help="a processed .md file")
    args = ap.parse_args()

    tables, bare = table_rows(args.document.read_text(encoding="utf-8"))
    print(f"{args.document}: {len(tables)} table(s)")
    for t in tables:
        where = f"{t['label']} ({t['caption_is']}, line {t['caption_line']})" if t["label"] else "no caption"
        print(f"  line {t['line']:>5}  {t['rows']:>3} x {t['cols']:<2}  {where}")
        print(f"              table_sha256: {t['table_sha256']}")
        if t["caption"]:
            print(f"              {t['caption'][:110]}")
    if bare:
        print(f"\n{len(bare)} table caption(s) with no table beneath:")
        for b in bare:
            print(f"  line {b['line']:>5}  {b['caption'][:110]}")


if __name__ == "__main__":
    main()
