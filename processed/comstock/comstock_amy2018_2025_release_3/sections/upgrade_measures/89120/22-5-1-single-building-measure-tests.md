<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89120.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89120.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89120.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/89120.md | section: 5.1  Single Building Measure Tests | lines: 253-284 -->
## 5.1  Single Building Measure Tests

To demonstrate the functionality of the measure on a single building, this measure was applied to a modified version of the packaged VAV warehouse model for Climate Zone 2A. The model uses a 10-zone packaged VAV system, with direct expansion cooling coils, and hot water coils for tempering supply air and for reheat. The 'baseline' version of the model, reflecting conditions without the measure applied, was configured with an 'always on' minimum outdoor air schedule and an air loop schedule based on the 'vent cycle' (cycle ventilation on during unoccupied periods to meet thermostat setpoints) approach.

The model was run with the Port Arthur, Texas, weather file. Measure tests were run to confirm that the version of the model with the measure applied ran successfully, and that the system outdoor air controller was now configured with a minimum outdoor air level set by a 'Schedule: Ruleset' and not a 'Schedule: Constant' object to reflect that minimum outdoor air levels are time-dependent. Time-series results were also evaluated for the example building model.

Figure 2 shows outdoor air flow through the air handling unit for a representative period of about 1 week (corresponding to January 1-8) in the base case and after the measure was applied. After applying the measure, the AHU does not bring in outdoor air during unoccupied periods, as neither of the models have an economizer enabled (If an economizer were enabled, economizing during unoccupied periods to meet temperature setpoints would be permitted.). The results shown in Figure 2 confirm this effect.

Figure 2. Outdoor air mass flow rate for AHU with fan cycling with ventilation ( base case), and fan cycling without ventilation (after measure applied)

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89120.yaml
     source: 89120_images/image_000009_4b56f9589ec0f6201c8d30852facc4b174e30e4322005a722a402b40ff578b7c.png
     method: vision-description
     described: 2026-08-20 -->

![One-week time series of outdoor airflow for a single air handling unit, comparing a constant baseline against the measure's occupancy-following square wave](89120_images/image_000009_4b56f9589ec0f6201c8d30852facc4b174e30e4322005a722a402b40ff578b7c.png)

Figure 2. Single-panel time-series plot for the example building's air handling unit. The y axis is 'Outdoor airflow (kg/s)', ticked 0.00 to 0.40; the x axis runs from 2016-01-01 to 2016-01-08, one week. Two series are overlaid: an orange 'Baseline' line that is flat at about 0.38 kg/s for the whole week, and a blue 'Measure' line that is a square wave alternating between the same 0.38 kg/s and zero. The blue series is high from roughly 05:00 to 18:00 on Friday 1 January and again on Monday 4 January through Thursday 7 January, and sits at zero overnight and across the whole 2-3 January weekend. Where the measure series is at its high value it is drawn on top of the baseline line, so only the vertical risers and falls are visible in blue. The plot is the single-building illustration of what the measure does: the baseline ventilates continuously, the measure ventilates only during occupied hours.

Figure 3 shows a comparison of energy use in end uses affected by the measure (electricity for cooling and fans and natural gas heating), before and after implementation in the example warehouse building. Because the baseline model uses a 'vent cycle' approach (the supply fans cycle to meet load during unoccupied hours), a reduction in fan operating hours is not expected through application of the measure. There was a reduction in heating and cooling energy use observed, as expected, through the reduction in load from tempering outdoor air. The reduction in fan energy use can also be attributed to this reduction in heating and cooling load.

Figure 3. Comparison of key energy end uses before and after implementing Improved Fan Scheduling and Outdoor Air Control measure in example building

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89120.yaml
     source: 89120_images/image_000010_98fde4ec9987be436e8df4a73d83378a97cb5529662072a8a81422786caefac4.png
     method: vision-description
     described: 2026-08-20 -->

![Grouped bar chart comparing baseline and measure energy use in gigajoules for three end uses in the example warehouse building](89120_images/image_000010_98fde4ec9987be436e8df4a73d83378a97cb5529662072a8a81422786caefac4.png)

Figure 3. Grouped vertical bar chart for the example warehouse. The y axis is 'Energy_Use_GJ', ticked 0 to 70; the x axis is 'End_Use' with three groups; the legend 'Case' distinguishes blue Baseline from orange Measure bars. Values: Heating_NG falls from 34.0 to 21.1 GJ; Cooling_Elec falls from 68.8 to 37.3 GJ; Fans_Elec falls from 19.1 to 11.1 GJ. Cooling is the largest end use and shows the largest absolute drop (-31.5 GJ, -46%); fans show the largest proportional drop after cooling (-42%) and heating gas falls 38%. Section 5.1 notes that because this building's baseline already uses a 'vent cycle' approach, no reduction in fan operating hours was expected, and attributes the observed fan reduction to the lower heating and cooling load from tempering less outdoor air.

