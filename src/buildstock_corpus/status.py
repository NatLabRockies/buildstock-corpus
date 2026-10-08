"""Publication status: one vocabulary for how a document reached the public.

Status is data, not a folder name. Output directories get renamed and do not travel with
a file fetched over HTTPS; a field does. The three values, decided by the corpus owner on
2026-10-06:

  osti_pdf   A report with an OSTI number -- citable as a publication in its own right.
             Detected from the publication URL (nlr.gov/docs/fyNNosti/NNNNN.pdf).
  site_page  Published on the ComStock site without an OSTI number. Whether the site
             serves it as a rendered page or as a PDF file does not matter: both are one
             class of document, and both may later be superseded by an OSTI publication.
  missing    Documented nowhere. Only crosswalk rows carry this -- a document that exists
             cannot be missing -- and it is what the crosswalk's tracked gaps resolve to.

Sources whose documents all share one status (the technical reference, the site's own
pages) declare it in the source registry. The measures source derives it per document
from the kind of link the upgrade-measures index page uses (see measures_index._classify),
because one source there mixes OSTI reports with site-served pages and PDFs.
"""

from __future__ import annotations

import re

OSTI_PDF = "osti_pdf"
SITE_PAGE = "site_page"
MISSING = "missing"

STATUSES = frozenset({OSTI_PDF, SITE_PAGE, MISSING})

# NREL/NLR publications: https://www.nlr.gov/docs/fy24osti/89340.pdf and the docs.nlr.gov
# mirror. The fyNNosti path segment is the OSTI number's home; nothing else on these hosts
# has it, and nothing published without an OSTI number is served from under it.
_OSTI_URL_RE = re.compile(r"^https?://(?:[\w-]+\.)*nlr\.gov/docs/fy\d{2}osti/\d+\.pdf$", re.I)


def is_osti_url(url: str | None) -> bool:
    return bool(url) and _OSTI_URL_RE.match(url.strip()) is not None


def status_for_url(url: str) -> str:
    """Status of a document published at an external URL.

    Every external measure document the corpus holds today is an OSTI report. A URL that
    is not one has no value in the vocabulary yet, so it is an error for the owner to
    rule on rather than a guess: silently calling it `site_page` would misname a document
    that is not on the ComStock site.
    """
    if is_osti_url(url):
        return OSTI_PDF
    raise ValueError(
        f"no publication status for external URL {url!r}: not an OSTI report; "
        f"extend the vocabulary in status.py or fix the link in the index page"
    )


def status_for_kind(kind: str, target: str | None = None) -> str:
    """Status for a measures-index link kind (measures_index.MeasureRef.kind).

    internal_md and local_pdf are both things the ComStock site serves; external_pdf is
    judged by its URL; everything else (no link, a non-PDF external link, a measure the
    index never lists) is documentation that does not exist yet.
    """
    if kind in ("internal_md", "local_pdf"):
        return SITE_PAGE
    if kind == "external_pdf":
        return status_for_url(target or "")
    return MISSING


def check_status(value: str | None, where: str) -> str:
    """Return `value` if it is in the vocabulary, else raise naming the offender."""
    if value not in STATUSES:
        raise ValueError(
            f"{where}: status {value!r} is not one of {sorted(STATUSES)}"
        )
    return value
