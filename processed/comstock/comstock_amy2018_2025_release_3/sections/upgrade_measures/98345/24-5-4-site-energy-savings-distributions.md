<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/98345.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/98345.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/98345.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/98345.md | section: 5.4  Site Energy Savings Distributions | lines: 561-600 -->
## 5.4  Site Energy Savings Distributions

This section discusses site energy consumption for quality assurance/quality control purposes for the Fan SP Reset measure. Note that while site energy savings can be informative for these purposes, it does not always correspond directly to outcomes of greater practical significance, such as source energy savings or reduced energy bills. It is important for a decision maker to consider which metrics best align with their specific goals or context.

Figure 12 shows distributions of energy savings by fuel type and end use for buildings to which the Fan SP Reset measure was applied. As expected, fans have the highest values of energy savings, followed by cooling (electric and district cooling), and heat rejection. Fan energy savings reflect fan operation at a lower SP setpoint due to the reset. The median fan energy savings value is 68%. As discussed previously, this is higher than reported in other studies but consistent with the fan operation conditions observed in ComStock. (Past studies have generally not quantified effects of SP resets on specific end uses other than fans.) The effect of operating conditions on fan energy savings is discussed in detail in Section 4.6. Cooling energy savings reflects a reduction in fan heat that would have otherwise produced a cooling load. Energy savings in heat rejection reflects reduced load on cooling towers in buildings with water-cooled chillers because of reduced load on the chiller.

As expected, energy penalties are observed in space heating for all space heating fuel types. The reduction in fan heat through the reset results in a heating energy penalty when the fan heat would otherwise have provided useful heating to the airstream. The magnitude of the cooling energy savings and heating penalty depends on the climate and the building's other thermal loads, which influence whether a building would otherwise have required cooling or heating at a given set of conditions. As discussed previously, the magnitudes of the aggregate cooling energy savings and heating energy penalty across the sample are reasonable given the magnitude of fan energy savings.

The relatively wide distribution of pump energy savings, roughly centered at 0, reflects the fact that in buildings with hydronic systems, both cooling and heating have associated distribution pump energy use. The net effect on pump energy use from the Fan SP Reset measure is a consequence of the balance of the heating and cooling energy impacts, which varies from building to building based on climate and space loads. This is discussed in more detail in Section 5.5.

The small change in interior equipment energy use in a few buildings (four) is the result of a known bug in ComStock regarding schedules for elevator operation (https://github.com/NREL/ComStock/issues/350) [20]. This has very minimal impact on the overall energy savings distributions.

Figure 12. Percentage site energy savings distribution for ComStock models with applied measure scenario by end use and fuel type.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98345.yaml
     source: 98345_images/image_000014_dd0827fddde19d3fc4b947122501a19072fe6e8a98f2e72254a7b1a8140baff4.png
     method: vision-description
     described: 2026-08-21 -->

![Box-and-whisker distributions of percentage site energy savings among applied models, broken out by end use and fuel type, with fans showing the largest savings.](98345_images/image_000014_dd0827fddde19d3fc4b947122501a19072fe6e8a98f2e72254a7b1a8140baff4.png)

Figure 12. Distribution of percentage site energy savings across the models to which the Fan SP Reset measure was applied, broken out by end use and fuel type. Each row is one horizontal box-and-whisker distribution with its model count n printed alongside; outliers beyond 1.5 times the interquartile range appear as points. Fans show by far the largest savings, with an interquartile range of roughly 65% to 70% and a median near 68%, matching the 68% median fan energy savings stated in the text. Cooling, both electric and district, comes next, followed by heat rejection, the ordering the text gives. The pump electricity distribution is wide and roughly centered on zero, which Section 5.5 explains as the balance between extra heating-driven pump energy and reduced cooling-driven pump energy in hydronic buildings. Heating rows sit on the penalty side for every heating fuel. The Interior Equipment Electricity row carries n = 4, matching the note that a small interior equipment change in four buildings stems from a known ComStock elevator-schedule bug, ComStock issue 350.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

Figure 13 shows the distribution of energy savings by fuel type. As expected, and for the reasons discussed previously, application of the measure results in electricity savings and net site energy savings, as well as savings for district cooling. The measure results in penalties for fuels used solely for heating: natural gas, fuel oil, propane, and district heating.

Figure 13. Percentage site energy savings distribution for ComStock models with the applied measure scenario by fuel type.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98345.yaml
     source: 98345_images/image_000015_d2a2bb9b8f2e3e3a34616c1907f19817624e6bd4466543de8de1327794c685e4.png
     method: vision-description
     described: 2026-08-21 -->

![Box-and-whisker distributions of percentage site energy savings among applied models, broken out by fuel type, with electricity saving and heating fuels penalized.](98345_images/image_000015_d2a2bb9b8f2e3e3a34616c1907f19817624e6bd4466543de8de1327794c685e4.png)

Figure 13. Distribution of percentage site energy savings across the models with the Fan SP Reset measure applied, broken out by fuel type. Each fuel is one horizontal box-and-whisker distribution with its model count n printed on the row and outliers beyond 1.5 times the interquartile range drawn as points. Electricity, district cooling and total site energy sit on the savings side of zero; natural gas, fuel oil, propane and district heating sit on the penalty side, exactly as Section 5.4 describes, because those fuels serve only heating in these models and the measure removes useful fan heat. The electricity median measures about 14.7%, close to Table 5's 14.0% applicable-buildings electricity savings, and the total site energy median measures about 9%, close to Table 5's 8.7%; the axis calibration is roughly 1.5 pixels per percent, so treat both medians as approximate. The n values across the fuel rows sum to 18,400, the same total as Figure 11's climate-zone rows.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

