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
from .extract.doc_dates import (
    DocDate,
    _is_shallow,
    git_doc_date,
    latex_doc_date,
    resolve_doc_dates,
)
from .extract.latex import load_latex_docs
from .extract.markdown import load_markdown_docs
from .extract.measures_index import MeasureRef, parse_index
from .extract.pdf import PdfSpec, load_pdf_docs
from .manifest import build_manifest, input_hashes
from .normalize import Document
from .overlay import apply_overlays
from .paths import (
    chunks_file,
    long_path,
    manifest_file,
    output_rel,
    processed_root,
    raw_root,
    remap_dir,
)
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


def _measure_extra(refs: list[MeasureRef], dates: dict[str, DocDate] | None = None) -> dict:
    """Fold one-or-more measure identities (shared docs) into chunk-metadata scalars."""
    if not refs:
        return {}
    dedupe = dict.fromkeys  # preserve order, drop dups
    extra = {
        "measure_id": ",".join(r.measure_id for r in refs),
        "measure_name": "; ".join(dedupe(r.name for r in refs)),
        "measure_initial_release": ",".join(dedupe(r.initial_release for r in refs)),
    }
    # Every ref here documents the same physical file, so they share one date. Omit the keys
    # when there is no date rather than writing None: chunk_document already drops None, and
    # Chroma metadata cannot hold it. (crosswalk.json keeps the keys always-present instead,
    # so a consumer never has to probe — that asymmetry is intentional.)
    d = dates.get(refs[0].target) if (dates and refs[0].target) else None
    if d:
        extra["date_last_updated"] = d.date
        extra["date_last_updated_source"] = d.source
    return extra


def _date_docs(docs: list[Document], clone_dir: Path, src_id: str, dater) -> list[str]:
    """Stamp date_last_updated/_source into each doc's extra via `dater(clone_dir, rel)`.

    Used for the non-measure sources (latex, github_site markdown), whose docs are dated by
    their place in the repo rather than by a crosswalk target. On a shallow clone git dating
    collapses every file onto the tip commit, so we refuse to date and warn once rather than
    emit a fake uniform date. Undated docs simply keep no date keys (chunk_document drops the
    absent keys) — the same omission the measure path uses. Returns any warnings to fold in.
    """
    if _is_shallow(clone_dir):
        return [f"{src_id}: shallow clone; docs left undated - run `bsc fetch` to restore history"]
    for doc in docs:
        d = dater(clone_dir, doc.source_path)
        if d:
            doc.extra["date_last_updated"] = d.date
            doc.extra["date_last_updated_source"] = d.source
    return []


def _pdf_specs(
    product: str,
    release: str,
    clone_dir: Path,
    src_state: dict,
    refs: list[MeasureRef],
    dates: dict[str, DocDate] | None = None,
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
                extra=_measure_extra(here, dates),
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
                extra=_measure_extra(here, dates),
            )
        )
    return specs


def _cap(items: list, sample: int | None) -> list:
    """First `sample` items (all of them when sample is None) — the per-category cap.

    Sampling is always a deterministic prefix of the existing registry/fetch-state order,
    never random, so a smoke test is reproducible and its manifest is comparable run to run.
    """
    return items if sample is None else items[:sample]


def _attach_internal_measure_identity(
    docs: list[Document], refs: list[MeasureRef], dates: dict[str, DocDate] | None = None
) -> None:
    """Tag internal measure pages with their measure id (index internal_md target = path)."""
    by_path: dict[str, list[MeasureRef]] = defaultdict(list)
    for r in refs:
        if r.kind == "internal_md" and r.target:
            by_path[r.target].append(r)
    for doc in docs:
        here = by_path.get(doc.source_path)
        if here:
            doc.extra.update(_measure_extra(here, dates))


def _extract_documents(
    product: str, release: str, state: dict, sample: int | None = None
) -> tuple[
    list[Document],
    dict[str, list[str]],
    list[str],
    dict | None,
    dict[str, Path],
    dict[tuple[str, str], Path],
]:
    """Extract every fetched source into Documents.

    `sample` caps the documents kept per category (latex / markdown / measures / pdf) for
    smoke tests. Where the cap can be pushed down into an extractor cheaply it is — latex
    stops after N pandoc runs, PDFs after N conversions — but markdown extracts fully and
    caps the resulting docs, because `published: false` pages are filtered during
    extraction and the first N input paths could all be unpublished.

    Returns the two image maps separately because they answer different questions:
    `pdf_images` says where a PDF's bitmaps are copied *to* under processed/, while
    `image_dirs` says where any document's bitmaps can be read *from* right now, which is
    what overlay.apply_overlays needs to hash one it has pinned.
    """
    reg = load_registry(product, release)
    docs: list[Document] = []
    excluded: dict[str, list[str]] = {}
    warnings: list[str] = []
    crosswalk: dict | None = None
    pdf_images: dict[str, Path] = {}
    image_dirs: dict[tuple[str, str], Path] = {}

    for src in reg.sources:
        src_state = state["sources"][src.id]
        clone_dir = _clone_dir(product, release, src)
        first = len(docs)  # so this source's own docs can be post-processed below

        if src.type == "latex":
            latex_docs, latex_warn = load_latex_docs(
                clone_dir, src.latex_main or "", product, release, src.id, limit=sample
            )
            # Date each chapter by its \input closure, not the chapter file alone.
            warnings += _date_docs(latex_docs, clone_dir, src.id, latex_doc_date)
            docs += latex_docs
            warnings += [f"{src.id}: {w}" for w in latex_warn]

        elif src.type == "markdown":
            rels = [i["path"] for i in src_state["inputs"]]
            md_docs, md_excl = load_markdown_docs(
                clone_dir, rels, product, release, src.id, "markdown"
            )
            md_docs = _cap(md_docs, sample)
            warnings += _date_docs(md_docs, clone_dir, src.id, git_doc_date)
            docs += md_docs
            if md_excl:
                excluded[src.id] = md_excl

        elif src.type == "measures":
            refs = _index_refs(clone_dir, src_state)
            # Resolve each measure document's date once, up front: the same dict feeds both
            # the chunk metadata (via _measure_extra below) and the crosswalk, so there is one
            # resolution and no chance the two drift. (build_crosswalk keeps its keys always-
            # present; chunk metadata omits them when undated — see _measure_extra.)
            doc_dates = resolve_doc_dates(src_state, raw_root(product, release), clone_dir)
            # internal measure markdown pages
            rels = [p["path"] for p in src_state["internal_pages"]]
            page_docs, page_excl = load_markdown_docs(
                clone_dir, rels, product, release, src.id, "measures"
            )
            _attach_internal_measure_identity(page_docs, refs, doc_dates)
            docs += _cap(page_docs, sample)
            if page_excl:
                excluded[src.id] = page_excl
            # external + local measure PDFs
            specs = _cap(
                _pdf_specs(product, release, clone_dir, src_state, refs, doc_dates), sample
            )
            pdf_docs, pdf_warn, pdf_imgs = load_pdf_docs(specs, product, release, src.id)
            docs += pdf_docs
            warnings += [f"{src.id}: {w}" for w in pdf_warn]
            for source_path, (rel_dir, cache_dir) in pdf_imgs.items():
                # follow the .md files if their dir is remapped, so `![](x_images/...)` resolves
                pdf_images[f"{src.id}/{remap_dir(rel_dir, src.output_remap)}"] = cache_dir
                # a PDF's bitmaps are only in the cache until _copy_source_images runs
                image_dirs[(src.id, source_path)] = cache_dir
            # crosswalk join (CSV + index), each measure dated by its own documentation
            cw = src_state.get("crosswalk")
            if cw:
                crosswalk = build_crosswalk(clone_dir / cw["path"], refs, release, doc_dates)

        # Everything not filled in above is a clone-sourced page, whose images sit beside it
        # at the same relative depth they keep in processed/.
        for doc in docs[first:]:
            image_dirs.setdefault(
                (doc.source_id, doc.source_path), (clone_dir / doc.source_path).parent
            )

    return docs, excluded, warnings, crosswalk, pdf_images, image_dirs


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
    """Write one .md per document.

    newline="\\n" is load-bearing, not style: manifest.json records the sha256 of these
    bytes, so letting the platform pick the line ending would make the same inputs hash
    differently on Windows than on Linux and `bsc validate` would depend on who ran the
    build. See .gitattributes, which pins the checkout to match.
    """
    root = processed_root(product, release)
    for doc in docs:
        out = root / output_rel(doc.source_id, doc.source_path, remaps.get(doc.source_id))
        out.parent.mkdir(parents=True, exist_ok=True)
        front = f"<!-- {doc.product} {doc.release} | {doc.source_id} | {doc.source_path} -->\n"
        body = _strip_leading_heading(doc.title, doc.body)
        out.write_text(front + f"# {doc.title}\n\n{body}", encoding="utf-8", newline="\n")


def _replace_dir(src_dir: Path, dst: Path) -> int:
    """Replace `dst` with a copy of `src_dir`, returning the number of files copied.

    Every filesystem call goes through long_path(): a handful of docling's image filenames
    push these destinations past Windows' 260-character limit, where both the rmtree of the
    previous build's tree and the copytree of the new one fail on paths that plainly exist.
    Counting here rather than at the call sites means the count uses the same reachable
    form — a plain rglob().is_file() silently reports False for those files.
    """
    if dst.exists():
        shutil.rmtree(long_path(dst))
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(long_path(src_dir), long_path(dst))
    return sum(1 for p in Path(long_path(dst)).rglob("*") if p.is_file())


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
        copied += _replace_dir(cache_dir, dst)

    for src in reg.sources:
        clone_dir = _clone_dir(product, release, src)
        if src.type == "measures":
            # measures pages reference media/*.png relative to the page's directory,
            # so media follows the pages when that directory is remapped
            src_media = clone_dir / (src.internal_dir or "") / "media"
            if src_media.is_dir():
                rel_media = f"{(src.internal_dir or '').strip('/')}/media"
                dst = root / src.id / remap_dir(rel_media, src.output_remap)
                copied += _replace_dir(src_media, dst)
        elif src.type == "markdown":
            # site pages reach up to the repo-root asset dir (../../assets/images/...);
            # output mirrors repo-relative depth, so one copy serves every page depth.
            src_assets = clone_dir / "assets" / "images"
            if src_assets.is_dir():
                dst = root / src.id / "assets" / "images"
                copied += _replace_dir(src_assets, dst)
        elif src.type == "latex":
            # pandoc emits <img src="figures/..."> relative to the chapter .tex files
            latex_main = clone_dir / (src.latex_main or "")
            src_figures = latex_main.parent / "figures"
            if src_figures.is_dir():
                rel = latex_main.parent.relative_to(clone_dir).as_posix()
                dst = root / src.id / rel / "figures"
                copied += _replace_dir(src_figures, dst)
    return copied


def build_release(
    product: str, release: str, sample: int | None = None, overlays: bool = True
) -> dict:
    """Build processed artifacts for a release; `sample` caps documents per category.

    A sampled build is a smoke test, not a release: its manifest is stamped partial (see
    build_manifest) so it can never be read as the record for this release tag.

    `overlays=False` skips the sidecar transcriptions (see overlay.apply_overlays), which
    is how you reproduce the pre-overlay output for a before/after comparison. A release
    build should leave them on — without them the affected tables exist only as bitmaps.
    """
    state = _load_fetch_state(product, release)
    docs, excluded, warnings, crosswalk, pdf_images, image_dirs = _extract_documents(
        product, release, state, sample
    )
    reg = load_registry(product, release)

    applied: dict[str, dict] = {}
    if overlays:
        # Inject before writing, so the transcribed tables reach both the processed .md
        # files and chunks.jsonl. Image-anchored entries hash the bitmap where it lives now;
        # caption-anchored entries verify against the fetched input hashes instead.
        applied, overlay_warnings = apply_overlays(
            docs, product, release, image_dirs, input_hashes(state)
        )
        warnings += overlay_warnings

    remaps = reg.output_remaps()
    _write_processed(product, release, docs, remaps)
    n_images = _copy_source_images(product, release, pdf_images)

    chunks = chunk_documents(docs)
    cf = chunks_file(product, release)
    cf.parent.mkdir(parents=True, exist_ok=True)
    with cf.open("w", encoding="utf-8", newline="\n") as f:
        for c in chunks:
            f.write(json.dumps({"id": c.id, "text": c.text, "metadata": c.metadata}) + "\n")

    if crosswalk is not None:
        (processed_root(product, release) / "crosswalk.json").write_text(
            json.dumps(crosswalk, indent=2), encoding="utf-8", newline="\n"
        )

    manifest = build_manifest(
        product, release, docs, crosswalk, warnings, excluded, state, len(chunks), remaps,
        sample, applied,
    )

    by_type: dict[str, int] = defaultdict(int)
    for d in docs:
        by_type[d.source_type] += 1
    n_excluded = sum(len(v) for v in excluded.values())
    n_overlay_docs = sum(len(v) for v in applied.values())
    n_overlay_tables = sum(
        len(rec["tables_applied"]) for docs_ in applied.values() for rec in docs_.values()
    )
    summary = {
        "sample": sample,
        "documents": len(docs),
        "chunks": len(chunks),
        "images": n_images,
        "by_type": dict(by_type),
        "excluded_unpublished": excluded,
        "overlay_tables": n_overlay_tables,
        "warnings": warnings,
        "crosswalk": crosswalk["counts"] if crosswalk else None,
        "chunks_file": str(cf),
        "manifest_file": str(manifest_file(product, release)),
    }
    if sample is not None:
        print(f"build: SAMPLE - at most {sample} document(s) per category; partial corpus")
    print(f"build: {len(docs)} docs -> {len(chunks)} chunks (by type: {dict(by_type)}) -> {cf}")
    print(f"  copied {n_images} image file(s) into processed/")
    if not overlays:
        print("  overlays: SKIPPED (--no-overlays); bitmap-only tables stay unconverted")
    elif n_overlay_tables:
        print(f"  overlays: injected {n_overlay_tables} table(s) into {n_overlay_docs} doc(s)")
    if crosswalk:
        c = crosswalk["counts"]
        note = " (full crosswalk: measure->doc mapping, not the sampled docs)" if sample else ""
        print(
            f"  crosswalk: {c['measures']} measures, {c['covered']} covered, {c['gaps']} gaps{note}"
        )
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
