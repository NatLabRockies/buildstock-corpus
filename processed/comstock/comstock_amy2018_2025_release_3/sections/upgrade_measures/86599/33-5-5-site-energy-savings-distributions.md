<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86599.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86599.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86599.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/86599.md | section: 5.5 Site Energy Savings Distributions | lines: 545-586 -->
## 5.5 Site Energy Savings Distributions

This section discusses site energy consumption for quality assurance/quality control purposes. Note that site energy savings can be useful for these purposes, but other factors should be considered when drawing conclusions, as these do not necessarily translate proportionally to source energy savings, greenhouse gas emissions avoided, or energy cost.

Figure 5 shows the percent savings distributions of the baseline ComStock models versus the High-Efficiency Envelope scenario by end use and fuel type for applicable models. Models are included in these distributions only if they experienced savings (or a penalty) for the specific distribution. Many end uses demonstrate a wide range of savings. In general, the energy efficiency measures in this package are expected to save heating and cooling energy. This is confirmed in the figure, with the median savings around 30% for natural gas heating, 45% for electric heating, and 15% for electric cooling. Heating savings are expected to be larger than cooling savings because of the larger temperature difference between inside and outside during heating season. The secondary effects are expected to be decreased fan and pump electricity used to move the air and water for heating and cooling. Both electricity for fans and pumps shows around a 5% to 10% median savings. The slight changes in energy consumption for heat recovery and heat rejection are minor third-order effects associated with the runtimes of the heating and cooling equipment.

Figure 5. Percent site energy savings distribution for ComStock models with the High-Efficiency Envelope upgrade package applied by end use and fuel type.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86599.yaml
     source: 86599_images/image_000007_ef113aecfaea2636221ff21c33a0c5821eb76a6025864fcacbf8ab8b40d76505.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by end use and fuel type](86599_images/image_000007_ef113aecfaea2636221ff21c33a0c5821eb76a6025864fcacbf8ab8b40d76505.png)

Figure 5: horizontal violin-and-box plot of percent site energy savings by end use and fuel type, x-axis -160% to 100%, one row per end use with model counts in the labels (electricity cooling n=328,853; natural gas heating n=219,351). Only models that saw a change are included. Section 5.5 gives the medians: roughly 30% for natural gas heating, 45% for electric heating and 15% for electric cooling.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

Some end uses show negative energy savings for a small portion of the savings distributions: other fuel; district heating; natural gas and electricity heating; and electricity cooling, pumps, and fans. Heating penalties are often found in buildings with mixed-fuel HVAC systems where large increases in insulation can change the heating profile of the building and cause one fuel to incur increased energy consumption while another fuel realizes savings. For this reason, a heating penalty in the savings distribution for a single fuel type does not mean the building experienced a net heating penalty when considering the impact on all heating fuels. Additionally, decreasing the SHGC via window replacement can block some beneficial solar heat gain and therefore increase heating load for a building. Whether annual heating savings are realized depends on a combination of factors, including the window to wall area, window orientation, thermostat set points, HVAC system, outdoor air temperatures, and amount of solar radiation affecting the window surface. Heating-only HVAC system types can be especially prone to energy penalties from lower SHGC because there is no cooling system to save energy from the decreased solar gains, although this does not reflect other potential such as thermal comfort or glare control.

Many models saw cooling savings. With reduced cooling loads due to increased insulation, a building's HVAC system will have to work less frequently to maintain indoor comfort. In climate zones where economizers are required, this can lead to longer periods where economizer mode can be active. When outdoor conditions are suitable for cooling, economizer mode will be more effective because the system can use more outdoor air to cool the building without resorting to mechanical cooling.

Some models experience increased cooling energy consumption, which is often due to increased insulation holding internally generated heat within the building during cooling season, which can cause an increased cooling load. In some cases, this can cause a net site energy penalty for the building, which is most common when the building's cooling requirements are much higher than the heating requirements. This effect is mitigated with the climate zone-specific insulation targets.

Fans and pumps follow the operation of the HVAC system, and models with heating or cooling penalties can also incur fan and pump penalties.

Figure 5 also shows especially high heating savings in some models. This generally occurs in building models with very low heating loads and energy consumption to begin with, where the increase in roof insulation removes most, or all, of whatever heating load there was. This can cause very high values in the percentage savings calculations.

Finally, some models saw an interior lighting electricity penalty. This is attributed to the lower VLT from the window measure impacting models with daylight controls. These models may not be able to turn down the interior lights as much or as often with lower VLT windows, which can increase lighting equivalent full load hours and therefore increase lighting energy consumption. Figure 6 shows the relationship between interior lighting electricity percent savings and daylight control fraction. Models with higher daylight control fraction generally see a higher interior lighting penalty. Furthermore, the design interior lighting power density does not change between the baseline and upgrade package scenarios, indicating the package is not impacting the interior lighting design. Equivalent full load hour output variables also show a 1:1 relationship between equivalent full load hour percent increase and interior lighting penalty, supporting the conclusion that lower VLT windows are causing the interior lighting energy consumption increase.

Figure 6. Daylight control fraction vs. percent savings for interior lighting electricity

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86599.yaml
     source: 86599_images/image_000008_8db3246416380a5125bb535bfc0e6303196c6c7c4dddbdc1190866e229b5fc37.png
     method: vision-description
     described: 2026-08-21 -->

![Scatter plot of daylight control fraction against interior lighting electricity savings](86599_images/image_000008_8db3246416380a5125bb535bfc0e6303196c6c7c4dddbdc1190866e229b5fc37.png)

Figure 6: scatter plot of daylight control fraction (y-axis 0 to 1.0) against interior lighting electricity savings (x-axis -0.65 to 0.00) for applicable models, densest near zero. Every point is a penalty rather than a saving, with the largest lighting increases at low control fractions. Note the x-axis is a fraction, not the percent the caption implies.

