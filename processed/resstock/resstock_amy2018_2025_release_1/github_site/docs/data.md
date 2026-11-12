<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/data.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/data.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/data.html | corpus_version: resstock_amy2018_2025_release_1-v1-pre -->
# Data

Given the complexity and computational intensity of ResStock, the best pathway for professionals and researchers to use ResStock successfully is to use pre-created results, rather than running ResStock themselves. This section provides information about accessing ResStock results and links to published datasets.

The most up to date technical reference documentation for ResStock is available [here](assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf). Below is technical documentation for each dataset, but the previous link more fully explains current assumptions and methodologies, and should be used in junction with the documentation for each dataset release.

## Published Datasets
These datasets explore the annual and timeseries energy consumption of the U.S. residential building stock at the end-use level.
 - ResStock 2025 Release 1 [technical reference documentation](assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf) and [short description of each package and important dataset changes](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2025/resstock_amy2018_release_1/README_resstock_20251.pdf)
    - This dataset includes the addition of two states, Alaska and Hawaii. In addition, electric vehicles, load shifting, and load shedding have all been added, while geothermal heat pumps were expanded upon. Electric panel capacity and breaker information was also added. Finally, the utility rate methodology was updated.
 - ResStock 2024 Release 2 [webinar recording](https://youtube/tk1Uoq5_a38?si=gjhOnzb4-AcbdwZt), [webinar slides](https://www.nlr.gov/docs/fy24osti/89600.pdf), and the [technical reference documentation](https://docs.nlr.gov/docs/fy25osti/91621.pdf)
 - ResStock 2024 Release 1 [technical documentation](https://www.nlr.gov/docs/fy24osti/88109.pdf)
 - ResStock 2022 Release 1 [webinar recording](https://youtu.be/fd1ofceDaH4), [webinar slides](https://docs.nlr.gov/docs/fy23osti/84931.pdf), and the [technical documentation](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/EUSS_ResRound1_Technical_Documentation.pdf)
 - ResStock 2021 Release 1 [webinar recording](https://www.youtube.com/watch?v=PlGPDyiQ6n8&list=PLmIn8Hncs7bEYCZiHaoPSovoBrRGR-tRS&index=18) and the [technical documentation](https://www.osti.gov/biblio/1854582)

ResStock dataset releases are summarized in the following table with links for accessing the aggregate results. Scroll to the right for information on all of the datasets.

**<span style="color:red">Dataset Alerts:</span>**

**2025 Release 1**
- A few columns are only correctly documented for one upgrade, and incorrect for the rest of the upgrades in the 2025 Release 1 datasets. This issue can be circumvented by using other columns. Please see the [known issue report](docs/resources/explanations/Issue_2025_1_Column_Applicability.md) for additional information.

|   | **<span style="color:red">ResStock 2025 Release 1</span>** | **<span style="color:red">ResStock 2025 Release 1</span>** | **ResStock 2024 Release 2** | **ResStock 2024 Release 2** | **ResStock 2024 Release 1** | **ResStock 2022 Release 1** | **ResStock 2022 Release 1** | **ResStock 2022 Release 1** | **ResStock 2021 Release 1** | **ResStock 2021 Release 1** |
| **Weather Year** | AMY 2012 | AMY 2018 | AMY 2018 | TMY3 | TMY3 | AMY 2018 | AMY 2012 | TMY3 | AMY 2018 | TMY3 |
| **OEDI Name** | 2025/<br>resstock_amy2012_release_1 | 2025/<br>resstock_amy2018_release_1  | 2024/<br>resstock_amy2018_release_2 | 2024/<br>resstock_tmy3_release_2 | 2024/<br>resstock_dataset_2024.1/resstock_tmy3 | 2022/<br>resstock_amy2018_release_1 | 2022/<br>resstock_amy2012_release_1 | 2022/<br>resstock_tmy3_release_1 | 2021/<br>resstock_2018_release_1 | 2021/<br>resstock_tmy3_release_1 |
| **Data Viewer Links** | coming soon | [by state](https://resstock.nlr.gov/dataviewer?datasetName=vizstock_resstock_amy2018_r1_2025_ts_by_state_vu)  | [by state](https://resstock.nlr.gov/dataviewer?datasetName=vizstock_resstock_amy2018_2024_release_2_by_state_vu) | [by state](https://resstock.nlr.gov/dataviewer?datasetName=vizstock_resstock_tmy3_2024_release_2_by_state_vu) | n/a | [by state](https://resstock.nlr.gov/user/sign-in?next=/dataviewer%3FdatasetName%3Dvizstock_resstock_amy2018_release_2022_1_by_state_view) | [by state](https://resstock.nlr.gov/user/sign-in?next=/dataviewer%3FdatasetName%3Dvizstock_resstock_amy2012_release_2022_1_by_state_view) | [by state](https://resstock.nlr.gov/user/sign-in?next=/dataviewer%3FdatasetName%3Dvizstock_resstock_tmy3_release_2022_1_by_state_view) | [by_state](https://resstock.nlr.gov/dataviewer?datasetName=vizstock_resstock_amy2018_release_1_by_state),<br> [by_puma_northeast](https://resstock.nlr.gov/dataviewer?datasetName=vizstock_resstock_amy2018_release_1_by_puma_northeast),<br> [by_puma_midwest](https://resstock.nlr.gov/dataviewer?datasetName=vizstock_resstock_amy2018_release_1_by_puma_midwest),<br> [by_puma_south](https://resstock.nlr.gov/dataviewer?datasetName=vizstock_resstock_amy2018_release_1_by_puma_south),<br> [by_puma_west](https://resstock.nlr.gov/dataviewer?datasetName=vizstock_resstock_amy2018_release_1_by_puma_west) | [by_state](https://resstock.nlr.gov/dataviewer?datasetName=vizstock_resstock_tmy3_release_1_by_state),<br> [by_puma_northeast](https://resstock.nlr.gov/dataviewer?datasetName=vizstock_resstock_tmy3_release_1_by_puma_northeast),<br> [by_puma_midwest](https://resstock.nlr.gov/dataviewer?datasetName=vizstock_resstock_tmy3_release_1_by_puma_midwest),<br> [by_puma_south](https://resstock.nlr.gov/dataviewer?datasetName=vizstock_resstock_tmy3_release_1_by_puma_south),<br> [by_puma_west](https://resstock.nlr.gov/dataviewer?datasetName=vizstock_resstock_tmy3_release_1_by_puma_west) |
| **Data Table with<br> Characteristics** | [metadata](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2025%2Fresstock_amy2012_release_1%2Fmetadata_and_annual_results%2F&limit=50) | [metadata](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2025%2Fresstock_amy2018_release_1%2Fmetadata_and_annual_results%2F)  | [metadata](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2024%2Fresstock_amy2018_release_2%2Fmetadata_and_annual_results%2F) | [metadata](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2024%2Fresstock_tmy3_release_2%2Fmetadata_and_annual_results%2F) | [metadata](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2024%2Fresstock_dataset_2024.1%2Fresstock_tmy3%2Fmetadata_and_annual_results%2F) | [metadata](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2022%2Fresstock_amy2018_release_1%2Fmetadata_and_annual_results%2F) | [metadata](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2022%2Fresstock_amy2012_release_1%2Fmetadata_and_annual_results%2F) | [metadata](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2022%2Fresstock_tmy3_release_1%2Fmetadata_and_annual_results%2F) | [metadata](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2021%2Fresstock_amy2018_release_1%2Ftimeseries_aggregates_metadata%2F) | [metadata](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2021%2Fresstock_tmy3_release_1%2Ftimeseries_aggregates_metadata%2F) |
| **OpenEI Data Lake** | [data dictionary from AMY 2018](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2025/resstock_amy2018_release_1/data_dictionary.tsv) | [data dictionary](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2025/resstock_amy2018_release_1/data_dictionary.tsv)  | [data dictionary](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2024/resstock_amy2018_release_2/data_dictionary.tsv) | [data dictionary](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2024/resstock_tmy3_release_2/data_dictionary.tsv) | [data dictionary](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2024/resstock_dataset_2024.1/resstock_tmy3/data_dictionary.tsv) | [data dictionary](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/resstock_amy2018_release_1.1/data_dictionary.tsv) | [data dictionary](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/resstock_amy2012_release_1.1/data_dictionary.tsv) | [data dictionary](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/resstock_tmy3_release_1.1/data_dictionary.tsv) | [data dictionary](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2021/resstock_amy2018_release_1/data_dictionary.tsv) | [data dictionary](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2021/resstock_tmy3_release_1/data_dictionary.tsv) |
| **Publication Date** | November 2025 | October 2025 | March 2024 | March 2024 | February 2024 | September 2022 | September 2022 | October 2022 | October 2021 | October 2021 |
| **Release #** | 2025.1 | 2025.1 | 2024.2 | 2024.2 | 2024.1 | 2022.1 | 2022.1 | 2022.1 | 2021.1 | 2021.1 |
| **Building Stock<br> Represented** | Residential housing<br> stock circa 2018 | Residential housing<br> stock circa 2018 | Residential housing<br> stock circa 2018 | Residential housing<br> stock circa 2018 | Residential housing<br> stock circa 2018 | Residential housing<br> stock circa 2018 | Residential housing<br> stock circa 2018 | Residential housing<br> stock circa 2018 | Residential housing<br> stock circa 2018 | Residential housing<br> stock circa 2018 |
| **Upgrade Measures** | 28 | 28 | 15 | 15 | 260 | 10 | 10 | 10 | 0 | 0 |
| **Samples Simulated** | 550,000 | 550,000 | 550,000 | 550,000 | 2,200,000 | 550,000 | 550,000 | 550,000 | 550,000 | 550,000 |
| **Timeseries or<br> Annual Data** | Timeseries and<br> annual | Timeseries and<br> annual | Timeseries and<br> annual | Timeseries and<br> annual | Annual | Timeseries and<br> annual | Timeseries and<br> annual | Timeseries and<br> annual | Timeseries and<br> annual | Timeseries and<br> annual |
| **Representative Number of<br> Dwellings for Each Modeled<br> Dwelling Unit** | 253.9 | 253.9 | 252.3016 | 252.3016 | 63.0753 | 242.1310 | 242.1310 | 242.1310 | 242.1310 | 242.1310 |
| **Energy output available** | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **Carbon Emissions output<br> available** | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No |
| **Utility Bills output<br> available** | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No |
| **Indoor Air Temperature<br> output available** | Yes | Yes | Yes | Yes | No | Yes | Yes | No | No | No |
| **Electric Panel output<br> available** | Yes | Yes | No | No | No | No | No | No | No | No |
| **Comparison Dashboard<br> available** | No | [Yes](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2025%2Fresstock_amy2018_release_1%2Fcomparisons%2F&limit=50) | No | No | No | No | No | No | No | No |

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
