<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95002.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95002.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95002.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/95002.md | section: 5.1  Single-Building Measure Tests | lines: 424-574 -->
## 5.1  Single-Building Measure Tests

This section reviews the application of the Reduced Thermostat Setbacks for Heat Pumps measure to two models in different climate zones to demonstrate the functionality of the measure. The HP-RTU with reduced setbacks measure was applied to two retail buildings with packaged single-zone RTUs in two different locations (Cody, Wyoming, in climate zone 6B and Phoenix, Arizonia, in climate zone 2B). In both cases, the measure was applied to implement a 2°F thermostat setback.

In the Wyoming location, with cold outdoor air temperatures during the winter, supplemental heating power draw is substantial but is lower in magnitude during the warm-up period with the reduced setbacks, as shown for the heating 'peak week' (the week of the lowest hourly outdoor air temperature) in Figure 2 (a and b). The lowest hourly outdoor air temperature during the simulation is -24.2°F and occurs the week of January 29. The reduction in setback reduces the overall supplemental heating peak for the year (which occurs during this week, in both cases) by about 13% and shifts the time when the peak occurs. At the time when the lowest temperature of the year occurs, the reduced setbacks lower the contemporaneous supplemental heating power draw, which is the daily peak, by about 45%. Additionally, the reduced setbacks reduce the peak supplemental heating power draw by a similar fraction on several other days during the peak week.

Figure 2. (a) Supplemental heating power, during the heating 'peak week,' with original (8°F) and reduced (2°F) unoccupied setbacks, Cody, Wyoming. (b) The same results for a subset of the heating peak week.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95002.yaml
     source: 95002_images/image_000004_3b35d73c648e77b471a3be77859dd49989cc91605b00392ef7e0559a7a363f20.png
     method: vision-description
     described: 2026-08-21 -->

![Two-panel time series of heat pump backup heating power with original vs reduced setbacks, Cody WY](95002_images/image_000004_3b35d73c648e77b471a3be77859dd49989cc91605b00392ef7e0559a7a363f20.png)

Figure 2: two stacked time-series panels for the Cody, Wyoming model. Left y-axis Power (kW) 0-160, right axis outdoor air temperature (deg F). Series: heat pump backup heating power with reduced setbacks (blue), with original setbacks (dashed orange), and outdoor air temperature (dashed green). Panel (a) spans the heating peak week Jan 29-Feb 5; (b) zooms to Feb 1-3. Peaks reach roughly 150 kW under both schemes but at different times.

As expected, the reduction in setbacks also changes the time when high supplemental heating power draw occurs. In the case with the reduced setbacks, peaks in supplemental heating power draw tend to occur in the evening, around 6 p.m. This is explained by the reduction in internal loads at that time, increasing the heating load, while the heating setpoint remains close to the occupied value. In the case with standard setbacks, peak supplemental heating power draw tends to occur around 6 a.m., when the setpoint returns to the occupied value for the day.

To illustrate the effects of the setback on supplemental heating power draw, Figure 3 (a and b) shows supplemental heating power draw along with heating setpoint and outdoor air temperature for the same week, for the cases with the original and modified setbacks, respectively. At the beginning of the week, outdoor air temperatures are comparatively moderate. On January 30, the low temperature is just below 20°F. On that day, the reduced setbacks lowered the peak supplemental heating power draw by about 75%. The compressor lockout temperature is configured for 0°F. Supplemental heating is required during morning warm-up with the standard setbacks because the compressor's heating capacity is insufficient to meet the large load to bring the spaces from unoccupied to occupied setpoints. This is largely mitigated with the reduced setbacks.

Figure 3. (a) Supplemental heating power, with setpoints and outdoor air temperatures, without setback modification, Cody, Wyoming, for the heating 'peak week.' (b) Supplemental heating power, with setpoints and outdoor air temperatures, with setback modification, Cody, Wyoming, during the heating 'peak week.'

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95002.yaml
     source: 95002_images/image_000005_ca8b2c7a4dbd50723762d9c95dfd93aa5930fadebf843946c42eaf7f66bb198a.png
     method: vision-description
     described: 2026-08-21 -->

![Two-panel time series of backup heating power with heating setpoint and outdoor air temperature, Cody WY](95002_images/image_000005_ca8b2c7a4dbd50723762d9c95dfd93aa5930fadebf843946c42eaf7f66bb198a.png)

Figure 3: two time-series panels for the Cody, Wyoming heating peak week (Jan 29-Feb 5). Left y-axis Power (kW) 0-160, right axis Temperature (deg F). Series: heat pump backup heating power (blue), outdoor air temperature (dashed green), and heating setpoint (dashed orange, right axis). Panel (a) is the original setbacks, whose setpoint shows a nightly sawtooth; (b) is the reduced setbacks, flatter. Backup peaks approach 130 kW in both.

However, the effect of the reduced setbacks on overall building peak demand is more complex. Figure 4a shows whole-building level power demand for the heating peak week for the cases with standard setbacks and the setback reduction. The reduction in setbacks shifts the supplemental heating peak, and the overall building-level peak power demand for the week, from the morning of February 3 rd to the evening of February 1 st . The net reduction in peak power demand for the week is only 3%, compared to the 13% reduction in peak supplemental heating power draw. This disparity is explained by the fact that the supplemental heating peak now coincides with a time when lighting loads are significantly higher, resulting in a smaller reduction in the overall peak than in the supplemental heating peak. Figure 4b shows a comparison of daily energy use (total and for heating only) under the scenarios with standard and reduced setbacks. The differences in total energy consumption for the two scenarios are attributable to the differences in heating energy use. The reduced setbacks scenario results in higher heating energy use due to the longer periods of operation of the heat pump at higher setpoint values.  Over the period from February 2 nd to February 4 th , the proportionate increase in overall daily building energy use with the reduced setbacks is relatively small, between 3.9% and 7.5%. (These annual energy use increase associated with the reduced setbacks is 4.6%. It is expected that days during the heating 'peak week' would see increases in energy use higher than this value.) On February 1 st , the reduced setbacks result in an increase in building energy use of 30.8%. This corresponds with a day of low temperatures, and a peak in backup heating power draw under the reduced setbacks scenario.

Figure 4. (a) Total building-level demand, with and without the setback reduction, for the heating 'peak week.' (b) Daily energy consumption (total and for heating only) for the two scenarios.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95002.yaml
     source: 95002_images/image_000006_0c76ebd95de266e009e29567adb82a3b14cbf5d0b0e35cc2a0a1a68aed28bb44.png
     method: vision-description
     described: 2026-08-21 -->

![Two panels: whole-building demand time series, and daily total and heating energy for the two setback cases](95002_images/image_000006_0c76ebd95de266e009e29567adb82a3b14cbf5d0b0e35cc2a0a1a68aed28bb44.png)

Figure 4: two panels for the Cody, Wyoming model. (a) Line chart of whole-building demand, y-axis Power (kW) 0-180, Feb 1-5, comparing reduced setbacks (blue) and original setbacks (dashed orange); peaks reach roughly 180 kW and 170 kW respectively. (b) Grouped bar chart, y-axis Energy consumption (kWh) 0-1750+, for Feb 1-4, with total and heating-only series under reduced and standard setbacks. Reduced setbacks raise both.

Figure 5a shows compressor heating power draw for the cases with and without the setback reduction during the heating peak week. During this week, the magnitudes of the peaks in compressor power draw are similar for the two cases, but their timing is different. Cumulatively over the year, compressor heating energy use is 28% higher in the case with reduced setbacks than in the case with standard setbacks. This reflects the greater number of hours of heating operation in the case with reduced setbacks, since the heat pump is now operating to meet a higher setpoint during unoccupied periods. During the heating peak week, outdoor air temperatures remain below 0°F (the compressor lockout temperature) for February 1 through February 3, and there is thus no compressor heating operation during that period. The greater number of hours of compressor heating operation is illustrated in Figure 5b for a winter week with milder conditions.

Figure 5. (a) Compressor heating power with original setbacks and with reduced setbacks, Cody, Wyoming, for the heating 'peak week.' (b) Compressor heating power with original setbacks and with reduced setbacks, Cody, Wyoming, for a week with milder outdoor air temperatures.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95002.yaml
     source: 95002_images/image_000007_c3aa8cb85ca7ad795e0e23be9f493644cda76ddeb2f5722b386f1ce3e782583e.png
     method: vision-description
     described: 2026-08-21 -->

![Two-panel time series of heat pump compressor heating power, reduced vs original setbacks, Cody WY](95002_images/image_000007_c3aa8cb85ca7ad795e0e23be9f493644cda76ddeb2f5722b386f1ce3e782583e.png)

Figure 5: two time-series panels of heat pump compressor heating power for Cody, Wyoming, with reduced setbacks (dashed orange) and original setbacks (blue). Panel (a) covers the heating peak week Jan 29-Feb 5 on a y-axis of 0-40 kW, with output at zero Feb 1-3 while outdoor air sits below the 0 deg F lockout. Panel (b) covers a milder week (Jan 8-15) on 0-17 kW and adds outdoor air temperature.

Figure 6 shows distributions of compressor heating power draw (for time steps when compressor heating power draw is nonzero) for the cases with standard and reduced setbacks. Figure 7 shows distributions of supplemental heating power draw for the two cases, for time steps when supplemental heating power draw is non-negligible, and less than 100 kW. (Note that there are a small number of time steps with higher supplemental heating power draw). The cumulative sums of supplemental heating power energy use between the two cases are almost identical.

Figure 6. Distributions of compressor heating power draw for the cases with original and reduced heating setbacks, Cody, Wyoming

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95002.yaml
     source: 95002_images/image_000008_f7a6a06bf2009c6646963e7dbd0bbaa0d93bfb9fd153aded247cf638c05f31dc.png
     method: vision-description
     described: 2026-08-21 -->

![Histogram of compressor heating power draw hours per year, original vs reduced setbacks, Cody WY](95002_images/image_000008_f7a6a06bf2009c6646963e7dbd0bbaa0d93bfb9fd153aded247cf638c05f31dc.png)

Figure 6: overlaid histogram, x-axis Compressor heating power draw (kW) 0-40, y-axis Hours per year 0-1400, with Reduced Setbacks (blue) and Original Setbacks (orange) bars. Both distributions are dominated by the lowest bin at roughly 1350 hours and then decay; the reduced-setback case holds more hours across the 2-15 kW range, reflecting more hours of compressor heating operation.

Figure 7. Distributions of supplemental heating power draw for the cases with original and reduced heating setbacks, Cody, Wyoming

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95002.yaml
     source: 95002_images/image_000009_e42779a3db54df3caa09320cd5392d1f1a6f7da5a280bfe4364aad30787ad307.png
     method: vision-description
     described: 2026-08-21 -->

![Histogram of supplemental heating power draw hours per year, original vs reduced setbacks, Cody WY](95002_images/image_000009_e42779a3db54df3caa09320cd5392d1f1a6f7da5a280bfe4364aad30787ad307.png)

Figure 7: overlaid histogram, x-axis Supplemental heating power draw (kW) 0-100, y-axis Hours per year 0-250, with Reduced Setbacks (blue) and Original Setbacks (orange) bars. The lowest bin dominates at about 245 hours reduced versus 215 original, both tails thin out above 40 kW, and the original-setback case holds more hours in the 5-40 kW band.

Figure 8 and Table 4 show monthly peak demand for the two scenarios (with and without setback reduction) for the Cody, Wyoming building, and the monthly percent reduction in peak demand through the reduced setbacks. The reduced setbacks lower monthly peak demand during most of the simulated year (and by over 20% in October, November, and March). The reduction in setbacks causes a negligible increase (less than 1%) in monthly peak demand in June through September. Table 4 also shows a comparison of overall electricity use between the two scenarios. The setback reduction results in an overall 4.6% penalty (increase) in electricity use in this location, due to the longer operating hours at high heating setpoints.

Figure 8. Building-level peak demand by month for cases with standard (std.) and reduced (red.) setbacks, Cody, Wyoming

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95002.yaml
     source: 95002_images/image_000010_4042358f5997764499bd3a15e0332435a37c42722f9e7a8bfb9e82f56c656f1d.png
     method: vision-description
     described: 2026-08-21 -->

![Grouped bar chart of monthly building-level peak demand, standard vs reduced setbacks, Cody WY](95002_images/image_000010_4042358f5997764499bd3a15e0332435a37c42722f9e7a8bfb9e82f56c656f1d.png)

Figure 8: grouped bar chart, x-axis calendar months January through December, y-axis Demand (kW) 0-175, with Std. Setback (blue) and Red. Setback (orange) bars for the Cody, Wyoming model. Winter is highest, with January and February near 170-175 kW. Reduced setbacks lower peak demand in most months, most visibly October, November, and March. See Table 4 for monthly values and percent reductions.

Table 4. Monthly Peak Demand Comparison for Cody, Wyoming, Model With and Without Heating Setback Reduction

| Month                       | Standard Setbacks   | Reduced Setbacks   | Reduction (%)   |
|-----------------------------|---------------------|--------------------|-----------------|
|                             | Peak Demand (kW)    | Peak Demand (kW)   | Reduction (%)   |
| Jan                         | 173                 | 142                | 18%             |
| Feb                         | 178                 | 173                | 2.7%            |
| Mar                         | 96.9                | 68.5               | 29%             |
| Apr                         | 55.2                | 54.2               | 1.8%            |
| May                         | 51.0                | 49.4               | 3.1%            |
| Jun                         | 49.4                | 49.7               | -0.6%           |
| Jul                         | 60.7                | 61.2               | -0.9%           |
| Aug                         | 58.3                | 58.6               | -0.5%           |
| Sep                         | 46.5                | 46.6               | -0.3%           |
| Oct                         | 98.4                | 73.1               | 26%             |
| Nov                         | 123                 | 95.0               | 23%             |
| Dec                         | 139                 | 114                | 18%             |
| Total electricity use (kWh) | 243,377             | 254,628            | -4.6%           |

Figure 9 shows the effects of the setpoint adjustment for the Phoenix model for the heating 'peak week' with lowest outdoor air temperature (36°F). Application of the measure successfully reduces the setback from the 8°F unoccupied setback originally in the 'baseline' model to 2°F.

In this warm climate, the effects of the setback modification on heating power draw by both the heat pump compressors and supplemental heating coils are minimal. Figure 10 shows the compressor and supplemental heating power draw for application of the measure without setback modification, for the Phoenix location, along with outdoor air temperature, for the same week. As shown in Figure 10, supplemental heating power draw in this warm climate is small. The power drawn by the supplemental heating coil and heat pump compressor with the setback adjustment is almost identical and is not shown on the plot for clarity. For most hours in the year, the outdoor air temperature in this location is above 50°F, virtually eliminating the need for supplemental heating. This measure is being applied in all climate zones, but the impacts from it in cooling-dominated climates such as Phoenix are expected to be minimal. Confirming this, Figure 11 shows peak demand by month with and without the setback reduction in the retail building in Phoenix. The values with and without the setback reduction are almost identical.

Figure 9. Implementation of 2°F unoccupied setbacks through measure application compared to baseline model for Phoenix, during week of coldest outdoor air temperature

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95002.yaml
     source: 95002_images/image_000011_b4bd8a50f9072e1ebbd2dca323cbc4e1f44c18dcaeacd0c4933dd390c99e0a92.png
     method: vision-description
     described: 2026-08-21 -->

![Time series of baseline vs measure heating setpoint for Phoenix during the coldest week](95002_images/image_000011_b4bd8a50f9072e1ebbd2dca323cbc4e1f44c18dcaeacd0c4933dd390c99e0a92.png)

Figure 9: time-series line chart, y-axis Temperature (deg F) 58-68, x-axis Jan 8-15, the Phoenix week with the coldest outdoor air temperature. Two series: Htg Setpoint-Baseline (solid orange), dropping nightly to about 59 deg F, and Htg Setpoint-Measure (dashed blue), dropping only to about 65 deg F. The measure narrows the unoccupied setback from 8 deg F to 2 deg F.

Figure 10. Heat pump compressor and supplemental heating power, with original setbacks approach, during week of coldest outdoor air temperature, Phoenix

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95002.yaml
     source: 95002_images/image_000012_49245cd1695e16af579107187eb2db2525e7611d7162550c471630b2c321df57.png
     method: vision-description
     described: 2026-08-21 -->

![Time series of heat pump compressor and backup heating power with outdoor air temperature, Phoenix](95002_images/image_000012_49245cd1695e16af579107187eb2db2525e7611d7162550c471630b2c321df57.png)

Figure 10: time-series chart for the Phoenix model under the original setbacks approach, Jan 8-15. Left y-axis Power (kW) 0-35, right axis Temperature (deg F) 35-65. Series: heat pump compressor heating power (blue), backup heating power (orange, flat at zero), and outdoor air temperature (green). Compressor power spikes to 25-35 kW during each morning warm-up; supplemental heat is never called.

Figure 11. Building-level peak demand by month for cases with and without setback reductions, Phoenix

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95002.yaml
     source: 95002_images/image_000013_aed2e7ec8c02262b3e30399dc98401649b1184d4b7d0fa1608463ae1a8ff27c5.png
     method: vision-description
     described: 2026-08-21 -->

![Grouped bar chart of monthly building-level peak demand with and without setback reduction, Phoenix](95002_images/image_000013_aed2e7ec8c02262b3e30399dc98401649b1184d4b7d0fa1608463ae1a8ff27c5.png)

Figure 11: grouped bar chart, x-axis months January through December, y-axis Demand (kW) 0-250, with Std. Setback (blue) and Red. Setback (orange) bars for the Phoenix model. Peaks are cooling-driven, rising from about 80-95 kW in winter to roughly 220-235 kW in June through August. The two setback cases are nearly identical in every month.

