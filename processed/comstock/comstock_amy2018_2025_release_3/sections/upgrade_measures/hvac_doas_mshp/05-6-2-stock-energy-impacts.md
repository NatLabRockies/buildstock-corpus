<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/hvac_doas_mshp.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/hvac_doas_mshp.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/hvac_doas_mshp.html | corpus_version: 0396270 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/hvac_doas_mshp.md | section: 6.2  Stock Energy Impacts | lines: 288-381 -->
## 6.2  Stock Energy Impacts

The DOAS MSHP measure demonstrates 3.9% total site energy savings (169
TBtu) for the U.S. commercial building stock modeled in ComStock (Figure
10). The savings are primarily attributed to:

-   18% (81 TBtu) gas heating site energy savings

-   2% (6 TBtu) electricity heating site energy savings

-   6% (39 TBtu) electricity cooling site energy savings

-   8.7% (52 kBtu) fan electricity site energy savings.

![](./media/0b3098bc-c83d-4729-837e-fd9d2e773920.jpeg)

Figure 10. Comparison of annual site energy consumption between the ComStock baseline and the DOAS MSHP measure. Energy consumption is categorized both by fuel type and end use.

The site gas heating savings are attributed to switching applicable gas-heated systems to all-electric DOAS MSHP systems. This removes virtually all the gas heating from these buildings, except for the small amount that may be nonapplicable (e.g., kitchens). The site electricity heating savings are due to replacing electric resistance RTUs with higher-efficiency DOAS MSHP RTUs. The baseline RTUs have electric resistance heating with a COP of 1, whereas the MSHPs generally have much higher COPs. The DOAS ERVs or HRVs also reduce the ventilation heating loads by preconditioning the outdoor air with conditioned building exhaust air. Note that some baseline ComStock models already have a form of energy recovery if required by code. However, the site electricity savings are reduced due to switching many gas-heated RTU systems to DOAS MSHP systems, which simply adds more buildings using electric heating. As previously mentioned, ComStock currently uses more electric heating energy in the stock relative to CBECS 2012. Adjusting this could possibly cause the electric heating energy savings of the DOAS MSHP scenario to be negative, as it could reduce the prevalence of the electric resistance RTU systems, which are the primary driver of the heating electricity savings.

The site cooling electricity also shows savings. The cause of this is fourfold: (1) The MSHPs have very high SEER ratings (over 30), and will generally exceed the cooling efficiency of the replaced baseline RTUs. (2) The DX system in the DOAS uses energy code efficiencies from ASHRAE-90.1, which will also generally outperform the baseline RTU DX efficiencies. (3) The ERV or HRV in the DOAS reduces cooling loads for the incoming ventilation air, whereas the baseline RTUs only have ERVs or HRVs if they were required by the code year during the last HVAC replacement. (4) The MSHPs have variable speed fans, and generally lower fan power, which reduces the waste heat in the airstream off the fan motor potentially causing a small reduction in cooling consumption.

Lastly, the heat recovery end use shows an increase in energy consumption. This is due to the energy required for the enthalpy wheel in ERV systems. By adding more ERV systems, the aggregate energy consumption for this end use increases. However, heat recovery energy consumption is relatively small, both at the individual building level and the stock level.

# 7.  Site Energy Savings Distributions

This section discusses site energy consumption for QAQC purposes. Note that site energy savings can be useful for QAQC purposes, but other factors should be considered when drawing conclusions, as these do not necessarily translate proportionally to source energy savings or energy cost.

Figure 12 shows the percent savings distributions of the baseline ComStock models versus the MSHP models by end use and fuel type for applicable models. Minimal differences are observed for water systems and refrigeration, which see small changes in the baseline due only to minor changes in ambient air temperature that affect the operation of these systems. Most of the savings for the "Other Fuel Heating" and "Natural Gas Heating" categories are at 100%, simply due to replacing the combustion fuel-based system in the baseline with an all-electric heat pump system in the proposed run. The values that show savings less than 100% are models that have some fraction of the baseline combustion fuel RTU deemed not applicable. This is either due to the unit being in a kitchen or a partially conditioned space where traditional RTU sizing does not apply. A very small number of outliers show negative natural gas heating savings; one such model is based in Hawaii with very small heating loads (\<0.5 kbtu/ft\^2/year) and represents atypical heating operation with very small impact. It should be noted that percent savings calculations are based on the baseline value, so a small change in heating energy for a model with very small heating energy to begin with may show a high percent savings.

![](./media/335f0d97-9a2a-457e-897d-bd7438a7ec98.jpeg)

Figure 12. Percent site energy savings distribution for ComStock models with the applied roof insulation measure by end use and fuel type. The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

Figure 12 also shows a distribution of outliers (indicated by the dots above the distribution) with negative heating electric heating savings, some of which are over 100%. These are typically models where the baseline is primarily gas heated with very small amounts of electric heating usage in the baseline. Adding an electric-heated system such as a heat pump RTU causes an electric heating percent savings penalty due to fuel switching. As previously mentioned, the percent savings calculations are based on the original baseline consumption, so baseline models with primarily gas heat (but still a small amount of electric heat) can experience high electricity gas heating penalties.

Electricity for energy recovery also exhibits negative savings in many cases. It should first be noted that the electricity used for energy recovery is only for powering the energy recovery wheel and makes up a very small amount of stock energy usage (Figure 10). The increased energy for this end use represents an increase in the prevalence of ERV and is expected. The energy saved by the ERV systems generally far exceeds this additional energy consumed.

The electric heating distribution shows a median savings of around 70%. The electric heating savings here are primarily from replacing electric baseline RTUs with higher-efficiency MSHPs with HRVs or ERVs. These high percent savings are expected, as the MSHPs often have a COP that is 2--4 times higher than the electric resistance systems. The cooling savings range from about 35%--65% for the 25<sup>th</sup> and 75<sup>th</sup> percentiles. These are primarily attributed to savings from the ERV or HRV, as well as the high-efficiency variable speed compressors for the MSHPs. RTUs in the ComStock baseline primarily follow older energy codes (Figure 2) and therefore are often single stage with lower efficiencies. Replacing these systems with high-efficiency, variable speed (\>30 SEER) MSHPs is expected to show substantial cooling savings.

Figure 13 shows site percent energy savings by fuel type, including the total site energy savings. Aside from a few outlier points, the entire distribution shows total site energy savings, generally between 20% and 40% for the 25<sup>th</sup> and 75<sup>th</sup> percentiles. As mentioned previously, other factors should be considered when assessing site energy savings, especially for an electrification measure that involves changes to the heating fuel. The electricity distribution shows some degree of site energy penalties. These are mostly buildings that changed from gas heat to electric heat and are expected. Some of this electricity penalty is reduced or mitigated through savings for cooling, fans, and heat recovery, as discussed. Many of the buildings, however, show electricity savings. Some of these are buildings that had electric heating in the baseline; in these cases, the higher-efficiency DOAS MSHP system reduces electricity usage across multiple end uses. Others may have had gas heating in the baseline, but the savings from cooling and fans outweighed the increase in electric heating from electrifying the end use. These occurrences will be specific to the building and climate zone due to the complicated interactions involved. The combustion fuels show many models with near 100% savings. These are buildings that are completely electrified from this measure (because all gas heated systems in the baseline were applicable) and where gas is not used for other end uses. Models that show less than 100% gas or other fuel savings generally have some nonapplicable gas HVAC system in the baseline, or other end uses, such as water heating, that are not electrified though this measure. Total building electrification may require multiple solutions to achieve.

![](./media/bc073143-ff53-4323-bdb0-dc1871aa21b3.jpeg)

Figure 13. Percent site energy savings distribution for ComStock models with the applied roof insulation measure by fuel type. The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

# References

\[1\] R. C. Analytics, "Energy Efficiency Analysis of DX-DOAS in the Pacific Northwest," 2021.

\[2\] Northeast Energy Efficiency Program (NEEP), "ASHP." \[Online\]. Available: [https://ashp.neep.org/#!/product/25333/7/25000///0](https://ashp.neep.org/#!/product/25333/7/25000///0).
\[Accessed: 19-Mar-2023\].

\[3\] "ANSI/ASHRAE. 2019. ANSI/ASHRAE Standard 62.1-2019: Ventilation for Acceptable Indoor Air Quality."

\[4\] "Commercial Buildings Energy Consumption Survey (CBECS)," 2012.

\[5\] A. Parker *et al.*, "ComStock Documentation," Golden, CO, 2022.

\[6\] N. Resources Canada, "AIR-SOURCE HEAT PUMP SIZING AND SELECTION GUIDE." 2020.

\[7\] ASHRAE, *2015 Ashrae Handbook HVAC applications*. 2015.

\[8\] Northeast Energy Efficiency Partners (NEEP), "NEEP Cold Climate Air Source Heat Pump List." \[Online\]. Available:
[https://ashp.neep.org/#!/](https://ashp.neep.org/#!/). \[Accessed: 21-Mar-2023\].

\[9\] J. Pratt, M. Murphy, and N. O'Neil, "DO AS We Say (and As We Do):
Maximizing HVAC Efficiency, Flexibility, and Resiliency with High Efficiency Dedicated Outdoor Air Systems," in *Summer Study on Energy Efficiency in Buildings*, 2022.

\[10\] Nick Agopian, "ERV & HRV FROST THRESHOLDS AND CONTROL METHODS,"
2022.

\[11\] "Cambium \| Energy Analysis \| NREL." \[Online\]. Available:
[https://www.nlr.gov/analysis/cambium.html](https://www.nlr.gov/analysis/cambium.html). \[Accessed: 02-Sep-2022\].

\[14\] G. Vijayakumar *et al.*, "ANSI/RESNET/ICC 301-2022 - Standard for the Calculation and Labeling of the Energy Performance of Dwelling and Sleeping Units using an Energy Rating Index," Oceanside, CA, 2022.

# Appendix A

![](./media/792b1fd4-592b-4987-8aa7-af89068eeb42.jpeg)

Figure A-1. Site annual natural gas consumption of the ComStock baseline and the DOAS MSHP scenario by building type.

![](./media/5bc4189b-6b16-4a3d-b555-75352e779c2e.jpeg)

Figure A-2. Site annual natural gas consumption of the ComStock baseline and the DOAS MSHP scenario by census division.

![](./media/9c1e9851-85a6-47e9-9616-c8582b4ba17d.jpeg)

Figure A-3. Site annual electricity consumption of the ComStock baseline and the DOAS MSHP scenario by building type.

![](./media/1b8e777d-d934-44e5-89fa-9af4656f31ec.jpeg)

Figure A-4. Site annual electricity consumption of the ComStock baseline and the DOAS MSHP scenario by census division.
