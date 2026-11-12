<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/93846.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/93846.md | section: 4.1  Single-Building Examples | lines: 473-544 -->
## 4.1  Single-Building Examples

We performed an initial ResStock test run to validate the operation of the load flexibility measures. This was a test run performed before the final input values were established, which is why some values differ from the final selection. The test run was performed using 50 models spread across the nation with two scenarios (also called upgrades):

- Upgrade 1: load shifting plus load shedding -a pre-peak duration of 2 hours, a peak duration of 1 hour, and an offset of 2°F during both the pre-peak and on-peak period
- Upgrade 2: load shedding only -no pre-peak load shifting, a peak duration of 1 hour, and an offset of 2°F during the on-peak period.

Figure 3 shows the time-series thermostat set point for a dwelling unit in Delaware. Note that this dwelling unit has a temperature setback during the night. We can see that for upgrade 1, there is both a pre-peak and peak offset, with the peak period being 18:00 to 19:00. For upgrade 2, there is no pre-peak offset. Both show the expected temperature offset of 2°F.

Figure 3. Verification of set point changes

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/93846.yaml
     source: 93846_images/image_000004_9fdc5c56e0145c0c5a74d4625ceb19c412c38ae3247f56420193b3bd7856b5b1.png
     method: vision-description
     described: 2026-11-11 -->

![Line chart of heating set point over five January days for three upgrade scenarios](93846_images/image_000004_9fdc5c56e0145c0c5a74d4625ceb19c412c38ae3247f56420193b3bd7856b5b1.png)

Figure 3: line chart titled 'Temperature setpoint'. X-axis is time over about five days in early January 2007; y-axis is temperature in °F. Three series, Upgrade 0, Upgrade 1 and Upgrade 2, are the heating set point. All follow the same daily schedule of a higher and a lower set point; once a day Upgrade 1 steps up above the others for a few hours and then drops below, and Upgrade 2 only drops. Axis values are too small to read in the bitmap.

Figure 4 shows the time-series conditioned space temperature changes. The results show that the indoor temperature quickly tracks the set point changes, especially during preheating. This hints that the preheating duration can be significantly shortened, at least for this building. See Section 4.6 on the known limitations for a discussion on the thermal capacitance of the models in ResStock, which also has a bearing on this observation.

Figure 4. Verification of conditioned space temperature changes

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/93846.yaml
     source: 93846_images/image_000005_07961a4f4885bb7ef48a54f29e7f3a97d1eafac235668c2a941a3f5648e1353b.png
     method: vision-description
     described: 2026-11-11 -->

![Line chart of conditioned space temperature over five January days for three upgrade scenarios](93846_images/image_000005_07961a4f4885bb7ef48a54f29e7f3a97d1eafac235668c2a941a3f5648e1353b.png)

Figure 4: line chart titled 'Conditioned Space Temperature'. X-axis is time over about five days in early January 2007; y-axis is temperature in °F. Three series, Upgrade 0, Upgrade 1 and Upgrade 2, follow the same daily pattern as the set points in Figure 3: the space temperature rises above the baseline for a few hours each day under Upgrade 1 and then dips, and only dips under Upgrade 2. Axis values are too small to read in the bitmap.

Figure 5 shows the time-series heating energy consumption. For upgrade 1, the results show additional energy consumption for preheating before the peak period and lower energy consumption during the peak period. There is also an occasional rebound after the peak period ends at 19:00. For upgrade 2, the energy consumption starts deviating from the baseline only at the beginning of the peak period. Although it consumes less energy than the baseline during the peak, it consumes slightly more than upgrade 1 because it does not have preheating.

Figure 5. Verification of conditioned space temperature changes

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/93846.yaml
     source: 93846_images/image_000006_237219a796170b95c283c7880a902ec35a40297ff8ae71239d18baa8505fdbb9.png
     method: vision-description
     described: 2026-11-11 -->

![Line chart of heating energy consumption over five January days for three upgrade scenarios](93846_images/image_000006_237219a796170b95c283c7880a902ec35a40297ff8ae71239d18baa8505fdbb9.png)

Figure 5: line chart titled 'Heating Energy Consumption'. X-axis is time over about five days in early January 2007; y-axis is energy. Three series, Upgrade 0, Upgrade 1 and Upgrade 2, lie almost on top of each other, with short sharp drops and spikes once a day where the set point changes. The caption calls this a conditioned space temperature check; the plot's own title is heating energy. Axis values are too small to read in the bitmap.

Figure 6 shows the daily total heating energy consumption for the same period as the time-series data in Figure 5. The jaggedness of the heating consumption profile was not investigated because of scope limitations. Although the daily consumption values are all very close, upgrade 2 is usually the lowest (though not always) due to the lack of preheating and the offset during the peak. Interestingly, upgrade 1 is also frequently lower than the baseline despite the preheating period, which is twice as long as the peak period, and the equal offset in the other direction.

Figure 6. Validation of daily energy consumption in one building

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/93846.yaml
     source: 93846_images/image_000007_10db1b29bf7776feccb0e8319ad0e975528394d7820b2a6d692c2bfcdc91a17f.png
     method: vision-description
     described: 2026-11-11 -->

![Line chart of daily total heating energy in one building over six days for three upgrade scenarios](93846_images/image_000007_10db1b29bf7776feccb0e8319ad0e975528394d7820b2a6d692c2bfcdc91a17f.png)

Figure 6: line chart titled 'Daily Total Heating Energy consumption'. X-axis is January 1 to 6, 2007; y-axis is energy usage, 65 to 95. Three series, Upgrade 0, Upgrade 1 and Upgrade 2, are heating electricity in kWh and stay within about 2 of each other every day: all rise from about 76 to a peak near 88 on January 5 and fall to about 65 on January 6.

Figure 7 shows a more consistent pattern of which upgrade uses the most energy when we consider more buildings. The results show that upgrade 1 consumes more energy on average than the baseline, and upgrade 2 consumes less energy than the baseline; however, the single-building example shows that there are exceptions, from both day-to-day and building-to-building perspectives.

Figure 7. Validation of daily energy consumption in 13 buildings

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/93846.yaml
     source: 93846_images/image_000008_3d2bc4c66e1a8bfb1a2e48c59565c0fbeafd4cf84475045a6c45fbd071788c3a.png
     method: vision-description
     described: 2026-11-11 -->

![Line chart of heating energy consumption in 13 buildings over seven days for three upgrade scenarios](93846_images/image_000008_3d2bc4c66e1a8bfb1a2e48c59565c0fbeafd4cf84475045a6c45fbd071788c3a.png)

Figure 7: line chart titled 'Heating Energy Consumption - 13 buildings'. X-axis is January 1 to 7, 2007; y-axis is energy usage, 24 to 34. Three series, Upgrade 0, Upgrade 1 and Upgrade 2, are heating electricity in kWh. All rise from about 25 to about 33.5 over the week; Upgrade 1 runs about 0.5 above the other two, which nearly coincide.

