<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89343.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89343.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89343.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/89343.md | section: 4.1  Uncertainty in Peak Prediction and Impact on Load Shed Strategy | lines: 409-436 -->
## 4.1  Uncertainty in Peak Prediction and Impact on Load Shed Strategy

Figure 3 shows load profiles from five consecutive days comparing the same single building model with the baseline scenario and with the load shedding measure applied with either the perfect prediction or bin-sampling method for load prediction. The perfect and bin-sampling methods show accordance in the first three days, but the bin-sampling method mis-predicts the time of peak load (much earlier than the actual peak in the baseline) and thus fails to shed peak load in the last two days. This is because the load profiles bin assignment by the bin-sampling method for the last two days are not representative of the true load profiles due to conditions that are not captured in the method (i.e., conditions other than outdoor temperature). The influence of these other conditions on load shape binning is generally trivial during summer and winter seasons when outdoor temperature characteristics are monotonous and their impact on building load dominates other weather factors such as solar radiation and cloud cover. However, the importance of other conditions increases during shoulder seasons when weather conditions are more random or fluctuating and are affected by multiple factors.

Figure 3. Load profile comparison for baseline and load shedding with the perfect prediction and bin-sampling options

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89343.yaml
     source: 89343_images/image_000004_695c75db8de7dace978c3158ac0a632083834a6247482ccc73c50423e3fe14da.png
     method: vision-description
     described: 2026-08-20 -->

![Line chart of hourly load over five days comparing Baseline, Perfect Prediction, and Bin-sampling load-shedding options](89343_images/image_000004_695c75db8de7dace978c3158ac0a632083834a6247482ccc73c50423e3fe14da.png)

Figure 3. Line chart of hourly electricity load (kWh) for one building over five consecutive days (9/24-9/28), y-axis 50 to 250. Three series: Baseline (blue dashed), Perfect Prediction (red), and Bin-sampling (yellow), each daily peak near 175-190 kWh. The perfect-prediction and bin-sampling load-shedding curves agree with each other for the first three days, but on 9/27 and 9/28 the bin-sampling method mispredicts the peak timing and shape while perfect prediction continues to track and shed the true peak.

Figure 4 and Figure 5 show load profiles for five consecutive days comparing the load shedding measure applied with the fixed schedule and OAT-based prediction options, respectively. Neither option is capable of capturing the load peak for the days shown. The assumed peak window (6-10 p.m. for the example model in climate zone 3A) in the fixed schedule option completely misses the actual peak period, which means the universal peak times derived for representative buildings are inconsistent with the actual building load profiles. The OAT-based option fails to predict the time of peak load except for the fourth day (9/27), indicating a high failure ratio for predicting peak time correctly, possibly due to non-negligible factors other than OAT affecting building load.

Figure 5. Load profile comparison for baseline and load shedding with perfect prediction and OAT-based prediction approaches

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89343.yaml
     source: 89343_images/image_000005_db5a0d2298c901c74744a8cf0fe1f3f96bb107fb6708908db9b6b5c16132073e.png
     method: vision-description
     described: 2026-08-20 -->

![Two stacked line charts of hourly load over five days: Figure 4 (fixed schedule) above Figure 5 (OAT-based prediction)](89343_images/image_000005_db5a0d2298c901c74744a8cf0fe1f3f96bb107fb6708908db9b6b5c16132073e.png)

Figures 4 and 5, stacked in one image. Both are line charts of hourly electricity load (kWh) for one building over five consecutive days (9/24-9/28), y-axis 50 to 250, daily peaks near 175-190 kWh. Top (Figure 4) compares Baseline (blue dashed), Perfect Prediction (red), and Fixed Schedule (yellow). Bottom (Figure 5) compares Baseline (blue dashed), Perfect Prediction (red), and OAT-based Prediction (yellow). In both, perfect prediction tracks and reduces the true baseline peak, while the fixed-schedule and OAT-based options largely fail to capture the actual peak timing, leaving load spikes unshed on most days.

