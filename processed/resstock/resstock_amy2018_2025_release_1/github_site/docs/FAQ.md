<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/FAQ.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/FAQ.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/FAQ.html | corpus_version: resstock_amy2018_2025_release_1-v1-pre -->
# FAQ

# Frequently Asked Questions

Below are some frequently asked questions (FAQ) about ResStock. The questions are divided into ResStock essentials, datasets and data access, the data viewer, analysis, and then finally a modeling methods, assumptions, and documentation section. If you have another question, please email our team at [ResStock@nlr.gov](mailto:ResStock@nlr.gov).

## ResStock Essentials

### Is ResStock credible?

Yes. The models underwent extensive calibration as part of the End Use Load Profiles (EULP) project where we compared model load profiles to AMI data from around the country, and updated baseline model schedules, power densities, among other things using various data sources. Reference the [EULP final report](https://www.nlr.gov/docs/fy22osti/80889.pdf) for more details. The EULP project concluded in 2021.

For details about how to determine whether the models are appropriate for a specific analysis, reference [this explanation](docs/resources/explanations/Considerations_for_ResStock_Calibration_and_Validation.md).

### Which dataset release should I use? And can I compare upgrades from different dataset releases?

We recommend using the latest data release whenever possible. However, older datasets still provide valuable information and can be used if newer datasets are not appropriate for a specific use. We do not recommend a comparison of upgrade measures across different dataset releases due to the changes and improvements made in each dataset release. Each new dataset release includes its own set of upgrade measures, some of which are repeats, and improvements made to the baseline model and modeling methodology. See the [Data page](docs/data.md) for a list of available datasets and access links, as well as technical documentation for the ResStock tool.

### What are weights in ResStock and how are they used?

Weights in ResStock represent the number of real buildings in the U.S. building stock that a ResStock model represents. Each ResStock dataset release has a different weighting factor for the building models. As seen in [this paper](https://www.nlr.gov/docs/fy22osti/80889.pdf), our model or sample weights are constructed using U.S. EIA 2009 RECS microdata. Use the weights by multiplying the column of interest by the weight. Some results columns already have the weight applied. These have the word “weighted” in the name.

### What building types does ResStock model?

ResStock models most types of housing including single-family, multifamily, and manufactured or mobile homes. See [this explanation](docs/resources/explanations/Building_Types.md) for more detail on what is not modeled.

### How many profiles or models should be used, and how does the number used affect uncertainty of results?

We recommend estimating the standard error using the standard deviation divided by the square root of the number of samples (i.e. profiles or models) and using the results to inform the appropriate minimum sample size for a particular analysis. As a conservative reference, using at least 1,000 samples  will maintain 15% or lower sampling discrepancy for many common quantities of interest, as described in the [End-Use Load Profiles methodology report section 5.1.3](https://docs.nlr.gov/docs/fy22osti/80889.pdf).

See [this explanation](docs/resources/explanations/Number_of_samples.md) which has more details and also points to other ResStock references about how to increase the number of samples and calculate the uncertainty.

### Are these load profiles measured or simulated?

The profiles are simulated using the ResStock and ComStock modeling tools, which have been validated and informed by the best available data against an array of empirical datasets. ResStock and ComStock use the EnergyPlus simulation engine. The validation results and uncertainty for quantities of interest are presented in the [End-Use Load Profiles final report](https://docs.nlr.gov/docs/fy22osti/80889.pdf).

ResStock generally simulates 550,000 individual building energy models, and ComStock simulates 150,000 building energy models.

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

## Data Viewer

### What is the Data Viewer?

The Data Viewer is a web-based visualization platform that takes data directly from our data hosting platform, the OEDI data lake.

The Data Viewer can show timeseries data or data aggregations in a web browser. More information can be found in the Web-Based Visualization Platform of the [ResStock technical reference documentation](assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf).

The link to the Data Viewer depends on the dataset, and other factors. View the [Data page](docs/data.md) for links to the Data Viewer specific to each dataset release.

### In the Data Viewer, what does "sum" or "average" mean?

The 'sum' aggregation is the total energy consumption for all buildings that meet the filter criteria across all the occurrences of the given time step within the selected month(s). For example, in a day timeseries range for a specific state for the month of July, the 7-7:15 AM hour time step shows the sum of all energy consumption statewide between 7-7:15 AM in July, from buildings that meet the filter criteria. The ‘sum’ view has fewer uses than the ‘average’ view. The 'average' aggregation is the total energy consumption for all buildings that meet the filter criteria, averaged across all the occurrences of the given time step within the selected month(s).

For example, in a day timeseries range for a specific state for the month of July, the 7-7:15 AM hour time step shows the average statewide energy consumption between 7-7:15 AM in July, from buildings that meet the filter criteria. The ‘average’ aggregation provides a view of the average day of total energy consumption in the state. This is the more logical view for most use cases. Note that while each time step within a day or a year has the same number of occurrences within each dataset, each time step for a week does not - some days of the week occur more times than others in each year or month range (except for February).

### In the Data Viewer, how are the peak day and min peak day defined?

The peak day is the day with the highest single-hour (peak) energy consumption within the selected months.

The min peak day is the day with the lowest single-hour energy consumption within the selected months.

### In the Data Viewer, why is the time series data slow to load after I click the update button?

We query data in real time to produce the time series graphs you see on the webpage, and this can involve scanning terabytes (TB) of data. Running a baseline-only query for California, Texas, New York, or Illinois takes around a minute, while running a query for a state like Colorado or Massachusetts takes about 10-20 seconds. However, if the graphs have previously been generated we have the data cached and can typically load the data in a few seconds. That's why the load time varies.

### In the Data Viewer, why can't I click on the "Explore Timeseries" button?

The “Explore Timeseries” option is available once a specific geography (e.g. state or PUMA region) is selected.

### In the Data Viewer, how do I see a profile for just one, or just a few, end uses?

Clicking on the end uses in the legend will highlight the end use in the visualization.

### In the Data Viewer, how can I access a specific day of time series data?

Choose “Export csv” and “15 minute resolution”. The resulting csv file will have 15 minute end use load profiles that are not aggregated over time.

### In the Data Viewer, can I aggregate over multiple locations?

The viewer allows aggregations of up to six locations (states or PUMAs, depending on the dataset). When viewing a single location, choose the “+ More Locations” option, add up to five additional locations, and choose “Update Search”. Additionally, the "+ Filter" button enables aggregations of an unlimited number of locations, including by PUMA and county. This button also allows users to filter the data by characteristics, such as vintage, floor area, and building type.

Additionally, sums of more than six locations can be created manually by downloading sums of up to six locations and summing further on your local computer.

TMY3 weather is not aligned between locations. This does not affect our recommendations for working with annual data. However, if your application requires timeseries data and therefore would benefit from aligned weather, we recommend either using an AMY dataset, or filtering by weather station and summing only within a single weather station’s PUMAs.

### In the Data Viewer, how can I see the building characteristics associated with an aggregate load profile from the data viewer?

The building characteristics are available on the Open Energy Data Initiative (OEDI) data lake. Visit the [Data page](docs/data.md) for links to the OEDI pages for each dataset.

Depending on your data viewer geography, choose either by_state or national. If you are interested in national building characteristics, choose national, your file type of interest (csv or parquet), and then a file with either baseline or a specific upgrade number in the name. If you are interested in state specific results, choose by_state, then pick the state, then the file type of interest (csv or parquet), and then a file with either baseline or a specific upgrade number in the name.

Once the data is downloaded and open, apply the same filters that were used in the Data Viewer.

## Analysis

### Can I run ComStock and ResStock myself?

The code required to run ComStock and ResStock is available on our public GitHub repositories: [https://github.com/NatLabRockies/ComStock](https://github.com/NatLabRockies/ComStock) ; [https://github.com/NatLabRockies/ResStock](https://github.com/NatLabRockies/ResStock). Other related code repositories are provided on the For Developers page for [ComStock](https://natlabrockies.github.io/ComStock.github.io/docs/for_developers/for_developers.html) and [ResStock](docs/developers.md).

While these resources are available, ComStock and ResStock are complex modeling tools and there is no documentation for running the model other than what exists in the codebase, and we are not able to support running the models at this time. We generally do not recommend running the model unless you have a deep understanding of the methodology and objectives. Please email us at [ComStock@nlr.gov](mailto:ComStock@nlr.gov) or [ResStock@nlr.gov](mailto:ResStock@nlr.gov)  if you have suggestions for improvements or specific needs.

### I am interested in an upgrade measure combination that is not currently available as an upgrade package in the public datasets. Can I combine results from the individual measures?

Our general guidance is to NOT combine measure results. There are interactions between most upgrade measures that affect the amount of savings and make results of multiple measures together misleading.

See an explanation and examples on this topic, for [ComStock](https://natlabrockies.github.io/ComStock.github.io/docs/resources/explanations/combining_measure_results.html) and [ResStock](docs/resources/explanations/Individual_Measures_Not_Combined.md).

Please email us at [ComStock@nlr.gov](mailto:ComStock@nlr.gov) or [ResStock@nlr.gov](mailto:ResStock@nlr.gov) if you have questions about combining specific measures.

### I want to analyze only part of a package, not the whole package. Can I compare samples that did not get this part of the upgrade, with samples that got the full upgrade to analyze the impact?

Yes you can, but there are a few caveats to be aware of. For example, if looking at one envelope package that includes air sealing, insulation, and duct sealing, downselecting to models without the wall insulation measure applied is creating a biased sample, since the package applies wall insulation only to uninsulated wood stud walls. Using this method, you are removing some of the poorest performing buildings. Take a look at the samples to see how many samples you would be removing with this approach, and then consider if it is reasonable.

### How do I calculate COP?

The as-simulated heating COP can be determined by calculating the heating delivered divided by the energy consumed for heating. Because ResStock outputs these values with different units, a unit conversion is also required.

For example, the COP of an all-electric heating system can be calculated as (out.load.heating.energy_delivered.kbtu * (293.07 / 1000)) / (out.electricity.heating.energy_consumption.kwh + out.electricity.heating_fans_pumps.energy_consumption.kwh + out.electricity.heating_hp_bkup.energy_consumption.kwh + out.electricity.heating_hp_bkup_fa.energy_consumption.kwh)

This can be calculated using the timeseries results to get the COP at an individual timestep, or using totals for the year from the metadata_and_annual files to get an annual average value.

Heating systems that use additional fuels in addition to electricity will require additional fields to be included in the denominator. E.g. out.natural_gas.heating.energy_consumption.kwh

## Modeling Methods, Assumptions, and Documentation

### Where can I find information about input data sources, modeling methodology, and assumptions?

ResStock reference documentation is available in the Published Datasets section of the [Data page](docs/data.md). This includes baseline and upgrade measure information. We generally publish an updated version with every dataset release.

Upgrade measure documentation is also available on the [Data page.](docs/data.md)

### Where is there documentation on what technologies are available in the upgrade measures?

The [Data page](docs/data.md) links to each dataset and the dataset technical documentation which covers the technologies and upgrades that are available.

### Does ResStock model rooftop solar PV?

Yes, ResStock does model rooftop solar PV. See more details on rooftop PV, assumptions, and limitations on [this explanation](docs/resources/explanations/PV_System_Assignment_and_Distributions.md).We recommend using [PVWatts](https://pvwatts.nlr.gov/) or [ReOPT](https://www.nlr.gov/reopt) to evaluate PV for a more comprehensive analysis.

### Are there electric vehicle (EV) charging profiles in the dataset?

Yes, there are EV profiles starting in the ResStock 2025 Release 1 dataset. See the [report](https://docs.nlr.gov/docs/fy25osti/93766.pdf) for more information.

### How are leap years modeled?

ResStock results using leap year weather are generated using weather files that contain 8784 hours.

Starting in ResStock 2025 Release 1, ResStock datasets are all 365 days. For datasets generated using leap year weather (i.e., AMY 2012), the dataset starts on January 1, includes February 29, and ends on December 30 instead of December 31. However, data from December 31 simulations are used when converting data into Eastern Standard Time for publication. Please see *What is the timezone of timestamps?* FAQ for more information.

In previous datasets that include results generated using leap year weather (AMY2012 in ResStock 2021 Release 1 and ResStock 2022 Release 1), ResStock datasets span 366 days or 8784 hours. Here is the relevant [OS-HPXML documentation](https://openstudio-hpxml.readthedocs.io/en/latest/workflow_inputs.html#id4).

### Are costs modeled?

ResStock models the cost of running the equipment, or the cost impact on the utility bill. None of the ResStock datasets include the first costs (also called upgrade or measure costs).

See the [ResStock technical reference documentation](assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf) for more information on how utility bills are calculated for the most recent release. Utility bill calculation methods may differ between releases.

### Does ResStock model water heaters in one location, or can the location vary?

The location can vary. They could be located in the attic, mechanical room, crawlspace, garage, basement, living area, outside, or in an unheated basement. More information can be found in the [ResStock technical reference documentation](assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf). Before the 2024 Release 2, we generally used this logic: in cold climates, the water heater was in the basement if there was one, living space otherwise. For hot climates, it'd be the garage if there was one, living space otherwise.

### Does ResStock consider duct sizing impacts with any HVAC upgrades?

When retrofitting a home with a heat pump, sometimes duct size needs to change because of a higher flow rate and a lower supply temperature. ResStock assumes that the duct size increases in all datasets up to and including the 2024 Release 2 dataset. However, this may not be done in practice.

### Partial air conditioning is being referenced from RECS 2009. Why has this not been updated?

We have not found a more recent dataset with the necessary data resolution. This includes RECS 2015 and RECS 2020. The dependencies of this characteristic’s distribution, such as cooling type, use more recent data, so the final distributions of partial air conditioning does not match RECS 2009 even though this is the data source.

### The lighting options available are 100% CFL or 100% of one lighting type. This is unlikely to be the case in buildings. How can I explain this to our clients?

This is a limitation of ResStock, we are not able to do a mixed lighting scenario because there are data limitations in RECS 2015. In reality, some homes may not have 100% of a certain type of lighting. If you are looking at this data, consider our other guidance on the number of samples recommended in order to draw conclusions.

### How are multifamily common areas modeled?

The residential housing units in multifamily buildings are modeled in ResStock and are not in ComStock.  All energy consumption specific to the housing unit is included in the modeled results, such as lighting, appliances, window air conditioners, and HVAC and water heaters that serve a single housing unit.

HVAC and water heating that serves multiple housing units are also included, with energy consumption allocated to the unit served and with adjustment factors applied to account for the energy consumption differences of shared equipment. These adjustment factors are set by OpenStudio-HPXML and from ANSI/RESNET 301.

Electric vehicle charging energy consumption from common areas is also included in ResStock results, allocated directly to the unit that is associated with each electric vehicle.

All other energy that provides services to common areas in multifamily buildings is not included in either ResStock or ComStock. Examples of this would include common area lighting, common laundry facilities, pools, and hot tubs, and elevators.

### How are wall cavity R-values determined?

Wall cavity R-values are determined through one-dimensional heat transfer within OS-HPXML. See [this explanation](docs/resources/explanations/Wood_Stud_Depth.md) for more information.

### What year of U.S. Census geography (e.g., counties, PUMAs) do ComStock and ResStock use?

ComStock and ResStock datasets reflect the 2010 National Historical GIS (NHGIS) GISJOIN standard codes for counties, PUMAs, and Census Tracts. Some model input data sources use 2020 Census geographies, and these are translated to 2010 before being integrated into the ComStock and ResStock workflows. However, 2020 geographic codes are not currently available in the ComStock and ResStock datasets.

For more information about geographic fields and codes used in the models, please refer to the [ComStock](https://natlabrockies.github.io/ComStock.github.io/docs/resources/explanations/reference_geographic_codes.html) and [ResStock](docs/resources/explanations/Geographic_Fields_and_Codes.md) user resources.
