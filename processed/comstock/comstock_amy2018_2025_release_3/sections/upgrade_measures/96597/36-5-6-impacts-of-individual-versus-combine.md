<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/96597.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96597.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96597.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/96597.md | section: 5.6  Impacts of Individual Versus Combined Controls | lines: 674-722 -->
## 5.6  Impacts of Individual Versus Combined Controls

While developing and testing this measure, we wanted to understand the impacts of daylighting controls and occupancy sensors individually before combining them together into the 'Lighting Controls' measure. We ran a medium-scale test run (~13,000 models) with three measure scenarios:

1. Only Daylighting Controls
2. Only Occupancy Controls
3. Lighting Controls (Daylighting Controls + Occupancy Controls).

This testing can help us understand which lighting control technology has the largest impact on energy savings, as well as looking further into which buildings benefit more from one technology or the other. When evaluating site energy savings at the stock level in Figure 7, the Daylighting Controls measure saved 0.7% (35 TBtu), the Occupancy Controls measure saved 1.2% (60 TBtu), and the Lighting Controls measure saved 1.8% (89 TBtu). Based on these results, we can conclude that the occupancy sensors are saving more energy at the stock than the daylighting controls. However, this may not be the case in every single building, which we will investigate further in this section. The Lighting Controls savings of 89 TBtu are less than the sum of the two individual control measures (35 + 60 = 95 TBtu), indicating that there is some interaction between the controls. For example, the occupancy sensor LPD reduction is less impactful during periods when the daylighting controls are also in effect because the LPD would be zero during those timesteps if the lights have been turned off. Therefore, we cannot expect that the savings for the Lighting Controls measure will be the same or higher than the sum of the individual control measures.

Figure 7. Comparison of annual site energy consumption between the ComStock baseline, Daylighting Controls, Occupancy Controls, and Lighting Controls measure scenarios

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/96597.yaml
     source: 96597_images/image_000008_be6a335227d8c03bf7ccf88e027f3511de7f088c3dff05ca9197009e058e8370.png
     method: vision-description
     described: 2026-08-20 -->

![Stacked column chart of annual stock site energy consumption for four scenarios: Baseline, Daylighting Controls, Occupancy Controls, and combined Lighting Controls](96597_images/image_000008_be6a335227d8c03bf7ccf88e027f3511de7f088c3dff05ca9197009e058e8370.png)

Figure 7. Stacked column chart of annual stock site energy consumption (TBtu), y-axis 0 to about 5000, comparing four scenarios: ComStock Baseline (total 4926), Daylighting Controls (4891), Occupancy Controls (4866), and combined Lighting Controls (4837). Columns are segmented by end use and fuel per the legend. The Interior Lighting Electricity segment falls progressively across the scenarios (about 435.3, 395.7, 361.9, 329.3), while Interior Equipment Electricity (750.9) is unchanged and Heating Natural Gas rises slightly (about 263.8 to 271.0) as a take-back. Shows the combined Lighting Controls scenario delivers the largest site energy reduction, roughly the sum of the daylighting-only and occupancy-only savings. (Dense stacked segments; flag for QA.)

When comparing the impacts on utility bills (Figure 8), we see that across all three electricity rate scenarios, the daylighting controls are saving $1 billion, the occupancy controls are saving $2 billion, and the combined lighting controls measure is saving $3 billion. The numbers in this figure are rounded to the nearest billion dollars, so some precision is lost. However, we can conclude that the occupancy sensors are contributing more to bill savings than daylighting controls at the stock level.

Figure 8. Comparison of annual utility bills between the ComStock baseline, Daylighting Controls, Occupancy Controls, and Lighting Controls measure scenarios

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/96597.yaml
     source: 96597_images/image_000009_ff43d27bc5250bd7bea08c9360a2b88fedb6a0fa4e58c2d0a9a32c94cb2283fb.png
     method: vision-description
     described: 2026-08-20 -->

![Grouped stacked bar chart of annual utility bills for four scenarios under maximum, mean, and minimum electricity rates](96597_images/image_000009_ff43d27bc5250bd7bea08c9360a2b88fedb6a0fa4e58c2d0a9a32c94cb2283fb.png)

Figure 8. Three-panel grouped stacked bar chart of annual utility bill (Billion USD, 2022), y-axis 0 to about 150, under three electricity-rate assumptions (With Max, Mean, Min Electricity Rate). Each panel has four bars (Baseline, Daylighting Controls, Occupancy Controls, Lighting Controls) stacked by fuel (Electricity, Natural Gas, Propane, Fuel Oil). Bills decline modestly from Baseline to the combined Lighting Controls scenario in every panel (roughly: Max about 149 to 141, Mean about 128 to 125, Min about 113 to 110), a low-single-digit percent reduction driven by electricity, with natural gas near 18 unchanged. The combined controls give the largest savings. (Small/dense labels; the exact per-scenario values are the least-certain reads in this doc -- flag for QA.)

Figure 9 shows both the median percent lighting energy savings and absolute lighting energy savings by building type and lighting control type. From this plot we can see that warehouses demonstrate the highest lighting energy savings (48%) when both daylighting and occupancy controls are applied. We can also see that the occupancy controls are contributing much more of the savings in warehouses then daylighting. This is because warehouses typically have a lot of unoccupied floor space that could benefit from occupancy sensors, but they also do not have large window-to-wall ratios, so it is difficult to get enough natural light for daylighting sensors to be effective. When looking at the absolute lighting energy savings on the right side of the plot, we can see that warehouses contribute by far the most to the stock lighting energy savings from this measure. Warehouses make up a large amount of square footage in the stock, therefore there is a lot of potential for reducing lighting energy in this building type.

One could do a similar analysis for each of the other building types to make conclusions about which lighting controls technology is most effective in determining how much lighting energy savings potential it has in the building stock. In all building types except offices, hospitals, large hotels, and stand-alone retail, occupancy controls are saving more energy than the daylighting controls. This outcome is influenced by many factors, including the presence of existing controls, occupancy sensor LPD reductions defined by ASHRAE 90.1-2019, compliance with daylighting controls criteria, and more.

Figure 9. Median percent lighting energy savings and absolute lighting energy savings by building type and lighting control type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/96597.yaml
     source: 96597_images/image_000010_d0823e4e9e884733772ed84e38599bd578e70909b08a0edf78b0b6f7eb192324.png
     method: vision-description
     described: 2026-08-20 -->

![Two-panel grouped horizontal bar chart of median percent and absolute interior lighting energy savings by building type and control type](96597_images/image_000010_d0823e4e9e884733772ed84e38599bd578e70909b08a0edf78b0b6f7eb192324.png)

Figure 9. Two-panel grouped horizontal bar chart of interior lighting energy savings by building type and control type. Left panel: Median Interior Lighting Energy Savings (%), x-axis 0 to about 50. Right panel: Absolute Interior Lighting Energy Savings (TBtu), x-axis 0 to about 40. Each building type has three bars: combined Lighting Controls (Daylighting + Occupancy), Occupancy Controls, and Daylighting Controls. Warehouse leads by a wide margin (combined 48.1% median / 37.6 TBtu, dominated by occupancy at 42.8% / 33.6 TBtu), followed by PrimarySchool (37.7% combined), SecondarySchool (33.9%), and Outpatient (20.3%); restaurants and hotels are lowest. For nearly all types occupancy controls contribute more than daylighting controls, and the combined measure is roughly additive.

