<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89117.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89117.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89117.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/89117.md | section: 5.1  Single Building Measure Tests | lines: 422-499 -->
## 5.1  Single Building Measure Tests

To demonstrate the functionality of the measure, the Advanced RTU Controls measure was applied to a retail model with single-zone, constant-volume RTU systems in Climate Zone 4A ('retail PSZ AC model'), with the Leesburg, Virginia, weather file. This section reviews the operation of the VAV fan control and air-side economizing features.

Illustrative results are presented for a zone with high fan power relative to the rest of the building, 'Retail, Retail B-Story Ground.' Figure 3 shows a comparison of the supply airflow rates for that zone for a roughly one-week period in July, for the 'base' case and with the measure applied ('measure'). The zone level cooling load for the same period in the 'measure' case is shown in the bottom plot in Figure 3. The upper figure shows how, in the measure case, fan speed modulates to meet the cooling load, while reducing to the 'low-load' level during periods when loads are low. The implementation of this measure is not expected to change zonelevel loads.

Figure 3. Supply airflow rate for the base case and with the measure applied for the selected zone (top), and zone load for the measure case (bottom)

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89117.yaml
     source: 89117_images/image_000008_1e6455e396be61ff49ba9a5bf20b0c7576f43ac1e3810ec95f6ca7b978f59e57.png
     method: vision-description
     described: 2026-08-21 -->

![Two stacked time series over a week in July for one retail zone: supply airflow for the base and measure cases (top) and the measure-case zone load (bottom).](89117_images/image_000008_1e6455e396be61ff49ba9a5bf20b0c7576f43ac1e3810ec95f6ca7b978f59e57.png)

Figure 3. Two stacked panels sharing an x-axis "Hour of year" running about 5040 to 5232, i.e. roughly eight days in late July, for the zone "Retail, Retail B-Story Ground" of the retail PSZ-AC test model. Top panel, y-axis "Fan airflow (kg/s)" 0.0 to 1.5, two series: the baseline (blue) is a square wave holding an occupied plateau of 1.45 kg/s and decaying to about 0.17-0.20 kg/s when unoccupied; the measure (orange) holds a much lower occupied plateau of 0.58 kg/s, which is 40% of the baseline plateau and matches the stated 40% minimum supply airflow ratio, spiking up to the full 1.45 kg/s only on the hottest days. Unoccupied hours track the baseline. Bottom panel, y-axis "Zone load (W)" from 0 down to -25000 with the legend showing "Measure" only. Every value is negative, so the zone is cooling throughout, consistent with the note that a negative load corresponds to cooling. Overnight load sits near -3,000 W and the daily peaks deepen through the week to about -23,300 W and -24,000 W on the last two days - the same two days on which the top panel's measure airflow spikes to the maximum.

Note that a negative load corresponds to cooling.

Figure 4 shows the fan power of the corresponding packaged unit for the same period, in the base case and with the measure applied. In this case, and for many zones in the building, the fan operates for much of the year at the 40% of maximum airflow rate that is set as the minimum allowable airflow, consistent with typical ARC configurations. (Note that the minimum was imposed as the larger of 40% of maximum airflow, or the minimum ventilation requirement, so this minimum airflow may exceed 40% of maximum in some zones.) A theoretical purely cubic fan law would result in fan power of 8% of the base case, under these conditions, with the airflow around 40% of maximum. Fan curves in practice and as represented in EnergyPlus are not purely cubic, and in modeling this system, a fan power minimum of 30% was imposed, reflecting the typical minimum turndown for VFDs attached to non-inverter duty motors, representative of retrofits of older existing systems. Thus, when the fan is operating at low-load conditions, as it does for many hours of the year, it is operating at 30% of the maximum power. (VFD losses were not accounted for as part of this analysis. Some single zone VAV retrofits can be accomplished through the use of electronically commutated motors, which in certain circumstances, can operate more efficiently than a motor and VFD combination.) In both the base and measure cases, the occupied hours in which a zone setpoint was not met were similar, and low, indicating that the systems continue to meet loads effectively with this measure applied. Note that the constant-volume fan in the baseline (represented with a Fan:OnOff object), as modeled in EnergyPlus, can drop to a lower minimum power level, resulting in the lower minimum fan power for the baseline shown in the figure.

Figure 4. Fan power for the base case and with the measure applied for the selected zone

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89117.yaml
     source: 89117_images/image_000009_5041f67115f583ae65ddd1a6742cf4b752974c2f9ca31e498e262e04e51a426d.png
     method: vision-description
     described: 2026-08-21 -->

![Time series of packaged unit fan power over the same July week, comparing the constant volume baseline against the measure case, which holds a continuous low-load floor.](89117_images/image_000009_5041f67115f583ae65ddd1a6742cf4b752974c2f9ca31e498e262e04e51a426d.png)

Figure 4. Single panel, y-axis "Fan power (W)" 0 to 2500, x-axis "Hour of year" over the same late-July window as Figure 3, for the same zone. The baseline (blue) is a square wave with an occupied plateau of about 2,330 W and an unoccupied floor of about 290-350 W. The measure (orange) never drops to the baseline's overnight floor; instead it holds a continuous low-load level of about 820 W, rising to the full 2,330 W only in the short high-airflow bursts that correspond to the airflow spikes in Figure 3. The plotted ratio of the measure floor to the baseline occupied plateau is about 35%, somewhat above the 30% fan power minimum the body text says was imposed, but 1 - 0.353 = 64.7% is consistent with section 5.4's observation that no datapoint shows fan energy savings above 67%. The baseline dipping below the measure's floor overnight is expected and explained in the text: the constant volume baseline is modelled with a Fan:OnOff object that can drop below the Fan:VariableSpeed minimum.

Figure 5 (a and b) confirms the economizer performance over a several-day period in October. The economizer is controlled based on differential enthalpy. As shown in Figure 5a, outdoor air enthalpy is less than return air enthalpy throughout the entire period. The system is generally operating at 100% outdoor air throughout this period, as shown in Figure 5b (top). Due to the limited cooling load (as shown in Figure 5b (bottom), the system is generally operating at its 'low load' flow rate throughout this period. In this zone, and in several other zones in the building, 40% of the maximum airflow is higher than the ventilation requirement, and thus the effects of DCV are not evident, as they would result in airflow below the minimum set based on the characteristics of common ARC controls. This is illustrated in Figure 6, showing that the airflow never drops below 0.6 kg/s (40% of the maximum airflow) during occupied periods, even with varying levels of occupants during the occupied periods. Figure 7 shows the zone occupant count over that time period, for reference. (Note that a lower minimum airflow rate would allow for greater opportunities for DCV implementation in spaces such as this in which the ventilation airflow is less than 40% of the maximum.)

Figure 5a. Outdoor air and return air enthalpy for the selected zone

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89117.yaml
     source: 89117_images/image_000010_9c17263f0b86e4a9beac22b8d2e7afa930a0eced002e2bc0386ac359de806194.png
     method: vision-description
     described: 2026-08-21 -->

![Time series of outdoor air and return air enthalpy over several days in October, with outdoor enthalpy below return enthalpy throughout the period.](89117_images/image_000010_9c17263f0b86e4a9beac22b8d2e7afa930a0eced002e2bc0386ac359de806194.png)

Figure 5a. Single panel, y-axis "Enthalpy (j/kg)" (the source label uses a lowercase j) from 10000 to 45000, x-axis "Hour of year" about 6910 to 7008 - a several-day window in mid-October. Two series: "Outdoor air enthalpy" (red) swings between roughly 9,800 and 36,500 J/kg on a daily cycle, and "Return air enthalpy" (green) stays in a much narrower band of roughly 31,500 to 44,200 J/kg. The green trace lies above the red trace for the entire period, with the narrowest gap of about 7,500 J/kg near hour 6923. Since the economizer in this measure is controlled on differential enthalpy, outdoor enthalpy being below return enthalpy throughout means the economizer is eligible for the whole window - exactly what section 5.1 asserts, and the premise for the 100% outdoor air operation shown in Figure 5b.

Figure 6b. System total airflow and outdoor airflow (top), and zone cooling load (bottom)

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89117.yaml
     source: 89117_images/image_000011_5d8524b687ae1b40dfba0ef4671e11567db4009c01cb4846ed756b5ad2d1bddc.png
     method: vision-description
     described: 2026-08-21 -->

![Two stacked time series for the October economizer window: system total and outdoor airflow (top), and zone cooling load (bottom).](89117_images/image_000011_5d8524b687ae1b40dfba0ef4671e11567db4009c01cb4846ed756b5ad2d1bddc.png)

Figure 5b, printed in the document with the caption "Figure 6b". Two stacked panels over the same mid-October window as Figure 5a (hour of year about 6910 to 7008). Top panel, y-axis "Airflow (kg/s)" 0.0 to 1.0, with "System total airflow" (blue) and "System outdoor airflow" (orange). During occupied hours the two series lie on top of one another at a plateau of 0.58 kg/s, i.e. the system is drawing essentially 100% outdoor air, which is what section 5.1 states for this period. Unoccupied hours decay to roughly 0.10-0.20 kg/s and one occupied peak reaches about 0.71 kg/s near hour 7002; two brief dropouts near hours 6929 and 6977 pull the traces down sharply. Bottom panel, y-axis "Zone load (W)" from 0 down to -8000, legend "Zone load". All values are negative, so the zone is cooling throughout, but the loads are shallow compared with the July week in Figure 3: overnight values sit around -2,000 to -3,600 W and daily peaks reach only about -6,900 to -7,300 W. That limited cooling load is why the system stays at its low-load flow rate for most of the window.

Figure 7. Outdoor airflow and overall fan airflow for selected zone, with measure applied

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89117.yaml
     source: 89117_images/image_000012_8d5e3ecc1f4c574e6a9e22ef54ac519812c870ba6265858182fa83cf4ab629fc.png
     method: vision-description
     described: 2026-08-21 -->

![Time series of system total and outdoor airflow over about eight days in October, with the occupied airflow pinned at the 0.58 kg/s low-load minimum.](89117_images/image_000012_8d5e3ecc1f4c574e6a9e22ef54ac519812c870ba6265858182fa83cf4ab629fc.png)

Figure 6, printed in the document with the caption "Figure 7". Single panel, y-axis "Airflow (kg/s)" 0.0 to 1.0, x-axis "Hour of year" about 6840 to 7030 - a wider October window than Figure 5b, covering eight occupancy cycles. "System total airflow" (solid blue) and "System outdoor airflow" (dashed orange) again coincide during occupied hours at a flat plateau of 0.58 kg/s, with short peaks to 0.91, 0.85, 0.73 and 0.71 kg/s on the days with the largest cooling demand. Unoccupied hours fall to roughly 0.10-0.33 kg/s, and the outdoor airflow trace drops to zero twice, when the outdoor air damper closes completely. The point of the figure is that the occupied plateau never falls below the low-load minimum, which is 40% of the 1.45 kg/s maximum airflow seen in Figure 3; section 5.1 rounds that plateau to 0.6 kg/s. Because the ventilation requirement in this zone is below 40% of maximum airflow, demand-controlled ventilation cannot pull the flow any lower, so no DCV modulation is visible even though occupancy varies substantially over the same period (Figure 7).

Figure 8. Zone occupant count for selected zone, with measure applied

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89117.yaml
     source: 89117_images/image_000013_6ffd14257cbc8c4e53a9f499f17117f42cb7899ea8171117e00dec552abc54bd.png
     method: vision-description
     described: 2026-08-21 -->

![Time series of zone occupant count over the same October window, showing eight daily occupancy pulses that peak near 73-74 people with one much lower day near 37.](89117_images/image_000013_6ffd14257cbc8c4e53a9f499f17117f42cb7899ea8171117e00dec552abc54bd.png)

Figure 7, printed in the document with the caption "Figure 8". Single panel, y-axis "Occupant count" 0 to 80, x-axis "Hour of year" about 6840 to 7030 - the same window as Figure 6 - with one red series labelled "Occupancy". Eight daily pulses rise from zero overnight to a peak of about 73 people, one of which holds a broader plateau near 74 around hours 6875-6880. Each pulse passes through an intermediate shoulder near 46 people on the way up and down. One day, near hours 6900-6905, peaks at only about 37 people, and a shorter shoulder near 19 appears around hour 6885. The figure is provided as reference for Figure 6: occupancy varies by roughly a factor of two from day to day, yet the occupied supply airflow in Figure 6 stays pinned at 0.58 kg/s, demonstrating that the 40%-of-maximum airflow floor governs over the demand-controlled ventilation setpoint in this zone.

