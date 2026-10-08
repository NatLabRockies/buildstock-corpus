<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/5_outputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/5_outputs.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 43ae2d4 | corpus_path: technical_reference/documentation/reference_doc/5_outputs.md | section: Building Characteristics | lines: 59-125 -->
## Building Characteristics

In addition to energy consumption data, ComStock outputs include a variety of building input characteristics. Most of these are either direct or indirect inputs to the building model generation workflow. Units for these characteristics are described in the files that accompany the ComStock data sets. Names and descriptions for these characteristics are included in Table <a href="#tab:building_input_characteristics" data-reference-type="ref" data-reference="tab:building_input_characteristics">[tab:building_input_characteristics]</a>.

| **Building Input Characteristic** | **Description** |
|:---|:---|
| in.year_built | Year of original building construction |
| in.building_id | ID number for model |
| in.upgrade_id | ID of upgrade, including 00 for baseline |
| in.upgrade_name | Name of upgrade (if an upgrade was run) |
| in.tstat_clg_delta_f | Cooling thermostat unoccupied set point temperature delta from primary occupied cooling set point. A value of 999 indicates that default values were used for the model |
| in.tstat_clg_sp_f | Cooling thermostat occupied set point. A value of 999 indicates that default values were used for the model |
| in.tstat_htg_delta_f | Heating thermostat unoccupied set point temperature delta from primary occupied heating set point. A value of 999 indicates that default values were used for the model |
| in.tstat_htg_sp_f | Heating thermostat occupied set point. A value of 999 indicates that default values were used for the model |
| in.aspect_ratio | Aspect ratio of building geometry, which is the ratio of the north/south facade length relative to the east/west facade length |
| in.window_type | Type of windows in the model |
| in.building_subtype | Building subtype of the model |
| in.county | County ID of the building model |
| in.comstock_building_type | Primary building type of the model |
| in.rotation | Building rotation off of north axis (positive value is clockwise) |
| in.number_of_stories | Building number of stories above grade |
| in.floor_area | Building total floor area |
| in.hvac_system_type | Building primary HVAC system type |
| in.wall_construction_type | Type of construction used for exterior walls |
| in.weekday_operating_hours | Building duration of weekday hours of operation, which influences the duration of schedules |
| in.weekday_opening_time | Building weekday start hour, which impacts the start time of schedules |
| in.weekend_operating_hours | Building duration of weekend hours of operation, which influences the duration of schedules |
| in.weekend_opening_time | Building weekend start hour, which impacts the start time of schedules |
| in.energy_code_followed_during_last_exterior_lighting_replacement | Specifies the energy code used to determine exterior lighting power and controls |
| in.energy_code_followed_during_last_hvac_replacement | Specifies the energy code used to determine HVAC system types, efficiencies, and controls |
| in.energy_code_followed_during_last_interior_equipment_replacement | Specifies the energy code used to determine interior equipment loads |
| in.energy_code_followed_during_last_roof_replacement | Specifies the energy code used to determine roof insulation values |
| in.energy_code_followed_during_last_service_water_heating_replacement | Specifies the energy code used to determine service water heating efficiencies |
| in.energy_code_followed_during_last_walls_replacement | Specifies the energy code used to determine wall insulation values |
| in.energy_code_followed_during_original_building_construction | Specifies the date of construction of the modeled building, which impacts the assumed energy code year of building subsystems |
| in.heating_fuel | Building primary HVAC heating fuel source |
| in.hvac_night_variability | Specifies the nighttime HVAC operation used in the model, which impacts fan and ventilation behavior during unoccupied times |
| in.interior_lighting_generation | The technology used for interior lighting in the building |
| in.number_stories | Specifies the number of stories of the building |
| in.floor_area_category | Specifies the rentable area range of the building |
| in.service_water_heating_fuel | Building primary service water heating fuel source |
| in.nhgis_tract_gisjoin | Census tract identifier in [National Historical Geographic Information System (NHGIS) format](https://www.nhgis.org/geographic-crosswalks#details) |
| in.nhgis_county_gisjoin | County identified in [NHGIS format](https://www.nhgis.org/geographic-crosswalks#details) |
| in.state_name | Full name of state |
| in.state_abbreviation | Postal abbreviation of state |
| in.census_division_name | Census division name |
| in.census_region_name | Census region name |
| in.weather_file_2018 | Weather file used for the 2018 AMY simulations |
| in.weather_file_TMY3 | Weather file used for the TMY3 simulations |
| in.climate_zone_building_america | DOE Building America climate zone |
| in.climate_zone_ashrae_2006 | ASHRAE Standard 169-2006 |
| in.iso_region | Electric system independent system operator/regional transmission organization (ISO/RTO) region |
| in.reeds_balancing_area | Balancing area ID for the NREL Regional Energy Deployment System (ReEDS) modeling tool |
| in.resstock_county_id | State abbreviation and county name |
| in.nhgis_puma_gisjoin | Census PUMA identifier in [NHGIS format](https://www.nhgis.org/geographic-crosswalks#details) |
| in.ejscreen_census_tract_percentile_for_people_of_color | Percentile for % people of color in building’s census tract. See [U.S. Environmental Protection Agency (EPA) Environmental Justice Screening and Mapping Tool (EJSCREEN) documentation](https://www.epa.gov/ejscreen) for details |
| in.ejscreen_census_tract_percentile_for_low_income | Percentile for % low-income in building’s census tract. See [EPA EJSCREEN documentation](https://www.epa.gov/ejscreen) for details |
| in.ejscreen_census_tract_percentile_for_less_than_high_school_education | Percentile for % less than high school in building’s census tract. See [EPA EJSCREEN documentation](https://www.epa.gov/ejscreen) for details |
| in.ejscreen_census_tract_percentile_for_people_in_linguistic_isolation | Percentile for % of individuals in linguistic isolation in building’s census tract. See [EPA EJSCREEN documentation](https://www.epa.gov/ejscreen) for details. |
| in.ejscreen_census_tract_percentile_percent_people_under_5 | Percentile for % under age 5 in building’s census tract. See [EPA EJSCREEN documentation](https://www.epa.gov/ejscreen) for details |
| in.ejscreen_census_tract_percentile_for_people_over_64 | Percentile for % over age 64 in building’s census tract. See [EPA EJSCREEN documentation](https://www.epa.gov/ejscreen) for details |
| in.ejscreen_census_tract_percentile_for_demographic_index | Percentile for demographic index in building’s census tract. See [EPA EJSCREEN documentation](https://www.epa.gov/ejscreen) for details |
| in.cejst_is_disadvantaged | Whether the building’s census tract is identified as a disadvantaged community in the EPA Climate and Economic Justice Screening Tool (CEJST). See [CEJST documentation](https://screeningtool.geoplatform.gov/en/methodology) for more details |
| in.include_refrigeration_technology_level | Flags buildings that should receive a refrigeration technology level assignment (e.g., grocery stores, restaurants, hospitals with kitchens). Restricts refrigeration modeling to relevant building types. |
| in.year_bin_of_last_refrigeration_replacement | Year bin of last refrigeration system replacement. Based on building year_built, size_bin, and year_of_simulation using DOE survival curves. Larger buildings are assumed to replace more frequently. |
| in.refrigeration_technology_level | Assigned refrigeration technology level (old, new, or advanced). Based on include_refrigeration_technology_level, year_bin_of_last_refrigeration_replacement, and size_bin. Derived from DOE shipment data and ORNL performance curves. |

