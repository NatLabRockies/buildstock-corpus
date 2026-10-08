<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89042.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/89042.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/89042.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89042.md | section: 3.2.1.2  Data Processing and Converting Available Public Data to an EnergyPlus Compatible Format | lines: 384-490 -->
## 3.2.1.2  Data Processing and Converting Available Public Data to an EnergyPlus Compatible Format

This section describes each step of data processing, showing the conversion of publicly available performance data to EnergyPlus compatible performance maps. A new set of performance maps are generated as lookup tables in OpenStudio rather than biquadratic curves to avoid any potential overfitting issues.

Table 3 includes a list of new performance maps derived and applied in this study for modeling standard performance HP-RTUs, and the table also includes which actual products (and their data) in the current market are used to derive the performance maps. Note: This is not an exhaustive list of all required performance maps for modeling HP-RTUs in EnergyPlus. Rather, it is a down-selected list that can be outsourced from the publicly available data from manufacturers. Capacity-related performance maps are all derived from 5 to 25 different Carrier and Lennox products, and performance data for energy input ratio (EIR), which is an inverse of COP, are derived from 2 to 18 York and Lennox products. While the power data from Carrier included the exact total consumption of components (i.e., compressor and condenser fan) that is compatible with what EnergyPlus requires, the power data from Lennox only included compressor power. This has an implication of slight underprediction of power, which results in slight overprediction of COP (or underprediction of EIR that EnergyPlus wants) from data points from Lennox. The new EIR curves that include Lennox data, shown in Table 3, are affected by this limitation. To reflect rated COP changes depending on the size of the unit, regression fittings are performed on Carrier and Lennox products. More detailed findings are included in the following paragraphs.

Table 3. List of New Performance Maps for Standard Performance Modeling

<!-- table recovered from measure_pdfs/89042.pdf p.21
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     method: vision-transcription -->

**Capacity modifiers as a function of temperatures (maps 1-3)**

| Performance map count | Independent variable 1 | Independent variable 2 | Dependent variable | Derived from | Count of products used for derivation |
|---|---|---|---|---|---|
| 1 | Indoor air wet-bulb temperature | Outdoor air temperature | Capacity modifier for cooling in high stage | Average performance of Carrier WeatherMaker/WeatherMaster (3-25 tons), Lennox Xion (2-20 tons) | 25 |
| 2 | Indoor air wet-bulb temperature | Outdoor air temperature | Capacity modifier for cooling in low stage | Average performance of Carrier WeatherMaker/WeatherMaster (3-25 tons), Lennox Xion (15-20 tons) | 13 |
| 3 | Indoor air dry-bulb temperature | Outdoor air temperature | Capacity modifier for heating | Average performance of Carrier WeatherMaker/WeatherMaster (3-25 tons) | 15 |

**EIR as a function of temperatures (maps 4-6)**

| Performance map count | Independent variable 1 | Independent variable 2 | Dependent variable | Derived from | Count of products used for derivation |
|---|---|---|---|---|---|
| 4 | Indoor air wet-bulb temperature | Outdoor air temperature | EIR for cooling in high stage | Average performance of York Sun Core, Sun Pro, Sunline (3-20 tons), Lennox Xion (2-20 tons) | 18 |
| 5 | Indoor air wet-bulb temperature | Outdoor air temperature | EIR for cooling in low stage | Lennox Xion (15-20 tons) | 2 |
| 6 | Indoor air dry-bulb temperature | Outdoor air temperature | EIR for heating | Average performance of York Sun Core, Sun Pro, Sunline (3-20 tons) | 8 |

**Capacity modifiers as a function of flow fraction (maps 7-9)**

| Performance map count | Independent variable 1 | Independent variable 2 | Dependent variable | Derived from | Count of products used for derivation |
|---|---|---|---|---|---|
| 7 | Flow fraction | - | Capacity modifier for cooling in high stage | Average performance of Carrier WeatherMaker (7.5-25 tons), Lennox Xion (2-20 tons) | 16 |
| 8 | Flow fraction | - | Capacity modifier for cooling in low stage | Average performance of Carrier WeatherMaker (12.5-25 tons), Lennox Xion (15 tons) | 5 |
| 9 | Flow fraction | - | Capacity modifier for heating | Average performance of Carrier WeatherMaker (7.5-25 tons), Lennox Xion (2-20 tons) | 17 |

**EIR as a function of flow fraction (maps 10-12)**

| Performance map count | Independent variable 1 | Independent variable 2 | Dependent variable | Derived from | Count of products used for derivation |
|---|---|---|---|---|---|
| 10 | Flow fraction | - | EIR for cooling in high stage | Average performance of York Sun Core, Sun Pro, Sunline (3-20 tons), Lennox Xion (2-20 tons) | 18 |
| 11 | Flow fraction | - | EIR for cooling in low stage | Lennox Xion (15-20 tons) | 2 |
| 12 | Flow fraction | - | EIR for heating | Average performance of York Sun Core, Sun Pro, Sunline (3-20 tons), Lennox Xion (2-20 tons) | 18 |

**Rated COP as a function of rated capacity (maps 13-14)**

| Performance map count | Independent variable 1 | Independent variable 2 | Dependent variable | Derived from | Count of products used for derivation |
|---|---|---|---|---|---|
| 13 | Rated capacity | - | Rated COP for heating | Average performance of Carrier WeatherMaker/WeatherMaster (3-25 tons), Lennox Xion (2-20 tons) | 24 |
| 14 | Rated capacity | - | Rated COP for cooling | Average performance of Carrier WeatherMaker/WeatherMaster (3-25 tons), Lennox Xion (2-20 tons) | 24 |

Figure 3 and Figure 4 show the averaged or fitted results of cooling performance maps, which are also listed in Table 3. For capacity or EIR performances as a function of temperatures, performance maps are formatted as a lookup table in EnergyPlus, where two inputs (e.g., indoor wet-bulb air temperature and outdoor dry-bulb temperature for cooling) are used to derive (or interpolate) the output (i.e., normalized capacity or EIR modifier). The capacity modifier and EIR are calculated with this lookup table in each simulation time step depending on the operating conditions represented with the two inputs. Once the capacity modifier and EIR are found from the lookup table, they are multiplied to the rated capacity to reflect the performance of off-rated condition. These lookup tables are derived by normalizing and averaging the table of manufacturer spec sheets. For example, as shown in Table 3, the capacity modifier lookup table for high stage cooling is derived from 25 different products covering 2- to 25-ton units. As can be expected, cooling performances degrade (i.e., capacity decreases or EIR increases) with hotter outdoor temperatures.

Figure 3. Averaging/fitting results of new performance maps: cooling capacity

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000005_0f72e827af6af6dbcc3ee8697ba4d3ccd927f3bbe9aaccb7807e13015765e0ef.png
     method: vision-description
     described: 2026-08-22 -->

![Four-panel cooling capacity performance maps: temperature heatmaps and airflow-fraction fits](89042_images/image_000005_0f72e827af6af6dbcc3ee8697ba4d3ccd927f3bbe9aaccb7807e13015765e0ef.png)

Figure 3: four-panel plot of the new cooling capacity performance maps, high stage above low stage. The left panels are heatmaps of capacity modifier over outdoor dry-bulb (30 to 50 degrees C) and indoor wet-bulb temperature; the right panels scatter manufacturer data against airflow fraction with a linear fit. Modifiers span roughly 0.74 to 1.30. Table 3 lists the fitted curves.

Figure 4. Averaging/fitting results of new performance maps: cooling efficiency

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000006_c0314c05258b1a902139123879981353ba11eeb7c673782800740fe98f9f8406.png
     method: vision-description
     described: 2026-08-22 -->

![Cooling energy input ratio performance maps plus the rated cooling COP capacity regression](89042_images/image_000006_c0314c05258b1a902139123879981353ba11eeb7c673782800740fe98f9f8406.png)

Figure 4: five-panel plot of the new cooling efficiency maps. Heatmaps give the energy input ratio (1/COP) modifier over outdoor dry-bulb and indoor wet-bulb temperature for high and low stage, and scatter panels fit the modifier against airflow fraction. A bottom panel regresses rated cooling COP on rated capacity as 3.772 minus 0.01005 times kW, bounded 2.94 to 3.86. See Table 3.

Capacity and EIR performances as a function of airflow fraction are derived by fitting a regression model based on data available in the manufacturer spec sheets. Relevant data in Table 1 are used to gather sample points and to derive a linear regression model as shown in Figure 3 and Figure 4. The regression fitting results (based on the EnergyPlus' formulation requirement)

also show how capacity or EIR under off-rated conditions can vary between different products within the same manufacturer.

Figure 4 also includes the fitting result of the rated cooling COP as a function of rated capacity (in kW). While the bottom left pane includes the equation and coefficients of the regression model, the figure in the bottom right shows the fitting results. During measure application, the final rated cooling COP applied to the model is 1) first calculated with the rated cooling capacity by using the equation shown in the figure (and where the value is capped with minimum [2.98] and maximum [3.92] values based on data available from the manufacturer spec sheets) and then 2) the output value from the equation is adjusted again with the EIR modifier curve (function of flow fraction shown in top right pane of Figure 4) based on a reference cfm/ton (i.e., rated airflow divided by rated capacity) threshold. The second adjustment is to properly reflect the differences of cfm/ton between initial modeling inputs (determined by EnergyPlus sizing algorithm) versus actual products. The rated COPs in manufacturer spec sheets are based on specific rated conditions, especially a specific rated airflow, and the rated airflow that EnergyPlus determines via the sizing logic will not align perfectly with the cfm/ton value of actual products. Thus, the second adjustment is necessary to properly shift the reference point performance of actual products' rated COP to EnergyPlus-compatible rated COP. The reference cfm/ton values are determined, separately for heating and cooling, by averaging the values of all products that were used to derive rated COP regression equations.

Additionally, the 'rated' COPs (for both heating and cooling) used as inputs to EnergyPlus are based on rated conditions and only account for compressor power and outdoor fan power. The rated conditions of cooling are indoor wet-bulb temperature of 67 ° F/19.4 ° C and outdoor dry-bulb temperature of 95 ° F/35 ° C. The rated conditions of heating are indoor dry-bulb temperature of 70 ° F/21.1 ° C and outdoor dry-bulb temperature of 47 ° F/8.3 ° C. Rated COP values are first extracted from the manufacturers' performance sheets corresponding to these rated conditions and based on AHRI rating. However, because rated COPs based on AHRI rating include blower power and heat gain in the COP calculation, we have increased those COP values from spec sheets by 5% and 8.5% for heating and cooling, respectively, to reflect the calculation regarding the blower power and fan heat gain. The two values were derived from Lennox's spec sheets, which include blower performance tables for units in different sizes. Fan input power is calculated from the brake horsepower values shown in the table and the fan heat gain is calculated with rated airflow and the external static pressure defined by the rated operating conditions. The rated COP figure in Figure 4 is also including the 5% shift.

Figure 5 and Figure 6 show the averaged or fitted results of heating performance maps, which are also listed in Table 3. As mentioned previously, heating is modeled with a single-stage operation (i.e., all compressors running if there are multiple compressors), thus not requiring lower stage performance maps. While performance degradations (i.e., capacity decrease and EIR increase) are shown as expected in the lower outdoor air temperature region in the figure, the actual heating lockout temperature is set to 0°F (-18°C) in the simulations. The rated heating COP fitting results are also included in Figure 6 with minimum (3.46) and maximum (3.99) bounds.

Figure 5. Averaging/fitting results of new performance maps: heating capacity

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000007_fed5c5c757f8a0f2c2be3c63006a4aefaf52058bd6f7f919a2e4f72e3c135eb6.png
     method: vision-description
     described: 2026-08-22 -->

![Two-panel heating capacity performance map: temperature heatmap and airflow-fraction fit](89042_images/image_000007_fed5c5c757f8a0f2c2be3c63006a4aefaf52058bd6f7f919a2e4f72e3c135eb6.png)

Figure 5: two-panel plot of the new heating capacity performance map for all/single stage operation. The left heatmap gives the capacity modifier over outdoor dry-bulb temperature (-20 to 10 degrees C) and indoor dry-bulb temperature, falling to about 0.26 at the coldest condition; the right panel fits the modifier against airflow fraction. Table 3 lists the coefficients.

Figure 6. Averaging/fitting results of new performance maps: heating efficiency

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000008_486605afefa62cc52e4b0b8ea923513f4222370518156c28bea9c11b2246b9d6.png
     method: vision-description
     described: 2026-08-22 -->

![Heating energy input ratio performance maps plus the rated heating COP capacity regression](89042_images/image_000008_486605afefa62cc52e4b0b8ea923513f4222370518156c28bea9c11b2246b9d6.png)

Figure 6: three-panel plot of the new heating efficiency maps. A heatmap gives the energy input ratio (1/COP) modifier over outdoor and indoor dry-bulb temperature, rising to 7.47 at the coldest condition, and a scatter panel fits the modifier against airflow fraction. Rated heating COP is regressed on rated capacity as 3.958 minus 0.008502 times kW, bounded 3.46 to 3.99. See Table 3.

