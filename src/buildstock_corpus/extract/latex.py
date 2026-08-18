"""LaTeX -> markdown for the technical reference, via pandoc (pypandoc-binary).

The reference is a multi-file LaTeX project: main.tex assembles chapters with
\\include, and each chapter pulls dense tables with \\input{tables/...}. We expand those
\\input tables ourselves (rather than letting pandoc read them raw from disk) so we can
normalize longtable environments — pandoc renders longtables as an unparsed raw block
unless their multi-page header/footer machinery is stripped first. The fully expanded,
normalized chapter is then converted with pandoc. Dense tables are the payoff for keeping
the tech reference as LaTeX rather than PDF; per-chapter conversion also yields clean
per-file provenance and avoids the custom documentclass.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from ..normalize import Document, collapse_blank_lines, first_heading

_INCLUDE_RE = re.compile(r"\\include\{([^}]+)\}")
_INPUT_RE = re.compile(r"\\input\{([^}]+)\}")
# \includegraphics with its options split across lines can trip pandoc's LaTeX reader —
# strip as a last-resort fallback so the chapter still converts (captions survive as text).
_INCLUDEGRAPHICS_RE = re.compile(r"\\includegraphics\s*(?:\[[^\]]*\])?\s*\{[^}]*\}", re.DOTALL)
_LONGTABLE_RE = re.compile(r"\\begin\{longtable\}.*?\\end\{longtable\}", re.DOTALL)
_GFM_SEP_RE = re.compile(r"^\s*\|[\s:|-]*-[\s:|-]*\|\s*$")  # a GFM header separator row
# `center` carries no meaning in markdown (pandoc would emit <div class="center"> noise), and
# dropping both delimiters also heals latent source bugs — one HVAC table has a commented-out
# \begin{center} but a live \end{center}, which pandoc rejects as an unbalanced environment.
_CENTER_RE = re.compile(r"\\(?:begin|end)\{center\}|\\centering\b")
# Multi-page longtable machinery: pandoc leaves the whole environment as a raw block unless
# these are removed. Scoped to inside longtable envs so real \caption on \begin{table} survive.
_LT_MACHINERY = re.compile(
    r"\\end(?:firsthead|head|foot|lastfoot)"
    r"|\\caption\s*(?:\[[^\]]*\])?\{[^}]*\}"
    r"|\\label\{[^}]*\}"
    r"|\\multicolumn\{[^}]*\}\{[^}]*\}\s*\{.*?\}\s*\\\\\s*\\hline"  # "Continued..." row
)


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


def _expand_inputs(text: str, proj_dir: Path, _depth: int = 0) -> str:
    """Inline \\input{...} files (recursively) so we can normalize their table content
    before pandoc sees it. Missing files are dropped. Longtable and center normalization runs
    once at the top level, after all inputs are inlined."""
    if _depth > 10:
        return text

    def repl(m: re.Match) -> str:
        rel = m.group(1).strip()
        fp = proj_dir / (rel if rel.endswith(".tex") else f"{rel}.tex")
        if not fp.is_file():
            return ""
        inner = fp.read_text(encoding="utf-8", errors="replace")
        return _expand_inputs(inner, proj_dir, _depth + 1)

    text = _INPUT_RE.sub(repl, text)
    if _depth == 0:
        text = _LONGTABLE_RE.sub(lambda m: _normalize_longtable(m.group(0)), text)
        text = _CENTER_RE.sub("", text)
    return text


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
    """Chapter stems in document order, from main.tex's \\include statements."""
    return _INCLUDE_RE.findall(main_tex.read_text(encoding="utf-8", errors="replace"))


def _pandoc(text: str, cwd: Path, citeproc: bool):
    import pypandoc

    args = [pypandoc.get_pandoc_path(), "-f", "latex", "-t", "gfm", "--wrap=none"]
    if citeproc:
        args += ["--citeproc", "--bibliography=bibliography.bib"]
    # Input via stdin (not filename) so we can preprocess; cwd resolves the relative bibliography.
    return subprocess.run(
        args, cwd=str(cwd), input=text, capture_output=True, text=True, encoding="utf-8"
    )


def _convert(tex_path: Path, cwd: Path) -> tuple[str, str]:
    """Convert one chapter to gfm, degrading gracefully: try the input-expanded source
    first, then a figure-stripped copy; resolve citations when a bibliography is present."""
    raw = _expand_inputs(tex_path.read_text(encoding="utf-8", errors="replace"), cwd)
    citeproc_opts = [True, False] if (cwd / "bibliography.bib").exists() else [False]
    last = ""
    for text in (raw, _INCLUDEGRAPHICS_RE.sub("", raw)):
        for citeproc in citeproc_opts:
            proc = _pandoc(text, cwd, citeproc)
            if proc.returncode == 0:
                return proc.stdout, proc.stderr
            last = proc.stderr
    raise RuntimeError(f"pandoc failed on {tex_path.name}: {last[:300]}")


def load_latex_docs(
    clone_dir: Path,
    latex_main_rel: str,
    product: str,
    release: str,
    source_id: str,
    limit: int | None = None,
) -> tuple[list[Document], list[str]]:
    """Convert each chapter of the LaTeX project into a Document. Returns (docs, warnings).

    `limit` stops after that many converted chapters (smoke-test sampling). Each chapter
    costs its own pandoc subprocess, so stopping early is a real saving rather than a
    post-hoc filter.
    """
    main_tex = clone_dir / latex_main_rel
    proj_dir = main_tex.parent
    docs: list[Document] = []
    warnings: list[str] = []

    for stem in _chapter_files(main_tex):
        tex_name = stem if stem.endswith(".tex") else f"{stem}.tex"
        tex_path = proj_dir / tex_name
        if not tex_path.is_file():
            warnings.append(f"missing chapter file: {tex_name}")
            continue
        try:
            md, stderr = _convert(tex_path, proj_dir)
        except RuntimeError as exc:  # one unparseable chapter must not abort the build
            warnings.append(str(exc))
            continue
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
