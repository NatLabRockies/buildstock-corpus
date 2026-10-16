"""Which of a measure PDF's leading bitmaps are decorative, and the comment that stands in (W6.1).

docling names a PDF's extracted bitmaps image_000000, image_000001, ... in page order. The
figure-description standard skips decorative images on purpose (no overlay entry), so they
reach the markdown as bare ``![Image](...)`` refs to files a clone does not even have. Build
replaces each with a comment naming the omission, so a report's first screen is text, and
validate fails if one survives. Which leading indices are decorative depends on where the
PDF came from:

* an OSTI measure report (``measure_pdfs/<osti number>.pdf``) opens with the NREL cover
  photo grid (image_000000) and the NREL wordmark (image_000001);
* a measure doc the ComStock site serves itself (``assets/files/ComStock Measure Doc_*.pdf``)
  has no cover grid: image_000000 is the ComStock wordmark and image_000001 is already
  Figure 1, a real diagram that must stay visible.

Only an *undescribed* ref is ever touched: a described figure's alt text is its description.
Shared by build and manifest so the omission and the check cannot drift apart.
"""

from __future__ import annotations

import re

# A bare docling ref to one of a PDF's first two bitmaps, on a line of its own.
DECORATIVE_REF_RE = re.compile(
    r"^!\[Image\]\((?P<path>[^)\s]*image_(?P<idx>00000[01])_[0-9a-f]+\.png)\)\s*$", re.M
)

# Source-path prefix of the PDFs the ComStock site serves itself (the `local_pdfs` of a
# source; see sources/*.yaml). Every other PDF document is an OSTI measure report.
SITE_PDF_PREFIX = "assets/files/"

_OSTI_REPORT = {"000000": "cover art", "000001": "wordmark"}
_SITE_DOC = {"000000": "wordmark"}


def decorative_indices(source_path: str) -> dict[str, str]:
    """image index -> label of the leading bitmaps that are decorative in this PDF."""
    return _SITE_DOC if source_path.startswith(SITE_PDF_PREFIX) else _OSTI_REPORT


def omission_comment(idx: str, label: str) -> str:
    """The line build writes in place of an omitted decorative image ref."""
    return f"<!-- decorative image omitted: image_{idx} ({label}; no description by the figure standard) -->"


def surviving_decorative_refs(source_path: str, text: str) -> list[str]:
    """The undescribed decorative refs still present in a built PDF document (for validate)."""
    decorative = decorative_indices(source_path)
    return [
        m.group(0).strip()
        for m in DECORATIVE_REF_RE.finditer(text)
        if m.group("idx") in decorative
    ]
