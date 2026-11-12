<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/5_ResStockOutputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/5_ResStockOutputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/5_ResStockOutputs.md | section: Building Characteristics | lines: 6-221 -->
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

