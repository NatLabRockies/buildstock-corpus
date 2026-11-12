"""Check every grid of one ResStock measure report against the PDF text layer.

    uv run python scripts/check_grids_against_pdf.py 96405

Three checks, each printed per grid (contents-page grids are skipped):
  1. cells: which cells are NOT found in the PDF text (whitespace, hyphens and quotes
     ignored). A cell missing words in the middle shows up here.
  2. row order: each row, as its cells run together, should appear in the text, and the
     rows in the same order.
  3. gaps: PDF text between consecutive rows that the grid does not carry: a dropped word
     at the edge of a row, or a dropped row.
A clean result does not prove the table is right: a merged cell left blank, or text filed in
the wrong row, passes. Compare the row structure with the page as well. Needs raw/ (the
fetched PDFs).
"""
import re
import sys
from pathlib import Path

import pypdfium2 as pdfium

sys.path.insert(0, "src")
sys.path.insert(0, "scripts")
from buildstock_corpus.overlay import _table_blocks
from count_footnotes import _squash

n = sys.argv[1]  # report number, e.g. 96405; run from the repo root where raw/ holds the PDFs
P = Path("processed/resstock/resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs")
lines = (P / f"{n}.md").read_text(encoding="utf-8").split("\n")
pdf = pdfium.PdfDocument(f"raw/resstock/resstock_amy2018_2025_release_1/measure_pdfs/{n}.pdf")
pages = []
for i in range(len(pdf)):
    tp = pdf[i].get_textpage()
    pages.append(_squash(tp.get_text_range().replace("&", "&")))
    tp.close()
whole = "".join(pages)
for s, e in _table_blocks(lines):
    blk = lines[s:e]
    if "....." in "".join(blk[:3]):
        continue
    miss, total = [], 0
    for r, ln in enumerate(blk):
        if re.match(r"^\s*\|[\s:|\-]+\|\s*$", ln):
            continue
        for c in [c.strip() for c in ln.strip().strip("|").split("|")]:
            if not c:
                continue
            total += 1
            q = _squash(c.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">"))
            if q not in whole:
                # which part fails? report the longest prefix found
                k = len(q)
                while k > 0 and q[:k] not in whole:
                    k -= 1
                miss.append((r, c[:70], q[max(0, k - 12):k + 12]))
    print(f"grid at line {s+1}: {total} cells, {len(miss)} not found in the PDF text")
    for r, c, where in miss[:12]:
        print(f"    row {r}: {c!r}  (breaks near ...{where}...)")

# Row order: each row, as its cells run together, should appear in the PDF text, and the rows
# should appear in the same order. Rows that are not found whole (cells not consecutive in
# the text layer, e.g. wrapped or merged cells) are listed; they need a look at the page.
print("\nrow order check")
for s, e in _table_blocks(lines):
    blk = lines[s:e]
    if "....." in "".join(blk[:3]):
        continue
    pos, whole_rows, missing, out_of_order = -1, 0, [], 0
    data = [ln for ln in blk if not re.match(r"^\s*\|[\s:|\-]+\|\s*$", ln)]
    for r, ln in enumerate(data):
        q = _squash("".join(c.strip() for c in ln.strip().strip("|").split("|")).replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">"))
        k = whole.find(q, max(pos, 0)) if q else -1
        if k < 0:
            k2 = whole.find(q)
            if k2 >= 0:
                out_of_order += 1
            else:
                missing.append(r)
            continue
        whole_rows += 1
        pos = k
    print(f"grid at line {s+1}: {len(data)} rows, {whole_rows} found whole and in order, "
          f"{out_of_order} found out of order, not found whole: {missing[:15]}")

# Gaps: when consecutive rows are both found whole, the PDF text between the end of one and
# the start of the next should be empty. Text in the gap is text the grid does not have (a
# dropped word at the edge of a row, a dropped row) or a cell that wraps out of order.
print("\ngap check (PDF text between consecutive rows that the grid does not carry)")
for s, e in _table_blocks(lines):
    blk = lines[s:e]
    if "....." in "".join(blk[:3]):
        continue
    data = [ln for ln in blk if not re.match(r"^\s*\|[\s:|\-]+\|\s*$", ln)]
    prev_end, gaps, found = None, [], 0
    for r, ln in enumerate(data):
        q = _squash("".join(c.strip() for c in ln.strip().strip("|").split("|")).replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">"))
        k = whole.find(q, prev_end if prev_end is not None else 0) if q else -1
        if k < 0:
            prev_end = None
            continue
        found += 1
        if prev_end is not None and k - prev_end > 0:
            gaps.append((r, whole[prev_end:k][:80]))
        prev_end = k + len(q)
    tail = whole[prev_end:prev_end + 40] if prev_end is not None else ""
    print(f"grid at line {s+1}: {found}/{len(data)} rows located, {len(gaps)} gap(s); text after last row: {tail!r}")
    for r, g in gaps[:8]:
        print(f"    before row {r}: {g!r}")
