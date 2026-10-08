<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86103.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/86103.md | section: Creating New Performance Maps for Outdoor Units | lines: 467-556 -->
## Creating New Performance Maps for Outdoor Units

Figure 9 and Figure 10 show heating and cooling performance, respectively, for two VRF manufacturers' outdoor units in terms of available capacity and COPcomp&amp;fan,design [26], [27]. In these figures, capacity 'modifier' represents a ratio rather than actual capacity that is multiplied to the rated capacity defined in the model under varying conditions (e.g., indoor dry-bulb and outdoor wet-bulb temperatures), and COPcomp&amp;fan,design calculation is based on accounting compressor and outdoor unit fan powers at design conditions. These products represent 2023 technology in the market including application in cold climates where the heat pump can operate down to -22 o F (-30 o C) outdoor air temperature (wet-bulb). To note, these performances represent standard conditions such as 100% combination ratio (i.e., outdoor unit capacity matches with the sum of indoor unit capacity) and without degradation due to longer piping length and height. As shown in Figure 9, these products maintain constant heating capacity down to a low outdoor air temperature and still achieve a COPcomp&amp;fan,design higher than one-i.e., higher efficiency than 100% efficient electric resistance heating-in the lower temperature region.

Figure 9. VRF outdoor unit performance comparisons: heating capacity and COPcomp&amp;fan,design

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000015_01bb7afc017e8808dacdaba9eebbd227860a2750ffda19d89edcde8ed29344ee.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 9: VRF outdoor unit heating capacity modifier and design COP for two manufacturers](86103_images/image_000015_01bb7afc017e8808dacdaba9eebbd227860a2750ffda19d89edcde8ed29344ee.png)

Figure 9: two line panels comparing two manufacturers' VRF outdoor units in heating against outdoor wet-bulb temperature (-35 to 10 deg C) - (a) capacity modifier, (b) COPcomp&fan,design - with Daikin RELQ72T and Mitsubishi PURY-HP72TNY/YNU series at several indoor dry-bulb temperatures. Capacity modifier plateaus near 1.2-1.3 above -15 deg C and falls to about 0.6 at -30 deg C. See Table 3.

Figure 10. VRF outdoor unit performance comparisons: cooling capacity and COPcomp&amp;fan,design

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000016_25a633a3d3ecc320e195e80a9f93620d0eb20f7c52abda541f542941a2e6a0a7.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 10: VRF outdoor unit cooling capacity modifier and design COP for two manufacturers](86103_images/image_000016_25a633a3d3ecc320e195e80a9f93620d0eb20f7c52abda541f542941a2e6a0a7.png)

Figure 10: two line panels comparing the same two VRF outdoor units in cooling against outdoor dry-bulb temperature (0-40 deg C) - (a) capacity modifier, (b) COPcomp&fan,design - with Daikin RELQ72T and Mitsubishi PURY-HP72TNY/YNU series at indoor wet-bulb temperatures of 16-24 deg C. Cooling COP falls steadily with outdoor temperature, from roughly 11 near 0 deg C to about 4 at 40 deg C. See Table 3.

Another modification we made during the testing phase is on the EIR (function of part-load ratio) curve for cooling used in the EnergyPlus VRF object. The performance-available capacity and COP, mainly-of VRF in EnergyPlus when using the older VRF object heavily depends on the combined effect of many things. For example, the power used by the compressor and outdoor unit fan is calculated in every simulation timestep with six different terms: rated capacity, rated COP, capacity modifier function of temperatures, EIR modifier function of temperatures, EIR modifier function of part-load ratio, and runtime fraction. If  all these curves are not created consistently with each other, the output (e.g., compressor and outdoor unit fan power) of the model can easily be inaccurate. After making updates (to reflect the latest technology) to curves shown in Figure 9 and Figure 10, we also noticed the operating COP of VRF system is sensitive on the EIR (function of part load ratio) curve. To provide a more common context, Figure 11 shows the cooling EIR and COPcomp&amp;fan,design applied in this work and compares this against the existing curves. The EIR curve is only used in actual simulations, and two changes-discussed below-were made in the new curve.

Figure 11. Cooling EIR (or COP) curve derivation and validation

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000017_ce86be988483907d4e3b3ca8fc6ff326a2d9390228423d908db1ef3acb4b951d.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 11: cooling EIR and COP multipliers versus part-load ratio for three curve sets](86103_images/image_000017_ce86be988483907d4e3b3ca8fc6ff326a2d9390228423d908db1ef3acb4b951d.png)

Figure 11: two panels plotting cooling part-load performance against part-load ratio (0.15-0.95) - (a) EIR multiplier, (b) COPcomp&fan,design multiplier - comparing the EnergyPlus IDF example curve, Daikin's original curve, and the new curve adopted here. The EIR multiplier rises from about 0.3 at low part load to 1.0 at full load; the COP multiplier falls from roughly 3.5-5 to 1.0. See Table 3.

Note that EIR is the function of part-load ratio.

One of the two changes is to reflect the part-load performance of VRF based on the manufacturer's data sheet [28]. The approach-using COPcomp&amp;fan,design variation against varying combination ratio-described in [29] is used for extracting/estimating COPcomp&amp;fan,design in partload conditions. Because the manufacturer data sheet only includes combination ratio (in this case equivalent to part-load ratio) down to 0.7, a slight shift was applied to the new curve where the difference against existing curves is reflected between part-load ratio of 0.7 and 1 in Figure 11. The second change, which is more of a guess due to limited evidence data, is on the EIR/COP when part-load ratio is very low. As shown in Figure 11, two existing curves' COP multipliers differ between 3 and 5 at part-load ratio of 0.25. This means if the Daikin curve is used and when the VRF system is at a part-load ratio of 0.25, five times more than the rated COP is applied as the system performance. It was difficult to find relevant references to decide on what is more realistic, thus, we have made an engineering judgement to reflect the performance in between two existing curves as shown in Figure 11 for the lower part-load ratio region. The heating EIR (function of part load ratio) curve did not show concerns as much as the cooling curve, thus, existing Daikin curve was used for all simulations.

While several performance data were newly created as described above, the older EnergyPlus VRF object requires significantly more curves for fully implementing all inputs required for VRF modeling: combination ratio correction (for both heating and cooling), part-load fraction correction (for both heating and cooling), piping correction factor, and EIR modifier for defrosting. Many of these other curves cannot be derived from publicly available data sheets. Thus, we decided to combine two sources into one complete performance curves set.

Table 3 shows the source of all curves required for the older VRF object; 'Source 1' represents the Daikin product shown in Figure 9 and Figure 10, 'Source 2' represents the Daikin product shown in Table 2, 'Unused' curves are unnecessary inputs for the single curve approach mentioned earlier, and 'New' mainly reflects the new cooling EIR curve shown in Figure 11. The main idea for this merging is to reflect 2023 capacity and COPcomp&amp;fan,design (inverse of EIR) performance while filling missing data with existing information. The only reason for selecting one of the two manufacturers shown in Figure 9 and Figure 10 is to capture the capacity variance depending on indoor conditions. Curves from Source 1 are all implemented with a lookup table (with two independent variables) object in EnergyPlus instead of a biquadratic equation because we noticed limitations, such as overfitting, in biquadratic curve fitting results during this exercise.

Table 3. Configuration of All Curves Used in VRF Object

<!-- table recovered from measure_pdfs/86103.pdf p.31
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     method: vision-transcription -->

**Cooling curves**

| Group | Curve Name | Source 1 | Source 2 | Unused | New |
|---|---|---|---|---|---|
| Cooling curves | Cooling Capacity Ratio Modifier Function of Low Temperature Curve Name | √ |  |  |  |
| Cooling curves | Cooling Capacity Ratio Boundary Curve Name |  |  | √ |  |
| Cooling curves | Cooling Capacity Ratio Modifier Function of High Temperature Curve |  |  | √ |  |
| Cooling curves | Cooling Energy Input Ratio Modifier Function of Low Temperature Curve Name | √ |  |  |  |
| Cooling curves | Cooling Energy Input Ratio Boundary Curve Name |  |  | √ |  |
| Cooling curves | Cooling Energy Input Ratio Modifier Function of High Temperature Curve Name |  |  | √ |  |
| Cooling curves | Cooling Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name |  |  |  | √ |
| Cooling curves | Cooling Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name |  |  | √ |  |
| Cooling curves | Cooling Combination Ratio Correction Factor Curve Name |  | √ |  |  |
| Cooling curves | Cooling Part-Load Fraction Correlation Curve Name |  | √ |  |  |

**Heating curves**

| Group | Curve Name | Source 1 | Source 2 | Unused | New |
|---|---|---|---|---|---|
| Heating curves | Heating Capacity Ratio Modifier Function of Low Temperature Curve Name | √ |  |  |  |
| Heating curves | Heating Capacity Ratio Boundary Curve Name |  |  | √ |  |
| Heating curves | Heating Capacity Ratio Modifier Function of High Temperature Curve |  |  | √ |  |
| Heating curves | Heating Energy Input Ratio Modifier Function of Low Temperature Curve Name | √ |  |  |  |
| Heating curves | Heating Energy Input Ratio Boundary Curve Name |  |  | √ |  |
| Heating curves | Heating Energy Input Ratio Modifier Function of High Temperature Curve Name |  |  | √ |  |
| Heating curves | Heating Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name |  | √ |  |  |
| Heating curves | Heating Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name |  |  | √ |  |
| Heating curves | Heating Combination Ratio Correction Factor Curve Name |  | √ |  |  |
| Heating curves | Heating Part-Load Fraction Correlation Curve Name |  | √ |  |  |

**Other**

| Group | Curve Name | Source 1 | Source 2 | Unused | New |
|---|---|---|---|---|---|
| Other | Piping Correction Factor for Length in Cooling Mode Curve Name |  | √ |  |  |
| Other | Defrost Energy Input Ratio Modifier Function of Temperature Curve Name |  | √ |  |  |

