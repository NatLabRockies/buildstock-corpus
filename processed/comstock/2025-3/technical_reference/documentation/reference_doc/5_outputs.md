<!-- comstock 2025-3 | technical_reference | documentation/reference_doc/5_outputs.tex -->
# ComStock Outputs

ComStock creates a wide array of data that can be analyzed and aggregated to draw conclusions. While it is common to look at how results vary by building type and climate zone, ComStock provides a wide range of outputs not traditionally provided in large-scale analyses, with the hope of providing maximum utility.

Sections <a href="#rawsimulationresults" data-reference-type="ref" data-reference="rawsimulationresults">[rawsimulationresults]</a> and <a href="#dataviewer" data-reference-type="ref" data-reference="dataviewer">[dataviewer]</a> describe how to access ComStock outputs. Additionally, the sample building energy models are available at <https://data.openei.org/> in the nrel-pds-building-stock data lake. See the README.md file for details.

## Energy Consumption by Fuel and End Use

ComStock provides energy consumption by fuel and end use at both an annual and time-series (typically 15-minute time steps for one year) resolution. Not all combinations of fuels and end uses are found in ComStock. The definitions below describe the fuels and end uses in detail.

ComStock provides modeled energy consumption for the following **fuels**:

- **Electricity**: This represents the electricity that is delivered to the building through the power grid and consumed on-site. How this electricity is generated depends on the generation mix found on the power grid in the region serving the building. This does not include electricity that is generated through a backup generator.

- **Natural Gas**: This represents the natural gas that is delivered to the building through the natural gas pipeline system and consumed on-site.

- **Propane**: This represents the propane that is delivered to the building in tanks and consumed on-site.

- **Fuel Oil**: This represents the liquid fuel oil that is delivered to the building, stored in tanks, and consumed on-site.

- **Other Fuel**: In some ComStock outputs, propane and fuel oil are combined and reported together as “other fuel” due to reporting limitations in the simulation engine. Where this is the case, propane and fuel oil are not reported separately to avoid double-counting.

- **District Heating**: This represents the hot water or steam that is delivered to the building through a district heating piping system and consumed on-site. The quantity of energy consumed represents only the energy extracted from the district heating system by the building; it does not represent the consumption of electricity or natural gas at the district heating plant required to provide heat to the building. In order to capture the energy consumption of the district heating plant, assumptions about distribution heat losses, pumping power, and district heating plant equipment efficiency and controls may be made.

- **District Cooling**: This represents the chilled water that is delivered to the building through a district cooling piping system and consumed on-site. The quantity of energy consumed represents only the energy extracted from the district cooling system by the building; it does not represent the consumption of electricity or natural gas at the district cooling plant required to provide chilled water to the building. In order to capture the energy consumption of the district cooling plant, assumptions about distribution heat gains, pumping power, and district cooling plant equipment efficiency and controls may be made.

ComStock provides modeled energy consumption for the following **end uses** for each applicable fuel:

- **Cooling**: This includes all energy consumed by primary cooling equipment such as chillers, direct expansion air conditioners (includes condenser fan energy), and direct expansion heat pumps in cooling mode (includes condenser fan energy). This also includes parasitic energy consumption of the equipment, such as pan heaters, defrost energy, and any energy needed to overcome modeled pipe losses.

- **Heating**: This represents all energy consumed by primary heating equipment such as boilers, furnaces, natural gas heating coils, electric resistance strip heating coils, and direct expansion heat pumps in heating mode (includes evaporator fan energy). This also includes parasitic energy consumption of the equipment, such as pilot lights, standby losses, defrost energy, and any energy needed to overcome modeled pipe losses.

- **Fans**: This includes all energy consumed by supply fans, return fans, exhaust fans, and kitchen hoods in the building. It excludes the condenser fan energy from direct expansion coils, which is captured in cooling and heating, as described above.

- **Pumps**: This includes all energy consumed by pumps for the purpose of moving hot water for heating and service water heating, chilled water for cooling, and condenser water for heat rejection.

- **Heat Recovery**: This includes the energy used to turn heat or enthalpy wheels, plus the increased fan energy associated with the increased pressure rise caused by the heat recovery wheels.

- **Heat Rejection**: This includes the energy used to run cooling towers and fluid coolers to reject heat from the condenser water loop to the air. As previously noted, condenser fans on direct expansion cooling and heating coils are included in heating and cooling.

- **Humidification**: This includes all energy used to purposely increase humidity in the building. Most buildings are assumed not to use humidification.

- **Water Systems**: This includes all energy consumed by the primary service hot water supply equipment, such as boilers and water heaters. This also includes parasitic energy consumption of the equipment, such as pilot lights, standby losses, and any energy needed to overcome modeled pipe losses.

- **Refrigeration**: This includes all energy used by large refrigeration cases and walk-ins such as those commonly found in grocery stores and large commercial kitchens. Plug-in refrigerators, such as those commonly found in the checkout areas of retail stores, are included in interior equipment.

- **Interior Lighting**: This includes all energy used to light the interior of the building, including general lighting, task lighting, accent lighting, and exit lighting.

- **Exterior Lighting**: This includes all energy used to light the exterior of the building and the surrounding area, including parking lot lighting, entryway illumination, and wall washing.

- **Interior Equipment**: This includes all energy used in the building that was not included in one of the other categories. This covers miscellaneous electric loads such as computers and monitors, large equipment such as elevators, and special-purpose equipment such as data center and IT-closet servers. This is a large and coarse bin, largely because the variety of energy-consuming devices found in buildings is large and little comprehensive data are available.

<figure id="fig:segments_typology">

<figcaption>Example ComStock Results</figcaption>
</figure>

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

## Building Summary Statistics

In addition to the building input characteristics, ComStock outputs include a variety of summary statistic information about the building. These statistics captures building characteristics that result from the complex rules that are applied to HVAC systems after sizing routines and are therefore not easy to discern from the building input characteristics. Units for these outputs are described in the files that accompany the ComStock data sets. Names and descriptions for these summary statistics are included in Table <a href="#tab:building_summary_stats" data-reference-type="ref" data-reference="tab:building_summary_stats">[tab:building_summary_stats]</a>

## Greenhouse Gas Emissions Reporting

ComStock calculates the greenhouse gas emissions from the building stock and savings from measures using both historical and projected emissions data.

### Electricity Emissions

#### eGRID Historical Emissions

Historical emissions use the CO<sub>2</sub>-equivalent total output emission rate from EPA’s Emissions and Generation Resource Integrated Database (eGRID)(U.S. Environmental Protection Agency (EPA) 2022). ComStock results include the historical emissions for 2018, 2019, 2020, and 2021 using eGRID U.S. state and eGRID subregion emissions factors. eGRID regions are similar to Cambium grid regions but not identical. Notably, eGrid separates out New York into upstate, New York City, and Long Island. Cambium uses a whole-state average, and historical emissions use the New York state average instead of the grid region for New York buildings. Historical eGrid emissions rates are an *annual* average multiplied by the total annual electricity use.

#### Cambium Projected Emissions

Projected emissions use data from NREL’s Cambium 2022 data set (Gagnon et al. 2023). Projected emissions consider both the average emissions rate (AER) and the long-run marginal emission rate (LRMER). LRMER, described in (Gagnon and Cole 2022), is an estimate of the rate of emissions that would be either induced or avoided by a long-term (i.e., more than several years) change in electrical demand. LRMER data is levelized over 15 and 30 years(Gagnon et al. 2023). ComStock results including End Use Savings Shapes round 1 results and earlier projects used emissions factors from the Cambium 2021 data (Gagnon et al. 2021),(Gagnon et al. 2022).

### On Site Fossil Fuel Emissions

Natural gas, propane, and fuel oil emissions use the emission factors in *Table 7.1.2(1) of draft National Average Emission Factors for Household Combustion Fuels* defined in *ANSI/RESNET/ICCC 301-2022 Addendum B-2022 Standard for the Calculation and Labeling of the Energy Performance of Dwelling and Sleeping Units using an Energy Rating Index*. Natural gas emissions include both combustion and pre-combustion emissions (e.g., methane leakage for natural gas).

On-Site Fossil Fuel Emissions Factors:\
Natural gas: 147.3 lb/MMBtu (228.0 kg/MWh)\
Propane: 177.8 lb/MMBtu (275.7 kg/MWh)\
Fuel oil: 195.9 lb/MMBtu (303.2 kg/MWh)\

### District Energy Emissions

District heating and cooling emissions use the emissions factors defined in the August 2024 version of the *Energy Star Portfolio Manager Technical Reference* available at <https://portfoliomanager.energystar.gov/pdf/reference/Emissions.pdf>. The district heating emissions factor is the same for both steam and hot water. The district cooling emissions factor assumes district chilled water served by electric driver chillers. The emissions factors were originally sourced from EIA data for district chilled water and the EPA voluntary reporting program for district steam and hot water. These district emissions factors do not include upstream methane leakage. There is considerable variation by location and type of district system, so you may need to scale the results by factors specific to your region or system.

On-Site Fossil Fuel Emissions Factors:\
District Cooling: 52.70 kg/MMBtu\
District Heating: 66.40 kg/MMBtu\

### Air Pollution from On Site Fossil Fuel Combustion

ComStock reports annual pollution emissions for NOx, CO, PM, SO2 from on-site combustion of natural gas, propane, and fuel oil. Emission factors are from U.S. EPA *AP-42: Compilation of Air Emissions Factors from Stationary Sources*(U.S. Environmental Protection Agency (EPA) 2024). Natural gas emissions use emissions factors from AP-42 Table 1.4-2 and particulate emissions are reported as *total* PM. Propane emissions use emissions factors from AP-42 Table 1.5-1 and particulate emissions are reported as *total* PM. Fuel oil emissions use emissions factors for No.2 fuel oil from AP-42 Table 1.3-1 and particulate emissions are reported as *filterable* PM. ComStock does not report air pollution from electricity generation, because grid emissions vary considerably by grid region and are typically located far away from the building site.

## Utility Bills

ComStock estimates utility bills for several of the primary fuels consumed in buildings. Although the rest of ComStock represents the building stock circa 2018, the utility bill estimates reflect utility rates circa 2022, which was the most recent year of data available from EIA at the time of implementation. We made this choice because most users of the data were assumed to prefer bills that most closely reflect the present for decision making.

### Electric Bills

The primary resource for the electric utility rates is the Utility Rate Database (URDB) (Ong and McKeel 2012). This database contains machine-readable descriptions of electric rate structures which have been compiled by manually processing utility rate documentation published by utilities.

#### Rate Selection

URDB contains electric rates that span all sectors (residential, commercial, industrial, etc.), so we limited the rates to those applicable to commercial buildings. First, we filtered down to rates identified as serving the commercial sector and not supplied at transmission voltage. Second, we processed the utility rate names to eliminate rates serving non-building loads based on certain keywords. The list of keywords included Agriculture, Irrigation, Farming, Pump, Snow, Vehicle, Oil, Cotton Gin, Outdoor Light, Security Light, Street, Wholesale, Recreation, Heating (typically found in names of heating-only rates), Substation, and Electric Motor Standby. We downloaded the detailed rate structure data in JSON format for the selected 13,923 rates.

Next, we fed each utility rate and an 8,760-hour electric consumption profile from a Small Hotel building energy model to NREL PySAM (NREL 2023) to calculate an annual electric bill. We eliminated rates with an annual average blended price below \$0.01/kWh. Upon reading the names and comments included with these rates, we found that they were mostly fixed rates for individual pieces of equipment such as cable or internet infrastructure that are not metered. We also eliminated rates with an annual average blended price above \$0.45/kWh, except in the case of AK or HI, which legitimately have high rates. Some of the high rates appeared to be data entry errors. We also removed rates where PySam could not calculate an annual bill based on the rate data. Overall, this process resulted in 10,623 remaining rates spread across 2,658 utilities. 90% of the utilities have 8 or fewer rates. The remainder have more rates, with the most ( 200) belonging to Southern California Edison. These rates cover 85% of the buildings and 85% of the floor area in ComStock. Rates are stored in machine-readable JSON format and organized by EIA Utility Identifier.

A distribution of blended rates calculated using URDB was compared to a distribution of the blended rates calculated using data from EIA (U.S. Energy Information Administration 2022a). The median blended price in the URDB rates was about \$0.08/kWh, while the median blended price reported to EIA in 2022 was \$0.12/kWh, which is about 50% higher than URDB. An analysis of the start date fields for the rates selected from URDB showed a median start date of 2013, which is more than ten years old at the time of writing.

In order to understand the change in rates between 2013 and 2022, a pairwise analysis of the utilities reporting to EIA (U.S. Energy Information Administration 2022a) in both years was performed, and a state-wide average annual change was calculated. The median increase was 1-3% per year. Thus in many cases the rates have increased by (2%/yr \* (2022-2013)) = 18% or more between 2013 and 2022.

#### Electric Utility Assignment

To assign an electric rate to a building in ComStock, we need to know which electric utility serves it. We joined the U.S. DOE Electric Utility Companies and Rates Look-up by Zipcode (Huggins 2021) with the U.S. HUD USPS ZIP Code Crosswalk Files (HUD PD&R 2023) to create a mapping between census tracts and utilities. This was done using both 2010 and 2020 census tracts, because ComStock uses a mix of both. As previously described, rates are assigned to 85% of the buildings in ComStock, and cover 85% of the weighted floor area. There are approximately 37,734 ZIP Codes in the United States. The dataset does not have an electric utility assignment for 738 of these ZIP Codes, which are spread across many states. There are 3,946 census tracts covered by these ZIP Codes which therefore do not have an electric utility assigned. Manually filling these missing mappings could be done in future work.

#### Bill Calculation

At runtime, an 8,670-hour electric load profile is extracted from the building energy model. The annual min and max demand (kW) and annual energy consumption (kWh) are calculated. The final census tract to which the simulation’s results will be allocated is not known at simulation time, but the range of possible tracts is known based on the sampling region. For all possible census tracts, the electric utility EIA identifier is looked up. If rates are found for this utility, the rates are downselected based on the observed load profile any min/max demand or energy consumption qualifiers the rate may have. For example, some rates only apply to buildings with a minimum annual peak demand of 500 kW. For each of the remaining applicable rates, the annual bill is calculated using the 8,760 load profile and the PySAM utility rate calculation engine. This engine accounts for complex rate structures with demand charges, lookback periods, time-of-use rates, etc. To adjust for the lag in the rates on the URDB, the start date for rate is collected and the number of years between the start date and 2022 is calculated. The average annual price increase for the state where the building is located, which was calculated from Form EIA861 data as previously described, is looked up. The annual bill is multiplied by this increase to estimate an adjustment to current 2022 rates.

A median bill cost is calculated from the set of all costs from all applicable rates. Any bill that is lower than 25% of the median or higher than 200% of the median is eliminated to avoid extreme bills. Although uncommon, in testing these extreme bills were found to be associated with rates whose names indicate they are likely not applicable to the building. For example, a “large secondary general” rate which has a high minimum demand charge is not likely applicable to a small retail customer. This step typically only affects the mean bill for a building +/- 10%, so the other applicability criteria appear to be downselecting appropriate rates effectively. The minimum, maximum, and mean bills area reported along with the URDB rate label for the applicable rate, which can be used to locate details of the rate with the URDB API or via a URL, e.g.: "https://apps.openei.org/USURDB/rate/view/\[rate_label\]". If the number of applicable rates is even, a single median bill will not have a specific applicable rate (being the average of the middle two values). Thus in all cases, a ’median_low’ and ’median_high’ bill and applicable rate label are reported, representing the two central values in the bill results if the total number is even, or the duplicated true median value if the total number is odd. For tracts where no electric utility assigned, or for buildings where none of the stored rates for the utility are applicable, the annual bill is estimated using the 2022 EIA Form861 (U.S. Energy Information Administration 2022a) average prices based on the state the building is located in. While this method does not reflect the detailed rate structures and demand charges, it is a fallback for the 15% of buildings in ComStock with no utility assigned.

After simulation, when individual results are allocated to tracts and weights computed, the applicable bills are weighted accordingly. The weighted bills are summed when the tract results area aggregated by geographies (e.g. by PUMA, County or State), and aggregate bill savings are calculated.

### Natural Gas Bills

Natural gas bills are calculated using state-level, volumetric rates due to a lack of detailed public databases of natural gas rates. 2022 U.S. EIA Natural Gas Prices  Commercial Price and U.S. EIA Heat Content of Natural Gas Delivered to Consumers (U.S. Energy Information Administration 2022b) were used to create an energy price in dollars per kBtu. State-level prices range from \$0.007/kBtu in ID to \$0.048/kBtu in HI, with a mean of \$0.012/kBtu nationally.

### Propane and Fuel Oil Bills

Propane and fuel oil bills are calculated using volumetric rates due to a lack of detailed public databases of rates. Rates are state-level where this data is available, and use national average pricing where not. These fuels are typically delivered in batches, so in any given year the number of deliveries could vary. Minimum charges per delivery are assumed to be included in the volumetric price. 2022 U.S. EIA residential No. 2 Distillate Prices by Sales Type and U.S. EIA residential Weekly Heating Oil and Propane Prices (October  March) (U.S. Energy Information Administration 2023) were downloaded, along with the EIA assumed heat content for these fuels. Residential prices were used because commercial prices are only available at the national scale. Additionally, most commercial buildings using these fuels are assumed to be smaller buildings where a residential rate is likely realistic. These data were used to create an energy price in dollars per kBtu for both fuels.

For states where state-level pricing was available, these prices are used directly. For other states, Petroleum Administration for Defense District (PADD)-average pricing was used. For states where PADD-level pricing was not available, national average pricing was used. For propane, prices ranged from \$0.022/kBtu in ND to \$0.052 in FL, with a mean of \$0.032/kBtu nationally. For fuel oil, prices ranged from \$0.027/kBtu in NE to \$0.036 in DE, with a mean of \$0.033/kBtu nationally. The mean national price for both fuels is roughly three times the mean national price of natural gas.

### District Heating and District Cooling Bills

No resources with utility rates for district heating and cooling were identified. Because there are several hundred district systems across the U.S., many of which are university or healthcare campuses, gathering individual rates manually was deemed impractical. Therefore, utility bills for these fuels are not calculated.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-GAGNON2022103915" class="csl-entry">

Gagnon, Pieter, and Wesley Cole. 2022. “Planning for the Evolution of the Electric Grid with a Long-Run Marginal Emission Rate.” *iScience* 25 (3): 103915. <https://doi.org/10.1016/j.isci.2022.103915>.

</div>

<div id="ref-cambium2022" class="csl-entry">

Gagnon, Pieter, Brady Cowiestoll, and Marty Schwarz. 2023. *Cambium 2022 Scenario Descriptions and Documentation*. NREL/TP-6A40-84916. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy23osti/84916.pdf>.

</div>

<div id="ref-cambium2021" class="csl-entry">

Gagnon, Pieter, Will Frazier, Wesley Cole, and Elaine Hale. 2021. *Cambium Documentation: Version 2021*. NREL/TP-6A40-81611. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy22osti/81611.pdf>.

</div>

<div id="ref-lrmer_data2022" class="csl-entry">

Gagnon, Pieter, Elaine Hale, and Wesley Cole. 2022. *Long-Run Marginal Emission Rates for Electricity - Workbooks for 2021 Cambium Data*. National Renewable Energy Laboratory. <https://doi.org/10.7799/1838370>.

</div>

<div id="ref-tract_to_zip" class="csl-entry">

HUD PD&R. 2023. *HUD USPS ZIP CODE CROSSWALK FILES*. U.S. Department of Housing; Urban Development Office of Policy Development; Research. <https://www.huduser.gov/portal/datasets/usps_crosswalk.html>.

</div>

<div id="ref-zip_to_util" class="csl-entry">

Huggins, Jay. 2021. *U.s. Electric Utility Companies and Rates: Look-up by Zipcode (2021)*. National Renewable Energy Laboratory. <https://catalog.data.gov/dataset/u-s-electric-utility-companies-and-rates-look-up-by-zipcode-2021>.

</div>

<div id="ref-pysam" class="csl-entry">

NREL. 2023. *NREL-PySAM Documentation*. <https://nrel-pysam.readthedocs.io/en/main/>.

</div>

<div id="ref-urdb" class="csl-entry">

Ong, Sean, and Ryan McKeel. 2012. *National Utility Rate Database: Preprint*. National Renewable Energy Laboratory. <https://doi.org/10.2172/1050105>.

</div>

<div id="ref-eia_electricity" class="csl-entry">

U.S. Energy Information Administration. 2022a. *Monthly Energy Review*. <https://www.eia.gov/totalenergy/data/browser/index.php?tbl=T07.06#/?f=A>.

</div>

<div id="ref-eia_natural_gas" class="csl-entry">

U.S. Energy Information Administration. 2022b. *Natural Gas Explained*. <https://www.eia.gov/energyexplained/natural-gas/use-of-natural-gas.php>.

</div>

<div id="ref-eia_fuel_oil_and_propane" class="csl-entry">

U.S. Energy Information Administration. 2023. *Petroleum and Other Liquids*. <https://www.eia.gov/dnav/pet/pet_pri_dist_a_epd2_prt_dpgal_a.htm>.

</div>

<div id="ref-egrid2020" class="csl-entry">

U.S. Environmental Protection Agency (EPA). 2022. *Emissions and Generation Resource Integrated Database (eGRID), 2020*. Https://www.epa.gov/egrid.

</div>

<div id="ref-epa_ap42" class="csl-entry">

U.S. Environmental Protection Agency (EPA). 2024. *AP-42: Compilation of Air Emissions Factors from Stationary Sources, 2024*. Https://www.epa.gov/air-emissions-factors-and-quantification/ap-42-compilation-air-emissions-factors-stationary-sources.

</div>

</div>
