<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_Dim Lighting During Peak Hours.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/3b69decb4e5f7bb3d6cc24f6224b318c921fd45f/assets/files/ComStock%20Measure%20Doc_Dim%20Lighting%20During%20Peak%20Hours.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_Dim%20Lighting%20During%20Peak%20Hours.pdf | corpus_version: e7ffee7a | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_Dim Lighting During Peak Hours.md | section: 5.2. Demand Flexibility Performance | lines: 313-346 -->
## 5.2. Demand Flexibility Performance

The simulation for the 10k samples is used to demonstrate the aggregated results. Figure 5 illustrates a daily lighting electricity load for each season to show that the load was reduced during the corresponding peak period. The peak periods do not necessarily coincide with the simulated peaks from ComStock, because they were identified from the projected grid-side net load shape including sectors other than commercial buildings. Besides, there can also be a gap between the ComStock baseline load shape and the real load shape from the utility AMI data [10]

Figure 5. Aggregated lighting electricity load profile for California for an example day in winter, summer and intermediate season

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Dim Lighting During Peak Hours.yaml
     source: ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000005_df7a4d58b8966e560bbfe77ca83d0a1930ae4c2962a4ff303a6a7c01517259f3.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 5: aggregated California lighting load profiles for a winter, summer and intermediate day, baseline vs measure](ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000005_df7a4d58b8966e560bbfe77ca83d0a1930ae4c2962a4ff303a6a7c01517259f3.png)

Figure 5: three stacked line panels (winter, summer, intermediate) of aggregated lighting
electricity in MWh (y, about 200,000 to 700,000) over one example day for California. Baseline
(blue) and post-measure (orange) overlap until about hour 17, where the post-measure profile
drops sharply for the 4-hour shed window and rebounds to the baseline at about hour 21.

For each day the measure is applied, a D3 value (percentage decrease) for the lighting end use is calculated, and the distribution of the daily D3 values for each state is illustrated in Figure 6 for the 10k samples, sorted by the 75 th percentile, which is used to represent the demand flexibility potential of the measure in DR-Path. The difference of D3 across states is mainly attributed to the different fraction of unoccupied spaces (such as warehouses) and inapplicable spaces (such as operation rooms) within each state.

Figure 6. Distribution of daily percentage lighting load reduction during the peak period for each state

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Dim Lighting During Peak Hours.yaml
     source: ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000006_12d0d4c8f67c44866e01f09e41a0d3fea74af9eee471619758eade06b0c0be4c.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 6: box plot by state of daily percentage lighting load reduction during the peak period](ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000006_12d0d4c8f67c44866e01f09e41a0d3fea74af9eee471619758eade06b0c0be4c.png)

Figure 6: box plot of daily percentage lighting load reduction during the peak period (y, 0 to
40%) for each state (x), with the median as a dashed line and the 75th percentile marked in red.
Reductions cluster between about 30 and 37% for most states; KS is highest near 40% and the
right-hand states trend toward 30%.

