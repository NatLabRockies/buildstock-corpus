<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89239.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89239.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89239.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/89239.md | section: 5.4  Site Energy Savings Distributions | lines: 541-614 -->
## 5.4  Site Energy Savings Distributions

Figure 13 shows the distribution of energy savings by end use for the Central Hydronic GHP measure. The elimination of natural gas space heating and other fuel-fired heating (shown by the distributions concentrated at a 100% reduction) in applicable buildings is expected because the measure involves full space heating electrification. The distribution concentrated at 100% for reduction in heat rejection energy use is also expected because the implementation of this measure eliminates the use of cooling towers in applicable buildings.

An increase in circulation pump energy use is also expected due to the increased pump head associated with the ground loop. (This is widely variable as a percent of existing pump energy use, since the head associated with the ground loop is fixed as an input to the measure, and flow through the ground loop is variable with the building loads, leading to the wide distribution of the proportionate pump energy savings.) Note that pump energy use on the ground and condenser loops is influenced by the condenser loop temperature set points, and the condenser loop temperature range influences the performance of the connected heat pumps. In the application of this measure, the condenser loop set point range was constant across all buildings, but in a particular application, the set point range could be optimized for trade-offs with space conditioning energy. As illustrated in Figure 11, in this case, the overall pump energy penalty in applicable buildings was small in magnitude in comparison with the space conditioning energy saved, confirming that the range of set points selected was generally effective.

In buildings with existing electric heating, electric heating energy savings is expected due to the replacement of electric resistance coils with more efficient heat pump heating as part of the primary heating system (any electric resistance coils in DOAS units were retained). Buildings without existing electric heating experienced a large increase in electric heating energy use, but this effect is not shown in Figure 13 because electric heating was not an existing end use in the building. Cooling energy use savings can be expected in cases in which the water-source heat pump's cooling efficiency is higher than that of the existing direct expansion coils or chilled water system. The heat pump loop configuration also allows for simultaneous heating and cooling loads to offset each other on the source-side loop.

Note that the small fluctuations in refrigeration and water heating energy use are due to small changes in zone conditions resulting from the implementation of this measure.

Figure 13. Percent site energy savings distribution for ComStock models with the Central Hydronic GHP measure applied by end use and fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89239.yaml
     source: 89239_images/image_000019_b2e3dd0babfd4cb380c51261e302ad2122fe0c196dc85dc366ce25d0371d7776.png
     method: vision-description
     described: 2026-08-21 -->

![Violin plot of percent site energy savings by end use and fuel type, unweighted](89239_images/image_000019_b2e3dd0babfd4cb380c51261e302ad2122fe0c196dc85dc366ce25d0371d7776.png)

Figure 13: horizontal violin-and-box plot titled Upgrade 15: Hydronic GHP (unweighted), x-axis percent site energy savings from -160 to 100, one row per end use and fuel with sample sizes in the row labels. Natural gas heating, other fuel heating, and electricity heat rejection concentrate at 100% savings, while electricity pumps spreads far negative. Section 5.4 explains each distribution.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

Figure 14 shows the distributions of site energy savings by baseline HVAC system type to which this measure was applicable. The chiller with gas boiler reheat-based systems had the highest

(75th percentile) level of site energy savings from this measure. Systems with packaged fanpowered (PFP) boxes had lower ranges of savings, including with a 25th percentile savings level less than zero in the case of the VAV water-cooled chiller with PFP boxes. Note that VAV chiller with PFP boxes and VAV air-cooled chiller with PFP boxes systems have electric reheat coils. As part of this measure, these coils are replaced with hydronic coils, further increasing pump energy use. The partial use of electric heat in the baseline also reduces the potential for site energy savings through the implementation of the GHP measure, as the electric coils are more efficient, on a site energy basis, than hydronic coils coupled to a gas-fired boiler, or gas-fired coils.

Figure 14. Percent site energy savings distribution for ComStock models with the applied Central Hydronic GHP measure by HVAC system type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89239.yaml
     source: 89239_images/image_000020_f35d1ad1d8cc0a117e3f085f4df65dc759984606f29428a6eaab731fe074ba4e.png
     method: vision-description
     described: 2026-08-21 -->

![Violin plot of percent site energy savings by baseline HVAC system type](89239_images/image_000020_f35d1ad1d8cc0a117e3f085f4df65dc759984606f29428a6eaab731fe074ba4e.png)

Figure 14: horizontal violin-and-box plot of percent site energy savings by baseline HVAC system type, x-axis roughly -100 to 80, six rows with sample sizes in the labels (largest VAV chiller with gas boiler reheat, n=5279). Chiller with gas boiler reheat systems show the highest 75th-percentile savings; VAV chiller with PFP boxes is lowest, with a 25th percentile below zero.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the HVAC system type category.

As part of this measure, in buildings with existing hydronic heating systems, heating supply water temperatures were reduced from 180°F to 140°F, to reflect the water temperatures that can be supplied by existing water-to-water heat pumps. In EnergyPlus, heating coils were allowed to 're-auto-size' after implementing this measure to account for the reduction in supply temperature. In a review of a sample of models, it was observed that water flow and the temperature differential through the resized coils generally remained comparable before and after the implementation of the measure, and that the coil resizing did not result in significantly higher water flows. (Fans were not resized in the implementation of this measure.) It was confirmed through a sample of models that the hours in which set points were not met remained comparable before and after the measure implementation, demonstrating that desired zone conditions were being met as effectively as before.

Figure 15 shows the distribution of percent site energy savings by climate zone for buildings to which this measure was applicable. These results do not show a strong climate-zone-related dependency in the range of energy savings, though for some climate zones (1A, 7A, 7B), the sample sizes are quite small (fewer than 200 buildings). The considered Central Hydronic GHP generally improved efficiency in both heating and cooling, at the expense of increased pump energy, which is generally small compared to the heating and cooling savings.

Figure 15. Percent site energy savings distribution for ComStock models with the applied Central Hydronic GHP measure by climate zone

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89239.yaml
     source: 89239_images/image_000021_cc950c22da16b72842227f7fcfc1f0bf0b51e0af3f34d47032e28ff6a6aaf651.png
     method: vision-description
     described: 2026-08-21 -->

![Violin plot of site EUI savings by ASHRAE climate zone; axis is kBtu/ft2 despite the caption](89239_images/image_000021_cc950c22da16b72842227f7fcfc1f0bf0b51e0af3f34d47032e28ff6a6aaf651.png)

Figure 15: horizontal violin-and-box plot with one row per ASHRAE climate zone, 1A through 7B, sample sizes in the row labels. The x-axis is labeled Site EUI Savings by Climate Zone in kBtu/ft2 and runs from about -50 to 320, whereas the caption says percent site energy savings. Medians cluster just above zero with long positive outlier tails and no strong climate dependency.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for the climate zone.

In this measure, the considered ground heat exchangers are sized to meet the full loads of the building over a 20-year period, accounting for the potential for long-term ground temperature shifts due to imbalanced loads. (Since these results are based on an analysis period of 1-year, long-term effects of unbalanced loads on ground heat exchanger performance do not arise within the analysis period.) Note that this potential for long-term temperature imbalance is an important consideration in field installations of ground heat exchangers. Often this can be mitigated by installing taps for fluid coolers or air-water heat pumps to maintain condenser loop temperatures if needed.

Figure 16 shows distributions of site energy savings by building type for buildings to which this measure was applicable. Primary and secondary schools and stand-alone retail buildings had the highest ranges (25th to 75th percentile) of site energy savings, within the range of 40%-60%. Note that the proportional overall site energy savings from this measure in a particular building is also a function of the relative share of HVAC-related end uses of the overall building energy use. Improved energy savings from this measure would be expected in buildings with a higher degree of load diversity at a given point in time, for long periods of the year, given that the water-source heat pumps providing heating and cooling share a common condenser loop, and the extent to which their return temperatures moderate each other's effects on the condenser loop reduces the flow rate through the ground loop required to provide the net level of heat or heat rejection necessary. The degree of load balance throughout the year is a function both of climate and building type. Note the small sample sizes for individual building types, given the relatively small proportion of buildings to which this measure was applicable, and the 10,000-building sample size. This disaggregation can be explored in more detail when full results are available.

Figure 16. Percent site energy savings distribution for ComStock models with the applied Central Hydronic GHP measure by building type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89239.yaml
     source: 89239_images/image_000022_479cb1da18c87c3854de19233a1678c625b6750feed15cf09e51b4c4e1a12971.png
     method: vision-description
     described: 2026-08-21 -->

![Violin plot of percent site energy savings by ComStock building type](89239_images/image_000022_479cb1da18c87c3854de19233a1678c625b6750feed15cf09e51b4c4e1a12971.png)

Figure 16: horizontal violin-and-box plot of percent site energy savings by ComStock building type, x-axis roughly -100 to 80, fourteen rows with sample sizes in the labels. Primary and secondary schools and stand-alone retail show the highest interquartile ranges, about 40%-60%; small office and small hotel have the widest spread and the smallest samples. See Section 5.4.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for the building type.

