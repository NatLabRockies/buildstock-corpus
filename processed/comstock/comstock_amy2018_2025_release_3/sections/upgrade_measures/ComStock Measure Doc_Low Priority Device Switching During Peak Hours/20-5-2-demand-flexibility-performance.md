<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/2036a73dc9b7a5dccb8b62fe835cdcbc777175fa/assets/files/ComStock%20Measure%20Doc_Low%20Priority%20Device%20Switching%20During%20Peak%20Hours.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_Low%20Priority%20Device%20Switching%20During%20Peak%20Hours.pdf | corpus_version: comstock_amy2018_2025_release_3-v3 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.md | section: 5.2. Demand Flexibility Performance | lines: 267-298 -->
## 5.2. Demand Flexibility Performance

The simulation for the 10k samples is used to demonstrate the aggregated results. Figure 5 illustrates a daily electric equipment electricity load for each season to show that the load was reduced during the corresponding peak period. The peak periods do not necessarily coincide with the simulated peaks from ComStock, because they were identified from the projected grid-side net load shape including sectors other than commercial buildings. Besides, there can also be a gap between the ComStock baseline load shape and the real load shape from the utility AMI data For each day the measure is applied, a D3 value (percentage decrease) for the electric equipment end use is calculated, and the distribution of the daily D3 values for each state is illustrated in Figure 6 for the 10k samples, sorted by the 75 th percentile, which is used to represent the demand flexibility potential of the measure in DR-Path. The measure reduces electric equipment load by 20% but it only applies to office-like spaces. The ratio of applicable space types in each applicable building type is different. For example, only 5% of the floor area in small hotels and warehouses are applicable for the Plug Load measure, while 63% of primary schools is applicable. Among all applicable building types, SmallHotel, Warehouse, Hospital, and Outpatient have smaller ratios of applicable spaces. Among all applicable building types, by weighted sqft, DC only has 8% of these four building types with lower ratios, while WV has 42%, which leads to the D3 differences across states.

Figure 5. Aggregated electric equipment electricity load profile for California for an example day in winter, summer and intermediate season

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.yaml
     source: ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000005_ff5640d3cdb2a11560ac1a261cee2d531995d43c99841e5ad0e7745fb2bda408.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 5: aggregated California electric equipment load profiles for three seasons, baseline versus post-measure](ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000005_ff5640d3cdb2a11560ac1a261cee2d531995d43c99841e5ad0e7745fb2bda408.png)

Figure 5: three stacked line panels (winter, summer, intermediate) of aggregated electric
equipment electricity in MWh (y, about 250,000 to 950,000) over one example day for California.
Baseline (blue) and post-measure (orange) overlap until about hour 17, where the post-measure
profile steps down for the 4-hour shed window and rejoins the baseline at about hour 21.

Figure 6. Distribution of daily percentage electric equipment load reduction during the peak period for each state

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.yaml
     source: ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000006_33b521abd4e24c3577da3b586d71e7778662affc58577e64cab2e7163cb75198.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 6: box plot by state of daily percentage electric equipment load reduction during the peak period](ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000006_33b521abd4e24c3577da3b586d71e7778662affc58577e64cab2e7163cb75198.png)

Figure 6: box plot of daily percentage electric equipment load reduction during the peak period
(y, 0 to 14%) for each state (x), median as a dashed line and 75th percentile in red. DC is
highest near 14%, MA and NJ near 10%; most states fall between about 4 and 9%, declining toward
WV at the right.

