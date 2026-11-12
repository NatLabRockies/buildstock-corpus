<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/6_PublicDataAccess.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/6_PublicDataAccess.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/6_PublicDataAccess.md | section: Open Energy Data Initiative | lines: 6-29 -->
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

