"""Nothing in the tooling assumes ComStock once a second product exists (R1.4 of
PLAN-resstock.md): the CLI resolves its target from the registries in sources/ instead of
defaulting to ComStock, prose that names a product takes the name from the registry, and
the decorative-image rule is keyed per product, hiding nothing for a product without one.
"""

from __future__ import annotations

import textwrap

import pytest
import typer

import buildstock_corpus.cli as C
import buildstock_corpus.paths as P
from buildstock_corpus.decorative import decorative_label, surviving_decorative_refs
from buildstock_corpus.registry import product_name


def _sources(tmp_path, monkeypatch, *pairs):
    d = tmp_path / "sources"
    d.mkdir()
    for product, release in pairs:
        (d / f"{product}_{release}.yaml").write_text(
            textwrap.dedent(f"product: {product}\nrelease: \"{release}\"\nsources: []\n"),
            encoding="utf-8",
        )
    monkeypatch.setattr(P, "SOURCES_DIR", d)


COM = ("comstock", "comstock_amy2018_2025_release_3")
RES = ("resstock", "resstock_amy2018_2025_release_1")


def test_one_registry_needs_no_flags(tmp_path, monkeypatch):
    _sources(tmp_path, monkeypatch, COM)
    assert C._target(None, None) == COM
    assert C._target("comstock", None) == COM
    assert C._target(None, COM[1]) == COM


def test_two_registries_resolve_by_product_or_release(tmp_path, monkeypatch):
    _sources(tmp_path, monkeypatch, COM, RES)
    assert C._target("resstock", None) == RES
    assert C._target(None, COM[1]) == COM
    assert C._target(*RES) == RES


def test_ambiguous_or_unknown_targets_exit_2_naming_the_registries(tmp_path, monkeypatch, capsys):
    _sources(tmp_path, monkeypatch, COM, RES)
    with pytest.raises(typer.Exit) as exc:
        C._target(None, None)
    assert exc.value.exit_code == 2
    err = capsys.readouterr().err
    assert "several registries match" in err and COM[1] in err and RES[1] in err

    with pytest.raises(typer.Exit) as exc:
        C._target("comstock", RES[1])  # a product/release pair that is not a registry
    assert exc.value.exit_code == 2
    assert "no registry in sources/ matches" in capsys.readouterr().err


def test_the_checked_in_registry_set_resolves_as_expected():
    """Today sources/ holds ComStock alone, so a bare `bsc validate` still means ComStock.
    When the ResStock registry lands (R2.1) this test changes to the two-registry case."""
    assert C._target(None, None) == COM


def test_product_names_are_spelled_as_the_products_spell_them():
    assert product_name("comstock") == "ComStock"
    assert product_name("resstock") == "ResStock"
    assert product_name("otherstock") == "Otherstock"


def test_decorative_rule_is_per_product_and_hides_nothing_without_one():
    assert decorative_label("comstock", "measure_pdfs/89040.pdf", "000000", "abc") == "cover art"
    assert decorative_label("comstock", "measure_pdfs/89040.pdf", "000001", "abc") == "wordmark"
    # ResStock's reports come from the same template, but until R3.2 has looked at one the
    # rule is "leave every image visible"
    assert decorative_label("resstock", "measure_pdfs/96634.pdf", "000000", "abc") is None
    text = "![Image](96634_images/image_000000_abc.png)\n![Image](96634_images/image_000001_def.png)\n"
    assert len(surviving_decorative_refs("comstock", "measure_pdfs/96634.pdf", text)) == 2
    assert surviving_decorative_refs("resstock", "measure_pdfs/96634.pdf", text) == []
