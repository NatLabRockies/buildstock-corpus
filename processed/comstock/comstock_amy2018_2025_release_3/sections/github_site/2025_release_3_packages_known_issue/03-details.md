<!-- comstock comstock_amy2018_2025_release_3 | github_site | docs/resources/explanations/2025_release_3_packages_known_issue.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/resources/explanations/2025_release_3_packages_known_issue.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/resources/explanations/2025_release_3_packages_known_issue.html | corpus_version: b5faf42 | corpus_path: github_site/docs/resources/explanations/2025_release_3_packages_known_issue.md | section: Details | lines: 12-43 -->
## Details
A known issue in ComStock 2025 Release 3 affects the following upgrade packages:

| Measure ID    | Upgrade ID | Correct Package Name                                   | Measures Included                                                                    |
|:--------------|:-----------|:-------------------------------------------------------|:-------------------------------------------------------------------------------------|
| pkg_0003      | 56         | Package 3, Package 1 + Package 2                       | Wall Insulation, Roof Insulation, New Windows, LED Lighting, HP-RTU, and ASHP-Boiler |
| pkg_0004      | 57         | Package 4, Package 2 with Standard Performance HP RTU  | LED Lighting, Standard Performance HP-RTU, and ASHP-Boiler                           |

The results for these two packages were mislabeled, with the data labeled as pkg_0003 actually reflecting the results of applying pkg_0004 to the building stock, and vice versa. The following sections summarize the impacts on the Open Energy Data Initiative (OEDI) files and Data Viewer for this dataset release.

Note that the package names within the files on OEDI and the Data Viewer interface cannot be changed and remain incorrect.

### OEDI Impacts
The `upgrades_lookup.json` and `measure_name_crosswalk.csv` files have been corrected and now reflect that that pkg_0003 data is found under Upgrade ID 56 and pkg_0004 results under 57. However, the incorrect names are still present in the metadata and annual results files on OEDI. In the files in the OEDI directories, below, the column “in.upgrade_name” for files under Upgrade ID 56 contains "Package 3, Package 2 with Standard Performance HP RTU," and for Upgrade ID 57, the column contains "Package 4, Package 1 + Package 2." These labels are **INCORRECT** and should not be used to identify the upgrade package applied to the building stock in these files.

OEDI directories affected
- metadata_and_annual_results
- metadata_and_annual_results_aggregates

### Data Viewer Impacts

![](../../../assets/images/2025_3_known_issue.png)

In the dropdown to select which upgrade scenario you are viewing (shown above), selecting "Package 3, Package 2 with Standard Performance HP RTU" will display the results from applying pkg_0004, and "Package 4, Package 1 + Package 2" will show results from pkg_0003.

All Data Viewer views (listed below) are impacted.
- by_state
- by_puma_northeast
- by_puma_midwest
- by_puma_south
- by_puma_west

