<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/87570.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/87570.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/87570.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/87570.md | section: 5.1  Single Building Example | lines: 398-433 -->
## 5.1  Single Building Example

In this section, we analyze the operation behavior of an example small office building in Gunnison, Colorado, with the HP-RTU measure applied. The model was simulated with both gas and electric supplemental heat to compare the differences.

Figure 3 compares the behavior of the two models for two winter days. In the upper plot, the heating rates of the heat pump (green line) and the supplemental heating coil (pink line) are displayed for both scenarios, illustrating a perfect overlap of these parameters, as anticipated. This alignment is due to the fact that the sole variable differing between the models is the fuel type of the supplemental heating coil. This change should not impact the required heating rates.

The lower plot shows the site's outdoor air temperature (blue line) alongside the site electricity use for the gas backup (yellow line) and electricity backup (dark green line) alternatives. Notably, the electricity usage diverges around the start of January 3, coinciding with the utilization of supplemental heating indicated in the upper plot. As anticipated, whenever supplemental heating is needed, the scenario employing electric supplemental heat exhibits higher electricity consumption.

In the specific example presented, a considerable peak in electric demand becomes evident for the electric backup option from 4 a.m. to 8 a.m. Meanwhile, the gas supplemental heating option shows a reduction in site electricity consumption during this time. This discrepancy stems from the outdoor temperature falling below the compressor lockout threshold of 0°F, resulting in zero heat pump heating output in both models (green line). To address this, the supplemental heating coils shoulder the entire heating load (pink line). In the electric option, electric resistance addresses the complete load, whereas the gas option uses a gas coil. As expected, the electric backup option reflects markedly higher site electricity consumption during this period, while the gas backup option shows a drop in site electricity during this same period because the model uses no electric heating below the compressor lockout temperature. Notably, the gas alternative would elevate gas consumption, a facet not illustrated in this plot.

Figure 3. Operation comparison of HP-RTU measure applied with gas vs. electric supplemental heating for an example small office model in Gunnison, Colorado. Note that the compressor lockout temperature is 0°F, below which the heat pump coils will not operate. Also note that the heating rates shown are for one of several RTUs in the building (top plot), whereas the site electricity is for the entire building (bottom plot).

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/87570.yaml
     source: 87570_images/image_000004_ac0bdb492f706e5c9cab7fc99ec954c26b591a3f4f0f79882d6ce32659550e9c.png
     method: vision-description
     described: 2026-08-20 -->

![Two-panel time-series comparing heat-pump and supplemental heating rates and site electricity for gas vs electric backup over two winter days](87570_images/image_000004_ac0bdb492f706e5c9cab7fc99ec954c26b591a3f4f0f79882d6ce32659550e9c.png)

Figure 3. Two-panel time-series comparing the HP-RTU measure with gas vs. electric supplemental heat for an example small office in Gunnison, Colorado, over two winter days (Jan 02-03). Top panel: heating rate (Btu/hr, 0 to about 21000) showing the heat pump heating rate (green) and the supplemental heating rate (pink); the electric-backup and gas-backup cases overlap exactly because only the supplemental fuel differs, not the required heating rate. Bottom panel: site outdoor air temperature (degrees F, left axis) plus whole-building site electricity (Wh, right axis to about 7500) for the electric-backup and gas-backup scenarios; site electricity spikes much higher under electric backup during the cold early-morning hours when supplemental resistance heat runs, while gas backup keeps electricity low. Illustrates that backup fuel choice does not change heating delivered but strongly changes electricity draw and peak demand.

Table 3 compares energy by end use for the HP-RTU measure applied with electric vs. gas supplemental heating for the example small office in Gunnison, Colorado. The gas backup option reduces the electric heating consumption from 72 (Gigajoules) GJ to 45 GJ. However, the gas backup option adds 34 GJ of gas heating compared to the electric backup option. Overall, the gas option uses more site energy than the electric option because the electric backup heating is 100% efficient at the site, whereas the gas backup option is 80% efficient at the site.

In conclusion, the electric backup option shows high electricity usage and demand, whereas the gas backup option shows higher total consumption of site energy and combustion fuels. Energy cost and greenhouse gas emissions are also considerations that were not discussed in this example. Therefore, deciding on the best-performing system would likely come down to balancing these factors, and others, with the priorities of the use case.

Table 3. End Use Comparison of the HP-RTU Measure Applied With Electric vs. Gas Backup Heating for an Example Small Office in Gunnison, Colorado

|   Electric |   Backup [GJ] | Gas Backup [GJ]   |
|------------|---------------|-------------------|
|          0 |            34 | Gas Heat          |
|         72 |            45 | Electric Heat     |
|          3 |             3 | Cooling           |
|         20 |            20 | Fans              |
|         77 |            77 | All Other         |
|        172 |           179 | Total             |

