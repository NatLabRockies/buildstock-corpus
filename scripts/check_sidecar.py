"""Dry-run one overlay sidecar against its processed document, without building.

`bsc build` is the real test of a sidecar, but it rebuilds the whole release and rewrites
processed/. While a sidecar is being written this applies just that one, in memory, to the
document as it is on disk, and prints what the build would: which tables, figures and
checked entries hold, and every warning. Nothing is written.

    uv run python scripts/check_sidecar.py --product resstock \
        --release resstock_amy2018_2025_release_1 upgrade_measures measure_pdfs/96635.pdf

Run it on a document that has not been patched yet (its sidecar never built). On an
already-patched document the table and figure entries report as already injected or stale,
because their anchors are gone; rebuild with --no-overlays into a --work-dir to re-check one.
The two links (source_url, publication_url) are not checked here: stamp them afterwards
with scripts/stamp_overlay_links.py.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from buildstock_corpus import overlay as O  # noqa: E402
from buildstock_corpus.normalize import Document  # noqa: E402
from buildstock_corpus.paths import manifest_file, processed_root  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--product", required=True)
    ap.add_argument("--release", required=True)
    ap.add_argument("source_id")
    ap.add_argument("source_path", help="as in the sidecar, e.g. measure_pdfs/96635.pdf")
    args = ap.parse_args()

    manifest = json.loads(manifest_file(args.product, args.release).read_text(encoding="utf-8"))
    artifact = next(
        (a for s in manifest["sources"] if s["id"] == args.source_id
         for a in s["artifacts"] if a["source_path"] == args.source_path),
        None,
    )
    if artifact is None:
        raise SystemExit(f"no artifact {args.source_id}/{args.source_path} in the manifest")
    out = processed_root(args.product, args.release) / artifact["output_path"]
    text = out.read_text(encoding="utf-8")
    body = text.split("\n", 1)[1] if text.startswith("<!--") else text  # drop the line-1 header

    doc = Document(
        product=args.product, release=args.release, source_id=args.source_id,
        source_type=artifact.get("source_type", "pdf"), source_path=args.source_path,
        title=artifact.get("title") or "", body=body,
    )
    applied, warnings = O.apply_overlays(
        [doc], args.product, args.release,
        image_dirs={(args.source_id, args.source_path): out.parent},
        input_shas={args.source_id: {args.source_path: artifact.get("input_sha256")}},
    )
    record = applied.get(args.source_id, {}).get(args.source_path, {})
    print(f"sidecar for {args.source_id}/{args.source_path}")
    print(f"  tables applied : {record.get('tables_applied', [])}")
    print(f"  tables checked : {record.get('tables_checked', [])}")
    print(f"  figures applied: {len(record.get('figures_applied', []))}")
    print(f"  text repairs   : {record.get('text_repairs_applied', 0)}")
    print(f"  warnings       : {len(warnings)}")
    for w in warnings:
        print(f"    - {w}")
    raise SystemExit(1 if warnings else 0)


if __name__ == "__main__":
    main()
