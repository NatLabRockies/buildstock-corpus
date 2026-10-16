<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_PV with Roof Insulation.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/2036a73dc9b7a5dccb8b62fe835cdcbc777175fa/assets/files/ComStock%20Measure%20Doc_PV%20with%20Roof%20Insulation.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_PV%20with%20Roof%20Insulation.pdf | corpus_version: comstock_amy2018_2025_release_3-v3 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_PV with Roof Insulation.md | section: 4.4  Utility Bill Savings Distributions | lines: 459-501 -->
## 4.4  Utility Bill Savings Distributions

Figure 5 shows the distribution of utility bill savings for all ComStock models across fuel types. The median building shows approximately 30% total bill savings using the mean electricity bill. This is due to reductions in purchased electricity, as well as reduced overall energy consumption due to the increased roof insulation. Electricity bills are reduced by 30% or more in most buildings.

Electricity is the only fuel whose bills are affected by PV generation. Energy from on-site combustion fuels (natural gas, propane, fuel oil) cannot be offset by PV, therefore bill savings for these fuels are solely attributable to the increased roof insulation. Median savings for combustion fuel bills are in the range of 5% -10% due to the added roof insulation reducing heating loads. The results show a small number of outliers in the distribution with negative combustion fuel savings. After investigation, most instances of negative natural gas bill savings occur in warehouses. Although rare, it is possible that the added roof insulation reduced beneficial solar heat gains in winter, leading to increased HVAC system runtime or cycling. This effect is plausible in warehouses, which typically have low internal gains and are therefore sensitive to internal gain fluctuation.

Some buildings (mostly outliers in the distribution) show negative electricity bill savings (increased bills) when adding PV and the increased roof insulation. This is primarily caused by ComStock's current electric utility rate selection scheme. ComStock selects applicable rates from the URDB, sometimes based on demand limits. Adding PV sometimes reduces these demand limits, which can change the included rates for a building. Therefore, these bill increases are generally caused by differences in the applicable electric rate structures or charges for a model, rather than a real increase in any single bill.

Figure 5. Percent annual utility bill savings distribution for ComStock models with the PV 40% + Roof Insulation measure scenario by fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_PV with Roof Insulation.yaml
     source: ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000005_cce74eced9d2a6d3283836452852af2824b503d0ab1ab99b55efe490e7dbd9bc.png
     method: vision-description
     described: 2026-10-16 -->

![Figure 5: violin and box plots of percent annual utility bill savings by fuel type for Package_12 (unweighted)](ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000005_cce74eced9d2a6d3283836452852af2824b503d0ab1ab99b55efe490e7dbd9bc.png)

Figure 5: horizontal violin plots with inset box plots of percent annual utility bill savings
(x, -160 to 100) for the package, one row per bill: propane state average (n=3,383), fuel oil state
average (n=1,486), natural gas state average (n=60,495), electricity with mean rate (n=124,410)
and bill mean (n=124,424). Electricity and total-bill medians sit near 30% to 35%; fuel bills near
5% to 10%, with long negative tails. See Table 9.

Results shown in this plot are the savings for the average available utility rate per building. The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of unweighted ComStock models that were applicable for energy savings for the fuel type category.

Figure 6 shows the distribution of total utility bill savings by climate zone, based on the mean electric rate. Warmer climates generally exhibit greater savings due to higher solar resource availability and a larger share of electric end uses that PV can offset (e.g., more cooling and electric heating, less gas heating). Outliers with increased utility bills are caused by the same factors discussed in Figure 5.

Figure 6. Percent annual utility bill savings distribution for ComStock models with PV-40% + Roof Insulation measure scenario by climate zone

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_PV with Roof Insulation.yaml
     source: ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000006_3d8c581165937f1795693d8820fab71f381c9e386b2d2fea60f998a806a81610.png
     method: vision-description
     described: 2026-10-16 -->

![Figure 6: violin and box plots of percent annual utility bill savings by ASHRAE climate zone for Package_12](ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000006_3d8c581165937f1795693d8820fab71f381c9e386b2d2fea60f998a806a81610.png)

Figure 6: horizontal violin plots with inset box plots of percent annual utility bill savings
(x, -100 to 80) for the package, one row per ASHRAE climate zone from 1A to 8 with model counts
(n=669 in zone 8 to n=19,709 in 4A). Medians fall between about 20% and 40%, highest in the hot
zones 2A, 2B and 3B and lowest in the cold zones 6A, 7 and 8. Distributions skew negative.

Results shown in this plot are the savings for the average available utility rate per building. The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of unweighted ComStock models that were applicable for energy savings for the fuel type category.

