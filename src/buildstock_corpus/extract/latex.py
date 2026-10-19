"""LaTeX -> markdown for the technical reference, via pandoc (pypandoc-binary).

The reference is a multi-file LaTeX project: main.tex assembles chapters with
\\include (ComStock) or \\input (ResStock), and each chapter pulls dense tables with
\\input{tables/...}. We expand those \\input tables ourselves (rather than letting pandoc
read them raw from disk) so we can normalize longtable environments — pandoc renders
longtables as an unparsed raw block unless their multi-page header/footer machinery is
stripped first. The fully expanded, normalized chapter is then converted with pandoc. Dense
tables are the payoff for keeping the tech reference as LaTeX rather than PDF; per-chapter
conversion also yields clean per-file provenance and avoids the custom documentclass.

Per-project knobs come from the source registry (R1.2 of PLAN-resstock.md): the
bibliography pandoc resolves citations from, and the directory figures live in. ResStock's
project also defines a `customLongTable` environment and ships six figures as PDF files;
both are rewritten here into forms pandoc and markdown can carry.
"""

from __future__ import annotations

import hashlib
import re
import struct
import subprocess
import zlib
from pathlib import Path

from ..normalize import Document, collapse_blank_lines, first_heading
from ..paths import PROJECT_ROOT
from ..registry import DEFAULT_BIBLIOGRAPHY

_INCLUDE_RE = re.compile(r"\\include\{([^}]+)\}")
_INPUT_RE = re.compile(r"\\input\{([^}]+)\}")
# Either command names a chapter when it appears in the main file: ComStock's main.tex
# \includes its chapters, ResStock's \inputs them.
_CHAPTER_CMD_RE = re.compile(r"\\(?:include|input)\{([^}]+)\}")
# An unescaped `%` starts a comment that runs to the end of the line; `\%` is a percent sign.
_COMMENT_RE = re.compile(r"(?<!\\)%.*")
# A table's LaTeX label, and the <div> wrapper pandoc emits for it. The label matches the
# table's file name in only 46 of 78 cases, so the wrapper is stamped with the file it came
# from (`data-source="tables/<file>.tex"`) for readers who know the LaTeX layout. ComStock
# labels tables `tab:`; ResStock uses `table:` and, in a few places, `Tab:`.
_TAB_PREFIXES = ("tab:", "table:", "tbl:")
_TAB_LABEL_RE = re.compile(r"\\label\{((?:tab|table|tbl):[^}]+)\}", re.IGNORECASE)
_TAB_DIV_RE = re.compile(r'<div id="((?:tab|table|tbl):[^"]+)"(?![^>]*data-source=)', re.IGNORECASE)
# ResStock's main file defines `customLongTable` with four arguments: column format,
# caption, label and header row. pandoc knows nothing about it, so it is rewritten into the
# plain longtable the definition expands to (see _expand_custom_longtables).
_CUSTOM_LT_BEGIN = "\\begin{customLongTable}"
_CUSTOM_LT_END = "\\end{customLongTable}"
# A figure shipped as a PDF file. Markdown cannot show it and a figure overlay has nothing
# to pin, so the build renders page 1 to PNG and points the reference at that instead.
_PDF_GRAPHIC_RE = re.compile(
    r"(\\includegraphics\s*(?:\[[^\]]*\])?\s*\{)([^}]*\.pdf)(\})", re.IGNORECASE
)
LATEX_PNG_CACHE = PROJECT_ROOT / ".cache" / "latex_png"
# \includegraphics with its options split across lines can trip pandoc's LaTeX reader —
# strip as a last-resort fallback so the chapter still converts (captions survive as text).
_INCLUDEGRAPHICS_RE = re.compile(r"\\includegraphics\s*(?:\[[^\]]*\])?\s*\{[^}]*\}", re.DOTALL)
_LONGTABLE_RE = re.compile(r"\\begin\{longtable\}.*?\\end\{longtable\}", re.DOTALL)
_GFM_SEP_RE = re.compile(r"^\s*\|[\s:|-]*-[\s:|-]*\|\s*$")  # a GFM header separator row
# `center` carries no meaning in markdown (pandoc would emit <div class="center"> noise), and
# dropping both delimiters also heals latent source bugs — one HVAC table has a commented-out
# \begin{center} but a live \end{center}, which pandoc rejects as an unbalanced environment.
_CENTER_RE = re.compile(r"\\(?:begin|end)\{center\}|\\centering\b")
# `\resizebox{<width>}{<height>}{<content>}` is a graphicx scaling wrapper. pandoc's LaTeX
# reader silently DROPS a tabular wrapped in it, so a resized table converts to nothing — the
# prose still \refs it but the data is gone (kitchen_prev_and_power in 4_7_plug_and_process was
# the one corpus-wide casualty). Scaling is meaningless in markdown, so unwrap to the content.
_RESIZEBOX_RE = re.compile(r"\\resizebox\b\s*")
# Multi-page longtable machinery: pandoc leaves the whole environment as a raw block unless
# these are removed. Scoped to inside longtable envs. The table's own \caption and \label
# stay: pandoc 3 carries both (the caption as a line inside a <div id="<label>"> wrapper),
# and every longtable in both references has one -- stripping them, as the first version of
# this loader did, lost the title of all eight ComStock longtables. `\noalign{}` (booktabs
# spacing, on every rule in the ResStock tables) makes pandoc emit an empty trailing row.
_LT_MACHINERY = re.compile(
    r"\\end(?:firsthead|head|foot|lastfoot)"
    r"|\\noalign\{[^}]*\}"
    r"|\\multicolumn\{[^}]*\}\{[^}]*\}\s*\{.*?\}\s*\\\\\s*\\hline"  # "Continued..." row
)


def _skip_braced_group(text: str, i: int) -> int | None:
    """If text[i] opens a `{...}` group, return the index just past its matching `}`.

    Brace-matched rather than regex'd because the group nests (a resized tabular holds
    `\\multicolumn{...}{...}` all the way down)."""
    if i >= len(text) or text[i] != "{":
        return None
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return j + 1
    return None


def _strip_resizebox(text: str) -> str:
    """Unwrap every `\\resizebox{<w>}{<h>}{<content>}` to just `<content>`.

    Leaves the two size arguments behind and keeps the third (content) group verbatim, so a
    resized tabular reaches pandoc as an ordinary tabular instead of being dropped."""
    out: list[str] = []
    pos = 0
    for m in _RESIZEBOX_RE.finditer(text):
        w = _skip_braced_group(text, m.end())  # {<width>}
        h = _skip_braced_group(text, w) if w is not None else None  # {<height>}
        c = _skip_braced_group(text, h) if h is not None else None  # {<content>}
        if c is None:  # not the shape we expect — leave it untouched for pandoc to handle
            continue
        out.append(text[pos : m.start()])
        out.append(text[h + 1 : c - 1])  # the content, minus its wrapping braces
        pos = c
    out.append(text[pos:])
    return "".join(out)


def _normalize_longtable(block: str) -> str:
    """Strip a longtable's multi-page machinery and its duplicated (first)head row."""
    block = _LT_MACHINERY.sub("", block)
    out: list[str] = []
    prev = None
    for line in block.splitlines():
        s = line.strip()
        if s and s == prev:  # drops the header row repeated by \endfirsthead/\endhead
            continue
        out.append(line)
        prev = s
    return "\n".join(out)


def _expand_inputs(
    text: str, proj_dir: Path, _depth: int = 0, labels: dict[str, str] | None = None
) -> str:
    """Inline \\input{...} files (recursively) so we can normalize their table content
    before pandoc sees it. Missing files are dropped. Longtable and center normalization runs
    once at the top level, after all inputs are inlined.

    `labels`, if given, collects which inlined file defined each table label
    (`tab:<label>` -> `tables/<file>.tex`, relative to the project dir), so the markdown's
    table wrappers can say which LaTeX file they came from (see _stamp_table_sources).
    """
    if _depth > 10:
        return text

    def repl(m: re.Match) -> str:
        rel = m.group(1).strip()
        rel = rel if rel.endswith(".tex") else f"{rel}.tex"
        fp = proj_dir / rel
        if not fp.is_file():
            return ""
        inner = fp.read_text(encoding="utf-8", errors="replace")
        if labels is not None:
            for lab in _TAB_LABEL_RE.findall(inner):
                labels.setdefault(lab, Path(rel).as_posix())
            for _s, _b, args, _e in _iter_custom_longtables(inner):
                labels.setdefault(args[2].strip(), Path(rel).as_posix())
        return _expand_inputs(inner, proj_dir, _depth + 1, labels)

    # An \input the authors commented out is not part of the document. Substituting across
    # the whole text would inline it anyway, its first line swallowed by the comment and the
    # rest live, which is how a table ComStock's HVAC chapter had retired kept appearing.
    text = _sub_outside_comments(_INPUT_RE, repl, text)
    if _depth == 0:
        text = _expand_custom_longtables(text)
        text = _strip_resizebox(text)
        text = _LONGTABLE_RE.sub(lambda m: _normalize_longtable(m.group(0)), text)
        text = _CENTER_RE.sub("", text)
    return text


def _sub_outside_comments(pattern: re.Pattern, repl, text: str) -> str:
    """`pattern.sub(repl, ...)` applied to each line's code, leaving its comment alone."""
    out: list[str] = []
    for line in text.split("\n"):
        m = _COMMENT_RE.search(line)
        code, comment = (line[: m.start()], line[m.start() :]) if m else (line, "")
        out.append(pattern.sub(repl, code) + comment)
    return "\n".join(out)


def _strip_comments(text: str) -> str:
    """Drop every LaTeX comment, keeping the line structure."""
    return "\n".join(_COMMENT_RE.sub("", line) for line in text.split("\n"))


def _iter_custom_longtables(text: str) -> list[tuple[int, int, list[str], int]]:
    """Every well-formed `\\begin{customLongTable}{fmt}{caption}{label}{header} ... \\end{...}`
    as (start, body_start, [fmt, caption, label, header], end), end being the index just
    past `\\end{customLongTable}`. Brace-matched: the format holds `p{3cm}` groups and the
    header `\\texttt{...}`. A malformed one is skipped and reaches pandoc as written."""
    found: list[tuple[int, int, list[str], int]] = []
    pos = 0
    while True:
        i = text.find(_CUSTOM_LT_BEGIN, pos)
        if i < 0:
            return found
        j = i + len(_CUSTOM_LT_BEGIN)
        args: list[str] = []
        for _ in range(4):
            while j < len(text) and text[j].isspace():
                j += 1
            end = _skip_braced_group(text, j)
            if end is None:
                break
            args.append(text[j + 1 : end - 1])
            j = end
        k = text.find(_CUSTOM_LT_END, j)
        if len(args) == 4 and k >= 0:
            found.append((i, j, args, k + len(_CUSTOM_LT_END)))
            pos = k + len(_CUSTOM_LT_END)
        else:
            pos = i + len(_CUSTOM_LT_BEGIN)


def _expand_custom_longtables(text: str) -> str:
    """Rewrite each customLongTable into the longtable its definition expands to: caption and
    label on the first row, the header row under \\toprule, `\\endhead` so the header is
    recognised, `\\bottomrule` closing. The multi-page continuation head the environment also
    defines is left out, as _normalize_longtable would strip it anyway."""
    out: list[str] = []
    pos = 0
    for start, body_start, (fmt, caption, label, header), end in _iter_custom_longtables(text):
        body = text[body_start : end - len(_CUSTOM_LT_END)].strip()
        out.append(text[pos:start])
        out.append(
            f"\\begin{{longtable}}{{{fmt.strip()}}}\n"
            f"\\caption{{{caption.strip()}}} \\label{{{label.strip()}}} \\\\\n"
            f"\\toprule\n{' '.join(header.split())} \\\\\n\\midrule\n\\endhead\n"
            f"{body}\n\\bottomrule\n\\end{{longtable}}"
        )
        pos = end
    out.append(text[pos:])
    return "".join(out)


# --- PDF figures -> PNG ---------------------------------------------------------------------


def _write_png(path: Path, width: int, height: int, rows: list[bytes]) -> None:
    """Write 8-bit RGB rows as a PNG. Hand-rolled (zlib + struct) so the build and the tests
    need neither Pillow nor numpy: the `dev` group has pypdfium2 alone."""

    def chunk(kind: bytes, data: bytes) -> bytes:
        return (
            struct.pack(">I", len(data)) + kind + data
            + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
        )

    raw = b"".join(b"\x00" + row for row in rows)  # filter type 0 (None) on every scanline
    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw, 9))
        + chunk(b"IEND", b"")
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(png)


def render_pdf_page_png(pdf: Path, dest: Path, scale: float = 2.0) -> None:
    """Render page 1 of `pdf` to `dest` as RGB PNG at `scale` x 72 dpi via pypdfium2."""
    import pypdfium2 as pdfium

    doc = pdfium.PdfDocument(str(pdf))
    try:
        bitmap = doc[0].render(scale=scale, rev_byteorder=True)
        buf = bytes(bitmap.buffer)
        n = bitmap.n_channels
        rows: list[bytes] = []
        for y in range(bitmap.height):
            line = buf[y * bitmap.stride : y * bitmap.stride + bitmap.width * n]
            if n == 3 and bitmap.rev_byteorder:
                rows.append(line)  # already RGB
            else:  # BGR / BGRx / BGRA, or RGBx: take three channels per pixel in RGB order
                px = [line[i : i + n] for i in range(0, len(line), n)]
                rows.append(b"".join(p[:3] if bitmap.rev_byteorder else p[2::-1] for p in px))
        _write_png(dest, bitmap.width, bitmap.height, rows)
    finally:
        doc.close()


def _rasterize_pdf_figures(text: str, proj_dir: Path, rasters: dict[str, Path] | None) -> str:
    """Point every `\\includegraphics{...pdf}` at a PNG rendering of the PDF's first page.

    The PNG is cached by the PDF's sha256 under .cache/latex_png/ and recorded in `rasters`
    as {<reference as rewritten, relative to the project dir>: <cache file>}, which the
    build copies next to the chapter so the reference resolves. A PDF that is missing or
    fails to render keeps its original reference, so the gap stays visible."""

    def repl(m: re.Match) -> str:
        rel = m.group(2).strip()
        src = proj_dir / rel
        if not src.is_file():
            return m.group(0)
        png_rel = str(Path(rel).with_suffix(".png").as_posix())
        try:
            sha = hashlib.sha256(src.read_bytes()).hexdigest()
            cached = LATEX_PNG_CACHE / f"{sha}.png"
            if not cached.is_file():
                render_pdf_page_png(src, cached)
        except Exception:  # noqa: BLE001 - leave the reference as written; the audit reports it
            return m.group(0)
        if rasters is not None:
            rasters[png_rel] = cached
        return f"{m.group(1)}{png_rel}{m.group(3)}"

    return _PDF_GRAPHIC_RE.sub(repl, text)


# Character-level fidelity. pandoc faithfully renders TeX's typesetting hints as Unicode:
# `\-` (a discretionary hyphen — a *hint* about where a word may break) becomes U+00AD, `~`
# becomes U+00A0, `--` becomes an en dash. The expanded chapter source carries `\-` in bulk
# (1369 in 6_AppendixA alone), so the character is introduced by our conversion, not upstream.
# The hints mean nothing in markdown, and the soft hyphens land *inside* identifiers where
# they are invisible — `HPA<AD>CCOOL<AD>PLFFPLR`, `FullService<AD>Restaurant`, `EIA<AD>861` —
# so any lexical or hybrid retrieval on the real spelling misses them. Normalize per class;
# one blanket ASCII fold would be wrong (see the placeholder note below).
_SOFT_HYPHEN = "\u00ad"  # deleted outright: a line-break hint with no meaning in markdown
_NBSP = "\u00a0"  # -> plain space
# An en dash between digits is a range: `1980–2004`, `132–220`. The corpus spells the same
# vintage bin both ways — 71 ASCII `1980-2004` against 47 en-dashed, while `Pre-1980` is ASCII
# in all 135 occurrences — so one entity has two spellings and a search for either misses the
# other. Only digit-flanked dashes fold, which is what makes this safe:
_RANGE_DASH_RE = re.compile(r"(?<=\d)\u2013(?=\d)")
# Deliberately NOT folded: the ~204 en dashes that stand alone in a table cell as an
# empty-value placeholder (`| QuickServiceRestaurant | – | – | ... |`). They mean "no value";
# an ASCII `-` there reads as a value or a minus sign, so folding them would put data into a
# cell that has none. Also untouched, none of them a fidelity problem: ° ® ™ ·, smart quotes,
# em dashes, and U+2212 minus.


def _normalize_characters(md: str) -> str:
    """Fold pandoc's typesetting-hint characters to their searchable spelling, per class."""
    md = md.replace(_SOFT_HYPHEN, "")
    md = md.replace(_NBSP, " ")
    return _RANGE_DASH_RE.sub("-", md)


def _dedupe_repeated_header(md: str) -> str:
    """Drop a longtable's header row where pandoc repeats it as the first data row
    (\\endfirsthead + \\endhead both carry the header). GFM shape: row, separator, row==row."""
    lines = md.splitlines()
    drop: set[int] = set()
    for i, line in enumerate(lines):
        if 0 < i < len(lines) - 1 and _GFM_SEP_RE.match(line):
            after = lines[i + 1].strip()
            if after.startswith("|") and after == lines[i - 1].strip():
                drop.add(i + 1)
    return "\n".join(l for j, l in enumerate(lines) if j not in drop)


def _chapter_files(main_tex: Path) -> list[str]:
    """Chapter stems in document order: the main file's \\include and \\input statements,
    comments removed first, so a chapter the authors commented out (ResStock's main does
    this to four, and to its appendix) is not part of the corpus either."""
    text = _strip_comments(main_tex.read_text(encoding="utf-8", errors="replace"))
    return _CHAPTER_CMD_RE.findall(text)


def _pandoc(text: str, cwd: Path, citeproc: bool, bibliography: str = DEFAULT_BIBLIOGRAPHY):
    import pypandoc

    args = [pypandoc.get_pandoc_path(), "-f", "latex", "-t", "gfm", "--wrap=none"]
    if citeproc:
        args += ["--citeproc", f"--bibliography={bibliography}"]
    # Input via stdin (not filename) so we can preprocess; cwd resolves the relative bibliography.
    return subprocess.run(
        args, cwd=str(cwd), input=text, capture_output=True, text=True, encoding="utf-8"
    )


# --- pandoc artefacts: cross-references and heading levels -----------------------------------
#
# pandoc renders `\ref{tab:x}` as <a href="#tab:x" data-reference-type="ref" ...>TEXT</a>,
# where TEXT is its own count within the one chapter file it converted (wrong for chapter 4,
# which is split across eight files) or the bare label in brackets when the target is in
# another file. Neither helps a reader of markdown. The target's own title does: "Table
# “Window Property Data Sources”" can be searched for and found, in this file or another.
_XREF_RE = re.compile(
    r'<a href="#(?P<label>[^"]+)" data-reference-type="[^"]*" data-reference="[^"]*">'
    r"(?P<text>[^<]*)</a>"
)
_BRACED = r"\{((?:[^{}]|\{[^{}]*\})*)\}"
_HEADING_CMD_RE = re.compile(
    r"\\(chapter|section|subsection|subsubsection|paragraph)\*?(?:\[[^\]]*\])?" + _BRACED
)
_CAPTION_CMD_RE = re.compile(r"\\caption(?:\[[^\]]*\])?" + _BRACED)
_ANY_LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
_TEX_CMD_RE = re.compile(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?")
_EQN_LABEL_RE = re.compile(r"(^|[:_])eqn?($|[:_])|equation", re.I)
_CAPTION_PREFIXES = _TAB_PREFIXES + ("fig:",)  # compared case-insensitively
_FORWARD_PREFIXES = ("chap:", "appendix:")  # labels written before their heading, not after


def _tex_to_text(s: str) -> str:
    """A caption or heading's plain text: unwrap macros, drop labels, resolve TeX spacing."""
    s = _ANY_LABEL_RE.sub("", s)
    for _ in range(3):  # nested macros: \textbf{\gls{x}}
        s = re.sub(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?\{([^{}]*)\}", r"\1", s)
    s = _TEX_CMD_RE.sub("", s)
    s = s.replace("~", " ").replace("--", "\u2013").replace("\\%", "%").replace("\\&", "&")
    s = s.replace("{", "").replace("}", "")
    return " ".join(s.split())


def _label_titles(proj_dir: Path) -> dict[str, str]:
    """Every `\\label` in the project -> the title of the thing it labels.

    A table or figure label takes the nearest preceding \\caption; a section-like label
    (sec:, chap:, a bare name) the nearest heading -- preceding, or following for chap:
    and appendix: labels, which are written before the heading. Equation labels have no
    title and are left out, so the reference keeps its plain label text.
    """
    titles: dict[str, str] = {}
    for tex in sorted(proj_dir.rglob("*.tex")):
        text = tex.read_text(encoding="utf-8", errors="replace")
        heads = [(m.start(), _tex_to_text(m.group(2))) for m in _HEADING_CMD_RE.finditer(text)]
        caps = [(m.start(), _tex_to_text(m.group(1))) for m in _CAPTION_CMD_RE.finditer(text)]
        # customLongTable carries caption and label as arguments, not as \caption/\label
        for _s, _b, (_fmt, caption, label, _hdr), _e in _iter_custom_longtables(text):
            titles.setdefault(label.strip(), _tex_to_text(caption))
        for m in _ANY_LABEL_RE.finditer(text):
            label = m.group(1).strip()
            if label in titles or _EQN_LABEL_RE.search(label):
                continue
            pos = m.start()
            if label.lower().startswith(_CAPTION_PREFIXES):
                prev = [t for p, t in caps if p < pos]
                if prev:
                    titles[label] = prev[-1]
            elif label.startswith(_FORWARD_PREFIXES):
                nxt = [t for p, t in heads if p > pos]
                if nxt:
                    titles[label] = nxt[0]
            else:
                prev = [t for p, t in heads if p < pos]
                if prev:
                    titles[label] = prev[-1]
    return titles


def _render_cross_references(md: str, titles: dict[str, str]) -> str:
    """Replace pandoc's cross-reference anchors with the target's title in quotes, or with
    the anchor's own text (brackets dropped) when the label has no title."""

    def repl(m: re.Match) -> str:
        title = titles.get(m.group("label"))
        if title:
            return f"\u201c{title}\u201d"
        return m.group("text").strip().strip("[]")

    return _XREF_RE.sub(repl, md)


_MD_HEADING_RE = re.compile(r"^(#{1,6})(\s+.*)$")


def _normalize_heading_levels(md: str) -> str:
    """No heading sits more than one level below the heading before it.

    pandoc maps \\paragraph to H5 even when a chapter uses it directly under its H1, and two
    chapters go \\section -> \\subsubsection. Each heading is re-levelled to at most its
    nearest open ancestor's level + 1; siblings at the same original level get the same new
    level, so structure is kept while the gaps close. Fenced code is left alone.
    """
    out: list[str] = []
    stack: list[tuple[int, int]] = []  # (original level, new level)
    in_fence = False
    for line in md.split("\n"):
        if line.startswith("```"):
            in_fence = not in_fence
        m = None if in_fence else _MD_HEADING_RE.match(line)
        if not m:
            out.append(line)
            continue
        orig = len(m.group(1))
        while stack and stack[-1][0] >= orig:
            stack.pop()
        new = min(orig, (stack[-1][1] + 1) if stack else 1)
        stack.append((orig, new))
        out.append("#" * new + m.group(2))
    return "\n".join(out)


def _stamp_table_sources(md: str, labels: dict[str, str], chapter_file: str) -> str:
    """Add `data-source="<file>.tex"` to every table wrapper pandoc emitted.

    A table whose label an inlined file defined names that file; a table written in the
    chapter itself names the chapter. Wrappers that already carry the attribute are left
    alone, so the stamp is idempotent.
    """
    return _TAB_DIV_RE.sub(
        lambda m: f'{m.group(0)} data-source="{labels.get(m.group(1), chapter_file)}"', md
    )


def _convert(
    tex_path: Path,
    cwd: Path,
    bibliography: str = DEFAULT_BIBLIOGRAPHY,
    rasters: dict[str, Path] | None = None,
) -> tuple[str, str]:
    """Convert one chapter to gfm, degrading gracefully: try the input-expanded source
    first, then a figure-stripped copy; resolve citations when the bibliography is present.
    Table wrappers in the result name the LaTeX file each table came from; PDF figures are
    rendered to PNG and the rendering recorded in `rasters` (see _rasterize_pdf_figures)."""
    labels: dict[str, str] = {}
    raw = _expand_inputs(tex_path.read_text(encoding="utf-8", errors="replace"), cwd, labels=labels)
    raw = _rasterize_pdf_figures(raw, cwd, rasters)
    chapter_file = tex_path.relative_to(cwd).as_posix() if tex_path.is_relative_to(cwd) else tex_path.name
    citeproc_opts = [True, False] if (cwd / bibliography).exists() else [False]
    last = ""
    for text in (raw, _INCLUDEGRAPHICS_RE.sub("", raw)):
        for citeproc in citeproc_opts:
            proc = _pandoc(text, cwd, citeproc, bibliography)
            if proc.returncode == 0:
                return _stamp_table_sources(proc.stdout, labels, chapter_file), proc.stderr
            last = proc.stderr
    raise RuntimeError(f"pandoc failed on {tex_path.name}: {last[:300]}")


def load_latex_docs(
    clone_dir: Path,
    latex_main_rel: str,
    product: str,
    release: str,
    source_id: str,
    limit: int | None = None,
    bibliography: str = DEFAULT_BIBLIOGRAPHY,
    rasters: dict[str, Path] | None = None,
) -> tuple[list[Document], list[str]]:
    """Convert each chapter of the LaTeX project into a Document. Returns (docs, warnings).

    `limit` stops after that many converted chapters (smoke-test sampling). Each chapter
    costs its own pandoc subprocess, so stopping early is a real saving rather than a
    post-hoc filter. `bibliography` is the registry's, relative to the project dir. If
    `rasters` is given it is filled with {<png ref relative to the project dir>: <cache
    file>} for every PDF figure that was rendered, for the build to copy into place.
    """
    main_tex = clone_dir / latex_main_rel
    proj_dir = main_tex.parent
    docs: list[Document] = []
    warnings: list[str] = []
    titles = _label_titles(proj_dir)  # once per project: cross-references span chapters

    for stem in _chapter_files(main_tex):
        tex_name = stem if stem.endswith(".tex") else f"{stem}.tex"
        tex_path = proj_dir / tex_name
        if not tex_path.is_file():
            warnings.append(f"missing chapter file: {tex_name}")
            continue
        try:
            md, stderr = _convert(tex_path, proj_dir, bibliography, rasters)
        except RuntimeError as exc:  # one unparseable chapter must not abort the build
            warnings.append(str(exc))
            continue
        md = _normalize_heading_levels(_render_cross_references(md, titles))
        md = _normalize_characters(_dedupe_repeated_header(md))
        body = collapse_blank_lines(md)
        if not body.strip():
            continue
        rel = (proj_dir / tex_name).relative_to(clone_dir).as_posix()
        docs.append(
            Document(
                product=product,
                release=release,
                source_id=source_id,
                source_type="latex",
                source_path=rel,
                title=first_heading(body) or Path(tex_name).stem,
                body=body,
            )
        )
        if stderr.strip():
            warnings.append(f"{tex_name}: {stderr.strip()[:150]}")
        if limit is not None and len(docs) >= limit:
            break
    return docs, warnings
