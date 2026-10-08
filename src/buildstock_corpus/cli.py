"""`bsc` command-line interface.

Commands map to pipeline stages, all addressed by (product, release):

    bsc fetch     download + hash raw sources into raw/<product>/<release>/
    bsc build     extract -> normalize -> crosswalk -> chunks -> manifest
    bsc index     embed chunks into a persistent Chroma collection
    bsc query     retrieve cited passages (optionally answer via an LLM)
    bsc validate  enforce provenance invariants on the manifest
    bsc changelog release notes: diff this build's manifest against a tagged one

Heavy dependencies (docling, fastembed, ...) are imported lazily inside each
command so `bsc --help` and unrelated commands stay fast.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Annotated

import typer

# Domain content is full of en-dashes, curly quotes, and § — force UTF-8 stdout so it
# doesn't mojibake under Windows' default cp1252 console encoding.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    help="BuildStock Level 1 AI-ready content pipeline (release-tagged, provenance-tracked).",
)

ProductOpt = Annotated[str, typer.Option(help="Dataset product, e.g. 'comstock'.")]
ReleaseOpt = Annotated[
    str,
    typer.Option(
        help="Dataset release id, following the OEDI data lake convention "
        "<dataset type>_<weather data>_<year of publication>_release_<release number>, "
        "e.g. 'comstock_amy2018_2025_release_3'.",
    ),
]
WorkDirOpt = Annotated[
    Path | None,
    typer.Option(
        help="Write derived outputs (processed/, index/) under this root instead of the "
        "project defaults, leaving the release artifacts untouched. raw/ and the "
        "conversion caches are still shared.",
    ),
]


def _workspace(work_dir: Path | None) -> None:
    """Point the derived-output paths at a sandbox root for this invocation."""
    from . import paths

    if work_dir is not None:
        work_dir.mkdir(parents=True, exist_ok=True)
    paths.use_workspace(work_dir)


@app.command()
def fetch(
    product: ProductOpt = "comstock",
    release: ReleaseOpt = "comstock_amy2018_2025_release_3",
) -> None:
    """Download and hash raw sources for a release."""
    from . import fetch as _fetch

    _fetch.fetch_release(product, release)


@app.command()
def build(
    product: ProductOpt = "comstock",
    release: ReleaseOpt = "comstock_amy2018_2025_release_3",
    sample: Annotated[
        int | None,
        typer.Option(
            help="Smoke test: build at most N documents per category (latex, markdown, "
            "measures, pdf). The manifest is stamped partial. Pair with --work-dir so the "
            "release artifacts are not overwritten.",
        ),
    ] = None,
    overlays: Annotated[
        bool,
        typer.Option(
            help="Inject the hand-authored sidecar overlays (tables the source embeds only "
            "as bitmaps). Use --no-overlays to reproduce the pre-overlay output for a "
            "before/after comparison; a release build wants them on.",
        ),
    ] = True,
    corpus_version: Annotated[
        str | None,
        typer.Option(
            help="Name for this build, written into every file header, the manifest and "
            "the map. A release build passes the tag it will be published under, e.g. "
            "'comstock_amy2018_2025_release_3-v1'. Defaults to the current commit's short "
            "hash ('-dirty' if the tree has local changes).",
        ),
    ] = None,
    work_dir: WorkDirOpt = None,
) -> None:
    """Extract, normalize, and chunk raw sources into release-tagged artifacts + manifest."""
    from . import build as _build

    _workspace(work_dir)
    _build.build_release(
        product, release, sample=sample, overlays=overlays, corpus_version=corpus_version
    )


# Named explicitly so the function does not shadow the `map` builtin at module scope.
@app.command("map")
def corpus_map(
    product: ProductOpt = "comstock",
    release: ReleaseOpt = "comstock_amy2018_2025_release_3",
    work_dir: WorkDirOpt = None,
) -> None:
    """Regenerate CORPUS_MAP.md, index.json, sections.json and sections/ for this release.

    The map is the entry point for a reader; index.json and sections.json are the entry
    point for a program fetching the corpus over HTTPS; sections/ holds every H2 as its
    own file. All are derived from the built artifacts (manifest, chunks, crosswalk, the
    processed files), so this needs no raw/ and runs in seconds -- including in a fresh
    clone.
    """
    import json

    from . import corpus_index as _corpus_index
    from . import corpus_map as _corpus_map
    from .chunk_files import write_chunk_files
    from .paths import chunks_file, manifest_file, processed_root
    from .sections import write_all_sections

    _workspace(work_dir)
    _corpus_map.build_map(product, release)
    proot = processed_root(product, release)
    manifest = json.loads(manifest_file(product, release).read_text(encoding="utf-8"))
    n = write_all_sections(
        proot, [a["output_path"] for s in manifest.get("sources", []) for a in s.get("artifacts", [])]
    )
    print(f"sections: {n} section file(s) regenerated under processed/.../sections/")
    cf = chunks_file(product, release)
    if cf.is_file():
        n = write_chunk_files(proot, manifest, cf.read_text(encoding="utf-8"))
        print(f"chunks: {n} per-document chunk file(s) regenerated under processed/.../chunks/")
    _corpus_index.build_index(product, release)


@app.command()
def index(
    product: ProductOpt = "comstock",
    release: ReleaseOpt = "comstock_amy2018_2025_release_3",
    work_dir: WorkDirOpt = None,
) -> None:
    """Embed chunks into a persistent Chroma collection for this release."""
    from . import index as _index

    _workspace(work_dir)
    _index.build_index(product, release)


@app.command()
def query(
    text: Annotated[str, typer.Argument(help="Natural-language question.")],
    product: ProductOpt = "comstock",
    release: ReleaseOpt = "comstock_amy2018_2025_release_3",
    k: Annotated[int, typer.Option(help="Number of passages to retrieve.")] = 5,
    answer: Annotated[
        bool, typer.Option(help="Also synthesize an answer via an LLM (requires an API key).")
    ] = False,
    work_dir: WorkDirOpt = None,
) -> None:
    """Retrieve top-k cited passages for a question, scoped to a release."""
    from . import query as _query

    _workspace(work_dir)
    _query.query_corpus(text, product=product, release=release, k=k, answer=answer)


@app.command()
def changelog(
    from_ref: Annotated[
        str | None,
        typer.Option(
            "--from",
            help="Git ref of the previous build to diff against, normally its release tag "
            "(e.g. 'comstock_amy2018_2025_release_3-v1').",
        ),
    ] = None,
    show: Annotated[
        str | None,
        typer.Option(
            "--show",
            help="Instead of diffing, print the body of CHANGELOG.md's entry for this version "
            "(what the release workflow publishes as the GitHub Release notes).",
        ),
    ] = None,
    to_ref: Annotated[
        str | None,
        typer.Option(
            "--to",
            help="Git ref of the new build. Default: the manifest in the working tree, i.e. "
            "the build you just ran.",
        ),
    ] = None,
    append: Annotated[
        bool,
        typer.Option(help="Also insert the entry at the top of CHANGELOG.md (refuses a duplicate heading)."),
    ] = False,
    product: ProductOpt = "comstock",
    release: ReleaseOpt = "comstock_amy2018_2025_release_3",
    work_dir: WorkDirOpt = None,
) -> None:
    """Print release notes computed from two builds' manifests.

    Lists documents added, removed, revised upstream (input hash moved), with a changed
    overlay, or re-rendered from an unchanged source (body hash moved), plus measure gaps
    opened or closed, registry exclusions and tooling versions. Paste the output into the
    GitHub Release; `--append` adds it to CHANGELOG.md. The reasons behind re-rendered
    documents are not in any manifest: add those bullets by hand.
    """
    from . import changelog as _changelog
    from .paths import PROJECT_ROOT

    _workspace(work_dir)
    changelog_md = PROJECT_ROOT / _changelog.CHANGELOG_FILENAME
    if (from_ref is None) == (show is None):
        print("changelog: pass exactly one of --from <ref> or --show <version>", file=sys.stderr)
        raise typer.Exit(code=2)
    try:
        if show is not None:
            print(_changelog.entry_for(show, changelog_md), end="")
            return
        _log, entry = _changelog.changelog(product, release, from_ref, to_ref)
        if append:
            _changelog.append_entry(entry, changelog_md)
    except _changelog.ChangelogError as exc:
        print(f"changelog: {exc}", file=sys.stderr)
        raise typer.Exit(code=1)
    print(entry, end="")
    if append:
        print(f"changelog: entry added to {_changelog.CHANGELOG_FILENAME}", file=sys.stderr)


@app.command()
def validate(
    product: ProductOpt = "comstock",
    release: ReleaseOpt = "comstock_amy2018_2025_release_3",
    work_dir: WorkDirOpt = None,
) -> None:
    """Check manifest provenance invariants; exit non-zero on failure."""
    from . import manifest as _manifest

    _workspace(work_dir)
    ok = _manifest.validate_release(product, release)
    raise typer.Exit(code=0 if ok else 1)


if __name__ == "__main__":
    app()
