<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/6_PublicDataAccess.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/6_PublicDataAccess.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre -->
# Public Data Access

ResStock results are publicly available for multiple weather years (generally 2018 and TMY) and a variety of upgrades in different formats to meet the various needs of decision makers and others who wish to make use of them. Not all runs that have some publicly available results are available in all formats.

## Open Energy Data Initiative

Since 2021, all ResStock data releases have included the publication of results in an Open Energy Data Initiative (OEDI) [data lake](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock). Our output typically includes the following, with minor variations from dataset to dataset:

- The timeseries results aggregated by state, ISO/RTO region, Building America climate zone, and ASHRAE/IECC climate zone, in .csv format

- The individual housing unit sample model timeseries results, in .parquet format

- The baseline ResStock characteristics for each individual housing unit sample model, in both .csv and .parquet formats

- The full-year (annual) results for each housing unit sample model, in both .csv and .parquet formats

- The building energy models used in the run, in either .idf, .osm, or .xml format

- The schedule files for each housing unit sample used in running the models

- Select fields of the weather data (e.g., [2024.2](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2024%2Fresstock_tmy3_release_2%2Fweather%2F)) that is associated with the model run

- Data dictionaries

- Documentation containing details of the ResStock run and upgrade measures.

Results on OEDI include energy consumption for electricity, natural gas, propane, and fuel oil, and are available for the baseline and for each upgrade measure package. In many datasets, results also include some or all of hot water consumption, CO<sub>2</sub> equivalent emissions impacts, utility bill impacts, heating and cooling load, peak energy consumption, cost multipliers, energy savings, zone temperature data, unmet heating and cooling hours, and energy burden. Typically we convert the field names and units from ResStock’s raw outputs before publishing data. We publish all energy consumption in kWh (even for direct on-site use of natural gas, propane, and fuel oil for equal comparison), and emissions in kg CO<sub>2</sub>e.

## Web-Based Visualization Platform

Portions of our datasets are available on a web-based visualization platform suite that pulls data directly from the OEDI data lake. Detailed examples, tutorials, and videos for using the data viewer are [available on the ResStock website](https://nrel.github.io/ResStock.github.io/), but here we provide an overview of the capabilities.

The headline element is the timeseries data viewer, which allows the user to see total aggregated ResStock timeseries results in the browser. Seven data customization options are currently visible in the timeseries data viewer.

1.  *Fuel type*: allows the user to choose which fuel consumption type to show (for example, to choose to view only electricity consumption results).

2.  *Upgrade*: allows the user to choose which measure or measure package to view results from, when looking at a dataset that has measure packages in addition to the baseline data. For example, from the ResStock 2022.1 dataset, a user might choose to view results from the “heat pump water heaters” model upgrade package.

3.  *Timeseries aggregation type*: four options are available.

    - *sum* is the current default. It shows the total energy consumption for all buildings that meet the current filter criteria across all the occurrences of the given time step within the selected month(s). For example, in a day timeseries range for a specific state for the month of July, the 7-7:15 AM time step shows the sum of all energy consumption statewide between 7 and 7:15 AM in July, from buildings that meet the filter criteria. The value in that timestamp would be approximately 1/96th of the total statewide energy consumption in that month in that sector.

    - *average* is the option that has the most uses. It shows the total energy consumption for all buildings that meet the filter criteria, averaged across all the occurrences of the given time step within the selected month(s). For example, in a day timeseries range for a specific state for the month of July, the 7-7:15 AM hour time step shows the average statewide energy consumption between 7 and 7:15 AM in July, from buildings that meet the filter criteria. The *average* aggregation provides a view of the average day of total energy consumption in the state.

    - *peak_day* shows results for the day with the highest single-hour (peak) energy consumption. It is only available when the month constraints are not used.

    - *min_peak_day* shows results for the day with the lowest single-hour energy consumption. It is only available when the month constraints are not used.

4.  *Timeseries range*: three options are available.

    - *day* shows 24 hours of results at a 15-minute time resolution

    - *week* shows 7 days of results at an hourly time resolution

    - *year* shows 365 days of results at a daily time resolution.

5.  *Month constraints*: sets which months of data are included in the view.

6.  *Add Filters*: allows the user to reduce the number of housing unit samples used to generate the results by selecting which characteristic values to include, for each of the 100+ characteristics included in each dataset.

7.  *More Locations*: allows the user to combine multiple locations into one set of results.

The web-based visualization platform functions as a custom aggregation tool as well. Any set of results generated using the “Add Filters” and “More Locations” options can be downloaded using the “export csv—15 minute resolution” option. This means any user can download aggregated results from any subset of the dataset that can be created using these data customization options. For example, a user could download aggregate results for a specific upgrade for single-family detached and single-family attached homes in Maryland, Delaware, and New Jersey that currently have electric heating. Generating these results would otherwise require a user to use their own AWS account or similar big data support service. These results include energy consumption at 15-minute increments in both the baseline and upgrade. They do not include other outputs such as energy bills, emissions, or energy burden.

An end-use annual results viewer and a histogram viewer are also currently available on the data viewer website. A building characteristics viewer was available for several years but has not been supported more recently. All of the information in these portions of the web-based data viewer is also accessible in Excel-friendly format from the OEDI data.

## BuildStock Query

The ResStock team has created the [BuildStockQuery Python library](https://github.com/NREL/buildstock-query/) designed to simplify and streamline the process of querying massive, terabyte-scale datasets generated by ResStock and ComStock. It is available for public use but does require the user to have access to connect their own AWS Athena account to pay for the queries. It offers an Object-Oriented Programming (OOP) interface to the ResStock datasets, allowing users to more easily perform common queries and receive results in pandas DataFrame format, abstracting away the need for complex SQL queries. By initializing a query object with the pertinent Athena database and table names, users can easily specify queries. For example, to extract timeseries electricity for a specific end use for a given state, grouped by building types. More information is available in the [wiki]( https://github.com/NREL/buildstock-query/wiki) as well as a set of [video tutorials on the use of BuildStockQuery](https://www.youtube.com/watch?v=jmmAHsOZAp8&list=PLmIn8Hncs7bEYCZiHaoPSovoBrRGR-tRS&index=8).

## Dashboards

The ResStock team currently hosts a [Tableau Public site](https://public.tableau.com/app/profile/nrel.buildingstock/vizzes) with Tableau dashboards that allow users to interactively view certain portions of results from specific ResStock projects. The two most popular are the *State Level Residential Building Stock and Energy Efficiency & Electrification Packages Analysis* dashboard, which presents state-level full-year results from the 2022.1 data release ((Present et al. 2022)), and the *US Building Typology Segmentation Residential* dashboard, which presents data from the 2022 U.S.  Building Stock Characterization Study by Reyna et al. (2024), which used data from ResStock 2021.1 ((Wilson et al. 2022)).

## Fact Sheets

The only significant data from ResStock made public prior to 2021 is in the [State Fact Sheets](https://resstock.nrel.gov/factsheets/) from 2017, which were published by NREL together with a technical report.

These fact sheets use an early version of ResStock to quantify the energy efficiency potential of the U.S. single-family housing stock. Each state’s fact sheet features the top 10 improvements in total statewide annual consumer utility bill savings with each of their statewide savings potential and average savings per applicable household. The fact sheets also include single values for statewide cost-effective percent energy savings, energy savings, electricity savings, and pollution reduction, and the number of existing jobs in energy efficiency in that state as of 2016. Documentation of the state fact sheets is included in (Wilson et al. 2017).

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-Present2022" class="csl-entry">

Present, E., P. R. White, R. Adhikari, N. Merket, E. Wilson, and A. Fontanini. 2022. *End-Use Savings Shapes Public Dataset Release for Residential Round 1*. <https://www.nrel.gov/buildings/assets/pdfs/euss-resround1-webinar.pdf>.

</div>

<div id="ref-Reyna2022" class="csl-entry">

Reyna, J., E. Wilson, A. Parker, et al. 2024. *<span class="nocase">U.S. Building Stock Characterization Study: A National Typology for Decarbonizing U.S. Buildings</span>*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy24osti/88109.pdf>.

</div>

<div id="ref-Wilson2017" class="csl-entry">

Wilson, Eric, Craig Christensen, Scott Horowitz, et al. 2017. *<span class="nocase">Electric End-Use Energy Efficiency Potential in the U.S. Single-Family Housing Stock</span>*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy17osti/65667.pdf>.

</div>

<div id="ref-Wilson2022" class="csl-entry">

Wilson, Eric, Andrew Parker, Anthony Fontanini, et al. 2022. *<span class="nocase">End-Use Load Profiles for the U.S. Building Stock: Methodology and Results of Model Calibration, Validation, and Uncertainty Quantification</span>*. National Renewable Energy Laboratory (NREL). <https://doi.org/10.2172/1854582>.

</div>

</div>
