<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95006.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95006.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95006.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/95006.md | section: 4  Output Variables | lines: 416-461 -->
## 4  Output Variables

Table 4 includes a list of output variables that are calculated in ComStock. These variables are important in terms of understanding the differences between buildings with and without this packaged measure. These output variables can also be used to help understand the economics of the upgrade (e.g., return on investment) if cost information (i.e., material, labor, and maintenance costs for technology implementation) is available.

Table 4. Output Variables Calculated from the Measure Application

| Upgrade   | Variable Name                                                      | Description                                                                                                    |
|-----------|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| HP-RTU    | out.params.hvac_count_dx_cooling _XX_to_XX_kbtuh                   | Total number of direct expansion (DX) cooling units within a size bin. XXs are values which vary.              |
| HP-RTU    | out.params.hvac_count_dx_heating _XX_to_XX_kbtuh                   | Total number of DX heating units within a size bin. XXs are values which vary.                                 |
| HP-RTU    | out.params.hvac_count_heat_pumps _XX_to_XX_kbtuh                   | Total number of heat pump units within a size bin. XXs are values which vary.                                  |
| HP-RTU    | out.params.dx_cooling_average _cop..COP                            | Average operational COP (compressor only) of DX cooling models during simulation.                              |
| HP-RTU    | out.params.dx_cooling_capacity _tons..tons                         | Total tons of DX cooling modeled.                                                                              |
| HP-RTU    | out.params.dx_cooling_design _cop..COP                             | Average rated (compressor only) COP of DX cooling units at rated conditions.                                   |
| HP-RTU    | out.params.dx_heating_average _cop..COP                            | Average operational COP (compressor only) of DX cooling models during simulation.                              |
| HP-RTU    | out.params.dx_heating_average _minimum_operating _temperature..C   | Average compressor minimum heating lockout temperature, below which the heat pump heating will be disabled.    |
| HP-RTU    | out.params.dx_heating_average _total_cop..COP                      | Average effective COP of DX heating. This includes energy from the defrost cycle and any supplemental heating. |
| HP-RTU    | out.params.dx_heating_capacity _at_XXF..kBtu_per_hr                | Average available heat pump capacity at a given temperature. XXs are values which vary.                        |
| HP-RTU    | out.params.dx_heating_capacity _at_rated..kBtu_per_hr              | Average available heat pump capacity at rated temperature (47°F).                                              |
| HP-RTU    | out.params.dx_heating_design _cop..COP                             | Average design COP of heat pumps.                                                                              |
| HP-RTU    | out.params.dx_heating_design _cop_XXf..COP                         | Heat pump COP at given temperature, or rated conditions (47°F). XXs are values which vary.                     |
| HP-RTU    | out.params.dx_heating_fraction _electric_defrost                   | Fraction of heat pump electric defrost energy to DX heating energy.                                            |
| HP-RTU    | out.params.dx_heating_fraction _electric_supplemental              | Fraction of heat pump electric supplemental heating energy to DX heating energy.                               |
| HP-RTU    | out.params.dx_heating_supplemental _capacity_electric..kBtu_per_hr | Electric coil supplemental heating capacity.                                                                   |

| Upgrade            | Variable Name                                                 | Description                                                                                       |
|--------------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
|                    | out.params.dx_heating_supplemental _capacity_gas..kBtu_per_hr | Gas coil supplemental heating capacity.                                                           |
|                    | out.params.dx_heating_supplemental _capacity..kBtu_per_hr     | Total (gas or electric) supplemental heating capacity.                                            |
|                    | out.params.dx_heating_fraction _supplemental                  | Fraction of heat pump heating energy from supplemental heating.                                   |
|                    | out.params.dx_heating_total_dx _electric..J                   | Total heat pump heating electric load.                                                            |
|                    | out.params.dx_heating_total_dx _load..J                       | Total heat pump heating load.                                                                     |
|                    | out.params.dx_heating_total_load..J                           | Total heat pump system heating load.                                                              |
|                    | out.params.dx_heating_total _supplemental_load_gas..J         | Total heating output energy from gas supplemental coil.                                           |
|                    | out.params.dx_heating_total _supplemental_load_electric..J    | Total heating output energy from electric supplemental coil.                                      |
|                    | out.params.dx_heating_defrost _energy..kBtu                   | Total heat pump electricity energy for defrost.                                                   |
|                    | out.params.dx_heating_ratio _defrost                          | Ratio of heat pump defrost electricity to heat pump heating energy.                               |
|                    | out.params.hours_below _XXF..hr                               | Number of hours below given outdoor air temperature during simulation. XXs are values which vary. |
|                    | out.params.unitary_sys_cycling _ratio_cooling                 | Annual average cycling ratio for cooling operation                                                |
|                    | out.params.unitary_sys_cycling _ratio_heating                 | Annual average cycling ratio for heating operation                                                |
| Window replacement | out.params.ext_window_area                                    | Total external window area in m 2 .                                                               |
|                    | out.params.average_window _shgc                               | Average solar heat gain coefficient of all the windows in the building model.                     |
|                    | out.params.average_window _u_value                            | Average thermal conductance (in Btu/hr-ft 2 -°F) of all the windows in the building model.        |
|                    | out.params.average_window _vlt                                | Average visual light transmission.                                                                |
|                    | out.params.window_to_wall _ratio                              | Window-to-wall ratio.                                                                             |

