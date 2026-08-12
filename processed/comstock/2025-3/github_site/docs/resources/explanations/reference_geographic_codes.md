<!-- comstock 2025-3 | github_site | docs/resources/explanations/reference_geographic_codes.md -->
# Geographic Fields and Codes

## Is there a legend or lookup for the geographic codes (G0100010, G01000100, etc.) in ComStock data sets?

ComStock provides many geographic fields to allow for a variety of analyses. Many of these codes are relatively self explanatory, however some of them are specifically designed for machine processing and not user friendly. The most extreme example of this are the strings used in ComStock to represent Counties, Census Tracts, and Public Use Microdata Areas (PUMAs). ComStock uses the National Historical GIS (NHGIS) GISJOIN standard codes for county, Census PUMA, and Census Tract, which are based on Federal Information Processing System (FIPS) codes.

Table 1 provides a list of ComStock geographic fields published with the dataset, also published as part of the spatial_tract_lookup_table.csv file (example file linked [here](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2021%2Fresstock_amy2018_release_1%2Fgeographic_information%2F)). As more geographic data becomes available, this list may grow. County and Census PUMA codes can be found in the ComStock dataset using the \"in.nhgis_county_gisjoin\" and \"in.nhgis_puma_gisjoin\" columns, respectively.

| Geospatial Fields             | ComStock Results Column Header   | Format and Example                          |
|-------------------------------|----------------------------------|---------------------------------------------|
| ASHRAE / IECC Climate Zone    | in.climate_zone_ashrae_2006      | String<br>Ex: 2A                            |
| Building America Climate Zone | in.climate_zone_building_america | String<br>Ex: Hot-Humid                     |
| Census Region                 | in.census_region_name            | String<br>Ex: South                         |
| Census Division               | in.census_division_name          | String<br>Ex: East South Central            |
| Cambium Grid Region           | in.cambium_grid_region           | String<br>Ex: SRSOc                         |
| State                         | in.state_abbreviation            | String<br>Ex: AL                            |
| County                        | in.nhgis_county_gisjoin          | NHGIS GISJOIN; String<br>Ex: G0100030       |
| Census PUMA                   | in.nhgis_puma_gisjoin            | NHGIS GISJOIN; String<br>Ex: G01002600      |
| Census Tract                  | in.nhgis_tract_gisjoin           | NHGIS GISJOIN; String<br>Ex: G0100030010800 |

Table 1. Geospatial fields in the ComStock dataset

Two steps are required to understand a GISJOIN string. First, the geography in question needs to be specified using a numeric FIPS codes. There are many databases available that assist in doing this, but [for quick reference this Wikipedia page listing State and County FIPS codes](https://en.wikipedia.org/wiki/List_of_United_States_FIPS_codes_by_county) is very handy. Specifying Census Tracts is generally best done using a Geographic Information System (GIS) tool, but maps are available on the [Census Bureau website](https://www.census.gov/geographies/reference-maps/2010/geo/2010-census-tract-maps.html).

A brief aside -- why, one might reasonably ask, can't we all just use the names of counties? The answer generally is two-fold. First of all, consider St. Croix County. A reasonable person might type this as "St. Croix County" or "St Croix County" or "Saint Croix County". Some databases really don't like having "."s in the names of things -- what do we do then? The second issue has to do with entities that are similar to but not the same as counties, including but not limited to independent cities, census areas, villages, and boroughs. For example, Fairfax City and Fairfax County are separate geographic areas within Virginia. This can introduce additional confusion as names can within a state. While various 'solutions' exist to this set of problems, none of them are nearly as standard as the use of FIPS codes.

Once the FIPS code has been determined, it must be 'encoded' into the NHGIS GISJOIN standard. Follow the [instructions provided by the NHGIS organization](https://www.nhgis.org/geographic-crosswalks#geog-ids) (summarized in Table 2 below) to do this encoding. The length of the string depends on the geographic resolution, with higher resolutions requiring more characters. All GISJOIN codes begin with the letter "G" to prevent applications from automatically reading the identifier as a number and, in effect, dropping important leading zeros.

| Component         | ComStock Field(s)                                                      | Example        | Notes |
|-------------------|------------------------------------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| State NHGIS code  | in.nhgis_county_gisjoin, in.nhgis_tract_gisjoin, in.nhgis_puma_gisjoin | G<u><b>010</b></u>           | 3 digits (FIPS + "0"). NHGIS adds a zero to state FIPS codes to differentiate current states from historical territories.<br>010 = Alabama                                                        |
| County NHGIS code | in.nhgis_county_gisjoin                                                | G010<u><b>0030</b></u>       | State NHGIS code plus 4 digits (county FIPS + "0"). NHGIS adds a zero to county FIPS codes to differentiate current counties from historical counties.<br>0030 = Baldwin County                   |
| PUMA NHGIS code   | in.nhgis_puma_gisjoin                                                  | G010<u><b>02600</b></u>      | State NHGIS code plus 5 digits (PUMA). To find the 5-digit PUMA code based on a city or place name, use this file from the U.S. Census Bureau: [2010_PUMA_Names.pdf](https://www2.census.gov/geo/pdfs/reference/puma/2010_PUMA_Names.pdf)<br>02600 = Baldwin County PUMA |
| Census tract code | in.nhgis_tract_gisjoin                                                 | G0100030<u><b>010800</b></u> | County NHGIS code plus 6 digits for 2000 and 2010 tracts. 1990 tract codes use either 4 or 6 digits.                                                                                              |
| Census block code | N/A, not supported at this time                                        | N/A            | 4 digits for 2000 and 2010 blocks. 1990 block codes use either 3 or 4 digits.                                                                                                                     |

Table 2. National Historical GIS organization FIPS codes
