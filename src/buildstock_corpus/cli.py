"""`bsc` command-line interface.

Commands map to pipeline stages, all addressed by (product, release):

    bsc fetch     download + hash raw sources into raw/<product>/<release>/
    bsc build     extract -> normalize -> crosswalk -> chunks -> manifest
    bsc index     embed chunks into a persistent Chroma collection
    bsc query     retrieve cited passages (optionally answer via an LLM)
    bsc validate  enforce provenance invariants on the manifest

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
ReleaseOpt = Annotated[str, typer.Option(help="Dataset release tag, e.g. '2025-3'.")]
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
def fetch(product: ProductOpt = "comstock", release: ReleaseOpt = "2025-3") -> None:
    """Download and hash raw sources for a release."""
    from . import fetch as _fetch

    _fetch.fetch_release(product, release)


@app.command()
def build(
    product: ProductOpt = "comstock",
    release: ReleaseOpt = "2025-3",
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
    work_dir: WorkDirOpt = None,
) -> None:
    """Extract, normalize, and chunk raw sources into release-tagged artifacts + manifest."""
    from . import build as _build

    _workspace(work_dir)
    _build.build_release(product, release, sample=sample, overlays=overlays)


@app.command()
def index(
    product: ProductOpt = "comstock",
    release: ReleaseOpt = "2025-3",
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
    release: ReleaseOpt = "2025-3",
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
def validate(
    product: ProductOpt = "comstock",
    release: ReleaseOpt = "2025-3",
    work_dir: WorkDirOpt = None,
) -> None:
    """Check manifest provenance invariants; exit non-zero on failure."""
    from . import manifest as _manifest

    _workspace(work_dir)
    ok = _manifest.validate_release(product, release)
    raise typer.Exit(code=0 if ok else 1)


if __name__ == "__main__":
    app()
