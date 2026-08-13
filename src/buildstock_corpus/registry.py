"""Load and validate the per-release source registry (sources/<product>_<release>.yaml)."""

from __future__ import annotations

from dataclasses import dataclass, field

import yaml

from .paths import sources_file

SOURCE_TYPES = {"latex", "markdown", "measures"}


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
    exclude_globs: list[str] = field(default_factory=list)
    index_page: str | None = None
    internal_dir: str | None = None
    crosswalk_csv: str | None = None
    # source dir -> output dir, for dirs the corpus must not name the way upstream does
    # (e.g. upstream "docs" holds pages absent from the live site). Output-side only:
    # source_path, input hashes, and the fetch/sparse config are never rewritten.
    output_remap: dict[str, str] = field(default_factory=dict)


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
            exclude_globs=list(raw.get("exclude_globs", [])),
            index_page=raw.get("index_page"),
            internal_dir=raw.get("internal_dir"),
            crosswalk_csv=raw.get("crosswalk_csv"),
            output_remap=dict(raw.get("output_remap") or {}),
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
        "measures": ["index_page", "internal_dir", "crosswalk_csv"],
    }[src.type]
    missing = [f for f in required if not getattr(src, f)]
    if missing:
        raise ValueError(f"source '{src.id}' ({src.type}) missing required fields: {missing}")
    for src_dir, out_dir in src.output_remap.items():
        if not str(src_dir).strip("/ ") or not str(out_dir).strip("/ "):
            raise ValueError(
                f"source '{src.id}': output_remap has an empty dir ({src_dir!r} -> {out_dir!r})"
            )
