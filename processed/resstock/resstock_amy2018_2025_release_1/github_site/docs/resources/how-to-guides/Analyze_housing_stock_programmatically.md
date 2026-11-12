<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/how-to-guides/Analyze_housing_stock_programmatically.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/how-to-guides/Analyze_housing_stock_programmatically.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/how-to-guides/Analyze_housing_stock_programmatically.html | corpus_version: resstock_amy2018_2025_release_1-v1 -->
# Analyze Housing Stock Programmatically

# How To: Analyze Housing Stock Programmatically

These example notebooks and scripts demonstrate how users can access the ResStock datasets programmatically using the ResStock 2025 Release 1 dataset.Some dataset attributes, like column names or weighting factor applications, may change in the future. Check out the [Data page](docs/data.md) for the most up to date information on ResStock datasets.

## AWS Athena and SQL Queries

These scripts address three questions using SQL.

- [Example AWS Athena Queries](docs/resources/how-to-guides/aws_athena_queries.md).

## Python

### Jupyter Notebook

Download the below Jupyter notebooks for the formatting to properly render. Previewing the notebooks online can present unreadable formatting.

- [Download Annual Baseline and Upgrade Data](docs/resources/how-to-guides/access_annual_data_programmatically.ipynb) Example Jupyter notebook for pulling annual baseline and upgrade results from the Open Energy Data Initiative (OEDI) data lake. This example filters to a specific geography and housing type, and then plots a comparison.
- [Download Timeseries Baseline and Upgrade Data](docs/resources/how-to-guides/access_timeseries_data_programmatically.ipynb) Example Jupyter notebook for pulling timeseries aggregate files from the OEDI data lake for a certain geography and housing type, and then plots a comparison.
