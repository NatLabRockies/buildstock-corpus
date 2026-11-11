"""Read a spreadsheet-screenshot grid cell by cell.

1. One detection pass finds the text boxes; they are grouped into rows by vertical centre.
2. Numbers in a spreadsheet are right-aligned, so the right edges of the single-number boxes
   cluster into columns.
3. Every (row, column) cell is cropped and recognised on its own, twice (colour at 4x, grey
   at 5x). A cell where the two readings differ is flagged.

Output: cells.json {image: {"rows": [{"kind": "data"|"text", "y": [y0, y1], "cells": [a...],
"alt": [b...], "text": "..."}], "cols": [x1...]}}
"""
import json
import os
import re
import sys
from pathlib import Path

import cv2
import numpy as np
from rapidocr import RapidOCR

G = Path(os.environ.get("GRID_DIR", "."))  # working folder: images in, JSON out
NUM = re.compile(r"^-?\d+(?:\.\d+)?$")
eng = RapidOCR()
eng_rec = RapidOCR()
PROJ = "--proj" in sys.argv


def detect(img, scale=3):
    big = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
    res = eng(big, use_det=True, use_cls=False, use_rec=True)
    out = []
    if res.boxes is None:
        return out
    for box, txt in zip(res.boxes, res.txts):
        xs, ys = [float(p[0]) / scale for p in box], [float(p[1]) / scale for p in box]
        out.append((min(xs), min(ys), max(xs), max(ys), txt.strip()))
    return out


def group_rows(boxes):
    boxes = sorted(boxes, key=lambda b: (b[1] + b[3]) / 2)
    rows, cur = [], []
    for b in boxes:
        cy = (b[1] + b[3]) / 2
        if cur:
            mean = np.mean([(c[1] + c[3]) / 2 for c in cur])
            h = np.median([c[3] - c[1] for c in cur])
            if cy - mean > 0.6 * h:
                rows.append(sorted(cur))
                cur = []
        cur.append(b)
    if cur:
        rows.append(sorted(cur))
    return rows


def columns(rows, tol=5.0):
    """Right edges of the number columns: clusters of x1 over single-number boxes."""
    edges = sorted(b[2] for r in rows for b in r if NUM.match(b[4].replace(" ", "")) and " " not in b[4])
    clusters = []
    for x in edges:
        if clusters and x - clusters[-1][-1] <= tol:
            clusters[-1].append(x)
        else:
            clusters.append([x])
    n_rows = len(rows)
    keep = [float(np.median(c)) for c in clusters if len(c) >= max(3, 0.25 * n_rows)]
    return keep


def rec(crop, scale, gray):
    big = cv2.resize(crop, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
    if gray:
        big = cv2.cvtColor(cv2.cvtColor(big, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
    big = cv2.copyMakeBorder(big, 12, 12, 12, 12, cv2.BORDER_REPLICATE)
    res = eng_rec(big, use_det=False, use_cls=False, use_rec=True)
    txts = getattr(res, "txts", None)
    return (txts[0] if txts else "").strip().replace(" ", "")


def ink_mask(crop):
    g = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY).astype(int)
    return np.abs(g - np.median(g)) > 70


def has_ink(crop):
    return ink_mask(crop).sum() >= 6


def tighten(crop, pad=5):
    # Cut the crop to the columns that hold ink, so a label in a wide cell is not lost in white.
    cols_with_ink = np.where(ink_mask(crop).any(axis=0))[0]
    if len(cols_with_ink) == 0:
        return crop
    a, b = max(0, cols_with_ink[0] - pad), min(crop.shape[1], cols_with_ink[-1] + pad + 1)
    return crop[:, a:b]


def read(path):
    img = cv2.imread(str(path))
    H, W = img.shape[:2]
    rows = group_rows(detect(img))
    cols = columns(rows)
    if PROJ:
        # Fallback when detection merged whole rows into one box: take the columns from the
        # ink itself. Over all rows, runs of ink separated by a gap of 5 px or more are columns.
        mask = np.zeros(W, dtype=bool)
        for r in rows:
            y0, y1 = max(0, int(min(b[1] for b in r))), min(H, int(max(b[3] for b in r)) + 1)
            mask |= ink_mask(img[y0:y1]).any(axis=0)
        cols, run_end, gap = [], None, 0
        for x in range(W):
            if mask[x]:
                run_end, gap = x, 0
            elif run_end is not None:
                gap += 1
                if gap == 5:
                    cols.append(float(run_end))
                    run_end = None
        if run_end is not None:
            cols.append(float(run_end))
    out_rows = []
    for r in rows:
        y0, y1 = max(0, int(min(b[1] for b in r)) - 2), min(H, int(max(b[3] for b in r)) + 3)
        joined = " ".join(b[4] for b in r)
        numeric = sum(bool(re.search(r"\d", b[4])) for b in r)
        if numeric == 0 or not cols:
            out_rows.append({"kind": "text", "y": [y0, y1], "text": joined})
            continue
        a, b2 = [], []
        left = 0.0
        for x1 in cols:
            xa, xb = max(0, int(left) + 2), min(W, int(x1) + 4)
            crop = img[y0:y1, xa:xb]
            if crop.size == 0 or not has_ink(crop):
                a.append("")
                b2.append("")
            else:
                crop = tighten(crop)
                a.append(rec(crop, 4, False))
                b2.append(rec(crop, 5, True))
            left = x1
        out_rows.append({"kind": "data", "y": [y0, y1], "cells": a, "alt": b2, "text": joined})
    return {"cols": cols, "rows": out_rows, "size": [W, H]}


if __name__ == "__main__":
    keys = [a for a in sys.argv[1:] if not a.startswith("-")]
    out_path = G / "cells.json"
    out = json.loads(out_path.read_text(encoding="utf-8")) if out_path.exists() else {}
    for key in keys:
        out[key] = read(G / f"{key}.png")
        out_path.write_text(json.dumps(out), encoding="utf-8")
        d = out[key]
        diff = sum(x != y for r in d["rows"] if r["kind"] == "data" for x, y in zip(r["cells"], r["alt"]))
        print(key, "cols", len(d["cols"]), "rows", len(d["rows"]), "cells where the two readings differ:", diff, flush=True)
        if "-v" in sys.argv:
            pass
