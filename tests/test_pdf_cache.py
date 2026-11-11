"""The docling conversion cache keys on PDF bytes *and* conversion options.

Content-addressing alone was a provenance trap: the key was the PDF's sha256, so editing
_pipeline_options() (say FAST -> ACCURATE table structure) would have been a silent no-op on
every already-cached PDF, and the manifest would have recorded options the markdown was never
produced with. pipeline.json next to each cached document is what closes that gap.

docling is never imported here: _fingerprint is memoized on the module, so these set it
directly and stub _convert_into to record that a re-conversion was attempted.
"""

from __future__ import annotations

import json

import pytest

import buildstock_corpus.extract.pdf as PDF

FINGERPRINT = {
    "do_ocr": False,
    "do_table_structure": True,
    "table_mode": "fast",
    "do_cell_matching": True,
    "generate_picture_images": True,
    "table_footnotes": "in_body",
}
SHA = "f" * 64


@pytest.fixture
def cache(tmp_path, monkeypatch):
    """A redirected cache root, a pinned fingerprint, and a conversion that only records."""
    root = tmp_path / "pdf_md"
    monkeypatch.setattr(PDF, "PDF_CACHE", root)
    monkeypatch.setattr(PDF, "_fingerprint", dict(FINGERPRINT))

    converted: list[str] = []

    def fake_convert(abs_path, dest):
        converted.append(str(abs_path))
        dest.mkdir(parents=True, exist_ok=True)
        (dest / PDF.CACHE_MD_NAME).write_text("# reconverted\n", encoding="utf-8")
        PDF._write_fingerprint(dest)

    monkeypatch.setattr(PDF, "_convert_into", fake_convert)

    class Cache:
        def __init__(self):
            self.converted = converted
            self.root = root
            self.spec = PDF.PdfSpec(
                source_path="measure_pdfs/89040.pdf",
                abs_path=tmp_path / "89040.pdf",
                sha256=SHA,
            )
            self.spec.abs_path.write_bytes(b"%PDF-1.7 pretend")

        def seed(self, *, opts: object = ..., body: str = "# cached\n"):
            """A populated cache dir. `opts` omitted = no pipeline.json (a pre-fingerprint dir)."""
            d = root / SHA
            d.mkdir(parents=True)
            (d / PDF.CACHE_MD_NAME).write_text(body, encoding="utf-8")
            if opts is not ...:
                (d / PDF.CACHE_OPTS_NAME).write_text(
                    opts if isinstance(opts, str) else json.dumps(opts), encoding="utf-8"
                )
            return d

    return Cache()


def test_conversion_records_the_options_it_used(cache):
    d = PDF._cache_dir_for(cache.spec)

    assert cache.converted == [str(cache.spec.abs_path)]
    assert json.loads((d / PDF.CACHE_OPTS_NAME).read_text(encoding="utf-8")) == FINGERPRINT


def test_matching_fingerprint_is_a_cache_hit(cache):
    cache.seed(opts=FINGERPRINT)

    d = PDF._cache_dir_for(cache.spec)

    assert cache.converted == []
    assert (d / PDF.CACHE_MD_NAME).read_text(encoding="utf-8") == "# cached\n"


def test_changed_options_force_a_reconvert(cache):
    """The point of the whole file: an options edit must actually take effect."""
    cache.seed(opts={**FINGERPRINT, "table_mode": "accurate"})

    d = PDF._cache_dir_for(cache.spec)

    assert cache.converted == [str(cache.spec.abs_path)]
    assert (d / PDF.CACHE_MD_NAME).read_text(encoding="utf-8") == "# reconverted\n"


def test_pre_fingerprint_cache_adopts_the_current_options(cache):
    """The 53 dirs converted before pipeline.json existed were made with today's options.

    They predate the file, not the settings — _pipeline_options() has one commit in its
    history — so recording the fingerprint is the honest answer. Re-converting instead would
    cost hours of GPU time to reproduce byte-identical markdown.
    """
    cache.seed()  # no pipeline.json

    d = PDF._cache_dir_for(cache.spec)

    assert cache.converted == []
    assert (d / PDF.CACHE_MD_NAME).read_text(encoding="utf-8") == "# cached\n"
    assert json.loads((d / PDF.CACHE_OPTS_NAME).read_text(encoding="utf-8")) == FINGERPRINT


def test_unreadable_fingerprint_is_not_treated_as_agreement(cache):
    """A corrupt record proves nothing about how the markdown beside it was produced.

    Distinct from *absent*: absence has a documented explanation, garbage does not, so the
    only safe reading is that the options may have differed.
    """
    cache.seed(opts="{not json")

    d = PDF._cache_dir_for(cache.spec)

    assert cache.converted == [str(cache.spec.abs_path)]
    assert (d / PDF.CACHE_MD_NAME).read_text(encoding="utf-8") == "# reconverted\n"


def test_fingerprint_omits_settings_that_cannot_change_the_output(cache):
    """Thread count and docling's version are deliberately not in the key.

    num_threads only changes how fast the conversion runs, and folding the library version in
    would invalidate all 53 cached PDFs on every routine dependency bump — a re-convert that
    reproduces the same markdown is cost without evidence.
    """
    fp = PDF._pipeline_fingerprint()

    assert "num_threads" not in fp and "docling" not in fp
    assert set(fp) == set(FINGERPRINT)


def test_legacy_single_file_cache_is_replaced(cache):
    """The original layout was one <sha256>.md with no images and no options record."""
    cache.root.mkdir(parents=True)
    legacy = cache.root / f"{SHA}.md"
    legacy.write_text("# old layout\n", encoding="utf-8")

    d = PDF._cache_dir_for(cache.spec)

    assert not legacy.exists()
    assert cache.converted == [str(cache.spec.abs_path)]
    assert (d / PDF.CACHE_OPTS_NAME).is_file()


def test_table_mode_switch_drops_the_converter_and_fingerprint(monkeypatch):
    """A source asking for ACCURATE must not reuse the converter or fingerprint built for
    FAST: the fingerprint is what makes a cache dir converted under the other mode a miss."""
    monkeypatch.setattr(PDF, "_table_mode", "fast")
    monkeypatch.setattr(PDF, "_converter", object())
    monkeypatch.setattr(PDF, "_fingerprint", dict(FINGERPRINT))
    PDF._set_table_mode("fast")  # unchanged: nothing is rebuilt
    assert PDF._converter is not None and PDF._fingerprint == FINGERPRINT
    PDF._set_table_mode("accurate")
    assert (PDF._table_mode, PDF._converter, PDF._fingerprint) == ("accurate", None, None)
    with pytest.raises(ValueError, match="pdf table mode"):
        PDF._set_table_mode("thorough")


# --- footnotes docling attaches to a table or figure (R4.2a) ----------------------------------


class _Item:
    def __init__(self, footnotes):
        self.footnotes = footnotes


class _Doc:
    def __init__(self, tables, pictures):
        self.tables, self.pictures = tables, pictures


def test_footnotes_attached_to_a_table_or_figure_are_released():
    """The markdown export writes neither a table's footnotes nor, because the table owns
    them, the same items in the body. Clearing the reference is what gets them exported."""
    doc = _Doc([_Item(["#/texts/6", "#/texts/7"]), _Item([])], [_Item(["#/texts/9"])])

    assert PDF._detach_footnotes(doc) == 3
    assert all(not item.footnotes for item in [*doc.tables, *doc.pictures])
    assert PDF._detach_footnotes(doc) == 0  # nothing left to release


def test_a_cache_built_before_footnotes_were_released_is_reconverted(cache):
    """The footnote step changes the markdown, so it is part of the fingerprint: a cache dir
    recorded without it is a miss, not a hit that silently keeps the dropped footnotes."""
    old = {k: v for k, v in FINGERPRINT.items() if k != "table_footnotes"}
    cache.seed(opts=old)

    PDF._cache_dir_for(cache.spec)

    assert cache.converted == [str(cache.spec.abs_path)]
