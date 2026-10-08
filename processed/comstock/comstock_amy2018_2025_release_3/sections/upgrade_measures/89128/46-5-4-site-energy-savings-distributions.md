<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89128.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89128.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89128.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/89128.md | section: 5.4 Site Energy Savings Distributions | lines: 856-922 -->
## 5.4 Site Energy Savings Distributions

This section discusses site energy consumption for quality assurance/quality control purposes. Note that site energy savings can be useful for these purposes, but other factors should be considered when drawing conclusions, as they do not necessarily translate proportionally to source energy savings, greenhouse gas emissions avoided, or energy cost.

Figure 11 shows the percent savings distributions of the baseline ComStock models versus the HP-RTU + ASHP Boiler + DCV + HR + Economizers scenario by end use and fuel type for applicable models. In other words, each data point in the distribution represents the percent energy savings between a baseline ComStock model and the corresponding upgrade model with measures applied.

Most of the savings for the 'Other Fuel Heating' and 'Natural Gas Heating' categories are at 100% owing to replacing the combustion fuel-based system in the baseline with an all-electric heat pump system in the HP-RTU + ASHP Boiler + DCV + HR + Economizers scenario.

Some models unintuitively show 'Natural Gas Heating' and 'Other Fuel' heating penalties. Closer investigation shows that these models are exclusively 'PVAV with gas heat with electric reheat,' which did not receive the heat pump upgrades and only received one or more of the DCV, Heat/Energy Recovery, or Economizer upgrades. For this system type, the efficiency measures applied must have had a negative effect on heating loads. However, upon looking at site energy savings for this system type only, there are still positive site energy savings, meaning cooling savings have more than offset the heating penalty.

Figure 11. Percent site energy savings distribution for ComStock models with the HP-RTU + ASHP Boiler + DCV + HR + Economizers package (Package 5) applied by end use and fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89128.yaml
     source: 89128_images/image_000018_f869c89db64d25ba1e9666d61ad415ecc27ab83f09bdeb3e24716dd51ab418f8.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by end use and fuel type](89128_images/image_000018_f869c89db64d25ba1e9666d61ad415ecc27ab83f09bdeb3e24716dd51ab418f8.png)

Figure 11: horizontal violin-and-box plots of percent site energy savings by end use and fuel type, x-axis -150% to 100%, seventeen rows each labeled with its model count (natural gas heating n=193,783; electricity cooling n=280,728). Natural gas and other fuel heating cluster at 100% savings while electricity pumps and heat recovery show penalties. Section 5.4 explains the outliers.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

Pump electricity increased between the baseline and upgrade scenario, as expected, due to the addition of heat pump boilers to some models. This measure adds an additional circulation pump to the heat pump loop, increasing the required pump power. In addition, the ASHP boiler system operates at a lower supply temperature than the existing gas boiler it is replacing, which increases the required loop flow rate. Both factors can increase pumping energy.

Most buildings saw heating, cooling, and fan electricity savings due to higher efficiency performance of HP-RTUs compared with traditional RTUs, combined with the additional efficiency measures applied. However, some models saw heating electricity penalties. If a building began with 100% natural gas heating and was converted to 100% electric heating, it is not shown on Figure 11 in the electric heating end use row, as the electric heating penalty would be infinity. Rather, the buildings showing an electric heating penalty are ones that started with mostly natural gas heating but some small portion of electric resistance heating (such as electric baseboards in a vestibule). When those buildings were converted to fully electric heating via a heat pump, the electric heating penalty becomes very large. In most buildings that began with some electric heating, the addition of the heat pump resulted in positive energy savings, with a median around 30% savings.

Some models show negative heat recovery savings, noting that the heat recovery end use is for electricity used to operate enthalpy wheels. Additionally, the heat recovery end use includes added fan energy needed to overcome the heat exchanger. The negative energy savings are due to increased prevalence of heat recovery from the measure package, noting that this penalty is generally made up for in heating and cooling savings. However, the heat recovery end use makes up a very small portion of building stock energy usage (as was seen in Figure 9), so negative percentage savings in this end use has minimal impact.

Minimal differences are observed for water systems, refrigeration, interior lighting, and interior equipment, as these systems are not directly impacted by the upgrade package. However, some buildings show minor changes due only to subtle differences in ambient air temperature that affect the operation of these systems. The interior lighting end use shows a small number of samples with savings/penalties from applying this measure scenario. This is a known bug in the workflow as this measure does not impact the lighting end use. However, this bug affects very few buildings and therefore the impact is minimal.

Figure 12 shows the site energy savings distributions between the ComStock baseline and the HP-RTU + ASHP Boiler + DCV + HR + Economizers scenario by fuel type and total site energy. The total site energy savings distribution shows savings values generally between 15% and 35% for the 25 th and 75 th percentiles, respectively. Combined site energy savings alone is not a comprehensive assessment of electrification measures, so other considerations should be made as well.

Figure 12. Percent site energy savings distribution for ComStock models with the applied HP-RTU + ASHP Boiler + DCV + HR + Economizers package (Package 5) by fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89128.yaml
     source: 89128_images/image_000019_9281d85d662875890ff746202281ab92c15f1dfb53881900e86ef5ce420ba0fc.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by fuel type and total site energy](89128_images/image_000019_9281d85d662875890ff746202281ab92c15f1dfb53881900e86ef5ce420ba0fc.png)

Figure 12: horizontal violin-and-box plots of percent site energy savings by fuel, x-axis -160% to 100%, six rows - district cooling n=53, district heating n=93, other fuel n=329, natural gas n=5,789, electricity n=8,452 and site n=8,452. Natural gas and other fuel sit near 80% to 100%; the site row's interquartile range spans roughly 15% to 35%, per Section 5.4.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

The site electricity distribution shows some energy penalties. These are mostly buildings that changed from gas heat to electric heat, so the penalties are expected, noting that these buildings likely show reductions in other heating fuel types that were electrified. Some of this electricity penalty is reduced or mitigated through savings for cooling, fans, and heat recovery, depending on the building and its climate zone. Most of the buildings, however, show electricity savings, as a result of replacing existing systems with high-efficiency heat pumps combined with the other efficiency measures.

The 'Natural Gas' and 'Other Fuel' end uses show many models with near 100% savings. These are buildings that are completely electrified from the HP-RTU or ASHP Boiler measures and where gas is not used for other end uses. Models with less than 100% gas or other fuel savings generally have some nonapplicable gas HVAC system type in the baseline, or other end uses, such as water heating, that are not electrified through the HP-RTU or ASHP Boiler measures. Some models show negative natural gas site savings. As discussed earlier, this was found to be buildings that did not receive either heat pump upgrade, and the additional HVAC upgrades applied resulted in a heating penalty.

A small portion of buildings show negative site energy savings. Upon further investigation, these are almost exclusively buildings that did not receive either one of the heat pump upgrades, and only received one or more of the DCV, Heat/Energy Recovery, or Economizer upgrades. These upgrades must have had a negative impact on the site energy for these buildings, which could be related to climate zone, internal loads, or other unique aspects of those buildings.

Figure 13 shows the site energy savings distributions between the ComStock baseline and the HP-RTU + ASHP Boiler + DCV + HR + Economizers scenario by HVAC system present in the baseline building. While this package is applicable to 35 different HVAC systems, some systems got a more comprehensive upgrade than others. Buildings that began with a rooftop unit or boiler system underwent a full system swap out via the HP-RTU or ASHP Boiler measure, while other HVAC systems only received some combination of DCV, HR, and/or Economizers. The HVAC systems that show the largest site energy savings (median of 20-30% savings) after the upgrade package was applied are PSZ-AC systems and boiler systems because they were retrofitted with a heat pump, in addition to other advanced HVAC controls measures. Most other systems saw site energy savings in the range of 5-10% for the median building. A few outliers, primarily in boiler systems, saw negative site energy savings, which is a result of adding substantial electric heating load to the building.

Figure 13. Percent site energy savings distribution for ComStock models with the applied HP-RTU + ASHP Boiler + DCV + HR + Economizers package (Package 5) by baseline HVAC system

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89128.yaml
     source: 89128_images/image_000020_b8330c1d3c8d02b826251d328fdd09f98eded0422c2c7c6fa41edaadddce1e03.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by baseline HVAC system type](89128_images/image_000020_b8330c1d3c8d02b826251d328fdd09f98eded0422c2c7c6fa41edaadddce1e03.png)

Figure 13: horizontal violin-and-box plots titled Upgrade 32: Package 5 (unweighted), percent site energy savings on an x-axis from -20% to 70%, with 35 baseline HVAC system rows labeled by model count (PSZ-AC with gas coil n=133,433; PVAV with gas heat with electric reheat n=29,393). The PSZ-AC and boiler rows carry the highest medians, which Section 5.4 puts at 20-30%.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

