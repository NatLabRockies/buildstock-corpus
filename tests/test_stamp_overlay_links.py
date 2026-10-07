"""stamp_overlay_links inserts the two links as text so a sidecar's comment block survives,
places them after source_path (adding source_id/source_path when a sidecar lacks them), and
is idempotent: re-running updates values in place and changes nothing when they agree."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "stamp_overlay_links", Path(__file__).resolve().parents[1] / "scripts" / "stamp_overlay_links.py"
)
S = importlib.util.module_from_spec(spec)
sys.modules["stamp_overlay_links"] = S
spec.loader.exec_module(S)

HEADER = "# Hand-authored figure descriptions for measure PDF 92504\n# (a long comment block)\n#\n"
FULL = HEADER + (
    "product: comstock\nrelease: comstock_amy2018_2025_release_3\n"
    "source_id: upgrade_measures\nsource_path: measure_pdfs/92504.pdf\n"
    "figures:\n- source_image: x.png\n"
)
ARGS = ("upgrade_measures", "measure_pdfs/92504.pdf",
        "https://docs.nlr.gov/docs/fy26osti/92504.pdf", "https://docs.nlr.gov/docs/fy26osti/92504.pdf")


def test_links_go_right_after_source_path_and_comments_survive():
    out = S.stamp(FULL, *ARGS)
    assert out.startswith(HEADER)
    lines = out.split("\n")
    i = lines.index("source_path: measure_pdfs/92504.pdf")
    assert lines[i + 1] == "source_url: https://docs.nlr.gov/docs/fy26osti/92504.pdf"
    assert lines[i + 2] == "publication_url: https://docs.nlr.gov/docs/fy26osti/92504.pdf"
    assert lines[i + 3] == "figures:"


def test_missing_identity_keys_are_added_after_release():
    bare = HEADER + "product: comstock\nrelease: comstock_amy2018_2025_release_3\nfigures:\n- source_image: x.png\n"
    lines = S.stamp(bare, *ARGS).split("\n")
    i = lines.index("release: comstock_amy2018_2025_release_3")
    assert lines[i + 1:i + 5] == [
        "source_id: upgrade_measures", "source_path: measure_pdfs/92504.pdf",
        "source_url: https://docs.nlr.gov/docs/fy26osti/92504.pdf",
        "publication_url: https://docs.nlr.gov/docs/fy26osti/92504.pdf",
    ]


def test_stamp_is_idempotent_and_updates_in_place():
    once = S.stamp(FULL, *ARGS)
    assert S.stamp(once, *ARGS) == once
    changed = S.stamp(once, ARGS[0], ARGS[1], "https://www.nlr.gov/docs/fy26osti/92504.pdf", ARGS[3])
    assert changed.count("source_url:") == 1
    assert "source_url: https://www.nlr.gov/docs/fy26osti/92504.pdf" in changed
