<!-- comstock comstock_amy2018_2025_release_3 | github_site | docs/resources/tutorials/join_geospatial_data.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/resources/tutorials/join_geospatial_data.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/resources/tutorials/join_geospatial_data.html | corpus_version: b5faf42 | corpus_path: github_site/docs/resources/tutorials/join_geospatial_data.md | section: Instructions | lines: 77-158 -->
## Instructions

ComStock has nine levels of geospatial granularity, from Climate Zone to
Census TRACT. These fields allow for many geospatial datasets to be
joined to the results for further analysis. This document provides
instructions on how to join data to ComStock.

Table 1 provides a summary of the geospatial fields in the ComStock
results, with information about the corresponding column header, and
format of the field. Climate zones cross state lines and are important
in establishing minimum standards for buildings and equipment. Census
Regions and Divisions are groupings of states that subdivide the U.S.
They are commonly used in building stock characteristic surveys and
analyses. Cambium Grid Regions are 20 regions covering the contiguous
U.S. and allow ComStock to include granular projected emissions in the
dataset. Census PUMA and Tract, as mentioned above, are the most
granular geographic resolution in the ComStock dataset and allow for
joining of common external datasets.

Table 1. Geospatial fields in the ComStock dataset

| **Geospatial Fields** | **ComStock Results Column Header** | **Format and Example** |
| ASHRAE / IECC Climate Zone | in.climate_zone_ashrae_2006 | String <br> Ex: 2A  |
| Building America Climate Zone  | in.climate_zone_building_america   | String <br> Ex: Hot-Humid |
| Census Region        | in.census_region_name   | String <br> Ex: South |
| Census Division      | in.census_division_name | String <br> Ex: East South Central  |
| Cambium Grid Region  | in.cambium_grid_region  | String <br> Ex: SRSOc  |
| State                | in.state_abbreviation   | String <br> Ex: AL   |
| County               | in.nhgis_county_gisjoin | NHGIS; String <br> Ex: G0100030 |
| Census PUMA          | in.nhgis_puma_gisjoin   | NHGIS; String <br> Ex: G01002600 |
| Census Tract         | in.nhgis_tract_gisjoin  | NHGIS; String <br> Ex: G0100030010800  |

To join a dataset to the ComStock results,

1.  First identify the ComStock geospatial field that matches the
    geospatial granularity in your external dataset.

2.  Down select the ComStock dataset to only the rows that match your
    dataset. For example, in the case of joining a dataset that only
    covers the state of Colorado, remove all ComStock results from
    outside of Colorado. This can dramatically increase join performance
    in Step 5.

3.  Create a new column in the external dataset with the desired
    geospatial join field reformatted to match the ComStock field.

    1.  If joining on the County, Census PUMA, or Census Tract IDs you
        will need to do the following:

        1.  Identify the geographies in the external dataset using their
            Federal Information Standard (FIPS) code. These codes
            identify the state and county using two- and three-digit
            numbers respectively, e.g. 02 and 131. FIPS codes are almost
            always included in any external dataset.

        2. Follow the instructions provided by the National Historical
            GIS (NHGIS) organization to encode the FIPS values into a
            GISJOIN string. The length of the string depends on the
            geographic resolution, with higher resolutions requiring
            more characters. Please review the NHGIS GISJOIN
            documentation here and Table 1 above for County, Census
            PUMA, and Census Tract examples.

4.  Verify that the reformatted external dataset column matches the
    ComStock geospatial field by manually checking a few values.

5.  Use your preferred data processing tool (Python, Microsoft Excel,
    etc.) to make the join.

    a.  If using Excel, use the Power Query feature. Use the reformatted
        join column in your external dataset, the columns to be joined
        in your external dataset, and the ComStock geospatial field.
        Documentation for how to use this feature can be found from
        Microsoft here.

    b.  If using the Pandas library in Python, use the merge command.
        Documentation for how to do this can be found from the Pandas
        team here.

6.  Manually verify that the join has worked as expected. Be sure to
    test at random throughout the ComStock data, and not just the first
    few entries in the dataset.
