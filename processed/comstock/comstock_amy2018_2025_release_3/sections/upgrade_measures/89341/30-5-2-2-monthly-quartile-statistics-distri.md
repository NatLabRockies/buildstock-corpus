<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89341.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89341.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89341.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/89341.md | section: 5.2.2 Monthly Quartile Statistics Distribution of Daily Peak Reduction | lines: 417-446 -->
## 5.2.2 Monthly Quartile Statistics Distribution of Daily Peak Reduction

Figure 4 and Figure 5 show the percentage distributions of median and maximum daily peak load reductions, respectively, by month for the default scenario compared to the baseline model.

Figure 4. Distribution of the percentage of median daily peak load reduction by month compared to the baseline model for the default scenario

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89341.yaml
     source: 89341_images/image_000006_144c1dc14e7ff87555850ce71a1b67a67e29dc135d2c5c4fad1d73a6a2a3e90f.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 4. Box plots by month of the percentage of median daily peak load reduction for the default load shift scenario relative to the baseline, on a y-axis from -3% to 4%](89341_images/image_000006_144c1dc14e7ff87555850ce71a1b67a67e29dc135d2c5c4fad1d73a6a2a3e90f.png)

Monthly box plot distribution of median daily peak load savings for the default load shift scenario, across all applicable large office models. The x-axis is the month, January through December, and the y-axis is Median Peak savings [%] from -3.0% to 4.0% with a reference line at zero. The winter and late-autumn months (January, February, March, November, December) are very tight, with boxes only a few tenths of a percent wide and medians slightly above zero. Spread grows through the shoulder months and is widest in the cooling season: May through September have boxes roughly spanning 0% to 1.3% with whiskers reaching about +3% and down to about -2%. July shows the largest interquartile range and August the deepest negative whisker. The overall picture is a small but positive median peak reduction concentrated in the cooling season, with a non-negligible share of models experiencing peak increases. Per the accompanying discussion, those negative cases arise when pre-cooling itself creates a new peak in setpoint-sensitive buildings, which would need smaller setpoint offsets and longer pre-conditioning windows; parameters therefore need per-model tuning. No clear correlation was found with heating fuel type.

Figure 5. Distribution of the percentage of maximum daily peak load reduction by month compared to the baseline model for the default scenario

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89341.yaml
     source: 89341_images/image_000007_a583e8f69883a83099bbcf5b98170691751514c18c89442c1e3a4afb1bc503ac.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 5. Box plots by month of the percentage of maximum daily peak load reduction for the default load shift scenario relative to the baseline, on a y-axis from -3% to 4%](89341_images/image_000007_a583e8f69883a83099bbcf5b98170691751514c18c89442c1e3a4afb1bc503ac.png)

Monthly box plot distribution of maximum daily peak load savings for the default load shift scenario, the companion to the median-peak view. The x-axis is the month, January through December, and the y-axis is Max Peak savings [%] from -3.0% to 4.0% with a zero reference line. The seasonal shape matches the median-peak chart but with wider tails: January through March and November through December sit tightly just above zero, while May through October open up substantially. June, July and August carry the widest boxes, roughly 0% to 1.5%, with upper whiskers reaching about +3.3% and lower whiskers down to about -2.2%; August has the most negative tail and October still shows a box reaching about +1.1%. Because this statistic tracks the worst-case day in each month rather than the typical day, the negative tails are the important read: peak reduction is not guaranteed, and the same pre-cooling that lowers most daily peaks can raise the monthly maximum in some models. Both this and the median view support the conclusion that overall monthly reductions are positive but modest and concentrated in cooling season.

Both distributions of the statistics share a similar trend: a daily peak load reduction is not guaranteed with the upgrade, but there is an overall positive monthly reduction especially for cooling seasons. The non-negligible portion of the stock with negative peak reductions is mainly due to the variability in peak load increases from pre-cooling. Building loads that are sensitive to setpoint change for pre-conditioning would require smaller setpoint adjustments and longer preconditioning lengths to avoid generating higher peak load in the pre-peak period than the original (unshifted) peak. Therefore, load shifting parameters need to be tuned for specific building models.

There is no obvious correlation between heating system (fuel) type (electric or non-electric heating) and the measure performance.

