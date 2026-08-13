"""Build processed artifacts for a release: extract every fetched source into cleaned
markdown, write them under processed/<product>/<release>/<source_id>/, join measures to
their docs via the crosswalk, and emit chunks.jsonl for indexing.

Build is driven by fetch_state.json (not a fresh glob) so the processed set matches
exactly what fetch hashed — keeping the provenance chain intact.
"""

from __future__ import annotations

import json
import shutil
from collections import defaultdict
from pathlib import Path

from .chunk import chunk_documents
from .extract.crosswalk import build_crosswalk
from .extract.latex import load_latex_docs
from .extract.markdown import load_markdown_docs
from .extract.measures_index import MeasureRef, parse_index
from .extract.pdf import PdfSpec, load_pdf_docs
from .manifest import build_manifest
from .normalize import Document
from .paths import chunks_file, manifest_file, output_rel, processed_root, raw_root, remap_dir
from .registry import Source, load_registry


def _load_fetch_state(product: str, release: str) -> dict:
    path = raw_root(product, release) / "fetch_state.json"
    if not path.exists():
        raise FileNotFoundError(f"no fetch_state.json at {path}; run `bsc fetch` first")
    return json.loads(path.read_text(encoding="utf-8"))


def _clone_dir(product: str, release: str, src: Source) -> Path:
    return raw_root(product, release) / "repos" / f"{Path(src.repo).stem}@{src.git_ref}"


def _index_refs(clone_dir: Path, src_state: dict) -> list[MeasureRef]:
    """Parse the measures index page (hashed by fetch) into measure->doc refs."""
    idx = src_state.get("index_page")
    if not idx:
        return []
    text = (clone_dir / idx["path"]).read_text(encoding="utf-8", errors="replace")
    return parse_index(text, idx["path"])


def _measure_extra(refs: list[MeasureRef]) -> dict:
    """Fold one-or-more measure identities (shared docs) into chunk-metadata scalars."""
    if not refs:
        return {}
    dedupe = dict.fromkeys  # preserve order, drop dups
    return {
        "measure_id": ",".join(r.measure_id for r in refs),
        "measure_name": "; ".join(dedupe(r.name for r in refs)),
        "measure_initial_release": ",".join(dedupe(r.initial_release for r in refs)),
    }


def _pdf_specs(
    product: str, release: str, clone_dir: Path, src_state: dict, refs: list[MeasureRef]
) -> list[PdfSpec]:
    """Build one PdfSpec per physical PDF, aggregating every measure that cites it."""
    url_refs: dict[str, list[MeasureRef]] = defaultdict(list)
    local_refs: dict[str, list[MeasureRef]] = defaultdict(list)
    for r in refs:
        if r.kind == "external_pdf" and r.target:
            url_refs[r.target].append(r)
        elif r.kind == "local_pdf" and r.target:
            local_refs[r.target].append(r)

    specs: list[PdfSpec] = []

    # External PDFs: several mirror URLs may resolve to one deduped file -> group by path.
    path_urls: dict[str, list[str]] = defaultdict(list)
    path_sha: dict[str, str] = {}
    for e in src_state.get("external_pdfs", []):
        path_urls[e["path"]].append(e["url"])
        path_sha[e["path"]] = e["sha256"]
    for path, urls in path_urls.items():
        here = [r for u in urls for r in url_refs.get(u, [])]
        specs.append(
            PdfSpec(
                source_path=path,
                abs_path=raw_root(product, release) / path,
                sha256=path_sha[path],
                title=here[0].name if here else None,
                extra=_measure_extra(here),
            )
        )

    # Local PDFs live in the clone (reference-style links to assets/files/*.pdf).
    for lp in src_state.get("local_pdfs", []):
        here = local_refs.get(lp["path"], [])
        specs.append(
            PdfSpec(
                source_path=lp["path"],
                abs_path=clone_dir / lp["path"],
                sha256=lp["sha256"],
                title=here[0].name if here else None,
                extra=_measure_extra(here),
            )
        )
    return specs


def _attach_internal_measure_identity(docs: list[Document], refs: list[MeasureRef]) -> None:
    """Tag internal measure pages with their measure id (index internal_md target = path)."""
    by_path: dict[str, list[MeasureRef]] = defaultdict(list)
    for r in refs:
        if r.kind == "internal_md" and r.target:
            by_path[r.target].append(r)
    for doc in docs:
        here = by_path.get(doc.source_path)
        if here:
            doc.extra.update(_measure_extra(here))


def _extract_documents(
    product: str, release: str, state: dict
) -> tuple[list[Document], dict[str, list[str]], list[str], dict | None, dict[str, Path]]:
    reg = load_registry(product, release)
    docs: list[Document] = []
    excluded: dict[str, list[str]] = {}
    warnings: list[str] = []
    crosswalk: dict | None = None
    pdf_images: dict[str, Path] = {}

    for src in reg.sources:
        src_state = state["sources"][src.id]
        clone_dir = _clone_dir(product, release, src)

        if src.type == "latex":
            latex_docs, latex_warn = load_latex_docs(
                clone_dir, src.latex_main or "", product, release, src.id
            )
            docs += latex_docs
            warnings += [f"{src.id}: {w}" for w in latex_warn]

        elif src.type == "markdown":
            rels = [i["path"] for i in src_state["inputs"]]
            md_docs, md_excl = load_markdown_docs(
                clone_dir, rels, product, release, src.id, "markdown"
            )
            docs += md_docs
            if md_excl:
                excluded[src.id] = md_excl

        elif src.type == "measures":
            refs = _index_refs(clone_dir, src_state)
            # internal measure markdown pages
            rels = [p["path"] for p in src_state["internal_pages"]]
            page_docs, page_excl = load_markdown_docs(
                clone_dir, rels, product, release, src.id, "measures"
            )
            _attach_internal_measure_identity(page_docs, refs)
            docs += page_docs
            if page_excl:
                excluded[src.id] = page_excl
            # external + local measure PDFs
            specs = _pdf_specs(product, release, clone_dir, src_state, refs)
            pdf_docs, pdf_warn, pdf_imgs = load_pdf_docs(specs, product, release, src.id)
            docs += pdf_docs
            warnings += [f"{src.id}: {w}" for w in pdf_warn]
            for rel_dir, cache_dir in pdf_imgs.items():
                # follow the .md files if their dir is remapped, so `![](x_images/...)` resolves
                pdf_images[f"{src.id}/{remap_dir(rel_dir, src.output_remap)}"] = cache_dir
            # crosswalk join (CSV + index)
            cw = src_state.get("crosswalk")
            if cw:
                crosswalk = build_crosswalk(clone_dir / cw["path"], refs, release)

    return docs, excluded, warnings, crosswalk, pdf_images


def _strip_leading_heading(title: str, body: str) -> str:
    """Remove the first line of body if it's an H1 matching the title we inject."""
    lines = body.split("\n", 1)
    if lines and lines[0].startswith("# "):
        heading_text = lines[0].lstrip("# ").strip()
        if heading_text == title:
            return lines[1].lstrip("\n") if len(lines) > 1 else ""
    return body


def _write_processed(
    product: str, release: str, docs: list[Document], remaps: dict[str, tuple[str, str]]
) -> None:
    root = processed_root(product, release)
    for doc in docs:
        out = root / output_rel(doc.source_id, doc.source_path, remaps.get(doc.source_id))
        out.parent.mkdir(parents=True, exist_ok=True)
        front = f"<!-- {doc.product} {doc.release} | {doc.source_id} | {doc.source_path} -->\n"
        body = _strip_leading_heading(doc.title, doc.body)
        out.write_text(front + f"# {doc.title}\n\n{body}", encoding="utf-8")


def _replace_dir(src_dir: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src_dir, dst)


def _copy_source_images(product: str, release: str, pdf_images: dict[str, Path]) -> int:
    """Copy image assets into processed/ so the relative refs in the .md files resolve.

    Clone-sourced images (measures media/, LaTeX figures/) are copied to the same relative
    depth as the .md files that reference them; PDF images come from the docling cache.
    """
    reg = load_registry(product, release)
    root = processed_root(product, release)
    copied = 0

    for rel_dir, cache_dir in pdf_images.items():
        dst = root / rel_dir
        _replace_dir(cache_dir, dst)
        copied += sum(1 for p in dst.rglob("*") if p.is_file())

    for src in reg.sources:
        clone_dir = _clone_dir(product, release, src)
        if src.type == "measures":
            # measures pages reference media/*.png relative to the page's directory,
            # so media follows the pages when that directory is remapped
            src_media = clone_dir / (src.internal_dir or "") / "media"
            if src_media.is_dir():
                rel_media = f"{(src.internal_dir or '').strip('/')}/media"
                dst = root / src.id / remap_dir(rel_media, src.output_remap)
                _replace_dir(src_media, dst)
                copied += sum(1 for p in dst.rglob("*") if p.is_file())
        elif src.type == "markdown":
            # site pages reach up to the repo-root asset dir (../../assets/images/...);
            # output mirrors repo-relative depth, so one copy serves every page depth.
            src_assets = clone_dir / "assets" / "images"
            if src_assets.is_dir():
                dst = root / src.id / "assets" / "images"
                _replace_dir(src_assets, dst)
                copied += sum(1 for p in dst.rglob("*") if p.is_file())
        elif src.type == "latex":
            # pandoc emits <img src="figures/..."> relative to the chapter .tex files
            latex_main = clone_dir / (src.latex_main or "")
            src_figures = latex_main.parent / "figures"
            if src_figures.is_dir():
                rel = latex_main.parent.relative_to(clone_dir).as_posix()
                dst = root / src.id / rel / "figures"
                _replace_dir(src_figures, dst)
                copied += sum(1 for p in dst.rglob("*") if p.is_file())
    return copied


def build_release(product: str, release: str) -> dict:
    state = _load_fetch_state(product, release)
    docs, excluded, warnings, crosswalk, pdf_images = _extract_documents(product, release, state)
    remaps = load_registry(product, release).output_remaps()
    _write_processed(product, release, docs, remaps)
    n_images = _copy_source_images(product, release, pdf_images)

    chunks = chunk_documents(docs)
    cf = chunks_file(product, release)
    cf.parent.mkdir(parents=True, exist_ok=True)
    with cf.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps({"id": c.id, "text": c.text, "metadata": c.metadata}) + "\n")

    if crosswalk is not None:
        (processed_root(product, release) / "crosswalk.json").write_text(
            json.dumps(crosswalk, indent=2), encoding="utf-8"
        )

    manifest = build_manifest(
        product, release, docs, crosswalk, warnings, excluded, state, len(chunks), remaps
    )

    by_type: dict[str, int] = defaultdict(int)
    for d in docs:
        by_type[d.source_type] += 1
    n_excluded = sum(len(v) for v in excluded.values())
    summary = {
        "documents": len(docs),
        "chunks": len(chunks),
        "images": n_images,
        "by_type": dict(by_type),
        "excluded_unpublished": excluded,
        "warnings": warnings,
        "crosswalk": crosswalk["counts"] if crosswalk else None,
        "chunks_file": str(cf),
        "manifest_file": str(manifest_file(product, release)),
    }
    print(f"build: {len(docs)} docs -> {len(chunks)} chunks (by type: {dict(by_type)}) -> {cf}")
    print(f"  copied {n_images} image file(s) into processed/")
    if crosswalk:
        c = crosswalk["counts"]
        print(f"  crosswalk: {c['measures']} measures, {c['covered']} covered, {c['gaps']} gaps")
    if n_excluded:
        print(f"  excluded {n_excluded} unpublished page(s): "
              + ", ".join(f"{k}={len(v)}" for k, v in excluded.items()))
    if warnings:
        print(f"  {len(warnings)} extraction warning(s); first few:")
        for w in warnings[:3]:
            print(f"    - {w}")
    print(f"  manifest -> {manifest_file(product, release)} "
          f"({len(manifest['gaps']['measures'])} measure gaps recorded)")
    return summary
