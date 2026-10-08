<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89126.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/89126.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/89126.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/89126.md | section: 5.4 Stock Utility Bill Impact | lines: 584-630 -->
## 5.4 Stock Utility Bill Impact

This section includes a comparison of national-level annual utility bills of the stock across different fuel sources (i.e., electricity, natural gas, propane, fuel oil). ComStock uses utility region mapping to determine all associated electricity rates that can be used by a building in that region. Therefore, the results can include many annual utility rates per building. The comparison in this section highlights three statistics (i.e., maximum, mean, and minimum) across all possible electric utility rates in a given location. For more information about the utility bill methodology in ComStock, see the ComStock Reference Documentation [2].

When combining all fuel types, Package 3 resulted in $7 billion to $9 billion nationally of utility bills savings (5% -8% reduction) depending on the electricity rate used (Figure 6). Natural gas bills are reduced by $10 billion (59%) as a result of fuel switching much of the heating end use. The natural gas rates used are fixed by state and therefore remain constant across all three scenarios shown.

Electricity rates are determined based on the utility region of each building in the dataset. Some utilities can have multiple rates; therefore, only the minimum, mean, and maximum rates are shown in the figure. For Package 3, the mean electricity rate showed a $2 billion increase in electricity bills nationally.

Compared to Package 2, the higher performance HP-RTU package, Package 3 demonstrates the same reduction in natural gas bills. However, Package 2 demonstrates no change or a slight reduction in electricity bills, while Package 3 results in $2 billion to $3 billion higher electricity bills nationally. This is due to the lower cooling savings and higher electric heating penalty compared to Package 2.

Figure 6. National annual utility bills comparison of the ComStock baseline, LED Lighting + HPRTU + ASHP Boiler (Package 2), and LED Lighting + HP-RTU Standard Performance + ASHP Boiler (Package 3)

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89126.yaml
     source: 89126_images/image_000008_7f12025aefcf37a78c778590b1a65e3a3e1e8dfdc004aea5ba1f33589faa4745.png
     method: vision-description
     described: 2026-08-20 -->

![Three-panel stacked bar chart of national annual utility bills under maximum, mean, and minimum electricity rates, Baseline vs Package 2 vs Package 3](89126_images/image_000008_7f12025aefcf37a78c778590b1a65e3a3e1e8dfdc004aea5ba1f33589faa4745.png)

Figure 6. Three-panel stacked bar chart of Annual Utility Bill (Billion USD, 2022), y-axis 0 to about 150, under three electricity-rate assumptions. Each panel has three bars (Baseline, Package 2, Package 3) stacked by fuel (Electricity, Natural Gas, Fuel Oil, Propane). With Max Electricity Rate: Baseline 143 (Electricity 123, Natural Gas 17), Package 2 132 (-7%), Package 3 136 (-5%). With Mean Rate: Baseline 124 (Electricity 104, NG 17), Package 2 113 (-9%), Package 3 116 (-6%). With Min Rate: Baseline 110 (Electricity 90, NG 17), Package 2 99 (-10%), Package 3 101 (-8%). Natural gas cost falls sharply relative to its baseline share as heating is fuel-switched; total bill savings are 5-10% depending on rate.

When evaluating utility bills savings distributions, there is not much correlation between total utility bills savings and building type (Figure 7). For most building types, the median utility bill is reduced by approximately 5% -10%, with the 75th percentile (the right whisker) reaching 15% -20% bill savings in some building types. The bottom 25% of buildings (the left whisker) can see bill increases in most building types, which are predominantly buildings that had large natural gas heating loads in the baseline that are now electric, resulting in high electricity bills.

Figure 7. Percentage utility bills savings distribution for ComStock models with the LED Lighting + HP-RTU Standard Performance + ASHP Boiler (Package 3) applied by building type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89126.yaml
     source: 89126_images/image_000009_e6a8296e74dc39f9b8e9bb57c0234e20d8ec3a7d5f9783ac3bad35cf751fe502.png
     method: vision-description
     described: 2026-08-20 -->

![Violin and box plots of percent utility bill savings by building type across the modeled stock for Package 3](89126_images/image_000009_e6a8296e74dc39f9b8e9bb57c0234e20d8ec3a7d5f9783ac3bad35cf751fe502.png)

Figure 7. Horizontal violin-plus-box plots of Percent Utility Bill Savings by Building Type (%), x-axis about -100% to 80%, titled 'Upgrade 36.0: Package 3 (unweighted)'. Rows are ComStock building types with model counts: FullServiceRestaurant (n=10615), Hospital (n=1727), LargeHotel (n=7939), LargeOffice (n=6410), MediumOffice (n=13950), Outpatient (n=7389), PrimarySchool (n=6586), QuickServiceRestaurant (n=5049), RetailStandalone (n=15963), RetailStripmall (n=13613), SecondarySchool (n=9236), SmallHotel (n=3476), SmallOffice (n=18124), and Warehouse (n=15369). Most types center on small positive median bill savings (roughly 0-10%) with long tails in both directions; a minority of models show bill increases where electrified heating raises electricity cost.

When evaluating utility bill savings by fuel type (Figure 8), we see that natural gas and propane bills show the highest reduction in bills, with up to 90% savings in the 75th percentile of buildings. Fuel oil shows negative bill savings; however, this is likely because buildings with fuel oil heating did not apply to either of the heat pump measures. Therefore, buildings with changes in fuel oil consumption likely only had the LED lighting measure applied, causing slight increases in winter heating requirements with higher efficiency lighting. The electricity bill shows savings in some buildings, and an increase in others. This is heavily dependent on the baseline HVAC system and heating fuel type; buildings that started with electric resistance heating and had it replaced by a more efficient heat pump see electricity bill savings, whereas buildings whose heating fuel switched to electric will see higher electricity bills. The total bill when using the mean electricity rate for each building saw 0% -10% savings in a majority of buildings.

Figure 8. Percentage utility bills savings distribution for ComStock models with the LED Lighting + HP-RTU Standard Performance + ASHP Boiler (Package 3) applied by fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89126.yaml
     source: 89126_images/image_000010_7d06d2d35035fb3169e46a7568a8bace469b268a0e481fdf778113c44542313a.png
     method: vision-description
     described: 2026-08-20 -->

![Violin and box plots of percent utility bill savings by fuel type across the modeled stock for Package 3](89126_images/image_000010_7d06d2d35035fb3169e46a7568a8bace469b268a0e481fdf778113c44542313a.png)

Figure 8. Horizontal violin-plus-box plots of Percent Utility Bill Savings by Fuel (%), x-axis about -160% to 100%, titled 'Upgrade 36.0: Package 3 (unweighted)'. Rows with model counts: Propane Bill (n=7999), Fuel Oil Bill (n=6588), Natural Gas Bill (n=54995), Electricity Bill with Mean Rate (n=135455), and Total Bill with Mean Electricity Rate (n=135446). Natural gas, propane, and fuel oil bills show large positive savings distributions (fuel switching eliminates much fossil use), the Electricity Bill is roughly centered near 0% with a slight negative skew (added electric heating), and the Total Bill is modestly positive. Consistent with the reported ~59% national natural gas bill reduction.

