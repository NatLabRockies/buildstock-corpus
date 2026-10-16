"""Which of a measure PDF's leading bitmaps are decorative, and the comment that stands in (W6.1).

docling names a PDF's extracted bitmaps image_000000, image_000001, ... in page order, each
suffixed with a content hash of the bitmap, so the same picture gets the same name wherever
it is extracted. The figure-description standard skips decorative images on purpose (no
overlay entry), so they reach the markdown as bare ``![Image](...)`` refs to files a clone
does not even have. Build replaces each with a comment naming the omission, so a report's
first screen is text, and validate fails if one survives. Only the first two bitmaps are
ever considered, and which of them are decorative depends on where the PDF came from:

* an OSTI measure report (``measure_pdfs/<osti number>.pdf``) opens with the NREL cover
  photo grid (image_000000) and the NREL wordmark (image_000001);
* a measure doc the ComStock site serves itself (``assets/files/ComStock Measure Doc_*.pdf``)
  has no cover grid. Its decorative bitmaps are the ComStock wordmark, which is image_000000
  wherever docling extracts it, and the "PRE-PUBLICATION" stamp, one bitmap identical across
  documents that docling extracts on its own when a page carries nothing else (the cover of
  HP RTU Higher Compressor Lockout, page iii of PV with Battery Storage). Anything else in
  the first two slots is already Figure 1, a real diagram that must stay visible.

Only an *undescribed* ref is ever touched: a described figure's alt text is its description.
Shared by build and manifest so the omission and the check cannot drift apart, and decided
from the ref alone (index, origin, bitmap hash) so validate needs no image files.
"""

from __future__ import annotations

import re

# A bare docling ref to one of a PDF's first two bitmaps, on a line of its own.
DECORATIVE_REF_RE = re.compile(
    r"^!\[Image\]\((?P<path>[^)\s]*image_(?P<idx>00000[01])_(?P<hash>[0-9a-f]+)\.png)\)\s*$",
    re.M,
)

# Source-path prefix of the PDFs the ComStock site serves itself (the `local_pdfs` of a
# source; see sources/*.yaml). Every other PDF document is an OSTI measure report.
SITE_PDF_PREFIX = "assets/files/"

# docling's name hash for the site docs' "PRE-PUBLICATION" stamp bitmap (402x410 px). A stamp
# rendered differently in a future document gets a different hash and simply stays visible,
# which is the safe failure: this rule can never hide a real figure.
PREPUB_WATERMARK_HASH = "a27ad8a4f51fb12164031d26c2a57ee089a2c899a7847e204fd3180f19454904"

_OSTI_REPORT = {"000000": "cover art", "000001": "wordmark"}


def decorative_label(source_path: str, idx: str, name_hash: str) -> str | None:
    """What a PDF's leading bitmap `idx` (named with `name_hash`) is, if it is decorative.

    None means it is a figure the build must leave alone.
    """
    if not source_path.startswith(SITE_PDF_PREFIX):
        return _OSTI_REPORT.get(idx)
    if name_hash == PREPUB_WATERMARK_HASH:
        return "pre-publication watermark"
    if idx == "000000":
        return "wordmark"
    return None


def omission_comment(idx: str, label: str) -> str:
    """The line build writes in place of an omitted decorative image ref."""
    return f"<!-- decorative image omitted: image_{idx} ({label}; no description by the figure standard) -->"


def surviving_decorative_refs(source_path: str, text: str) -> list[str]:
    """The undescribed decorative refs still present in a built PDF document (for validate)."""
    return [
        m.group(0).strip()
        for m in DECORATIVE_REF_RE.finditer(text)
        if decorative_label(source_path, m.group("idx"), m.group("hash")) is not None
    ]
