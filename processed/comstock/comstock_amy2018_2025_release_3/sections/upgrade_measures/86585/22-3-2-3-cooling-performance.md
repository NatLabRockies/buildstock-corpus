<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86585.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86585.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86585.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/86585.md | section: 3.2.3  Cooling Performance | lines: 335-397 -->
## 3.2.3  Cooling Performance

The variable-speed direct expansion (DX) cooling system in the proposed HP-RTUs is modeled using the EnergyPlus 'Coil:Cooling:DXMultiSpeed' object using four speeds of cooling [4], [5]. The highest speed (speed 4) represents the cooling performance at rated conditions with the compressor fully loaded. The efficiency values used for this study are based on a 10-ton variablespeed RTU with a full-load COP of 3.6 at rated conditions (35°C outdoor drybulb temperature and 26.7°C/19.4°C indoor drybulb/wetbulb temperature) with an integrated energy efficiency ratio above 17 [9]. Because the indoor fan energy use is modeled in a separate object from the HP-RTU, the efficiency input is adjusted to 4.11 COP using the methodology from the Pacific Northwest National Laboratory's (PNNL's) Daikin Rebel study [9].

The other speed levels (speeds 1 through 3) represent lower compressor speeds, which would occur when the required load to be met is less than the full capacity of the unit. Each speed corresponds to a fraction of the rated capacity, rated COP, and rated airflow. Lower compressor speeds generally show higher COP values, which allow for higher efficiencies during these periods of partial loading. For instance, a PNNL lab testing and modeling study showed 20%50% annual cooling energy savings for variable-speed RTUs over conventional RTU cooling systems [9]. The capacity fractions and COPs for the different compressor speeds were determined using NREL lab testing data for three variable-speed, central-ducted air-conditioning (AC) systems. Because the testing is based on residential central AC units rather than commercial RTUs, the values derived from the testing are normalized to the rated COP of 4.11 to better represent a commercially available HP-RTU for this study (Table 1) [9]. Variable-speed HP-RTUs are capable of modulating to the specified fractions, but they may not do so in the same manner as the residential units the performance parameters are based on [7].

Table 1. Multispeed Cooling Coil Performance Parameters

Units with high outdoor air fraction may not achieve lower compressor speeds if it violates ventilation requirements.

| Compressor Speed Level   |   Capacity Fraction of Rated |   COP Fraction of Rated |   Applied HP-RTU COP |   Sensible Heat Ratio Fraction |
|--------------------------|------------------------------|-------------------------|----------------------|--------------------------------|
| Rated                    |                         1.00 |                    1.00 |                 4.11 |                           1.00 |
| 4                        |                         1.00 |                    1.00 |                 4.11 |                           1.00 |
| 3                        |                         0.67 |                    1.08 |                 4.44 |                           1.01 |
| 2                        |                         0.51 |                    1.11 |                 4.56 |                           1.03 |
| 1                        |                         0.36 |                    1.07 |                 4.40 |                           1.11 |

Five performance curve modifiers are used for modeling the DX multispeed cooling objects. The performance curves were derived from separate work that used NREL lab testing data of three variable-speed, central-ducted AC systems where values representative of the three systems are used. For multispeed objects, these modifier curves are specific to the compressor speed to which they are applied, so each speed will have its own set of curves. They are described as follows:

1. Energy input ratio (EIR) as a function of part load ratio -uses the calculated part load ratio to determine an EIR modifier from compressor cycling, which is multiplied against the full-load EIR for the stage (Figure 4). Note that EIR is the inverse of COP, so decreasing the EIR increases the realized efficiency. For the multispeed units modeled in this work, this curve is only used for the lowest compressor speed where cycling losses may occur.
2. Capacity as a function of temperature -uses outdoor drybulb and indoor wetbulb temperatures to predict a capacity modifying factor that is multiplied against the rated capacity for each stage (Figure 5). For heat pumps, the available capacity decreases as outdoor temperature increases.
3. EIR as a function of temperature -uses outdoor drybulb and indoor wetbulb temperatures to determine an EIR (1/COP) modifying factor that is multiplied against the rated EIR for each stage for the time step (Figure 6). Note that other modifier functions can also affect the final COP.
4. Capacity as a function of flow -modifies capacity based on the determined flow rate for a time step. This curve is not used because capacity is already accounted for in the

- speed level. Therefore, capacity changes as a function of flow rate within a speed level are not considered in this work.
5. EIR as a function of flow -modifies EIR based on the determined flow rate for a time step. This curve is not used because the EIR is already accounted for in the speed level. Therefore, EIR changes as a function of flow rate within a speed level are not considered in this work.

The cooling performance maps for EIR as a function of part load ratio, capacity as a function of temperature, and COP as a function of temperature are shown Figure 4, Figure 5, and Figure 6, respectively.

Figure 4. Heating and cooling energy input ratio modifier as a function of part load ratio for all speed levels. This curve primarily captures losses due to part-load cycling at compressor speed 1. This value is divided by the EIR for the time step, which effectively decreases efficiency at lower part load ratios.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86585.yaml
     source: 86585_images/image_000008_cfba557bdcd8313a48635f4ecb1411e7a001eea5521c4306bbba8ab8c97e50ef.png
     method: vision-description
     described: 2026-08-21 -->

![Line chart of the energy input ratio modifier versus part load ratio, rising linearly from 0.76 at a part load ratio of 0 to 1.00 at a part load ratio of 1.](86585_images/image_000008_cfba557bdcd8313a48635f4ecb1411e7a001eea5521c4306bbba8ab8c97e50ef.png)

Single-panel line chart. The x-axis is "Part Load Ratio" from 0 to 1; the y-axis is "EIR Modifier" from 0.75 to 1. One blue line is plotted and it is straight: it starts at 0.76 at a part load ratio of 0 and rises linearly to 1.00 at a part load ratio of 1, a slope of 0.24 over the full range, passing through roughly 0.82 at 0.25, 0.88 at 0.5 and 0.94 at 0.75. The same curve is used for both heating and cooling coils. Note a documented inconsistency in the surrounding text about how this modifier is applied: the figure caption says the value "is divided by the EIR for the time step, which effectively decreases efficiency at lower part load ratios", whereas section 3.2.3 item 1 says it "is multiplied against the full-load EIR" and that "decreasing the EIR increases the realized efficiency". Only the divided reading produces the cycling penalty the caption describes. The caption also says the curve applies to "all speed levels" while section 3.2.3 says it is used only for the lowest compressor speed, where cycling losses occur.

Figure 5. Capacity as a function of temperature performance map for the four stages of cooling. This value is multiplied by the nominal capacity for each time step to determine the actual available capacity for the time step.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86585.yaml
     source: 86585_images/image_000009_1fe8e49b5d32ef2cadf9000d5fa63c0064ff74d18b8a96221271653f6b43649e.png
     method: vision-description
     described: 2026-08-21 -->

![Four-panel contour map of the cooling capacity modifier as a function of outdoor drybulb and indoor wetbulb temperature, one panel per compressor stage.](86585_images/image_000009_1fe8e49b5d32ef2cadf9000d5fa63c0064ff74d18b8a96221271653f6b43649e.png)

Two-by-two grid of filled contour maps titled "Capacity Function of Temperature: Stage 1" through "Stage 4" (the Stage 1 title drops the word "of"). In every panel the x-axis is "Outdoor Air Drybulb Temperature (C)" from 10 to 50 and the y-axis is "Indoor Air Wetbulb Temperature (C)" from about 15 to 24.5. Each panel has its own colour bar, "Capacity Modifier", spanning 0.0 to 2.0 on a blue-white-red diverging scale centred near 1.0, with unevenly spaced ticks at 0.0, 0.2, 0.5, 0.8, 1.0, 1.2, 1.5, 1.8 and 2.0. Inline contour labels are printed on each panel. Stages 3 and 4 behave as the body text describes: broad diagonal contours with the highest modifiers (about 1.2 for Stage 3 and about 1.6 for Stage 4) at low outdoor drybulb and high indoor wetbulb in the upper left, falling monotonically to about 0.9 at high outdoor drybulb and low indoor wetbulb in the lower right. Stages 1 and 2 are not monotonic: both show an interior blue depression near 25-35 C outdoor where the modifier drops to roughly 0.8-0.9, then rise again toward the right edge, Stage 1 reaching above 1.5 at 50 C. That reversal contradicts section 3.2.3's statement that available capacity decreases as outdoor temperature increases, and is consistent with biquadratic extrapolation beyond the fitted data range at low compressor speeds.

Figure 6. COP as a function of temperature performance map for the four stages of cooling. Note that these COP values are for the compressor only-adding in supply fan energy would decrease the values presented.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86585.yaml
     source: 86585_images/image_000010_663a1a3387dc1acfbb8a27cadd5dd4511bc913e48e5e27197a83f4af4d448db4.png
     method: vision-description
     described: 2026-08-21 -->

![Four-panel contour map of cooling COP as a function of temperature, one panel per compressor stage, with the two axis tick scales apparently transposed.](86585_images/image_000010_663a1a3387dc1acfbb8a27cadd5dd4511bc913e48e5e27197a83f4af4d448db4.png)

Two-by-two grid of filled contour maps titled "COP Function of Temperature: Stage 1" through "Stage 4". Each panel has its own colour bar labelled "COP" spanning 0.0 to 14.1, blue at the low end through white to red at the high end, with ticks at 0.0, 1.6, 3.1, 4.7, 6.3, 7.8, 9.4, 10.9, 12.5 and 14.1. Inline contour labels are printed on every panel. In all four panels COP is highest in the upper-left corner and falls smoothly toward the lower right, so the gradients run in the physically expected directions for cooling (better efficiency at lower outdoor temperature and higher indoor wetbulb). The axis tick scales, however, appear transposed relative to Figure 5: the horizontal axis is labelled "Outdoor Air Drybulb Temperature (C)" but is ticked only 15 to 24.5, while the vertical axis is labelled "Indoor Air Wetbulb Temperature (C)" but is ticked 10 to 50 - each axis carries the other's range. Because of this, Table 1's rated point of 4.11 COP at 35 C outdoor drybulb and 19.4 C indoor wetbulb cannot be located on the figure as ticked, and no point value is asserted here. Stage 1's x-axis label is misspelled "Temperaustre". Stages 1 and 2 show closed contour lobes of the kind seen in Figure 5's low-speed panels; Stages 3 and 4 have smooth diagonal contours.

