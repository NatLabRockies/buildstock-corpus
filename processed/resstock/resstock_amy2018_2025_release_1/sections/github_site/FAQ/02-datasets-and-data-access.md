<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/FAQ.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/FAQ.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/FAQ.html | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: github_site/docs/FAQ.md | section: Datasets and Data Access | lines: 40-142 -->
## Datasets and Data Access

### How do I access the dataset?

There are several access platforms available to access ComStock and ResStock datasets. See the [ComStock Data page](https://natlabrockies.github.io/ComStock.github.io/docs/data.html) and [ResStock Data page](docs/data.md) for more detail about dataset access and links to the public datasets.

### What do the codes used to describe "county_id" and other geographic fields mean?

ComStock and ResStock use the National Historical GIS (NHGIS) GISJOIN standard codes for county, census PUMA, and census tract, which are based on Federal Information Processing System (FIPS) codes. The datasets use the 2010 version of the GISJOIN codes--2020 are not available at this time. For more information about the geospatial fields available in the datasets, see [this explanation](https://natlabrockies.github.io/ComStock.github.io/docs/resources/explanations/reference_geographic_codes.html) for ComStock, and [this explanation](docs/resources/explanations/Geographic_Fields_and_Codes.md) for ResStock.

In most ComStock and ResStock datasets, county name is available in addition to the GISJOIN county code. For both tools, the column in the metadata_and_annual_results files on OEDI is called "in.county_name".

### I am trying to match buildings between releases, but noticed the building IDs do not match between them.

The building IDs and exact building characteristics between releases will not match because we re-sample our input characteristic distributions for every release. However, you can filter the building models using building characteristics to identify similar samples between releases. For instance, using building type, size, location, and wall construction type to identify similar models. The fields with the prefix “in.” show the available model inputs that you can use to do the comparison. You can see a complete list and description of available fields in the “data_dictionary.tsv” file on the OEDI Data Lake.

### Are descriptions available for the end-use categories and fields available for filtering?

Descriptions of each of the building characteristics and the end-use categories can be found in the “data_dictionary.tsv” file. Descriptions of the values used in those filters can be found in the “enumeration_dictionary.tsv”. Both files can be downloaded from the OEDI Data Lake and are unique to each dataset release. Use the correct data dictionary for the relevant dataset. They can be opened with Excel or a text editor.

Links to the OEDI Data Lake for each dataset release can be found on the [ComStock Data page](https://natlabrockies.github.io/ComStock.github.io/docs/data.html) and [ResStock Data page](docs/data.md).

### What are the data units?

ComStock and ResStock data have multiple units. For annual results data downloaded from the Open Energy Data Initiative (OEDI) data lake, units can be found in the "data_dictionary.tsv" file. Some fields will also have the units in the column header at the end of the name (e.g., "out.electricity.total.jan.energy_consumption..**kwh**"). Timeseries energy consumption data on OEDI are provided in kWh. Natural gas, fuel oil, and propane are output in kwh--this is intentional though unconventional.

The Data Viewer provides energy data in metric units, visible in the y-axis label. Depending on the scale of energy being shown, the metric prefix will automatically adjust (T for tera, G for giga, M for mega, etc.).

For Tableau dashboards, use the relevant column headers or the graph axis to see the units.

### What is the timezone of the timestamps?

The timestamps of all load profiles have been converted to Eastern Standard Time, to prevent issues when aggregating across time zones. The underlying modeling was conducted using local standard time for each location, with occupant schedules adjusted for daylight savings as applicable. All EnergyPlus timeseries outputs were converted from local standard time to Eastern Standard Time for publication in the web Data Viewer, Data Viewer exports, timeseries aggregates, and individual timeseries parquet files. In converting from local Standard Time to Eastern Standard Time, if necessary the last few hours of each dataset were moved to the beginning of the timeseries. For example, the first two hours of data from Colorado in Eastern Standard Time (Jan 1, midnight to 2 AM) were originally modeled as the last two hours of the year in Mountain Standard Time (Dec 31, 10 PM to midnight) using the corresponding weather. For leap years (e.g., 2012), the two hours come from Dec 31 regardless of whether the data is 365 or 366 days. Please see the *How are leap years modeled?* FAQ for more info.

### Do the timeseries aggregates have the sample weighting factors applied?

Yes. The aggregates represent the total relevant building stock with all relevant weights applied (e.g., all small office buildings in the state of Colorado), not just the sum of the model results.

### Are weather data files available in EPW format?

Weather data used for the modeling have been provided in .csv format for regression modeling, forecasting, or other analyses. The TMY3 weather files in EnergyPlus input format (EPW) can be downloaded from the NLR Data Catalog (https://data.nlr.gov/submissions/156), with filenames that correspond to county IDs in the ResStock and ComStock metadata. EPW format weather files for 2018 or other actual meteorological years (AMY) have not been publicly released. These files can be purchased from private sector vendors. See [here](https://energyplus.net/weather/simulation) for a list of providers.

### Is there an API to access data without downloading locally?

Currently, there is no API. However, we have posted a [tutorial](https://www.youtube.com/watch?v=qSR1MFpSiro&list=PLmIn8Hncs7bEYCZiHaoPSovoBrRGR-tRS&index=4) showing how to load the datasets into cloud services such as Amazon Web Services (AWS) so the data can be queried by analytic tools like Athena.

Example notebooks and SQL queries are also available on the [Access ComStock datasets programmatically](https://natlabrockies.github.io/ComStock.github.io/docs/resources/how_to_guides/example_scripts.html) page, and more will be added as we develop them. The queries and example notebooks are a good starting point for accessing ResStock programmatically, too.

### What software can I use to open the .parquet files?

Parquet files can be read using programming languages such as Python, using the pyarrow package. For other options, see [https://arrow.apache.org/docs/index.html](https://arrow.apache.org/docs/index.html). There are a few third-party graphical tools for viewing parquet files, but we have not tested them and the third-party support is limited.

See below for example Python code to convert parquet file to csv.

<pre><code>import pandas as pd
import os
folder_path = 'C:/Users/username/Documents/EUSS/Results'
file_name = '813-2'
suffix = '.parquet'
file = pd.read_parquet(os.path.join(folder_path, file_name+suffix))
new_suffix = '.csv'
file.to_csv(os.path.join(folder_path, file_name+new_suffix), index = False)
    </code></pre>

### Does the timestamp represent the beginning, middle, or end of each 15-minute interval?

The timestamp indicates the end of each 15-minute interval. So "12:15" represents the energy use between 12:00 and 12:15.

### Are the EnergyPlus model input files (.idf) or OpenStudio (.osm) files available?

Most ResStock datasets include the input files, though the file format provided varies. More recent datasets have xml and osm files, like the 2024 release 2. Older releases, have the following files:  2024 release 1 does not have either,  2022 release 1 has xml files, and 2021 release 1 has osm files.

### Are there load profiles available for the 16 California Climate Zones?

Yes, ResStock includes California Climate zone as a characteristic.

### How do I access the timeseries data for a specific building model?

To download a few results by IDs, you can use a manual approach. First use the metadata_and_annual_results to find the IDs you want to access. Then, note the download URL for any easy-to-access ID and edit it to reflect the ID you want.

For example, right clicking on the first ID under ResStock dataset 2022.1.1, AMY 2018, upgrade 02, and choosing “copy link” provides this URL [https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/resstock_amy2018_release_1.1/timeseries_individual_buildings/by_state/upgrade=2/state=WA/100025-2.parquet](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/resstock_amy2018_release_1.1/timeseries_individual_buildings/by_state/upgrade=2/state=WA/100025-2.parquet). To access ID 813 instead of 100025, change the “100025-2” to “813-2” in the URL, and paste it into a web browser. That will download the data for ID 813.

### How can I use AWS Athena to query ComStock and ResStock datasets?

Sample queries showing how to create prompts for different ComStock questions are available in the "[AWS Athena Queries](https://natlabrockies.github.io/ComStock.github.io/docs/resources/how_to_guides/aws_athena_queries.html)" how-to guide. These examples can be easily adapted to ResStock datasets.

A [training video](https://www.youtube.com/watch?v=qSR1MFpSiro) on how to load ComStock and ResStock data into AWS Athena is also available.

### What pre-aggregated timeseries data are available on the Open Energy Data Initiative (OEDI) data lake?

Pre-aggregated timeseries data are available in the "timeseries_aggregates" directory on OEDI and are provided for multiple geographic levels:

- ASHRAE/IECC climate zone
- Building America climate zone
- ISO/RTO region
- State

The data are further disaggregated into separate files by dwelling type.

These files provide aggregate, weighted, subhourly end-use energy data by fuel type for all ResStock models that meet the specified criteria. For example, the file **up00-co-mobile_home** contains aggregate end use load profiles for all mobile homes in Colorado.

Each file also includes "models_used" and "units_represented" columns, which indicate the number of ResStock models represented and the associated weighted number of units, respectively.

