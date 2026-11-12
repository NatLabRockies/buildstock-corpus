<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/FAQ.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/FAQ.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/FAQ.html | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: github_site/docs/FAQ.md | section: Data Viewer | lines: 143-196 -->
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

