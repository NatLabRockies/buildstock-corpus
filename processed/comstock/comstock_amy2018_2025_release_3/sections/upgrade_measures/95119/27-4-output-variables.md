<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95119.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95119.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95119.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/95119.md | section: 4  Output Variables | lines: 483-522 -->
## 4  Output Variables

Table 5 includes a list of output variables that are calculated in ComStock. These variables are important in terms of understanding the differences between buildings with and without the HPRTU with Lab Data measure applied. These output variables can also be used for understanding the economics of the upgrade (e.g., return on investment) if cost information (e.g., material, labor, and maintenance costs for technology implementation) is available.

Table 5. Output Variables Calculated From the Measure Application

| Upgrade         | Variable Name                                            | Description                                                                                                                                                                       |
|-----------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Roof Insulation | Energy Code Followed During Last Roof Replacement        | The energy code followed during the last roof replacement (or installation) for a building model, which dictates the roof performance properties for the ComStock baseline models |
|                 | stat.hvac_count_dx_cooling_XX_to_XX_kbtuh                | Total number of direct expansion (DX) cooling units within a size bin                                                                                                             |
|                 | stat.hvac_count_dx_heating_XX_to_XX_kbtuh                | Total number of DX heating units within a size bin                                                                                                                                |
|                 | stat.hvac_count_heat_pumps_XX_to_XX_kbtuh                | Total number of heat pump units within a size bin                                                                                                                                 |
|                 | stat.dx_cooling_average_cop..COP                         | Average operational COP (compressor only) of DX cooling models during simulation                                                                                                  |
|                 | stat.dx_cooling_capacity_tons..tons                      | Total tons of DX cooling modeled                                                                                                                                                  |
|                 | stat.dx_cooling_design_cop..COP                          | Average rated (compressor only) COP of DX cooling units at rated conditions                                                                                                       |
| HP-RTU          | stat.dx_heating_average_cop..COP                         | Average operational COP (compressor only) of DX cooling models during simulation                                                                                                  |
|                 | stat.dx_heating_average_minimum_operating_temperature..C | Average compressor minimum heating lockout temperature, below which the heat pump heating will be disabled (°C)                                                                   |
|                 | stat.dx_heating_average_total_cop..COP                   | Average effective COP of DX heating. This includes energy from the defrost cycle and any supplemental heating                                                                     |
|                 | stat.dx_heating_capacity_at_XXF..kBtu_per_hr             | Average available heat pump capacity at a given temperature (kBtu/h)                                                                                                              |
|                 | stat.dx_heating_capacity_at_rated..kBtu_per_hr           | Average available heat pump capacity at rated temperature (47°F)                                                                                                                  |

| Upgrade   | Variable Name                                               | Description                                                                     |
|-----------|-------------------------------------------------------------|---------------------------------------------------------------------------------|
|           | stat.dx_heating_design_cop..COP                             | Average design COP of heat pumps                                                |
|           | stat.dx_heating_design_cop_XXf..COP                         | Heat pump COP at a given temperature, or rated conditions (47°F)                |
|           | stat.dx_heating_fraction_electric_defrost                   | Fraction of heat pump electric defrost energy to DX heating energy              |
|           | stat.dx_heating_fraction_electric_supplemental              | Fraction of heat pump electric supplemental heating energy to DX heating energy |
|           | stat.dx_heating_supplemental_capacity_electric..kBtu_per_hr | Electric coil supplemental heating capacity (kBtu/h)                            |
|           | stat.dx_heating_supplemental_capacity_gas..kBtu_per_hr      | Gas coil supplemental heating capacity (kBtu/h)                                 |
|           | stat.dx_heating_supplemental_capacity..kBtu_per_hr          | Total (gas or electric) supplemental heating capacity (kBtu/h)                  |
|           | stat.dx_heating_fraction_supplemental                       | Fraction of heat pump heating energy from supplemental heating                  |
|           | stat.dx_heating_total_dx_electric..J                        | Total heat pump heating electric load (J)                                       |
|           | stat.dx_heating_total_dx_load..J                            | Total heat pump heating load (J)                                                |
|           | stat.dx_heating_total_load..J                               | Total heat pump system heating load (J)                                         |
|           | stat.dx_heating_total_supplemental_load_gas..J              | Total heating output energy from gas supplemental coil (J)                      |
|           | stat.dx_heating_total_supplemental_load_electric..J         | Total heating output energy from electric supplemental coil (J)                 |
|           | stat.dx_heating_defrost_energy..kBtu                        | Total heat pump electricity energy for defrost (kBtu)                           |
|           | stat.dx_heating_ratio_defrost                               | Ratio of heat pump defrost electricity to heat pump heating energy              |
|           | stat.hours_below_XXF..hr                                    | Number of hours below given outdoor air temperature during simulation           |

