<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95015.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95015.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95015.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/95015.md | section: 3  Modeling Approach | lines: 395-413 -->
## 3  Modeling Approach

This measure replaces existing natural gas and fuel oil boilers with electric resistance boilers. The implementation of this measure is rather simple-it converts the fuel type of existing boilers in the model from 'Natural Gas' or 'FuelOilNo2' to 'Electricity.' In addition, it modifies the nominal thermal efficiency from the original value (around 0.8 for natural gas boilers) to 1.0. The capacity, water flow rate, and all other settings of the boiler will remain the same as in the baseline.

Finally, the existing boiler efficiency performance curve is replaced. The new electric boiler curve is a linear function derived from the MASControl3 database maintained by the California Public Utilities Commission [7]. The new linear performance curve plots the electric input ratio (EIR) as a function of PLR using the following equation:

This equation is shown in Figure 3. As shown, the electric input ratio always exceeds 0.98, or 98% efficiency, and reaches 100% efficiency when operating at maximum capacity; therefore, this curve suggests minimal cycling efficiency losses for electric boilers.

Figure 3. Electric boiler performance curve

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95015.yaml
     source: 95015_images/image_000004_a03bb66e09376fe471aca0401be62ef1ccf6e654f98b855b56c78bd2292af712.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 3. Line plot of the electric boiler performance curve, showing electric input ratio rising linearly from about 0.98 at zero part load ratio to 1.00 at full load](95015_images/image_000004_a03bb66e09376fe471aca0401be62ef1ccf6e654f98b855b56c78bd2292af712.png)

Figure 3 is a single-line plot of the new electric boiler performance curve derived from the MASControl3 database. The x-axis is PLR (part load ratio) from 0 to 1 and the y-axis is EIR (electric input ratio) on a tight range from 0.9 to 1.1, with gridlines at 0.95, 1.00, and 1.05. The line is essentially straight, starting at an EIR of about 0.98 at PLR 0 and rising steadily to exactly 1.00 at PLR 1, with markers at each 0.1 increment. Because EIR never drops below about 0.98, the curve implies the electric boiler operates at 98% or better efficiency at any load and reaches 100% at maximum capacity -- that is, minimal cycling efficiency losses. The body text says this curve is given by an equation, but the equation itself was dropped in extraction; the plotted line is consistent with approximately EIR = 0.98 + 0.02 x PLR, which is an inference from the figure rather than a transcription of the source equation.

