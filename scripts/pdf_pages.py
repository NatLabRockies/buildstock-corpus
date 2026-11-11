"""Render the pages of a source PDF that hold its tables and figures, with their text layer.

Step 2 of the checking method in overlays/README.md: a table the extractor emitted is
compared with the page it came from, and that needs the page as a picture (what a reader
sees) and as text (what the PDF says the cells contain). This finds every `Table N.` and
`Figure N.` caption in the PDF's text layer and writes, for each page that has one:

    <out>/page_<NNN>.png    the page rendered at --scale (default 1.5)
    <out>/page_<NNN>.txt    the page's text layer
    <out>/captions.json     caption label -> 1-based page number(s), in reading order

Pages that are a "List of Tables" or "List of Figures" are skipped: every line there
matches the caption pattern and none is a table. `--pages 12,14-16` renders the named pages
instead, for a table that runs onto a page with no caption of its own.

    uv run python scripts/pdf_pages.py raw/resstock/<release>/measure_pdfs/96634.pdf --out <dir>

The page number printed here is what a sidecar entry's `page:` records.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import pypdfium2 as pdfium

_CAPTION_RE = re.compile(r"^\s*(Table|Figure)\s+([A-Z]?-?[0-9]+[A-Za-z]?)\s*[.:]", re.M)
_LIST_PAGE_RE = re.compile(r"^\s*List of (Tables|Figures)\s*$", re.M | re.I)
# A contents-style line: caption text, dot leaders or spaces, then a page number.
_LEADER_RE = re.compile(r"\.{4,}\s*\d+\s*$", re.M)


def page_text(page) -> str:
    textpage = page.get_textpage()
    try:
        return textpage.get_text_range()
    finally:
        textpage.close()


def is_list_page(text: str) -> bool:
    return bool(_LIST_PAGE_RE.search(text)) or len(_LEADER_RE.findall(text)) >= 4


def parse_pages(spec: str, n_pages: int) -> list[int]:
    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        lo, _, hi = part.partition("-")
        for p in range(int(lo), int(hi or lo) + 1):
            if 1 <= p <= n_pages:
                pages.add(p)
    return sorted(pages)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--out", type=Path, required=True, help="directory to write into")
    ap.add_argument("--scale", type=float, default=1.5)
    ap.add_argument("--pages", help="render these 1-based pages (e.g. 12,14-16) instead")
    ap.add_argument("--kind", choices=("table", "figure", "both"), default="both")
    args = ap.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    pdf = pdfium.PdfDocument(str(args.pdf))
    n_pages = len(pdf)
    texts = [page_text(pdf[i]) for i in range(n_pages)]

    captions: dict[str, list[int]] = {}
    wanted: set[int] = set()
    for i, text in enumerate(texts):
        if is_list_page(text):
            continue
        for m in _CAPTION_RE.finditer(text):
            kind = m.group(1).lower()
            if args.kind != "both" and kind != args.kind:
                continue
            label = f"{m.group(1)} {m.group(2)}"
            captions.setdefault(label, [])
            if i + 1 not in captions[label]:
                captions[label].append(i + 1)
            wanted.add(i + 1)

    pages = parse_pages(args.pages, n_pages) if args.pages else sorted(wanted)
    for p in pages:
        bitmap = pdf[p - 1].render(scale=args.scale)
        bitmap.to_pil().save(args.out / f"page_{p:03d}.png")
        (args.out / f"page_{p:03d}.txt").write_text(texts[p - 1], encoding="utf-8", newline="\n")
    (args.out / "captions.json").write_text(
        json.dumps({"pdf": args.pdf.name, "pages": n_pages, "captions": captions}, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    print(f"{args.pdf.name}: {n_pages} page(s), {len(captions)} caption(s), {len(pages)} page(s) written to {args.out}")
    for label, where in captions.items():
        print(f"  {label}: page {', '.join(map(str, where))}")


if __name__ == "__main__":
    main()
