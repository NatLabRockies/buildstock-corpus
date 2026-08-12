"""`bsc` command-line interface.

Commands map to pipeline stages, all addressed by (product, release):

    bsc fetch     download + hash raw sources into raw/<product>/<release>/
    bsc build     extract -> normalize -> crosswalk -> chunks -> manifest
    bsc index     embed chunks into a persistent Chroma collection
    bsc query     retrieve cited passages (optionally answer via an LLM)
    bsc validate  enforce provenance invariants on the manifest
    bsc eval      score the index against a gold set, vs. bare Claude as the baseline

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


@app.command()
def fetch(product: ProductOpt = "comstock", release: ReleaseOpt = "2025-3") -> None:
    """Download and hash raw sources for a release."""
    from . import fetch as _fetch

    _fetch.fetch_release(product, release)


@app.command()
def build(product: ProductOpt = "comstock", release: ReleaseOpt = "2025-3") -> None:
    """Extract, normalize, and chunk raw sources into release-tagged artifacts + manifest."""
    from . import build as _build

    _build.build_release(product, release)


@app.command()
def index(product: ProductOpt = "comstock", release: ReleaseOpt = "2025-3") -> None:
    """Embed chunks into a persistent Chroma collection for this release."""
    from . import index as _index

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
) -> None:
    """Retrieve top-k cited passages for a question, scoped to a release."""
    from . import query as _query

    _query.query_corpus(text, product=product, release=release, k=k, answer=answer)


@app.command()
def validate(product: ProductOpt = "comstock", release: ReleaseOpt = "2025-3") -> None:
    """Check manifest provenance invariants; exit non-zero on failure."""
    from . import manifest as _manifest

    ok = _manifest.validate_release(product, release)
    raise typer.Exit(code=0 if ok else 1)


@app.command()
def eval(
    gold: Annotated[
        Path | None, typer.Option(help="Gold question set (default: eval/gold_set.yaml).")
    ] = None,
    product: Annotated[str | None, typer.Option(help="Override the gold set's product.")] = None,
    release: Annotated[str | None, typer.Option(help="Override the gold set's release.")] = None,
    k: Annotated[int, typer.Option(help="Passages retrieved per question.")] = 5,
    answer: Annotated[
        bool,
        typer.Option(help="Also generate index-backed and bare-Claude answers (needs an API key)."),
    ] = False,
    judge: Annotated[
        bool, typer.Option(help="Grade both answers with an LLM judge; implies --answer.")
    ] = False,
    out: Annotated[Path | None, typer.Option(help="Results JSON (default: eval/results.json).")] = None,
) -> None:
    """Score retrieval against a gold set, with bare Claude as the baseline."""
    from . import evaluate as _evaluate

    _evaluate.evaluate_release(
        product=product,
        release=release,
        gold_path=gold or _evaluate.DEFAULT_GOLD,
        k=k,
        answer=answer,
        judge=judge,
        out_path=out or _evaluate.DEFAULT_RESULTS,
    )


if __name__ == "__main__":
    app()
