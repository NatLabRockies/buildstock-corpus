<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95119.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95119.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95119.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/95119.md | section: 3.2.2  Heat Pump Heating | lines: 306-380 -->
## 3.2.2  Heat Pump Heating

The modeling methodology used in this study intends to align with the performance data from NREL laboratory testing of a standard efficiency 7.5-ton HP-RTU, and other assumptions from typical commercial off-the-shelf HP-RTUs on the market today. The RTUs are modeled with one stage of direct expansion (DX) heat pump heating. Although these RTUs often have two compressor stages, the default operation of the tested unit as well as other available products [4] use both compressors as the first and only stage of heat pump heating.

Table 1. Heat Pump Rated Heating COP and Capacity by Heating Stage

Gross COP and capacity values shown in this table are at rated conditions and therefore do not include the impact of performance modifier curves. Rated values are at 47°F ambient air temperature and 70°F at the indoor coil.

|   Heating Stage | Stage Name   |   Capacity Fraction of Rated |   Fan Flow Fraction |   COP Fraction of Rated |   Applied Rated COP 1 | Minimum Lockout Temperature   |
|-----------------|--------------|------------------------------|---------------------|-------------------------|-----------------------|-------------------------------|
|               1 | High (rated) |                            1 |                   1 |                       1 |                   4.0 | 0°F                           |

1 Rated COP is the gross COP, which does not include indoor fan heat or fan power

As discussed in Section 3.2.1, the rated heating capacity is sized to match the required rated cooling capacity, which is determined for every individual RTU in ComStock. If the required heating load is greater than what the heat pump can provide for a timestep, or the heat pump is locked out, then supplemental heating is used to address any unmet heating loads.

Heat pump performance and capacity can vary substantially based on operating conditions, including indoor/outdoor temperature, fan flow fraction, and part load ratio. These interactions are accounted for in the simulation through performance modifier curves. This performance curve set was constructed using NREL laboratory testing data of a 7.5-ton standard performance HP-RTU.

1. Heating capacity as a function of temperature : Indoor and outdoor drybulb temperature are used at each timestep to determine a capacity modifying factor that is multiplied against the gross rated capacity for each stage. The data fits are illustrated for each heating stage in Figure 2, with each data point reflecting the result of laboratory testing. During simulation, the ratios (right plot) are multiplied by the nominal heat pump heating capacity for each time step to determine the actual available capacity for the time step.
2. Heating efficiency as a function of temperature : Indoor and outdoor drybulb temperature are used at each timestep to determine an efficiency modifying factor that is multiplied against the gross rated energy input ratio (EIR) (EIR = 1/COP) for each heating stage. The curves are illustrated for each heating stage in Figure 3 with each data point reflecting the results of laboratory testing. During simulation, the ratios (right plot) are multiplied by the gross heat pump heating efficiency for each time step to determine the realized COP for the time step.
3. Heating efficiency as a function of part load ratio: Part load ratio, which is defined as the fraction of load required for the timestep divided by the total available heating capacity, is used at each timestep to determine an efficiency modifier factor that is divided by the gross rated EIR. This performance curve essentially reduces equipment efficiency due to cycling losses. The curve is illustrated in Figure 4.
4. Defrost power as a function of temperature : Indoor wetbulb and outdoor drybulb temperature are used at each timestep to determine a power modifying factor that is multiplied by the rated heating capacity. This performance curve dictates compressor power usage during reverse cycle defrost operation and is only active during timesteps where defrost occurs. The curve is illustrated in Figure 5. Defrost operation is discussed further in Section 3.2.4.

Figure 2 . Heat pump gross heating capacity as a function of temperature performance map.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95119.yaml
     source: 95119_images/image_000003_2e2ac92c7d0fe66d2ca0e918ed8ef81c83ad4875780d2646afa15d158758e5c1.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 2. Two-panel performance map of heat pump gross heating capacity and capacity ratio versus outdoor drybulb temperature, for three indoor drybulb conditions at Stage 2](95119_images/image_000003_2e2ac92c7d0fe66d2ca0e918ed8ef81c83ad4875780d2646afa15d158758e5c1.png)

Figure 2 is a two-panel performance map from laboratory test data. Both panels plot Outdoor Drybulb (degrees F) on the x-axis from 0 to 60, with markers for measured points and fitted lines through them. Three series are given by a legend titled "Indoor Drybulb (F)": 40 Stage 2 (blue), 55 Stage 2 (orange), and 70 Stage 2 (green). The left panel plots Gross Cap (SL) in kW on a y-axis from about 10 to 35; all three series rise roughly linearly with outdoor temperature, from about 11, 10, and 9 kW at 0 degrees F to about 34.5, 31, and 29 kW at 60 degrees F for the 40, 55, and 70 degree indoor conditions respectively. The right panel plots Gross Capacity Ratio, the same quantity normalized to rated conditions, on a y-axis from about 0.4 to 1.4; the three series run from roughly 0.45, 0.42, and 0.38 at 0 degrees F to roughly 1.35, 1.22, and 1.15 at 60 degrees F. The consistent message is severe capacity derating in cold weather -- heating capacity at 0 degrees F outdoors is under half the value at 60 degrees F -- and that a lower indoor drybulb yields higher gross capacity at any given outdoor temperature.

The left plot shows the raw gross heating capacity of the tested unit, while the right plot shows the generalized ratios applied in modeling.

Figure 3 . Heat pump gross heating COP as a function of temperature performance map.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95119.yaml
     source: 95119_images/image_000004_3dfa0b5ee02a466336d4736838cb84aaa6a5979d99449903a719a4160e681df4.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 3. Two-panel performance map of heat pump gross heating COP and COP ratio versus outdoor drybulb temperature, for three indoor drybulb conditions at Stage 2](95119_images/image_000004_3dfa0b5ee02a466336d4736838cb84aaa6a5979d99449903a719a4160e681df4.png)

Figure 3 is the coefficient-of-performance companion to Figure 2, again two panels plotting Outdoor Drybulb (degrees F) from 0 to 60 with measured markers and fitted lines, and the same "Indoor Drybulb (F)" legend of 40 Stage 2 (blue), 55 Stage 2 (orange), and 70 Stage 2 (green). The left panel plots Gross COP (SL) on a y-axis from about 1 to 7; the curves rise with outdoor temperature and flatten slightly at the warm end, running from about 2.7, 2.2, and 1.7 at 0 degrees F to about 7.0, 5.7, and 4.6 at 60 degrees F for the 40, 55, and 70 degree indoor conditions. The right panel plots Gross COP Ratio, normalized to rated conditions, on a y-axis from about 0.4 to 1.8, running from roughly 0.68, 0.55, and 0.42 at 0 degrees F to roughly 1.75, 1.42, and 1.15 at 60 degrees F. Efficiency therefore falls even faster than capacity in cold weather: at 0 degrees F the unit delivers roughly a quarter to two-fifths of its rated COP. Lower indoor drybulb again gives better performance, because the lift the compressor must overcome is smaller.

The left plot shows the raw gross heating COP of the tested unit, while the right plot shows the generalized ratios applied in modeling.

Figure 4 . Energy input ratio (EIR) as a function of part load ratio.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95119.yaml
     source: 95119_images/image_000005_1b7f87298f31a00bb9921da3bb0dfc398134dfa8fe1f1ca7f99f632981342a51.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 4. Scatter plot of energy input ratio as a function of part load ratio, with measured and estimated points and a two-segment piecewise curve fit](95119_images/image_000005_1b7f87298f31a00bb9921da3bb0dfc398134dfa8fe1f1ca7f99f632981342a51.png)

Figure 4 plots EIR Ratio (energy input ratio, dimensionless) on the y-axis from about 0.4 to 1.0 against Part Load Ratio (PLR, dimensionless) on the x-axis from 0 to 1. A legend gives four series: Measured (blue circles), Estimated ON (red diamonds), Estimated OFF (green squares), and Curve fit (black dash-dot line). A vertical dashed line marks a breakpoint at PLR 0.293, and the two printed piecewise quadratic fits are: for PLR < 0.293, y = -4.5732x^2 + 3.1067x + 0.3151; for PLR > 0.293, y = -0.2706x^2 + 0.5865x + 0.6841. The fitted curve rises steeply from an EIR ratio of roughly 0.40-0.45 at very low PLR to about 0.83 at the 0.293 breakpoint, then climbs gently and nearly linearly to 1.0 at full load. Data points cluster densely along the fit, with the Estimated OFF series concentrated below the breakpoint and Estimated ON above it, and a couple of measured points near PLR 0.45 falling noticeably below the curve. The shape encodes the cycling penalty: at low part load the unit consumes proportionally more input energy per unit of output than the linear-scaling assumption would predict.

The output of this curve is divided by the EIR (1/COP) at each timestep, effectively reducing efficiency due to cycling losses. EnergyPlus does not currently support performance curves in the form of piecewise regressions functions, therefore, the above functions are implemented in the models through lookup tables generated with these functions.

Figure 5 . Defrost power modifier curve as a function of indoor wetbulb and outdoor drybulb temperature.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95119.yaml
     source: 95119_images/image_000006_3efe4e409d0f41267ab837ea1783805321106c5d5f0c92512f72b79a2a6e6aba.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 5. Heatmap of the defrost power modifier fraction as a function of outdoor drybulb and indoor wetbulb temperature, with measured test points overlaid](95119_images/image_000006_3efe4e409d0f41267ab837ea1783805321106c5d5f0c92512f72b79a2a6e6aba.png)

Figure 5 is a two-dimensional heatmap of the defrost power modifier curve. The x-axis is Outdoor Dry Bulb Temperature in degrees F, running from about -10 to 35, and the y-axis is Indoor Wet Bulb Temperature in degrees F, running from about 40 to 67. Color encodes a quantity labeled simply "Fraction" on a colorbar spanning roughly 0.35 (dark blue) to above 0.42 (yellow), with intermediate teal and green. The surface varies smoothly and near-diagonally: the highest fraction (yellow, above 0.42) sits in the upper-left corner at low outdoor drybulb and high indoor wetbulb, and the lowest (dark blue, around 0.35) sits in the lower-right at high outdoor drybulb and low indoor wetbulb. Roughly eight red dots overlay the surface marking the actual laboratory test conditions from which the curve was regressed; they are spread across the corners and middle of the domain rather than clustered. The physical reading is that the defrost power penalty is largest in cold, humid conditions, which is when frost accumulation on the outdoor coil is worst.

The output of this curve is multiplied by the rated heating capacity, the fractional defrost time and the runtime fraction of the heating coil to give the defrost power for the timestep. The red dots are the testing points.

