"""Report figure-description length against the §2.1 depth budget.

The figure-description standard drifted badly between Batch A and Batch C: the two
prototypes the user accepted (85853, 86100) average 45 and 69 words per description,
Batch A landed around 110, and Batches B and C ran ~180. Nobody decided to triple the
depth — each batch just anchored on the previous one, and the rollout got slow enough
that the user asked for it to be rolled back.

Length is a proxy, not the goal. But it is the *observable* proxy: an author who has
stopped enumerating data labels, narrating every panel of a grid, and reconciling figure
values against the prose will land in the 40-70 word band more or less automatically,
and one who hasn't will not. So this script exists to make the drift visible at the end
of a batch, while it is still cheap to trim, rather than at review time.

Reports per-file mean/max and flags:

  OVER    mean description length above the budget ceiling -- the batch drifted
  LONG    an individual description well past the ceiling (listed so you can trim it)
  ALT     an `alt` over the character cap, or containing ']' (which breaks markdown)

Exits non-zero if any *unwaived* file is OVER, so it can gate a batch. Files authored
before the standard changed are waived via GRANDFATHERED -- they are intentionally not
being rewritten, so failing on them forever would just train you to ignore the exit code.
"""

from __future__ import annotations

import argparse
import statistics
import sys
from pathlib import Path

import yaml

OVERLAY_ROOT = Path("overlays")

# §2.1: description 40-70 words (ceiling 70, soft), alt <=120 chars, one line.
MEAN_CEILING = 90       # a batch whose *mean* exceeds this has drifted
SINGLE_CEILING = 130    # an individual description this long gets listed for trimming
ALT_CEILING = 120

# Authored before the 2026-08-21 rollback; deliberately left as-is (see the rollout doc).
GRANDFATHERED = {
    "85853", "86100",
    # Batch A
    "89343", "92546", "95004", "96597", "95006", "87570", "95013", "89126", "89133", "92618",
    # Batch B
    "95009", "95015", "95119", "89132", "89341", "89131", "92502", "87542", "89340", "89481",
    # Batch C
    "95014", "86897", "98223", "92504", "89120", "98345", "98346", "86585", "89117", "86105",
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="*", type=Path,
                    help="overlay YAML files to check (default: all under overlays/)")
    ap.add_argument("--all", action="store_true",
                    help="include grandfathered pre-rollback files in the pass/fail decision")
    args = ap.parse_args()

    files = args.paths or sorted(OVERLAY_ROOT.rglob("*.yaml"))
    failed = []
    checked = 0

    for path in files:
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        figs = [f for f in (doc.get("figures") or []) if not f.get("decorative")]
        if not figs:
            continue

        checked += 1
        stem = path.stem
        waived = stem in GRANDFATHERED and not args.all
        words = [len((f.get("description") or "").split()) for f in figs]
        mean = statistics.mean(words)

        status = "OVER" if mean > MEAN_CEILING else "ok"
        note = "  (pre-rollback, waived)" if waived and status == "OVER" else ""
        print(f"{stem:9} {len(figs):>3} figs   mean {mean:>5.0f}w   max {max(words):>4}w   "
              f"{status}{note}")

        if status == "OVER" and not waived:
            failed.append(stem)

        for fig in figs:
            name = (fig.get("source_image") or "?").split("/")[-1]
            n = len((fig.get("description") or "").split())
            if n > SINGLE_CEILING and not waived:
                print(f"    LONG  {n:>4}w  {name}")
            alt = fig.get("alt") or ""
            if len(alt) > ALT_CEILING and not waived:
                print(f"    ALT   {len(alt):>4}c  {name}  (cap {ALT_CEILING})")
            # Not a budget question -- ']' breaks the markdown alt, so report it anywhere.
            if "]" in alt:
                print(f"    ALT   ']' in alt  {name}  (breaks the markdown alt)")

    print(f"\n{checked} overlay file(s) with figures.")
    if failed:
        print(f"drifted past the {MEAN_CEILING}-word mean ceiling: {', '.join(failed)}")
        print("Trim before opening the PR, or revisit §2.1 in the rollout doc.")
        return 1
    print(f"All non-waived files within the {MEAN_CEILING}-word mean ceiling.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
