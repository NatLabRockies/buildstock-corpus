<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89042.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/89042.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/89042.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/89042.md | section: 4  Output Variables | lines: 546-586 -->
## 4  Output Variables

includes a list of output variables that are calculated in ComStock. These variables are important in terms of understanding the differences between buildings with and without the 'HP-RTU with standard performance' measure applied. These output variables can also be used for understanding the economics of the upgrade (e.g., return on investment) if cost information (i.e., material, labor, and maintenance costs for technology implementation) is available.

Table 6. Output Variables Calculated From the Measure Application

| Variable Name                                                      | Description                                                                                                    |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| out.params.hvac_count_dx_cooling_XX_to_XX_kbtuh                    | Total number of direct expansion (DX) cooling units within a size bin.                                         |
| out.params.hvac_count_dx_heating_XX_to_XX_kbtuh                    | Total number of DX heating units within a size bin.                                                            |
| out.params.hvac_count_heat_pumps_XX_to_XX_kbtuh                    | Total number of heat pump units within a size bin.                                                             |
| out.params.dx_cooling_average_cop..COP                             | Average operational COP (compressor only) of DX cooling models during simulation.                              |
| out.params.dx_cooling_capacity_tons..tons                          | Total tons of DX cooling modeled.                                                                              |
| out.params.dx_cooling_design_cop..COP                              | Average rated (compressor only) COP of DX cooling units at rated conditions.                                   |
| out.params.dx_heating_average_cop..COP                             | Average operational COP (compressor only) of DX cooling models during simulation.                              |
| out.params.dx_heating_average_minimum_operating_tempe rature..C    | Average compressor minimum heating lockout temperature, below which the heat pump heating will be disabled.    |
| out.params.dx_heating_average_total_cop..COP                       | Average effective COP of DX heating. This includes energy from the defrost cycle and any supplemental heating. |
| out.params.dx_heating_capacity_at_XXF..kBtu_per_hr                 | Average available heat pump capacity at a given temperature.                                                   |
| out.params.dx_heating_capacity_at_rated..kBtu_per_hr               | Average available heat pump capacity at rated temperature (47°F).                                              |
| out.params.dx_heating_design_cop..COP                              | Average design COP of heat pumps.                                                                              |
| out.params.dx_heating_design_cop_XXf..COP                          | Heat pump COP at given temperature, or rated conditions (47°F).                                                |
| out.params.dx_heating_fraction_electric_defrost                    | Fraction of heat pump electric defrost energy to DX heating energy.                                            |
| out.params.dx_heating_fraction_electric_supplemental               | Fraction of heat pump electric supplemental heating energy to DX heating energy.                               |
| out.params.dx_heating_supplemental_capacity_electric..kBt u_per_hr | Electric coil supplemental heating capacity.                                                                   |

| Variable Name                                                 | Description                                                            |
|---------------------------------------------------------------|------------------------------------------------------------------------|
| out.params.dx_heating_supplemental_capacity_gas..kBtu_p er_hr | Gas coil supplemental heating capacity.                                |
| out.params.dx_heating_supplemental_capacity..kBtu_per_hr      | Total (gas or electric) supplemental heating capacity.                 |
| out.params.dx_heating_fraction_supplemental                   | Fraction of heat pump heating energy from supplemental heating.        |
| out.params.dx_heating_total_dx_electric..J                    | Total heat pump heating electric load.                                 |
| out.params.dx_heating_total_dx_load..J                        | Total heat pump heating load.                                          |
| out.params.dx_heating_total_load..J                           | Total heat pump system heating load.                                   |
| out.params.dx_heating_total_supplemental_load_gas..J          | Total heating output energy from gas supplemental coil.                |
| out.params.dx_heating_total_supplemental_load_electric..J     | Total heating output energy from electric supplemental coil.           |
| out.params.dx_heating_defrost_energy..kBtu                    | Total heat pump electricity energy for defrost.                        |
| out.params.dx_heating_ratio_defrost                           | Ratio of heat pump defrost electricity to heat pump heating energy.    |
| out.params.hours_below_XXF..hr                                | Number of hours below given outdoor air temperature during simulation. |
| out.params.unitary_sys_cycling_ratio_cooling                  | Annual average cycling ratio for cooling operation                     |
| out.params.unitary_sys_cycling_ratio_heating                  | Annual average cycling ratio for heating operation                     |

