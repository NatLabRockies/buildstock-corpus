<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89340.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89340.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89340.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/89340.md | section: 5.2.2 Monthly Quartile Statistics Distribution of Daily Peak Reduction | lines: 486-515 -->
## 5.2.2 Monthly Quartile Statistics Distribution of Daily Peak Reduction

Figure 6 and Figure 7 show the percentage distributions of median and maximum daily peak load reductions, respectively, by month for the default scenario compared to the baseline model.

Figure 6. Distribution of the percentage of median daily peak load reduction by month compared to the baseline model for the default scenario

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89340.yaml
     source: 89340_images/image_000007_2601336e826ecef6cb6b6156dae61022978dcd064b882db54022206e91e5d65a.png
     method: vision-description
     described: 2026-08-20 -->

![Box plot by month of the percentage reduction in median daily peak load for the default scenario, with medians a few percent above zero, widest spread in June through August, and whiskers extending below zero in every month](89340_images/image_000007_2601336e826ecef6cb6b6156dae61022978dcd064b882db54022206e91e5d65a.png)

Figure 6 of the ComStock thermostat-control-for-load-shedding measure documentation shows the distribution of median daily peak load reduction by month for the default scenario relative to the baseline. Twelve box plots, January through December, are drawn on a y-axis of median peak savings in percent spanning -10% to +20%. Every month has a positive median, roughly 1% to 3%, and the interquartile boxes sit almost entirely above zero. The distributions widen through the cooling season: upper whiskers reach about 10% to 11% in January through April, rise to roughly 13% to 15% in May through August, peak in July at about 15.5%, then fall back toward 9% to 10% in November and December. Lower whiskers extend to roughly -5% to -6% in every month, so peak reduction is not guaranteed for an individual building on an individual day. The text attributes the negative tail to the fixed two-hour rebound-control length, which is not optimal for every building and weather combination, and notes larger variance for median statistics in summer and winter. Performance showed no correlation with floor area or heating fuel type.

Figure 7. Distribution of the percentage of maximum daily peak load reduction by month compared to the baseline model for the default scenario

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89340.yaml
     source: 89340_images/image_000008_d40f5e987448287276893c4b95adefdb2cc87c30a362caa4a994c531287f6e16.png
     method: vision-description
     described: 2026-08-20 -->

![Box plot by month of the percentage reduction in maximum daily peak load for the default scenario, with medians near 1 to 4 percent, upper whiskers near 15 to 18 percent in the cooling season, and lower whiskers reaching about minus 10 percent](89340_images/image_000008_d40f5e987448287276893c4b95adefdb2cc87c30a362caa4a994c531287f6e16.png)

Figure 7 of the ComStock thermostat-control-for-load-shedding measure documentation shows the distribution of maximum daily peak load reduction by month for the default scenario relative to the baseline. Twelve box plots, January through December, are drawn on a y-axis of maximum peak savings in percent spanning -10% to +20%. Medians are positive in every month, roughly 1% in the winter months and rising to roughly 3% to 4% from April through October. Interquartile boxes reach about 6% to 8% at the third quartile in the warmer months. Upper whiskers run about 14% to 16% in January through March and about 16% to 18% from April through October, so the best-case daily peak reduction is larger than the median-peak view of Figure 6. Lower whiskers extend to roughly -8% to -10% in most months, again showing that reduction is not guaranteed. Compared with Figure 6, the maximum-peak metric shows both higher upside and a deeper negative tail, consistent with the text's observation that the fixed two-hour rebound period is not tuned per building.

Both distributions of the statistics share a similar trend: a daily peak load reduction is not guaranteed with the upgrade, but there is an overall positive monthly reduction. The nonnegligible portion of the stock with negative peak reductions is mainly due to the uncertainty in rebound effects with fixed rebound control length (2 hours) for all applicable buildings; some rebound effects are too strong to mitigate in 2 hours or the peak window ends too early for rebound control to take effect. Therefore, rebound control could and should be tuned for specific building models (in future work), as the impact of rebound effects is highly dependent on building properties and weather conditions. The larger variances for median statistics in summer and winter are contributed due to a similar reason, where rebound effects are typically stronger in summer and winter when the highest and lowest temperatures occur.

There is no obvious correlation between building size (floor area) and measure performance, or between heating system (fuel) type (electric or non-electric heating) and measure performance.

