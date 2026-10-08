<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/98224.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/98224.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/98224.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/98224.md | section: 3.2.1.2  Performance Under Various Operating Conditions | lines: 321-494 -->
## 3.2.1.2  Performance Under Various Operating Conditions

While rated capacities and efficiencies are commonly available from public resources, data on performance variation under off-rated operating conditions are relatively scarce. When such data exist, they often lack the detail needed to implement the performance in EnergyPlus or OpenStudio models. Additionally, this information is not well organized or documented in a format that others can easily download and process like the structured data available in the AHRI database.

To address this challenge, we conducted a comprehensive review of 15 catalogs featuring highefficiency (designated by manufacturers) RTUs from three major manufacturers to identify suitable performance map data [12]-[26]. Table 2 summarizes how fragmented information from each catalog was interpreted and translated into EnergyPlus-compatible performance curves.

Table 2. Mapping of Data Sources to RTU Performance Curves

<!-- table recovered from measure_pdfs/98224.pdf p.21
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98224.yaml
     method: vision-transcription -->

**From data source**

| Manufacturer | A | B | C |
|---|---|---|---|
| Rated capacities available? | Yes for some units | Yes | No |
| Rated power available? | Yes | No | No |
| Rated airflow available? | Yes for some units | Yes | No |
| Reference capacities (for lower stages) available? | No | No | No |
| Reference power (for lower stages) available? | No | No | No |
| Reference airflow (for lower stages) available? | No | No | No |
| Off-rated performances of highest stage cooling capacities available? | Yes | Yes | Yes |
| Off-rated performances of highest stage compressor power available? | Yes | No | No |
| Off-rated performances of lower stage cooling capacities available? | No | Yes | No |
| Off-rated performances of lower stage compressor power available? | No | No | No |

**To EnergyPlus: cooling capacity curves**

| Curve | Size | A: Low Stage | A: Med Stage | A: High Stage | B: Low Stage | B: Med Stage | B: High Stage | C: Low Stage | C: Med Stage | C: High Stage |
|---|---|---|---|---|---|---|---|---|---|---|
| Total Cooling Capacity Function of Temperature Curve derived from | Larger Units |  |  | O | Δ | Δ | O |  |  | Δ |
| Total Cooling Capacity Function of Temperature Curve derived from | Smaller Units | Δ | Δ | O | Δ | Δ | O |  |  |  |
| Total Cooling Capacity Function of Air Flow FractionCurve derived from | Larger Units |  |  | O | Δ | Δ | O |  |  | Δ |
| Total Cooling Capacity Function of Air Flow FractionCurve derived from | Smaller Units | Δ | Δ | O | Δ | Δ | O |  |  |  |

**To EnergyPlus: energy input ratio and part load fraction curves**

| Curve | Size | A: Low Stage | A: Med Stage | A: High Stage | B: Low Stage | B: Med Stage | B: High Stage | C: Low Stage | C: Med Stage | C: High Stage |
|---|---|---|---|---|---|---|---|---|---|---|
| Energy Input Ratio Function of Temperature Curve Name derived from | Larger Units |  |  | O |  |  |  |  |  |  |
| Energy Input Ratio Function of Temperature Curve Name derived from | Smaller Units | Δ | Δ | O |  |  |  |  |  |  |
| Energy Input Ratio Function of Air Flow Fraction Curve Name derived from | Larger Units |  |  | O |  |  |  |  |  |  |
| Energy Input Ratio Function of Air Flow Fraction Curve Name derived from | Smaller Units | Δ | Δ | O |  |  |  |  |  |  |
| Part Load Fraction Correlation Curve Name | Larger Units |  |  |  |  |  |  |  |  |  |
| Part Load Fraction Correlation Curve Name | Smaller Units | O | O | O |  |  |  |  |  |  |

* Circle means sufficient data, triangle means data available but insufficient for curve development, and blank means no data.

The 'From Data Source' section outlines the type of specific data required by EnergyPlus and whether that data were available from each manufacturer. For example, while Manufacturer A provided rated power data (including compressor and condenser fan power), similar information was not available in Manufacturer B's catalogs.

The 'To EnergyPlus' section illustrates which EnergyPlus performance curves were informed by public data from each source. For instance:

- Both Manufacturers A and B provide sufficient information to develop the capacity modifier (function of temperatures) curve for full-load operation (highest stage), particularly for larger units (shown with circle symbol).
- Manufacturer A did not include enough data to generate capacity modifier curves for lower-stage operation and for larger units (shown as blank).
- Manufacturer B offered data showing how capacity varies with temperature but lacked the reference capacity values needed to create normalized capacity modifier curves for lower-stage operation and for larger units (shown with triangle symbol).

EnergyPlus performance curves for modeling RTUs require normalizing actual capacity, power, and airflow. To do this, both rated values (at full-load operation) and reference values (at lower stages) are needed. While the absence of reference values for lower stages was expected, rated values were also occasionally missing, as shown in Table 2-particularly for these highefficiency products. These values were more commonly available for flagship or lower-tier models. As a result, certain assumptions were made during the normalization process-for example, estimating rated capacity based on the product's nameplate tonnage.

Among the reviewed data, only one manufacturer (Manufacturer A) provided performance maps for larger RTUs (25 to 150 tons) that included both capacity and power variations under varying indoor/outdoor temperatures and airflow rates, as shown in Table 2. In contrast, the other manufacturers reported only capacity variations, which are insufficient for deriving powerrelated (i.e., EIR) curves. Consequently, we developed normalized off-rated performance curves-focused on power consumption at the highest stage of operation-based on detailed maps from Manufacturer A.

Also, the larger, high-efficiency RTUs from Manufacturer A are variable-speed units equipped with three or four compressors and two refrigerant circuits. Their catalogs provide performance maps only for the highest stage of operation (i.e., no data for lower-stage performance). In contrast, EnergyPlus requires performance maps for intermediate stages to accurately simulate lower-stage performance in variable-speed systems.

As shown in Table 2, lower-stage capacity data for larger units are available only from Manufacturer B. A further challenge with these lower-stage data is the lack of 'reference' values for capacity, power, and airflow. As previously noted, EnergyPlus performance maps must be normalized, meaning that EnergyPlus determines the rated/reference capacity and airflow (via the sizing algorithm), and the normalized performance data are scaled accordingly based on these 'reference' values.

To estimate the reference capacity, power, and airflow values for lower-stage operation, we approximated the location of the reference condition within the performance map using parameters similar to those of the full-load rated condition. For instance, standard rated temperatures are 67°F for the evaporator inlet wet-bulb and 95°F for the condenser inlet drybulb. The remaining unknown-rated airflow-was not consistently available across all products, as shown in Table 2. However, when rated capacity became available (with approximation) but rated airflow was missing, we estimated airflow by interpolating within the available data. In other words, based on (1) the estimated position of the rated airflow within the airflow range of the highest-stage performance maps and (2) the consistent use of rated temperature conditions, we extracted the reference capacity and power values for the lower-stage performance maps.

When simulating system behavior in tools like EnergyPlus, data gaps across manufacturers often force engineers to stitch together performance curves using fragmented information. Since no single source provides comprehensive data covering all operating conditions-full-load and partload capacities, compressor power, airflow dependencies, and temperature sensitivities-we must combine partial datasets like a patchwork quilt. This approach is not ideal, but it is often the only option for capturing any semblance of real-world operation in these behaviors.

Based on engineering judgment using the available data, Figure 7 to Figure 11 present the performance assumptions applied in this simulation study. The key highlights from these figures are summarized below:

- Figure 7 to Figure 11: The existing/old curves are sourced from OpenStudio Standards ASHRAE 90.1-2019 data, representing some of the better performance levels typically found in existing buildings.
- Figure 7 to Figure 11: With the exception of very small units ( ≤ 5 tons), products with multistage data included up to three stages. Accordingly, we applied engineering judgment to model variable-speed units using performance data distinguished across three stages.
- Example of an operating COP determination based on performance maps shown:
- o If rated COP = 4.2 (small unit shown in Figure 5) and
- o EIR = 0.5 (small unit, lower stage, and colder temperature in Figure 10), then
- o off-rated COP  = 4.2 / 0.5 = 8.4.
- Figure 7 and Figure 8: Off-rated performance of high-efficiency RTUs (based on airflow) is similar to reference/existing curves.
- Figure 9 and Figure 10: Off-rated performance of high-efficiency RTUs (based on temperature) is slightly better than reference/existing curves.
- Figure 11: Part-load performance of high-efficiency RTUs is better than reference/existing curves. But we still use the new curves in Figure 11.
- Overall: High-efficiency RTUs generally perform better.
- Key drivers of benefits: The modeled benefits of high-efficiency RTUs primarily stem from (1) higher rated efficiency, (2) reduced cycling with variable-speed systems, and (3) improved performance under off-rated operating conditions.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98224.yaml
     source: 98224_images/image_000008_d30096ed3cdcf4fb02621fcd5543095e64236a7a7328976d92060a8e863aaa3d.png
     method: vision-description
     described: 2026-08-22 -->

![Capacity modifier versus evaporator airflow curves for small and medium units, three operation stages](98224_images/image_000008_d30096ed3cdcf4fb02621fcd5543095e64236a7a7328976d92060a8e863aaa3d.png)

Figure 7, small and medium unit blocks: six-panel grid of cooling capacity modifier against normalized evaporator airflow, columns running from highest to lowest operation stage and rows for small and medium unit sizes. Each panel plots manufacturer data, the new fitted quadratic with its equation and R-squared, and the existing/old curve. Table 2 maps data sources to curves.

Figure 7. Performance curves used in the study: capacity modifier function of fraction of airflow

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98224.yaml
     source: 98224_images/image_000009_b070d272838cf72eca1ea4012fbd8ed872e84a4ad4db14c4d7a9000708bb61bb.png
     method: vision-description
     described: 2026-08-22 -->

![Capacity modifier versus evaporator airflow curves for large units, three operation stages](98224_images/image_000009_b070d272838cf72eca1ea4012fbd8ed872e84a4ad4db14c4d7a9000708bb61bb.png)

Figure 7, large unit block: the continuation of the grid, three panels of cooling capacity modifier against normalized evaporator airflow for large units at high, medium and low operation stage. The fits are strong here, with R-squared of 0.89, 0.96 and 0.99, and the new curves fall below the old curve at high airflow fractions. See Table 2.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98224.yaml
     source: 98224_images/image_000010_4637ec562ca7c97d240ec659f19d0341ca7346a39011c42eddb8ae1e0964dd10.png
     method: vision-description
     described: 2026-08-22 -->

![EIR modifier versus evaporator airflow curves for small and medium units, three operation stages](98224_images/image_000010_4637ec562ca7c97d240ec659f19d0341ca7346a39011c42eddb8ae1e0964dd10.png)

Figure 8, small and medium unit blocks: six-panel grid of cooling energy input ratio modifier against normalized evaporator airflow, columns from highest to lowest operation stage and rows for small and medium unit sizes. Each panel shows manufacturer data, the new fitted quadratic with equation and R-squared, and the existing/old curve. Table 2 maps data sources to curves.

Figure 8. Performance curves used in the study: EIR modifier function of fraction of airflow

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98224.yaml
     source: 98224_images/image_000011_6bfa4ea67f7f22c1136a1f1bdbeaa9af623c1a79b0de61200fa0d4eed944bb8e.png
     method: vision-description
     described: 2026-08-22 -->

![EIR modifier versus evaporator airflow curve for large units, with two stages lacking data](98224_images/image_000011_6bfa4ea67f7f22c1136a1f1bdbeaa9af623c1a79b0de61200fa0d4eed944bb8e.png)

Figure 8, large unit block: the continuation of the grid for large units. Only the highest operation stage has a fitted curve, quadratic with R-squared 0.90; the medium and low stage cells are placeholders reading no data available for curve development, use curve on the left. Section 3.2.1.2 explains the fallback. See Table 2.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98224.yaml
     source: 98224_images/image_000012_9b281bf93c4460ce118fdd9b5dfafc1713edb752f3ef19cb503f71453a77f254.png
     method: vision-description
     described: 2026-08-22 -->

![Capacity modifier versus condenser inlet temperature for small and medium units, new and old maps](98224_images/image_000012_9b281bf93c4460ce118fdd9b5dfafc1713edb752f3ef19cb503f71453a77f254.png)

Figure 9, small and medium unit blocks: six-panel grid of cooling capacity modifier against condenser inlet dry-bulb temperature in degrees C, columns from highest to lowest operation stage and rows for small and medium units. Each panel shades the band between evaporator wet-bulb 25.0 and 13.9 degrees C for the new map against the same band for the old map. See Table 2.

Figure 9. Performance curves used in the study: capacity modifiers function of fraction of temperatures

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98224.yaml
     source: 98224_images/image_000013_4ae3e2e6da5769a5cf1ad7ca37b6e94ccd9cca0913ef7fbc483a3668485a298c.png
     method: vision-description
     described: 2026-08-22 -->

![Capacity modifier versus condenser inlet temperature for large units, new and old maps](98224_images/image_000013_4ae3e2e6da5769a5cf1ad7ca37b6e94ccd9cca0913ef7fbc483a3668485a298c.png)

Figure 9, large unit block: three panels of cooling capacity modifier against condenser inlet dry-bulb temperature for large units at high, medium and low operation stage, again shading the new map's evaporator wet-bulb band against the old map's. The medium and low stage panels use wet-bulb bounds of 24.4 and 14.4 degrees C rather than 25.0 and 13.9. See Table 2.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98224.yaml
     source: 98224_images/image_000014_e55d4444229a7a38a3879a04a2fdb925e4e82fc1c4d2a09773faf0d6934c136e.png
     method: vision-description
     described: 2026-08-22 -->

![EIR modifier versus condenser inlet temperature for small and medium units, new and old maps](98224_images/image_000014_e55d4444229a7a38a3879a04a2fdb925e4e82fc1c4d2a09773faf0d6934c136e.png)

Figure 10, small and medium unit blocks: six-panel grid of cooling energy input ratio modifier against condenser inlet dry-bulb temperature in degrees C, columns from highest to lowest operation stage and rows for small and medium units, shading the new map's evaporator wet-bulb band against the old map's. Modifiers rise steeply with condenser temperature. See Table 2.

Figure 10. Performance curves used in the study: EIR modifiers function of fraction of temperatures

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98224.yaml
     source: 98224_images/image_000015_a46e43d55cb76ed4fda46968297bc904c1419164172a84a3b2bb725c53cef546.png
     method: vision-description
     described: 2026-08-22 -->

![EIR modifier versus condenser inlet temperature for large units, with two stages lacking data](98224_images/image_000015_a46e43d55cb76ed4fda46968297bc904c1419164172a84a3b2bb725c53cef546.png)

Figure 10, large unit block: the continuation for large units, where only the highest operation stage has a lookup table. The medium and low stage cells are placeholders reading no data available for lookup table development, using map on the left. Section 3.2.1.2 explains the fallback. See Table 2.

Figure 11. Performance curves used in the study: Power modifier function of part-load ratio

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98224.yaml
     source: 98224_images/image_000016_fbf71ee436d5181deb56cfc9c97a57edbefec382413e7cf0c500b912d8126134.png
     method: vision-description
     described: 2026-08-22 -->

![Normalized power versus part-load ratio curves for small and medium units, large lacking data](98224_images/image_000016_fbf71ee436d5181deb56cfc9c97a57edbefec382413e7cf0c500b912d8126134.png)

Figure 11: three stacked panels of normalized power against part-load ratio by unit size. Small units fit 0.911407x plus 0.097728 with R-squared 0.943 and medium units 0.947828x plus 0.068913 with R-squared 0.993; the large-unit panel reads no data available for curve development, use the curve above. Both new curves sit well below the old curve. See Table 2.

