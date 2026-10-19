"""Load and validate the per-release source registry (sources/<product>_<release>.yaml)."""

from __future__ import annotations

import re
from dataclasses import dataclass, field

import yaml

from .links import is_absolute_https
from .paths import sources_file
from .status import STATUSES

SOURCE_TYPES = {"latex", "markdown", "measures"}

# How each product spells its own name in prose (the map, the query prompt). A product
# not listed here is title-cased, which is wrong for CamelCase names: add it.
PRODUCT_NAMES = {"comstock": "ComStock", "resstock": "ResStock"}


def product_name(product: str) -> str:
    return PRODUCT_NAMES.get(product, product.title())

# Defaults for the per-product knobs below. They are the ComStock values, so a registry
# written before the fields existed keeps meaning exactly what it did.
DEFAULT_MEASURE_ID_PATTERN = r"[a-z]+_\d+"  # hvac_0001, env_0003, pkg_0012
DEFAULT_BIBLIOGRAPHY = "bibliography.bib"  # relative to the LaTeX project dir
DEFAULT_IMAGES_DIR = "figures"  # likewise; where \includegraphics targets live


@dataclass
class Source:
    id: str
    type: str
    repo: str
    git_ref: str
    sparse: list[str] = field(default_factory=list)
    # type-specific (only some are set depending on `type`)
    root_hint: str | None = None
    doc_glob: str | None = None
    latex_main: str | None = None
    # latex only: the BibTeX file pandoc resolves citations from, and the directory that
    # \includegraphics targets live in, both relative to latex_main's directory. ComStock's
    # project uses bibliography.bib and figures/; ResStock's files/refs.bib and images/.
    bibliography: str = DEFAULT_BIBLIOGRAPHY
    images_dir: str = DEFAULT_IMAGES_DIR
    exclude_globs: list[str] = field(default_factory=list)
    index_page: str | None = None
    # measures only. internal_dir holds measure pages the site renders itself; a site whose
    # measures are all external reports has none. The per-release upgrade map is one of two
    # things: a crosswalk CSV committed in the site repo (ComStock) or a JSON lookup published
    # with the dataset (ResStock's OEDI upgrades_lookup.json); at least one is required.
    internal_dir: str | None = None
    crosswalk_csv: str | None = None
    upgrades_lookup_url: str | None = None
    # Regex for a measure id in the index table's first column. Every match in the cell is
    # one measure (a combined row names several). ComStock ids look like hvac_0001; ResStock
    # numbers its measures 1 to 32.
    measure_id_pattern: str = DEFAULT_MEASURE_ID_PATTERN
    # source dir -> output dir, for dirs the corpus must not name the way upstream does.
    # Output-side only: source_path, input hashes, and the fetch/sparse config are never
    # rewritten.
    output_remap: dict[str, str] = field(default_factory=dict)
    # Publication status shared by every document of this source (see status.py). Required
    # for latex/markdown sources; a measures source derives it per document instead.
    status: str | None = None
    # Where the documents are published (see links.py). A markdown or measures source names
    # the live site that renders its pages and serves its files (`site_url`); a latex source
    # names the one publication its chapters are part of (`publication_url`).
    site_url: str | None = None
    publication_url: str | None = None
    # alias URL -> canonical URL, for one upstream file the index page links under more than
    # one spelling (www.nlr.gov vs docs.nlr.gov). Every link to the file is recorded under
    # the canonical one; build refuses an undeclared duplicate rather than picking one.
    canonical_urls: dict[str, str] = field(default_factory=dict)
    # External PDF URLs the index page links that are not corpus documents (release webinar
    # slide decks, for instance). Build skips them; fetch is untouched, so no re-download
    # and no overlay pins move. Recorded in the manifest as excluded_by_registry.
    exclude_urls: list[str] = field(default_factory=list)


@dataclass
class Registry:
    product: str
    release: str
    sources: list[Source]

    def output_remaps(self) -> dict[str, dict[str, str]]:
        """source_id -> {source_dir: output_dir} for sources that rename output dirs."""
        return {s.id: s.output_remap for s in self.sources if s.output_remap}

    def by_id(self, source_id: str) -> Source:
        for s in self.sources:
            if s.id == source_id:
                return s
        raise KeyError(f"no source '{source_id}' in registry {self.product} {self.release}")


def load_registry(product: str, release: str) -> Registry:
    path = sources_file(product, release)
    if not path.exists():
        raise FileNotFoundError(f"no source registry at {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    reg_product = str(data["product"])
    reg_release = str(data["release"])
    if (reg_product, reg_release) != (product, release):
        raise ValueError(
            f"registry {path} declares {reg_product} {reg_release}, expected {product} {release}"
        )

    sources: list[Source] = []
    seen_ids: set[str] = set()
    for raw in data.get("sources", []):
        src = Source(
            id=str(raw["id"]),
            type=str(raw["type"]),
            repo=str(raw["repo"]),
            git_ref=str(raw["git_ref"]),
            sparse=list(raw.get("sparse", [])),
            root_hint=raw.get("root_hint"),
            doc_glob=raw.get("doc_glob"),
            latex_main=raw.get("latex_main"),
            bibliography=str(raw.get("bibliography") or DEFAULT_BIBLIOGRAPHY),
            images_dir=str(raw.get("images_dir") or DEFAULT_IMAGES_DIR),
            exclude_globs=list(raw.get("exclude_globs", [])),
            index_page=raw.get("index_page"),
            internal_dir=raw.get("internal_dir"),
            crosswalk_csv=raw.get("crosswalk_csv"),
            upgrades_lookup_url=raw.get("upgrades_lookup_url"),
            measure_id_pattern=str(raw.get("measure_id_pattern") or DEFAULT_MEASURE_ID_PATTERN),
            output_remap=dict(raw.get("output_remap") or {}),
            status=raw.get("status"),
            site_url=raw.get("site_url"),
            publication_url=raw.get("publication_url"),
            canonical_urls=dict(raw.get("canonical_urls") or {}),
            exclude_urls=list(raw.get("exclude_urls") or []),
        )
        if src.type not in SOURCE_TYPES:
            raise ValueError(f"source '{src.id}': unknown type '{src.type}'")
        if src.id in seen_ids:
            raise ValueError(f"duplicate source id '{src.id}'")
        seen_ids.add(src.id)
        _validate_source(src, path)
        sources.append(src)

    if not sources:
        raise ValueError(f"registry {path} has no sources")
    return Registry(product=reg_product, release=reg_release, sources=sources)


def _validate_source(src: Source, path) -> None:
    required = {
        "latex": ["doc_glob", "latex_main"],
        "markdown": ["doc_glob"],
        "measures": ["index_page"],
    }[src.type]
    missing = [f for f in required if not getattr(src, f)]
    if missing:
        raise ValueError(f"source '{src.id}' ({src.type}) missing required fields: {missing}")
    if src.type == "latex":
        for name in ("bibliography", "images_dir"):
            value = getattr(src, name)
            if not value.strip("/ ") or value.startswith("/") or ".." in value.split("/"):
                raise ValueError(
                    f"source '{src.id}' (latex): {name} must be a relative path inside the "
                    f"LaTeX project dir, got {value!r}"
                )
    if src.type == "measures":
        if not (src.crosswalk_csv or src.upgrades_lookup_url):
            raise ValueError(
                f"source '{src.id}' (measures) needs a per-release upgrade map: set "
                f"crosswalk_csv (a CSV in the site repo) or upgrades_lookup_url (a JSON "
                f"lookup published with the dataset)"
            )
        if src.upgrades_lookup_url is not None and not is_absolute_https(src.upgrades_lookup_url):
            raise ValueError(
                f"source '{src.id}' (measures): upgrades_lookup_url must be an absolute https "
                f"URL, got {src.upgrades_lookup_url!r}"
            )
        try:
            re.compile(src.measure_id_pattern)
        except re.error as exc:
            raise ValueError(
                f"source '{src.id}' (measures): measure_id_pattern {src.measure_id_pattern!r} "
                f"is not a valid regex: {exc}"
            ) from None
        if src.status is not None:
            raise ValueError(
                f"source '{src.id}' (measures) must not set status: it is derived per "
                f"document from the index page's link kinds"
            )
    elif src.status not in STATUSES:
        raise ValueError(
            f"source '{src.id}' ({src.type}): status {src.status!r} must be one of "
            f"{sorted(STATUSES)}"
        )
    # Publication links: a site-backed source must say which site, a latex source which
    # publication. Absolute https only -- these are written into every artifact as-is.
    link_field = "publication_url" if src.type == "latex" else "site_url"
    link = getattr(src, link_field)
    if not is_absolute_https(link):
        raise ValueError(
            f"source '{src.id}' ({src.type}): {link_field} must be an absolute https URL, "
            f"got {link!r}"
        )
    for alias, canonical in src.canonical_urls.items():
        if not (is_absolute_https(alias) and is_absolute_https(canonical)):
            raise ValueError(
                f"source '{src.id}': canonical_urls entries must be absolute https URLs, "
                f"got {alias!r} -> {canonical!r}"
            )
        if alias == canonical or canonical in src.canonical_urls:
            raise ValueError(
                f"source '{src.id}': canonical_urls must map an alias to a canonical URL "
                f"that is not itself an alias ({alias!r} -> {canonical!r})"
            )
    for url in src.exclude_urls:
        if not is_absolute_https(url):
            raise ValueError(
                f"source '{src.id}': exclude_urls entries must be absolute https URLs, got {url!r}"
            )
    for src_dir, out_dir in src.output_remap.items():
        if not str(src_dir).strip("/ ") or not str(out_dir).strip("/ "):
            raise ValueError(
                f"source '{src.id}': output_remap has an empty dir ({src_dir!r} -> {out_dir!r})"
            )
