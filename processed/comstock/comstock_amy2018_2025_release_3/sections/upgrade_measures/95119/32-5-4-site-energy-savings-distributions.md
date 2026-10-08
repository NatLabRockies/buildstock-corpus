<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95119.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95119.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95119.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/95119.md | section: 5.4  Site Energy Savings Distributions | lines: 604-662 -->
## 5.4  Site Energy Savings Distributions

This section discusses site energy consumption for quality assurance/quality control purposes. Note that site energy savings can be useful for these purposes, but other factors should be considered when drawing conclusions, as they are not necessarily proportional to source energy savings or energy cost. When presenting the pairwise distribution of percentage savings, only samples that contain a non-zero value for the corresponding baseline ComStock model are included.

Figure 9 shows the annual percentage site energy savings broken down by end use and fuel type for the HP-RTU Lab Data measure scenario compared to the corresponding models in the ComStock baseline before the measure is applied. The highest savings are for combustion fuel heating, as these systems are replaced by electric heat pump systems. Many buildings save 100% of the energy for this combination of end use and fuel type. Buildings that save less than 100% include some systems that are not applicable to the HP-RTU measure scenario, such as gas unit heaters.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95119.yaml
     source: 95119_images/image_000010_6e491239132321355348fde3c709bffab49f3311a0e24dcb4b14e3cddfd836e9.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 9. Violin and box plot distribution of percent site energy savings by end use and fuel type for models with the HP-RTU lab data measure scenario applied](95119_images/image_000010_6e491239132321355348fde3c709bffab49f3311a0e24dcb4b14e3cddfd836e9.png)

Figure 9 is a horizontal violin plot with embedded box plots of per-model percent site energy savings by end use and fuel type, annotated "Upgrade 5.0: HPRTU_Lab_Data (unweighted)". The x-axis runs from about -160% to +100% with a reference line at 0%. Rows top to bottom, with model counts, grouped by fuel: Other Fuel -- Water Systems (n=119), Heating (n=3287); Natural Gas -- Water Systems (n=1541), Heating (n=16594); Electricity -- Water Systems (n=1690), Refrigeration (n=6028), Interior Equipment (n=27), Heating (n=14092), Heat Recovery (n=826), Fans (n=34342), Cooling (n=34289). The two combustion heating rows show the highest savings, with boxes roughly spanning 80%-100%, since those systems are replaced by electric heat pumps and many buildings save 100% of that fuel. Electricity Heating shows a wide positive box around 35%-70%. Electricity Fans centers around 10%-30% and Electricity Cooling around 5%-15%. Electricity Heat Recovery is the one clearly negative row, centered near -25% to -15%. Water systems, refrigeration, and interior equipment collapse to ticks at 0%. Points beyond the whiskers are outliers past 1.5 times the interquartile range; a few gas outliers show increased usage in buildings with small residual non-applicable gas systems.

Figure 9. Percent site energy savings distribution for ComStock models with applied measure scenario by end use and fuel type.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they lie outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category. Each data point represents the pairwise comparison between a ComStock baseline model and the corresponding model after the measure scenario is applied.

A few outliers show increased gas usage, mostly in buildings that still have some non-applicable gas systems and very small overall heating loads. In these cases, even minor changes in gas heating energy can lead to large fluctuations in percent savings. Figure A-2 in the Appendix shows the same plot using EUI savings instead of percentage savings, with no building showing a notable increase in gas use.

The electricity heating end use also shows savings in Figure 9, representing buildings with some electric resistance heating replaced with more efficient electric heat pump heating. However, it is important to note that this does not include buildings that start with no electric heating. Buildings that did not have electric heating in the baseline are not shown because the percent savings calculation would be invalid from a starting point of 0. These buildings result in increased electric heating, although this is not depicted in the plot.

The cooling and fan end uses also show savings for the median building around 10%-20%. This is due to replacing older, less efficient RTUs in the existing building stock with higher efficiency multispeed fan and cooling systems. A small portion of the distribution shows increases usage (negative savings) in these categories. The energy increases are mostly buildings showing increased fan and outdoor air usage during night cycling, or buildings with very low HVAC usage that are sensitive to change in a percent savings calculation.

Figure 10 shows the annual percentage site energy savings by fuel type for the HP-RTU Lab Data measure scenario compared to the corresponding models in the ComStock baseline before the measure is applied. Most on-site combustion fuel is removed in applicable buildings, but some remains due to non-applicable HVAC systems as well as other end uses that use combustion fuels (e.g. kitchen equipment).

Figure 10. Percent site energy savings distribution for ComStock models with the applied measure scenario by fuel type.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95119.yaml
     source: 95119_images/image_000011_753379c841760a656ae46d806254fe291144f999e1d13e4db207cd5c07c2a612.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 10. Violin and box plot distribution of percent site energy savings by fuel type for models with the HP-RTU lab data measure scenario applied](95119_images/image_000011_753379c841760a656ae46d806254fe291144f999e1d13e4db207cd5c07c2a612.png)

Figure 10 is a horizontal violin plot with embedded box plots of per-model percent site energy savings aggregated by fuel type, annotated "Upgrade 5.0: HPRTU_Lab_Data (unweighted)". The x-axis is "Percent Site Energy Savings by Fuel (%)" running from about -160% to +100% with a reference line at 0%. Four rows top to bottom with model counts: Other Fuel (n=3300), Natural Gas (n=16893), Electricity (n=34034), and Site (n=34348), where Site is the all-fuel total. Other Fuel is heavily right-skewed with a box roughly spanning 65%-95% and a dense mass against 100%. Natural Gas is similar but wider, with a box around 55%-95%. Both fall short of a clean 100% because some combustion fuel remains in applicable buildings -- from non-applicable HVAC systems and from non-HVAC end uses such as kitchen equipment. Electricity is centered much lower, with a box around 5%-25% and a long thin left tail past -140% for a small number of models. The Site row is the tightest distribution, centered around 15%-25%, showing that the typical applicable building saves roughly a fifth of its total site energy.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they lie outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category. Each data point represents the pairwise comparison between a ComStock baseline model and the corresponding model after the measure scenario is applied.

The electricity end use shows mixed results with notable portions of the distribution showing both savings and increases. Buildings that save electricity with this measure scenario generally do so by replacing less efficient electric resistance RTUs with HP-RTUs, and/or in cases where the reduction in fan/cooling electricity use outweighs the increased electricity use for heating when transitioning from a gas unit (e.g., buildings in warmer climates). Buildings that show increased electricity are generally those that start with primarily gas heating, where transitioning to electric heating outweighs any fan/cooling savings associated with the newer units.

The median building shows 20% site energy savings, which is expected when switching from electric resistance or gas heating to relatively more efficient heat pumps. However, site energy savings do not consider the energy used to generate and distribute electricity to the site and may not translate proportionally to utility bill savings or source energy savings. These other factors should be considered depending on the priorities of the application.

Figure 11 shows the annual percent site energy savings by climate zone for the HP-RTU Lab Data measure scenario compared to the corresponding models in the ComStock baseline before the measure is applied. Higher percent site energy savings are seen in colder climate zones. This result is driven by the heating end use representing a higher prevalence of the total site energy usage, and this measure scenario implements relatively higher efficiency heating systems. But again, site energy savings may not translate directly to other important considerations such as utility bills.

Figure 11. Percent site energy savings distribution for ComStock models with the applied measure scenario by climate zone.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95119.yaml
     source: 95119_images/image_000012_b006f46d4440586c55576864e5614a059f1d8c2e788a26909bb7069b4ebd0c74.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 11. Violin and box plot distribution of percent site energy savings by ASHRAE climate zone for models with the HP-RTU lab data measure scenario applied](95119_images/image_000012_b006f46d4440586c55576864e5614a059f1d8c2e788a26909bb7069b4ebd0c74.png)

Figure 11 is a horizontal violin plot with embedded box plots of per-model percent site energy savings by ASHRAE climate zone, annotated "Upgrade 5.0: HPRTU_Lab_Data (unweighted)". The x-axis runs from about -10% to +60% with a reference line at 0%, so nearly the entire distribution is on the savings side. Rows top to bottom with model counts: 1A (n=794), 2A (n=1768), 2B (n=1082), 3A (n=3302), 3B (n=3842), 3C (n=1277), 4A (n=5154), 4B (n=1547), 4C (n=443), 5A (n=5299), 5B (n=2781), 6A (n=3151), 6B (n=1350), 7 (n=2315), 8 (n=243). Savings increase steadily with heating climate: the hot-humid zone 1A has the lowest median at roughly 7%, mid zones 3A through 4A center around 12%-18%, and the cold zones 6A, 6B, 7, and 8 reach medians of roughly 22%-28% with zone 8 the highest and widest on the smallest sample (n=243). The trend follows from where a heat pump displaces the most combustion heating -- colder zones have more heating load to convert -- and it is the opposite of the pattern seen for electric resistance retrofits, where cold zones fare worst.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category. Each data point represents the pairwise comparison between a ComStock baseline model and the corresponding model after the measure scenario is applied.

