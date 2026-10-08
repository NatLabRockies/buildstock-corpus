<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86602.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86602.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86602.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/86602.md | section: 4  Output Variables | lines: 712-788 -->
## 4  Output Variables

Table 12 includes a list of output variables that are calculated in ComStock by the upgrades included in this upgrade package. These variables are important in terms of understanding the differences between buildings with and without the High Efficiency Envelope, Interior Lighting and Heat Pump upgrade package applied. These output variables can also be used for understanding the economics of the upgrades (e.g., return on investment) if cost information (i.e., material, labor, and maintenance costs for technology implementation) is available.

Table 12. Output Variables Calculated From the Upgrade Applications

| Variable Name                                     | Description                                                                                                                                                                       |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Window to Wall Ratio                              | Ratio of window area to exterior wall area for the building model                                                                                                                 |
| Window Type                                       | Name of window type, as described in Table 1                                                                                                                                      |
| Average Window SHGC                               | Average solar heat gain coefficient of all the windows in the building model                                                                                                      |
| Average Window U-Value                            | Average thermal conductance of all the windows in the building model (Btu/hr ft 2 F)                                                                                              |
| Window Area                                       | Total window area replaced by the upgrade (ft 2 )                                                                                                                                 |
| Target R-value                                    | Target insulation R-value based on climate zone (ft 2 -hr- R/Btu)                                                                                                                 |
| Insulation R-value per Inch                       | XPS R-value per inch (hr ft 2 R/Btu per inch)                                                                                                                                     |
| Required Insulation Thickness                     | Insulation thickness required to meet target R-value (in.)                                                                                                                        |
| Exterior Wall Insulation Area                     | Area of insulation added (ft 2 )                                                                                                                                                  |
| Energy Code Followed During Last Roof Replacement | The energy code followed during the last roof replacement (or installation) for a building model, which dictates the roof performance properties for the ComStock baseline models |
| Average Roof Absorptance                          | The average absorptance of all roof surfaces for a building model                                                                                                                 |

| Upgrade      | Variable Name                                            | Description                                                                                                     |
|--------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
|              | Average Roof U-Value                                     | The average thermal conductivity of all roof surfaces for a building model (Btu/hr ft 2 F)                      |
|              | Roof Area                                                | The exterior roof area for a building model (ft 2 )                                                             |
|              | Initial Lighting Power                                   | Initial power by lighting technology (W)                                                                        |
|              | Initial LPD                                              | Average building LPD before upgrade is applied (W/ft 2 )                                                        |
| LED Lighting | Final Lighting Generation                                | Lighting generation after upgrade is applied (should be Generation 5 if upgrade is applicable)                  |
|              | Final Lighting Power                                     | Final lighting power by technology (W)                                                                          |
|              | Final LPD                                                | Average building LPD after upgrade is applied (W/ft 2 )                                                         |
|              | stat.hvac_count_dx_cooling_XX_to_XX_kbtuh                | Total number of direct expansion (DX) cooling units within a size bin                                           |
|              | stat.hvac_count_dx_heating_XX_to_XX_kbtuh                | Total number of DX heating units within a size bin                                                              |
|              | stat.hvac_count_heat_pumps_XX_to_XX_kbtuh                | Total number of heat pump units within a size bin                                                               |
|              | stat.dx_cooling_average_cop..COP                         | Average operational COP (compressor only) of DX cooling models during simulation                                |
| HP-RTU       | stat.dx_cooling_capacity_tons..tons                      | Total tons of DX cooling modeled                                                                                |
|              | stat.dx_cooling_design_cop..COP                          | Average rated (compressor only) COP of DX cooling units at rated conditions                                     |
|              | stat.dx_heating_average_cop..COP                         | Average operational COP (compressor only) of DX cooling models during simulation                                |
|              | stat.dx_heating_average_minimum_operating_temperature..C | Average compressor minimum heating lockout temperature, below which the heat pump heating will be disabled (°C) |
|              | stat.dx_heating_average_total_cop..COP                   | Average effective COP of DX heating. This includes energy                                                       |

| Upgrade   | Variable Name                                               | Description                                                                     |
|-----------|-------------------------------------------------------------|---------------------------------------------------------------------------------|
|           |                                                             | from the defrost cycle and any supplemental heating                             |
|           | stat.dx_heating_capacity_at_XXF..kBtu_per_hr                | Average available heat pump capacity at a given temperature (kBtu/h)            |
|           | stat.dx_heating_capacity_at_rated..kBtu_per_hr              | Average available heat pump capacity at rated temperature (47°F)                |
|           | stat.dx_heating_design_cop..COP                             | Average design COP of heat pumps                                                |
|           | stat.dx_heating_design_cop_XXf..COP                         | Heat pump COP at given temperature, or rated conditions (47°F)                  |
|           | stat.dx_heating_fraction_electric_defrost                   | Fraction of heat pump electric defrost energy to DX heating energy              |
|           | stat.dx_heating_fraction_electric_supplemental              | Fraction of heat pump electric supplemental heating energy to DX heating energy |
|           | stat.dx_heating_supplemental_capacity_electric..kBtu_per_hr | Electric coil supplemental heating capacity (kBtu/h)                            |
|           | stat.dx_heating_supplemental_capacity_gas..kBtu_per_hr      | Gas coil supplemental heating capacity (kBtu/h)                                 |
| HP-RTU    | stat.dx_heating_supplemental_capacity..kBtu_per_hr          | Total (gas or electric) supplemental heating capacity (kBtu/h)                  |
|           | stat.dx_heating_fraction_supplemental                       | Fraction of heat pump heating energy from supplemental heating                  |
|           | stat.dx_heating_total_dx_electric..J                        | Total heat pump heating electric load (J)                                       |
|           | stat.dx_heating_total_dx_load..J                            | Total heat pump heating load (J)                                                |
|           | stat.dx_heating_total_load..J                               | Total heat pump system heating load (J)                                         |
|           | stat.dx_heating_total_supplemental_load_gas..J              | Total heating output energy from gas supplemental coil (J)                      |
|           | stat.dx_heating_total_supplemental_load_electric..J         | Total heating output energy from electric supplemental coil (J)                 |

| Upgrade   | Variable Name                          | Description                                                           |
|-----------|----------------------------------------|-----------------------------------------------------------------------|
|           | stat.dx_heating_ratio_defrost          | Ratio of heat pump defrost electricity to heat pump heating energy    |
|           | stat.hours_below_XXF..hr               | Number of hours below given outdoor air temperature during simulation |
|           | Heat pump capacity weighted design COP | COP of the heat pump at the rated design conditions                   |
|           | Heat pump average COP                  | Average heat pump COP                                                 |
|           | Heat pump total load                   | Total heating provided by heat pump (J)                               |
|           | Boiler total load                      | Total heating provided by boiler (J)                                  |
|           | Heat pump total electricity            | Total electricity consumption by heat pump (J)                        |
|           | Boiler total electricity               | Total electricity consumption by boiler (J)                           |
| Boiler    | Heat pump capacity                     | Heat pump capacity (kBtu/h)                                           |
|           | Count heat pumps                       | Count of heat pumps                                                   |
| ASHP      | Count heat pumps 0-300 kBtuh           | Count of heat pumps in the range of 0-300 kBtu/h capacity             |
|           | Count heat pumps 300-2,500 kBtuh       | Count of heat pumps in the range of 300-2,500 kBtu/h capacity         |
|           | Count heat pumps 2,500+ kBtuh          | Count of heat pumps with more than 2,500 kBtu/h capacity              |
|           | Hot water loop total load              | Total heating load in the hot water loop (J)                          |
|           | Hot water loop boiler fraction         | Fraction of heating load provided by boiler                           |
|           | Hot water loop heat pump fraction      | Fraction of heating load provided by heat pump                        |

