"""Save the bitmaps embedded in a PDF's pages at their own resolution.

    uv run python scripts/figure_grids/extract.py <pdf> <out dir> [first page]

A grid of numbers pasted into a report as a picture is far easier to read from the embedded
bitmap than from a page render. Writes pNNN_K.png (page NNN, K-th image from the top) for
every image at least 200 px wide, and prints each one's size.
"""
import sys
from pathlib import Path

import pypdfium2 as pdfium
import pypdfium2.raw as raw

pdf = pdfium.PdfDocument(sys.argv[1])
out = Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
first = int(sys.argv[3]) if len(sys.argv) > 3 else 1
for p in range(first - 1, len(pdf)):
    objs = sorted(pdf[p].get_objects(filter=[raw.FPDF_PAGEOBJ_IMAGE]), key=lambda o: -o.get_bounds()[3])
    for k, o in enumerate(objs):
        w, h = o.get_px_size()
        if w < 200:
            continue
        name = f"p{p + 1:03d}_{k}.png"
        o.get_bitmap().to_pil().save(out / name)
        print(name, w, h)
