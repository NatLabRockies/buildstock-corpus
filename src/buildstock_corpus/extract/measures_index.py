"""Parse the upgrade-measures index page — the authoritative measure -> doc map.

Each table row maps a measure id to its canonical documentation and the release it
first appeared in. Links come in four forms:
  * internal Jekyll page  [Name]({{site.baseurl}}{% link docs/.../page.md %})
  * external PDF          [Name](https://docs.nlr.gov/.../NNNN.pdf)
  * reference-style       [Name][8]     with  [8]:../../assets/files/....pdf  at the bottom
  * no link (plain text)  Name**        -> "documentation expected soon" = a tracked gap

This one parser is shared by fetch (to discover which local PDFs to hash) and build
(to attach measure identity to extracted docs and to build the crosswalk).
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import PurePosixPath

_REF_DEF_RE = re.compile(r"^\[(\d+)\]:\s*(.+?)\s*$", re.MULTILINE)
# First cell captured loosely so combined rows ("dr_0005 / dr_0006", one shared doc)
# yield one ref per id; rows whose first cell holds no measure id are skipped.
_ROW_RE = re.compile(r"^\|\s*([^|]*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$", re.MULTILINE)
_MEASURE_ID_RE = re.compile(r"[a-z]+_\d+")
_INLINE_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_REF_LINK_RE = re.compile(r"\[([^\]]+)\]\[(\d+)\]")
_LIQUID_LINK_RE = re.compile(r"\{%\s*link\s+(.+?)\s*%\}")
_SUP_RE = re.compile(r"<sup>.*?</sup>")


@dataclass
class MeasureRef:
    measure_id: str
    name: str
    initial_release: str
    kind: str  # internal_md | external_pdf | local_pdf | none
    target: str | None  # repo-relative path (internal_md/local_pdf) or URL (external_pdf)


def _clean_name(raw: str) -> str:
    name = _SUP_RE.sub("", raw)
    return name.replace("*", "").strip()


def _resolve_relative(target: str, index_dir: str) -> str:
    """Resolve a link relative to the index page's dir into a repo-relative posix path,
    collapsing '.' and '..' segments (PurePosixPath does not collapse '..')."""
    parts: list[str] = []
    for seg in f"{index_dir}/{target}".split("/"):
        if seg in ("", "."):
            continue
        if seg == "..":
            if parts:
                parts.pop()
        else:
            parts.append(seg)
    return "/".join(parts)


def _classify(target: str, index_dir: str) -> tuple[str, str]:
    """Return (kind, resolved_target) for a raw link target."""
    liquid = _LIQUID_LINK_RE.search(target)
    if liquid:
        return "internal_md", liquid.group(1).strip()
    low = target.lower()
    if low.startswith(("http://", "https://")):
        return ("external_pdf" if low.endswith(".pdf") else "external_other", target)
    if low.endswith(".pdf"):
        return "local_pdf", _resolve_relative(target, index_dir)
    return "external_other", target


def parse_index(text: str, index_page_path: str) -> list[MeasureRef]:
    """Parse the index markdown into MeasureRefs, in table order.

    index_page_path is the repo-relative path of the index page, used to resolve
    reference-style relative links (e.g. ../../assets/files/foo.pdf).
    """
    index_dir = PurePosixPath(index_page_path).parent.as_posix()
    refs = {n: t for n, t in _REF_DEF_RE.findall(text)}

    out: list[MeasureRef] = []
    for id_cell, cell, release in _ROW_RE.findall(text):
        ids = _MEASURE_ID_RE.findall(id_cell)
        if not ids:
            continue  # header / separator / non-measure table rows
        release = _clean_name(release) or "unknown"
        inline = _INLINE_LINK_RE.search(cell)
        refl = _REF_LINK_RE.search(cell)
        if inline:
            name = _clean_name(inline.group(1))
            kind, target = _classify(inline.group(2), index_dir)
        elif refl and refl.group(2) in refs:
            name = _clean_name(refl.group(1))
            kind, target = _classify(refs[refl.group(2)], index_dir)
        else:
            name = _clean_name(_INLINE_LINK_RE.sub("", cell))
            kind, target = "none", None
        for measure_id in ids:  # combined rows share one doc across several measures
            out.append(MeasureRef(measure_id, name, release, kind, target))
    return out


def local_pdf_paths(refs: list[MeasureRef]) -> list[str]:
    """Repo-relative paths of local PDFs referenced by the index (deduped, sorted)."""
    return sorted({r.target for r in refs if r.kind == "local_pdf" and r.target})
