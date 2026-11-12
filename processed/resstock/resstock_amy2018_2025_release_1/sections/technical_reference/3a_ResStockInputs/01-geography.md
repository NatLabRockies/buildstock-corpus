<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3a_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3a_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/3a_ResStockInputs.md | section: Geography | lines: 8-911 -->
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
<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/technical_reference/docs/technical_reference_guide/3a_ResStockInputs.yaml
     source: images/2010-PUMAs.png
     method: vision-description
     described: 2026-11-11 -->

<img alt="Outline map of the United States divided into 2010 Public Use Microdata Areas" src="images/2010-PUMAs.png" style="width:100.0%" />

Greyscale outline map of the contiguous United States with insets for Alaska and Hawaii. State borders are drawn heavy and Public Use Microdata Area boundaries thin. The areas are small and densely packed around large cities and along the coasts, and large across the rural West and Plains, where a single area can cover many counties. The map has no labels or legend.

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
<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/technical_reference/docs/technical_reference_guide/3a_ResStockInputs.yaml
     source: images/aiannh_48b.jpg
     method: vision-description
     described: 2026-11-11 -->

<img alt="Map of the contiguous United States with American Indian, Alaska Native and Native Hawaiian areas in green" src="images/aiannh_48b.jpg" style="width:100.0%" />

Map of the contiguous United States with state and county outlines on a pale background and AIANNH areas filled in green. The largest green areas are in the Four Corners region of Arizona, New Mexico and Utah, in eastern Oklahoma, and in South Dakota and Montana; many smaller areas are scattered across the West, the upper Midwest and the Southeast. Alaska and Hawaii are not shown.

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
<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/technical_reference/docs/technical_reference_guide/3a_ResStockInputs.yaml
     source: images/ashrae_iecc_cz_map_2004.jpg
     method: vision-description
     described: 2026-11-11 -->

<img alt="County-level map of the United States coloured by ASHRAE and IECC climate zone 1 to 7" src="images/ashrae_iecc_cz_map_2004.jpg" style="width:100.0%" />

County-level map of the contiguous United States coloured by climate zone, numbered 1 (the southern tip of Florida) to 7 (the northern Plains, northern Minnesota and high mountains), with zones 2 to 6 in bands between. A scale across the top divides the country into Marine (C), Dry (B) and Moist (A), and a white line marks the warm-humid area below it. Notes say all of Alaska is in Zone 7 except nine named boroughs in Zone 8, and that Zone 1 includes Hawaii, Guam, Puerto Rico and the Virgin Islands.

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
<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/technical_reference/docs/technical_reference_guide/3a_ResStockInputs.yaml
     source: images/building_america_cz.png
     method: vision-description
     described: 2026-11-11 -->

<img alt="Map of the United States coloured by Building America climate zone" src="images/building_america_cz.png" style="width:100.0%" />

Map of the contiguous United States and Puerto Rico coloured by Building America climate zone, with the zone names printed beside it: Marine along the Pacific coast; Cold / Very Cold across the northern half, with the Very Cold areas dotted; Mixed-Humid across the middle of the East; Hot-Humid along the Gulf and southern Atlantic coasts; and Hot-Dry / Mixed-Dry in the Southwest, with the Mixed-Dry areas dotted.

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
<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/technical_reference/docs/technical_reference_guide/3a_ResStockInputs.yaml
     source: images/CEC_Building_Climate_Zones.png
     method: vision-description
     described: 2026-11-11 -->

<img alt="Map of California&#x27;s 16 building climate zones, 2020, with an inset of the Los Angeles area" src="images/CEC_Building_Climate_Zones.png" style="width:100.0%" />

Map titled 'Building Climate Zones, California, 2020', from the California Energy Commission, with the 16 zones shaded and numbered and an inset enlarging the Los Angeles area. Zones 1 to 7 run down the coast from north to south, 8 to 10 lie inland in the south, 11 to 13 fill the Central Valley, 14 and 15 cover the deserts and 16 the mountains. A printed note says these zones are based on energy use, temperature, weather and other factors.

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
<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/technical_reference/docs/technical_reference_guide/3a_ResStockInputs.yaml
     source: images/ENERGY_STAR_Climate_Zone_Map.png
     method: vision-description
     described: 2026-11-11 -->

<img alt="Map of the United States coloured by the four ENERGY STAR climate zones" src="images/ENERGY_STAR_Climate_Zone_Map.png" style="width:100.0%" />

Map of the United States, with Alaska and Hawaii, coloured by the four ENERGY STAR climate zones. Northern (blue) covers the northern tier, the Mountain West and Alaska; North-Central (yellow) a band from California through the mid-Atlantic; South-Central (orange) the Southwest and the inland South; and Southern (red) southern California and Arizona, south Texas, the Gulf Coast, Florida and Hawaii.

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
<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/technical_reference/docs/technical_reference_guide/3a_ResStockInputs.yaml
     source: images/reeds_ba_map.png
     method: vision-description
     described: 2026-11-11 -->

<img alt="Map of the contiguous United States divided into ReEDS balancing areas, with interconnect boundaries" src="images/reeds_ba_map.png" style="width:100.0%" />

Map of the contiguous United States divided into ReEDS balancing areas, shaded in muted blue, green, tan and white so that neighbours differ, each subdivided by thin lines into wind and concentrating solar power regions. A red line marks the interconnect boundaries, running north to south through the Plains and around most of Texas. The legend names Interconnect, Balancing Area and Wind/CSP Region; the areas are not labelled.

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
<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/technical_reference/docs/technical_reference_guide/3a_ResStockInputs.yaml
     source: images/Cambium_GEA_map_2023.png
     method: vision-description
     described: 2026-11-11 -->

<img alt="Map of the contiguous United States divided into the 18 Cambium 2023 generation and emission assessment regions" src="images/Cambium_GEA_map_2023.png" style="width:100.0%" />

Map of the contiguous United States divided into 18 labelled regions: NorthernGrid West, NorthernGrid East, NorthernGrid South, CAISO, WestConnect North, WestConnect South, SPP North, SPP South, ERCOT, MISO North, MISO Central, MISO South, PJM West, PJM East, SERTP, FRCC, NYISO and ISONE. Each region is a group of smaller numbered balancing areas, 1 to 134, outlined in grey.

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
<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/technical_reference/docs/technical_reference_guide/3a_ResStockInputs.yaml
     source: images/custom_region_map.png
     method: vision-description
     described: 2026-11-11 -->

<img alt="Map of the contiguous United States coloured and numbered by ResStock custom region" src="images/custom_region_map.png" style="width:100.0%" />

Map of the contiguous United States, over a road-map background, coloured by ResStock custom region with each region's number and name printed on it: 2 Upper Midwest, 3 New England, 4 Great Lakes, 5 Mountain North, 6 Pacific Northwest, 7 Mid-Atlantic, 8 Zone 4A (two separate areas, in the central Plains and from Kentucky to Virginia), 9 Southeast, 10 Southwest and 11 California.

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

