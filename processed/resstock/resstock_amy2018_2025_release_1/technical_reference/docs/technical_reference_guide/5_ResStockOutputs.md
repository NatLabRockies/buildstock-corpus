<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/5_ResStockOutputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/5_ResStockOutputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 -->
# ResStock Outputs

ResStock produces a range of results around energy, housing characteristics, schedules, emissions, and costs. This section overviews the outputs available in the latest ResStock data release (2024 release 2). The data dictionary that summarizes these outputs is available with the [data release](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2024/resstock_amy2018_release_2/data_dictionary.tsv).

## Building Characteristics

The ResStock workflow generates a sample of residential housing units using the conditional distributions and sampling methodology described in Section “Sampling Methodology”. Each housing unit sample is specified using a set of characteristics, which include location, housing type, vintage, heating fuel, building size and geometry, materials, information on the HVAC system, insulation, infiltration, appliances, as well as information on occupant demographics and behavior. These characteristics are used for the model creation process, but they are also available as metadata associated with the results. The metadata is useful for performing analysis and slicing the data into segments. Some characteristics directly impact the OpenStudio model creation (e.g., wall insulation levels), whereas others are meta-parameters used as tags (e.g., ISO/RTO region) or as characteristics that correlate with other energy-relevant characteristics (e.g., vintage). Each of these characteristics is described in detail in Section “Housing Characteristics and Inputs”, and are summarized in Table “ResStock building characteristic output field names and descriptions”. In published ResStock datasets, these housing characteristics are the fields that use the “in” prefix followed by the housing characteristic name, for example “in.windows” for the Windows characteristic. If an upgrade or measure changes a housing characteristic, the post-upgrade characteristic uses the “upgrade” prefix, for example “upgrade.windows.”

Most national ResStock data releases have approximately one sample for every 250 housing units that actually exist in the modeled geography, though this can vary if the sample size is increased or decreased. Taken together, the set of samples describes the housing stock with its intrinsic variety and is used as both an output of ResStock and an input to further steps in the ResStock workflow (see Section “ResStock Workflow” for more information about the workflow).

Note that ResStock assigns certain characteristics that are not always used. Two examples of this are *cooling setpoint* in housing units with no cooling system, and *clothes washer usage level* in housing units with no clothes washer. This doesn’t impact the building energy models, this is merely a mechanism that allows for variability in probability distributions if the schedules are used for an upgrade. These characteristics, however, can lead to confusion because they’re preserved in the metadata as being assigned even if they’re not modeled. For further discussion see the the BuildStock Batch [Upgrade Scenario](https://buildstockbatch.readthedocs.io/en/v2023.10.0/project_defn.html#upgrade-scenarios) documentation.

<div id="table:hc_output_fields" data-source="5_ResStockOutputs.tex">

| **Field Name** | **Field Description** |
|:---|:---|
| in.ahs_region | American Housing Survey region |
| in.aiannh_area | The sample is or is not located in census-designated American Indian/Alaska Native/Native Hawaiian Area |
| in.area_median_income | Area median income of the household occupying the housing unit |
| in.ashrae_iecc_climate_zone_2004 | IECC climate zone according to ASHRAE 169 in 2004 and IECC in 2012 |
| in.ashrae_iecc_climate_zone_2004_sub_cz_split | Climate zone according to ASHRAE 169 in 2004 and IECC in 2012, where climate zone 2A is split between counties in TX, LA versus FL, GA, AL, and MS and climate zone 1A is split between FL and HI |
| in.bathroom_spot_vent_hour | Bathroom spot ventilation daily start hour |
| in.battery | The presence, size, location, and efficiency of an on-site battery (not modeled in 2024.2 dataset) |
| in.bedrooms | Number of bedrooms |
| in.building_america_climate_zone | Building America climate zone |
| in.cec_climate_zone | California Energy Code climate zone |
| in.ceiling_fan | Presence and energy usage of ceiling fans at medium speed |
| in.census_division | 2010 U.S. Census Division |
| in.census_division_recs | Census Division as used in RECS 2015 |
| in.census_region | 2010 U.S. Census Region |
| in.city | The census-designated city where the sample is located |
| in.clothes_dryer | The presence, rated efficiency, and fuel type of the clothes dryer in the housing unit |
| in.clothes_dryer_usage_level | Clothes dryer energy usage level multiplier |
| in.clothes_washer | Presence and rated efficiency of the clothes washer |
| in.clothes_washer_presence | Presence of clothes washer |
| in.clothes_washer_usage_level | Clothes washer energy usage level multiplier |
| in.cooking_range | Presence and fuel type of the cooking range |
| in.cooking_range_usage_level | Cooking range energy usage level multiplier |
| in.cooling_setpoint | Base cooling setpoint with no offset applied |
| in.cooling_setpoint_has_offset | Presence of cooling setpoint offset |
| in.cooling_setpoint_offset_magnitude | The magnitude of cooling setpoint offset |
| in.cooling_setpoint_offset_period | The period during which the cooling setpoint offset is applied |
| in.cooling_unavailable_days | The number of days in a year the cooling system is unavailable. |
| in.corridor | Type of corridor |
| in.county | County GISJOIN identifier |
| in.county_and_puma | The GISJOIN identifier for the County and the PUMA that the sample is located |
| in.dehumidifier | Presence, water removal rate, and humidity setpoint of dehumidifier (not modeled in 2024.2 dataset) |
| in.dishwasher | Presence and rated efficiency of dishwasher |
| in.dishwasher_usage_level | Dishwasher energy usage level multiplier |
| in.door_area | Area of exterior doors |
| in.doors | Exterior door material and properties |
| in.duct_leakage_and_insulation | Duct insulation and leakage to outside from the portion of ducts in unconditioned spaces |
| in.duct_location | Location of duct system |
| in.eaves | Depth of roof eaves |
| in.electric_panel_breaker_space_total_count | Total breaker spaces on electric panel |
| in.electric_panel_service_rating | Electrical panel service or max current rating (A) |
| in.electric_panel_service_rating_bin | Electrical panel service or max current rating in bins (A) |
| in.electric_vehicle_battery | The type of battery used by EV |
| in.electric_vehicle_charge_at_home | Percentage of EV charging that occurs at home |
| in.electric_vehicle_charger | The type of charger used by EV |
| in.electric_vehicle_miles_traveled | Annual miles traveled by EV |
| in.electric_vehicle_outlet_access | The type of outlet access available for EV |
| in.electric_vehicle_ownership | Whether the EV is present or not |
| in.energystar_climate_zone_2023 | Climate zones for windows, doors, and skylights per ENERGY STAR guidelines as of 2023 |
| in.federal_poverty_level | Federal poverty level of the household occupying the housing unit |
| in.generation_and_emissions_assessment_region | Generation and carbon emissions assessment (GEA) region from Cambium 2023 |
| in.geometry_attic_type | Type of attic |
| in.geometry_building_horizontal_location_mf | Location of the multifamily unit horizontally within the building (left, middle, right) |
| in.geometry_building_horizontal_location_sfa | Location of the single-family attached unit horizontally within the building (left, middle, right) |
| in.geometry_building_level_mf | Location of the multifamily unit vertically within the building (bottom, middle, top) |
| in.geometry_building_number_units_mf | Number of units in the multifamily building in which the housing unit is located |
| in.geometry_building_number_units_sfa | Number of units in the single-family attached building in which housing unit is located |
| in.geometry_building_type_acs | American Community Survey building type |
| in.geometry_building_type_height | RECS 2009 building type with multifamily buildings split out by low-rise, mid-rise, and high-rise |
| in.geometry_building_type_recs | PUMS 2019 building type |
| in.geometry_floor_area | Finished floor area bin (American Housing Survey) |
| in.geometry_floor_area_bin | Finished floor area bin |
| in.geometry_foundation_type | Type of building foundation |
| in.geometry_garage | Presence and size of an attached garage |
| in.geometry_space_combination | Valid combinations of building type, building level MF, attic, foundation, and garage |
| in.geometry_stories | Number of building stories in which housing unit is located |
| in.geometry_stories_low_rise | Number of building stories for low rise building in which housing unit is located |
| in.geometry_story_bin | The building in which housing unit is located has 8 or more versus fewer than 8 stories |
| in.geometry_wall_exterior_finish | Exterior wall finish material and color |
| in.geometry_wall_type | Exterior wall material |
| in.ground_thermal_conductivity | The thermal conductivity of the ground using in foundation and geothermal heat pump heat transfer calculations |
| in.has_pv | Presence of rooftop PV |
| in.heating_fuel | Fuel used for primary heating |
| in.heating_setpoint | Baseline heating setpoint with no offset applied |
| in.heating_setpoint_has_offset | Presence of heating setpoint offset |
| in.heating_setpoint_offset_magnitude | The magnitude of heating setpoint offset |
| in.heating_setpoint_offset_period | The period during which the heating setpoint offset is applied |
| in.heating_unavailable_days | The number of days in a year the heating system is unavailable. |
| in.holiday_lighting | Presence, energy usage, and schedule of holiday lighting |
| in.hot_water_distribution | Hot water piping material and insulation level |
| in.hot_water_fixtures | Hot water fixture usage and flow levels |
| in.household_has_tribal_persons | The housing unit houses at least one Tribal person |
| in.hvac_cooling_efficiency | Presence and efficiency of cooling system |
| in.hvac_cooling_partial_space_conditioning | The fraction of the finished floor area that is cooled by the cooling system |
| in.hvac_cooling_type | Presence and type of cooling system |
| in.hvac_has_ducts | Presence of ducts |
| in.hvac_has_shared_system | Presence of shared HVAC system |
| in.hvac_has_zonal_electric_heating | Presence of electric baseboard heating |
| in.hvac_heating_efficiency | Presence and efficiency of primary heating system |
| in.hvac_heating_type | Presence and type of primary heating system |
| in.hvac_heating_type_and_fuel | Presence, type, and fuel of primary heating system |
| in.hvac_secondary_heating_efficiency | Presence and efficiency of secondary heating system |
| in.hvac_secondary_heating_fuel | Secondary HVAC system heating type and fuel |
| in.hvac_secondary_heating_partial_space_conditioning | Fraction of heat load served by secondary heating system (not modeled in 2024.2 baseline dataset) |
| in.hvac_shared_efficiencies | Presence and efficiency of shared HVAC system |
| in.hvac_system_is_faulted | Not used |
| in.hvac_system_single_speed_ac_airflow | Not used |
| in.hvac_system_single_speed_ac_charge | Not used |
| in.hvac_system_single_speed_ashp_airflow | Not used |
| in.hvac_system_single_speed_ashp_charge | Not used |
| in.income | Income bin of the household occupying the housing unit |
| in.income_recs_2015 | Income bin of the household occupying the housing unit aligned with the 2015 U.S. EIA RECS |
| in.income_recs_2020 | Income bin of the household occupying the housing unit aligned with the 2020 U.S. EIA RECS |
| in.infiltration | Air leakage rates for the living and garage spaces |
| in.insulation_ceiling | Ceiling insulation level (between the living space and unconditioned attic) |
| in.insulation_floor | Floor insulation level |
| in.insulation_foundation_wall | Foundation walls insulation level |
| in.insulation_rim_joist | Insulation level for rim joists |
| in.insulation_roof | Finished roof insulation level between roof and conditioned space |
| in.insulation_slab | Slab insulation level |
| in.insulation_wall | Wall construction type and insulation level |
| in.interior_shading | Fraction of the window area shaded from the interior in the summer and winter |
| in.iso_rto_region | ISO or RTO region |
| in.lighting | Fraction of lighting types |
| in.lighting_interior_use | Interior lighting usage relative to the national average |
| in.lighting_other_use | Exterior and garage lighting usage relative to the national average |
| in.location_region | Custom ResStock region |
| in.mechanical_ventilation | Mechanical ventilation type and efficiency |
| in.misc_extra_refrigerator | Presence and rated efficiency of extra refrigerator |
| in.misc_freezer | Presence and rated efficiency of standalone freezer |
| in.misc_gas_fireplace | Presence of gas fireplace |
| in.misc_gas_grill | Presence of gas grill |
| in.misc_gas_lighting | Presence of exterior gas lighting |
| in.misc_hot_tub_spa | Presence and fuel type of hot tub |
| in.misc_pool | Presence of pool |
| in.misc_pool_heater | Presence and fuel type of pool heater |
| in.misc_pool_pump | Presence and size of pool pump |
| in.misc_well_pump | Presence and efficiency of well pump |
| in.natural_ventilation | Schedule of natural ventilation from windows |
| in.neighbors | Presence and distance between the housing unit and the nearest neighbors to the left and right. |
| in.occupants | The number of occupants living in the housing unit |
| in.orientation | Orientation of the building |
| in.overhangs | Presence, depth, and location of window overhangs |
| in.plug_load_diversity | Plug load diversity multiplier relative to the national average |
| in.plug_loads | Plug load usage level relative to the national average |
| in.puma | The 2010 U.S. Census PUMA where the sample is located |
| in.puma_metro_status | The PUMA metropolitan status |
| in.pv_orientation | Presence and orientation of rooftop PV system |
| in.pv_system_size | Presence and size of rooftop PV system |
| in.radiant_barrier | Presence of radiant barrier in attic |
| in.range_spot_vent_hour | Range spot ventilation daily start hour |
| in.reeds_balancing_area | Regional Energy Deployment System Model balancing area |
| in.refrigerator | The presence and rated efficiency of the primary refrigerator |
| in.refrigerator_usage_level | Refrigerator energy usage level multiplier |
| in.roof_material | Roof material type |
| in.solar_hot_water | Presence, size, and location of solar hot water system |
| in.sqft | Finished floor area of the representative housing unit |
| in.state | State |
| in.tenure | The tenancy (owner or renter) of the household occupying the housing unit |
| in.units_represented | Number of housing units the building model represents (this field is no longer used) |
| in.usage_level | Usage of major appliances relative to the national average |
| in.vacancy_status | Presence of occupants |
| in.vintage | Range in which the building was constructed |
| in.vintage_acs | Range in which the building was constructed using ACS bins |
| in.water_heater_efficiency | Efficiency, type, and heating fuel of water heater |
| in.water_heater_fuel | Water heater fuel |
| in.water_heater_in_unit | Individual water heater present or not present in the housing unit that solely serves the specific housing unit |
| in.water_heater_location | Water heater location for the housing unit if applicable |
| in.weather_file_city | City of weather file |
| in.window_areas | Window to wall ratios of the front, back, left, and right walls |
| in.windows | Construction type and efficiency levels of windows |

ResStock building characteristic output field names and descriptions

</div>

In addition to the housing characteristics themselves, several other ResStock outputs receive the “in.” prefix. These are inputs that are not provided as housing characteristics, but that are necessary inputs to the model. Most of these values are specified in the [project configuration file](https://github.com/NREL/resstock/blob/v3.2.0-2024.2/project_national/EUSSRR2_project_500k_AMY2018.yml).

<div id="table:supplmentary_input_fields" data-source="5_ResStockOutputs.tex">

| **Field Name** | **Field Description** |
|:---|:---|
| in.emissions_electricity_folders | Relative paths of electricity emissions factor schedule files with hourly values. Paths are relative to the resources folder. If multiple scenarios, use a comma-separated list. File names must contain GEA region names. |
| in.emissions_electricity_units | Electricity emissions factors units. If multiple scenarios, use a comma-separated list. Only lb/MWh and kg/MWh are allowed. |
| in.emissions_electricity_values_or_filepaths | Electricity emissions factors values, specified as either an annual factor or an absolute/relative path to a file with hourly factors. If multiple scenarios, use a comma-separated list. |
| in.emissions_fossil_fuel_units | Fossil fuel emissions factors units. If multiple scenarios, use a comma-separated list. Only lb/MBtu and kg/MBtu are allowed. |
| in.emissions_fuel_oil_values | Fuel oil emissions factors values, specified as an annual factor. If multiple scenarios, use a comma-separated list. |
| in.emissions_natural_gas_values | Natural gas emissions factors values, specified as an annual factor. If multiple scenarios, use a comma-separated list. |
| in.emissions_propane_values | Propane emissions factors values, specified as an annual factor. If multiple scenarios, use a comma-separated list. |
| in.emissions_scenario_names | Names of emissions scenarios. If multiple scenarios, use a comma-separated list. |
| in.simulation_control_run_period_begin_day_of_month | The starting day of the starting month for the annual run period. |
| in.simulation_control_run_period_begin_month | The starting month number (1 = January, 2 = February, etc.) for the annual run period. |
| in.simulation_control_run_period_calendar_year | The calendar year that determines the start day of week. |
| in.simulation_control_run_period_end_day_of_month | The ending day of the ending month for the annual run period. |
| in.simulation_control_run_period_end_month | The end month number (1 = January, 2 = February, etc.) for the annual run period. |
| in.simulation_control_timestep | Value must be a divisor of 60. |
| in.utility_bill_detailed_filepaths | n/a |
| in.utility_bill_electricity_filepaths | n/a |
| in.utility_bill_electricity_fixed_charges | Electricity utility bill monthly fixed charges. If multiple scenarios, use a comma-separated list. |
| in.utility_bill_electricity_marginal_rates | Electricity utility bill marginal rates. If multiple scenarios, use a comma-separated list. |
| in.utility_bill_fuel_oil_fixed_charges | Fuel oil utility bill monthly fixed charges. If multiple scenarios, use a comma-separated list. |
| in.utility_bill_fuel_oil_marginal_rates | Fuel oil utility bill marginal rates. If multiple scenarios, use a comma-separated list. |
| in.utility_bill_natural_gas_fixed_charges | Natural gas utility bill monthly fixed charges. If multiple scenarios, use a comma-separated list. |
| in.utility_bill_natural_gas_marginal_rates | Natural gas utility bill marginal rates. If multiple scenarios, use a comma-separated list. |
| in.utility_bill_propane_fixed_charges | Propane utility bill monthly fixed charges. If multiple scenarios, use a comma-separated list. |
| in.utility_bill_propane_marginal_rates | Propane utility bill marginal rates. If multiple scenarios, use a comma-separated list. |
| in.utility_bill_scenario_names | Names of utility bill scenarios. If multiple scenarios, use a comma-separated list. If multiple scenarios, use a comma-separated list. |
| in.utility_bill_simple_filepaths | Relative paths of simple utility rates. Paths are relative to the resources folder. If multiple scenarios, use a comma-separated list. |
| in.weather_file_latitude | Latitude of location of weather file. |
| in.weather_file_longitude | Longitude of location of weather file. |

ResStock building characteristic output field names and descriptions

</div>

## Energy Consumption by Fuel and End Use

The ResStock workflow models each housing unit sample in OpenStudio and EnergyPlus to produce energy consumption of each model at subhourly time steps and then processes the results into ResStock outputs. These outputs are produced by fuel type (e.g., electricity, natural gas) and end use (e.g., lighting, heating). Totals are calculated for each fuel and for all fuels combined. For electricity and all fuels combined, net totals are also calculated, which incorporate the impacts of on-site photovoltaics. The full list of energy consumption outputs from the ResStock workflow is available in Table “ResStock energy output field names, units, and descriptions”. Note that to date, ResStock has included only consumption of electricity, natural gas, propane, and fuel oil—excluding on-site consumption, wood, coal, or other fuels in its modeling, although the workflow is set up to include these additional fuels. Future releases will likely include wood.

As an output, the energy consumption results are all preceded with an “out.” prefix, followed by either the fuel type (e.g., “out.electricity.”) or “total.” if it is an aggregate of all fuel types, and then the end use, “net.” or “total.” if it is an aggregate of all end uses in that fuel type.

<div id="table:results_output_fields" data-source="5_ResStockOutputs.tex">

| **Field Name** | **Units** | **Field Description** |
|:---|:---|:---|
| out.electricity.ceiling_fan.energy_consumption.kwh | kWh | Electricity consumed by ceiling fans |
| out.electricity.clothes_dryer.energy_consumption.kwh | kWh | Electricity consumed by clothes dryers |
| out.electricity.clothes_washer.energy_consumption.kwh | kWh | Electricity consumed by clothes washers |
| out.electricity.cooling.energy_consumption.kwh | kWh | Electricity consumed by cooling systems; excludes usage by fans/pumps |
| out.electricity.cooling_fans_pumps.energy_consumption.kwh | kWh | Electricity consumed by supply fan (air distribution) or circulating pump (geothermal loop) during cooling |
| out.electricity.dishwasher.energy_consumption.kwh | kWh | Electricity consumed by dishwashers |
| out.electricity.electric_vehicle_charging.energy_consumption.kwh | kWh | Electricity consumed by charging electric vehicles |
| out.electricity.freezer.energy_consumption.kwh | kWh | Electricity consumed by standalone freezers |
| out.electricity.heating.energy_consumption.kwh | kWh | Electricity consumed by heating systems; excludes usage by fans/pumps |
| out.electricity.heating_fans_pumps.energy_consumption.kwh | kWh | Electricity consumed by supply fan (air distribution) or circulating pump (hydronic distribution or geothermal loop) during heating |
| out.electricity.heating_hp_bkup.energy_consumption.kwh | kWh | Electricity consumed by heat pump backup; excludes usage by heat pump backup fans/pumps |
| out.electricity.heating_hp_bkup_fa.energy_consumption.kwh | kWh | Electricity consumed by supply fan (air distribution) or circulating pump (hydronic distribution) during heat pump backup |
| out.electricity.hot_water.energy_consumption.kwh | kWh | Electricity consumed by hot water system excludes recirculation pump and solar thermal pump |
| out.electricity.lighting_exterior.energy_consumption.kwh | kWh | Electricity consumed by exterior lighting |
| out.electricity.lighting_garage.energy_consumption.kwh | kWh | Electricity consumed by lighting in the garage |
| out.electricity.lighting_interior.energy_consumption.kwh | kWh | Electricity consumed by interior lighting |
| out.electricity.mech_vent.energy_consumption.kwh | kWh | Electricity consumed by mechanical ventilation system |
| out.electricity.net.energy_consumption.kwh | kWh | Total electricity consumed subtracts any power produced by PV or generators |
| out.electricity.permanent_spa_heat.energy_consumption.kwh | kWh | Electricity consumed by spa heating |
| out.electricity.permanent_spa_pump.energy_consumption.kwh | kWh | Electricity consumed by spa pump |
| out.electricity.plug_loads.energy_consumption.kwh | kWh | Electricity consumed by plug loads not elsewhere accounted for |
| out.electricity.pool_heater.energy_consumption.kwh | kWh | Electricity consumed by pool heaters |
| out.electricity.pool_pump.energy_consumption.kwh | kWh | Electricity consumed by pool pumps |
| out.electricity.pv.energy_consumption.kwh | kWh | Energy produced by rooftop PV systems. Negative value for any power produced. |
| out.electricity.range_oven.energy_consumption.kwh | kWh | Electricity consumed by range and oven |
| out.electricity.refrigerator.energy_consumption.kwh | kWh | Electricity consumed by refrigerators |
| out.electricity.total.energy_consumption.kwh | kWh | Total electricity consumed |
| out.natural_gas.clothes_dryer.energy_consumption.kwh | kWh | Natural gas consumed by natural gas clothes dryers |
| out.natural_gas.fireplace.energy_consumption.kwh | kWh | Natural gas consumed by natural gas fireplaces |
| out.natural_gas.grill.energy_consumption.kwh | kWh | Natural gas consumed by natural gas grills |
| out.natural_gas.heating.energy_consumption.kwh | kWh | Natural gas consumed by natural gas heating systems |
| out.natural_gas.heating_hp_bkup.energy_consumption.kwh | kWh | Natural gas consumed by heat pump backup |
| out.natural_gas.hot_water.energy_consumption.kwh | kWh | Natural gas consumed by natural gas hot water systems |
| out.natural_gas.lighting.energy_consumption.kwh | kWh | Natural gas consumed by natural gas lighting |
| out.natural_gas.permanent_spa_heat.energy_consumption.kwh | kWh | Natural gas consumed by spa heating |
| out.natural_gas.permanent_spa_pump.energy_consumption.kwh | kWh | Natural gas consumed by spa pump |
| out.natural_gas.pool_heater.energy_consumption.kwh | kWh | Natural gas consumed by natural gas pool heaters |
| out.natural_gas.range_oven.energy_consumption.kwh | kWh | Natural gas consumed by natural gas range and oven |
| out.natural_gas.total.energy_consumption.kwh | kWh | Total natural gas consumed |
| out.params.size_cooling_system_primary_k_btu_h | kBtu/h | Size of primary cooling system |
| out.params.size_heat_pump_backup_primary_k_btu_h | kBtu/h | Size of primary heat pump backup |
| out.params.size_heating_system_primary_k_btu_h | kBtu/h | Size of primary heating system |
| out.params.size_heating_system_secondary_k_btu_h | kBtu/h | Size of secondary heating system |
| out.propane.clothes_dryer.energy_consumption.kwh | kWh | Propane consumed by propane clothes dryers |
| out.propane.heating.energy_consumption.kwh | kWh | Propane consumed by propane heating systems |
| out.propane.heating_hp_bkup.energy_consumption.kwh | kWh | Propane consumed by heat pump backup |
| out.propane.hot_water.energy_consumption.kwh | kWh | Propane consumed by propane hot water systems |
| out.propane.range_oven.energy_consumption.kwh | kWh | Propane consumed by propane range and oven |
| out.propane.total.energy_consumption.kwh | kWh | Total propane energy consumed |
| out.site_energy.net.energy_consumption.kwh | kWh | Total site energy consumed subtracts any power produced by PV or generators |
| out.site_energy.total.energy_consumption.kwh | kWh | Total site energy consumed |

ResStock energy output field names, units, and descriptions

</div>

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

## Emissions

The ResStock workflow includes the capability of including emissions factors as supplemental inputs, which are then used to calculate the corresponding emissions outputs. These outputs are generated by end use and fuel type, as well as per-fuel totals. Total emissions impacts of a measure across fuels are calculated from ResStock results.

### Emissions From On-Site Combustion (Scope 1)

The ResStock workflow currently accepts emissions factors for non-electric energy consumption as annual values only. Our typical approach is to use the values from Table 7.1.2(1) of PDS-01 of BSR/RESNET/ICCC 301 Addendum B, CO<sub>2</sub> Index ((Network 2022)), which account for both combustion and pre-combustion (e.g., methane leakage) impacts. These are 147.3 lb/MMBtu (228.5 kg/MWh) for natural gas, 177.8 lb/MMBtu (275.8 kg/MWh) for propane, and 195.9 lb/MMBtu (303.9 kg/MWh) for fuel oil. ResStock then outputs the associated carbon-equivalent emissions for every fuel and end-use combination.

If multiple emissions scenarios are being run, ResStock will output values for each fuel for each end use for each scenario, even if that particular fuel’s emissions factors do not differ between scenarios. This occurs frequently when we run multiple electricity emissions scenarios with different values for emissions factors related to electricity generation that all use the same emissions factors for on-site non-electric fuel consumption. The full list of emissions output fields from non-electric energy consumption is in Table “ResStock utility bill output field names, units, and descriptions”. In published ResStock datasets, we convert the units on these results to kilograms of CO<sub>2</sub> equivalent emissions. These are the fields in public datasets that begin “out.emissions.natural_gas,” “out.emissions.propane,” and “out.emissions.fuel_oil.”

### Emissions From Electricity Generation (Scope 2)

The ResStock workflow currently accepts emissions factors for electricity consumption as either annual or hourly values. We have used several approaches in selecting electricity emissions factors for use. Our most commonly used approach is to include multiple scenarios, generally relying on data from NREL’s Cambium database ((Gagnon et al. 2025)). When using Cambium data, we use multiple standard scenarios (potential futures of the electric grid) as a type of sensitivity. ResStock releases generally have five long-run marginal emissions scenarios with a computed a levelized factor over a 15 or 25 year lifetime with a 3% discount rate, starting a few years in the future. We then use timeseries (hourly) data at the GEA geographic resolution. ResStock also published average emissions rates, which are a simple average from the beginning to the end of the analysis period.

The full list of emissions output fields from electric energy consumption is in Table “ResStock utility bill output field names, units, and descriptions”. In published ResStock datasets, we convert the units on these results to kilograms of CO<sub>2</sub> equivalent emissions. These are the fields in public datasets that begin “out.emissions.electricity.”

<div id="table:emissions_output" data-source="5_ResStockOutputs.tex">

| **Field Name** | **Units** | **Field Description** |
|:---|:---|:---|
| out.emissions.all_fuels.lrmer_mid_case_25.co2e_kg | co2e_kg | Emissions using on-site fossil fuel rates from ANSI/RESNET and electricity using Cambium 2024 mid case scenario with long run marginal emissions rate levelized by 3% over 25 years |
| out.emissions.all_fuels.lrmer_mid_case_15.co2e_kg | co2e_kg | Emissions using on-site fossil fuel rates from ANSI/RESNET and electricity using Cambium 2024 mid case scenario with long run marginal emissions rate levelized by 3% over 15 years starting in 2027 |
| out.emissions.all_fuels.lrmer_high_re_cost_25.co2e_kg | co2e_kg | Emissions using on-site fossil fuel rates from ANSI/RESNET and electricity using Cambium 2024 high renewable cost scenario with long run marginal emissions rate levelized by 3% over 25 years |
| out.emissions.all_fuels.lrmer_high_re_cost_15.co2e_kg | co2e_kg | Emissions using on-site fossil fuel rates from ANSI/RESNET and electricity using Cambium 2024 high renewable cost scenario with long run marginal emissions rate levelized by 3% over 15 years starting in 2027 |
| out.emissions.all_fuels.lrmer_low_re_cost_25.co2e_kg | co2e_kg | Emissions using on-site fossil fuel rates from ANSI/RESNET and electricity using Cambium 2024 low renewable cost scenario with long run marginal emissions rate levelized by 3% over 25 years |
| out.emissions.all_fuels.lrmer_low_re_cost_15.co2e_kg | co2e_kg | Emissions using on-site fossil fuel rates from ANSI/RESNET and electricity using Cambium 2024 low renewable cost scenario with long run marginal emissions rate levelized by 3% over 15 years starting in 2027 |
| out.emissions.all_fuels.lrmer_low_re_cost_high_ng_price_25.co2e_kg | co2e_kg | Emissions using on-site fossil fuel rates from ANSI/RESNET and electricity using Cambium 2024 low renewable cost high natural gas price scenario with long run marginal emissions rate levelized by 3% over 25 years |
| out.emissions.all_fuels.lrmer_low_re_cost_high_ng_price_15.co2e_kg | co2e_kg | Emissions using on-site fossil fuel rates from ANSI/RESNET and electricity using Cambium 2024 low renewable cost high natural gas price scenario with long run marginal emissions rate levelized by 3% over 15 years starting in 2027 |
| out.emissions.all_fuels.lrmer_high_re_cost_low_ng_price_25.co2e_kg | co2e_kg | Emissions using on-site fossil fuel rates from ANSI/RESNET and electricity using Cambium 2024 high renewable cost low natural gas price scenario with long run marginal emissions rate levelized by 3% over 25 years |
| out.emissions.all_fuels.lrmer_high_re_cost_low_ng_price_15.co2e_kg | co2e_kg | Emissions using on-site fossil fuel rates from ANSI/RESNET and electricity using Cambium 2024 high renewable cost low natural gas price scenario with long run marginal emissions rate levelized by 3% over 15 years starting in 2027 |
| out.emissions.all_fuels.aer_high_re_cost_avg.co2e_kg | co2e_kg | Emissions using on-site fossil fuel rates from ANSI/RESNET and electricity using Cambium 2024 high renewable cost scenario with average emissions rates averaged from 2025-2050. |
| out.emissions.all_fuels.aer_high_re_cost_low_ng_price_avg.co2e_kg | co2e_kg | Emissions using on-site fossil fuel rates from ANSI/RESNET and electricity using Cambium 2024 high renewable cost low natural gas price scenario with average emissions rates averaged from 2025-2050. |
| out.emissions.all_fuels.aer_low_re_cost_avg.co2e_kg | co2e_kg | Emissions using on-site fossil fuel rates from ANSI/RESNET and electricity using Cambium 2024 low renewable cost scenario with average emissions rates averaged from 2025-2050. |
| out.emissions.all_fuels.aer_low_re_cost_high_ng_price_avg.co2e_kg | co2e_kg | Emissions using on-site fossil fuel rates from ANSI/RESNET and electricity using Cambium 2024 low renewable cost high natural gas price scenario with average emissions rates averaged from 2025-2050. |
| out.emissions.all_fuels.aer_mid_case_avg.co2e_kg | co2e_kg | Emissions using on-site fossil fuel rates from ANSI/RESNET and electricity using Cambium 2024 mid case scenario with average emissions rates averaged from 2025-2050. |

ResStock utility bill output field names, units, and descriptions

</div>

## Utility Bills

The ResStock workflow is able to accept a limited range of utility rate inputs and output the corresponding utility bills. The inputs available are fixed charges and volumetric rates for each modeled fuel (typically electricity, natural gas, propane, and fuel oil). These can vary by any one housing characteristic, such as State. Multiple scenarios may be specified. For the list of utility bill outputs, see Table “ResStock cost multiplier output field names, units, and descriptions”.

Our most common approach within the ResStock workflow for utility rates for electricity and natural gas is to use a single scenario, using both a flat charge and a per-consumption charge. We typically use data downloaded from [NREL’s Utility Rate Database](https://openei.org/wiki/Utility_Rate_Database) to calculate the customer-weighted average fixed monthly electricity charge across all utilities in the database, which comes out to approximately \$10/customer/month or \$120/customer/year. For natural gas, we use the American Gas Association’s 2015 value of \$11.25/customer/month for the fixed portion of the utility bill (generally referred to as the “customer charge”). We additionally use EIA state-level information on revenue, sales, and number of customers to calculate the average per-consumption electricity and natural gas rate for each state with the fixed charges removed. The total electricity and natural gas bills for each housing unit model sample are then calculated by summing the flat charge and the product of the per-consumption charge and the total consumption. For example, this process may result in a flat charge of \$120/year and a per-consumption electricity rate of \$0.20/kWh—for a housing unit with a full year electricity consumption of 3000 kWh, the total electricity bill would be \$120 + (3,000 kWh \* \$0.20/kWh) = \$720. If a housing unit has uses no natural gas for the year, the flat charge is not included as it is presumed not to have natural gas service.

Our most common approach within the ResStock workflow for utility rates for propane and fuel oil is to use a single scenario using weekly volumetric rate data from the EIA, averaged over a year (either a calendar year or a winter). When state-level data are not available, we use data from the state’s Petroleum Administration for Defense Districts (PADD) region. When PADD region data are not available, we use U.S. national average values. We then calculate propane and fuel oil bills by multiplying the fuel consumption for each housing unit model by the volumetric rate for that fuel and state. An example of this is in ResStock dataset 2024.1 (Present et al. 2024).

In public ResStock datasets, these fields are prefixed with “out.bills.”

We do not currently commonly model other on-site fuel use in ResStock, such as on-site use of wood or coal, or district steam, and we do not have a common approach for calculating associated bills.

<div id="table:hc_cost_multipliers" data-source="5_ResStockOutputs.tex">

| **Field Name** | **Units** | **Description** |
|:---|:---|:---|
| out.bills.all_fuels.usd | \$ | Annual total charges for electricity, fuel oil, natural gas, and propane |
| out.bills.electricity.usd | \$ | Annual total charges for electricity |
| out.bills.fuel_oil.usd | \$ | Annual total charges for fuel oil |
| out.bills.natural_gas.usd | \$ | Annual total charges for natural gas |
| out.bills.propane.usd | \$ | Annual total charges for propane |

ResStock utility bill output field names, units, and descriptions

</div>

ResStock results can also be used as inputs to calculate utility bills using other rate structures, such as time-of-use electricity rates or tiered rates. However, these calculations are currently not included in the primary ResStock workflow or any published datasets.

## Energy Burden

Energy burden is calculated as the ratio of two values from ResStock data. The first is the energy bill, which is calculated for each individual housing unit model in an analysis as described in the above section. The second is the representative household income, which is converted from income bin and other household characteristics described in Section “Energy Burden”. The energy burden is the energy bill total divided by the representative household income, typically expressed as a percentage. As the utility bill does not account for financial assistance such as LIHEAP, energy burden may be overestimated for low-income households who may qualify for those assistance. Additionally, the representative income is in 2019 USD, reflecting the vintage of PUMS used to derived the data. The dollar value of the utility bill is typically more recent and thus may not align with that of the income denominator.

When this field is available in public datasets, it begins with “out.energy_burden.“

## Schedules

ResStock optionally outputs schedules into the timeseries files. These schedules include energy use schedules as fractions (0-1) and unavailable period schedules from HVAC, power outage, and vacancy periods.

<div id="tab:schedule_outputs" data-source="5_ResStockOutputs.tex">

| **Field Name** | **Units** | **Field Description** |
|:---|:---|:---|
| out.schedules_ceiling_fan | frac | Ceiling fan energy use schedule. |
| out.schedules_clothes_dryer | frac | Clothes dryer energy use schedule. |
| out.schedules_clothes_washer | frac | Clothes washer energy use schedule. |
| out.schedules_cooking_range | frac | Cooking range and oven energy use schedule. |
| out.schedules_dishwasher | frac | Dishwasher energy use schedule. |
| out.schedules_hot_water_clothes_washer | frac | Clothes washer hot water use schedule. |
| out.schedules_hot_water_dishwasher | frac | Dishwasher hot water use schedule. |
| out.schedules_hot_water_fixtures | frac | Fixtures (sinks, showers, baths) hot water use schedule. |
| out.schedules_lighting_garage | frac | Garage lighting energy use schedule. |
| out.schedules_lighting_interior | frac | Interior lighting energy use schedule. |
| out.schedules_no_space_cooling | 0,1 | Cooling unavailable period. |
| out.schedules_no_space_heating | 0,1 | Heating unavailable period. |
| out.schedules_occupants | frac | Occupant heat gain schedule. |
| out.schedules_plug_loads_other | frac | Other plug load energy use schedule. |
| out.schedules_plug_loads_tv | frac | Television plug load energy use schedule. |
| out.schedules_power_outage | 0,1 | Power outage unavailable period. |
| out.schedules_vacancy | 0,1 | Vacancy unavailable period. |

ResStock schedule output field names, units, and descriptions

</div>

## Electrical Panels

For electrical panel, occupied capacity and breaker spaces are tabulated by end use. The total occupied capacity and spaces are calculated as well as their headroom, or the amount of capacity or space left unused. In public ResStock datasets, these fields are prefixed with “out.electric_panel“ and described in “ResStock electrical panel output field names, units, and descriptions”. For capacity, the total occupied load (W) can be calculated using different methods and will be labeled accordingly. In the public datasets, results are available for the 2023 load-based (NEC 220.83) method only for existing dwellings. See Section “Electrical Panels” for the method description. The occupied capacity (A) is converted from occupied load (W) by dividing by 240V, the panel voltage, and then subtracted from the input field “in.electrical_panel_service_rating“” (A) to get the headroom capacity (A). The headroom capacity is used to determine capacity constraint – the panel is considered capacity-constrained if headroom is negative and unconstrained otherwise. This outcome is useful to account for any additional costs needed to resolve the constraint, such as through an electrical panel or service upgrade, or by using lower power appliances as an alternative. Users are encouraged to calculate the capacity constraint on their own to reflect their desired margin of error.

For breaker space, total rated count is labeled as an input metric in table “ResStock building characteristic output field names and descriptions”. This is actually derived from the breaker space headroom, which is probabilistically assigned based on the panel ampacity rating and other housing characteristics, and a tabulation of electrical equipment in the baseline home. In the upgrade simulations, the total breaker space count is carried over from the baseline simulation and the headroom count is recalculated according to the content of the upgrade package. See Section “Electrical Panels” for details. For ease of interpretation by mirroring the structure of the capacity metrics, total breaker space count is labeled as an input just like the panel service rating. All occupied and headroom tabulations are labeled as outputs. Breaker space headroom is used to calculate the space constraint, which exists when the headroom count is negative. The overall panel constraint is summarized into "no constraint", "space constrained only", "capacity constrained only", or "capacity and space constrained".

All results should be interpreted with uncertainty in mind, even if they look reasonable. The prediction of the panel service rating and headroom space do not account for all electrical and connected loads in the model. As a result, the capacity headroom can be negative for a model in the baseline, although it is uncommon. This can be interpreted as the house already being constrained prior to any upgrade and is consistent with anecdotal observations that some houses do trip their breakers often, an indication of a capacity shortfall. On the otherhand, the breaker space headroom in the baseline can never be negative because our modeling approach prevents this by sampling a non-negative headroom count directly. This is also consistent with the physical constraint of breaker space.

<div id="tab:panels" data-source="5_ResStockOutputs.tex">

| **Field Name** | **Units** | **Field Description** |
|:---|:---|:---|
| out.panel.load.total_load.\<method\>.w | W | Total service feeder load calculated per selected NEC method |
| out.panel.load.occupied_capacity.\<method\>.a | A | Total capacity occupied on the panel, calculated as total load (W) divided by panel voltage (240V) |
| out.panel.load.headroom_capacity.\<method\>.a | A | Available capacity on the panel, calculated as panel service rating (A) minus total occupied capacity (A) |
| out.panel.load.heating.w | W | Sum of space heating system and heat pump heating electric loads. For the load calculation, only the max of heating or cooling is used, not both |
| out.panel.load.cooling.w | W | Sum of space cooling system and heat pump cooling electric loads. For the load calculation, only the max of heating or cooling is used, not both |
| out.panel.load.hot_water.w | W | Sum of water heating system electric loads, for electric only |
| out.panel.load.clothes_dryer.w | W | Sum of clothes dryer electric loads, for electric only |
| out.panel.load.dishwasher.w | W | Sum of dishwasher electric loads |
| out.panel.load.range_oven.w | W | Sum of range/oven electric loads, for electric only |
| out.panel.load.mech_vent.w | W | Sum of mechanical ventilation electric loads |
| out.panel.load.permanent_spa_heat.w | W | Sum of permanent spa heater electric load, for electric only |
| out.panel.load.permanent_spa_pump.w | W | Sum of permanent spa pump electric loads |
| out.panel.load.pool_heater.w | W | Sum of pool heater electric loads |
| out.panel.load.pool_pump.w | W | Sum of pool pump electric loads |
| out.panel.load.well_pump.w | W | Sum of well pump electric loads |
| out.panel.load.ev_charging.w | W | Sum of electric vehicle charging equipment electric loads |
| out.panel.load.other.w | W | Sum of other electric loads, including but not limited to lighting/general receptacles at 3 W/sqft, refrigerator, microwave, and garbage disposal |
| out.panel.breaker_space.occupied.count | count | Total number of occupied spaces on the panel |
| out.panel.breaker_space.headroom.count | count | Available spaces, calculated as total rated spaces minus occupied spaces |
| out.panel.breaker_space.heating.count | count | Sum of heating system and heat pump heating occupied spaces |
| out.panel.breaker_space.cooling.count | count | Sum of cooling system and heat pump cooling occupied spaces |
| out.panel.breaker_space.hot_water.count | count | Sum of water heating system occupied spaces |
| out.panel.breaker_space.clothes_dryer.count | count | Sum of clothes dryer occupied spaces |
| out.panel.breaker_space.dishwasher.count | count | Sum of dishwasher occupied spaces |
| out.panel.breaker_space.range_oven.count | count | Sum of range/oven occupied spaces |
| out.panel.breaker_space.mech_vent.count | count | Sum of mechanical ventilation occupied spaces |
| out.panel.breaker_space.permanent_spa_heat.count | count | Sum of permanent spa heater occupied spaces |
| out.panel.breaker_space.permanent_spa_pump.count | count | Sum of permanent spa pump occupied spaces |
| out.panel.breaker_space.pool_heater.count | count | Sum of pool heater occupied spaces |
| out.panel.breaker_space.pool_pump.count | count | Sum of pool pump occupied spaces |
| out.panel.breaker_space.well_pump.count | count | Sum of well pump occupied spaces |
| out.panel.breaker_space.ev_charging.count | count | Sum of electric vehicle charging occupied spaces |
| out.panel.breaker_space.other.count | count | Sum of other electric load occupied spaces |
| out.panel.constraint.capacity.\<method\> | bool | Whether electric panel is capacity-constrained per the given method, defined as when out.panel.load.headroom_capacity.\<method\>.a \< 0 |
| out.panel.constraint.breaker_space | bool | Whether electric panel is space-constrained, defined as when out.panel.breaker_space.headroom.count \< 0 |
| out.panel.constraint.overall.\<method\> | categorical | Summarize overall electric panel constraint per the given method as "no constraint", "space constrained only", "capacity constrained only", or "capacity and space constrained" |
| out.panel.load.total_load.\<method\>.w.savings | W | For an upgrade measure only, total service feeder load reduced per selected NEC method |
| out.panel.load.occupied_capacity.\<method\>.a.savings | A | For an upgrade measure only, total occupied capacity reduced per selected NEC method |
| out.panel.breaker_space.occupied.count.savings | count | For an upgrade measure only, total number of occupied spaces reduced |

ResStock electrical panel output field names, units, and descriptions

</div>

## Other Outputs

The ResStock workflow can optionally output any variable available in EnergyPlus. We regularly use this capability for a variety of purposes, including modeling improvement and validation, debugging, special purpose variables for specific projects, and additional variables to publish as part of public datasets.

Table “Other ResStock results output field names, units, and descriptions” shows a list of output variables that are not covered in other headings in this section but that we have typically included in many of our recent public datasets, where they begin with “out.x.”

<div id="tab:other_outputs" data-source="5_ResStockOutputs.tex">

| **Field Name** | **Units** | **Field Description** |
|:---|:---|:---|
| out.cooling_unavailable_period |  | Cooling unavailable period. |
| out.electricity.summer.peak.kw | kW | Maximum power value in Jun/Jul/Aug |
| out.electricity.winter.peak.kw | kW | Maximum power value in Dec/Jan/Feb |
| out.heating_unavailable_period |  | Heating unavailable period. |
| out.hot_water.clothes_washer.gal | gal | Hot water consumed by clothes washer |
| out.hot_water.dishwasher.gal | gal | Hot water consumed by dishwasher |
| out.hot_water.distribution_waste.gal | gal | Hot water consumed by water distribution system (water remaining in the pipe) |
| out.hot_water.fixtures.gal | gal | Hot water consumed by showers, sinks, and baths |
| out.params.size_water_heater_gal | gal | Size of water heater |
| out.load.cooling.energy_delivered.kbtu | kbtu | Total energy delivered by cooling system includes HVAC distribution losses |
| out.load.cooling.peak.kbtu_hr | kbtu/hr | Maximum cooling load delivered by cooling system includes HVAC distribution losses |
| out.load.heating.energy_delivered.kbtu | kbtu | Total energy delivered by heating system includes HVAC distribution losses |
| out.load.heating.peak.kbtu_hr | kbtu/hr | Maximum heating energy delivered by heating system includes HVAC distribution losses over a 60 min time period |
| out.load.hot_water.energy_delivered.kbtu | kbtu | Total energy delivered by hot water system includes contributions by desuperheaters or solar thermal systems |
| out.unmet_hours.cooling.hour | hr | Number of hours where the cooling setpoint is not maintained |
| out.unmet_hours.heating.hour | hr | Number of hours where the heating setpoint is not maintained |
| weight | n/a | the number of housing units the sample represents |

Other ResStock results output field names, units, and descriptions

</div>

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-Gagnon2025" class="csl-entry">

Gagnon, Pieter, {Pedro Andres} {Sanchez Perez}, Julian Florez, James Morris, Marck {Llerena Velasquez}, and Jordan Eisenman. 2025. *Cambium 2024 Scenario Descriptions and Documentation*. Other. <https://doi.org/10.2172/2558937>.

</div>

<div id="ref-RESNET2022" class="csl-entry">

Network, Residential Energy Services. 2022. *PDS-01, BSR/RESNET/ICC 301-2022 Addendum b, CO2 Index.* <https://www.resnet.us/wp-content/uploads/FS_301-2022AdndmB_v.2-1.pdf>.

</div>

<div id="ref-Present2024" class="csl-entry">

Present, E., P. R. White, C. Harris, et al. 2024. *ResStock Dataset 2024.1 Documentation*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy24osti/88109.pdf>.

</div>

</div>
