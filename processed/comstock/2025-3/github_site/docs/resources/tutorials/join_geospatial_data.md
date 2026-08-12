<!-- comstock 2025-3 | github_site | docs/resources/tutorials/join_geospatial_data.md -->
# Joining External Geospatial Data

# Tutorial: Joining Data from an External Dataset to ComStock using Geospatial Fields

**_This tutorial uses the ComStock 2023 Release 1 dataset. Some dataset attributes, like column names, may have changed in later releases. Most notably, the [ComStock sampling method was updated](docs/resources/explanations/new_sampling_method.md) to improve geographic resolution beginning with 2024 Release 2._**

## Introduction

The publicly available ComStock dataset provides users with a means to
analyze their building stock. Fields included in the dataset encompass
building stock characteristics, energy consumption, and some demographic
information. While these may be sufficient for some applications/use
cases, other users may need to join data to the ComStock dataset for
more specific analysis. This how-to guide will explain ComStock's
geo-encoding, including considerations for performing analysis with data
joined to ComStock, and instructions for joining the data.

## Best Practices and Considerations

ComStock building characteristics are sampled at the county-level. As
such, the assignment of building characteristics (and corresponding
energy results) have a high level of confidence at geospatial
resolutions of county-level and larger (state, census region, climate
zone, etc.). ComStock data also includes more granular geospatial
information for each model using common geospatial units: U.S. Census
PUMAs and Tracts. As defined by the U.S. Census, PUMAs, or Public Use
Microdata Areas, are "non-overlapping, statistical geographic areas that
partition each state or equivalent entity into geographic areas
containing no fewer than 100,000 people each." Census Tracts are "small,
relatively permanent statistical subdivisions of a county or
statistically equivalent entity that can be updated by local
participants prior to each decennial census as part of the Census
Bureau's Participant Statistical Areas Program (PSAP)."

Census PUMA and Tract are assigned to ComStock models *after* sampling
based on building type and building floor area distributions. There are
many Tracts within a single county, as is the case for many PUMAs
especially in densely populated areas. Building characteristics and
energy results analyzed at these geographic levels therefore have
*lower* confidence. There are relatively few ComStock models in single
counties, and separating the models further can lead to unrealistic
results. For example, consider a single county with around 300 building
models in it representing 14 building types and 80+ other building
characteristics included in ComStock. When ComStock places these models
into PUMAs or Tracts, the size of the building and the type of the
building are considered, but nothing else. This can have unintended
consequences when using this data at a PUMA or Tract level.

To better explain these consequences, let's consider a county that has
multiple Secondary Schools. Each school likely has different interior
lighting technologies, including but not limited to LEDs. However, a
single Secondary School ComStock model may be assigned to a PUMA or
Tract, and for the sake of this example let us assume this school is
modeled with LEDs. None of the decisions on which ComStock models are
assigned to a PUMA or Tract relied on data sources specifying which
lighting technology belongs in which Census Tract or PUMA. This makes
statements like "All schools in PUMA/Tract X have LEDs" problematic. The
geographic resolution of the ComStock lighting system-type attribute is
specified at a higher geographic resolution than a Tract or PUMA. As
such, it is entirely possible that instead of LED lighting technology,
the school(s) in the Tract/PUMA have not been updated since the 1980s,
and vice versa.

While this example used interior lighting, this issue is relevant for
all ComStock model properties and should be considered for every
analysis at the sub-county geographic level.

All this to say: Take care when analyzing ComStock data and joining
external datasets to results at sub-county geographic levels. When
possible, join data at a county-level or larger.

\*\*Note: Future iterations of ComStock sampling will assign building
characteristics at more geographically granular levels. This document
will be kept up-to-date as new features are rolled out.

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
