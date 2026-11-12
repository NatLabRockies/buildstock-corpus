"""Surface-fit check for the single-block grids.

These grids are outputs of fitted performance curves, so the printed values should lie on a
low-order polynomial surface in (Tair, Twater) to within rounding. Fit polynomials of
increasing order by least squares and report the largest residual in units of the last
printed digit. If the surface fits to about half a unit, a single misread digit (an error of
at least one unit) would stand out; cells with a residual over 0.8 unit are listed.
"""
import json
import os
import sys
from pathlib import Path

import numpy as np

G = Path(os.environ.get("GRID_DIR", "."))  # working folder: images in, JSON out
grids = json.loads((G / "grids.json").read_text(encoding="utf-8"))


def dec(s):
    return len(s.split(".")[1]) if "." in s else 0


for key, blocks in grids.items():
    if len(blocks) != 1 or (sys.argv[1:] and key not in sys.argv[1:]):
        continue
    b = blocks[0]
    nl = b["n_label"]
    try:
        xs = np.array([float(v) for v in b["header"][-1][nl:]])
        ys = np.array([float(r[nl - 1]) for r in b["rows"]])
        z = np.array([[float(v) for v in r[nl:]] for r in b["rows"]])
    except (ValueError, IndexError) as exc:
        print(key, "cannot parse:", exc)
        continue
    unit = 10.0 ** (-max(dec(v) for r in b["rows"] for v in r[nl:]))
    X, Y = np.meshgrid((xs - xs.mean()) / xs.std(), (ys - ys.mean()) / ys.std())
    best = None
    for order in (2, 3, 4):
        A = np.stack([X.ravel() ** i * Y.ravel() ** j for i in range(order + 1) for j in range(order + 1)], axis=1)
        coef, *_ = np.linalg.lstsq(A, z.ravel(), rcond=None)
        res = (z.ravel() - A @ coef).reshape(z.shape) / unit
        best = (order, res)
        if np.abs(res).max() <= 0.8:
            break
    order, res = best
    bad = np.argwhere(np.abs(res) > 0.8)
    print(f"{key}: {z.shape[0]}x{z.shape[1]}, order {order}, max residual {np.abs(res).max():.2f} unit(s), "
          f"{len(bad)} cell(s) over 0.8")
    for i, j in bad[:10]:
        print(f"     row {ys[i]:g} col {xs[j]:g}: printed {b['rows'][i][nl + j]}, residual {res[i, j]:+.2f} unit")
