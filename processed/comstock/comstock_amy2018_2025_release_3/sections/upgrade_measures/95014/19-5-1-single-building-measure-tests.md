<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95014.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95014.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95014.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/95014.md | section: 5.1  Single Building Measure Tests | lines: 599-660 -->
## 5.1  Single Building Measure Tests

This section demonstrates the Condensing Gas Boiler measure application to a 300,000-ft 2 large office test model in Boise, Idaho. The building has a 'VAV chiller with gas boiler reheat' HVAC system. The measure replaced the model's central 80% efficient natural gas boiler with a condensing boiler with 95% nominal efficiency. The condensing boiler has an outdoor air reset, which allows the system to achieve optimal performance when outdoor air conditions are warm enough. In addition to the efficiency improvement, the boiler performance curve was also updated with data from a manufacturer. A summary of the energy use intensity (EUI), annual site energy, and heating site energy impacts are shown in Table 7.

Table 7. Energy Impacts of Condensing Boiler Measure Scenario for Single Building Example

|                                                     |   Baseline Scenario |   Condensing Boiler Measure Scenario | Percent Savings   |
|-----------------------------------------------------|---------------------|--------------------------------------|-------------------|
| EUI (kBtu per square foot)                          |                58.8 |                                 53.6 | 8.8%              |
| Annual site energy consumption (MMBtu)              |              17,636 |                               16,073 | 8.9%              |
| Natural gas heating site energy consumption (MMBtu) |               8,391 |                                6,828 | 18.6%             |

This 18.6% savings in heating site energy is consistent with what we'd expect for a 15% improvement in nominal boiler efficiency and new boiler performance curve. In addition, this measure implements supply temperature reset based on outdoor air, which allows the boiler to operate more efficiently during certain times of year. The annual site energy for this building was reduced by 9%, which should also result in similar utility bill savings because this measure does not involve fuel switching. The building's exact utility pricing structures would be required to calculate the change in annual utility bills.

Figure 8 shows the boiler efficiency (blue) and return water temperature (orange) during a week in January. The boiler's efficiency fluctuates between 88% and 93%, which is a result of the performance curve output multiplied by the nominal efficiency of 95% at each time step. The average boiler efficiency throughout the year for this building is 92%. As the return water temperature drops, the boiler achieves higher efficiencies, which demonstrates the effect of the supply temperature reset. Although this building showed an annual average boiler efficiency of 92% and site energy savings of 9%, the boiler efficiency, and thus the realized site energy savings of any specific building, will be highly dependent on the return water temperature profile.

Figure 8. Boiler efficiency and return water temperature (January 3-10)

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95014.yaml
     source: 95014_images/image_000010_dfc049a7bc3cda8e868718e21a173fd70d9db028961e17eaa23326e4f88ec5a7.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 8. Dual-axis time-series chart for the single-building example showing return water temperature in orange on the left axis and boiler efficiency in blue on the right axis over the week of January 3 to 10, with efficiency rising as return temperature falls](95014_images/image_000010_dfc049a7bc3cda8e868718e21a173fd70d9db028961e17eaa23326e4f88ec5a7.png)

Dual-axis time-series line chart titled Boiler Efficiency vs. Return Water Temperature - January 3-10, for the 300,000 square foot large office test model in Boise, Idaho. X-axis: timestamps from 1/3/18 00:00 to 1/10/18 00:00 with daily ticks. Left y-axis: Return Water Temperature (F), 0 to 180 in steps of 20; the orange Return Water Temperature trace oscillates on a daily cycle roughly between 115 F and 160 F, dipping lowest in the middle of each day. Right y-axis: Boiler Efficiency, 0.87 to 0.98 in 0.01 steps; the blue Boiler Efficiency trace runs between about 0.88 and 0.93 and is clearly anticorrelated with the orange trace, peaking near 0.92-0.93 when return water temperature bottoms out and falling to about 0.88-0.89 when return temperature is highest. Section 5.1 states the boiler's efficiency fluctuates between 88% and 93%, the performance-curve output multiplied by the 95% nominal efficiency at each time step, and that the annual average boiler efficiency for this building is 92%. The inverse relationship demonstrates the effect of the supply temperature reset, and the text cautions that realized site energy savings for any specific building depend heavily on its return water temperature profile.

Figure 9 shows the breakdown of energy consumption by month and end use before and after the condensing boiler measure scenario was applied. In the figure, the hashed bars represent natural gas end uses, whereas solid fill bars represent electricity. As can be seen, the natural gas heating load in the baseline is the main end use affected, with the highest savings seen in winter months, when heating dominates this building's load.

Figure 9. Single building example: monthly energy consumption by end use for baseline scenario (top) versus condensing boiler measure scenario (bottom)

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95014.yaml
     source: 95014_images/image_000011_f5439b5dec50b295588892b0e7b36da4cd8c1cd2cfbfe0e6ddd6539d732c1493.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 9. Two stacked monthly bar charts of single-building energy consumption by end use in kWh, baseline on top and condensing boiler measure scenario below, with the hatched red natural gas heating band shrinking in every month](95014_images/image_000011_f5439b5dec50b295588892b0e7b36da4cd8c1cd2cfbfe0e6ddd6539d732c1493.png)

Two stacked column charts for the Boise large office test model, one bar per calendar month January through December. Top panel: Monthly Energy Consumption by End Use - Baseline Building. Bottom panel: Monthly Energy Consumption by End Use - Condensing Boiler Measure Scenario. Both share a y-axis of Energy Consumption (kWh) from 0 to 700,000 in 100,000 steps. The legend lists, top to bottom, Water Systems, Heat Rejection, Pumps, Fans, Interior Equipment, Exterior Lighting, Interior Lighting, Cooling and Heating; per the caption, hatched colored bars indicate natural gas energy and solid colored bars indicate electricity, so the large red hatched band at the base of each winter bar is natural gas heating. Baseline monthly totals peak in December near 670,000 kWh and January near 645,000 kWh, fall to a summer floor near 300,000 kWh from June through September, and rise again in October and November. In the measure panel the same two months peak near 600,000 and 580,000 kWh. Every bar keeps the same solid electric bands, with cooling appearing only in the warmer months, and the only visibly changed component is the hatched natural gas heating band, which is exactly the Section 5.1 conclusion.

Hashed colored bars indicate natural gas energy, whereas solid colored bars indicate electricity.

Figure 11 shows the absolute and percent natural gas heating savings by month for this single building example. Although the majority of the heating savings (by magnitude) occur during the winter months, the summer months see higher percent savings in natural gas heating with the condensing boiler. This is because the high outdoor air temperatures (&gt;50°F) allow for lower return temperatures and higher boiler efficiency. So, even though the boiler is not operating as much during the shoulder and summer months, it is doing so more efficiently because of the outdoor air reset controls. Over the entire year, the natural gas heating is reduced by 18.6%.

Table 8. Natural Gas Heating Savings by Month for Single Building Example

|        |   Absolute Natural Gas Heating Savings (MMBtu) |   Percent Natural Gas Heating Savings (%) |
|--------|------------------------------------------------|-------------------------------------------|
| Jan.   |                                          218.9 |                                      14.0 |
| Feb.   |                                          182.9 |                                      16.9 |
| Mar.   |                                          193.9 |                                      19.3 |
| Apr.   |                                          133.8 |                                      23.7 |
| May    |                                           88.3 |                                      28.5 |
| Jun.   |                                           54.7 |                                      33.7 |
| Jul.   |                                           26.2 |                                      40.6 |
| Aug.   |                                           43.5 |                                      35.7 |
| Sep.   |                                           69.5 |                                      32.4 |
| Oct.   |                                          141.9 |                                      21.5 |
| Nov.   |                                          185.9 |                                      18.9 |
| Dec.   |                                          222.7 |                                      13.5 |
| Annual |                                         1562.3 |                                      18.6 |

