<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/93846.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/93846.md | section: 4.3  Final Sensitivity Analysis | lines: 671-720 -->
## 4.3  Final Sensitivity Analysis

After further reviewing the real-world demand response programs and reviewing the initial sensitivity analysis results, we narrowed the analysis space. First, we narrowed the offset to only 2 -4°F, and then we limited the precooling windows to 1 hour and 4 hours. More details can be seen in Table 7.

In this round, we also introduced a random shift. This was used to reduce the 'snapback , ' or rebound, seen after the peak period when all thermostats reset to the normal set point at the same time. A maximum random shift of ± 30 minutes will make some buildings start their peak period up to 30 minutes early or up to 30 minutes late (i.e., the shift can be anything ranging from +30 minutes, to +15 minutes, to 0 minutes, to -15 minutes, to -30 minutes). This random shifting was assigned on a building-by-building basis, not on a per-event basis. In a real deployment, this staggering of individual homes could be accomplished through a combination of intentional control, inherent time delays, and equipment states found across the portfolio at any point in time.

Table 7. Test Run Specification for Final Sensitivity Analysis

|                    | Pre-Peak    | Pre-Peak    | On-Peak    | On-Peak     |
|--------------------|-------------|-------------|------------|-------------|
| Upgrade            | Duration    | Offset (°F) | Duration   | Offset (°F) |
| 1 (peak only)      | No pre-peak | N/A         | 4 hours    | 2           |
| 2 (pre-peak only)  | 4 hours     | 2           | No on-peak | N/A         |
| 3 (both)           | 4 hours     | 2           | 4 hours    | 2           |
| 4 (peak only)      | No pre-peak | N/A         | 4 hours    | 4           |
| 5 (pre-peak only)  | 4 hours     | 4           | No on-peak | N/A         |
| 6 (both)           | 4 hours     | 4           | 4 hours    | 4           |
| 7 (peak only)      | No pre-peak | N/A         | 4 hours    | 2           |
| 8 (pre-peak only)  | 1 hour      | 2           | No on-peak | N/A         |
| 9 (both)           | 1 hour      | 2           | 4 hours    | 2           |
| 10 (peak only)     | No pre-peak | N/A         | 4 hours    | 4           |
| 11 (pre-peak only) | 1 hour      | 4           | No on-peak | N/A         |
| 12 (both)          | 1 hour      | 4           | 4 hours    | 4           |

First, as shown in Figure 13, the impacts of precooling only are the lowest, followed by on-peak reduction, followed by the largest impacts when both precooling and the on-peak set point changes were applied on the same day. The anomalous behavior in West Virginia and South Dakota was not investigated for this test run, but it is believed to be a product of the small number of samples and the characteristics of the dwelling units in the test run. Figure 14 shows the same pattern but for heating. The anomalous behavior in California was not investigated for this test run, but it is believed to be a product of the relatively mild weather and the associated low absolute heating demands for most dwellings in the state.

Figure 13. D3 percentage reduction of the cooling energy consumption during the peak on the day of the year with the highest daily average temperature

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/93846.yaml
     source: 93846_images/image_000016_a50df4318adb1579dae25e91dee8489873e29d12106594e88fbce365042f5d6f.png
     method: vision-description
     described: 2026-11-11 -->

![Line chart of percent cooling reduction by state on the hottest day for five pre-peak and peak combinations](93846_images/image_000016_a50df4318adb1579dae25e91dee8489873e29d12106594e88fbce365042f5d6f.png)

Figure 13: line chart. X-axis is state, ordered by reduction; y-axis is percent reduction, about -10 to 80. Five series: peak only (4 hours, 4°F), pre-peak only for 1 hour and for 4 hours, and both for 1 hour and for 4 hours. Pre-peak only gives the least, mostly under 15%; peak only runs from about 50% down to about 15%; both together give the most, about 60% down to about 20%.

Figure 14. D3 percentage reduction of the heating energy consumption during the peak on the day of the year with the lowest daily average temperature

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/93846.yaml
     source: 93846_images/image_000017_05cb93c72021777f372119f5a582fda107b0e9b4adaf8974bf75f22ea6f5b5e0.png
     method: vision-description
     described: 2026-11-11 -->

![Line chart of percent heating reduction by state on the coldest day for five pre-peak and peak combinations](93846_images/image_000017_05cb93c72021777f372119f5a582fda107b0e9b4adaf8974bf75f22ea6f5b5e0.png)

Figure 14: line chart. X-axis is 24 states from NY to SC; y-axis is percent reduction, about -30 to 100. Five series: peak only (4 hours, 4°F), pre-peak only for 1 hour and for 4 hours, and both for 1 hour and for 4 hours. Reductions are near 100% in the first states and fall to about 40% to 50% for peak only; the pre-peak-only lines are lowest and most erratic, and several lines dip below zero for California.

Another notable result, though not shown in the figures, was a minimal difference between a pre-peak offset of 2°F and 4°F for pre-peak durations of 1 hour. This makes sense because the rate of the temperature increase possible in a home within 1 hour is limited by physical characteristics, such as the thermal mass of the dwelling and the capacity of the heating equipment.

