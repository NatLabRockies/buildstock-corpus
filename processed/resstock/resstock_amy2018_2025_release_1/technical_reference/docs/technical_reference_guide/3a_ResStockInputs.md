<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3a_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3a_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre -->
# Housing Characteristics and Inputs

In this section, we overview each of the input housing characteristics for ResStock in detail including ResStock options, associated ResStock arguments, and the details of each of those arguments. In ResStock, each input characteristic gets its own input file. The full set of housing characteristic input files is available in the main [ResStock GitHub repository](https://github.com/NREL/resstock/tree/v3.3.0/project_national). We discuss each of these input files as well as the general theory for how different systems and components are modeled. Within each section we also provide the national-level stock saturation of each option within a characteristic. These top-level saturations collapse much of the detail and nuance in ResStock’s probability distributions, but the saturations serve to give a sense of how common different options are, generally, in the United States.

We organize this discussion by the major types of inputs: Geography, Geometry, Envelope, HVAC, Water Heating, Appliances, Lighting, Plug Loads, and Household characteristics. For each of these major sections, we discuss ResStock’s approach to these input types, highlighting where it might vary from OS-HPXML. In the argument tables, a selection of “auto” means that the value is being calculated or defaulted in OS-HPXML. Additionally, we discuss weather inputs to ResStock, which is specified separately from the main input files.

## Geography

ResStock provides a wide range of geographic inputs and outputs. These fields allow for detailed input probability distributions for the U.S. residential building stock characterization. These geography fields are also useful for aggregating and analyzing ResStock outputs.

All the geography fields are compiled into a geography lookup table that contains census block-level resolution. For reference, the Geography Hierarchy Diagram for Census geographies can be found on the [Geography Hierarchy Diagram](https://www2.census.gov/geo/pdfs/reference/geodiagram.pdf) U.S. Census website. This diagram shows that the fundamental geography is a census block. All other census geographies stem from this definition. This hierarchy is used to create a lookup table for all geography characteristics in ResStock.

Added to this table are occupied and vacant unit counts for each census block from the [2020 U.S. Census Redistricting Data](https://www.census.gov/programs-surveys/decennial-census/about/rdo.html) and ACS 5-year 2016 data. The ACS number of units is specified by census tract and downscaled to the census block level using the 2020 Redistricting data. The 2020 census block data are converted to 2010 census blocks using the National Historical Geographic Information System (NHGIS) [Geographic Crosswalks](https://www.nhgis.org/geographic-crosswalks). All the characteristics and distributions of housing characteristics are pivoted from this lookup table relating the geography definitions and housing unit counts. Also in this lookup file is the NHGIS GISJOIN codes that help join this file to other geography fields not in the lookup table or the ResStock outputs.

The ACS housing unit data are typically used by ResStock to specify in the project file the number of housing units in the United States. The ACS data are a 5-year average compared to the single-year 2020 Redistricting data. Consistency for using ACS for unit counts at the census geographies is also achieved except for the “City” characteristic. The City characteristic uses the downscaled data from the ACS to census block, because City boundaries are specified by census blocks.

The census geographies are set to be consistent with the U.S. Census Bureau’s definitions as of July 1, 2015. The 2010 Census geography definitions and changes between the 2010 Census and July 1, 2015, can be found on the [U.S. Census Bureau Decennial Census](https://www.census.gov/programs-surveys/decennial-census/decade.html) website.

When looking at the structure of the Geography dependencies, the ASHRAE IECC 2004 input file does not have any dependencies. ASHRAE IECC 2004 is the top-level geography characteristic. The reason this climate zone characteristic is first and not some U.S. Census characteristic is because of the way the ResStock Sampling algorithm works. By using the large climate zones, more uniformity is achieved in the spatial allocation of the samples. From ASHRAE IECC climate zone, the County and Public Use Microdata Area (PUMA) characteristic is assigned, placing the sample in the smallest resolution geographic characteristic. From here the other geographic characteristics are various aggregations of the County and PUMA field or larger geographies.

In discussing the Geography inputs to ResStock, we break it down into four subcategories: Census Geographies, Climate Zones, Grid and Emissions Geographies, and Other Geographies.

### Census Geographies

This section contains ResStock characteristics based on the U.S. Census geographic definitions. There are 11 input files to ResStock that specify Census Geographies:

- Census Region

- Census Division

- State

- County

- PUMA

- County and PUMA

- Metropolitan and Micropolitan Statistical Area

- City

- American Indian/Alaska Native/Native Hawaiian (AIANNH) Area

- County Metro Status

- PUMA Metro Status.

#### Census Region

##### Description

The U.S. Census Region where the sample is located. The regions are a collection of U.S. Census Divisions.

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

##### Direct Conditional Dependencies

- Census Division.

##### Options

The options are the four U.S. Census Regions: Midwest, Northeast, South, and West.

##### Distribution Assumption(s)

No assumptions are made.

#### Census Division

##### Description

The U.S. Census Division where the sample is located. The regions are a collection of U.S. states.

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

##### Direct Conditional Dependencies

- State.

##### Options

The option are the U.S. Census divisions: East North Central, East South Central, Middle Atlantic, Mountain, New England, Pacific, South Atlantic, West North Central, and West South Central.

##### Distribution Assumption(s)

No assumptions are made.

#### State

##### Description

The U.S. state where the sample is located. In ResStock, States are defined by a collection of Counties.

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

##### Direct Conditional Dependencies

- County.

##### Options

The options for each State are the collection of postal abbreviations (e.g., AL, AK, AR). Each option sets the `site_state_code` argument. The `site_state_code` argument choices are also the State abbreviations. An example option and argument assignment for Alabama is as follows: the option name is AL and `site_state_code`=AL. The rest of the States follow this structure.

<div id="table:hc_arg_def_state" data-source="3a_ResStockInputs.tex">

| Name | Required | Type | Choices | Description |
|:---|:---|:---|:---|:---|
| `site_state_code` | false | Choice | auto, AK, AL, AR, AZ, CA, CO, CT, DC, DE, FL, GA, HI, IA, ID, IL, IN, KS, KY, LA, MA, MD, ME, MI, MN, MO, MS, MT, NC, ND, NE, NH, NJ, NM, NV, NY, OH, OK, OR, PA, RI, SC, SD, TN, TX, UT, VA, VT, WA, WI, WV, WY | State code of the home address. |

The ResStock argument definitions for the State characteristic

</div>

##### Distribution Assumption(s)

No assumptions are made.

#### County

##### Description

The U.S. County where the sample is located.

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

##### Direct Conditional Dependencies

- County and PUMA.

##### Options

The County characteristic options are structured using the State name and County name. An example of the option corresponding to Denver County in Colorado would be “CO, Denver County”. The ResStock arguments `simulation_control_daylight_saving_enabled`, `site_zip_code`, `site_time_zone_utc_offset`, and `weather_station_epw_filepath` are not constant across all the County options.

The `simulation_control_daylight_saving_enabled` argument is set to “true” except in Arizona where all the counties are set to “false.”

The `site_zip_code` argument is assigned by using a single zip code for the entire county.

The `site_time_zone_utc_offset` argument is assigned using the population centroid of each county. As time zones cut through counties, some units will have the wrong time zone. Since the population centroid is used, the bounding error for units being in the wrong counties is 50%.

The `weather_station_epw_filepath` argument is “../../../weather/\<County GISJOIN\>.epw” where \<County GISJOIN\> is the NHGIS GISJOIN value for the county. The NHGISJOIN for a county always starts with the letter “G” followed by the state’s two-digit FIPS, a “0,” and then the County 3-digit FIPS code. An example of this argument assignment for the option “CO, Denver County” is `weather_station_epw_filepath`=../../../weather/G0800310.epw.

<div id="table:hc_arg_def_county" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `simulation_control_daylight_saving_enabled` | false |  | Boolean | auto, true, false | Whether to use daylight saving. |
| `site_zip_code` | false |  | String |  | Zip code of the home address. |
| `site_time_zone_utc_offset` | false | hr | Double | auto | Time zone UTC offset of the home address. Must be between -12 and 14. |
| `weather_station_epw_filepath` | true |  | String |  | Path of the EnergyPlus Weather (EPW) file. |

The ResStock argument definitions for the County characteristic

</div>

##### Distribution Assumption(s)

No assumptions are made.

#### Public Use Microdata Area

##### Description

The Public Use Microdata Area (PUMA) from 2010 U.S. Census that the sample is located. PUMAs are a collection of census tracts that do not cross state boundaries. They contain no fewer than 100,000 people and typically represent no more than 200,000 people. PUMAs are smaller in land area when located near large cities compared to rural areas. PUMAs typically do not follow County boundaries. A map of the 2010 PUMAs can be seen in Figure “2010 Public Use Microdata Area boundaries”.

<figure id="fig:2010_puma_boundaries">
<img src="images/2010-PUMAs.png" style="width:100.0%" />
<figcaption>2010 Public Use Microdata Area boundaries</figcaption>
</figure>

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

##### Direct Conditional Dependencies

- County and PUMA.

##### Options

The options for PUMAs are structured by their state abbreviation and the PUMA code from the GISJOIN code. The GISJOIN values are found in the 2010 TIGER/LINE Basis file on the [IPUMS GIS Boundary Files](https://usa.ipums.org/usa/volii/boundaries.shtml) website. An example is G01002100, which represents state FIPS code AL, and 02100 is the AL, Elmore, Autauga, Montgomery -Outer- and Lowndes Counties PUMA.

There are three ResStock arguments set with the PUMA options: `site_elevation`, `site_latitude`, and `site_longitude`. All three of these arguments are set to “auto” and use the default [OpenStudio-HPXML Building Site](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-site) values.

<div id="table:hc_arg_def_puma" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `site_elevation` | false | ft | Double | auto | Elevation of the home address. |
| `site_latitude` | false | deg | Double | auto | Latitude of the home address. Must be between -90 and 90. Use negative values for southern hemisphere. |
| `site_longitude` | false | deg | Double | auto | Longitude of the home address. Must be between -180 and 180. Use negative values for the western hemisphere. |

The ResStock argument definitions set in the PUMA characteristic

</div>

##### Distribution Assumption(s)

No assumptions are made.

#### County and PUMA

##### Description

The GISJOIN identifier for the County and the PUMA where the sample is located. Since Counties and PUMAs are both a collection of census tracts, often a PUMA is in multiple counties. This characteristic describes the combination of County and PUMA where the sample is located.

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

##### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004.

##### Options

The options for County and PUMA are a combination of the NHGIS GISJOIN Code for the County and the PUMA separated by a comma. An example option is “G0100010, G01002100”—G0100010 is the County GISJOIN for Autauga County, AL, and G01002100 is the PUMA GISJOIN for the AL, Elmore, Autauga, Montgomery -Outer- and Lowndes Counties PUMA.

##### Distribution Assumption(s)

No assumptions are made.

#### Metropolitan and Micropolitan Statistical Area

##### Description

The U.S. Metropolitan Statistical Area (MSA) or Micropolitan Statistical Area (MicroSA) where sample is located. The U.S. Census defines a set of counties as Core-Based Statistical Areas (CBSAs). These CBSAs are either assigned a MicroSA or combined into a larger MSA. According to the U.S. Census, each metropolitan statistical area must have at least one urban area of 50,000 or more inhabitants. According to the U.S. Census, each MicroSA must have at least one urban area of at least 10,000 but less than 50,000 population.

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

- County-MSA crosswalk comes from the Quarterly Census of Employment and Wages NAICS-based data between 2013 and 2022 by the U.S. Bureau of Labor Statistics (<https://www.bls.gov/cew/classifications/areas/county-msa-csa-crosswalk.htm>).

##### Direct Conditional Dependencies

- County.

##### Options

Options of the Metropolitan and Micropolitan Statistical Area characteristic are structured by having the name of the MSA or MicroSA, a comma, the State abbreviation, and either “MSA” or “MicroSA.” An example is “Albany-Schenectady-Troy, NY MSA,” which corresponds to the Albany-Schenectady-Troy MSA in New York State.

##### Distribution Assumption(s)

No assumptions are made.

#### City

##### Description

The City where the sample is located.

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Cities are defined by Census blocks by their Census Place in the 2010 Census.

- Unit counts are from the American Community Survey 5-year 2016.

##### Direct Conditional Dependencies

- County and PUMA.

##### Options

The options are structured as the State abbreviation of the city, a comma, and the name of the city. An example is “AR, Jonesboro,” which corresponds to Jonesboro, Arkansas.

The ResStock argument `site_city` is assigned in the City characteristic. The argument is set to “auto,” which is the OpenStudio-HPXML default value; see the OpenStudio-HPXML [Building Site](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-site) section of the documentation for the default values.

<div id="table:hc_arg_def_city" data-source="3a_ResStockInputs.tex">

| Name        | Required | Type   | Description                            |
|:------------|:---------|:-------|:---------------------------------------|
| `site_city` | false    | String | City/municipality of the home address. |

The ResStock argument definitions set in the City characteristic

</div>

##### Distribution Assumption(s)

- 2020 Decennial Redistricting data were used to map tract-level unit counts to census blocks.

- 1,099 cities are tagged in ResStock, but there are over 29,000 Places in the Census data.

- The threshold for including a Census Place in the City characteristic is 15,000 housing units.

- The value “In Another Census Place” designates the fraction of housing units in a Census Place with fewer total housing units than the threshold.

- The value “Not in a Census Place” designates the fraction of housing units not in a Census Place according to the 2010 Census.

#### AIANNH Area

##### Description

American Indian/Alaska Native/Native Hawaiian (AIANNH) Area where the sample is located. See Figure “AIANNH area map. The image is created by https://proximityone.com/aiannh.htmProximityOne and excludes Alaska and Hawaii.” for a map of AIANNH areas in the contiguous United States.

<figure id="fig:aiannh_map">
<img src="images/aiannh_48b.jpg" style="width:100.0%" />
<figcaption>AIANNH area map. The image is created by <a href="https://proximityone.com/aiannh.htm">ProximityOne</a> and excludes Alaska and Hawaii.</figcaption>
</figure>

##### Distribution Data Source(s)

- 2010 Census Tract to American Indian Area (AIA) Relationship File provides the percent housing units in the census tract that belong to AIA.

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

##### Direct Conditional Dependencies

- County and PUMA.

##### Options

The options are either “Yes” or “No,” indicating if the housing unit is in an AIANNH area.

##### Distribution Assumption(s)

- The 2010 Census Tracts are mapped to 2015 County and PUMA by adjusting for known geographic changes (e.g., renaming of Shannon County to Oglala Lakota County, SD) However, Tract=G3600530940103 (Oneida city, Madison County, NY) could not be mapped to County and PUMA and was removed. The tract contains only 11 units for AIA.

#### County Metro Status

##### Description

The Metro Status of the county where the sample is located and is based on MSA and MicroSA.

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

- County-MSA crosswalk comes from the Quarterly Census of Employment and Wages NAICS-based data between 2013 and 2022 by the [U.S. Bureau of Labor Statistics](https://www.bls.gov/cew/classifications/areas/county-msa-csa-crosswalk.htm).

##### Direct Conditional Dependencies

- Metropolitan and Micropolitan Statistical Area.

##### Options

The options are either “Metropolitan” or “Non-Metropolitan.”

##### Distribution Assumption(s)

No assumptions are made.

#### PUMA Metro Status

##### Description

The PUMA metropolitan status where the housing unit is located.

##### Distribution Data Source(s)

- 2019 5-year PUMS from the University of Minnesota.

##### Direct Conditional Dependencies

- PUMA.

##### Options

The options are either (1) In metro area, not/partially in principal city, (2) In metro area, principal city, or (3) Not/partially in metro area.

##### Distribution Assumption(s)

- The PUMA Metro Status, derived from ACS IPUMS METRO codes, indicates whether the household resided within a metropolitan area and, for households in metropolitan areas, whether the household resided within or outside of a central/principal city. Each PUMA has a unique METRO status in ACS and therefore has a unique PUMA Metro Status. IPUMS derives METRO codes for samples not directly identified based on available geographic information and whether the associated county group or PUMA lies wholly or only partially within metropolitan areas or principal cities.

### Climate Zones

This section of ResStock characteristics is a set of climate zone definitions. There are five input files to ResStock that specify climate zones:

- ASHRAE IECC Climate Zone 2004

- ASHRAE IECC Climate Zone 2004—Sub-CZ Split

- Building America Climate Zones

- California Energy Commission (CEC) Climate Zones

- ENERGY STAR<sup>®</sup> Climate Zone 2023.

#### ASHRAE IECC Climate Zone 2004

##### Description

Climate zone according to ASHRAE 169 in 2004 and IECC in 2012 where the sample is located. See Figure “The 2004 ASHRAE 169 and IECC 2012 climate zone map” for a map of the climate zones.

<figure id="fig:ashrae_169_2004_cz">
<img src="images/ashrae_iecc_cz_map_2004.jpg" style="width:100.0%" />
<figcaption>The 2004 ASHRAE 169 and IECC 2012 climate zone map</figcaption>
</figure>

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

- Climate zone data are from ASHRAE 169 2004, IECC 2012, and [M.C. Baechler 2015](https://www.energy.gov/sites/prod/files/2015/10/f27/ba_climate_region_guide_7.3.pdf).

##### Direct Conditional Dependencies

There are no direct conditional dependencies.

##### Options

A set of counties defines each climate and moisture zone. Climate zones range from 1-8 and moisture zones are indicated by A, B, and C.

The ASHRAE IECC Climate Zone 2004 sets the `site_type` and `site_iecc_zone` arguments. The `site_type` is always set to “auto.” The `site_iecc_zone` argument matches the climate zone with the exception of climate zones 7 and 8 in Alaska. ResStock departs from the climate zone definitions by using 7AK and 8AK instead of 7 and 8 from the standards.

<div id="table:hc_arg_def_ashrae_2004" data-source="3a_ResStockInputs.tex">

| Name | Required | Type | Choices | Description |
|:---|:---|:---|:---|:---|
| `site_type` | false | Choice | auto, suburban, urban, rural | The type of site. |
| `site_iecc_zone` | false | Choice | auto, 1A, 1B, 1C, 2A, 2B, 2C, 3A, 3B, 3C, 4A, 4B, 4C, 5A, 5B, 5C, 6A, 6B, 6C, 7, 8 | IECC zone of the home address. |

The ResStock arguments set in the ASHRAE IECC Climate Zone 2004 characteristic

</div>

##### Distribution Assumption(s)

No assumptions are made.

#### ASHRAE IECC Climate Zone 2004 – Sub-CZ Split

##### Description

The climate zone, according to ASHRAE 169 in 2004 and IECC in 2012, where the sample is located. Climate zone where climate zone 2A is split between counties in (1) TX and LA, and (2) FL, GA, AL, and MS. Climate zone where climate zone 1A is split between counties in (1) HI, and (2) FL. See Figure “The 2004 ASHRAE 169 and IECC 2012 climate zone map” for the climate zones and the climate zone 2A counties that are split between the states mentioned previously.

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

- Climate zone data are from ASHRAE 169 2004, IECC 2012, and [M.C. Baechler 2015](https://www.energy.gov/sites/prod/files/2015/10/f27/ba_climate_region_guide_7.3.pdf).

##### Direct Conditional Dependencies

- County.

##### Options

A set of counties defines each climate and moisture zone. Climate zones range from 1-8 and moisture zones are indicated by A, B, and C. Climate zone 2A is split between options “2A—FL, GA, AL, MS” and “2A—TX, LA.”

##### Distribution Assumption(s)

- This characteristic is used to better represent HVAC types in the 2A climate zone.

- This characteristic is used to better represent partial conditioning in the 1A climate zone.

#### Building America Climate Zones

##### Description

The Building America Climate Zone where the sample is located. See Figure “Building America Climate Zone map” for a map of the climate zones.[^1]

<figure id="fig:building_america_cz">
<img src="images/building_america_cz.png" style="width:100.0%" />
<figcaption>Building America Climate Zone map</figcaption>
</figure>

##### Distribution Data Source(s)

- Unit counts are from the American Community Survey 5-year 2016.

- Spatial definitions are from U.S. Census 2010.

- Climate zone data are from ASHRAE 169 2004, IECC 2012, and [M.C. Baechler 2015](https://www.energy.gov/sites/prod/files/2015/10/f27/ba_climate_region_guide_7.3.pdf).

##### Direct Conditional Dependencies

- County.

##### Options

The options for the Building America Climate Zone characteristic are the same as the climate zones: Cold, Hot-Dry, Hot-Humid, Marine, Mixed-Dry, Mixed-Humid, Subarctic, and Very Cold.

##### Distribution Assumption(s)

No assumptions are made.

#### California Energy Commission Climate Zones

##### Description

The CEC Climate Zone where the sample is located. See Figure “California Energy Commission https://cecgis-caenergy.opendata.arcgis.com/documents/CAEnergy::building-climate-zones/exploreBuilding Climate Zone map” for a map of the CEC building climate zones.

<figure id="fig:cec_cz">
<img src="images/CEC_Building_Climate_Zones.png" style="width:100.0%" />
<figcaption>California Energy Commission <a href="https://cecgis-caenergy.opendata.arcgis.com/documents/CAEnergy::building-climate-zones/explore">Building Climate Zone map</a></figcaption>
</figure>

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Zip code definitions are from the end of Q2 2020.

- The climate zone to zip codes in California are from the CEC website.

##### Direct Conditional Dependencies

- County and PUMA.

##### Options

The options range from 1-16 in California. For other states, the option is set to None.

##### Distribution Assumption(s)

- CEC Climate zones are defined by zip codes.

- The dependency selected is County and PUMA as zip codes are not modeled in ResStock.

- The mapping between Census Tracts and zip codes is approximate and some discrepancies may exist.

#### ENERGY STAR Climate Zone 2023

##### Description

Climate zones for windows, doors, and skylights per ENERGY STAR guidelines as of 2023. See Figure “https://www.energystar.gov/sites/default/files/asset/document/Promotional_Map.pdfENERGY STAR V7 climate zone map” for a map of the climate zones.

<figure id="fig:energy_star_cz">
<img src="images/ENERGY_STAR_Climate_Zone_Map.png" style="width:100.0%" />
<figcaption><a href="https://www.energystar.gov/sites/default/files/asset/document/Promotional_Map.pdf">ENERGY STAR V7 climate zone</a> map</figcaption>
</figure>

##### Distribution Data Source(s)

- Area definition approximated based on published map retrieved in May 2023 from the [ENERGY STAR windows, doors, and skylights key product criteria](https://www.energystar.gov/products/residential_windows_doors_and_skylights/key_product_criteria) website.

##### Direct Conditional Dependencies

- CEC Climate Zone

- County.

##### Options

The options for the ENERGY STAR Climate Zone 2023 characteristic are the same as climate zones: North-Central, Northern, South-Central, and Southern.

##### Distribution Assumption(s)

- ENERGY STAR Climate Zones assigned based on CEC Climate Zone for California and based on County everywhere else.

### Grid and Emissions Geographies

In ResStock there are three input files describing geographies relevant to the electric grid and emissions calculations:

- ReEDS Balancing Area

- Generation and Emissions Assessment (GEA) Region

- ISO RTO Region.

#### ReEDS Balancing Area

##### Description

The Regional Energy Deployment System Model (ReEDS) balancing area where the sample is located. See Figure “ReEDS balancing area map” to see a map of the balancing areas.

<figure id="fig:reeds_ba_map">
<img src="images/reeds_ba_map.png" style="width:100.0%" />
<figcaption>ReEDS balancing area map</figcaption>
</figure>

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

- Regional Energy Deployment System (ReEDS) Model Documentation: Version 2019 ((Brown et al. 2020))

##### Direct Conditional Dependencies

- County.

##### Options

The options for the ReEDS Balancing Area characteristic is a set of integers 1-134 based on Figure “ReEDS balancing area map”. Alaska and Hawaii do not have a ReEDS balancing area and are labeled with the None option.

##### Distribution Assumption(s)

No assumptions are made.

#### Generation and Emissions Assessment (GEA) Region

##### Description

The 2023 and later Cambium generation and carbon emissions assessment region where the sample is located. See Figure “Map of the https://www.nrel.gov/analysis/cambium.htmlCambium 2023 Generation and Emission Assessment Regions” for a map of these regions.

<figure id="fig:cambium_gea_map">
<img src="images/Cambium_GEA_map_2023.png" style="width:100.0%" />
<figcaption> Map of the <a href="https://www.nrel.gov/analysis/cambium.html">Cambium</a> 2023 Generation and Emission Assessment Regions</figcaption>
</figure>

##### Distribution Data Source(s)

- Cambium Documentation: Version 2024 ((Gagnon et al. 2025)).

##### Direct Conditional Dependencies

- County.

##### Options

The options follow the Cambium GEA region names: CAISO, ERCOT, FRCC, ISONE, MISO Central, MISO North, MISO South, None, Northern Grid East, Northern Grid South, Northern Grid West, NYISO, PJM East, PJM West, SERTP, SPP North, SPP South, West Connect North, and West Connect South. The None option is set for Alaska and Hawaii as these states are not modeled in Cambium.

##### Distribution Assumption(s)

No assumptions are made.

#### ISO RTO Region

##### Description

The independent system operator (ISO) or regional transmission organization (RTO) region where the sample is located.

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

- ISO and RTO regions are from EIA Form 861, 2018.

##### Direct Conditional Dependencies

- County

##### Options

The options are a list of options that represent ISOs and RTOs:

- Pennsylvania New Jersey Maryland Interconnection (PJM)

- Midcontinent Independent System Operator (MISO)

- Electric Reliability Council of Texas (ERCOT)

- California ISO (CAISO)

- New York ISO (NYISO)

- Southwest Power Pool (SPP)

- ISO New England (NEISO).

If the county is not in any of these regions, the option is listed as the None option.

##### Distribution Assumption(s)

No assumptions were made.

### Other Geographies

In this section, we cover other miscellaneous geographies in ResStock. This includes four input files:

- Census Division RECS

- Custom State

- Location Region

- American Housing Survey Region.

#### Census Division RECS

##### Description

Census Division as used in RECS 2015 where the sample is located.

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

- U.S. EIA 2015 RECS codebook.

##### Direct Conditional Dependencies

- State.

##### Options

The options match the names of the Census divisions except for RECS 2015 splits the Mountain Census Division into North (CO, ID, MT, UT, WY) and South (AZ, NM, NV).

##### Distribution Assumption(s)

No assumptions were made.

#### Custom State

##### Description

A custom selection of states to be able to have more fine-tuned probability distribution in states where we have more data.

##### Distribution Data Source(s)

No data sources were used.

##### Direct Conditional Dependencies

- State.

##### Options

The options for the Custom State characteristic are “AK” and “Others.” The characteristic was added during the calibration of Alaska to integrate the Alaska Retrofit Information System data.

##### Distribution Assumption(s)

No assumptions were made.

#### Location Region

##### Description

A custom ResStock region constructed of EIA RECS 2009 reportable domains where the sample is located. See Figure “Map of the custom regions in ResStock. Alaska and Hawaii are their own custom regions.” for a map of these regions.

<figure id="fig:location_region_map">
<img src="images/custom_region_map.png" style="width:100.0%" />
<figcaption> Map of the custom regions in ResStock. Alaska and Hawaii are their own custom regions.</figcaption>
</figure>

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

- U.S. EIA 2009 RECS microdata.

##### Direct Conditional Dependencies

- State.

##### Options

A list of custom regions (CRs) that range from CR02–CR11. These numbered CRs are the historical options of the contiguous United States. When Alaska and Hawaii were added, CRAK and CRHI options were added, respectively.

##### Distribution Assumption(s)

No assumptions are made.

#### American Housing Survey Region

##### Description

The American Housing Survey region where the sample is located.

##### Distribution Data Source(s)

- Spatial definitions are from the U.S. Census Bureau as of July 1, 2015.

- Unit counts are from the American Community Survey 5-year 2016.

- Core Based Statistical Area (CBSA) data based on the Feb 2013 CBSA delineation file.

- 2013 American Housing Survey microdata.

##### Direct Conditional Dependencies

- County.

##### Options

Using the American Housing Survey microdata, 15 of the largest core-based statistical areas (CBSAs) were separated from their census divisions. This process resulted in 15 CBSA geographies and 9 Census Division Geographies that do not include the list of largest CBSAs. The list of options are: CBSA Atlanta-Sandy Springs-Roswell, GA; CBSA Boston-Cambridge-Newton, MA-NH; CBSA Chicago-Naperville-Elgin, IL-IN-WI; CBSA Dallas-Fort Worth-Arlington, TX; CBSA Detroit-Warren-Dearborn, MI; CBSA Houston-The Woodlands-Sugar Land, TX; CBSA Los Angeles-Long Beach-Anaheim, CA; CBSA Miami-Fort Lauderdale-West Palm Beach, FL; CBSA New York-Newark-Jersey City, NY-NJ-PA; CBSA Philadelphia-Camden-Wilmington, PA-NJ-DE-MD; CBSA Phoenix-Mesa-Scottsdale, AZ; CBSA Riverside-San Bernardino-Ontario, CA; CBSA San Francisco-Oakland-Hayward, CA; CBSA Seattle-Tacoma-Bellevue, WA CBSA Washington-Arlington-Alexandria, DC-VA-MD-WV; Non-CBSA East North Central; Non-CBSA East South Central; Non-CBSA Middle Atlantic; Non-CBSA Mountain; Non-CBSA New England; Non-CBSA Pacific; Non-CBSA South Atlantic; Non-CBSA West North Central; and Non-CBSA West South Central.

##### Distribution Assumption(s)

No assumptions were made.

### Weather Data

Weather data are closely related to the specification of geography inputs, since weather varies by location. In ResStock, weather data are not specified in the Housing Characteristics input data like most things, but are specified as their own set of input files. In ResStock, weather files are specified at the county level, although sometimes adjacent counties share the same weather files.

As is standard in most building energy models, ResStock can be run with either Typical Meteorological Year (TMY) or Actual Meteorological Year (AMY) data. Hypothetically, ResStock could be run with any other weather data in EPW format, but all data releases to date have been based upon TMY or AMY data. TMY are synthetically constructed files based upon historic weather where each month of the year is picked from the most representative (i.e., “typical”) real month from the previous 30 years ((Wilcox and Marion 2008)). This has the advantage of avoiding extreme or unusual weather, and can be appropriate for analyses that aggregate annual energy use. However, TMY files, by design, will not capture worst-case or extreme situations. Also, given that TMYs are constructed upon historical weather, it is unlikely they truly represent what is “typical” for a location given the reality of accelerating climate change. “Typical” is a moving target, and what was typical 10 years ago is less likely to be typical today. Furthermore, TMY has the disadvantage that adjacent weather stations might not use the same historical years for the same months. For example, a TMY in Denver, CO, might use 2012 for the July file, but 30 miles (40 kilometers) away, the Boulder, CO, TMY station might use 1999 for July. This misalignment of weather years can lead to modeling of non-coincident temporal energy use in ResStock and will likely lead to the underrepresentation of electricity peaks when considering geographies spread across more than one weather file.

AMY weather files overcome the location misalignment issue by using real weather data from a recent historical year. Having a recent file also helps with some of the historical bias from constructing files from data up to 30 years old, but it does not capture future climate change-driven weather patterns. A potential problem with AMY is that it inherits any abnormalities that occurred in a given year. For example, if a particular year was unusually cold, cooling demands would be lower than you might generally see and heating loads a bit higher. In ResStock, we generally run our models with both 2018 AMY and TMY weather (Bianchi and Fontanini 2021). 2018 is a year for which we have sufficient metered data for comparison, and it is also a compatible year for many grid simulation tools.

#### Weather File Development

Since ResStock is a composite model of many EnergyPlus models, it employs the standard EnergyPlus Weather (EPW) files ((Big Ladder Software 2015)). The EPW weather format provides a timeseries dataset of a wide array of weather variables across all 8,760 hours of a non-leap year. These weather variables provide the climatic inputs for simulating heat transfer at each time step for each model within ResStock. For the TMY files, we use the most recent release, TMY3 from Wilcox and Marion (2008).[^2] For AMY, we construct our own EPW files for internal use that are not available to the public. Some of the weather variables needed to construct an EPW are available on the [Load Profiles OEDI submission](https://data.openei.org/submissions/4520).

We develop custom AMY weather data files by pulling historic hourly temperature, humidity, wind speed/direction, and atmospheric pressure from the [Integrated Surface Database](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database), developed by the National Oceanic and Atmospheric Administration’s National Climatic Data Center. Additionally, we add in satellite-derived solar radiation data from NREL’s National Solar Radiation Database (Sengupta et al. 2018). Ground-based solar radiation data are not widely collected, so using satellite-derived solar radiation data is standard practice for both the solar industry and building energy modelers using historical weather data. Caveats and further information on the data compilation and gap filling of this custom AMY approach can be found in Section 2.4 of Wilson et al. (2022).

#### Mapping Weather Files to ResStock Samples

To produce weather files for ResStock, we develop AMY EPWs for approximately 1,200 weather stations pulling data from the year 2018—with the 2018 AMY roughly mapping to the locations of the TMY3 data.[^3] In ResStock, each county is assigned one of these available 1,200 weather stations. Each county will receive a weather station that is located in the county if one is available; if not, the county will be assigned a weather station closest to the county’s population centroid, with prioritization of stations in the same climate zone. Timestamps are shifted if the chosen weather file is in a different time zone. All housing units within a given county will use the assigned weather data for that county for simulations. Within the model, actual weather file assignment occurs in the options_lookup.tsv as a parameter input into the ResStockArguments script.

#### Weather Files and Equipment Sizing

In addition to the 8,760 timeseries of weather variables in the timeseries energy simulation, EPW files also provide a header with basic information on the weather location. ResStock uses some of this header information for sizing HVAC equipment—see Table “Relevant fields from the EPW header”.

<div id="Tab:Packages" data-source="3a_ResStockInputs.tex">

| Field | Layer | Application |
|:---|:---|:---|
| LOCATION | OS-HPXML | OpenStudio-HPXML uses the stated latitude, longitude, and elevation in the EPW header. At the moment, this does not control much in the simulation, but could be important for controlling solar water heating (not currently in ResStock). |
| DESIGN CONDITIONS | OS-HPXML | The design conditions of the EPW header are used in sizing HVAC equipment according to ACCA Manual J and system selection according to ACCA Manual S. |
| GROUND TEMPERATURES | N/A | Unused by ResStock. Instead OS-HPXML uses an analytical method to convert weather station temperatures to ground temperatures (Xing 2014). |
| HOLIDAYS/DAYLIGHT SAVINGS | ResStock | ResStock does not run daylight savings, so the “No” is passed through ResStock to OS-HPXML. |

Relevant fields from the EPW header

</div>

## Geometry

In this section, we discuss the inputs that control the actual geometry of the building energy model used for simulation of each sample. We discuss the geometry parameters in five categories: housing unit location, building type, construction year, housing unit geometry, and space geometry.

### Housing Unit Location

There are two reference frames for locating the housing units modeled in ResStock: (1) the building frame of reference and (2) the polar reference frame. The building frame defines the front, back, top, bottom, left, and right sides of the unit. The polar reference frame defines the orientation of the unit’s front door with respect to the cardinal directions north, south, east, and west.

In ResStock, housing units are modeled as single zones, regardless if they are in larger buildings. To do this, adiabatic walls are assigned/modeled for walls, ceilings, or floors shared between the modeled housing unit, an adjacent unit, and a corridor.

The units are shaded by how near other buildings are to the modeled unit. OpenStudio-HPXML can model shading with exterior corridors for multifamily units, but ResStock does not use these capabilities for multifamily or single-family attached units.

The height above grade for the unit is based on the the number of floors the average ceiling height and the unit level (top floor, middle floors, or bottom floor). The height above grade largely impacts the importance of wind driven infiltration. For bottom units the above grade height is 0 ft. For middle units, the average height of all middle units is used. For top units, the height of the top floor.

There are 12 input files controlling building siting in ResStock:

- Orientation

- Geometry Stories

- Geometry Stories Bin

- Geometry Building Type Height

- Geometry Stories Low Rise

- Geometry Building Number Units MF

- Geometry Building Number Units SFA

- Geometry Building Level MF

- Geometry Building Horizontal Location MF

- Geometry Building Horizontal Location SFA

- Neighbors

- Corridor.

#### Orientation

##### Description

Orientation of the front of the housing unit as it faces the street. The front door is assumed to face the street.

##### Distribution Data Source(s)

- OpenStreetMap data queried by Radiant Labs.

##### Direct Conditional Dependencies

No direct conditional dependencies.

##### Options

The options for the Orientation characteristic are east, west, northeast, southwest, north, south, northwest, and southeast. The options set the `geometry_unit_orientation` ResStock argument; see Table “Orientation options and arguments that vary for each option”. The argument definition can be found in Table “The ResStock argument definitions set in the Orientation characteristic”.

<div id="table:hc_opt_orient" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_unit_orientation` |
|:------------|:-----------------|:----------------------------|
| East        | 17%              | 90                          |
| West        | 17%              | 270                         |
| Northeast   | 7.2%             | 45                          |
| Southwest   | 7.2%             | 225                         |
| North       | 18%              | 0                           |
| South       | 18%              | 180                         |
| Northwest   | 7.7%             | 315                         |
| Southeast   | 7.7%             | 135                         |

Orientation options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Geometry Stories characteristics”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_oient" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `geometry_unit_orientation` | true | degrees | Double | The unit’s orientation is measured clockwise from north (e.g., North=0, East=90, South=180, West=270). |

The ResStock argument definitions set in the Orientation characteristic

</div>

##### Distribution Assumption(s)

No assumptions were made. The distribution was taken directly from the Radiant Labs query.

#### Geometry Stories

##### Description

The number of stories in the building in which the housing unit is located.

##### Distribution Data Source(s)

- U.S. EIA 2009 RECS microdata.

##### Direct Conditional Dependencies

- Geometry Building Type ACS

- Geometry Floor Area Bin.

##### Options

The options for Geometry stories are a set of integers between 1 and 35; see Table “Geometry Stories options and arguments that vary for each option”. The stories of a building refer to the number of floors above grade. The number of stories does not include basements but would include finished attics. The `geometry_num_floors_above_grade` argument definition is in Table “Argument definitions for the Geometry Stories characteristics”.

<div id="table:hc_opt_geom_stories" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_num_floors_above_grade` |
|:------------|:-----------------|:----------------------------------|
| 1           | 49%              | 1                                 |
| 2           | 37%              | 2                                 |
| 3           | 8%               | 3                                 |
| 4           | 2%               | 4                                 |
| 5           | 0.79%            | 5                                 |
| 6           | 0.7%             | 6                                 |
| 7           | 0.16%            | 7                                 |
| 8           | 0.16%            | 8                                 |
| 9           | 0.13%            | 9                                 |
| 10          | 0.17%            | 10                                |
| 11          | 0.09%            | 11                                |
| 12          | 0.19%            | 12                                |
| 13          | 0.12%            | 13                                |
| 14          | 0.11%            | 14                                |
| 15          | 0.12%            | 15                                |
| 20          | 0.21%            | 20                                |
| 21          | 0.66%            | 21                                |
| 35          | 0.11%            | 35                                |

Geometry Stories options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Geometry Stories characteristics”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_geom_stories" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `geometry_num_floors_above_grade` | true | \# | Integer | The number of floors above grade (in the unit if single-family detached or single-family attached, and in the building if apartment unit). Conditioned attics are included. |

Argument definitions for the Geometry Stories characteristics

</div>

##### Distribution Assumption(s)

- All mobile homes are 1 story.

- Single-Family Detached and Single-Family Attached use the STORIES field in RECS, whereas Multifamily with 5+ units uses the NUMFLRS field.

- Building types 2 Unit and 3 or 4 Unit use the stories distribution of Multifamily 5 to 9 Unit (capped at 4 stories) because RECS does not report stories or floors for multifamily with 2-4 units.

- The dependency on floor area bins is removed for multifamily with 5+ units.

- Vintage ACS rows for the 2010s are copied from the 2000-09 rows.

#### Geometry Story Bin

##### Description

Tags the building in which the housing unit is located as having more than 8 stories or less than 8 stories.

##### Distribution Data Source(s)

- U.S. EIA 2009 RECS microdata.

##### Direct Conditional Dependencies

- Geometry Stories.

##### Options

The options are either \<8 stories or 8+ stories. This characteristic is an aggregation of the Geometry stories characteristic to identify units in high-rise buildings. No arguments are assigned based on this housing characteristic, but it is used as a dependency for other input files.

| Option name | Stock saturation |
|:------------|:-----------------|
| \<8         | 98%              |
| 8+          | 2.1%             |

Options and saturation for the Geometry Story Bin

##### Distribution Assumption(s)

- The probability values are a direct mapping of the Geometry Stories characteristic.

#### Geometry Building Type Height

##### Description

The 2009 U.S. EIA RECS building type with multifamily buildings split out by low-rise, mid-rise, and high-rise.

##### Distribution Data Source(s)

- The assignment of building type and height are assigned based on the building type and the number of stories.

##### Direct Conditional Dependencies

- Geometry Building Type RECS

- Geometry Stories.

##### Options

The options break up the Geometry Building Type RECS multi-family 5+ unit buildings into low-rise (1-3 stories), mid-rise (4-7 stories), and high-rise (8+ stories). No arguments are directly assigned based on the options in this input file.

| Option name                             | Stock saturation |
|:----------------------------------------|:-----------------|
| Mobile Home                             | 6.2%             |
| Multi-Family with 2-4 Units             | 8%               |
| Multi-Family with 5+ Units, 1-3 Stories | 13%              |
| Multi-Family with 5+ Units, 4-7 Stories | 3.4%             |
| Multi-Family with 5+ Units, 8+ Stories  | 2.1%             |
| Single-Family Attached                  | 5.9%             |
| Single-Family Detached                  | 61%              |

Options and saturation for Geometry Building Type Height

##### Distribution Assumption(s)

No assumptions are made.

#### Geometry Stories Low Rise

##### Description

Number of building stories for low-rise buildings.

##### Distribution Data Source(s)

- The assignment of building type and height are assigned based on the number of stories.

##### Direct Conditional Dependencies

- Geometry Stories.

##### Options

The options are a categorization of the Geometry Stories characteristic for low-rise buildings (1 story, 2 stories, 3 stories, 4+ stories).

##### Distribution Assumption(s)

None.

#### Geometry Building Number Units MF

##### Description

The number of housing units in the multifamily building.

##### Distribution Data Source(s)

- U.S. EIA 2009 RECS microdata.

##### Direct Conditional Dependencies

- Geometry Building Type ACS

- Geometry Stories.

##### Options

The options for the Geometry Building Level MF characteristic are a set of integers between 2 and 326; see Table “Geometry Building Level Number of Units MF options and arguments that vary for each option”. The “None” option is used for all building types other than multifamily. The options set the `geometry_building_num_units` ResStock argument; see Table “Argument definitions for the Geometry Building Number of Units MF characteristic”.

<div id="table:hc_opt_geom_build_units_mf" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_building_num_units` |
|:------------|:-----------------|:------------------------------|
| 2           | 3.6%             | 2                             |
| 3           | 1.4%             | 3                             |
| 4           | 3%               | 4                             |
| 5           | 0.54%            | 5                             |
| 6           | 1.5%             | 6                             |
| 7           | 0.26%            | 7                             |
| 8           | 2.3%             | 8                             |
| 9           | 0.15%            | 9                             |
| 10          | 0.95%            | 10                            |
| 11          | 0.098%           | 11                            |
| 12          | 1.9%             | 12                            |
| 13          | 0.15%            | 13                            |
| 14          | 0.18%            | 14                            |
| 15          | 0.27%            | 15                            |
| 16          | 0.61%            | 16                            |
| 17          | 0.023%           | 17                            |
| 18          | 0.22%            | 18                            |
| 19          | 0.016%           | 19                            |
| 20          | 0.75%            | 20                            |
| 24          | 0.96%            | 24                            |
| 30          | 0.81%            | 30                            |
| 36          | 0.48%            | 36                            |
| 43          | 0.67%            | 43                            |
| 67          | 2.7%             | 67                            |
| 116         | 1.2%             | 116                           |
| 183         | 0.62%            | 183                           |
| 326         | 1%               | 326                           |
| None        | 74%              |                               |

Geometry Building Level Number of Units MF options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Geometry Building Number of Units MF characteristic”. See the OpenStudio-HPXML [Whole-SFA-MF-Buildings](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#whole-sfa-mf-buildings) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_geom_build_units_mf" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `geometry_building_num_units` | false | \# | Integer | The number of units in the building. Required for single-family attached and apartment units. |

Argument definitions for the Geometry Building Number of Units MF characteristic

</div>

##### Distribution Assumption(s)

- Uses NUMAPTS (number of apartments) field in EIA RECS 2009

- EIA RECS 2009 does not report NUMAPTS for Multifamily 2-4 units, so assumptions are made based on the number of stories

- Data were sampled from the following bins of Geometry Stories: 1, 2, 3, 4-7, 8+.

#### Geometry Building Number Units Single-Family Attached

##### Description

The number of housing units in the single-family attached (SFA) building.

##### Distribution Data Source(s)

- U.S. EIA 2009 RECS microdata.

##### Direct Conditional Dependencies

- Geometry Building Type ACS.

##### Options

The options for the Geometry Building Level SFA characteristic are a set of integers between 2 and 144; see Table “Geometry Building Level Number of Units SFA options and arguments that vary for each option”. The “None” option is used for all building types other than SFA.

<div id="table:hc_opt_geom_build_units_sfa" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_building_num_units` |
|:------------|:-----------------|:------------------------------|
| None        | 94%              |                               |
| 2           | 0%               | 2                             |
| 3           | 0%               | 3                             |
| 4           | 0%               | 4                             |
| 5           | 0.72%            | 5                             |
| 6           | 0.78%            | 6                             |
| 7           | 0.36%            | 7                             |
| 8           | 1.1%             | 8                             |
| 9           | 0%               | 9                             |
| 10          | 0.38%            | 10                            |
| 12          | 0.57%            | 12                            |
| 15          | 0.14%            | 15                            |
| 16          | 0.33%            | 16                            |
| 20          | 0.27%            | 20                            |
| 24          | 0.27%            | 24                            |
| 30          | 0.27%            | 30                            |
| 36          | 0.27%            | 36                            |
| 50          | 0.13%            | 50                            |
| 60          | 0.1%             | 60                            |
| 90          | 0.086%           | 90                            |
| 144         | 0.11%            | 144                           |

Geometry Building Level Number of Units SFA options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Geometry Building Number of Units MF characteristic”. See the OpenStudio-HPXML [Whole-SFA-MF-Buildings](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#whole-sfa-mf-buildings) documentation for the available HPXML schema elements, default values, and constraints.

##### Distribution Assumption(s)

No assumptions were made.

#### Geometry Building Level Multifamily

##### Description

Location of the multifamily (MF) unit vertically within the building (bottom, middle, top).

##### Distribution Data Source(s)

- Calculated directly from the Geometry Building Type RECS and Geometry Stories characteristics.

##### Direct Conditional Dependencies

- Geometry Building Type RECS

- Geometry Stories.

##### Options

The options for the Geometry Building Level MF characteristic are Bottom, Middle, None, and Top; see Table “Geometry Building Level MF options and arguments that vary for each option”. The None option is used for all building types other than MF. The characteristic sets the `geometry_unit_level` ResStock argument; see Table “Argument definitions for the Geometry Building Level MF characteristic”.

<div id="table:hc_opt_geom_build_lev_mf" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_unit_level` |
|:------------|:-----------------|:----------------------|
| Bottom      | 11%              | Bottom                |
| Middle      | 6.1%             | Middle                |
| Top         | 8.9%             | Top                   |
| None        | 74%              |                       |

Geometry Building Level MF options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Geometry Building Level MF characteristic”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_build_lev_mf" data-source="3a_ResStockInputs.tex">

| Name | Required | Type | Choices | Description |
|:---|:---|:---|:---|:---|
| `geometry_unit_level` | false | Choice | Bottom, Middle, Top | The level of the unit. This is required for apartment units. |

Argument definitions for the Geometry Building Level MF characteristic

</div>

##### Distribution Assumption(s)

- Calculated using the number of stories, where buildings greater than or equal to 2 stories have Top and Bottom probabilities = 1/Geometry Stories, and Middle probabilities = 1-2/Geometry stories.

#### Geometry Building Horizontal Location Multifamily

##### Description

Location of the multifamily unit horizontally within the building (left, middle, right).

##### Distribution Data Source(s)

- Calculated directly from the Geometry Number of Units MF and Geometry Stories characteristics.

##### Direct Conditional Dependencies

- Geometry Number of Units MF

- Geometry Stories.

##### Options

The options of the Geometry Building Horizontal Location MF characteristic are None, Left, Middle, Right, and Not Applicable. The characteristic sets the `geometry_unit_horizontal_location` ResStock argument; see Table “Geometry Building Horizontal Location Multifamily options and arguments that vary for each option”. The “Not Applicable” option is used for a pair of number of units and stories that cannot be sampled. For example, a 9-story, 2-unit multifamily building is unlikely to exist in reality and cannot be modeled in ResStock. ResStock does not model units in buildings with more stories than units. All building types other than multifamily receive the “None” option. For the argument definitions, see Table “Argument definitions for the Geometry Building Horizontal Location MF and Geometry Building Horizontal Location SFA characteristics”.

<div id="table:hc_opt_geom_build_hor_loc_mf" data-source="3a_ResStockInputs.tex">

| Option name    | Stock saturation | `geometry_unit_horizontal_location` |
|:---------------|:-----------------|:------------------------------------|
| Left           | 7.1%             | Left                                |
| Middle         | 8%               | Middle                              |
| Right          | 7.1%             | Right                               |
| Not Applicable | 4.2%             | None                                |
| None           | 74%              |                                     |

Geometry Building Horizontal Location Multifamily options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Geometry Building Horizontal Location MF and Geometry Building Horizontal Location SFA characteristics”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_geom_build_hor_loc_mf" data-source="3a_ResStockInputs.tex">

| Name | Required | Type | Choices | Description |
|:---|:---|:---|:---|:---|
| `geometry_unit_horizontal_location` | false | Choice | None, Left, Middle, Right | The horizontal location of the unit when viewing the front of the building. This is required for single-family attached and apartment units. |

Argument definitions for the Geometry Building Horizontal Location MF and Geometry Building Horizontal Location SFA characteristics

</div>

##### Distribution Assumption(s)

- All probabilities are calculated assuming the building has double-loaded corridors (with some exceptions like 3 units in a single-story building).

#### Geometry Building Horizontal Location Single-Family Attached

##### Description

Location of the SFA unit horizontally within the building (left, middle, right).

##### Distribution Data Source(s)

- Calculated directly from the Geometry Number of Units SFA and Geometry Stories characteristics.

##### Direct Conditional Dependencies

- Geometry Number of Units SFA

- Geometry Stories.

##### Options

The options of the Geometry Building Horizontal Location SFA characteristic are None, Left, Middle, and Right. The characteristic sets the `geometry_unit_horizontal_location` ResStock argument; see Table “Geometry Building Horizontal Location SFA options and arguments that vary for each option”. All non-single-family-attached building types receive the “None” option. For the argument definitions, see Table “Argument definitions for the Geometry Building Horizontal Location MF and Geometry Building Horizontal Location SFA characteristics”.

<div id="table:hc_opt_geom_build_hor_loc_sfa" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_unit_horizontal_location` |
|:------------|:-----------------|:------------------------------------|
| Left        | 0.63%            | Left                                |
| Middle      | 4.6%             | Middle                              |
| Right       | 0.63%            | Right                               |
| None        | 94%              |                                     |

Geometry Building Horizontal Location SFA options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Geometry Building Horizontal Location MF and Geometry Building Horizontal Location SFA characteristics”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) documentation for the available HPXML schema elements, default values, and constraints.

##### Distribution Assumption(s)

- All probabilities are calculated from the direct conditional dependencies.

#### Neighbors

##### Description

Presence and distance between the housing unit and the nearest neighbors to the left and right.

##### Distribution Data Source(s)

- OpenStreetMap data queried by Radiant Labs for Multifamily and Single-Family Attached

- Engineering judgment for others.

##### Direct Conditional Dependencies

- Geometry Building Type RECS.

##### Options

The options for Neighbors are Left/Right at 15 ft, 2, 4, 7, 12, 27, and None. The option values correspond to distances in feet to the nearest neighbor on the left and right sides of the building. The options set ResStock arguments corresponding to the distance and height a shading object. The `neighbor_front_height`, `neighbor_back_height`, `neighbor_left_height` and `neighbor_right_height` arguments are all set to “auto,” which sets the shading object height to the total height of the housing unit. The other arguments assign the distance from the housing unit. The `neighbor_front_distance` and `neighbor_back_distance` arguments are set to 0 (meaning there are no neighbors to the front and back of the unit). The left and right distances are set by Table “Neighbors options and arguments that vary for each option”. The None option sets distances to 0 (meaning there are no neighbors). The argument definitions can be seen in Table “The ResStock argument definitions set in the Neighbors characteristic”.

<div id="table:hc_opt_neighbor" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `neighbor_left_distance` | `neighbor_right_distance` |
|:---|:---|:---|:---|
| Left/Right at 15ft | 68% | 15 | 15 |
| 2 | 0.19% | 2 | 2 |
| 4 | 3.4% | 4 | 4 |
| 7 | 5% | 7 | 7 |
| 12 | 9.2% | 12 | 12 |
| 27 | 13% | 27 | 27 |
| None | 1.3% | 0 | 0 |

Neighbors options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Neighbors characteristic”. See the OpenStudio-HPXML documentation section [Neighbor Buildings](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-neighbor-buildings) for the available elements, default values, and constraints.

<div id="table:hc_arg_def_neighbors" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `neighbor_front_distance` | true | ft | Double |  | The distance between the unit and the neighboring building to the front (not including eaves). A value of zero indicates no neighbors. Used for shading. |
| `neighbor_back_distance` | true | ft | Double |  | The distance between the unit and the neighboring building to the back (not including eaves). A value of zero indicates no neighbors. Used for shading. |
| `neighbor_left_distance` | true | ft | Double |  | The distance between the unit and the neighboring building to the left (not including eaves). A value of zero indicates no neighbors. Used for shading. |
| `neighbor_right_distance` | true | ft | Double |  | The distance between the unit and the neighboring building to the right (not including eaves). A value of zero indicates no neighbors. Used for shading. |
| `neighbor_front_height` | false | ft | Double | auto | The height of the neighboring building to the front. |
| `neighbor_back_height` | false | ft | Double | auto | The height of the neighboring building to the back. |
| `neighbor_left_height` | false | ft | Double | auto | The height of the neighboring building to the left. |
| `neighbor_right_height` | false | ft | Double | auto | The height of the neighboring building to the right. |

The ResStock argument definitions set in the Neighbors characteristic

</div>

##### Distribution Assumption(s)

None

#### Corridor

##### Description

Type of corridor attached to multifamily units.

##### Modeling Approach

Single-family attached and multifamily buildings can have corridors, which are passageways between units. Interior corridors are enclosed and assumed to be conditioned, which are modeled by adiabatic walls being created for the wall of the unit that is adjacent to the corridor. Exterior corridors provide shading, but are not enclosed. The way this is modeled is to add a shading object to the front and/or the back of the unit. ResStock only allows multifamily units to have a double-loaded interior corridor. ResStock does not model energy use (e.g., lighting, plug load, or HVAC) associated with corridors; it only models their impact on the multifamily housing units.

##### Distribution Data Source(s)

- Engineering judgment.

##### Direct Conditional Dependencies

- Geometry Building Type RECS.

##### Options

For Mobile Homes, Single-Family Detached, and Single-Family Attached building types the option assigned is “Not Applicable.” Multifamily units all have a “Double-Loaded Interior” corridor with a width of 10 feet. The Corridor characteristic assigns the `geometry_corridor_position` and the `geometry_corridor_width` arguments. For the options and arguments set for each option, see Table “Corridor options and arguments that vary for each option”. For the argument definitions, see Table “Argument definitions for the Corridor characteristic”.

<div id="table:hc_opt_corridor" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_corridor_position` | `geometry_corridor_width` |
|:---|:---|:---|:---|
| Not Applicable | 74% | None | 0 |
| Double-Loaded Interior | 26% | Double-Loaded Interior | 10 |
| None | 0% | None | 0 |
| Single Exterior Front | 0% | Single Exterior (Front) | 10 |
| Double Exterior | 0% | Double Exterior | 10 |

Corridor options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Corridor characteristic”. See the OpenStudio-HPXML [Dwelling Units](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#dwelling-units) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_corridor" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_corridor_position` | true |  | Choice | Double-Loaded Interior, Double Exterior, Single Exterior (Front), None | The position of the corridor. Only applies to single-family attached and apartment units. Exterior corridors are shaded, but not enclosed. Interior corridors are enclosed and conditioned. |
| `geometry_corridor_width` | true | ft | Double |  | The width of the corridor. Only applies to apartment units. |

Argument definitions for the Corridor characteristic

</div>

##### Distribution Assumption(s)

- Single-Family Attached units do not have corridors.

- All Multifamily units have a double-loaded interior corridor with a width of 10 ft.

### Building Type

This section discusses the ResStock input files that control tagging and model differentiation of building type. These building types control a lot of assumptions and treatment of variables in the OpenStudio-HPXML workflow. An example is that the plug load energy is based on a regression equation, and the equation coefficients are different between the building types.

There are two input files controlling building type assignment in ResStock:

- Geometry Building Type ACS

- Geometry Building Type RECS.

#### Geometry Building Type ACS

##### Description

The building type classification according to the U.S. Census American Community Survey.

##### Distribution Data Source(s)

- 2019 5-year PUMS from the University of Minnesota.

##### Direct Conditional Dependencies

- PUMA.

##### Options

ACS considers nine building types, which are tagged in ResStock based on PUMA. No arguments are directly assigned based on this input characteristic.

<div id="table:test" data-source="3a_ResStockInputs.tex">

| Option name            | Stock saturation |
|:-----------------------|:-----------------|
|                        |                  |
| 2 Unit                 | 3.6%             |
| 3 or 4 Unit            | 4.4%             |
| 5 to 9 Unit            | 4.7%             |
| 10 to 19 Unit          | 4.5%             |
| 20 to 49 Unit          | 3.7%             |
| 50 or More Unit        | 5.6%             |
| Mobile Home            | 6.2%             |
| Single-Family Attached | 5.9%             |
| Single-Family Detached | 61%              |

Options and saturation for Geometry Building Type ACS

</div>

##### Distribution Assumption(s)

None.

#### Geometry Building Type RECS

##### Description

The building type classification according to the U.S. EIA RECS.

##### Distribution Data Source(s)

- 2019 5-year PUMS from the University of Minnesota.

##### Direct Conditional Dependencies

- Geometry Building Type ACS.

##### Options

The EIA RECS building types are direct aggregations of the ACS building types. Multifamily units are grouped into 2-4 unit buildings and 5+ unit buildings. The options set the `geometry_unit_type`, `geometry_unit_aspect_ratio`, and `geometry_average_ceiling_height` ResStock arguments; see Table “Geometry Building Type RECS options and arguments that vary for each option”. The `geometry_average_ceiling_height` is always set to 8 ft. The argument definitions are in Table “The ResStock argument definitions set in the Geometry Building Type RECS characteristic”.

<div id="table:hc_opt_gbt_recs" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_unit_type` | `geometry_unit_aspect_ratio` |
|:---|:---|:---|:---|
| Mobile Home | 6.2% | manufactured home | 1.8 |
| Multifamily with 2-4 Units | 8% | apartment unit | 0.5556 |
| Multifamily with 5+ Units | 18% | apartment unit | 0.5556 |
| Single-Family Attached | 5.9% | single-family attached | 0.5556 |
| Single-Family Detached | 61% | single-family detached | 1.8 |

Geometry Building Type RECS options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Geometry Building Type RECS characteristic”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_gbt_recs" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_unit_type` | true |  | Choice | single-family detached, single-family attached, apartment unit, manufactured home | The type of housing unit. Use single-family attached for a housing unit with 1 or more stories, attached units to one or both sides, and no units above/below. Use apartment unit for a housing unit with 1 story, attached units to one, two, or three sides, and units above and/or below. |
| `geometry_unit_aspect_ratio` | true | Frac | Double |  | The ratio of front/back wall length to left/right wall length for the unit, excluding any protruding garage wall area. |
| `geometry_average_ceiling_height` | true | ft | Double |  | Average distance from the floor to the ceiling. |

The ResStock argument definitions set in the Geometry Building Type RECS characteristic

</div>

##### Distribution Assumption(s)

None.

### Construction Year

ResStock captures the change in energy codes over time by relying on survey data (mainly from ACS and EIA RECS) to inform how housing units have adopted energy code vintages and retrofits over time. The approach used in ResStock is to assign a decadal bin when the building was constructed. The decadal bins range from pre-1940s to the 2010s. The Vintage and Vintage ACS characteristics are then used as dependencies to assign probabilities for each Vintage bin. For example, wall insulation being dependent on vintage allows the wall insulation R-value mean to increase over time.

There are two input files controlling building type assignment in ResStock:

- Vintage

- Vintage ACS.

#### Vintage

##### Description

Time period in which the building was originally constructed.

##### Distribution Data Source(s)

- 2019 5-year PUMS from the University of Minnesota.

##### Direct Conditional Dependencies

- Geometry Building Type ACS

- PUMA.

##### Options

The options are decade bins for when the building was constructed: \<1940, 1940s, 1950s, 1960s, 1970s, 1980s, 1990s, 2000s, 2010s. The options set the `year_built` and `vintage` ResStock arguments. The `year_built` argument is always set to “auto.” The `vintage` argument is set to the same value as the option name; see Table “Vintage options and arguments that vary for each option”.

<div id="table:hc_opt_vintage" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `vintage` |
|:------------|:-----------------|:----------|
| \<1940      | 13%              | \<1940    |
| 1940s       | 4.9%             | 1940s     |
| 1950s       | 10%              | 1950s     |
| 1960s       | 11%              | 1960s     |
| 1970s       | 15%              | 1970s     |
| 1980s       | 13%              | 1980s     |
| 1990s       | 14%              | 1990s     |
| 2000s       | 14%              | 2000s     |
| 2010s       | 5.1%             | 2010s     |

Vintage options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Vintage characteristic”.

<div id="table:hc_arg_def_vintage" data-source="3a_ResStockInputs.tex">

| Name | Required | Type | Description |
|:---|:---|:---|:---|
| `year_built` | false | Integer | The year the building was built. |
| `vintage` | false | String | The building vintage, used for informational purposes only. |

The ResStock argument definitions set in the Vintage characteristic

</div>

##### Distribution Assumption(s)

- Where sample counts are less than 10 (812 / 21024 rows), the State average distribution has been inserted.

- “Mobile Home” does not exist in the PUMS DC sample and is replaced by “Single-Family Detached.”

#### Vintage ACS

##### Description

Time period in which the housing unit was constructed as defined by the U.S. Census American Community Survey.

##### Distribution Data Source(s)

- 2019 5-year PUMS from the University of Minnesota.

##### Direct Conditional Dependencies

- Vintage.

##### Options

The options for Vintage ACS are the same vintage bins as ACS, “Option and saturation for Vintage ACS”. They are roughly 20-year bins. No arguments are set based on this input file.

<div id="table:hc_vintage_acs" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation |     |
|:------------|:-----------------|:----|
| \<1940      | 13%              |     |
| 1940-59     | 15%              |     |
| 1960-79     | 26%              |     |
| 1980-99     | 27%              |     |
| 2000-09     | 14%              |     |
| 2010s       | 5.1%             |     |

Option and saturation for Vintage ACS

</div>

##### Distribution Assumption(s)

- The Vintage ACS options are directly mapped from the Vintage characteristic options.

### Housing Unit Geometry

There are seven input files controlling housing unit geometry in ResStock:

- Geometry Building Floor Area

- Geometry Building Floor Area Bin

- Bedrooms

- Geometry Attic Type

- Geometry Foundation Type

- Geometry Garage

- Geometry Space Combination.

#### Geometry Floor Area

##### Description

The conditioned floor area of the housing unit using bins from 2017-2019 American Housing Survey.

##### Distribution Data Source(s)

- 2017 and 2019 American Housing Survey microdata.

##### Direct Conditional Dependencies

- Census Division

- Geometry Building Type RECS

- Income RECS2020

- PUMA Metro Status

- Tenure.

##### Options

The options of Geometry Floor Area characteristic are the American Housing Survey floor area bins. The options set the `geometry_unit_cfa`, `geometry_unit_cfa_bin`, and the `geometry_garage_protrusion` ResStock arguments; see Table “Geometry Floor Area options and arguments that vary for each option”. The `geometry_unit_cfa` argument is always set to “auto.” Because in the ResStockArguments measure “auto” is used for the `geometry_unit_cfa` argument, a representative conditioned floor area is assigned using the `geometry_unit_cfa_bin` argument. The values of the conditioned floor area bin are taken from the 2017 and 2019 American Housing Surveys and split out by housing type. The housing types are single-family detached, single-family attached, apartment, and manufactured homes. Currently, the same conditioned floor area values are used for single-family detached and manufactured homes. For the ResStock argument definition see Table “The ResStock argument definitions set in the Geometry Floor Area characteristic”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) section of the documentation. The floor area is used many places in the OpenStudio-HPXML model workflow.

<div id="table:hc_opt_geom_floor_area" data-source="3a_ResStockInputs.tex">

| Option name | `geometry_garage_protrusion` | `geometry_unit_cfa_bin` |
|:------------|:-----------------------------|:------------------------|
| 0-499       | 0.72                         | 0-499                   |
| 500-749     | 0.75                         | 500-749                 |
| 750-999     | 0.5                          | 750-999                 |
| 1000-1499   | 0.5                          | 1000-1499               |
| 1500-1999   | 0.5                          | 1500-1999               |
| 2000-2499   | 0.5                          | 2000-2499               |
| 2500-2999   | 0.5                          | 2500-2999               |
| 3000-3999   | 0.5                          | 3000-3999               |
| 4000+       | 0.5                          | 4000+                   |

Geometry Floor Area options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_geom_floor_area" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_unit_cfa_bin` | true |  | String |  | E.g., '2000-2499'. |
| `geometry_unit_cfa` | true | ft<sup>2</sup> | Double |  | E.g., '2000' or 'auto'. |
| `geometry_garage_protrusion` | true | Frac | Double |  | The fraction of the garage that is protruding from the conditioned space. Only applies to single-family detached units. |

The ResStock argument definitions set in the Geometry Floor Area characteristic

</div>

##### Distribution Assumption(s)

- Due to low sample count, the characteristic distributions are constructed by downscaling a core input file with 4 sub-input files of different dependencies.

- Sub-input file 1 has dependencies: 'Census Division', 'PUMA Metro Status', 'Geometry Building Type RECS', 'Income RECS2020'

- Sub-input file 2 has dependencies: 'Census Division', 'PUMA Metro Status', 'Geometry Building Type RECS', 'Tenure'

- Sub-input file 3 has dependencies: 'Census Division', 'PUMA Metro Status', 'Geometry Building Type RECS', 'Vintage ACS'

- Sub-input file 4 has dependencies: 'Census Division', 'PUMA Metro Status', 'Income RECS2020', 'Tenure'.

- For each sub-input file, rows with \<10 samples are replaced with coarsening dependency Census Region, followed by the national distribution.

#### Geometry Floor Area Bin

##### Description

The finished floor area of the housing unit using bins.

##### Distribution Data Source(s)

- Directly assigned from the Geometry Floor Area characteristic.

##### Direct Conditional Dependencies

- Geometry Floor Area.

##### Options

The options of the Geometry Floor Area Bin characteristic are 0-1499, 1500-2499, 2500-3999, and 4000+. These floor area bins options are a coarser representation than the Geometry Floor Area characteristic. The Geometry Floor Area Bin Characteristic is often used as a dependency for other characteristics.

##### Distribution Assumption(s)

- The options are directly assigned from the Geometry Floor area characteristic.

### Space Geometry

#### Bedrooms

##### Description

The number of bedrooms in the housing unit.

##### Distribution Data Source(s)

- 2017 and 2019 American Housing Survey microdata.

- Building type categorization based on U.S. EIA 2009 RECS.

##### Direct Conditional Dependencies

- Geometry Building Type RECS

- Geometry Floor Area.

##### Options

The Bedrooms characteristic set the `geometry_unit_num_bedrooms` and the `geometry_unit_num_bathrooms` ResStock arguments. The options for bedrooms are integers from 1 to 5; see Table “Bedroom options and arguments that vary for each option”. The `geometry_unit_num_bathrooms` argument is always set to “auto.” For the argument definitions, see Table “The ResStock argument definitions set in the Bedrooms characteristic”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) section of the documentation. The number of bedrooms is used many places in the OpenStudio-HPXML model workflow.

<div id="table:hc_opt_bed" data-source="3a_ResStockInputs.tex">

| Option name | `geometry_unit_num_bedrooms` |
|:------------|:-----------------------------|
| 1           | 1                            |
| 2           | 2                            |
| 3           | 3                            |
| 4           | 4                            |
| 5           | 5                            |

Bedroom options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_bed" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_unit_num_bedrooms` | true | \# | Integer |  | The number of bedrooms in the unit. |
| `geometry_unit_num_bathrooms` | false | \# | Integer | auto | The number of bathrooms in the unit. |

The ResStock argument definitions set in the Bedrooms characteristic

</div>

##### Distribution Assumption(s)

- More than 5 bedrooms are labeled as 5 bedrooms and 0 bedrooms are labeled as 1 bedroom.

- Limit 0-499 ft<sup>2</sup> housing units to only 1 or 2 bedrooms. The geometry measure has a limit of (ffa-120)/70 \>= bedrooms.

#### Geometry Attic Type

##### Description

The housing unit attic type.

##### Distribution Data Source(s)

- U.S. EIA 2020 RECS microdata.

##### Direct Conditional Dependencies

- Census Division RECS

- Geometry Building Type RECS

- Geometry Stories Low Rise

- Vintage ACS.

##### Options

The options for Geometry Attic Type are Finished Attic or Cathedral Ceilings, Unvented Attic, Vented Attic. The None option is used for multifamily and mobile homes. The options in the Geometry Attic Type characteristic set the `geometry_attic_type`, `geometry_roof_type`, and `geometry_roof_pitch` ResStock arguments; see Table “Geometry Attic Type options and arguments that vary for each option”. The `geometry_roof_type` is always set to “gable.” The `geometry_roof_pitch` is always set to 6:12. For ResStock argument definitions, see Table “The ResStock argument definitions set in the Geometry Attic characteristic”. See OpenStudio-HPXML [Attics](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-attics) section of the documentation for elements, constraints, and default values.

<div id="table:hc_opt_attic" data-source="3a_ResStockInputs.tex">

| Option name                          | `geometry_attic_type` |
|:-------------------------------------|:----------------------|
| Finished Attic or Cathedral Ceilings | ConditionedAttic      |
| None                                 | FlatRoof              |
| Unvented Attic                       | UnventedAttic         |
| Vented Attic                         | VentedAttic           |

Geometry Attic Type options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_attic" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_attic_type` | true |  | Choice | FlatRoof, VentedAttic, UnventedAttic, ConditionedAttic, BelowApartment | The attic type of the building. Attic type ConditionedAttic is not allowed for apartment units. |
| `geometry_roof_type` | true |  | Choice | gable, hip | The roof type of the building. Ignored if the building has a flat roof. |
| `geometry_roof_pitch` | true |  | Choice | 1:12, 2:12, 3:12, 4:12, 5:12, 6:12, 7:12, 8:12, 9:12, 10:12, 11:12, 12:12 | The roof pitch of the attic. Ignored if the building has a flat roof. |

The ResStock argument definitions set in the Geometry Attic characteristic

</div>

##### Distribution Assumption(s)

- Multifamily building types and Mobile Homes have Flat Roof (None) only.

- 1-story Single-Family building types cannot have Finished Attic/Cathedral Ceiling because that attic type is modeled as a new story, and 1-story does not have a second story.

- 4+story Single-family and mobile homes are an impossible combination. The None option is assigned but not sampled.

#### Geometry Foundation Type

##### Description

The type of foundation.

##### Distribution Data Source(s)

- The sample counts and sample weights are constructed using U.S. EIA 2009 RECS microdata.

##### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Building Type RECS

- Vintage ACS.

##### Options

The options of the Geometry Foundation type characteristic are Ambient, Heated Basement, Slab, Unheated Basement, Unvented Crawlspace, and Vented Crawlspace. The options set the `geometry_foundation_type`, `geometry_foundation_height`, `geometry_foundation_height_above_grade`, and `geometry_rim_joist_height` ResStock arguments; see Table “Geometry Foundation Type options and arguments that vary for each option”. For ResStock argument definitions, see Table “The ResStock argument definitions set in the Geometry Foundation Type characteristic”. Another name for Ambient foundations is pier and beam.

<div id="table:hc_opt_geom_found_type" data-source="3a_ResStockInputs.tex">

| Option name | `geometry_foundation_type` | `geometry_foundation_height` | `geometry_foundation_height_above_grade` | `geometry_rim_joist_height` |
|:---|:---|:---|:---|:---|
| Ambient | Ambient | 4 | 4 | 0 |
| Heated Basement | ConditionedBasement | 8 | 1 | 9.25 |
| Slab | SlabOnGrade | 0 | 0 | 0 |
| Unheated Basement | UnconditionedBasement | 8 | 1 | 9.25 |
| Unvented Crawlspace | UnventedCrawlspace | 4 | 1 | 9.25 |
| Vented Crawlspace | VentedCrawlspace | 4 | 1 | 9.25 |

Geometry Foundation Type options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_geom_found_type" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_foundation_type` | true |  | Choice | SlabOnGrade, VentedCrawlspace, UnventedCrawlspace, ConditionedCrawlspace, UnconditionedBasement, ConditionedBasement, Ambient, AboveApartment, BellyAndWingWithSkirt, BellyAndWingNoSkirt | The foundation type of the building. Foundation types ConditionedBasement and ConditionedCrawlspace are not allowed for apartment units. |
| `geometry_foundation_height` | true | ft | Double |  | The height of the foundation (e.g., 3 ft for crawlspace, 8 ft for basement). Only applies to basements/crawlspaces and Ambient. |
| `geometry_foundation_height_above_grade` | true | ft | Double |  | The depth above grade of the foundation wall. Only applies to basements/crawlspaces and Ambient. |
| `geometry_rim_joist_height` | false | in | Double |  | The height of the rim joists. Only applies to basements/crawlspaces. |

The ResStock argument definitions set in the Geometry Foundation Type characteristic

</div>

##### Distribution Assumption(s)

- All mobile homes have Ambient foundations.

- Multifamily buildings cannot have Ambient or Heated Basements foundations.

- Single-family attached buildings cannot have Ambient foundations.

- All foundation types are used across all housing types except for mobile homes, which have constrained options.

- Because we need to assume a foundation type for ground-floor MF units, we use the lumped SFD+SFA distributions for MF2-4 and MF5+ building foundations. (RECS data for households in MF2-4 unit buildings are not useful since we do not know which floor the unit is on. RECS does not include foundation responses for households in MF5+ unit buildings.)

- For SFD and SFA, if no foundation type is specified, then the sample has Ambient foundation.

#### Geometry Garage

##### Description

The presence and size of an attached garage.

##### Distribution Data Source(s)

- U.S. EIA 2020 RECS microdata.

##### Direct Conditional Dependencies

- Census Division RECS

- Geometry Building Type RECS

- Geometry Floor Area Bin

- Geometry Foundation Type

- Geometry Stories Low Rise.

##### Options

The options for the Geometry Garage characteristic are 1 Car, 2 Car, 3 Car, and None. The options set the `geometry_garage_width`, `geometry_garage_depth`, and `geometry_garage_position` ResStock arguments; see Table “Bedroom options and arguments that vary for each option”. The `geometry_garage_depth` argument is always set to 24 ft. The `geometry_garage_position` argument is always set to “Right.” ResStock argument definitions can be seen in Table “The ResStock argument definitions set in the Geometry Garage characteristic”.

<div id="table:hc_opt_garage" data-source="3a_ResStockInputs.tex">

| Option name | `geometry_garage_width` |     |     |
|:------------|:------------------------|:----|:----|
| 1 Car       | 12                      |     |     |
| 2 Car       | 24                      |     |     |
| 3 Car       | 36                      |     |     |
| None        | 0                       |     |     |

Bedroom options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_garage" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_garage_width` | true | ft | Double |  | The width of the garage. Enter zero for no garage. Only applies to single-family detached units. |
| `geometry_garage_depth` | true | ft | Double |  | The depth of the garage. Only applies to single-family detached units. |
| `geometry_garage_position` | true |  | Choice | Right, Left | The position of the garage. Only applies to single-family detached units. |

The ResStock argument definitions set in the Geometry Garage characteristic

</div>

##### Distribution Assumption(s)

Most of the assumptions below are not from the survey data, but are constraints of the geometry modeling in OpenStudio and are set to avoid errors.

- Only Single-Family Detached homes are assigned a probability for attached garage.

- No garage for ambient (i.e., pier & beam) foundation type.

- Due to modeling constraints restricting that garage cannot be larger or deeper than livable space: Single-family detached units that are 0-1499 square feet can only have a maximum of a 1-car garage.

- Single-family detached units that are 0-1499 square feet and 3+ stories cannot have a garage.

- The geometry stories distributions are all the same except for 0-1499 square feet and 3 stories.

- Single-family detached units that are 1500-2499 square feet cannot have a 3-car garage.

- Single-family detached units that are 2500-3999 square feet and a heated basement cannot have a 3-car garage.

- Due to low sample sizes, the following sets of dependencies are progressively lumped together.

  - Crawl, basements, and slab are lumped.

  - Story levels are lumped together.

  - Census Division RECS is grouped into Census Region.

  - Vintage ACS is grouped into: pre-1960, 1960-1999, and 2000+.

#### Geometry Space Combination

##### Description

Valid combinations of building type, building level mf, attic, foundation, and garage.

##### Distribution Data Source(s)

- U.S. EIA 2020 RECS microdata.

##### Direct Conditional Dependencies

- Geometry Attic Type

- Geometry Building Level MF

- Geometry Building Type RECS

- Geometry Foundation Type

- Geometry Garage.

##### Options

The options are a direct mapping of Geometry Building Type, Geometry Building Level MF, Geometry Foundation Type, Geometry Attic Type, and Geometry Garage.

##### Distribution Assumption(s)

No assumptions are made. The options of the dependencies are directly mapped into options of this characteristic.

## Envelope

The envelope components of ResStock inputs interface closely with the Geometry inputs, but focus more on the materials and thermal properties of the envelope. In this section, we discuss the various input files that control the modeled envelope in ResStock by envelope component.

### Walls

There are three major input files to ResStock that control the wall properties:

- Geometry Wall Type

- Geometry Wall Exterior Finish

- Insulation Wall.

Collectively, they specify the material choices and R-value of the housing unit walls.

#### Geometry Wall Type

##### Description

The wall material used for thermal mass calculations of exterior walls.

##### Distribution Data Source(s)

- HIFLD Parcel data.

##### Direct Conditional Dependencies

- Geometry Building Type RECS

- Geometry Story Bin

- State

- Vintage ACS.

##### Option(s)

ResStock models four different wall types: Brick, Concrete, Steel Frame, and Wood Frame. This is the interior structure of the wall, not the exterior cladding. This input file does not have any ResStock arguments, but other input files that influence the thermal properties of the model are dependent on Geometry Wall Type.

##### Distribution Assumption(s)

- Rows where sample size \< 10 are replaced with aggregated values down-scaled from dep='State' to dep='Census Division RECS'.

#### Geometry Wall Exterior Finish

##### Description

Wall siding material and color. This is the main input file that provides the thermal property arguments for the exterior cladding of a wall.

##### Distribution Data Source(s)

- HIFLD Parcel data.

##### Direct Conditional Dependencies

- Geometry Wall Type

- State

- Vintage ACS.

##### Option(s)

ResStock uses 11 options (see Table “Geometry Wall Exterior Finish options and arguments that vary for each option”) for the exterior finish of the walls—correlated with the Geometry Wall Type via the input dependencies. A portion of the wall R-value is attributable to this exterior finish.

<div id="table:hc_opt_geo_wall_ext_fin" data-source="3a_ResStockInputs.tex">

| Option name | `wall_siding_type` | `wall_color` | `exterior_finish_r` |  |
|:---|:---|:---|:---|:---|
| Aluminum, Light | aluminum siding | light | 0.6 |  |
| Brick, Light | brick veneer | light | 0.7 |  |
| Brick, Medium/Dark | brick veneer | medium dark | 0.7 |  |
| Fiber-Cement, Light | fiber cement siding | light | 0.2 |  |
| None | none | medium | 0 |  |
| Shingle, Asbestos, Medium | asbestos siding | medium | 0.6 |  |
| Shingle, Composition, Medium | composite shingle siding | medium | 0.6 |  |
| Stucco, Light | stucco | light | 0.2 |  |
| Stucco, Medium/Dark | stucco | medium dark | 0.2 |  |
| Vinyl, Light | vinyl siding | light | 0.6 |  |
| Wood, Medium/Dark | wood siding | medium dark | 1.4 |  |

Geometry Wall Exterior Finish options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions for the Geometry Exterior Finish characteristic”. See the OpenStudio-HPXML [Walls](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-walls) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ext_finish" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `wall_siding_type` | false |  | Choice | auto, aluminum siding, asbestos siding, brick veneer, composite shingle siding, fiber cement siding, masonite siding, none, stucco, synthetic stucco, vinyl siding, wood siding | The siding type of the walls. Also applies to rim joists. |
| `wall_color` | false |  | Choice | auto, dark, light, medium, medium dark, reflective | The color of the walls. Also applies to rim joists. |
| `exterior_finish_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | R-value of the exterior finish. |

The ResStock argument definitions for the Geometry Exterior Finish characteristic

</div>

##### Distribution Assumption(s)

- Rows where sample size \< 10 are replaced with aggregated values down-scaled from dep='State' to dep='Census Division RECS'

- Brick wall types are assumed to not have an additional brick exterior finish

- Steel and wood frame walls must have an exterior finish.

#### Insulation Wall

##### Description

Wall construction type and insulation level. Provides the main R-value for the walls of the home. This is in addition to the R-values provided by the exterior wall cladding.

##### Distribution Data Source(s)

- *Single-Family Heating and Cooling Requirements: Assumptions, Methods, and Summary Results* ((Ritschard et al. 1992)).

- *Data Collection-Data Characterization Summary* from the NorthernSTAR Building America Partnership ((Nettleton and Edwards 2012)), as described in Roberts et al., *Assessment of the U.S. Department of Energy’s Home Energy Score Tool* (2012), and Merket et al., *Building America Field Data Repository* webinar (2014).

##### Direct Conditional Dependencies

- Location Region

- Geometry Wall Type

- Vintage.

##### Option(s)

ResStock models 15 different Insulation Wall levels; see Table “Insulation Wall options and arguments that vary for each option”. These are based upon the Geometry Wall Type defined, but provide a distribution of insulation levels for each of those options.

<div id="table:hc_ins_wall" data-source="3a_ResStockInputs.tex">

| Option name | `wall_type` | `wall_assembly_r` |  |
|:---|:---|:---|:---|
| Wood Stud, Uninsulated | WoodStud | 3.4 |  |
| Wood Stud, R-7 | WoodStud | 8.7 |  |
| Wood Stud, R-11 | WoodStud | 10.3 |  |
| Wood Stud, R-15 | WoodStud | 12.1 |  |
| Wood Stud, R-19 | WoodStud | 15.4 |  |
| CMU, 6-in Hollow, Uninsulated | ConcreteMasonryUnit | 4 |  |
| CMU, 6-in Hollow, R-7 | ConcreteMasonryUnit | 9.4 |  |
| CMU, 6-in Hollow, R-11 | ConcreteMasonryUnit | 12.4 |  |
| CMU, 6-in Hollow, R-15 | ConcreteMasonryUnit | 15 |  |
| CMU, 6-in Hollow, R-19 | ConcreteMasonryUnit | 17.4 |  |
| Brick, 12-in, 3-wythe, Uninsulated | StructuralBrick | 4.9 |  |
| Brick, 12-in, 3-wythe, R-7 | StructuralBrick | 10.3 |  |
| Brick, 12-in, 3-wythe, R-11 | StructuralBrick | 13.3 |  |
| Brick, 12-in, 3-wythe, R-15 | StructuralBrick | 15.9 |  |
| Brick, 12-in, 3-wythe, R-19 | StructuralBrick | 18.3 |  |

Insulation Wall options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Insulation Wall characteristic”. See the OpenStudio-HPXML [Walls](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-walls) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ins_wall" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `wall_type` | true |  | Choice | WoodStud, ConcreteMasonryUnit, DoubleWoodStud, InsulatedConcreteForms, LogWall, StructuralInsulatedPanel, SolidConcrete, SteelFrame, Stone, StrawBale, StructuralBrick | The type of walls. |
| `wall_assembly_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Assembly R-value of the walls. |

The ResStock argument definitions set in the Insulation Wall characteristic

</div>

##### Distribution Assumption(s)

- Updated per new wall type from Lightbox, all wall type-specific distributions follow that of Wood Frame (WoodStud).

### Roof and Ceiling

There are three input files describing thermal properties of the roof and/or ceilings of housing units:

- Insulation Roof

- Insulation Ceiling

- Roof Material.

Additionally, there is an input for defining Radiant Barriers in homes with attics, but it is not currently used in ResStock.

A major assumption in ResStock is that multifamily buildings and mobile homes do not have attics (see Section “Space Geometry”), so their insulation is assigned in Insulation Ceiling, while for other building types it is assigned in the Insulation Roof housing characteristic.

#### Insulation Roof

##### Description

Finished roof insulation level. Insulation levels for unfinished attics covered separately.

##### Distribution Data Source(s)

- Derived from Home Innovation Research Labs 1982-2007 Data

- NEEA Residential Building Stock Assessment, 2012.

##### Direct Conditional Dependencies

- Geometry Attic Type.

##### Option(s)

Insulation roof options correspond to the amount of insulation at the roof deck and if the roof is finished; see Table “Insulation Roof options and arguments that vary for each option”. A finished roof is a cathedralized construction of the roof. An unfinished roof corresponds to the roof deck being open to the attic.

<div id="table:hc_ins_roof" data-source="3a_ResStockInputs.tex">

| Option name             | `roof_assembly_r` |
|:------------------------|:------------------|
| Unfinished, Uninsulated | 2.3               |
| Finished, Uninsulated   | 3.7               |
| Finished, R-7           | 10.2              |
| Finished, R-13          | 14.3              |
| Finished, R-19          | 21.2              |
| Finished, R-30          | 29.7              |
| Finished, R-38          | 36.5              |
| Finished, R-49          | 47.0              |

Insulation Roof options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Insulation Roof characteristic”. See the OpenStudio-HPXML [Roofs](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-roofs) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ins_roof" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `roof_assembly_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Assembly R-value of the roof |

The ResStock argument definitions set in the Insulation Roof characteristic

</div>

##### Distribution Assumption(s)

None

#### Radiant Barrier

##### Description

Presence of radiant barrier in the attic (not currently used in ResStock).

##### Distribution Data Source(s)

- Not applicable

- All homes are assumed to not have attic radiant barriers installed.

##### Direct Conditional Dependencies

- Geometry Building Type RECS.

##### Option(s)

Three options for radiant barriers are available in ResStock: “Yes,” “No,” and “None”; see Table “Radiant Barrier options and arguments that vary for each option”. “No” is assigned to homes with attics but without radiant barriers, while “None” is assigned to homes without attics. No homes in ResStock currently have the “Yes” option assigned.

<div id="table:hc_opt_rad_bar" data-source="3a_ResStockInputs.tex">

| Option name | `radiant_barrier_attic_location` | `radiant_barrier_grade` |     |
|:------------|:---------------------------------|:------------------------|:----|
| None        | none                             | 1                       |     |
| Yes         | attic roof only                  | 1                       |     |
| No          | none                             | 1                       |     |

Radiant Barrier options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Radiant Barrier characteristic”. See the OpenStudio-HPXML [Roofs](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-roofs) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_rad_bar" data-source="3a_ResStockInputs.tex">

| Name | Required | Type | Choices | Description |
|:---|:---|:---|:---|:---|
| `radiant_barrier_attic_location` | false | Choice | auto, none, attic roof only, attic roof and gable walls, attic floor | The location of the radiant barrier in the attic |
| `radiant_barrier_grade` | false | Choice | auto, 1, 2, 3 | The grade of the radiant barrier in the attic |

The ResStock argument definitions set in the Radiant Barrier characteristic

</div>

##### Distribution Assumption(s)

None

#### Roof Material

##### Description

Roof material and color.

##### Distribution Data Source(s)

- U.S. EIA 2020 RECS microdata.

##### Direct Conditional Dependencies

- Census Division RECS

- Geometry Building Type RECS

- Vintage ACS.

##### Option(s)

Seven roof material options are used in the ResStock baseline; see Table “Roof Material options and arguments that vary for each option”. These correspond to options available within OpenStudio-HPXML and have thermal properties associated with each within OpenStudio-HPXML, but this is not specified at the ResStock level.

<div id="table:hc_opt_roof_mat" data-source="3a_ResStockInputs.tex">

| Option name              | `roof_material_type`           | `roof_color` |
|:-------------------------|:-------------------------------|:-------------|
| Asphalt Shingles, Medium | asphalt or fiberglass shingles | medium       |
| Composition Shingles     | asphalt or fiberglass shingles | medium       |
| Metal, Dark              | metal surfacing                | dark         |
| Slate                    | slate or tile shingles         | medium       |
| Tile, Clay or Ceramic    | slate or tile shingles         | medium       |
| Tile, Concrete           | slate or tile shingles         | medium       |
| Wood Shingles            | wood shingles or shakes        | medium       |

Roof Material options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Roof Material characteristic”. See the OpenStudio-HPXML [Roof](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-roof) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_roof_mat" data-source="3a_ResStockInputs.tex">

| Name | Required | Type | Choices | Description |
|:---|:---|:---|:---|:---|
| `roof_material_type` | false | Choice | auto, asphalt or fiberglass shingles, concrete, cool roof, slate or tile shingles, expanded polystyrene sheathing, metal surfacing, plastic/rubber/synthetic sheeting, shingles, wood shingles or shakes | The material type of the roof |
| `roof_color` | false | Choice | auto, dark, light, medium, medium dark, reflective | The color of the roof |

The ResStock argument definitions set in the Roof Material characteristic

</div>

##### Distribution Assumption(s)

- Multifamily with 5+ Units is assigned ‘Asphalt Shingles, Medium’ only.

- Due to low samples, Vintage ACS is progressively grouped into: pre-1960, 1960-1999, and 2000+.

- Geometry Building Type RECS is progressively grouped into: Single-Family (including Mobile Home), and Multifamily.

- Census Division RECS is coarsened to Census Region.

#### Insulation Ceiling

##### Description

This characteristic in ResStock specifies the insulation level of the ceiling on the top floor of the home in housing units with vented or unvented attics.

##### Distribution Data Source(s)

- NEEA Residential Building Stock Assessment, 2012.

- *Data Collection-Data Characterization Summary* from the NorthernSTAR Building America Partnership ((Nettleton and Edwards 2012)), as described in Roberts et al., *Assessment of the U.S. Department of Energy’s Home Energy Score Tool* (2012) and Merket et al., *Building America Field Data Repository* webinar, 2014.

- Derived from Home Innovation Research Labs 1982-2007 Data.

##### Direct Conditional Dependencies

- Geometry Attic Type

- Location Region

- Vintage.

##### Option(s)

The options are levels of ceiling insulation by R-value; see Table “Insulation Ceiling options and arguments that vary for each option”. Uninsulated indicates that the housing unit could have ceiling insulation, but doesn’t, whereas “None” indicates the housing unit cannot have ceiling insulation because it does not have an unfinished attic.

<div id="table:hc_opt_ins_ceil" data-source="3a_ResStockInputs.tex">

| Option name | `ceiling_assembly_r` | `ceiling_insulation_r` |
|:------------|:---------------------|:-----------------------|
| None        | 0                    | 0                      |
| Uninsulated | 2.1                  | 0                      |
| R-7         | 8.7                  | 7                      |
| R-13        | 14.6                 | 13                     |
| R-19        | 20.6                 | 19                     |
| R-30        | 31.6                 | 30                     |
| R-38        | 39.6                 | 38                     |
| R-49        | 50.6                 | 49                     |

Insulation Ceiling options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Insulation Ceiling characteristic”. See the OpenStudio-HPXML [Attics](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-attics) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ins_ceil" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `ceiling_assembly_r` | true | h-ft<sup>2</sup>-R/Btu | Double | Assembly R-value for the ceiling (attic floor). |
| `ceiling_insulation_r` | true | h-ft<sup>2</sup>-R/Btu | Double | Nominal R-value for the ceiling (attic floor). |

The ResStock argument definitions set in the Insulation Ceiling characteristic

</div>

##### Distribution Assumption(s)

- Vented Attic has the same distribution as Unvented Attic

- CRHI is a copy of CR09

- CRAK is a copy of CR02.

### Foundation

Five input files specify insulation and heat transfer parameters with the ground:

- Insulation Floor

- Insulation Foundation Wall

- Insulation Rim Joist

- Insulation Slab

- Ground Thermal Conductivity.

The inputs starting with “Insulation” specify insulation levels that vary depending upon Geometry Foundation Type (Section “Geometry Foundation Type”).

#### Insulation Floor

##### Description

Sets the insulation levels of all foundation types except for slab-on-grade.

##### Distribution Data Source(s)

- Derived from Home Innovation Research Labs 1982-2007 Data

- Pre-1980 uses engineering judgment.

##### Direct Conditional Dependencies

- Location Region

- Vintage

- Geometry Building Type RECS

- Geometry Foundation Type.

##### Option(s)

ResStock has three different levels of floor insulation, plus a None option that is assigned to buildings with an illegible foundation type for the Insulation Floor characteristic; see Table “Insulation Floor options and arguments that vary for each option”. All options set the `floor_type` to `WoodFrame`.

<div id="table:hc_opt_ins_floor" data-source="3a_ResStockInputs.tex">

| Option name | `floor_over_foundation_assembly_r` | `floor_over_garage_assembly_r` |
|:---|:---|:---|
| None | 0 | 5.3 |
| Uninsulated | 5.3 | 5.3 |
| Ceiling R-13 | 17.8 | 17.8 |
| Ceiling R-19 | 22.6 | 22.6 |
| Ceiling R-30 | 30.3 | 30.3 |

Insulation Floor options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Insulation Floor characteristic”. See the OpenStudio-HPXML [Floors](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-floors) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ins_floor" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `floor_over_foundation_assembly_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Assembly R-value for the floor over the foundation. Ignored if the building has a slab-on-grade foundation. |
| `floor_over_garage_assembly_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Assembly R-value for the floor over the garage. Ignored unless the building has a garage under conditioned space. |
| `floor_type` | true |  | Choice | WoodFrame, StructuralInsulatedPanel, SolidConcrete, SteelFrame | The type of floors. |

The ResStock argument definitions set in the Insulation Floor characteristic

</div>

##### Distribution Assumption(s)

- CRHI is a copy of CR09

- CRAK is a copy of CR02.

#### Insulation Slab

##### Description

Defines the insulation level for all slab-on-grade foundation types.

##### Distribution Data Source(s)

- Derived from Home Innovation Research Labs 1982-2007 Data

- Pre-1980 uses engineering judgment.

##### Direct Conditional Dependencies

- Location Region

- Vintage

- Geometry Building Type RECS

- Geometry Foundation Type.

##### Option(s)

ResStock uses eight different options for Insulation Slab, plus a “None” flag for homes without a slab-on-grade foundation; see Table “Insulation Slab options and arguments that vary for each option”. The options specify both the R-value as well as the location of the slab insulation. The ResStock arguments `slab_thickness`,`slab_carpet_fraction`, and `slab_carpet_r` are constant across all the options and are all set to auto. The ResStock arguments `slab_under_insulation_width`, `slab_exterior_horizontal_insulation_width`, and `lab_exterior_horizontal_insulation_depth_below_grade` are constant and set to 0.

<div id="table:hc_opt_ins_slab" data-source="3a_ResStockInputs.tex">

| Option name | `slab_perimeter_insulation_r` | `slab_perimeter_depth` | `slab_under_insulation_r` | `slab_under_insulation_width` |
|:---|:---|:---|:---|:---|
| None | 0 | 0 | 0 | 0 |
| Uninsulated | 0 | 0 | 0 | 0 |
| 2ft R5 Under, Horizontal | 0 | 0 | 5 | 2 |
| 2ft R10 Under, Horizontal | 0 | 0 | 10 | 2 |
| 4ft R5 Under, Horizontal | 0 | 0 | 5 | 4 |
| 2ft R5 Perimeter, Vertical | 5 | 2 | 0 | 0 |
| 2ft R10 Perimeter, Vertical | 10 | 2 | 0 | 0 |
| R10 Whole Slab, Horizontal | 0 | 0 | 10 | 999 |

Insulation Slab options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Insulation Slab characteristic”. See the OpenStudio-HPXML [ Slabs](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-slabs) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ins_slab" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `slab_perimeter_insulation_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Nominal R-value of the vertical slab perimeter insulation. Applies to slab-on-grade foundations and basement/crawlspace floors. |
| `slab_perimeter_insulation_depth` | true | ft | Double |  | Depth from grade to bottom of vertical slab perimeter insulation. Applies to slab-on-grade foundations and basement/crawlspace floors. |
| `slab_exterior_horizontal_insulation_width` | false | h-ft<sup>2</sup>-R/Btu | Double |  | Nominal R-value of the slab exterior horizontal insulation. Applies to slab-on-grade foundations and basement/crawlspace floors. |
| `slab_exterior_horizontal_insulation_width` | false | ft | Double |  | Width of the slab exterior horizontal insulation measured from the exterior surface of the vertical slab perimeter insulation. Applies to slab-on-grade foundations and basement/crawlspace floors. |
| `slab_exterior_horizontal_insulation_depth_below_grade` | false | ft | Double |  | Depth of the slab exterior horizontal insulation measured from the top surface of the slab exterior horizontal insulation. Applies to slab-on-grade foundations and basement/crawlspace floors. |
| `slab_under_insulation_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Nominal R-value of the horizontal under slab insulation. Applies to slab-on-grade foundations and basement/crawlspace floors. |
| `slab_under_insulation_width` | true | ft | Double |  | Width from slab edge inward of horizontal under-slab insulation. Enter 999 to specify that the under slab insulation spans the entire slab. Applies to slab-on-grade foundations and basement/crawlspace floors. |
| `slab_thickness` | false | in | Double | auto | The thickness of the slab. Zero can be entered if there is a dirt floor instead of a slab. |
| `slab_carpet_fraction` | false | Frac | Double | auto | Fraction of the slab floor area that is carpeted. |
| `slab_carpet_r` | false | h-ft<sup>2</sup>-R/Btu | Double | auto | R-value of the slab carpet. |

The ResStock argument definitions set in the Insulation Slab characteristic

</div>

##### Distribution Assumption(s)

- CRHI is a copy of CR09

- CRAK is a copy of CR02.

#### Insulation Foundation Wall

##### Description

Specifies the insulation level of foundation types with foundation walls (i.e., crawlspaces and basements).

##### Distribution Data Source(s)

- Derived from Home Innovation Research Labs 1982-2007 Data

- Pre-1980 uses engineering judgment.

##### Direct Conditional Dependencies

- Location Region

- Vintage

- Geometry Building Type RECS

- Geometry Foundation Type.

##### Option(s)

ResStock provides four different options for Insulation Foundation Wall, plus a “None” flag for homes without foundation walls (Table “Insulation Foundation Wall options and arguments that vary for each option”). Several ResStock arguments are constant across all options: `foundation_wall_thickness` and `foundation_wall_assembly_r` are always set to *auto*, `foundation_wall_insulation_location` is always *exterior*, and `foundation_wall_insulation_distance_to_top` is 0.

<div id="table:hc_opt_ins_found_wall" data-source="3a_ResStockInputs.tex">

| Option name | `foundation_wall_type` | `foundation_wall_insulation_r` | `foundation_wall_insulation_distance_to_bottom` |
|:---|:---|:---|:---|
| None | solid concrete | 0 | 0 |
| Uninsulated | solid concrete | 0 | 0 |
| Wall R-5, Exterior | solid concrete | 5 | auto |
| Wall R-10, Exterior | solid concrete | 10 | auto |
| Wall R-15, Exterior | solid concrete | 15 | auto |

Insulation Foundation Wall options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Insulation Foundation Wall characteristic”. See the OpenStudio-HPXML [Foundation Walls](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-foundation-walls) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ins_found_wall" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `foundation_wall_type` | false |  | Choice | auto, solid concrete, concrete block, concrete block foam core, concrete block perlite core, concrete block vermiculite core, concrete block solid core, double brick, wood | The material type of the foundation wall. |
| `foundation_wall_thickness` | false | in | Double | auto | The thickness of the foundation wall. |
| `foundation_wall_insulation_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Nominal R-value for the foundation wall insulation. Only applies to basements/crawlspaces. |
| `foundation_wall_insulation_location` | false | ft | Choice | auto, interior, exterior | Whether the insulation is on the interior or exterior of the foundation wall. Only applies to basements/crawlspaces. |
| `foundation_wall_insulation_distance_to_top` | false | ft | Double | auto | The distance from the top of the foundation wall to the top of the foundation wall insulation. Only applies to basements/crawlspaces. |
| `foundation_wall_insulation_distance_to_bottom` | false | ft | Double | auto | The distance from the top of the foundation wall to the bottom of the foundation wall insulation. Only applies to basements/crawlspaces. |
| `foundation_wall_assembly_r` | false | h-ft<sup>2</sup>-R/Btu | Double |  | Assembly R-value for the foundation walls. Only applies to basements/crawlspaces. If provided, overrides the previous foundation wall insulation inputs. |

The ResStock argument definitions set in the Insulation Foundation Wall characteristic

</div>

##### Distribution Assumption(s)

- CRHI is a copy of CR09

- CRAK is a copy of CR02.

#### Insulation Rim Joist

##### Description

Insulation level for rim joists. Set the same as the insulation level for the foundation wall.

##### Distribution Data Source(s)

- Engineering judgment.

##### Direct Conditional Dependencies

- Insulation Foundation Wall.

##### Option(s)

ResStock uses four different levels of rim-joist insulation as well as a “None” flag for homes without rim joists. These options map directly to the foundation wall insulation levels. The ResStock argument for `rim_joist_assembly_r` is always set to *auto*, and `rim_joist_continuous_interior_r` and `rim_joist_assembly_interior_r` are both set to 0 for all options.

| Option name    | Stock saturation | `rim_joist_continuous_exterior_r` |
|:---------------|:-----------------|:----------------------------------|
| None           | 48%              | 0                                 |
| Uninsulated    | 47%              | 0                                 |
| R-5, Exterior  | 1.2%             | 5                                 |
| R-10, Exterior | 2.8%             | 10                                |
| R-15, Exterior | 0.52%            | 15                                |

Options and saturation for Insulation Rim Joist

For the argument definitions, see Table “The ResStock argument definitions set in the Rim Joist characteristic”. See the OpenStudio-HPXML [Rim Joists](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-rim-joists) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ins_rim_joists" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `rim_joist_assembly_r` | false | h-ft<sup>2</sup>-R/Btu | Double |  | Assembly R-value for the rim joists. Only applies to basements/crawlspaces. Required if a rim joist height is provided. |
| `rim_joist_continuous_exterior_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Nominal R-value for the rim joist continuous exterior insulation. Only applies to basements/crawlspaces. |
| `rim_joist_continuous_interior_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Nominal R-value for the rim joist continuous interior insulation that runs parallel to floor joists. Only applies to basements/crawlspaces. |
| `rim_joist_assembly_interior_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Assembly R-value for the rim joist assembly interior insulation that runs perpendicular to floor joists. Only applies to basements/crawlspaces. |

The ResStock argument definitions set in the Rim Joist characteristic

</div>

##### Distribution Assumption(s)

- Rim joist insulation is the same value as the foundation wall insulation.

#### Ground Thermal Conductivity

##### Description

The thermal conductivity (in Btu/hr-ft-F) of the ground used in foundation and geothermal heat pump heat transfer calculations.

##### Distribution Data Source(s)

- Data from the Southern Methodist University Geothermal Laboratory. The data are from the Thermal Conductivity Observation in Content Model Format dataset. The data are available at <https://www.smu.edu/dedman/academics/departments/earth-sciences/research/geothermallab/datamaps/ngds-project>.

##### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004.

##### Option(s)

ResStock uses 8 options for Thermal Ground Conductivity, which is expressed in BTU/hr-ft-F (Table “Ground Thermal Conductivity options and arguments that vary for each option”). The ResStock arguments associated with each option vary only in the `site_ground_conductivity` parameter. The other two arguments, `site_soil_and_moisture_type` and `site_ground_diffusivity`, both receive `auto` assignment, regardless of the ResStock option.

<div id="table:hc_opt_ground_k" data-source="3a_ResStockInputs.tex">

| Option name | `site_ground_conductivity` |     |
|:------------|:---------------------------|:----|
| 0.5         | 0.5                        |     |
| 0.8         | 0.8                        |     |
| 1.1         | 1.1                        |     |
| 1.4         | 1.4                        |     |
| 1.7         | 1.7                        |     |
| 2.0         | 2.0                        |     |
| 2.3         | 2.3                        |     |
| 2.6         | 2.6                        |     |

Ground Thermal Conductivity options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Ground Thermal Conductivity characteristic”. See the OpenStudio-HPXML [Site](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-site) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ground_k" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `site_soil_and_moisture_type` | false |  | Choice | auto, clay, dry, clay, mixed, clay, wet, gravel, dry, gravel, mixed, gravel, wet, loam, dry, loam, mixed, loam, wet, sand, dry, sand, mixed, sand, wet, silt, dry, silt, mixed, silt, wet, unknown, dry, unknown, mixed, unknown, wet | Type of soil and moisture. This is used to inform ground conductivity and diffusivity. |
| `site_ground_conductivity` | false | Btu/hr-ft-F | Double |  | Conductivity of the ground soil. If provided, overrides the previous soil and moisture type input. |
| `site_ground_diffusivity` | false | ft<sup>2</sup>/hr | Double |  | Diffusivity of the ground soil. If provided, overrides the previous soil and moisture type input. |

The ResStock argument definitions set in the Ground Thermal Conductivity characteristic

</div>

##### Distribution Assumption(s)

- The data obtained are from surveyed oil and gas well data.

- The latitudes and longitudes were assigned to counties and the data were joined to the ResStock spatial lookup tables. In this process, 1,482 of 59,332 samples did not have a FIPS match or did not have data and were dropped.

- Due to limited data in climate zone 1A, data were pulled from samples in 1A plus Florida 2A.

- Samples less than 0.5 Btu/hr-ft-F are assigned a value of 0.5 Btu/hr-ft-F. Samples greater than 2.6 Btu/hr-ft-F are assigned a value of 2.6 Btu/hr-ft-F.

### Doors and Windows

In ResStock, two input files control door specification in ResStock:

- Doors

- Door Area.

Two similar input files specify windows:

- Windows

- Window Areas.

Discussed also in this section are building features that might impact shading in windows. All three of these inputs are either not used or have constant values for the entire stock:

- Interior Shading

- Eaves

- Overhangs.

#### Door Area

##### Description

Area of exterior doors. All ResStock models currently receive the same option.

##### Distribution Data Source(s)

- Engineering judgment.

##### Direct Conditional Dependencies

- None.

##### Option(s)

All ResStock housing units currently receive an option of 20 ft<sup>2</sup> for the exterior area of doors; see Table “Door Area options and arguments that vary for each option”.

<div id="table:hc_opt_door_area" data-source="3a_ResStockInputs.tex">

| Option name       | `door_area` |
|:------------------|:------------|
| 20 ft<sup>2</sup> | 20          |

Door Area options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Door Area characteristic”. See the OpenStudio-HPXML [Doors](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-doors) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_door_area" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Description |  |
|:---|:---|:---|:---|:---|:---|
| `door_area` | true | ft<sup>2</sup> | Double | The area of the opaque door(s). |  |

The ResStock argument definitions set in the Door Area characteristic

</div>

##### Distribution Assumption(s)

None

#### Doors

##### Description

Exterior door material and properties.

##### Distribution Data Source(s)

- Engineering judgment.

##### Direct Conditional Dependencies

- None

##### Option(s)

All homes in ResStock receive Fiberglass doors with an R-value of 5 (Table “Door options and arguments that vary for each option”).

<div id="table:hc_opt_door" data-source="3a_ResStockInputs.tex">

| Option name | `door_rvalue` |
|:------------|:--------------|
| Fiberglass  | 5             |

Door options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Door characteristic”. See the OpenStudio-HPXML [Doors](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-doors) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_door" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `door_rvalue` | true | h-ft<sup>2</sup>-R/Btu | Double |  | R-value of the opaque door(s) |

The ResStock argument definitions set in the Door characteristic

</div>

##### Distribution Assumption(s)

None.

#### Windows

##### Description

Construction type and efficiency levels of windows.

##### Distribution Data Source(s)

- U.S. EIA 2020 RECS microdata.

##### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Federal Poverty Level

- Geometry Building Type RECS

- Tenure

- Vintage ACS.

##### Option(s)

ResStock uses 10 window options in the baseline, with variation across number of panes, low-emissivity coating, and frame material. Across all Window options, multiple ResStock arguments are constant (Table “Windows options and arguments that vary for each option”). `window_natvent_availability`, `window_exterior_shading_winter`, `window_exterior_shading_summer`, `window_shading_summer_season`, and `skylight_storm_type` are all set to *auto*. Furthermore, two skylight window parameters are constant: `skylight_ufactor` is always set to 0.37 and `skylight_shgc` is always 0.3.

<div id="table:hc_opt_window" data-source="3a_ResStockInputs.tex">

| Option name | `window_ufactor` | `window_shgc` |
|:---|:---|:---|
| Single, Clear, Metal | 1.16 | 0.76 |
| Single, Clear, Metal, Exterior Clear Storm | 0.67 | 0.56 |
| Single, Clear, Non-metal | 0.84 | 0.63 |
| Single, Clear, Non-metal, Exterior Clear Storm | 0.47 | 0.54 |
| Double, Clear, Metal, Air | 0.76 | 0.67 |
| Double, Clear, Metal, Air, Exterior Clear Storm | 0.55 | 0.51 |
| Double, Clear, Non-metal, Air | 0.49 | 0.56 |
| Double, Clear, Non-metal, Air, Exterior Clear Storm | 0.34 | 0.49 |
| Double, Low-E, Non-metal, Air, M-Gain | 0.38 | 0.44 |
| Triple, Low-E, Non-metal, Air, L-Gain | 0.29 | 0.26 |

Windows options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Windows characteristic”. See the OpenStudio-HPXML [Windows](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-windows) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_wind" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `window_natvent_availability` | false | Days/week | Integer | auto | For operable windows, the number of days/week that windows can be opened by occupants for natural ventilation. |
| `window_ufactor` | true | Btu/hr-ft<sup>2</sup>-R | Double |  | Full-assembly National Fenestration Rating Council (NFRC) U-factor. |
| `window_shgc` | true |  | Double |  | Full-assembly NFRC solar heat gain coefficient. |
| `window_exterior_shading_winter` | false | Frac | Double | auto | Exterior shading coefficient for the winter season. 1.0 indicates no reduction in solar gain, 0.85 indicates 15% reduction, etc. |
| `window_exterior_shading_summer` | false | Frac | Double | auto | Exterior shading coefficient for the summer season. 1.0 indicates no reduction in solar gain, 0.85 indicates 15% reduction, etc. |
| `window_shading_summer_season` | false |  | String | auto | Enter a date like 'May 1 - Sep 30'. Defines the summer season for purposes of shading coefficients; the rest of the year is assumed to be winter. |
| `skylight_ufactor` | true | Btu/hr-ft<sup>2</sup>-R | Double |  | Full-assembly NFRC U-factor. |
| `skylight_shgc` | true |  | Double |  | Full-assembly NFRC solar heat gain coefficient. |
| `skylight_storm_type` | false |  | Choice | auto, clear, low-e | The type of storm, if present. If not provided, assumes there is no storm. |

The ResStock argument definitions set in the Windows characteristic

</div>

##### Distribution Assumption(s)

- All Triple-Pane options assumed to be low-e.

- Only breaking out clear and low-e windows for the Double, Non-Metal frame type.

- Source of low-e distribution is based on engineering judgment, informed by high-level sales trends observed in Ducker Worldwide studies of the U.S. market for windows, doors and skylights.

- Due to low sample sizes, the following adjustments are made:

  - Vintage data are grouped into: (1) \<1960, (2) 1960-79, (3) 1980-99, (4) 2000s, (5) 2010s.

  - Building Type data are grouped into: (1) Single-Family Detached, Single-Family Attached, and Mobile homes, and (2) Multifamily 2-4 units and Multifamily 5+ units.

  - Climate zones are grouped into:

    - 1A, 2A, 2B

    - 3A, 3B, 3C, 4B

    - 4A, 4C

    - 5A, 5B

    - 6A, 6B and

    - 7A, 7B 7AK, 8AK.

  <!-- -->

  - Federal Poverty Levels are progressively grouped together until all bins are combined.

  - Tenure options are progressively grouped together until all bins are combined.

- Storm window saturations are based on D&R International, Ltd. [2013](https://www.energy.gov/sites/prod/files/2013/11/f5/residential_windows_coverings.pdf). *Residential Windows and Window Coverings: A Detailed View of the Installed Base and User Behavior*. Cut the % storm windows by factor of 55% because only 55% of storms are installed year-round.

- Due to lack of performance data, Triple-Pane windows with storms are modeled without the storm windows.

- Due to lack of performance data, Double-Pane, Low-E, Non-Metal, Air, M-gain, and Exterior Clear Storm windows are modeled as Double-Pane, Clear, Non-Metal, Air, Exterior Clear Storm windows.

#### Window Areas

##### Description

Window-to-wall ratios for the front, back, left, and right walls.

##### Distribution Data Source(s)

- 2016-17 Residential Building Stock Assessment (RBSA) II microdata.

##### Direct Conditional Dependencies

- Geometry Building Type Height.

##### Option(s)

ResStock arguments use window-to-wall ratios to specify the window area instead of defining absolute window areas. Therefore, the following wall area constants are all set to zero in ResStock:

- `window_area_front` = 0

- `window_area_back` = 0

- `window_area_left` = 0

- `window_area_right` = 0

- `skylight_area_front` = 0

- `skylight_area_back` = 0

- `skylight_area_left` = 0

- `skylight_area_right` = 0.

ResStock has six different levels of window-to-wall ratios between 0.06 and 0.3 (Table “Window Area options and arguments that vary for each option”). Window-to-wall ratios are assumed constant on all sides of the home.

Additionally, the `window_aspect_ratio` is set to 1.333 for all ResStock options.

<div id="table:hc_opt_window_area" data-source="3a_ResStockInputs.tex">

| Option name | `window_front_wwr` | `window_back_wwr` | `window_left_wwr` | `window_right_wwr` |
|:---|:---|:---|:---|:---|
| F6 B6 L6 R6 | 0.06 | 0.06 | 0.06 | 0.06 |
| F9 B9 L9 R9 | 0.09 | 0.09 | 0.09 | 0.09 |
| F12 B12 L12 R12 | 0.12 | 0.12 | 0.12 | 0.12 |
| F15 B15 L15 R15 | 0.15 | 0.15 | 0.15 | 0.15 |
| F18 B18 L18 R18 | 0.18 | 0.18 | 0.18 | 0.18 |
| F30 B30 L30 R30 | 0.30 | 0.30 | 0.30 | 0.30 |

Window Area options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Window Area characteristic”. See the OpenStudio-HPXML [Windows](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-windows) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_window_area" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `window_front_wwr` | true | Frac | Double | The ratio of window area to wall area for the unit’s front facade. Enter 0 if specifying Front Window Area instead. |
| `window_back_wwr` | true | Frac | Double | The ratio of window area to wall area for the unit’s back facade. Enter 0 if specifying Back Window Area instead. |
| `window_left_wwr` | true | Frac | Double | The ratio of window area to wall area for the unit’s left facade (when viewed from the front). Enter 0 if specifying Left Window Area instead. |
| `window_right_wwr` | true | Frac | Double | The ratio of window area to wall area for the unit’s right facade (when viewed from the front). Enter 0 if specifying Right Window Area instead. |
| `window_area_front` | true | ft<sup>2</sup> | Double | The amount of window area on the unit’s front facade. Enter 0 if specifying Front Window-to-Wall Ratio instead. |
| `window_area_back` | true | ft<sup>2</sup> | Double | The amount of window area on the unit’s back facade. Enter 0 if specifying Back Window-to-Wall Ratio instead. |
| `window_area_left` | true | ft<sup>2</sup> | Double | The amount of window area on the unit’s left facade (when viewed from the front). Enter 0 if specifying Left Window-to-Wall Ratio instead. |
| `window_area_right` | true | ft<sup>2</sup> | Double | The amount of window area on the unit’s right facade (when viewed from the front). Enter 0 if specifying Right Window-to-Wall Ratio instead. |
| `window_aspect_ratio` | true | Frac | Double | Ratio of window height to width. |
| `skylight_area_front` | true | ft<sup>2</sup> | Double | The amount of skylight area on the unit’s front conditioned roof facade. |
| `skylight_area_back` | true | ft<sup>2</sup> | Double | The amount of skylight area on the unit’s back conditioned roof facade. |
| `skylight_area_left` | true | ft<sup>2</sup> | Double | The amount of skylight area on the unit’s left conditioned roof facade (when viewed from the front). |
| `skylight_area_right` | true | ft<sup>2</sup> | Double | The amount of skylight area on the unit’s right conditioned roof facade (when viewed from the front). |

The ResStock argument definitions set in the Window Area characteristic

</div>

##### Distribution Assumption(s)

- The window-to-wall ratios (WWR) are exponential weibull distributed

- Multifamily with 2-4 Units distributions are independent of Geometry Stories

- Multifamily with 5+ Units distributions are grouped by 1-3 stories, 4-7 stories, and 8+ stories

- High-rise Multifamily buildings (8+ stories) have a 30% WWR

- SFD, SFA, and Mobile Homes are represented by the SFD window area distribution.

#### Overhangs

##### Description

Presence, depth, and location of window overhangs (not currently used in ResStock baseline).

##### Distribution Data Source(s)

- Not applicable.

##### Direct Conditional Dependencies

- None.

##### Option(s)

ResStock currently assumes all buildings have no overhang. Therefore, all models are assigned the option of “None” for this characteristic, and receive the following ResStock arguments:

- `overhangs_front_depth` = 0

- `overhangs_front_distance_to_top_of_window` = 0

- `overhangs_front_distance_to_bottom_of_window` = 4

- `overhangs_back_depth` = 0

- `overhangs_back_distance_to_top_of_window` = 0

- `overhangs_back_distance_to_bottom_of_window` = 4

- `overhangs_left_depth` = 0

- `overhangs_left_distance_to_top_of_window` = 0

- `overhangs_left_distance_to_bottom_of_window` = 4

- `overhangs_right_depth` = 0

- `overhangs_right_distance_to_top_of_window` = 0

- `overhangs_right_distance_to_bottom_of_window` = 4

For the argument definitions, see Table “The ResStock argument definitions set in the Overhangs characteristic”. See the OpenStudio-HPXML [Overhangs](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-overhangs) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_overhang" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `overhangs_front_depth` | true | ft | Double | The depth of overhangs for windows for the front facade. |
| `overhangs_front_distance_to_top_of_window` | true | ft | Double | The overhangs distance to the top of window for the front facade. |
| `overhangs_front_distance_to_bottom_of_window` | true | ft | Double | The overhangs distance to the bottom of window for the front facade. |
| `overhangs_back_depth` | true | ft | Double | The depth of overhangs for windows for the back facade. |
| `overhangs_back_distance_to_top_of_window` | true | ft | Double | The overhangs distance to the top of window for the back facade. |
| `overhangs_back_distance_to_bottom_of_window` | true | ft | Double | The overhangs distance to the bottom of window for the back facade. |
| `overhangs_left_depth` | true | ft | Double | The depth of overhangs for windows for the left facade. |
| `overhangs_left_distance_to_top_of_window` | true | ft | Double | The overhangs distance to the top of window for the left facade. |
| `overhangs_left_distance_to_bottom_of_window` | true | ft | Double | The overhangs distance to the bottom of window for the left facade. |
| `overhangs_right_depth` | true | ft | Double | The depth of overhangs for windows for the right facade. |
| `overhangs_right_distance_to_top_of_window` | true | ft | Double | The overhangs distance to the top of window for the right facade. |
| `overhangs_right_distance_to_bottom_of_window` | true | ft | Double | The overhangs distance to the bottom of window for the right facade. |

The ResStock argument definitions set in the Overhangs characteristic

</div>

##### Distribution Assumption(s)

- All homes are assumed to not have window overhangs (roof eaves are defined separately).

#### Eaves

##### Description

Depth of roof eaves.

##### Distribution Data Source(s)

- Building America House Simulation Protocols ((Wilson et al. 2014)).

##### Direct Conditional Dependencies

None.

##### Option(s)

All buildings receive the same value of 2 feet for `geometry_eaves_depth`.

For the argument definitions, see Table “The ResStock argument definitions set in the Eaves characteristic”. See the OpenStudio-HPXML [Enclosure](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-enclosure) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_eaves" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_eaves_depth` | true | ft | Double |  | The eaves depth of the roof. |

The ResStock argument definitions set in the Eaves characteristic

</div>

##### Distribution Assumption(s)

None.

#### Interior Shading

##### Description

Amount of window shading in the summer and winter.

##### Distribution Data Source(s)

- ANSI/RESNET/ICC 301 Standard.

##### Direct Conditional Dependencies

- None.

##### Option(s)

All models in ResStock receive the same shading option (Table “Interior Shading options and arguments that vary for each option”).

<div id="table:hc_opt_int_shade" data-source="3a_ResStockInputs.tex">

| Option name | `window_interior_shading_winter` | `window_interior_shading_summer` |
|:---|:---|:---|
| Summer = 0.7, Winter = 0.85 | 0.85 | 0.7 |

Interior Shading options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Interior Shading characteristic”. See the OpenStudio-HPXML [Windows](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-windows) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_int_shad" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `window_interior_shading_winter` | false | Frac | Double | auto | Interior shading coefficient for the winter season. 1.0 indicates no reduction in solar gain, 0.85 indicates 15% reduction, etc. |
| `window_interior_shading_summer` | false | Frac | Double | auto | Interior shading coefficient for the summer season. 1.0 indicates no reduction in solar gain, 0.85 indicates 15% reduction, etc. |

The ResStock argument definitions set in the Interior Shading characteristic

</div>

##### Distribution Assumption(s)

None.

### Infiltration

Infiltration is air leakage between the envelope and the outdoor environment. In the U.S. residential sector, it is the leading driver of heating and cooling loads (compared to, for example, heat transfer through other parts of the envelope). In ResStock, infiltration is controlled by a single input file that provides a whole-home infiltration rate.

#### Infiltration

##### Description

Total infiltration to the dwelling unit.

##### Distribution Data Source(s)

- Distributions are based on the cumulative distribution functions from the [Residential Diagnostics Database (ResDB)](http://resdb.lbl.gov/).

- Alaska-specific distribution is based on Alaska Retrofit Information System (2008 to 2022), maintained by Alaska Housing Finance Corporation.

##### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Floor Area

- Vintage.

##### Option(s)

All infiltration options in ResStock are provided in air changes per hour (ACH) at 50 Pascals, as calculated by a blower door test. The characteristic sets the `air_leakage_leakiness_description`, `air_leakage_units`, `air_leakage_house_pressure`, `air_leakage_value`, `air_leakage_type`, and `site_shielding_of_home` ResStock arguments. For the argument definitions, see Table “The ResStock argument definitions set in the Infiltration characteristic”. See the OpenStudio-HPXML [Site](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html##hpxml-site) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_infil" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `site_shielding_of_home` | false |  | Choice | auto, exposed, normal, well-shielded | Presence of nearby buildings, trees, obstructions for infiltration model. |
| `air_leakage_leakiness_description` | false |  | Choice | auto, very tight, tight, average, leaky, very leaky | Qualitative description of infiltration. If provided, the Year Built of the home is required. Either provide this input or provide a numeric air leakage value below. |
| `air_leakage_units` | true |  | Choice | ACH, CFM (cubic feet per minute), ACHnatural, CFMnatural, EffectiveLeakageArea | The unit of measure for the air leakage if providing a numeric air leakage value. |
| `air_leakage_house_pressure` | false | Pa | Double |  | The house pressure relative to outside if providing a numeric air leakage value. Required when units are ACH or CFM. |
| `air_leakage_value` | false |  | string |  | Numeric air leakage value. For 'EffectiveLeakageArea', provide value in sq. in. If provided, overrides Leakiness Description input. |
| `air_leakage_type` | false |  | Choice | auto, unit total, unit exterior only | Type of air leakage. Type of air leakage if providing a numeric air leakage value. If 'unit total', represents the total infiltration to the unit as measured by a compartmentalization test, in which case the air leakage value will be adjusted by the ratio of exterior envelope surface area to total envelope surface area. Otherwise, if 'unit exterior only', represents the infiltration to the unit from outside only as measured by a guarded test. Required when unit type is single-family attached or apartment unit. |

The ResStock argument definitions set in the Infiltration characteristic

</div>

The options of the Infiltration characteristic range between 1 ACH 50 to 50 ACH 50 and set the `air_leakage_value` ResStock argument, Table “Infiltration options and arguments that vary for each option”.

Below is a list of arguments and their values that are constant across all the options.

- `air_leakage_leakiness_description` = auto

- `air_leakage_units` = ACH

- `air_leakage_house_pressure` = 50

- `air_leakage_type` = unit total

- `site_shielding_of_home` = normal

<div id="table:hc_opt_infil" data-source="3a_ResStockInputs.tex">

| Option name | `air_leakage_value` |
|:------------|:--------------------|
| 1 ACH50     | 1                   |
| 2 ACH50     | 2                   |
| 3 ACH50     | 3                   |
| 4 ACH50     | 4                   |
| 5 ACH50     | 5                   |
| 6 ACH50     | 6                   |
| 7 ACH50     | 7                   |
| 8 ACH50     | 8                   |
| 10 ACH50    | 10                  |
| 15 ACH50    | 15                  |
| 20 ACH50    | 20                  |
| 25 ACH50    | 25                  |
| 30 ACH50    | 30                  |
| 40 ACH50    | 40                  |
| 50 ACH50    | 50                  |

Infiltration options and arguments that vary for each option

</div>

##### Distribution Assumption(s)

- All ACH50 are based on Single-Family Detached blower door tests.

- Climate zones that are copied: 2A to 1A, 6A to 7A, and 6B to 7B.

- Vintage bins that are copied: 2000s to 2010s, 1950s to 1940s, 1950s to \<1940s.

- Homes are assumed to not be Weatherization Assistance Program qualified and not ENERGY STAR certified.

- Climate zones 7AK and 8AK are averages of 6A and 6B.

- ResStock models multi-family and SFA units with the unit total air leakage type. The unit total air leakage assume that some of the sampled ACH50 value goes to neighboring units. The model infiltration value to the exterior is a smaller infiltration value that what is sampled and is adjusted by the ratio of exterior envelope surface area to total envelope surface area. The modeled infiltration to the exterior is reported in the results.

- For Alaska, we are using a field in ARIS that lumps multifamily 2-4 units and multifamily 5+ units buildings together. Data from the American Community Survey are used to distribute proportionally between these two building types.

- For Alaska, Infiltration ACH50 values are calculated based on CFM50 from blower door test and estimated volume of the home.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-Bianchi2021" class="csl-entry">

Bianchi, Carlo, and Anthony Fontanini. 2021. *<span class="nocase">TMY3 Weather Data for ComStock and ResStock</span>*. <https://doi.org/10.7799/1756695>.

</div>

<div id="ref-BigLadderSoftware2015" class="csl-entry">

Big Ladder Software. 2015. *EnergyPlus Weather File (EPW) Data Dictionary*. <https://bigladdersoftware.com/epx/docs/8-3/auxiliary-programs/energyplus-weather-file-epw-data-dictionary.html>.

</div>

<div id="ref-Brown2019" class="csl-entry">

Brown, M., W. Cole, K. Eurek, et al. 2020. *Regional Energy Deployment System (ReEDS) Model Documentation: Version 2019*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy20osti/74111.pdf>.

</div>

<div id="ref-Gagnon2025" class="csl-entry">

Gagnon, Pieter, {Pedro Andres} {Sanchez Perez}, Julian Florez, James Morris, Marck {Llerena Velasquez}, and Jordan Eisenman. 2025. *Cambium 2024 Scenario Descriptions and Documentation*. Other. <https://doi.org/10.2172/2558937>.

</div>

<div id="ref-Nettleton2012" class="csl-entry">

Nettleton, G, and J Edwards. 2012. *Data Collection-Data Characterization Summary*. NorthernSTAR Building America Partnership, Building Technologies Program, U.S. Department of Energy.

</div>

<div id="ref-Ritschard1992" class="csl-entry">

Ritschard, R. L., J. W. Hanford, and A. O. Sezgen. 1992. *<span class="nocase">Single family heating and cooling requirements: Assumptions, methods, and summary results</span>*. Lawrence Berkeley Laboratory. <https://www.osti.gov/biblio/7243112>.

</div>

<div id="ref-nsrdb" class="csl-entry">

Sengupta, M., Y. Xie, A. Lopez, A. Habte, G. Maclaurin, and J. Shelby. 2018. “The National Solar Radiation Data Base (NSRDB).” *Renewable and Sustainable Energy Reviews*. <https://www.sciencedirect.com/science/article/pii/S136403211830087X>.

</div>

<div id="ref-Wilcox2008" class="csl-entry">

Wilcox, S., and W. Marion. 2008. *<span class="nocase">Users Manual for TMY3 Data Sets</span>*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy08osti/43156.pdf>.

</div>

<div id="ref-Wilson2014" class="csl-entry">

Wilson, E., C. Engebrecht Metzger, S. Horowitz, and R. Hendron. 2014. *2014 Building America House Simulation Protocols*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy14osti/60988.pdf>.

</div>

<div id="ref-Wilson2022" class="csl-entry">

Wilson, Eric, Andrew Parker, Anthony Fontanini, et al. 2022. *<span class="nocase">End-Use Load Profiles for the U.S. Building Stock: Methodology and Results of Model Calibration, Validation, and Uncertainty Quantification</span>*. National Renewable Energy Laboratory (NREL). <https://doi.org/10.2172/1854582>.

</div>

<div id="ref-Xing2014" class="csl-entry">

Xing, Lu. 2014. “<span class="nocase">Estimations of undisturbed ground temperatures using numerical and analytical modeling</span>.” PhD thesis, Oklahoma State University. <https://shareok.org/bitstream/handle/11244/15208/Xing_okstate_0664D_13659.pdf;jsessionid=B5F9178909D3631F0CCE74C1AA4F033D?sequence=1>.

</div>

</div>

[^1]: The Subarctic climate zone is not shown and is only found in Alaska.

[^2]: In review of the TMY3 data, we have identified some outliers in the initially published TMY3 data (e.g., erroneous temperature spikes). We have corrected those for ResStock use and published our corrected versions (Bianchi and Fontanini 2021).

[^3]: Occasionally nearby stations are used if data are missing from the target weather station.
