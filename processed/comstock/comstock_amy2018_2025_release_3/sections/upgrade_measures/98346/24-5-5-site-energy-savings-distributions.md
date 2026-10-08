<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/98346.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/98346.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/98346.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/98346.md | section: 5.5  Site Energy Savings Distributions | lines: 515-598 -->
## 5.5  Site Energy Savings Distributions

This section discusses site energy consumption for quality assurance/quality control purposes for the Thermostat Setbacks measure. Note that while site energy savings can be informative for these purposes, it does not always correspond directly to outcomes of greater practical significance, such as source energy savings or reduced energy bills. It is important for a decision maker to consider which metrics best align with their specific goals or context.

Figure 12 shows distributions of the percentage site energy use savings from the Thermostat Setbacks measure by end use. Heating (across various fuel types) and heat recovery (in a smaller subset of buildings) are the end uses with the largest savings rates. Heat recovery energy savings results from reduced heating loads through the thermostat setbacks. The measure also results in cooling and fan energy savings, at lower levels, as shown in the aggregate results. The small changes in refrigeration energy use observed in some buildings result from changes in indoor conditions because of the setback. The small change in interior equipment energy use in some buildings (33) is the result of a known bug in ComStock regarding schedules for elevator operation [12]. This has very minimal impact on the overall energy savings distributions.

As discussed previously, implementation of the thermostat setback can result in changes in distribution of heating energy use by fuel type in buildings with multiple types of heating systems (for example, electricity and natural gas). In Figure 12, all heating fuels have some negative area of savings distribution, but very few buildings in the sample (only 2.2% of applicable buildings) had negative aggregate heating energy savings. Figure 13 shows a distribution of heating energy savings among most of the sample for which this value was nonnegative. The largest share of buildings have heating energy savings from this measure of less than 10%. Buildings with proportionately very high (greater than 70%) heating energy savings from this measure tend to be those with low heating energy use in the baseline, which magnifies the effects of small absolute changes. This effect is illustrated in Figure 14, which shows boxplots of absolute heating energy savings for buildings with non-negative savings, those with high savings, and those with negative savings. Those with high proportionate savings have much lower absolute heating energy savings than the full sample, indicating low absolute heating energy use in the baseline. Those with negative savings also have low magnitudes of absolute savings. In some cases, increased operation of heating coils to recover zone temperatures after a large setback can contribute to higher energy use, especially if the coils are now undersized for the 'recovery' load. (In ComStock, thermostat setbacks are not considered when sizing heating coils.) This effect was very limited in the sample.

The pump energy end use has a small portion of negative savings distribution. Figure 15 shows boxplots of pump energy savings for buildings with positive and negative pump savings, respectively. As shown in Figure 15, the median value of negative savings is very low, indicating that this effect is primarily due to small fluctuations. Figure 16 shows distribution of site energy savings by fuel type, which generally mirrors the trends shown in Figure 12.

Figure 12. Percentage site energy savings distribution for ComStock models with applied measure scenario by end use and fuel type.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98346.yaml
     source: 98346_images/image_000014_2220882166b4b318c1f723c4c2a5efa8231e3305ce9a61e6dfae95f17bd48e3b.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box distributions of percent site energy savings by end use and fuel, with the heating end uses showing the widest positive distributions.](98346_images/image_000014_2220882166b4b318c1f723c4c2a5efa8231e3305ce9a61e6dfae95f17bd48e3b.png)

Figure 12. Distributions of percentage site energy savings by end use and fuel, drawn as violins with boxplots inside; the horizontal axis is Percent Site Energy Savings by End Use, running from about -160 to 100. Eighteen rows are plotted with their sample counts, from the top: District Heating Water Systems 201, District Heating Heating 1,359, District Cooling Cooling 1,062, Fuel Oil Water Systems 108, Fuel Oil Heating 3,305, Propane Water Systems 380, Propane Heating 4,820, Natural Gas Water Systems 2,661, Natural Gas Heating 19,427, Electricity Water Systems 3,770, Electricity Refrigeration 16,108, Electricity Pumps 7,501, Electricity Interior Equipment 33, Electricity Heating 19,280, Electricity Heat Rejection 2,422, Electricity Heat Recovery 964, Electricity Fans 35,769 and Electricity Cooling 47,060. The heating rows are the widest: gas heating and electric heating both run from about 5% to the high 30s with medians near 18% to 20%, matching the 19% and 18% applicable-only heating savings in Table 5. Fans sit near 0% to 3% and cooling near 0% to 7%, matching Table 5's 1.8% and 4.8%. The tiny Interior Equipment row, n=33, is the elevator-schedule bug noted in Section 5.5.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

Figure 13. Distribution of heating energy savings among buildings in sample with non-negative energy savings from Thermostat Setbacks measure

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98346.yaml
     source: 98346_images/image_000015_82eeaa475ac28ed71c387eb9f992961f7c9a2024d9c2fc0d9bbd02506078190c.png
     method: vision-description
     described: 2026-08-21 -->

![Histogram of percentage heating energy savings across buildings with non-negative savings, declining from a tall first bin with an uptick in the top bin.](98346_images/image_000015_82eeaa475ac28ed71c387eb9f992961f7c9a2024d9c2fc0d9bbd02506078190c.png)

Figure 13. Histogram of heating energy savings among the buildings in the sample with non-negative heating savings from the Thermostat Setbacks measure. The horizontal axis is heating energy savings from 0% to 100% in ten ten-point bins; the vertical axis is Number of buildings in sample, 0 to 16,000. The first bin, 0% to 10%, is much the tallest at roughly 15,200 buildings, and the counts then fall away steadily through roughly 6,300, 5,300, 3,800, 2,800, 2,500, 1,900, 1,100 and 640, before turning up again in the final 90% to 100% bin at roughly 2,500. The bins sum to roughly 42,000 buildings. Section 5.5 makes two points from this shape: the largest share of buildings have heating savings below 10%, and the group above 70% savings, which the final uptick belongs to, consists of buildings with very low baseline heating use, so a large percentage saving corresponds to a small absolute one. The bins above 70% together account for roughly 10% of the plotted sample. Buildings with negative heating savings, about 2.2% of the applicable sample per Section 5.5, are excluded from this figure by construction.

Figure 14. Boxplots of absolute heating energy savings for the full sample with non-negative savings, buildings with high savings (&gt;70%), and buildings with negative savings

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98346.yaml
     source: 98346_images/image_000016_ddf713a87f9e3e8bb9727e5af3892180f795931e155669b8c8a756d2acc83b2c.png
     method: vision-description
     described: 2026-08-21 -->

![Three boxplots of absolute heating energy savings in MBtu for the full non-negative sample, the high-percentage-savings subset and the negative-savings subset.](98346_images/image_000016_ddf713a87f9e3e8bb9727e5af3892180f795931e155669b8c8a756d2acc83b2c.png)

Figure 14. Boxplots of absolute heating energy savings for three groups of buildings. The vertical axis is Absolute heating energy savings in MBtu, running from about -50 to 350, and the three groups along the horizontal axis are labeled Positive heating savings, High heating savings and Negative heating savings. The positive-savings group is much the widest: its first quartile sits at about 0, its median near 30 MBtu, its third quartile near 135 MBtu and its upper whisker near 350 MBtu. The high-savings group, the buildings with more than 70% percentage savings, is compressed close to zero, with a median of about 0 to 1 MBtu and a third quartile near 20 MBtu; that contrast is the point of the figure, since it shows that the high percentage savings of that group correspond to very small absolute savings because their baseline heating use is low. The negative-savings group sits just below zero, with a third quartile at about 0, a median near -5 MBtu, a first quartile near -22 MBtu and a lower whisker near -60 MBtu. Note that the caption says non-negative savings where the axis tick reads Positive heating savings.

Figure 15. Boxplots of pump energy savings for buildings disaggregated by the nature of the savings

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98346.yaml
     source: 98346_images/image_000017_988e72114c899909f18e3df74a22ed96e332a317d35d7d9a1c395aa8b03b6bc3.png
     method: vision-description
     described: 2026-08-21 -->

![Two boxplots of pump energy savings in kWh for buildings with positive and with negative pump savings; the negative group is clustered close to zero.](98346_images/image_000017_988e72114c899909f18e3df74a22ed96e332a317d35d7d9a1c395aa8b03b6bc3.png)

Figure 15. Boxplots of pump energy savings for the buildings with positive and with negative pump savings respectively. The vertical axis is Pump energy savings in kWh, running from about -1,000 to 4,000, and the two groups along the horizontal axis are labeled Positive pump savings and Negative pump savings. The positive group has a first quartile near 100 kWh, a median near 400 kWh, a third quartile near 1,600 kWh and an upper whisker reaching about 3,900 kWh. The negative group is far more compressed and sits just below zero, with a third quartile at about 0, a median near -120 kWh, a first quartile near -500 kWh and a lower whisker near -1,200 kWh. Section 5.5 draws exactly this conclusion from the figure: the median magnitude of negative pump savings is very low, so the negative pump-energy tail visible in Figure 12 reflects small fluctuations rather than a systematic energy penalty.

Figure 16. Percentage site energy savings distribution for ComStock models with the applied measure scenario by fuel type.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98346.yaml
     source: 98346_images/image_000018_b5db3fe1686366d3df269424bc22ff4e6b0743eddb13679b5d089c4d4a9318da.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box distributions of percent site energy savings by fuel, with the heating fuels showing wide positive distributions and electricity a narrow one.](98346_images/image_000018_b5db3fe1686366d3df269424bc22ff4e6b0743eddb13679b5d089c4d4a9318da.png)

Figure 16. Distributions of percentage site energy savings by fuel for the ComStock models under the applied measure scenario, in the same violin-with-boxplot style as Figure 12. The title reads Upgrade 25.0: Thermostat_Setbacks (unweighted) and the horizontal axis is Percent Site Energy Savings by Fuel, running from about -160 to 100. Seven rows are plotted with their sample counts, from the top: District Cooling n=1,062, District Heating n=1,363, Propane n=4,867, Fuel Oil n=3,308, Natural Gas n=20,223, Electricity n=48,371 and Site n=48,404. The heating-dominated fuels are the widest: district heating, propane, fuel oil and natural gas all have interquartile ranges running from roughly 4% or 5% into the middle or high 20s with medians in the middle teens, and all carry long negative tails past -100% together with dense outlier strings above 60%. District cooling and electricity are narrow bands close to zero, and the aggregate Site row runs from roughly 1% to 6%. Section 5.5 notes that this figure generally mirrors the trends shown in Figure 12.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

Figure 17 shows distributions of site energy use savings from this measure by building type. Primary and secondary schools have some of the highest savings from this measure, reflecting their relatively high number of unoccupied hours during which the setback can occur. Hospitals and hotels, which have limited space types to which this measure is applicable, have low energy savings. (Guest room spaces in hotels and patient-serving and laboratory areas in hospitals were not eligible for this measure).

Figure 17. Percentage site energy savings distribution for ComStock models with the applied measure scenario by building type.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98346.yaml
     source: 98346_images/image_000019_9909ab49e6ac05cf7aea1cdb00367bc70d0b7c1927b92917d3e074bc7c9d822c.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box distributions of percent site energy savings by building type; the two school types have the highest savings and hospitals and hotels the lowest.](98346_images/image_000019_9909ab49e6ac05cf7aea1cdb00367bc70d0b7c1927b92917d3e074bc7c9d822c.png)

Figure 17. Distributions of percentage site energy savings by ComStock building type under the applied measure scenario, in violin-with-boxplot style, with the horizontal axis running from about -100 to 50. Fourteen building-type rows are plotted with their sample counts: FullServiceRestaurant n=5,891, Grocery n=4,037, Hospital n=305, LargeOffice n=3,126, MediumOffice n=5,540, Outpatient n=1,285, PrimarySchool n=1,742, QuickServiceRestaurant n=3,667, RetailStandalone n=5,559, RetailStripmall n=3,163, SecondarySchool n=1,138, SmallHotel n=728, SmallOffice n=6,509 and Warehouse n=5,710. The two school types stand out with much the widest and highest distributions, medians near 12% for primary and 14% for secondary schools against roughly 1% to 7% for every other type, which Section 5.5 attributes to their large number of unoccupied hours. Hospital, SmallHotel, Grocery, QuickServiceRestaurant and Warehouse sit lowest at roughly 1% to 2%, consistent with the exclusion of patient-serving, laboratory and guest-room space types. LargeHotel has no row at all, matching the zero applicable floor area shown for it in Figure 1. The fourteen counts sum to about 48,400, against the 48,404 Site count in Figure 16.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

