<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/98346.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/98346.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/98346.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/98346.md | section: 5.1  Single-Building Measure Tests | lines: 322-398 -->
## 5.1  Single-Building Measure Tests

In this section, we describe the operation of a large office building in Lawrence, Massachusetts, climate zone 5A, to demonstrate the measure scenario application on a single building. The baseline model uses packaged rooftop units (RTUs) with direct expansion cooling, hot water primary heating coils (supplied by an oil-fired boiler), and electric resistance supplemental heating coils. Outdoor ventilation air is provided directly through the RTUs.

In the baseline, the building has fixed setpoint schedules. Two measure scenarios are considered: one with a 5°F heating setback and one with a 10°F heating setback. In both cases, a 5°F setback is applied in cooling, and an optimum start is implemented over a 3-hour period before morning occupancy, gradually ramping the setpoint up or down to the occupied values. Note that in this case, for purposes of demonstrating the optimum start feature, the 10,000-cfm threshold that is generally used in the measure for implementation of an optimum start, consistent with 2022 ASHRAE 90.1, was not considered.

Figure 2 shows the modified zone-level heating setpoint schedules when applying the measure for a 5°F setback with the building occupancy schedule for a week starting on Monday, January 2. The measure treated the space as occupied if it had an occupancy fraction greater than 0.05. The measure successfully implements the setback during unoccupied hours and an optimum start, during which the temperature gradually ramps to the occupied value during a 3-hour period before occupancy. Figure 3 shows the same plots for a 1-day period to highlight the implementation of the optimum start. Based on the assumed threshold for occupancy, the building is occupied from 10:45 a.m. to 11:30 p.m. on weekdays. (Note that in ComStock, a building's hours of operation are assigned via distributions based on the building type [12].)

Figure 2. Thermostat heating setpoint schedule with setbacks and building occupancy schedule for the first week of January, 5°F setback

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98346.yaml
     source: 98346_images/image_000003_69cc188fd949ca9ce388f016cc615c433750702a399bff75ed84df7a0d67a4bc.png
     method: vision-description
     described: 2026-08-21 -->

![Dual-axis time series over the first week of January showing the 5°F-setback heating setpoint schedule against the building occupancy fraction and the 0.05 occupancy threshold.](98346_images/image_000003_69cc188fd949ca9ce388f016cc615c433750702a399bff75ed84df7a0d67a4bc.png)

Figure 2. Thermostat heating setpoint schedule with setbacks plotted against the building occupancy schedule for the first week of January in the 5°F setback case. The left vertical axis is Temperature in degrees Fahrenheit, 65 to 70; the right vertical axis is occupancy as a fraction, 0.0 to 1.0; the horizontal axis runs from 01-Jan 20:00 to 09-Jan 08:00. The blue Setpoint schedule sits at the 65°F unoccupied setback value overnight and rises to the 70°F occupied value each weekday morning, not as a step but as a three-hour optimum start ramp with treads at about 66.25, 67.5 and 68.75°F, that is 1.25°F per hour. The green Occupancy schedule is zero overnight and reaches 1.0 on the five weekdays of January 2 to 6, dipping to about 0.4 around midday each day before recovering. Saturday January 7 peaks at only about 0.3, and January 1 and January 8 are flat near zero, so no setup occurs on those days. A red dashed horizontal line marks the Threshold for occupancy at 0.05; hours above it are treated as occupied when the setback schedule is constructed.

Figure 3. Thermostat heating setpoint schedule with setbacks and building occupancy schedule for one day in January, 5°F setback

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98346.yaml
     source: 98346_images/image_000004_0e2d1e4bd6ce44bf509861cb084e70798e600b135134a30c9cf0d5f801fb4265.png
     method: vision-description
     described: 2026-08-21 -->

![Dual-axis time series for a single January day showing the 5°F heating setback releasing through a three-hour optimum start ramp as occupancy rises.](98346_images/image_000004_0e2d1e4bd6ce44bf509861cb084e70798e600b135134a30c9cf0d5f801fb4265.png)

Figure 3. The same two series as Figure 2 but zoomed to one day, with the horizontal axis running from 02-Jan 01:00 to 03-Jan 01:00. The left axis is Temperature in degrees Fahrenheit, 65 to 70, and the right axis is occupancy fraction, 0.0 to 1.0. The blue heating setpoint holds the 65°F setback value through the night, then climbs the three-hour optimum start staircase with treads near 66.25, 67.5 and 68.75°F before reaching the 70°F occupied setpoint. Section 5.1 gives this model's occupied period as 10:45 a.m. to 11:30 p.m. on weekdays, and the plotted setpoint holds 70°F to the end of that period before returning to 65°F. The green occupancy series is zero overnight, rises to 1.0 in the middle of the day, dips to about 0.4 in mid-afternoon, returns to 1.0 in the late afternoon and decays to about 0.1 by 8 p.m. The red dashed line is the 0.05 occupancy threshold. The point of the figure is the phase relationship: the ramp begins three hours before the occupied period so that the space reaches the occupied setpoint as occupancy arrives rather than after it.

Figure 4 shows a comparison of the setpoint schedules under the baseline and measure-modified conditions. Figure 5 shows the same comparison for the cooling setpoint schedules for a week in June. The measure successfully modifies the thermostat schedule and implements an optimum start in cooling mode as well as heating mode. Figure 6 demonstrates the successful implementation of the 10°F heating setback.

Figure 4. Baseline and modified heating thermostat setpoint schedules for one week in January, 5°F setback case

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98346.yaml
     source: 98346_images/image_000005_aff561ec7219c3659627080b01e156215019b280c2666555d76a3a8b1a4878d7.png
     method: vision-description
     described: 2026-08-21 -->

![Line chart comparing the flat 70°F baseline heating setpoint against the modified schedule that sets back to 65°F each night, over one week in January.](98346_images/image_000005_aff561ec7219c3659627080b01e156215019b280c2666555d76a3a8b1a4878d7.png)

Figure 4. Baseline and modified heating thermostat setpoint schedules for one week in January in the 5°F setback case. The vertical axis is Temperature in degrees Fahrenheit, 64 to 70; the horizontal axis runs from 01-Jan 23:00 to 08-Jan 23:00. The green Baseline setpoint schedule is a flat constant 70°F for the entire week, which is the point of the comparison: the baseline model has no setback at all, and this measure is applied only to models of that kind. The blue Modified setpoint schedule drops to 65°F during each unoccupied period and climbs back to 70°F through the three-hour optimum start staircase each morning, producing six ramp cycles across January 2 to 7. After the evening of January 7 the blue line stays at 65°F because January 8 is unoccupied. The 5°F vertical separation between the two lines during unoccupied hours is the setback depth being modeled.

Figure 5. Baseline and modified cooling thermostat setpoint schedules for one week in June

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98346.yaml
     source: 98346_images/image_000006_52e34b035f67ecd1ea9b5eb893fa5c608b4c46a3e82eee162a6c52cc2b1b3d0a.png
     method: vision-description
     described: 2026-08-21 -->

![Line chart comparing the flat 76°F baseline cooling setpoint against the modified schedule that sets up to 81°F when unoccupied; the plotted span is a single June day, not a week.](98346_images/image_000006_52e34b035f67ecd1ea9b5eb893fa5c608b4c46a3e82eee162a6c52cc2b1b3d0a.png)

Figure 5. Baseline and modified cooling thermostat setpoint schedules. The vertical axis is Temperature in degrees Fahrenheit, 76 to 81. The green Baseline setpoint schedule is a flat constant 76°F, matching the occupied cooling setpoint quoted in Section 3.2. The blue Modified setpoint schedule sits at 81°F when the space is unoccupied, that is the 76°F occupied setpoint plus the 5°F cooling setback, which stays below the 82°F maximum unoccupied cooling setpoint the measure enforces. It steps down through a three-hour optimum start staircase with treads near 79.75, 78.5 and 77.25°F, reaching 76°F at about 9 a.m., holds there through the occupied period, and returns to 81°F at about 11 p.m. Note a caption discrepancy: the caption and the body text both describe one week in June, but the plotted horizontal axis spans only 06-Jun 01:00 to about 07-Jun 03:00, a single day and a single setback cycle. Figure 4, the heating counterpart, does show a full week.

Figure 6. Thermostat heating setpoint schedule with setbacks and building occupancy schedule for one week in January, 10°F setback case

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98346.yaml
     source: 98346_images/image_000007_ed313d99875f5a1d81806a9c2c043ed9a6ecb9d300197f525cbc801b00ca5bf3.png
     method: vision-description
     described: 2026-08-21 -->

![Dual-axis time series over the first week of January for the 10°F setback case, showing the heating setpoint dropping to 60°F when unoccupied.](98346_images/image_000007_ed313d99875f5a1d81806a9c2c043ed9a6ecb9d300197f525cbc801b00ca5bf3.png)

Figure 6. Thermostat heating setpoint schedule with setbacks and the building occupancy schedule for one week in January in the 10°F setback case, which is the case ComStock actually applies. The layout is identical to Figure 2, but the left Temperature axis now spans 60 to 70 degrees Fahrenheit because the deeper setback puts the unoccupied heating setpoint at 60°F rather than 65°F. The blue setpoint series holds 60°F overnight and recovers to the 70°F occupied setpoint through the same three-hour optimum start, now with treads near 62.5, 65 and 67.5°F, that is 2.5°F per hour. The green occupancy series and the red dashed 0.05 occupancy threshold are unchanged from Figure 2: full occupancy on the five weekdays with a midday dip, a low Saturday peak, and near zero on January 1 and January 8. The resulting 60°F unoccupied setpoint sits above the 55°F minimum unoccupied heating setpoint the measure enforces, so no clipping occurs in this schedule.

Table 4 shows site energy savings by applicable end use for the two scenarios (5°F and 10°F heating setbacks) of the measure applied to the office building in Massachusetts, relative to the baseline. To reiterate, both scenarios had a 5°F cooling setback and optimum start. This measure results in cooling energy savings of around 9% and fuel oil heating energy savings of 17% to 25%, with greater savings resulting from the higher setback. In this building, the HVAC system fans run throughout the day and night to provide ventilation, whether the heating and cooling setpoints are met. As a result, there are no fan energy savings when applying the measure for this building. In general, fan energy savings from this measure are expected in buildings in which fans cycle on and off during unoccupied periods to meet thermostat setpoints as well as in variable air volume (VAV) systems (due to modulating airflow) and systems with decoupled ventilation and space conditioning. (In the latter case, energy savings would be expected from fans supplying air for space conditioning.) There is a small amount of electric supplemental heating energy use in the baseline, which is virtually eliminated through this measure. Note that in this case, there are no annual peak demand impacts when applying this measure since the peak is set by cooling energy use on a summer afternoon.

Table 4. Summary of Site Energy Savings From Single Building Run of Thermostat Setbacks Measure

| End Use/Fuel Type         |   Baseline |   Measure Applied 5°F Heating Setback | Percent Savings 5°F Setback   |   Measure Applied 10°F Heating Setback | Percent Savings 10°F Setback   |
|---------------------------|------------|---------------------------------------|-------------------------------|----------------------------------------|--------------------------------|
| Electric cooling (kWh)    |    153,333 |                               140,278 | 8.5%                          |                                140,000 | 8.8%                           |
| Fuel oil heating (therms) |     18,264 |                                15,175 | 16.9%                         |                                 13,639 | 25.3%                          |
| Electric heating (kWh)    |         28 |                                   0.0 | 100%                          |                                    0.0 | 100%                           |
| Electric fans (kWh)       |    453,334 |                               453,334 | 0%                            |                                453,334 | 0%                             |
| Annual peak demand (kW)   |        409 |                                   409 | 0%                            |                                    409 | 0%                             |

