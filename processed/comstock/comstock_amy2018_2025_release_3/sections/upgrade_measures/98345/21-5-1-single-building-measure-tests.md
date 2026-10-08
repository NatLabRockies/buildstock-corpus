<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/98345.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/98345.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/98345.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/98345.md | section: 5.1  Single-Building Measure Tests | lines: 392-444 -->
## 5.1  Single-Building Measure Tests

In this section, we describe the operation of a hospital in Hattiesburg, Mississippi, climate zone 3A, to demonstrate the measure scenario application on a single building. The baseline model uses VAV systems with central hot water and chilled water coils and terminals with hot water reheat. Chilled water is supplied by an air-cooled chiller, and heating hot water is supplied by a natural-gas-fired boiler.

The building is served by two air-handling units, each with one supply fan. One of the two supply fans (SF-1) operates at or below 40% of design airflow for almost 75% of the year, and the other fan (SF-2) operates at or below that threshold for 86% of the year. Figure 4 shows the distribution of fan airflow fraction for SF-1.

Figure 4. Distribution of fan airflow fraction over 15-minute time steps of year for SF-1

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98345.yaml
     source: 98345_images/image_000005_85f5b906e7b92a9f9c831bf942d1e12fe6f9b6cf73ca8c4e7f86ef172cefacf8.png
     method: vision-description
     described: 2026-08-21 -->

![Histogram of fan airflow fraction across the 15-minute time steps of a year for supply fan SF-1, strongly concentrated in the lowest bin.](98345_images/image_000005_85f5b906e7b92a9f9c831bf942d1e12fe6f9b6cf73ca8c4e7f86ef172cefacf8.png)

Figure 4. Histogram of fan airflow fraction over the 15-minute time steps of the year for supply fan SF-1 of the single example building, a hospital in Hattiesburg, Mississippi, climate zone 3A. Airflow fraction is on the horizontal axis and a count of time steps on the vertical. Nine bins about 0.033 wide span roughly 0.333 to 0.630. The distribution is strongly right-skewed: the first bin holds about 21,256 time steps, then about 4,905, 3,119, 2,230, 1,470, 1,200, 783, 440 and 96 in the highest bin. The nine bins sum to about 35,500, consistent with the 35,040 15-minute steps in a year, and the first two bins together hold about 26,161 steps, or roughly 75% of the year, matching Section 5.1's statement that SF-1 operates at or below 40% of design airflow for almost 75% of the year. The bin range also matches the 0.33 to 0.66 span of the SF-1 markers in Figure 6. Because SF-1's fan spends most of the year at low airflow ratio, the reset curve's much lower power fraction at low flow applies for most operating hours, which is why the modeled fan energy savings for this building reach 59.2%.

The fan power reduction follows the expected trend based on the reset curve. At an airflow fraction of 40%, the fraction of design power is reduced from about 40% under the baseline curve for these models in ComStock, to 12% under the 'good' SP reset curve. As a result of the substantial fraction of the year with the fan operating at low loads, implementation of the SP reset in this model results in a large reduction in fan energy use. Figure 5 shows total buildinglevel fan power draw under the baseline and with the SP reset and, as a reference, calculated fan power draw based on a fixed 40% airflow fraction under the two cases. The SP reset results in a 59% reduction in building-level fan energy use. Figure 6 shows power fraction as a function of flow fraction for SF-1 in the base and SP reset cases, superimposed on the modeled fan curves for the two cases. Table 4 summarizes energy savings by relevant end uses for this building.

Table 4. Summary of Energy Savings by End Use

| End Use/Fuel Type       |   Baseline |   SP Reset |   Absolute Savings | Percentage Savings (%)   |
|-------------------------|------------|------------|--------------------|--------------------------|
| Heating (therms)        |     16,634 |     17,487 |               -853 | -5.1%                    |
| Cooling (electric, kWh) |    650,278 |    593,889 |             56,389 | 8.7%                     |
| Fans (electric, kWh)    |    246,806 |    100,611 |            146,195 | 59.2%                    |

Figure 5. Total fan power draw for SP reset and baseline

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98345.yaml
     source: 98345_images/image_000006_8a6ba69e9a980985d648f56932b97efec9508e5247eb969c04e015023a2dbb94.png
     method: vision-description
     described: 2026-08-21 -->

![Annual time series of building-level fan power draw for the baseline and SP reset cases, with two dashed reference lines giving fan power at 40% airflow under each curve.](98345_images/image_000006_8a6ba69e9a980985d648f56932b97efec9508e5247eb969c04e015023a2dbb94.png)

Figure 5. Total building-level fan power draw for the SF-1 example building over the 15-minute time steps of a year, baseline versus SP reset. The horizontal axis runs from 0 to about 35,000 time steps and the vertical axis is fan power in kilowatts. Two dense bands of points are plotted. The baseline band sits mostly between about 28 and 31 kW, with a floor near 14 kW and one excursion to roughly 50 kW near time step 23,000 to 24,000. The SP reset band sits far lower, mostly between about 7 and 10 kW. Two dashed reference lines mark calculated power at a fixed 40% airflow fraction, per the note below the figure: a red line at about 31.0 kW for the baseline fan curve and a black line at about 9.7 kW for the reset curve. Their ratio is about 0.31, consistent with Figure 2's 0.137 over 0.476 at 40% airflow and with the roughly 30% quoted in Section 5.6. The separation between the two bands is the graphical form of Table 4's 59.2% reduction in fan electricity for this building, from 246,806 to 100,611 kWh.

Red dashed line shows fan power at 40% airflow under the baseline fan curve. Black dashed line shows fan power at 40% airflow under the reset curve.

Figure 6. Power fraction as a function of airflow fraction for SF-1 for base and SP reset cases and modeled fan curves

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98345.yaml
     source: 98345_images/image_000007_99889466c4e0cf26d07e33b0dd9da199ae5063356959189f9c3f5afe03858305.png
     method: vision-description
     described: 2026-08-21 -->

![Scatter of observed airflow fraction against power fraction for fan SF-1 in the baseline and SP reset cases, overlaid on the two modeled fan curves, which converge at full flow.](98345_images/image_000007_99889466c4e0cf26d07e33b0dd9da199ae5063356959189f9c3f5afe03858305.png)

Figure 6. Power fraction as a function of airflow fraction for supply fan SF-1, baseline and SP reset cases, with the modeled fan curves superimposed. Airflow fraction is on the horizontal axis and power fraction on the vertical, both spanning 0 to 1. Two solid curves rise from their zero-flow intercepts to meet exactly at the point 1.0, 1.0: the upper orange curve is the baseline multizone VAV with discharge dampers curve, intercepting near 0.19, and the lower blue curve is the SP reset curve, intercepting near 0.05. Plotted markers are pairs of observed flow fraction and power for SF-1 in the model and lie along their respective curves. The markers span airflow fraction about 0.33 to 0.66, the same range as the histogram bins of Figure 4, with baseline power fraction from about 0.34 to 0.62 and reset power fraction from about 0.07 to 0.36. The convergence at full flow is the point made in Section 3.2: the reset saves nothing at design airflow and progressively more as airflow falls. Note that these intercepts differ from the corresponding series in Figure 2, about 0.229 and 0.064, for what should be the same two curves.

Plotted points represent pairs of observed flow fraction and power for SF-1 in the model, and solid lines represent the modeled fan curves.

