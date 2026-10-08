<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/98224.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/98224.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/98224.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/98224.md | section: 3.2.1.1  Rated Performance | lines: 248-320 -->
## 3.2.1.1  Rated Performance

Metrics reflecting the rated performance of RTUs sold in the United States are well documented in the AHRI certification directory [4]. We have extracted RTU data entries from the AHRI database and filtered the products based on the following criteria: (1) production status should be active and (2) must be sold in the United States. The final list of products used to extract average RTU performance included 2,847 products (or individual entries in the AHRI database) manufactured by 35 different manufacturers. Figure 3 to Figure 5 include snapshots of the data collected. As shown in Figure 3, products used for extracting rated performance range from 5-59 tons.

Figure 3. Distribution of rated cooling capacities from data used for modeling

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98224.yaml
     source: 98224_images/image_000004_ec866a72c4e0cac44f7bad96faaa6d980406493e4d137f08024045e866a14806.png
     method: vision-description
     described: 2026-08-22 -->

![Histogram of rated cooling capacities in the manufacturer data used for modeling](98224_images/image_000004_ec866a72c4e0cac44f7bad96faaa6d980406493e4d137f08024045e866a14806.png)

Figure 3: histogram of rated cooling capacity in tons across the manufacturer performance data used for modeling, count on the vertical axis and capacity from roughly 5 to 55 tons on the horizontal. The distribution is heavily weighted below 30 tons, clustering at common nominal sizes, and thins out above 40 tons. Section 3.2.1.1 describes the data set.

To capture the relationship between unit size and rated efficiency (EER and IEER), three capacity bins were defined (following bin categories used in ASHRAE 90.1-2016 [11]) to reflect the typical decline in efficiency as RTU size increases, as illustrated in Figure 4. The first bin covers rated capacities from 0 to 135 kBtu/h (11.3 tons), the second from 135 to 240 kBtu/h (20 tons), and the third includes units with capacities above 240 kBtu/h. As shown in Figure 4, the latest ASHRAE 90.1-2016 [11] standard applied in ComStock sets the minimum product efficiency requirements for each capacity bin, with the lowest flat points in each bin representing these minimum thresholds. In other words, this analysis includes (1) only products that meet or exceed current building energy codes and represent the highest-performing models currently available on the market and (2) products that manufacturers identify as 'high efficiency' as of July 31, 2025.

Figure 4. Rated EER/IEER against rated cooling capacity from data used for modeling

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98224.yaml
     source: 98224_images/image_000005_9484e45afbd80c2c3b218db2855e50d11fbe6b9be9e41b953dfc5b9ede6d8937.png
     method: vision-description
     described: 2026-08-22 -->

![Two scatter panels of rated EER and IEER against rated cooling capacity from manufacturer data](98224_images/image_000005_9484e45afbd80c2c3b218db2855e50d11fbe6b9be9e41b953dfc5b9ede6d8937.png)

Figure 4: two stacked scatter panels of rated EER above rated IEER, both against rated cooling capacity in Btu/hr, with dashed vertical lines marking the 135 kBtu/hr and 240 kBtu/hr breakpoints that bin units by size. Rated EER spans roughly 10 to 14 and IEER roughly 10 to 25, both trending down as capacity rises. See Section 3.2.1.1.

Figure 5 presents the final linear regression fits used to estimate the rated COP based on the rated capacity. The rated COP values in this figure are converted from the rated EER values shown in Figure 4, using the formula from the OpenStudio Standards, which accounts for condenser fan and excludes supply blower fan power from the rated EER. Regarding the measure execution sequence, the RTU model first undergoes the EnergyPlus sizing algorithm to determine its rated capacity. Then, based on this calculated rated capacity, the rated COP is computed and assigned using the linear equations depicted in Figure 5 (and in Figure 4); rated COPs generally decrease as rated capacity increases. Although there is noticeable variability among the data points compared to the linear regression lines, we have chosen to represent average rated COP performance using the three regression curves, one for each size category.

Figure 5. Linear regressions for estimating rated COP from rated capacity

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98224.yaml
     source: 98224_images/image_000006_fa7ee8888325efce13ea1dbe5fcc98e414781777704b81825fd33e57202efd18.png
     method: vision-description
     described: 2026-08-22 -->

![Scatter of rated COP against rated capacity with three piecewise linear regressions](98224_images/image_000006_fa7ee8888325efce13ea1dbe5fcc98e414781777704b81825fd33e57202efd18.png)

Figure 5: scatter of manufacturer rated cooling COP against rated capacity in watts, overlaid with three linear regressions, one per size bin split at 135 and 240 kBtu/hr. The fits are weak, with R-squared values of 0.0037, 0.0748 and 0.0014, and intercepts of 4.26, 4.24 and 3.68. Section 3.2.1.1 gives the resulting modeling assumptions.

One observation from this and previous research is that the rated COP values used (e.g., using Figure 5 based on rated capacity only) in EnergyPlus models often differ technically from those listed in manufacturer catalogs. This discrepancy arises because the term 'rated' is not always used consistently between real-world product documentation and EnergyPlus modeling conventions. For example, manufacturer catalogs typically define rated conditions using specific values-such as 67°F evaporator inlet wet-bulb, 95°F condenser inlet dry-bulb, and a productspecific rated airflow. While the temperature conditions are usually easy to align in EnergyPlus, the rated airflow is often overlooked. This is because EnergyPlus determines airflow based on its auto-sizing algorithms, which are designed to ensure the system can meet the cooling or heating loads of the modeled building. Referring to the values shown in Figure 5, the rated COPs based on manufacturer data are tied to these catalog-rated airflows. Therefore, when applying these COP values in our models, we must adjust them to reflect the airflow conditions generated by the EnergyPlus sizing routines rather than use the manufacturer's rated airflow directly.

To make this adjustment, we modify the rated COP based on the difference between the airflow sized by EnergyPlus and the reference airflow from product data. This is done by calculating the ratio of actual to reference airflow and then applying a performance curve-specifically, an EIR modifier curve that is a function of flow fraction (described in the following section)-to estimate how the airflow difference affects energy consumption. Once the adjustment factor is determined from the curve, it is applied to the rated COP derived from Figure 5. The adjusted COP better reflects the actual operating conditions in the building model, resulting in a more accurate simulation of system performance. Because the COP values in Figure 5 are based on real product data, we also fit a corresponding rated cubic feet per minute per ton (cfm/ton) (as shown in Figure 6) to estimate each product's rated airflow, which is then aligned with the rated capacity calculated by EnergyPlus.

Figure 6. Linear regressions for estimating rated cubic feet per minute per ton (cfm/ton) from rated capacity

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98224.yaml
     source: 98224_images/image_000007_9eac1dad66a2e9a6de7233d77b93a17db7eb702c154ca608aba4c4658bf660d9.png
     method: vision-description
     described: 2026-08-22 -->

![Scatter of rated cfm per ton against rated capacity with three piecewise linear regressions](98224_images/image_000007_9eac1dad66a2e9a6de7233d77b93a17db7eb702c154ca608aba4c4658bf660d9.png)

Figure 6: scatter of rated airflow in cfm per ton against rated capacity in watts, with three linear regressions fitted by size bin. Values center near 350 cfm/ton across the whole capacity range and the fits are weak, with R-squared values of 0.1562, 0.0001 and 0.0185. Section 3.2.1.1 explains how the regressions set modeled airflow.

For EnergyPlus modeling, inputs such as sensible heat ratio (SHR) and reference COP at reduced compressor speeds are necessary to accurately simulate lower-stage equipment performance. To derive these values, we filtered manufacturer performance data (from three different manufacturers and across 28 different products) at standard rated conditions-specifically, 67°F evaporator inlet wet-bulb temperature, 95°F condenser inlet dry-bulb temperature, and the corresponding rated airflow for each product. Based on this filtered dataset, we calculated the relative changes in SHR and COP for each stage of operation, as summarized in Table 1.

Table 1. Modeling Assumptions for Lower-Stage Sensible Heat and Reference COP Ratios

|                                     | Low Stage   | Middle Stage   | High Stage   |
|-------------------------------------|-------------|----------------|--------------|
| SHR (from data / actual simulation) | 0.81 / 0.7  | 0.74 / 0.64    | 0.73 / 0.63  |
| Reference COP ratio                 | 1.13        | 1.10           | 1 (rated)    |

As shown in Table 1 and based on manufacturer data representing high-efficiency RTUs-which includes two-stage (only for very small units), three-stage, and variable-speed systems, with three-stage systems being the most commonly available in public catalogs-we chose to model a variable-speed system in EnergyPlus using separate performance characteristics for each stage. EnergyPlus represents variable-speed systems through discrete stages, so to align with this modeling approach, we incorporated intermediate-stage performance data. While the manufacturer data include variable-speed systems, they also provide detailed performance information for many three-stage systems. We leverage this intermediate-stage data to effectively represent the performance of a variable-speed system within the EnergyPlus framework.

However, while extracting SHR values for each stage from the manufacturer's data, we noticed that the values did not initially align well with the EnergyPlus simulations. This discrepancy arose because the SHR values provided in the data went beyond the limits of those calculated by EnergyPlus using psychrometric principles. We suspect that this stems from differences in the humidity conditions of the inlet air entering the evaporator-specifically, between the conditions assumed in the manufacturer data (which is not specified) and those used by EnergyPlus during simulation. Since EnergyPlus generated frequent warnings with the original SHR values (listed as 'from data' in Table 1), leading to increased simulation time, we made an engineering decision to reduce the SHR values consistently across all three stages (as shown under 'actual simulation' in Table 1). We believe this adjustment has minimal impact on air property modeling, as it prevents throwing the air outlet properties beyond 100% relative humidity.

As shown in Table 1, the SHR (from data) increases at lower-speed stages (e.g., from 0.73 at high speed to 0.81 at low speed). This trend is expected because at lower compressor speeds, the evaporator coil operates at higher temperatures and the airflow often decreases, reducing the coil's ability to condense moisture from the air. As a result, latent cooling capacity drops more than sensible capacity, causing the SHR to rise.

Similarly, the reference COP increases at lower stages, with the low-speed COP reaching 1.13 times the rated high-speed COP. This improvement in efficiency is primarily due to lower compressor power draw, reduced fan power, and improved heat exchanger effectiveness at partload conditions. Since the system operates more efficiently under reduced load-with less energy input per unit of cooling delivered-the part-load COP surpasses the full-load rated COP.

