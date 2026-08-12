"""Fetch raw sources for a release into raw/<product>/<release>/ and record provenance.

Repos are cloned shallow + sparse (deduped by repo+ref), the exact commit SHA is
recorded, and every raw input file is sha256-hashed. External upgrade-measure PDFs are
downloaded; unreachable ones are recorded as gaps rather than aborting the run. The
resulting fetch_state.json is the provenance input to the build/manifest stage.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

import httpx

from .extract.measures_index import local_pdf_paths, parse_index
from .paths import raw_root
from .registry import Registry, Source, load_registry

PDF_URL_RE = re.compile(r"https?://[^\s)\"'<>]+?\.pdf", re.IGNORECASE)


def fetch_release(product: str, release: str) -> Path:
    reg = load_registry(product, release)
    root = raw_root(product, release)
    repos_dir = root / "repos"
    repos_dir.mkdir(parents=True, exist_ok=True)

    # 1. Clone each unique (repo, ref) once, unioning sparse paths.
    clones = _plan_clones(reg)
    for c in clones.values():
        _ensure_clone(c, repos_dir)
        print(f"  {c.name}: {c.sha[:10]} ({c.repo} @ {c.git_ref})")

    # 2. Per-source: hash inputs; for measures, download external PDFs.
    state: dict = {
        "product": product,
        "release": release,
        "clones": [c.as_state() for c in clones.values()],
        "sources": {},
    }
    for src in reg.sources:
        clone = clones[(src.repo, src.git_ref)]
        clone_dir = repos_dir / clone.name
        if src.type == "measures":
            state["sources"][src.id] = _fetch_measures(src, clone, clone_dir, root)
        else:
            state["sources"][src.id] = _fetch_docs(src, clone, clone_dir)

    state_path = root / "fetch_state.json"
    state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
    print(f"fetch complete -> {state_path}")
    return state_path


# --- clone planning / execution -------------------------------------------------


@dataclass
class Clone:
    repo: str
    git_ref: str
    sparse: list[str]
    name: str
    sha: str = ""

    def as_state(self) -> dict:
        return {
            "repo": self.repo,
            "git_ref": self.git_ref,
            "sha": self.sha,
            "dest": f"repos/{self.name}",
            "sparse": sorted(self.sparse),
        }


def _clone_name(repo: str, git_ref: str) -> str:
    stem = repo.rstrip("/").rsplit("/", 1)[-1]
    if stem.endswith(".git"):
        stem = stem[:-4]
    return f"{stem}@{git_ref}"


def _plan_clones(reg: Registry) -> dict[tuple[str, str], Clone]:
    clones: dict[tuple[str, str], Clone] = {}
    for src in reg.sources:
        key = (src.repo, src.git_ref)
        if key not in clones:
            clones[key] = Clone(
                repo=src.repo,
                git_ref=src.git_ref,
                sparse=list(src.sparse),
                name=_clone_name(src.repo, src.git_ref),
            )
        else:
            for p in src.sparse:
                if p not in clones[key].sparse:
                    clones[key].sparse.append(p)
    return clones


def _git(dest: Path, *args: str) -> str:
    out = subprocess.run(
        ["git", "-C", str(dest), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return out.stdout.strip()


def _ensure_clone(clone: Clone, repos_dir: Path) -> None:
    dest = repos_dir / clone.name
    if (dest / ".git").exists():
        if clone.sparse:
            _git(dest, "sparse-checkout", "set", *clone.sparse)
        clone.sha = _git(dest, "rev-parse", "HEAD")
        return

    # Shallow, blobless, sparse clone pinned to the ref (tag or branch).
    subprocess.run(
        [
            "git", "clone", "--no-checkout", "--depth", "1",
            "--branch", clone.git_ref, "--filter=blob:none",
            clone.repo, str(dest),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    if clone.sparse:
        _git(dest, "sparse-checkout", "init", "--cone")
        _git(dest, "sparse-checkout", "set", *clone.sparse)
    _git(dest, "checkout")
    clone.sha = _git(dest, "rev-parse", "HEAD")


# --- hashing / per-source fetch --------------------------------------------------


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def _matches_exclude(rel: str, exclude_globs: list[str]) -> bool:
    return any(Path(rel).match(pat) for pat in exclude_globs)


def _fetch_docs(src: Source, clone: Clone, clone_dir: Path) -> dict:
    """Hash every file matching the source's doc_glob (respecting exclude_globs)."""
    inputs = []
    for path in sorted(clone_dir.glob(src.doc_glob or "**/*")):
        if not path.is_file():
            continue
        rel = path.relative_to(clone_dir).as_posix()
        if _matches_exclude(rel, src.exclude_globs):
            continue
        inputs.append({"path": rel, "sha256": _sha256_file(path)})
    print(f"  {src.id}: {len(inputs)} files")
    return {"type": src.type, "clone": clone.name, "inputs": inputs}


def _fetch_measures(src: Source, clone: Clone, clone_dir: Path, root: Path) -> dict:
    """Collect internal measure pages + crosswalk, and download external measure PDFs."""
    result: dict = {"type": src.type, "clone": clone.name}

    # Internal measure markdown pages (source of the on-site HTML measure docs).
    internal_dir = clone_dir / (src.internal_dir or "")
    internal_pages = []
    index_name = Path(src.index_page).name if src.index_page else None
    for path in sorted(internal_dir.glob("*.md")):
        if path.name == index_name:
            continue  # the index page itself is not a measure doc
        internal_pages.append(
            {"path": path.relative_to(clone_dir).as_posix(), "sha256": _sha256_file(path)}
        )
    result["internal_pages"] = internal_pages

    # Crosswalk CSV (the per-measure versioning anchor).
    crosswalk_path = clone_dir / (src.crosswalk_csv or "")
    if crosswalk_path.is_file():
        result["crosswalk"] = {
            "path": crosswalk_path.relative_to(clone_dir).as_posix(),
            "sha256": _sha256_file(crosswalk_path),
        }
    else:
        result["crosswalk"] = None

    # Index page: the authoritative measure -> doc map. Hash it (it drives the build),
    # then use it to find external URLs to download and local PDFs to hash in place.
    index_path = clone_dir / (src.index_page or "")
    urls: list[str] = []
    local_pdfs: list[dict] = []
    if index_path.is_file():
        result["index_page"] = {
            "path": index_path.relative_to(clone_dir).as_posix(),
            "sha256": _sha256_file(index_path),
        }
        text = index_path.read_text(encoding="utf-8", errors="replace")
        urls = sorted(set(PDF_URL_RE.findall(text)))
        refs = parse_index(text, result["index_page"]["path"])
        for rel in local_pdf_paths(refs):
            fp = clone_dir / rel
            if fp.is_file():
                local_pdfs.append({"path": rel, "sha256": _sha256_file(fp)})
    else:
        result["index_page"] = None
    result["external_pdf_urls_found"] = len(urls)

    pdf_dir = root / "measure_pdfs"
    downloaded, gaps = _download_pdfs(urls, pdf_dir, root)
    result["external_pdfs"] = downloaded
    result["local_pdfs"] = local_pdfs
    result["missing"] = gaps
    print(
        f"  {src.id}: {len(internal_pages)} internal pages, "
        f"{len(downloaded)} PDFs downloaded, {len(local_pdfs)} local PDFs, "
        f"{len(gaps)} unreachable"
    )
    return result


def _download_pdfs(urls: list[str], pdf_dir: Path, root: Path) -> tuple[list[dict], list[dict]]:
    if not urls:
        return [], []
    pdf_dir.mkdir(parents=True, exist_ok=True)
    downloaded, gaps = [], []
    by_sha: dict[str, str] = {}  # content sha256 -> rel path (mirror dedupe)
    used_names: set[str] = set()
    with httpx.Client(follow_redirects=True, timeout=60.0) as client:
        for url in urls:
            try:
                resp = client.get(url)
                resp.raise_for_status()
                data = resp.content
            except Exception as exc:  # network/HTTP failures are gaps, not fatal
                gaps.append({"url": url, "status": "error", "note": str(exc)[:200]})
                continue
            sha = hashlib.sha256(data).hexdigest()
            if sha in by_sha:
                # A different URL already served byte-identical content (host mirror):
                # record this URL against the same file rather than a second copy.
                downloaded.append(
                    {"url": url, "path": by_sha[sha], "sha256": sha,
                     "status": "ok", "note": "duplicate content"}
                )
                continue
            name = _unique_name(_pdf_filename(url), sha, used_names)
            used_names.add(name)
            dest = pdf_dir / name
            dest.write_bytes(data)
            rel = dest.relative_to(root).as_posix()
            by_sha[sha] = rel
            downloaded.append({"url": url, "path": rel, "sha256": sha, "status": "ok"})
    return downloaded, gaps


def _pdf_filename(url: str) -> str:
    stem = url.rsplit("/", 1)[-1].split("?", 1)[0]
    return stem if stem.lower().endswith(".pdf") else stem + ".pdf"


def _unique_name(base: str, sha: str, used: set[str]) -> str:
    """Keep the natural basename unless it's taken by different content, then salt it."""
    if base not in used:
        return base
    stem = base[:-4] if base.lower().endswith(".pdf") else base
    return f"{stem}.{sha[:8]}.pdf"
