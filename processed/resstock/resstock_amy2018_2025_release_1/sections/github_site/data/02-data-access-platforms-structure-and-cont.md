<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/data.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/data.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/data.html | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: github_site/docs/data.md | section: Data Access Platforms, Structure, and Content | lines: 44-161 -->
## Data Access Platforms, Structure, and Content
ResStock data releases are collections of datasets that include energy use across technology (e.g., air-conditioning, refrigerators, lighting) and fuel type that represent the United States housing stock. Data include either 550,000 or 2,200,000 models that if scaled up cover all residential energy use in the U.S. housing sector. Data releases also include “what-if” scenarios of technology adoption. The output of each energy model is one year of energy consumption, either summed for the whole year or at 15-minute intervals.

Dealing with the raw output data from a national ResStock dataset requires skills for dealing with large files and large numbers of files, that might make interpretation inaccessible for many users. To support many use cases, aggregate load profiles (i.e. timeseries energy use added together from multiple models) for the following geographic resolutions  are published for ResStock releases:
- 17 ASHRAE/International Energy Conservation Code (IECC) climate zones
- 8 U.S. Department of Energy Building America climate zones
- 2,300 + U.S. Census Public Use Microdata Areas
- 3,100+ U.S. counties
- 50 states (as of ResStock 2025 Release 1, all 50 U.S. states are now represented)

### Data Access Platforms
The following table summarizes the various ways to access and use ResStock data. Scroll right to see all of the options.

|   | **Metadata** | **Individual Load Profiles** | **Aggregate Load<br> Profiles** | **Data Viewer** | **Dashboards** | **Full Database** |
| **Data Format** | .csv and<br> parquet files | .csv and<br> parquet files | .csv and<br> parquet files | Interactive dashboard<br> with .csv exports | Interactive dashboards<br> with image, .xlsx, .csv, .pdf<br>, .pptx, and tableau workbook<br> exports | Amazon S3 bucket|
| **Time Scale** | Annual | 15-minute intervals | 15-minute intervals | Customizable | Annual | Annual or 15-minute<br> intervals |
| **Grouped By** | Individual<br> Building ID | Individual<br> Building ID | ASHRAE IECC<br> Climate Zone 2004,<br> Building America Climate<br> Zone, ISO RTO region,<br> State | Customizable | Customizable | Customizable |
| **Fields By** | Building Input<br> Characteristics | - | Building type | - | Building Input<br> Characteristics |Building Input<br> Characteristics |
| **Fields By** | Energy Consumption |Energy Consumption |Energy Consumption |Energy Consumption |Energy Consumption |Energy Consumption |
| **Fields By** | Energy Savings |Energy Savings |Energy Savings |Energy Savings |Energy Savings |Energy Savings |
| **Fields By** | Emissions | Emissions | Emissions | Emissions | Emissions | Emissions |
| **Fields By** | Calculated Fields | Calculated Fields | Calculated Fields | - | Calculated Fields | Calculated Fields |
| **Accessed Via** | [Open Energy Data<br> Initiative](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F) (OEDI) | [Open Energy Data<br> Initiative](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F) (OEDI) | [Open Energy Data<br> Initiative](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F) (OEDI) | [resstock.nlr.gov](https://resstock.nlr.gov/) | [public.tableau.com/app/profiles/nrel.buildingstock/vizzes](https://public.tableau.com/app/profile/nrel.buildingstock/vizzes) | Scripting Languages |

The dataset has been formatted in multiple ways to meet the needs of different users and use cases.
- **Metadata**: File of individual modeled dwelling unit housing and demographic characteristics together with annual energy and other results. This is often called the “metadata” file.
- **Load Profiles**: Timeseries energy and other results (individual building or pre-aggregated by geography) in downloadable spreadsheets.
- **Data Viewer**: A web-based interactive data viewer with customizable time scales and aggregations.
- **Dashboards**: In-depth web-based interactive data viewer with customizable aggregations for exploring annual results and sometimes supplemental metrics (e.g., upgrade costs).
- **Full Database**: Full raw model results. Big data skills required.

Aggregate ResStock datasets can be accessed via the [Open Energy Initiative (OpenEI) Data Lake](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2F), the [ResStock Data Viewer](https://resstock.nlr.gov/datasets), and the [ResStock dashboards](https://public.tableau.com/app/profile/nrel.buildingstock/vizzes). Each data release can have multiple datasets for different weather years. Within the weather years, all dataset releases include 2018 and a “TMY3” weather year, which is a “typical meteorological year”. These weather files attempt to avoid capturing any year’s unusual weather pattern by compiling the most representative historical weather for a location. TMY3 timeseries energy data should not be used for larger geographies, i.e., one or more counties. In compiling the typical/representative weather TMY3 weather files pull months of historical weather from different years (e.g., January 2005, February 2002, March 1995). A key issue is that adjacent counties might pull their historical weather from different years, so regional weather patterns will not be aligned in aggregate timeseries results. Aggregate annual energy results can be used together because they will smooth out weather differences.

Note that there are separate public datasets available for residential and commercial building stocks. If you are interested in commercial buildings, please check out our sibling tool [ComStock](https://comstock.nlr.gov/).

### Open Energy Data Initiative (OEDI) Data Lake
OpenEI, or OEDI, is an energy information portal developed and maintained by NLR with funding and support from the U.S. Department of Energy and a network of international partners and sponsors. The OpenEI data lake contains comprehensive aggregate data for ResStock releases. This includes metadata and timeseries energy consumption results (baseline and upgrades, if applicable), individual building energy models, weather files, geographic information, and data dictionaries.

The ResStock release directory structure of the data lake is summarized in the table below.

### ResStock Data Viewer
The ResStock Data Viewer exists to quickly filter, slice, combine, visualize, and download results in custom ways. This platform is available at [resstock.nlr.gov/datasets](https://resstock.nlr.gov/datasets), and the Data Viewer link for each dataset is listed when available. Multiple geographic views of the datasets on the data viewer have been created: by state, by Census region, and by PUMA.

![](../assets/images/data-viewer-home-page.png)

### ResStock Dashboards
ResStock dashboards exist to give a more comprehensive overview of results in different ways, from housing characteristics, specific housing upgrade scenarios, or even focusing on a specific topic like heat pumps. This platform is available at [public.tableau.com/app/profile/nrel.buildingstock/vizzes](https://public.tableau.com/app/profile/nrel.buildingstock/vizzes). Multiple geographic views of the datasets on the dashboards have been created: by state, by Building America Climate Zone, and by AHSRAE/IECC Climate Zone.

![](../assets/images/tableau-home.png)

### OEDI Directory Structure and Contents

| **Name** | **Contents** |
| building_energy_models | Building energy models, in OpenStudio format, that were run to<br> create the dataset. |
| geographic_information | Information on various geographies used in the dataset<br> provided for convenience. Includes map files showing the<br> shapes of the geographies (states, PUMAs) used for<br> partitioning and lookup table mapping between census tracts<br> and various other geographies. |
| metadata_and_annual_results | Building characteristics (age, area, HVAC system type, etc.) for<br> each of the building energy models run and annual results for<br> the data. |
| timeseries_aggregates | Aggregate end-use load profiles by building type and geography<br> that can be opened and analyzed in Excel, Python, or other<br> common data analysis tools. Aggregated at different<br> geographies. |
| timeseries_individual_buildings | The raw timeseries data for each building energy model. **This is<br> a large number of individual files!** |
| weather | Key weather data used as an input to run the building energy<br> models to create the dataset. |
| data_dictionary.tsv | Describes the column names found in the metadata and<br> timeseries data files. |
| enumeration_dictionary.tsv | Expands the definitions of the enumerations used in the<br> metadata files. |
| upgrades_lookup.json | Measure package number matched with measure package<br> name for quick reference. |

### Dataset Naming Convention
ResStock releases on OEDI and the Data Viewer use a variation of the following naming convention.

Example 1: \<dataset type\>_\<weather data\>\_release\_<release number\>

Example 1: resstock_amy2018_release_1

1. Dataset type
    - resstock = residential building stock
    - comstock = commercial building stock

2. Weather data
    - amy2018 = actual meteorological year 2018 (2018 weather data from NOAA ISD, NSRDB, and MesoWest)
    - tmy3 = typical meteorological year from 1991-2005 (see [this publication](https://www.nlr.gov/docs/fy08osti/43156.pdf) for details )

3. Release
    - release_1 = first release of the dataset during the year of publication
    - release_2 = second release of the dataset during the year of publication
    - release_1.1 = first minor release that modifies the release_1 dataset

### Field Naming Convention as of ResStock 2025 Release 1
Below is a description of the field naming convention. The general topics are below, but this may not be a comprehensive list depending on the dataset, and not all fields may be represented depending on the file type.

At the highest level there is – “in.” for inputs, “out.” For outputs, and then a handful of other columns that provide simulation information.

For the “out.” prefix there is a second level that includes – fuel type, model parameter and statistic fields, site energy, and other results. The “in.” prefix does not have a second level.

The third level of “out.” includes the end uses.

Finally, units are denoted by a “..” with the unit following.

| **First Level** |   |   |
| **Prefix or name** | **Description** | **Example** |
| bldg_id | unique id of the building model | 673 |
| upgrade | unique id number of the upgrade | 1 |
| weight | how many dwelling units this<br> building model represents<br> in real life | 63.075 |
| applicability | indication if the upgrade<br> was applied to that building<br> model| TRUE |
| completed status | if the building energy model was successfully run | Success |
| in. | inputs of building characteristics<br> and geospatial codes | in.sqft..Ft2 |
| out. | modeled outputs | out.electricity.plug_loads.<br>energy_consumption..Kwh |

| **Second Level** |   |   |
| **Prefix or name** | **Description** | **Example** |
| out.params | value of characteristics of<br> the upgraded dwelling that<br> can be potentially used as<br> cost multiplier | out.params.size water heater..gal |
| out.[fuel type] | fuel type - electricity, natural gas,<br> propane, etc. | out.electricity.net.energy consumption..kwh |
| out.site energy | total of all end uses, site energy | out.site energy.total.energy consumption..kwh |
| out.load | energy delivered by the technology | out.load.hot water.energy delivered..kbtu |
| out.emissions | amount emissions are reduced | out.emissions reduction.propane.total..co2e kg |
| out.energy_burden | energy burden of the dwelling unit | out.energy burden..percentage |
| out.utility bills | energy bill of the dwelling unit<br> and currency | out.utility bills.fuel oil bill..usd |
| out.unmet hours | number of hours the HVAC system<br> could not meet load | out.unmet hours.cooling..hr |
| upgrade.hvac [system efficiency] | HVAC system efficiency | upgrade.hvac cooling efficiency |

| **Units** |   |   |
| ..foo | ".." denotes the start of the unit name | ..co2e kg |
