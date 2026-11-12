"""Structure and arithmetic checks on the cell-wise readings; writes grids.json.

For each image: split into blocks at title rows; within a block, header rows (a non-numeric
label cell) then data rows. Checks:
  A  the two recognitions of each cell agree
  B  every value cell is a number with the block's number of decimals
  C  appendix figures: Manufacturer - Curvefit = Difference in every cell (to rounding)
  D  smoothness: a cell whose second difference along its row or column stands out
  E  row labels and column headers are strictly monotonic
Anything flagged is printed; nothing is corrected here. Corrections go in OVERRIDES, each
one made after looking at the image.
"""
import json
import os
import re
import sys
from pathlib import Path

import numpy as np

G = Path(os.environ.get("GRID_DIR", "."))  # working folder: images in, JSON out
NUM = re.compile(r"^-?\d+(?:\.\d+)?$")
OVERRIDES = json.loads((G / "overrides.json").read_text(encoding="utf-8")) if (G / "overrides.json").exists() else {}


def dec(s):
    return len(s.split(".")[1]) if "." in s else 0


def blocks_of(img, key, flags):
    blocks, cur = [], {"title": None, "header": [], "rows": []}
    for ri, r in enumerate(img["rows"]):
        if r["kind"] == "text":
            if cur["header"] or cur["rows"]:
                blocks.append(cur)
            cur = {"title": r["text"], "header": [], "rows": []}
            continue
        cells = list(r["cells"])
        for ci, (a, b) in enumerate(zip(r["cells"], r["alt"])):
            ov = OVERRIDES.get(key, {}).get(f"{ri},{ci}")
            if ov is not None:
                cells[ci] = ov
            elif a != b:
                flags.append(f"A r{ri}c{ci}: two readings differ: {a!r} vs {b!r}")
        nonnum = [c for c in cells if c and not NUM.match(c)]
        if nonnum and not cur["rows"]:
            cur["header"].append((ri, cells))
        else:
            if nonnum:
                flags.append(f"B r{ri}: non-numeric cell(s) in a data row: {nonnum}")
            cur["rows"].append((ri, cells))
    if cur["header"] or cur["rows"]:
        blocks.append(cur)
    return blocks


def values(block, n_label):
    return [[c for c in cells[n_label:]] for _, cells in block["rows"]]


def check_block(block, flags, name):
    rows = block["rows"]
    if not rows:
        flags.append(f"B {name}: no data rows")
        return None
    # label columns: leading columns; values start at the first column of the header's numbers
    n_label = block["n_label"]
    vals = values(block, n_label)
    decs = [dec(c) for row in vals for c in row if c]
    mode = max(set(decs), key=decs.count) if decs else 0
    arr = np.full((len(vals), len(vals[0])), np.nan)
    for i, (ri, _) in enumerate(rows):
        for j, c in enumerate(vals[i]):
            if not c:
                flags.append(f"B {name} r{ri}c{j + n_label}: empty value cell")
            elif not NUM.match(c):
                pass
            else:
                if dec(c) != mode:
                    flags.append(f"B {name} r{ri}c{j + n_label}: {c!r} has {dec(c)} decimals, block has {mode}")
                arr[i, j] = float(c)
    # E: labels monotonic
    for k in range(n_label):
        lab = [cells[k] for _, cells in rows]
        if all(NUM.match(x or "") for x in lab):
            f = [float(x) for x in lab]
            if not all(b > a for a, b in zip(f, f[1:])):
                flags.append(f"E {name}: row labels (column {k}) not increasing: {lab}")
        else:
            flags.append(f"E {name}: row label column {k} has a non-number: {lab}")
    for ri, cells in block["header"]:
        h = cells[n_label:]
        if all(NUM.match(x or "") for x in h):
            f = [float(x) for x in h]
            if not all(b > a for a, b in zip(f, f[1:])):
                flags.append(f"E {name}: header r{ri} not increasing: {h}")
        else:
            flags.append(f"E {name}: header r{ri} has a non-number: {h}")
    # D: smoothness
    unit = 10.0 ** (-mode)
    for axis in (0, 1):
        a = arr if axis == 1 else arr.T
        for i, row in enumerate(a):
            if len(row) < 4 or np.isnan(row).any():
                continue
            d2 = row[:-2] - 2 * row[1:-1] + row[2:]
            med = np.median(d2)
            mad = np.median(np.abs(d2 - med)) + unit
            for j, v in enumerate(d2):
                if abs(v - med) > max(6 * mad, 4 * unit):
                    r_, c_ = (i, j + 1) if axis == 1 else (j + 1, i)
                    flags.append(f"D {name} near r{rows[r_][0]}c{c_ + n_label} (value {arr[r_, c_]}): "
                                 f"second difference {v:.4g} vs typical {med:.4g} along {'row' if axis == 1 else 'column'}")
    return arr, mode


def main():
    cells = json.loads((G / "cells.json").read_text(encoding="utf-8"))
    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    out = {}
    total = 0
    for key, img in cells.items():
        if only and key not in only:
            continue
        flags = []
        blocks = blocks_of(img, key, flags)
        arrs = []
        for b in blocks:
            # number of label columns = leading columns that are non-numeric or empty in the last header row
            last = b["header"][-1][1] if b["header"] else []
            n_label = 0
            for c in last:
                if c and NUM.match(c):
                    break
                n_label += 1
            if not b["header"]:
                n_label = 1
            b["n_label"] = max(1, n_label)
            res = check_block(b, flags, b["title"] or "grid")
            arrs.append(res)
        # C: appendix arithmetic
        titles = [(b["title"] or "").lower() for b in blocks]
        if len(blocks) == 3 and "manufacturer" in titles[0] and "curve" in titles[1] and "diff" in titles[2] and all(arrs):
            (m, _), (c, _), (d, dm) = arrs
            if m.shape == c.shape == d.shape:
                tol = 1.5 * 10.0 ** (-dm) + 1e-9
                bad = np.argwhere(np.abs(m - c - d) > tol)
                for i, j in bad:
                    flags.append(f"C row {i} col {j}: {m[i, j]} - {c[i, j]} = {m[i, j] - c[i, j]:.5g}, Difference says {d[i, j]}")
                n_ok = m.size - len(bad)
                arith = f"arithmetic {n_ok}/{m.size}"
            else:
                flags.append(f"C block shapes differ: {m.shape} {c.shape} {d.shape}")
                arith = "arithmetic n/a"
        else:
            arith = f"{len(blocks)} block(s)"
        out[key] = [{"title": b["title"], "n_label": b["n_label"], "header": [c for _, c in b["header"]],
                     "rows": [c for _, c in b["rows"]]} for b in blocks]
        n_cells = sum(len(c) for b in blocks for _, c in b["rows"])
        total += len(flags)
        print(f"{key}: {len(blocks)} block(s), {n_cells} cells, {arith}, {len(flags)} flag(s)")
        for f in flags[:40 if only else 12]:
            print("    ", f)
    (G / "grids.json").write_text(json.dumps(out, indent=0, ensure_ascii=False), encoding="utf-8")
    print("total flags", total)


if __name__ == "__main__":
    main()
