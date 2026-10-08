<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86585.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86585.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86585.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/86585.md | section: 3.2.4  Heat Pump Heating Performance | lines: 398-471 -->
## 3.2.4  Heat Pump Heating Performance

The variable-speed heat pump heating in the proposed HP-RTUs is modeled using the EnergyPlus 'Coil:Heating:DXMultiSpeed' object using four speeds of heating [4], [5]. This object performs similarly to the 'Coil:Cooling:DXMultiSpeed' object described previously. The rated efficiency values used for this study are based on a 10-ton variable-speed RTU with a fullload COP of 3.42 at rated conditions (8.3°C outdoor air temperature and 21.1°C drybulb indoor air temperature entering the coil) [9]. Because the indoor fan energy use is modeled in a separate object from the HP-RTU, the efficiency input is adjusted to 3.8 COP, using the methodology from PNNL's study [9]. The parameters for each stage of heating are shown in Table 2. The capacity and COP fractions for each speed level were determined using manufacturer-provided data for a variable-speed, central-ducted, forced-air heat pump system (Table 2). The data are roughly 10 years old but are expected to be a reasonable representation of a variable-speed system. The heating COP increases with lower speed levels, similar to what was described for the cooling COPs. Because the testing is based on residential central heat pump units rather than commercial RTUs, the values derived from the testing are normalized to the rated COP of 3.8 to better represent a commercially available HP-RTU for this study (Table 1) [9]. Variable-speed HP-RTUs are capable of modulating to the specified fractions, but they may not do so in the same manner as the residential units the performance parameters are based on, which emphasizes the need for additional research in this area [7]. The minimum operating temperature for the heat pumps is modeled at -17.8°C, which is the default setting for some manufacturers. The compressor will lock out below this temperature, and only backup heat will be available.

Table 2. Multispeed Heating Coil Performance Parameters

COP values are at rated conditions and vary based on temperature.

| Compressor Speed Level   |   Capacity Fraction of Rated |   COP Fraction of Rated |   Applied HP- RTU COP |
|--------------------------|------------------------------|-------------------------|-----------------------|
| Rated                    |                         1.00 |                    1.00 |                  3.80 |
| 4                        |                         1.00 |                    1.00 |                  3.80 |
| 3                        |                         0.85 |                    1.05 |                  3.98 |
| 2                        |                         0.48 |                    1.24 |                  4.71 |
| 1                        |                         0.28 |                    1.45 |                  5.51 |

Similar to the DX multispeed cooling objects, five performance curve modifier types are used for modeling the DX multispeed heating objects. The descriptions of these are discussed in the cooling performance section of this document, with the only difference being that the heating coils use indoor air drybulb temperature instead of indoor air wetbulb temperature, which is used for the cooling coils. The performance curves were derived from manufacturer-provided data for a central-ducted, variable-speed heat pump system. The resulting performance maps for all speed levels are shown in Figure 4, Figure 7, and Figure 8 for EIR as a function of part load ratio, COP, and capacity retention, respectively. As expected with heat pumps, heating COP and capacity generally decrease as outdoor air drybulb temperature decreases.

Heat pump performance maps are especially impactful because of the general reduction of capacity and efficiency at lower outdoor air temperatures where increased heating loads often occur. This study attempts to utilize the best available data, as described previously, because this will notably impact the results. However, it should be emphasized that complete heat pump performance data are still scarce at the time of this study, especially for variable-speed commercial RTUs and low-temperature operation, which limits the understanding of heat pump performance and operation in this analysis. Further research on heat pump performance could increase confidence in heat pump modeling, and this study may be updated as more data become available.

Comparisons of modeled performance data versus alternative data sources were made, where possible, to validate that the performance data used were reasonable. Table 3 and Table 4 compare some key points on the modeled heat pump performance maps for COP and capacity retention as a function of outdoor air temperature, respectively, with other available data sources for validation. The first data source is for the variable-speed Daikin Rebel HP-RTU, with specification sheet data providing capacity and COP at 8.3°C (rated) and -8.3°C [11]. The second source is a Rheem two-stage HP-RTU with heating performance data at various outdoor air temperatures [10]. The last data source is from a study that performed lab testing on a Carrier cold climate variable-speed HP-RTU, which provides COP values at various outdoor air temperatures [11].

The modeled HP-RTU outperforms the capacity retention of the reference units by 5% to 9%, with the largest difference occurring with the Rheem unit at -17.8°C (Table 3). For COP retention, the modeled HP-RTU outperforms the reference units by 3% to 14%, with the largest difference occurring with the Rheem unit at -17.8°C (Table 4). Although there are some notable differences between the modeled and reference unit performance, and the modeled HP-RTU outperforms the reference units in all cases, these comparisons still suggest the modeled HPRTU performance is reasonably appropriate compared to other available data, especially considering they are different units from different data sources. Note that no alternative data sources were found for comparing part-load performance or the impacts of cycling on variablespeed heat pump units, further emphasizing the need for more research in this space to increase modeling confidence.

Figure 7. COP as a function of temperature performance map for the four stages of heating. Note that these COP values are for the compressor only-adding in supply fan energy would decrease the values presented.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86585.yaml
     source: 86585_images/image_000011_b836a769e0357fb5368b56866aa94a23950a506bb2e604705b25ee9ca89e2018.png
     method: vision-description
     described: 2026-08-21 -->

![Four-panel contour map of heat pump heating COP as a function of outdoor and indoor drybulb temperature, one panel per compressor stage.](86585_images/image_000011_b836a769e0357fb5368b56866aa94a23950a506bb2e604705b25ee9ca89e2018.png)

Two-by-two grid of filled contour maps titled "COP Function of Indoor and Outdoor Drybulb Temperature: Stage 1" through "Stage 4". In every panel the x-axis is "Outdoor Air Drybulb Temperature (C)" from -17.8 to about 22.2 and the y-axis is "Indoor Air Drybulb Temperature (C)" from 15 to 30. Each panel carries a colour bar labelled "COP" spanning 0.0 to 7.4, blue through white to red, with ticks at 0.0, 1.1, 2.1, 3.2, 4.3, 5.3, 6.4 and 7.4. Inline contour labels are printed on every panel. Stages 2, 3 and 4 show smooth diagonal contours: COP rises with outdoor drybulb temperature and falls as indoor drybulb temperature rises (a larger lift), so the cold-outdoor, warm-indoor upper-left corner is the least efficient. Stage 4 spans roughly 2 to 5 COP across the plotted domain, Stage 3 slightly higher, and Stage 2 higher again, consistent with Table 2's rising COP fractions at lower compressor speeds. Stage 1 is not monotonic: it contains a closed maximum lobe above 7.4 COP centred near 12 C outdoor and 15-16 C indoor, with COP falling again above about 15 C outdoor. That closed peak is non-physical for heating and is consistent with extrapolation of the low-speed performance curves beyond their fitted range. No point value is asserted from this figure; use Table 4 for the modelled COP at reference temperatures.

Figure 8. Capacity as a function of temperature performance map for the four stages of heating. This value is multiplied by the nominal capacity for each time step to determine the actual available capacity for the time step.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86585.yaml
     source: 86585_images/image_000012_d10a810ea2bd700e99f1c512263be924eb9294547cda53b185445ed4c0a806c1.png
     method: vision-description
     described: 2026-08-21 -->

![Four-panel contour map of heat pump heating capacity modifier as a function of outdoor and indoor drybulb temperature, one panel per compressor stage.](86585_images/image_000012_d10a810ea2bd700e99f1c512263be924eb9294547cda53b185445ed4c0a806c1.png)

Two-by-two grid of filled contour maps titled "Capacity Function of Indoor and Outdoor Drybulb Temperature: Stage 1" through "Stage 4". In every panel the x-axis is "Outdoor Air Drybulb Temperature (C)" from -17.8 to about 22.2 and the y-axis is "Indoor Air Drybulb Temperature (C)" from 15 to 30. Each panel carries a colour bar labelled "Capacity Modifier" spanning 0.0 to 2.0 on a blue-white-red diverging scale, with ticks at 0.0, 0.2, 0.5, 0.8, 1.0, 1.2, 1.5, 1.8 and 2.0. The contour bands are close to vertical and only slightly tilted, so the modifier depends almost entirely on outdoor drybulb temperature and only weakly on indoor temperature, and it increases monotonically with outdoor temperature in all four stages - the expected heat pump behaviour. Stage 1 is much more strongly derated than the others: its printed contour labels run from about 0.2 near -15 C through 0.5 near -6 C and 0.9 near 5 C to 1.4 near 15 C. Stages 2, 3 and 4 are similar to one another and far flatter, with Stage 4 labelled about 0.6 near -16 C, 0.8 near -3 C, 1.0 near 8 C and 1.2 near 15 C. A pixel scan of the Stage 4 panel along the 21 C indoor line puts the 1.0 contour crossing at 8.56 C outdoor, matching Table 3's 8.3 C rated point. Use Table 3 for capacity fractions at reference temperatures.

Table 3. Capacity Retention As a Function of Outdoor Air Temperature Comparison for Daikin Rebel, Rheem Renaissance, and the Modeled HP-RTU Performance Curves

| Reference Temperature, °C                                      | 8.3°C   | - 8.3°C   | - 17.8°C   |
|----------------------------------------------------------------|---------|-----------|------------|
| Modeled HP-RTU Capacity Fraction                               | 1       | 0.64      | 0.45       |
| Daikin Rebel Capacity (kW)                                     | 30.8    | 18.0      | -          |
| Daikin Rebel Capacity Fraction                                 | 1       | 0.59      | -          |
| % Diff. Modeled HP-RTU vs. Daikin Capacity Fraction            | -       | 7.80%     | -          |
| Rheem Renaissance Capacity (kW)                                | 31.5    | 19.1      | 12.9       |
| Rheem Renaissance Capacity Fraction                            | 1       | 0.61      | 0.41       |
| % Diff. Modeled HP-RTU vs. Rheem Renaissance Capacity Fraction | -       | 5.47%     | 9.33%      |

Table 4. COP comparison of the modeled HP-RTU, the Daikin Rebel, and a lab-tested Carrier unit. Note that the COPs associated with the modeled HP-RTU and Rheem unit are compressor only while the other include the supply fan. Including the supply fan in the calculation will decrease the COP.

| Reference Temperature, °C                                | 8.3°C          | - 8.3°C        | - 17.8°C       |
|----------------------------------------------------------|----------------|----------------|----------------|
| Modeled HP-RTU COP (compressor only)                     | 3.80 (speed 4) | 2.66 (speed 4) | 2.11 (speed 4) |
| Modeled HP-RTU COP Fraction (compressor only)            | 1              | 0.70           | 0.55           |
| Daikin Rebel COP                                         | 3.42           | 2.38           | -              |
| Daikin Rebel COP Fraction                                | 1              | 0.70           | -              |
| % Diff Modeled vs. Daikin COP Fraction                   | -              | 0%             | -              |
| Carrier COP Estimate                                     | 3.1            | 2.1            | 1.62           |
| Carrier COP Fraction                                     | 1              | 0.68           | 0.52           |
| % Diff Modeled vs. Carrier COP Fraction                  | -              | 2.9%           | 5.5%           |
| Rheem Renaissance COP (compressor only)                  | 4.2            | 2.77           | 1.98           |
| Rheem Renaissance COP Fraction (compressor only)         | 1              | 0.66           | 0.47           |
| % Diff Modeled HP-RTU vs. Rheem Renaissance COP Fraction | -              | 5.8%           | 14.3%          |

