<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/hvac_doas_mshp.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/hvac_doas_mshp.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/hvac_doas_mshp.html | corpus_version: b5faf42 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/hvac_doas_mshp.md | section: 4.3  Limitations and Concerns | lines: 200-250 -->
## 4.3  Limitations and Concerns

Limited data exists for comprehensive performance maps for heat pump systems. The performance maps used in this study were derived from lab testing data, but generally exceed the performance of other available data points from NEEP's cold climate heat pump list \[8\], even for premium units. Part of this can be explained simply by comparing different units. Additionally. the EnergyPlus® COP data compares compress-only COP values that do not include supply fans. Overestimating the performance of the MSHPs can show savings beyond what is reasonable for available units. Expanding the body of data for MSHP performance maps, especially higher-efficiency variable speed systems, can enhance this type of modeling work and increase confidence in the modeled results. Performance maps can be very influential to heat pump modeling results.

ComStock has limited assumptions for "once-through" RTU systems that exhaust air at a different location than the RTU. ComStock does assume some exhaust air for kitchens and bathrooms, but no specific validation has been made to ComStock to ensure that the prevalence of once-through systems aligns with the building stock. Underestimating once-through systems may cause an overestimation of the exhaust air available for energy recovery, which may overestimate savings associated with energy recovery.

Lastly, relative to CBECS 2012, the ComStock baseline currently underestimates gas heating energy, overestimates electric heating energy, and underestimates heating energy generally. This could partly be due to comparing the stock at different years, including different weather years. These discrepancies, if we assume CBECS to be a reasonable representation of the commercial building stock, can impact both applicability and stock savings results.

# 5.  Output Variables

Table 4 includes a list of output variables that are calculated in ComStock. These variables are important in terms of understanding the differences between buildings with and without the DOAS MSHP measure applied. These output variables can also be used for understanding the economics of the upgrade (e.g., return on investment) if cost information (i.e., material, labor, and maintenance costs for technology implementation) is available.

Table 4. Output Variables Calculated From the Measure Application

| **Variable Name** | **Description** |
|---|---|
| stat.hvac_count_dx_cooling_XX_to_XX_kbtuh | Total number of DX cooling units within a size bin. |
| stat.hvac_count_dx_heating_XX_to_XX_kbtuh | Total number of DX heating units within a size bin. |
| stat.hvac_count_heat_pumps_XX_to_XX_kbtuh | Total number of heat pump units within a size bin. |
| stat.dx_cooling_average_cop..COP | Average operational COP (compressor only) of DX cooling models during simulation. |
| stat.dx_cooling_capacity_tons..tons | Total tons of DX cooling modeled. |
| stat.dx_cooling_design_cop..COP | Average rated (compressor only) COP of DX cooling units at rated conditions. |
| stat.dx_heating_average_cop..COP | Average operational COP (compressor only) of DX cooling models during simulation. |
| stat.dx_heating_average_minimum_operating_temperature..C | Average compressor minimum heating lockout temperature, below which the heat pump heating will be disabled. |
| stat.dx_heating_average_total_cop..COP | Average effective COP of DX heating. This includes energy from the defrost cycle and any supplemental heating. |
| stat.dx_heating_capacity_at_XXF..kBtu_per_hr | Average available heat pump capacity at a given temperature. |
| stat.dx_heating_capacity_at_rated..kBtu_per_hr | Average available heat pump capacity at rated temperature (47°F). |
| stat.dx_heating_design_cop..COP | Average design COP of heat pumps. |
| stat.dx_heating_design_cop_XXf..COP | Heat pump COP at given temperature, or rated conditions (47°F). |
| stat.dx_heating_fraction_electric_defrost | Fraction of heat pump electric defrost energy to DX heating energy. |
| stat.dx_heating_fraction_electric_supplemental | Fraction of heat pump electric supplemental heating energy to DX heating energy. |
| stat.dx_heating_supplemental_capacity_electric..kBtu_per_hr | Electric coil supplemental heating capacity. |
| stat.dx_heating_supplemental_capacity_gas..kBtu_per_hr | Gas coil supplemental heating capacity. |
| stat.dx_heating_supplemental_capacity..kBtu_per_hr | Total (gas or electric) supplemental heating capacity. |
| stat.dx_heating_fraction_supplemental | Fraction of heat pump heating energy from supplemental heating. |
|  |
| stat.dx_heating_total_dx_electric..J | Total heat pump heating electric load. |
| stat.dx_heating_total_dx_load..J | Total heat pump heating load. |
| stat.dx_heating_total_load..J | Total heat pump system heating load. |
| stat.dx_heating_total_supplemental_load_gas..J | Total heating output energy from gas supplemental coil. |
| stat.dx_heating_total_supplemental_load_electric..J | Total heating output energy from electric supplemental coil. |
| stat.dx_heating_defrost_energy..kBtu | Total heat pump electricity energy for defrost. |
| stat.dx_heating_ratio_defrost | Ratio of heat pump defrost electricity to heat pump heating energy. |
| stat.hours_below_XXF..hr | Number of hours below given outdoor air temperature during simulation. |

# 6.  Results

In this section, results are presented both at the stock level and for individual buildings through savings distributions. Stock-level results include the combined impact of all the analyzed buildings in ComStock, including buildings that are not applicable to this measure. Therefore do not represent the energy savings of a particular building. Stock-level results should not be interpreted as the savings that a building might realize by implementing the DOAS MSHP measure.

Total site energy savings are also presented in this section. Total site energy savings can be a useful metric, especially for quality assurance/quality control (QAQC), but this metric on its own can have limitations for drawing conclusions. Further context should be considered, as site energy savings alone do not necessarily translate proportionally to savings for a particular fuel type (e.g., gas or electricity), source energy savings, or cost savings. This is especially important when a measure impacts multiple fuel types or causes decreased consumption of one fuel type and increased consumption of another. Many factors should be considered when analyzing the impact of an energy efficiency or electrification strategy, depending on the use case.

