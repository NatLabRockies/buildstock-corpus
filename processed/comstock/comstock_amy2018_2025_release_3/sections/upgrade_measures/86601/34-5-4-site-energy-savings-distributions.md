<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86601.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86601.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86601.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/86601.md | section: 5.4 Site Energy Savings Distributions | lines: 696-754 -->
## 5.4 Site Energy Savings Distributions

This section discusses site energy consumption for quality assurance/quality control purposes. Note that site energy savings can be useful for these purposes, but other factors should be considered when drawing conclusions, as these do not necessarily translate proportionally to source energy savings, greenhouse gas emissions avoided, or energy cost.

Figure 6 shows the percent savings distributions of the baseline ComStock models versus the Interior Lighting and Heat Pump scenario by end use and fuel type for applicable models. Minimal differences are observed for water systems and refrigeration, which see small changes in the baseline due only to minor changes in ambient air temperature that affect the operation of these systems. Most of the savings for the 'Other Fuel Heating' and 'Natural Gas Heating' categories are at 100% owing to replacing the combustion fuel-based system in the baseline with an all-electric heat pump system in the Interior Lighting and Heat Pump scenario. A number of models unexpectedly show 'Natural Gas Heating' and 'Other Fuel' heating penalties. Closer investigation shows that these models (1) only have the LED lighting measure applicable and are therefore losing the internal load provided by pre-LED lighting technologies that was beneficial for heating, and (2) have low heating loads, in general, because they are located in warm climates and therefore any small change between the baseline and upgrade model will result in high percent change. When considering the site energy use intensity (EUI) savings rather than percent savings, this second point is evident (Figure 7).

Figure 6. Percent site energy savings distribution for ComStock models with the Interior Lighting and Heat Pump package applied by end use and fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86601.yaml
     source: 86601_images/image_000007_bf4ceffa4568d406d915d04dc2c4b42ca0cbc1f71684978a02a4e767593a5553.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by end use and fuel type for Package 2](86601_images/image_000007_bf4ceffa4568d406d915d04dc2c4b42ca0cbc1f71684978a02a4e767593a5553.png)

Figure 6: horizontal violin-and-box plot of percent site energy savings by end use and fuel type, x-axis -160% to 100%, titled Upgrade 17: Package 2 (unweighted), with model counts per row (electricity cooling n=286,960; natural gas heating n=211,863). Other fuel and natural gas heating pile up at 100% as combustion heating is replaced, while electricity heating carries a wide penalty tail. Section 5.4 explains the gas penalties.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

Pump electricity increased between the baseline and upgrade scenario, as expected, due to the addition of heat pump boilers to the models which adds equipment to the loop and operates at a lower supply temperature than the existing gas boilers they are replacing.

A number of models saw heating electricity savings due to higher efficiency performance of HPRTUs compared with traditional RTUs. Some models also saw heating electricity penalties. This can be attributed to the conversion of combustion-based heating to electricity-based.

Some models show negative heat recovery savings, noting that the heat recovery end use is for electricity used to operate enthalpy wheels. The negative energy savings are due to increased prevalence of wheel operation caused by increased cycling operation with the HP-RTUs compared to the baseline RTUs. In other words, increased runtime for the air handler can cause increased run time for the enthalpy wheel. This is in part due to an EnergyPlus bug that causes longer cycling operation with the multispeed coil objects used for modeling the HP-RTU. However, the heat recovery end use makes up a very small portion of building stock energy usage, so negative percentage savings in this end use has minimal impact.

Eight models show greater than 100% energy savings for the cooling end use. This is a documented issue in the HP-RTU upgrade for these models. The DX cooling coil in a fraction of zones that the HP-RTU measure are applied to incur a negative EIR at certain times throughout the year. This issue will be resolved in the next cycle of EUSS upgrade measures, likely by applying curve bounds. This affects a very small subset of the models and has minimal impact on the results.

Figure 7. Site EUI energy savings distribution for ComStock models with the Interior Lighting and Heat Pump package applied by end use and fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86601.yaml
     source: 86601_images/image_000008_90353263a2ff02cac43cbc61519abb5ed630fa38ae30cc6f4aa2c126887dd150.png
     method: vision-description
     described: 2026-08-21 -->

![Dot and box plots of site EUI savings by end use for Package 2, in kBtu per square foot](86601_images/image_000008_90353263a2ff02cac43cbc61519abb5ed630fa38ae30cc6f4aa2c126887dd150.png)

Figure 7: horizontal dot-and-box plot of site EUI savings by end use, x-axis -200 to 550 kBtu/ft2, titled Upgrade 17: Package 2 (unweighted), one row per end-use intensity with the same model counts as Figure 6. Nearly all mass sits at or just above zero and natural gas heating has the widest spread; plotting EUI removes the extreme percentage penalties of Figure 6.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

Figure 8 shows the site energy savings distributions between the ComStock baseline and the Interior Lighting and Heat Pump scenario by fuel type and total site energy. The total site energy savings distribution shows savings values generally between 10% and 35% for the 25 th and 75 th percentiles, respectively. Combined site energy savings alone is not a comprehensive assessment of electrification measures, so other considerations should be made as well.

The site electricity distribution shows some energy penalties. These are mostly buildings that changed from gas heat to electric heat, so the penalties are expected. Some of this electricity penalty is reduced or mitigated through savings for cooling, fans, and heat recovery, depending on the building and its climate zone. Many of the buildings, however, show electricity savings. Many of these models had their interior lighting replaced with LEDs. Others are buildings that had electric heating in the baseline; in these cases, the higher-efficiency HP-RTU system reduces electricity usage across multiple end uses.

The 'Natural Gas' and 'Other Fuel' end uses show many models with near 100% savings. These are buildings that are completely electrified from the HP-RTU or ASHP Boiler measures and where gas is not used for other end uses. Models with less than 100% gas or other fuel savings generally have some nonapplicable gas HVAC system type in the baseline, or other end uses, such as water heating, that are not electrified through the HP-RTU or ASHP Boiler measures. Several models show negative natural gas site savings. These are primarily models that either only had the LED lighting measure applicable and therefore had higher heating requirements, or have low heating loads that show a misleadingly high percent change in heating consumption, as previously discussed. This is the case for district heating negative savings, as well.

Figure 8. Percent site energy savings distribution for ComStock models with the applied Interior Lighting and Heat Pump package by fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86601.yaml
     source: 86601_images/image_000009_e9b7942ea7fc57229eff0b8d8bf32db55df9b028b52f72de0fffef2770bb9405.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by fuel type, including total site energy](86601_images/image_000009_e9b7942ea7fc57229eff0b8d8bf32db55df9b028b52f72de0fffef2770bb9405.png)

Figure 8: horizontal violin-and-box plot of percent site energy savings by fuel, x-axis -160% to 100%, six rows - district cooling, district heating, other fuel, natural gas, electricity, and total site (n=304,607). Other fuel and natural gas cluster near 100%; the total site row runs roughly 10% to 35% between the 25th and 75th percentiles, as stated in Section 5.4.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

