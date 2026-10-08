<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/98223.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/98223.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/98223.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/98223.md | section: where: | lines: 277-301 -->
## where:

- 𝑃𝑃 𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑 is design power consumption in watts (W), mapped with manufacturer data
- Q is design flow rate in cubic meters per second (m³/s), calculated from EnergyPlus sizing algorithm
- H is pump head in pascals (Pa, or N/m²), calculated from OpenStudio ®  Standards workflow
- 𝜂𝜂 𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝 is pump efficiency (decimal, e.g., 0.75), assumed a constant value
- 𝜂𝜂 𝑝𝑝𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚 is motor efficiency (decimal, e.g., 0.90), mapped with manufacturer data.

Since motor efficiency (which we are correlating with design power) is already accounted for in the equation, an iterative approach is adopted to estimate design power by leveraging the observed relationship between design power consumption and motor efficiency derived from published manufacturer data. Figure 5 illustrates this relationship using data from two manufacturer catalogs, covering pumps ranging from 0.46 hp to 50 hp, with corresponding motor efficiencies ranging from 89% to 96% [7], [8], all of which meet or exceed the IEC IE5 efficiency standard.

Figure 5. Regression fitting on manufacturer data: motor nominal efficiency

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98223.yaml
     source: 98223_images/image_000006_0441d304b3011c0496277650d87c4893fbb659bc8ad2f6d34ab363c9e8912367.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 5: scatter plot of pump motor nominal efficiency against nominal power with seven candidate regression curves overlaid and the selected piecewise equation printed in an inset box](98223_images/image_000006_0441d304b3011c0496277650d87c4893fbb659bc8ad2f6d34ab363c9e8912367.png)

Figure 5 of the ComStock Variable-Speed Pumps measure documentation. Manufacturer catalog points for pump motor efficiency are plotted with 'Motor Efficiency [%]' on the y axis spanning about 88 to 96 percent and 'Nominal Power [kW]' on the x axis spanning 0 to about 40 kW, and seven candidate fits are overlaid. The legend lists Poly deg 2, Poly deg 3, Logarithmic, Exponential, Logistic, Rational and 'Piecewise break at x=5', plus the Manufacturer data series - the seven regression models Section 3.2.1 says were evaluated. An inset box prints the selected fit: 'Piecewise breakpoint at x=5; if x < 5: y = 1.64645*ln(x) + 92.25876; else: y = 50.22495*(1 - exp(-0.00062*x)) + 94.75316; R2 = 0.63'. The two branches are continuous at the breakpoint, both giving 94.909 percent. The cloud of manufacturer points rises steeply below about 5 kW and then flattens, which is the behavior Section 3.2.1 cites as the reason for choosing the piecewise form over the logarithmic model. The lowest plotted point sits at roughly 88.5 percent efficiency near 0.4 kW and the highest at roughly 96.1 percent near 39 kW; the text describes the catalog range as 0.46 hp to 50 hp with efficiencies from 89 to 96 percent. No point carries a data label.

Seven regression models were evaluated, and a piecewise regression curve with a fixed breakpoint at 5 kW was selected for final implementation. This model best captures the steep increase in efficiency at lower power ratings and the gradual rise at higher ratings. While other models failed to reflect this nonlinear trend adequately, the logarithmic model captured the behavior well. However, it was ultimately unsuitable, as motor efficiency cannot be calculated for power inputs equal to or below 1 kW (e.g., log(1) = 0), limiting its applicability in the lower range.

2 Definitions of these terms can be found at https://bigladdersoftware.com/epx/docs/24-2/input-outputreference/group-pumps.html.

