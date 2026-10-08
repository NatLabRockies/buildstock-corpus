<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: b5faf42 | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: Outdoor Air Ventilation Rates | lines: 172-225 -->
## Outdoor Air Ventilation Rates

Commercial buildings require outdoor ventilation air when the building is occupied. The design outdoor air rate for a system is the minimum amount of outdoor air the system must supply while the building is occupied. The amount of outdoor air required for an HVAC system is calculated by the combined needs of the space type(s) served by a system.

ComStock design outdoor air ventilation rates follow the requirements set forth by ASHRAE Standard 62.1: Ventilation for Acceptable Indoor Air Quality (non-California models), or by DEER (California models). Both of these sources dictate the minimum design outdoor air flow rate by space type. The minimum outdoor air requirements for each space type are composed of a flow rate per person, a flow rate per area, and in some cases, an exhaust rate. Combined, these components determine the design outdoor air requirement for each space and its respective HVAC system. Table “Design Outdoor Air Rates by Building Type and HVAC Code Template for Buildings Outside California” and Table “Design Outdoor Air Rates by Building Type and HVAC Code Template for Buildings Inside California” show the average design outdoor air flow rate per area (cfm/m<sup>2</sup>) for non-California models and California models, respectively. These averages are influenced by the number of buildings of each type and their vintage. Both methods are heavily influenced by the space type composition of the model; ComStock models assume space type ratios for building types, with some building types having variation in the space type ratios. ComStock space types are described further in Section “Space Type Ratios”.

Some ComStock HVAC system types are residential style systems (denoted “residential” in Table “Fuel Type Category for ComStock HVAC System Types”). These systems do not include ventilation air and are an exception to the aforementioned ASHRAE-62.1 outdoor air methodology. Although commercial buildings all require outdoor ventilation air per code, some commercial buildings in the stock use residential systems without outdoor air. This is reflected in ComStock through the use of these residential system types. ComStock’s HVAC system selection methodology is described further in Section “HVAC System Types Probability Distributions”.

<div id="tab:outdoor_air_table" data-source="tables/design_outdoor_air_rates.tex">

| **Building Type** | **Pre-1980 (cfm/sf)** | **1980-2004 (cfm/sf)** | **90.1-2004 (cfm/sf)** | **90.1-2007 (cfm/sf)** | **90.1-2010 (cfm/sf)** | **90.1-2013 (cfm/sf)** |
|:---|:---|:---|:---|:---|:---|:---|
| **FullServiceRestaurant** | 1.103 | 1.103 | 1.107 | 1.048 | 1.067 | 1.077 |
| **Hospital** | \- | 0.258 | 0.254 | 0.258 | 0.258 | 0.258 |
| **LargeHotel** | 0.240 | 0.240 | 0.240 | 0.224 | 0.234 | 0.226 |
| **LargeOffice** | 0.098 | 0.098 | 0.098 | 0.098 | 0.098 | 0.098 |
| **MediumOffice** | 0.100 | 0.100 | 0.100 | 0.098 | 0.098 | 0.098 |
| **Outpatient** | 0.215 | 0.215 | 0.223 | 0.215 | 0.215 | 0.215 |
| **PrimarySchool** | 0.376 | 0.376 | 0.378 | 0.374 | 0.374 | 0.374 |
| **QuickServiceRestaurant** | 0.935 | 0.935 | 0.935 | 0.849 | 0.884 | 0.886 |
| **RetailStandalone** | 0.276 | 0.276 | 0.276 | 0.268 | 0.270 | 0.270 |
| **RetailStripmall** | 0.449 | 0.461 | 0.461 | 0.449 | 0.451 | 0.453 |
| **SecondarySchool** | 0.547 | 0.547 | 0.547 | 0.543 | 0.542 | 0.542 |
| **SmallHotel** | \- | \- | 0.138 | 0.100 | 0.100 | 0.100 |
| **SmallOffice** | 0.100 | 0.100 | 0.100 | 0.100 | 0.098 | 0.098 |
| **Warehouse** | 0.049 | 0.049 | 0.049 | 0.051 | 0.051 | 0.051 |

Design Outdoor Air Rates by Building Type and HVAC Code Template for Buildings Outside California

</div>

<div id="tab:outdoor_air_table_deer" data-source="tables/design_outdoor_air_rates_deer.tex">

| **Building Type** | **DEER Pre-1975 (cfm/sf)** | **DEER 1985 (cfm/sf)** | **DEER 1996 (cfm/sf)** | **DEER 2003 (cfm/sf)** | **DEER 2007 (cfm/sf)** | **DEER 2011 (cfm/sf)** | **DEER 2014 (cfm/sf)** | **DEER 2015 (cfm/sf)** | **DEER 2017 (cfm/sf)** |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| **FullServiceRestaurant** | 0.540 | 0.540 | 0.540 | 0.540 | 0.540 | 0.540 | 0.540 | 0.540 | 0.540 |
| **Hospital** | \- | 0.152 | 0.152 | 0.152 | 0.152 | 0.152 | 0.152 | 0.152 | \- |
| **LargeHotel** | 0.000 | 0.104 | 0.104 | 0.104 | 0.104 | 0.104 | 0.104 | 0.104 | 0.104 |
| **LargeOffice** | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 |
| **MediumOffice** | \- | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 |
| **Outpatient** | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 |
| **PrimarySchool** | \- | 0.447 | 0.447 | 0.447 | 0.447 | 0.447 | 0.447 | 0.447 | 0.447 |
| **QuickServiceRestaurant** | 0.439 | 0.439 | 0.439 | 0.439 | 0.439 | 0.439 | 0.439 | 0.439 | 0.439 |
| **RetailStandalone** | 0.268 | 0.268 | 0.268 | 0.268 | 0.268 | 0.268 | 0.268 | 0.268 | 0.268 |
| **RetailStripmall** | 0.327 | 0.323 | 0.323 | 0.323 | 0.323 | 0.323 | 0.325 | 0.323 | 0.323 |
| **SecondarySchool** | 0.433 | 0.433 | 0.433 | 0.433 | 0.433 | 0.433 | 0.433 | 0.433 | 0.433 |
| **SmallHotel** | 0.069 | 0.069 | 0.069 | 0.069 | 0.069 | 0.069 | 0.069 | 0.069 | 0.069 |
| **SmallOffice** | 0.077 | 0.077 | 0.077 | 0.077 | 0.077 | 0.077 | 0.077 | 0.077 | 0.077 |
| **Warehouse** | 0.150 | 0.150 | 0.150 | 0.150 | 0.150 | 0.150 | 0.150 | 0.150 | 0.150 |

Design Outdoor Air Rates by Building Type and HVAC Code Template for Buildings Inside California

</div>

