<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/6_PublicDataAccess.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/6_PublicDataAccess.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/6_PublicDataAccess.md | section: Web-Based Visualization Platform | lines: 30-67 -->
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

