<!-- comstock comstock_amy2018_2025_release_3 | github_site | docs/resources/explanations/aggregate_file_discrepancy_known_issue.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/resources/explanations/aggregate_file_discrepancy_known_issue.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/resources/explanations/aggregate_file_discrepancy_known_issue.html | corpus_version: 43ae2d4 | corpus_path: github_site/docs/resources/explanations/aggregate_file_discrepancy_known_issue.md | section: Details | lines: 9-26 -->
## Details
In ComStock 2024 Release 2, the "metadata_and_annual_results_aggregates" files hosted on the Open Energy Data Initiative (OEDI) data lake are impacted by a known consistency issue. Specifically, the sum of the aggregated metadata and results files at different geographic levels—such as county and state—to a national level may produce slightly different totals. For example, summing energy consumption results in the county-level aggregate files for all counties in the U.S. yields national totals that differ by up to &plusmn;5% from those in the state-level aggregate files.

This discrepancy stems from a minor error during the process in which we generate a sample weight table to appropriately weight and reallocate the ComStock samples based on the stock truth data (see the [New ComStock Sampling Method](docs/resources/explanations/new_sampling_method.md) explanation and [ComStock reference documentation](https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2024_2.pdf) for details). In 2024 Release 2, this weight table was generated using a non-deterministic method, meaning that it can produce slightly different—but still valid—results when rerun. Some of the “metadata_and_annual_results_aggregates” files were unintentionally generated using a different version of this weight table, resulting in small inconsistencies between geographic aggregations.

The following groups of geographies in the “metadata_and_annual_results_aggregates” directory used the same weight table and therefore have identical results:

**Group A**
-	by_state_and_county
-	by_state_and_puma

**Group B**
-	by_state
-	national

The results in the aggregate files in Group A also match the raw, tract-level results in the “metadata_and_annual_results” directory. Neither group of files are considered more “correct” than the other. The difference in total, national energy consumption between the two groups is 2%. The total floor area between the two groups is identical because the weighting and reallocation process matches the total floor area in the stock truth data.

The issue will be addressed in the next dataset release.
