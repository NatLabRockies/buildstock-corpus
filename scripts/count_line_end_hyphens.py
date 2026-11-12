"""Count the hyphens a PDF prints at a line end, and what became of each in the markdown.

docling joins the lines of a paragraph, and when a line ends in a hyphen between two words
it drops the hyphen and runs the halves together. That is right for a word the typesetter
split at a syllable ('Applica-' / 'bility') and wrong for a word that is spelled with the
hyphen and merely broke there ('Post-' / 'Retrofit' became 'PostRetrofit'; a URL lost a
hyphen of its path). No character is left behind, so nothing else reports it (plan step
R4.7).

For every line-end hyphen in a PDF's text layer this prints the two halves and four counts
that say which kind it is and whether the markdown has it right:

    pdf_hyph    times the PDF prints the two halves hyphenated inside a line
    pdf_joined  times the PDF prints them as one unbroken word inside a line
    md_hyph     times the markdown has them hyphenated
    md_joined   times the markdown has them run together

A break whose joined form the PDF never prints inside a line is a hyphen that belongs to
the word (`keep`); one the PDF prints joined and never hyphenated is a syllable break
(`join`); the rest are `unclear`. `md_joined` above `pdf_joined` means the markdown runs
together something the PDF does not.

pdfium marks a line-end hyphen after a letter as U+FFFE (and gives no line break after
it); after a digit it leaves '-' and the line break. Both are counted.

    uv run python scripts/count_line_end_hyphens.py --product resstock \
        --release resstock_amy2018_2025_release_1 [--json out.json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import pypdfium2 as pdfium

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from buildstock_corpus.paths import PROJECT_ROOT, manifest_file, raw_root  # noqa: E402

_WORD = r"[A-Za-z0-9]"
# A line-end hyphen: U+FFFE (pdfium's mark, no newline follows) or '-' then a line break,
# with a word character on each side.
_BREAK_RE = re.compile(rf"({_WORD}+)(?:￾|-\r?\n)({_WORD}+)")


def pdf_text(path: Path) -> str:
    doc = pdfium.PdfDocument(str(path))
    try:
        pages = []
        for i in range(len(doc)):
            tp = doc[i].get_textpage()
            try:
                pages.append(tp.get_text_range())
            finally:
                tp.close()
        return "\n".join(pages)
    finally:
        doc.close()


def _count(pattern: str, text: str) -> int:
    return len(re.findall(rf"(?<!{_WORD}){pattern}(?!{_WORD})", text))


def breaks_in(pdf: str, md: str) -> list[dict]:
    """One record per distinct (left, right) pair broken at a line end in `pdf`."""
    inline = _BREAK_RE.sub(lambda m: f"{m.group(1)}\x00{m.group(2)}", pdf)  # breaks masked out
    out = []
    for (left, right), n in sorted(Counter(m.groups() for m in _BREAK_RE.finditer(pdf)).items()):
        l, r = re.escape(left), re.escape(right)
        rec = {
            "left": left,
            "right": right,
            "breaks": n,
            "pdf_hyph": _count(f"{l}-{r}", inline),
            "pdf_joined": _count(f"{l}{r}", inline),
            "md_hyph": _count(f"{l}-{r}", md),
            "md_joined": _count(f"{l}{r}", md),
        }
        if rec["pdf_joined"] == 0:
            rec["kind"] = "keep"
        elif rec["pdf_hyph"] == 0:
            rec["kind"] = "join"
        else:
            rec["kind"] = "unclear"
        rec["md_wrong"] = max(0, rec["md_joined"] - rec["pdf_joined"]) if rec["kind"] != "join" else 0
        out.append(rec)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--product", required=True)
    ap.add_argument("--release", required=True)
    ap.add_argument("--json", type=Path, help="also write every record here")
    args = ap.parse_args()

    manifest = json.loads(manifest_file(args.product, args.release).read_text(encoding="utf-8"))
    processed = manifest_file(args.product, args.release).parent
    raw = raw_root(args.product, args.release)
    report: dict[str, list[dict]] = {}
    totals: Counter = Counter()
    for source in manifest["sources"]:
        for a in source["artifacts"]:
            if not a["source_path"].lower().endswith(".pdf"):
                continue
            pdf = next((p for p in (raw / a["source_path"], PROJECT_ROOT / a["source_path"]) if p.is_file()), None)
            if pdf is None:
                print(f"  skip {a['source_path']}: PDF not on disk", file=sys.stderr)
                continue
            md = (processed / a["output_path"]).read_text(encoding="utf-8")
            recs = breaks_in(pdf_text(pdf), md)
            report[a["source_path"]] = recs
            kinds = Counter()
            for r in recs:
                kinds[r["kind"]] += r["breaks"]
            wrong = sum(r["md_wrong"] for r in recs)
            totals.update(kinds)
            totals["md_wrong"] += wrong
            print(f"{a['source_path']}: {sum(kinds.values())} line-end hyphens "
                  f"(keep {kinds['keep']}, join {kinds['join']}, unclear {kinds['unclear']}); "
                  f"{wrong} run together in the markdown")
            for r in recs:
                if r["md_wrong"] or r["kind"] != "keep":
                    print(f"    {r['kind']:7} {r['left']}|{r['right']}  x{r['breaks']}  "
                          f"pdf {r['pdf_hyph']}-/{r['pdf_joined']}j  md {r['md_hyph']}-/{r['md_joined']}j")
    print(f"total: keep {totals['keep']}, join {totals['join']}, unclear {totals['unclear']}; "
          f"{totals['md_wrong']} run together in the markdown")
    if args.json:
        args.json.write_text(json.dumps(report, indent=1), encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
