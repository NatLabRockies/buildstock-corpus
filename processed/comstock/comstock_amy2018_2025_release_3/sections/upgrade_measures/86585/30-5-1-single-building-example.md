<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86585.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86585.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86585.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/86585.md | section: 5.1  Single Building Example | lines: 552-566 -->
## 5.1  Single Building Example

The operation behavior of a small office building in Chicago is described in this section. Figure 9. illustrates how the multispeed object functions. As the sensible load increases, either positive for heating load or negative for cooling load, the airflow rate generally increases. Speeds 1 through 4 are prevalent at different airflow bins. Speed 0 represents a time step where the part load ratio, and therefore the speed level, is below 1, meaning the unit is cycling. Cycling operation is subject to efficiency losses, per Figure 4. In general, the HP-RTU operates as expected.

Figure 9. Scatterplot of HP-RTU speed level, airflow rate, and predicted load

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86585.yaml
     source: 86585_images/image_000014_3e4e0fa5c54fb799c57e628badfcf2d0cf457ed0acf5f416623005e5d32cfcc8.png
     method: vision-description
     described: 2026-08-21 -->

![Scatterplot of supply air mass flow rate against predicted sensible load for a single Chicago small office, coloured by DX coil speed level, forming a V shape.](86585_images/image_000014_3e4e0fa5c54fb799c57e628badfcf2d0cf457ed0acf5f416623005e5d32cfcc8.png)

Scatterplot of one simulated building (a small office in Chicago) at time-step resolution. The x-axis is "Predicted Sensible Load (W)" running from about -5,800 to +8,500, where negative values are cooling load and positive values are heating load; the y-axis is "Supply Air Mass Flow Rate (kg/s)" running from about 0.25 to 0.65. Points are coloured by "Unitary System DX Coil Speed Level" with a legend listing 4 (blue), 3 (orange), 2 (green), 1 (red) and 0 (purple). The cloud forms a broad V: flow sits on a floor of 0.255 kg/s in a narrow band of near-zero load, occupied by speed 0 (cycling) and speed 1, then rises on both the cooling and heating sides through green speed 2 up to about 0.385 kg/s, orange speed 3 from 0.385 to about 0.51 kg/s, and blue speed 4 from 0.51 kg/s up to a saturated plateau at 0.64 kg/s that extends to the largest loads in both directions. The speed bands therefore sit at roughly 40%, 60%, 80% and 100% of design airflow, and the 0.255 kg/s floor is 39.8% of the 0.64 kg/s maximum, matching the 40% minimum supply airflow ratio stated in section 3.2.2.

