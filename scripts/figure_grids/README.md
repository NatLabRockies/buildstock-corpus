# Reading a number grid that a report shows as a picture

Some measure reports paste a spreadsheet range into the document as an image and caption it
as a figure (performance maps by air and water temperature). The values have no text layer.
These scripts read such a grid and, more to the point, check the reading by means that do
not depend on the reader. They were used for the 42 figure grids of 95032, 95034, 95036 and
96826 (plan step R4.2b); the transcriptions are `tables:` entries labelled "Figure N" in
those sidecars.

Run from the repo root with `GRID_DIR` set to a working folder outside the repo.

1. `extract.py <pdf> $GRID_DIR/<stem>`: the embedded bitmaps at their own resolution. A
   page render at 1.5x is too coarse for these; the bitmap itself is legible.
2. `cells.py <stem>/<image> ...`: finds the rows and the right-aligned number columns, then
   recognises every cell on its own, twice (colour at 4x, grey at 5x), with RapidOCR.
   `--proj` takes the columns from the ink when text detection merged a whole row.
   Writes `cells.json`.
3. `check.py`: structure and arithmetic. Flags a cell where the two recognitions differ, a
   value with the wrong number of decimals, labels that do not increase, and, for a figure
   with Manufacturer / Curvefit / Difference blocks, any cell where Manufacturer minus
   Curvefit is not Difference. Corrections made after looking at the image go in
   `overrides.json` (`{"<image>": {"<row>,<col>": "value"}}`). Writes `grids.json`.
4. `fit.py`: for a single grid, fits a low-order surface and reports the largest residual in
   units of the last printed digit. Curve outputs fit to about half a unit, so a misread
   digit stands out.

What the checks cannot see: a last-digit error of one unit that happens to fall inside
rounding. Two agreeing recognitions make that unlikely, not impossible, so a sample of grids
is also compared with the image by eye.
