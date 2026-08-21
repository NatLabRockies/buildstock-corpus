# Figure-description overlay rollout — kickoff / handoff

**Purpose.** Roll the `figures:` overlay treatment (already prototyped and accepted on `85853`
and `86100`) across the rest of the ComStock 2025-3 corpus. This file is written to be opened
cold in a fresh session — everything you need to start is here.

**Read this first, then pick up the next unfinished batch.** Do not try to do the whole corpus
in one pass.

**Progress:** Batch A done (PR #14). Batch B done (PR #15, + manifest fix #16). Batch C done
(PR #17). 528 figures described across 32 docs. **Next up: Batch D.**

> ⚠️ **The description standard was deliberately lowered on 2026-08-21 — read §2.1 before
> authoring anything.** Batches B and C ran ~180 words per description, roughly 3x the
> prototype standard the user actually accepted. That drift is the reason the rollout was
> taking too long. Do not use B/C entries as your model for length; use `86100`. Existing
> entries are **not** being rewritten, so the corpus is intentionally uneven — recent files
> being longer is not a precedent.

---

## 0. TL;DR of the task

docling extracts every picture in a measure PDF as a bare `![Image](…png)` reference. The
chart/photo itself is invisible to retrieval and unreadable without the bitmap. For each
**real figure** we hand-author an overlay entry that (a) rewrites the ref with a written
`alt`, and (b) injects a `description` paragraph below it for retrieval. Decorative images
(logos, cover art, dividers, section icons) are **skipped entirely** — no entry at all.

Overlays are hand-authored YAML sidecars injected at build time. They never touch
`processed/`. Each entry is pinned to the on-disk PNG's sha256 so `bsc validate` flags a
stale/repointed bitmap instead of silently shipping a wrong description.

---

## 1. What's already done (reference examples)

Branch: `alt-text-85853-prototype` (the `figures:` engine lives here; base your work on it or
merge it first).

- `overlays/…/measure_pdfs/85853.yaml` — EUSS Commercial webinar deck, **60 figures = 11
  decorative + 49 described**. Shows the `decorative: true` shape.
- `overlays/…/measure_pdfs/86100.yaml` — LED Lighting measure doc, **10 figures described,
  cover images skipped entirely** (the pattern the user endorsed: "figures only, disregard
  decorative"). This is the cleaner template — **copy its structure *and its length*.** At ~69
  words per description it is the closest thing in the corpus to the §2.1 budget.

⚠️ **Do not use Batch B or C files as length models** (`86105`, `98223`, `86585`, `86897`,
`87542`, `89117`, `89131`, `95014`, … ~180 words each). Their *structure* is fine; their depth
is 3x what the user wants. `85853` (45 words) and `86100` (69 words) are the reference points.

Engine: `src/buildstock_corpus/overlay.py` (`_apply_figure`, `_find_image_refs`,
`_figure_injection`, `_figure_applied_above`); counted in `manifest.py` + `build.py`; tests in
`tests/test_overlay.py`. **Do not modify the engine** — the schema below is stable. (One
loose end: `overlays/README.md` documents `tables:` but not `figures:` yet. Optional nicety:
add a figures section there mirroring §3. Not required to do the work.)

---

## 2. Fixed decisions (do not re-litigate)

| Decision | Value |
|---|---|
| Scope | **Figures only.** Skip decorative images entirely (no entry). |
| Entry shape | `alt` **and** `description` for every real figure. |
| `method` | `vision-description` (we interpret a chart; we do not transcribe legible cells — that's `vision-transcription`, used by table overlays). |
| `described_utc` | The date you author it (YYYY-MM-DD). |
| Pinning | Every entry pins `source_image_sha256`, computed from the PNG **on disk**. |
| Decorative-in-85853 | 85853 used `decorative: true` + short alt. **New docs: just omit decorative images** (86100 style). |
| Depth | **Prototype level (~55 words).** See §2.1 — this is a hard budget, not a floor. |
| Corroboration | **Dropped.** Do not reconcile figure values against body text or tables. |

### 2.1 Depth budget (set 2026-08-21 — this replaces the earlier "read numbers off the figure")

**Target: `description` ≈ 40–70 words. `alt` ≤ 120 characters, one line.** Treat 70 words as a
ceiling you have to justify, not an average to hit. If a figure genuinely needs more (a rare
multi-panel diagram that is the whole point of the document), it may go to ~100 — but that
should be one or two figures per doc, not the default.

A description has exactly four jobs, in this order:

1. **Figure number + chart type** — "Figure 12: three-panel stacked bar chart of…"
2. **Axes with units, and the series/legend** — enough for a retrieval hit on the right chart.
3. **One quantitative takeaway** — the headline number or the direction and rough magnitude.
4. **A pointer to the authoritative table** where per-segment values live ("See Table 8").

**Stop doing these** (all three are what inflated Batches B and C):

- **Enumerating data labels.** If a chart prints values on every bar, do not transcribe them —
  they are in the table. Name the two or three largest and move on. (86100's per-building-type
  list is the *one* legacy exception; don't imitate it.)
- **Exhaustive panel walkthroughs.** For an N-panel grid, say what the rows/columns are and
  give the one or two panels where the scenarios visibly diverge. Do not narrate every panel.
  Compare `98223` figure 9 (214 words) against what §2.1 asks for — that figure should be ~60.
- **Reconciling the figure against the prose.** No recomputing percentages to explain a
  rounded `(-0%)` label, no "consistent with the sub-1-percent value in Table 3", no
  cross-checks against the exec summary. If you happen to spot a *blatant* contradiction
  (figure says up, text says down), note it in the sidecar's QA header — one line — and keep
  going. Don't go looking.

**Don't zoom to resolve unlabeled geometry.** If a value isn't legible at normal resolution,
it doesn't go in the description. The table has it. (This supersedes the zoom/corroboration
techniques used in Batches B and C.)

The stacked-bar guidance that already existed for Figure-7-type charts is now just a special
case of this rule: pattern + totals + direction, cite the table, never enumerate bands.

---

## 3. The `figures:` schema

Top of file (identical across docs except `source_path`):

```yaml
product: comstock
release: comstock_amy2018_2025_release_3
source_id: upgrade_measures
source_path: measure_pdfs/<ID>.pdf      # or draft_publications/files/<name>.pdf
figures:
- source_image: <ID>_images/image_000002_<64hex>.png   # basename must match the ![](…) target
  source_image_sha256: <sha256 of that PNG on disk>
  method: vision-description
  described_utc: '2026-08-20'
  alt: One line, <=120 chars, no ']' character (it breaks the markdown alt)
  description: |-
    40-70 words: chart type, axes + units, series/legend, one quantitative takeaway, and a
    pointer to the table holding the per-segment values. See §2.1 — do not exceed the budget.
```

Rules the engine enforces (each failure **warns and skips**, never raises):

- `source_image`, `source_image_sha256`, and `alt` are required. `]` in `alt` is refused.
- The basename of `source_image` must match exactly **one** not-yet-described `![](…)` ref in
  the doc. Zero matches (or a stale/absent image) → warn+skip. Two matches → neither is
  touched (ambiguous). So one entry ⇢ one image ref.
- `source_image_sha256` is re-hashed from disk at build **and** at `bsc validate`. Mismatch →
  the injection is dropped and reported (folded into the image `checked`/`unverifiable`
  counters — **do not add new stats keys; tests assert exact stats dicts**).
- Injection is idempotent — re-running the build won't double-inject.
- Decorative (85853 only): add `decorative: true` and omit `description` (alt-only).
- Figures run **after** tables in `apply_overlays`, so if a table overlay already anchors on
  the same bitmap, the table replacement wins.

---

## 4. The proven workflow (per document)

1. **Branch first** (standing rule). One branch per batch, e.g. `figures-batch-a`.
2. Open the doc's processed markdown:
   `processed/comstock/comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/<ID>.md`.
   Note each `![Image](…png)` ref and the caption line above it (if any).
3. **View every PNG** in `…/measure_pdfs/<ID>_images/` with the Read tool (it renders images).
   For each: decide **figure vs decorative**. Decorative = logos, cover/title art, dividers,
   footer icons, NREL branding → skip. Figure = any chart/plot/diagram/photo carrying
   information → describe.
4. For each figure, write `alt` (one line, ≤120 chars) + `description` (**40–70 words** per
   §2.1: chart type, axes + units, series, one takeaway, table pointer). One pass per figure —
   read it, write it, move on. No zooming to resolve unlabeled geometry, no cross-checking
   against the prose. Flag only the least-certain *headline* reads for QA.
5. **Generate the YAML with a throwaway script** (see §5) so the sha256 pins come from disk,
   never hand-typed.
   - Net-new doc → new file `…/measure_pdfs/<ID>.yaml`.
   - **Doc that already has a table overlay** (see §6 list) → **add a `figures:` block to the
     existing file**, do not create a second file. Keep the existing `tables:` block.
6. Build + validate + inspect:
   ```bash
   uv run bsc build && uv run bsc validate && uv run pytest
   ```
   Then read the injected region of the processed `.md` to eyeball before/after.
7. Show the user before/after for a couple of figures per batch for the QA pass.
8. Delete the throwaway generator script.

---

## 5. Generator script pattern

Author the data in Python (index, alt, desc), compute sha256 from disk, emit YAML with block
scalars. Skeleton (adapt from the 85853/86100 generators — they were deleted after use, but
this is their shape):

```python
# _gen_<ID>_overlay.py  — run with:  uv run python _gen_<ID>_overlay.py  ,  then delete
import hashlib, yaml
from pathlib import Path

ID = "95006"
IMG_DIR = Path(f"processed/comstock/comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/{ID}_images")
OUT = Path(f"overlays/comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/{ID}.yaml")

# (image_index, alt, description) — figures only; omit decorative indices entirely
DATA = [
    ("000002", "…alt…", "…description…"),
    # …
]

def resolve(index):
    hits = list(IMG_DIR.glob(f"image_{index}_*.png"))
    assert len(hits) == 1, f"{index}: {len(hits)} matches"
    return hits[0]

class Dumper(yaml.SafeDumper): pass
def str_rep(d, data):
    style = "|" if len(data) > 120 else None
    return d.represent_scalar("tag:yaml.org,2002:str", data, style=style)
Dumper.add_representer(str, str_rep)

figs = []
for index, alt, desc in DATA:
    p = resolve(index)
    figs.append({
        "source_image": f"{ID}_images/{p.name}",
        "source_image_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        "method": "vision-description",
        "described_utc": "2026-08-20",
        "alt": alt,
        "description": desc,
    })

doc = {"product": "comstock", "release": "comstock_amy2018_2025_release_3",
       "source_id": "upgrade_measures", "source_path": f"measure_pdfs/{ID}.pdf",
       "figures": figs}

header = f"# Hand-authored figure descriptions for measure_pdfs/{ID}.pdf\n# …context…\n\n"
OUT.write_text(header + yaml.dump(doc, Dumper=Dumper, sort_keys=False,
                                  allow_unicode=True, width=98), encoding="utf-8")
```

For a doc that already has a `tables:` overlay, don't overwrite — read the file, append the
generated `figures:` block, and write it back (or hand-merge).

---

## 6. Work-list — 49 measure PDFs remaining

51 measure PDFs have images; `85853` and `86100` are done → **49 left**. Batches are sliced
smallest-first (image count in parentheses) so early batches are quick wins. **≤10 docs per
batch / branch** (standing rule). Actual described-figure counts will be lower (decorative
skipped).

### Net-new figure overlays (create `<ID>.yaml`) — 36 docs

**Batch A** (10): `89343`(7) `92546`(8) `95004`(11) `96597`(11) `95006`(14) `87570`(15)
`95013`(15) `89126`(16) `89133`(16) `92618`(16)

**Batch B** (10): `95009`(16) `95015`(16) `95119`(16) `89132`(17) `89341`(17) `89131`(18)
`92502`(18) `87542`(20) `89340`(20) `89481`(20)

**Batch C** (10): `95014`(20) `86897`(21) `98223`(22) `92504`(23) `89120`(24) `98345`(25)
`98346`(25) `86585`(26) `89117`(26) `86105`(28)

**Batch D** (6, the heavies): `89239`(31) `95003`(33) `95002`(40) `92766`(50) `87746`(61)
`89653`(64)

### Add a `figures:` block to an existing table overlay — 13 docs

These already have a `tables:` overlay file — **edit it, keep `tables:`, add `figures:`.**

**Batch E** (10): `86599`(15) `86601`(17) `96598`(18) `86602`(20) `95005`(20) `86199`(25)
`89128`(25) `89130`(27) `87536`(29) `89040`(29)

**Batch F** (3): `89042`(29) `98224`(30) `86103`(37)

---

## 7. Other categories (scope notes)

The user said "all the categories." After surveying the three top-level dirs:

- **`technical_reference`** (LaTeX docs) — **0 image refs. Nothing to do.**
- **`upgrade_measures`** — the work above. Also 2 live docs under
  `draft_publications/files/` (space-named `.md`, dated Aug 20). These are the "holding area
  for docs that will eventually be published" — **do them last / optionally**, and only the
  space-named live outputs. ⚠️ The underscore-named `_images` dirs (dated Jul 31) are **stale
  orphans from before the `assets`→`draft_publications` rename** — do not describe those.
- **`github_site`** (18 `.md` files with image refs) — **treat as a separate follow-up, not
  part of this sweep.** Per project findings, dense tables on the measure pages are embedded
  as PNG *table-images* whose data survives via the PDF/table-overlay path — those are not
  figures. Some pages may carry real charts too. Before touching github_site, triage each
  ref as figure-chart vs table-image; the latter is out of scope for `figures:`.

---

## 8. Standing constraints (from project memory — all still in effect)

- **Branch before making changes.** One branch per batch.
- **Never run `bsc fetch`** — it re-downloads every PDF and can break hash pins. Rebuild
  instead (`bsc build`).
- **Versioning/provenance is load-bearing** — every entry pinned to the release via the
  overlay's top-level `release`/`source_path` and the per-entry sha256.
- **Chunks of ≤10 docs** at a time.
- **Vision-generated numbers need a human QA pass** before treated as a release record. Call
  out the least-certain reads (dense stacked bars, unlabeled segments) per batch. Under §2.1
  there are far fewer numbers to QA by design — the tables carry the values, and the
  `description` carries the headline only.
- **Depth is capped (§2.1).** ~40–70 words, `alt` ≤120 chars, no corroboration against prose.
  If you find yourself investigating a figure, you have left the intended scope.
- **The user handles PRs** — do not install `gh` or create PRs.
- Do not swap the embedder (`bge-small-en-v1.5` stands); keep the transform retrieval-agnostic.

---

## 9. Definition of done (per batch)

`uv run bsc build && uv run bsc validate && uv run pytest` all green; injected regions
eyeballed in a couple of the processed `.md` files; before/after shown to the user for the QA
pass; throwaway generator scripts deleted; branch left for the user to PR.

Plus the length check — the batch's mean `description` word count should land in the 40–70
band. If it's drifting past ~90, the standard has slipped again; trim before opening the PR:

```bash
uv run python scripts/check_figure_desc_budget.py
```

It exits non-zero if a file you authored drifted past the 90-word mean ceiling, and lists
individual over-long descriptions and over-cap `alt`s so you know what to trim. Pre-rollback
files (85853/86100 + Batches A–C) are waived by name in `GRANDFATHERED` — **add your batch's
IDs there only if the user decides not to trim them**, never to silence a fresh drift.
