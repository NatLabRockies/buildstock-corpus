<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95014.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95014.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95014.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/95014.md | section: 5.5  Site Energy Savings Distributions | lines: 744-798 -->
## 5.5  Site Energy Savings Distributions

This section discusses site energy consumption for quality assurance/quality control purposes. Note that site energy savings can be useful for these purposes, but other factors should be considered when drawing conclusions, as they do not necessarily translate proportionally to source energy savings, energy costs, and impact to emissions avoided.

Figure 14 shows the percentage savings distributions of the baseline ComStock models versus the Condensing Boiler measure by fuel type for applicable models. In other words, each data point in the distribution represents the percentage energy savings between a baseline ComStock model and the corresponding model with measures applied.

Natural gas and other fuels show 10%-20% savings in the middle 50% of buildings. Electricity shows very minor changes in site energy consumption with the Condensing Boiler measure. Some outlier buildings show an increase in electricity, which is a result of minor changes to the cooling, fan, or pump load when replacing the boiler (e.g., reduced supply temperature requires higher pumping to deliver the same energy). In total, site energy is reduced by up to 7% in the middle 50% of buildings, and up to 15% at the upper whisker. A few outliers show negative savings (an increase) in natural gas or total site energy. Upon investigation, these outliers were a small number of buildings in hot climates that either (a) have a negligible heating load, or (b)

appear to have had some anomaly with outdoor air behavior that caused an increase in heating and/or cooling loads.

Figure 14. Percent site energy savings distribution for ComStock models with applied Condensing Boiler measure scenario by fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95014.yaml
     source: 95014_images/image_000016_fa84c0241d8f556c214fc119dad0cbcc11ae191fad0655caa578b8cce4a2082c.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 14. Horizontal violin-and-box distributions of percent site energy savings by fuel type for applicable ComStock models, with natural gas and other fuel centered on 10 to 20% savings and total site savings up to about 7% for the middle 50%](95014_images/image_000016_fa84c0241d8f556c214fc119dad0cbcc11ae191fad0655caa578b8cce4a2082c.png)

Horizontal violin plots with embedded box plots, annotated Upgrade 16.0: Condensing Boilers (unweighted). X-axis: Percent Site Energy Savings by Fuel (%), -120 to 40, with a reference line at 0. Rows top to bottom with their applicable-model counts: District Heating (n=12), Other Fuel (n=545), Natural Gas (n=30333), Electricity (n=30784), Site (n=30878). The district heating row holds only 12 models and shows essentially no spread. Per Section 5.5, natural gas and other fuels show 10%-20% savings for the middle 50% of buildings; electricity shows very minor changes, a narrow distribution around zero with outlier buildings on the increase side caused by small changes in cooling, fan or pump load, for example a reduced supply temperature requiring more pumping to deliver the same energy; and total Site energy is reduced by up to 7% for the middle 50% and up to 15% at the upper whisker. Long left tails and isolated points below -40% are outliers beyond 1.5 times the interquartile range, traced to buildings in hot climates with negligible heating load or an outdoor-air anomaly. The Site row's n=30878 is the applicable-model total used throughout Section 5.5.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

Figure 15 shows the percentage savings distributions by end use of the baseline ComStock models versus the Condensing Boiler measure for applicable models. Natural gas and other fuel heating are the main end uses with energy savings. These end uses see savings of 15%-20% for the middle 50% of buildings. Two end uses see nontrivial negative savings (an increase in energy) when replacing the existing boiler system with a condensing boiler-electricity pumps and electricity heating.

With the condensing boiler, we are using lower supply temperatures, which increases pumping needs to supply the same amount of energy. Electric heating sees high percent increases in a small fraction of buildings that include both a boiler and another type of electric heating (e.g., DOAS with water-source heat pumps and cooling tower with boiler). With the lower supply temperatures, the electric heating in the system may operate slightly differently. With both pumps and electric heating, these end uses have very minimal impact in terms of energy use intensity (EUI) contributions. Although the percent changes might look high, there is very little impact on the total energy of the building, which is going to be most impacted by the changes in natural gas or fuel oil boiler heating load.

Figure 15. Percent site energy savings distribution for ComStock models with applied Condensing Boiler measure scenario by end use

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95014.yaml
     source: 95014_images/image_000017_852387d7715c82e6750eebdf60286076b1d4af4a1bb270a2b44098ab1d691b10.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 15. Horizontal violin-and-box distributions of percent site energy savings by end use for applicable ComStock models, with natural gas and other fuel heating saving 15 to 20% and electricity pumps and electricity heating showing large percentage increases](95014_images/image_000017_852387d7715c82e6750eebdf60286076b1d4af4a1bb270a2b44098ab1d691b10.png)

Horizontal violin plots with embedded box plots, annotated Upgrade 16.0: Condensing Boilers (unweighted). X-axis: Percent Site Energy Savings by End Use (%), -160 to 40, reference line at 0. Fourteen rows, top to bottom: Other Fuel Water Systems (n=24), Other Fuel Heating (n=541), District Heating Water Systems (n=12), Natural Gas Water Systems (n=2763), Natural Gas Heating (n=30335), Electricity Water Systems (n=1015), Electricity Refrigeration (n=7428), Electricity Pumps (n=30678), Electricity Interior Equipment (n=13), Electricity Heating (n=1239), Electricity Heat Rejection (n=3457), Electricity Heat Recovery (n=1289), Electricity Fans (n=27253), Electricity Cooling (n=23058). Natural Gas Heating and Other Fuel Heating are the only rows with substantial positive savings, centered on 15%-20% for the middle 50%. Two rows sit clearly on the negative side: Electricity Pumps, since lower supply temperatures increase pumping to deliver the same energy, and Electricity Heating, spanning to -160% for the few buildings that pair a boiler with another electric heat source such as DOAS with water-source heat pumps. Section 5.5 stresses that both have very small EUI contributions, so the large percentages barely affect building totals.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

When looking at site energy savings by climate zone in Figure 16, we see a clear trend of higher savings in colder climate zones. These results make intuitive sense, given that site energy use in colder climates is more driven by heating loads. Therefore, we see the site energy savings increase as we move from warmer climates (climate zones 1-3) to colder climates (climate zones 5-8). Median site energy savings are minimal (under 2%) in climate zones 1-2, while median savings are 7%-10% in climate zones 6-8. A small number of buildings, mainly in warmer climate zones, show an increase in site energy. These were primarily found to be buildings with a negligible heating load; therefore, even a small magnitude change in load appears as a large percent change.

Figure 16. Percent site energy savings distribution for ComStock models with applied Condensing Boiler measure scenario by climate zone

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95014.yaml
     source: 95014_images/image_000018_1c77c8d75b22c324affb2c99b86d76d9f84d45d6675dc2a5c2fd60c6b448fa09.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 16. Horizontal violin-and-box distributions of percent site energy savings by ASHRAE climate zone for applicable ComStock models, rising from under 2% median in zones 1A and 2A to roughly 7 to 10% in zones 6 through 8](95014_images/image_000018_1c77c8d75b22c324affb2c99b86d76d9f84d45d6675dc2a5c2fd60c6b448fa09.png)

Horizontal violin plots with embedded box plots, annotated Upgrade 16.0: Condensing Boilers (unweighted). X-axis: Percent Site Energy Savings by Climate Zone (%), about -70 to 20, with a reference line at 0. Fifteen zone rows, top to bottom, with applicable-model counts: 1A (n=563), 2A (n=1518), 2B (n=760), 3A (n=3542), 3B (n=4239), 3C (n=1265), 4A (n=5268), 4B (n=1325), 4C (n=516), 5A (n=4698), 5B (n=2280), 6A (n=2548), 6B (n=939), 7 (n=1307), 8 (n=110). These counts sum to exactly 30,878, the applicable-model total printed as Site (n=30878) in Figure 14. The distributions shift steadily right as the climate gets colder: medians are under 2% in zones 1A through 2B, mid single digits through zones 3 to 5, and roughly 7%-10% in zones 6A through 8, with zone 8 the widest and most positive. Section 5.5 explains the trend as site energy in colder climates being more heating driven. Long left tails, most pronounced in the warm zones 2A and 3A, are buildings with negligible heating load where a small absolute change reads as a large percentage increase in energy use.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

