<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/5_ResStockOutputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/5_ResStockOutputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/5_ResStockOutputs.md | section: Cost Multipliers | lines: 288-321 -->
## Cost Multipliers

The ResStock workflow calculates and outputs certain values to support the calculation of costs of implementation of upgrades and upgrade packages. These are values that are available to scale measure implementation cost—for example, the total square feet of exterior window area in a housing unit model sample that can be multiplied by a user-provided window cost per square foot for a specific measure to get a per-housing-unit measure cost. They are calculated from the building energy models. ResStock currently provides 21 such values, as listed in Table “ResStock cost multiplier output field names, units, and descriptions”. In published ResStock datasets, these cost multipliers are the fields that use the “out.params” prefix, for example “out.params.window_area_ft_2.” The exception is that “upgrade_costs.floor_area_conditioned_ft_2” has to-date been published as “in.sqft.”

<div id="table:cost_multipliers" data-source="5_ResStockOutputs.tex">

| **Field Name** | **Units** | **Description** |
|:---|:---|:---|
| upgrade_costs.door_area_ft_2 | ft<sup>2</sup> | Door Area |
| upgrade_costs.duct_unconditioned_surface_area_ft_2 | ft<sup>2</sup> | Duct Unconditioned Surface Area |
| upgrade_costs.floor_area_attic_ft_2 | ft<sup>2</sup> | Floor Area, Attic |
| upgrade_costs.floor_area_attic_insulation_increase_ft_2_delta_r_value | ft<sup>2</sup> \* $`\Delta`$ R-value | Floor Area, Attic \* Insulation Increase |
| upgrade_costs.floor_area_conditioned_ft_2 | ft<sup>2</sup> | Floor Area, Conditioned |
| upgrade_costs.floor_area_conditioned_infiltration_reduction_ft_2_delta_ach_50 | ft<sup>2</sup> \* $`\Delta`$ ACH50 | Floor Area, Conditioned \* Infiltration Reduction |
| upgrade_costs.floor_area_foundation_ft_2 | ft<sup>2</sup> | Floor Area, Foundation |
| upgrade_costs.floor_area_lighting_ft_2 | ft<sup>2</sup> | Floor Area, Lighting |
| upgrade_costs.flow_rate_mechanical_ventilation_cfm | cfm | Flow Rate, Mechanical Ventilation |
| upgrade_costs.rim_joist_area_above_grade_exterior_ft_2 | ft<sup>2</sup> | Rim Joist Area, Above-Grade, Exterior |
| upgrade_costs.roof_area_ft_2 | ft<sup>2</sup> | Roof Area |
| upgrade_costs.size_cooling_system_primary_k_btu_h | kBtu/h | Size, Cooling System Primary |
| upgrade_costs.size_heat_pump_backup_primary_k_btu_h | kBtu/h | Size, Heat Pump Backup Primary |
| upgrade_costs.size_heating_system_primary_k_btu_h | kBtu/h | Size, Heating System Primary |
| upgrade_costs.size_heating_system_secondary_k_btu_h | kBtu/h | Size, Heating System Secondary |
| upgrade_costs.size_water_heater_gal | gal | Size, Water Heater |
| upgrade_costs.slab_perimeter_exposed_conditioned_ft | ft | Slab Perimeter, Exposed, Conditioned |
| upgrade_costs.wall_area_above_grade_conditioned_ft_2 | ft<sup>2</sup> | Wall Area, Above-Grade, Conditioned |
| upgrade_costs.wall_area_above_grade_exterior_ft_2 | ft<sup>2</sup> | Wall Area, Above-Grade, Exterior |
| upgrade_costs.wall_area_below_grade_ft_2 | ft<sup>2</sup> | Wall Area, Below-Grade |
| upgrade_costs.window_area_ft_2 | ft<sup>2</sup> | Window Area |

ResStock cost multiplier output field names, units, and descriptions

</div>

