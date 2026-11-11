<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/93846.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/93846.md | section: 4.1  Single-Building Examples | lines: 438-474 -->
## 4.1  Single-Building Examples

We performed an initial ResStock test run to validate the operation of the load flexibility measures. This was a test run performed before the final input values were established, which is why some values differ from the final selection. The test run was performed using 50 models spread across the nation with two scenarios (also called upgrades):

- Upgrade 1: load shifting plus load shedding -a pre-peak duration of 2 hours, a peak duration of 1 hour, and an offset of 2°F during both the pre-peak and on-peak period
- Upgrade 2: load shedding only -no pre-peak load shifting, a peak duration of 1 hour, and an offset of 2°F during the on-peak period.

Figure 3 shows the time-series thermostat set point for a dwelling unit in Delaware. Note that this dwelling unit has a temperature setback during the night. We can see that for upgrade 1, there is both a pre-peak and peak offset, with the peak period being 18:00 to 19:00. For upgrade 2, there is no pre-peak offset. Both show the expected temperature offset of 2°F.

Figure 3. Verification of set point changes

![Image](93846_images/image_000004_9fdc5c56e0145c0c5a74d4625ceb19c412c38ae3247f56420193b3bd7856b5b1.png)

Figure 4 shows the time-series conditioned space temperature changes. The results show that the indoor temperature quickly tracks the set point changes, especially during preheating. This hints that the preheating duration can be significantly shortened, at least for this building. See Section 4.6 on the known limitations for a discussion on the thermal capacitance of the models in ResStock, which also has a bearing on this observation.

Figure 4. Verification of conditioned space temperature changes

![Image](93846_images/image_000005_07961a4f4885bb7ef48a54f29e7f3a97d1eafac235668c2a941a3f5648e1353b.png)

Figure 5 shows the time-series heating energy consumption. For upgrade 1, the results show additional energy consumption for preheating before the peak period and lower energy consumption during the peak period. There is also an occasional rebound after the peak period ends at 19:00. For upgrade 2, the energy consumption starts deviating from the baseline only at the beginning of the peak period. Although it consumes less energy than the baseline during the peak, it consumes slightly more than upgrade 1 because it does not have preheating.

Figure 5. Verification of conditioned space temperature changes

![Image](93846_images/image_000006_237219a796170b95c283c7880a902ec35a40297ff8ae71239d18baa8505fdbb9.png)

Figure 6 shows the daily total heating energy consumption for the same period as the time-series data in Figure 5. The jaggedness of the heating consumption profile was not investigated because of scope limitations. Although the daily consumption values are all very close, upgrade 2 is usually the lowest (though not always) due to the lack of preheating and the offset during the peak. Interestingly, upgrade 1 is also frequently lower than the baseline despite the preheating period, which is twice as long as the peak period, and the equal offset in the other direction.

Figure 6. Validation of daily energy consumption in one building

![Image](93846_images/image_000007_10db1b29bf7776feccb0e8319ad0e975528394d7820b2a6d692c2bfcdc91a17f.png)

Figure 7 shows a more consistent pattern of which upgrade uses the most energy when we consider more buildings. The results show that upgrade 1 consumes more energy on average than the baseline, and upgrade 2 consumes less energy than the baseline; however, the single-building example shows that there are exceptions, from both day-to-day and building-to-building perspectives.

Figure 7. Validation of daily energy consumption in 13 buildings

![Image](93846_images/image_000008_3d2bc4c66e1a8bfb1a2e48c59565c0fbeafd4cf84475045a6c45fbd071788c3a.png)

