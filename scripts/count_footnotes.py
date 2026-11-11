"""Count the numbered page footnotes of each measure PDF and how many reached the markdown.

docling's layout model labels each text block; a footnote it labels `footnote` is exported,
one it labels `page_footer` is not, and nothing in the markdown says a block was left out.
This script measures the loss from the outside, without docling: it reads each PDF's text
layer for footnotes and looks each one up in the processed document.

A footnote is found by its marker: a superscript number at the left margin with the
footnote's words after it on the same line (see _markers). A footnote counts as
present when its opening words are in the markdown (whitespace and hyphens ignored).

    uv run python scripts/count_footnotes.py --product resstock --release resstock_amy2018_2025_release_1
    uv run python scripts/count_footnotes.py --product resstock --release ... --list 95036

Needs raw/ (the fetched PDFs), so it runs where `bsc fetch` has run, not in a fresh clone.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from buildstock_corpus.paths import manifest_file, processed_root  # noqa: E402

_DIGITS = "0123456789"
_LEAD = 40  # characters of a footnote's opening used to look it up in the markdown


# whitespace, hyphens and dashes (U+2010 to U+2014, U+2212, soft hyphen, U+FFFE), quotes
_IGNORED = re.compile(
    r"""[\s\-'"￾­‐-—−‘’“”]+"""
)


def _squash(s: str) -> str:
    """Lower-case with whitespace, hyphens and quotation marks removed.

    Those are the characters the converter changes without changing the words: line-wrap
    hyphens and spaces, and curly quotes that it writes as straight ones.
    """
    return _IGNORED.sub("", s).lower()


def _page_chars(tp) -> list[tuple[str, float, float, float, float, float]]:
    """(character, left, bottom, right, top, font size) for every character of a page."""
    import pypdfium2.raw as raw

    out = []
    for i in range(tp.count_chars()):
        left, bottom, right, top = tp.get_charbox(i)
        out.append((chr(raw.FPDFText_GetUnicode(tp, i)), left, bottom, right, top,
                    raw.FPDFText_GetFontSize(tp, i)))
    return out


def _markers(chars) -> list[tuple[float, int, int]]:
    """(baseline y, number, index of the first character after the number) per footnote marker.

    A footnote's number is a superscript at the left margin, followed on the same line by the
    footnote's words. The reports encode a superscript in two ways and both are accepted:
    the digits are in a smaller font than the words after them, or they are in the same
    nominal font (some reports scale their text with a matrix and report every font as size
    1) but drawn smaller and raised off the baseline. A numbered table row fails both tests
    (full-size digits on the baseline), and so does a page number (nothing follows it).

    Positions are used, not the order of the page's text: where several one-line footnotes
    follow each other the text layer runs them together as one line, so "starts a line" has
    to mean "sits at the left margin".
    """
    starts = [c[1] for k, c in enumerate(chars) if c[0].strip() and (k == 0 or chars[k - 1][0] == "\n")]
    if not starts:
        return []
    # The left margin is where most lines start; a stray label further left must not move it.
    margin = Counter(round(x) for x in starts).most_common(1)[0][0]
    out = []
    k = 0
    while k < len(chars):
        ch, left, bottom, right, top, size = chars[k]
        if ch not in _DIGITS or abs(left - margin) > 6 or (k and chars[k - 1][0] in _DIGITS):
            k += 1
            continue
        j = k
        while j < len(chars) and chars[j][0] in _DIGITS:
            j += 1
        digits = "".join(c[0] for c in chars[k:j])
        while j < len(chars) and chars[j][0] in " \t":
            j += 1
        if len(digits) <= 3 and j < len(chars) and chars[j][0].strip():
            t_left, t_bottom, _, _, t_size = chars[j][1], chars[j][2], chars[j][3], chars[j][4], chars[j][5]
            same_line = abs(bottom - t_bottom) < 8 and t_left > left
            base = _baseline(chars, j)
            smaller_font = size and t_size and size < 0.85 * t_size
            raised = (top - bottom) < 6 and bottom > base + 1.5
            if same_line and (smaller_font or raised):
                out.append((bottom, int(digits), j))
        k = max(j, k + 1)
    return out


def _baseline(chars, i: int) -> float:
    """Lowest box bottom among the next few characters without descenders: the text baseline."""
    bottoms = []
    for c in chars[i : i + 30]:
        if c[0] == "\n":
            break
        if c[0].isalnum() and c[0] not in "gjpqyQ":
            bottoms.append(c[2])
    return min(bottoms) if bottoms else chars[i][2]


def footnotes(pdf_path: Path) -> list[dict]:
    """Every numbered page footnote: {n, page (1-based), text}."""
    import pypdfium2 as pdfium

    pdf = pdfium.PdfDocument(str(pdf_path))
    found: list[dict] = []
    for pno in range(len(pdf)):
        tp = pdf[pno].get_textpage()
        chars = _page_chars(tp)
        tp.close()
        marks = _markers(chars)
        lowest: dict[int, tuple[float, int]] = {}  # a marker can also open a body line: keep the lowest
        for y, n, j in marks:
            if n not in lowest or y < lowest[n][0]:
                lowest[n] = (y, j)
        ends = sorted(j for _, _, j in marks)
        for n in sorted(lowest):
            j = lowest[n][1]
            stop = next((e for e in ends if e > j), len(chars))
            text = "".join(c[0] for c in chars[j : min(stop, j + 260)])
            text = re.sub(r"\s+", " ", text).strip()
            # the next footnote's own number trails this one's text; drop it
            text = re.sub(r"\s\d{1,3}$", "", text) if stop < len(chars) else text
            found.append({"n": n, "page": pno + 1, "text": text})
    return found


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--product", required=True)
    ap.add_argument("--release", required=True)
    ap.add_argument("--source", default="upgrade_measures")
    ap.add_argument("--list", metavar="STEM", help="print every footnote of one report, e.g. 95036")
    ap.add_argument("--json", metavar="FILE", help="also write the full result as JSON")
    args = ap.parse_args()

    manifest = json.loads(manifest_file(args.product, args.release).read_text(encoding="utf-8"))
    src = next(s for s in manifest["sources"] if s["id"] == args.source)
    proot = processed_root(args.product, args.release)
    raw_root = REPO / "raw" / args.product / args.release

    rows, total, lost_total, result = [], 0, 0, {}
    for art in sorted(src["artifacts"], key=lambda a: a["source_path"]):
        if not art["source_path"].lower().endswith(".pdf"):
            continue
        stem = Path(art["source_path"]).stem
        if args.list and stem != args.list:
            continue
        pdf = raw_root / art["source_path"]
        if not pdf.is_file():
            # a PDF committed in a source repo lives under the clone, not beside the fetched ones
            pdf = next(iter(raw_root.rglob(Path(art["source_path"]).name)), pdf)
        if not pdf.is_file():
            rows.append((stem, "-", "-", "PDF not in raw/"))
            continue
        md = _squash((proot / art["output_path"]).read_text(encoding="utf-8"))
        notes = footnotes(pdf)
        for f in notes:
            lead = _squash(f["text"])[:_LEAD]
            f["present"] = bool(lead) and lead in md
        lost = [f for f in notes if not f["present"]]
        total += len(notes)
        lost_total += len(lost)
        result[stem] = notes
        rows.append((stem, len(notes), len(lost), ", ".join(f"{f['n']} (p.{f['page']})" for f in lost[:12])
                     + (" ..." if len(lost) > 12 else "")))
        if args.list:
            for f in notes:
                print(f"  {'ok  ' if f['present'] else 'LOST'} {f['n']:>3} p.{f['page']:<3} {f['text'][:110]}")

    print(f"{'report':<10} {'footnotes':>9} {'lost':>5}  lost footnotes (number, PDF page)")
    for stem, n, lost, which in rows:
        print(f"{stem:<10} {n:>9} {lost:>5}  {which}")
    print(f"{'total':<10} {total:>9} {lost_total:>5}")
    if args.json:
        Path(args.json).write_text(json.dumps(result, indent=1, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
