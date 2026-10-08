<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95004.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95004.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95004.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/95004.md | section: 5.3  Stock Utility Bill Impacts | lines: 504-550 -->
## 5.3  Stock Utility Bill Impacts

The PV 40% measure scenario demonstrates ~25% ($28-$37 billion USD, 2022) utility bill savings for the U.S. commercial building stock modeled in ComStock, depending on the electricity rate structure (Figure 3). This report reviews utility bill results for the maximum, mean, and minimum electricity rate structures available for each building. Bill savings are solely due to reducing purchased grid electricity by using generated on-site PV electricity. This bill analysis does not consider excess PV electricity sent back to the grid. However, excess PV generation is reported in the ComStock public dataset if users want to include it in their analysis. For example, users could assume and apply some $/kWh for electricity sold back to the grid. Doing so would increase bill savings further. Utility bills from on-site combustion of fossil fuels do not change across scenarios because they are unaffected by PV generation.

Figure 3. Annual utility bill impacts using the maximum, mean, and minimum bills across available rate structures for buildings for the PV 40% measure scenario

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95004.yaml
     source: 95004_images/image_000005_ecaa3ed6ea8084255f6b06d30e39801b1886aef8a6f89b8522736e6dd00027cb.png
     method: vision-description
     described: 2026-08-20 -->

![Three-panel stacked bar chart of annual utility bill by fuel under maximum, mean, and minimum electricity rates, Baseline vs PV 40%](95004_images/image_000005_ecaa3ed6ea8084255f6b06d30e39801b1886aef8a6f89b8522736e6dd00027cb.png)

Figure 3. Three-panel stacked bar chart of annual utility bill (Billion USD, 2022), y-axis 0 to about 150, under three electricity-rate assumptions (With Max, Mean, and Min Electricity Rate). Each panel has two bars (Baseline, Add_PV_40pct) stacked by fuel per the legend (Electricity, Natural Gas, Propane, Fuel Oil). Max rate: Baseline 144 (Electricity 125, Natural Gas 17) vs PV 107, a 26% reduction (Electricity 88, Natural Gas 17). Mean rate: Baseline 127 (Electricity 108, Natural Gas 17) vs PV 95, a 25% reduction (Electricity 76). Min rate: Baseline 112 (Electricity 93, Natural Gas 17) vs PV 84, a 25% reduction (Electricity 65). Natural gas cost is unchanged at 17 across scenarios; the roughly 25% total bill savings comes entirely from reduced electricity purchases, matching the about 25% ($28-$37 billion, 2022) savings cited in the summary.

Figure 4 shows the distribution of utility bill savings for all ComStock models across fuel types. The median building shows over 20% total bill savings using the mean electricity bill. This is solely due to reductions in purchased electricity. One notable factor for percentage of total bill savings is the prevalence of on-site combustion fuels, which are not reduced by adding PV. Buildings with higher gas bills will generally experience smaller total percentage bill savings from PV. Some buildings (mostly outliers in the distribution) show negative electricity bill savings (increased bills) when adding PV. This is primarily caused by ComStock's current electric utility rate selection scheme. ComStock selects applicable rates from the URDB, sometimes based on demand limits. Adding PV sometimes reduces these demand limits, which can change the included rates for a building. Therefore, these bill increases are generally caused by differences in the included electric utilities for a model, rather than a real increase in any single bill.

Figure 4 shows a small number of outliers in the distribution with changes to combustion fuel bills. This is caused by a bug in the ComStock model generation workflow where window blinds are sometimes not applied consistently between the baseline model and corresponding measure scenario model. The overall impact on the results is negligible, but users should be aware that they may find some instances of this unexpected behavior when using the ComStock public dataset until this issue is resolved in future work.

Figure 4. Percent annual utility bill savings distribution for ComStock models with PV 40% measure scenario by fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95004.yaml
     source: 95004_images/image_000006_871cca580f73440d87bf93ca8f39cbdbb7517409aea9cd8172f5504392a9327a.png
     method: vision-description
     described: 2026-08-20 -->

![Violin and box plots of percent utility bill savings by fuel type across the modeled stock](95004_images/image_000006_871cca580f73440d87bf93ca8f39cbdbb7517409aea9cd8172f5504392a9327a.png)

Figure 4. Horizontal violin-plus-box plots of Percent Utility Bill Savings by Fuel (%), x-axis about -160% to 100%, titled 'Upgrade 41.0: Add_PV_40pct (unweighted)'. Rows (with model counts): Propane Bill State Average (n=102), Fuel Oil Bill State Average (n=65), Natural Gas Bill State Average (n=5420), Electricity Bill with Mean Rate (n=124059), and Bill Mean (n=124077). The fossil-fuel rows cluster tightly at 0% (PV does not change gas/propane/oil bills). The Electricity Bill and overall Bill Mean distributions center around 25-35% savings with the interquartile box on the positive side, but have long left tails reaching below -100%, indicating a minority of building/rate combinations where PV increases the net bill. Median bill savings exceed 20%, consistent with the summary.

Results shown in this plot are the savings for the average available utility rate per building. The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of unweighted ComStock models that were applicable for energy savings for the fuel type category.

Figure 5 shows the percentage of total utility bill savings by climate zone, based on the mean electric rate. Warmer climates generally exhibit greater savings due to higher solar resource availability and a larger share of electric end uses that PV can offset (e.g., more cooling and electric heating, less gas heating). Outliers with increased utility bills are caused by the same factors discussed in Figure 4.

Figure 5. Percent annual utility bill savings distribution for ComStock models with PV 40% measure scenario by climate zone

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95004.yaml
     source: 95004_images/image_000007_6a9047489663583aa44b044d1323e3c79de8ad3e048c9fc70dc5593fac2ae4d3.png
     method: vision-description
     described: 2026-08-20 -->

![Violin and box plots of percent utility bill savings by ASHRAE climate zone across the modeled stock](95004_images/image_000007_6a9047489663583aa44b044d1323e3c79de8ad3e048c9fc70dc5593fac2ae4d3.png)

Figure 5. Horizontal violin-plus-box plots of Percent Utility Bill Savings by Climate (%), x-axis about -100% to 90%. Rows are ASHRAE climate zones with model counts: 1A (n=3053), 2A (n=6593), 2B (n=3706), 3A (n=12963), 3B (n=15905), 3C (n=5290), 4A (n=19672), 4B (n=5228), 4C (n=1870), 5A (n=18539), 5B (n=9311), 6A (n=10385), 6B (n=4247), 7 (n=6651), and 8 (n=650). Most zones center around 20-40% bill savings; sunnier, cooling-dominated dry zones (2B, 3B, 4B, 5B) skew toward the higher end, while every zone shows a long negative tail for a minority of buildings. Confirms PV bill savings are positive across all U.S. climates with regional spread.

Results shown in this plot are the savings for the average available utility rate per building. The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of unweighted ComStock models that were applicable for energy savings for the fuel type category.

