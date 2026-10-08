<!-- comstock comstock_amy2018_2025_release_3 | github_site | docs/resources/explanations/2025_release_2_packages_known_issue.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/resources/explanations/2025_release_2_packages_known_issue.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/resources/explanations/2025_release_2_packages_known_issue.html | corpus_version: b5faf42 | corpus_path: github_site/docs/resources/explanations/2025_release_2_packages_known_issue.md | section: Details | lines: 12-40 -->
## Details
A known issue in ComStock 2025 Release 2 (both 2012 and 2018 Weather) affects the following upgrade packages:

| Measure ID    | Package Name                                                                                          | Incorrect Upgrade ID  | Correct Upgrade ID    |
|:--------------|:------------------------------------------------------------------------------------------------------|:----------------------|:----------------------|
| pkg_0006      | Package 9, Hydronic GHP or Packaged GHP or Console GHP                                                | 58                    | 55                    |
| pkg_0009      | Package 6, Demand Flexibility, Lighting + Thermostat Control, Load Shed for Daily Bldg Peak Reduction | 55                    | 58                    |

The results for these two packages were mislabeled, with the data labeled as pkg_0006 actually reflecting the results of applying pkg_0009 to the building stock, and vice versa. The following sections summarize the impacts on the Open Energy Data Initiative (OEDI) files and Data Viewer for these two dataset releases.

### OEDI Impacts
The `upgrades_lookup.json` and `measure_name_crosswalk.csv` files have been corrected and now reflect that pkg_0006 data is found under Upgrade ID 55 and pkg_0009 results under 58. However, the incorrect names are still present in the metadata and annual results files on OEDI. In the files in the OEDI directories, below, the column "in.upgrade_name" for files under Upgrade ID 55 contains "Package 6, Demand Flexibility, Lighting + Thermostat Control, Load Shed for Daily Bldg Peak Reduction," and for Upgrade ID 58, the column contains "Package 9, Hydronic GHP or Packaged GHP or Console GHP." These labels are **INCORRECT** and should not be used to identify the upgrade package applied to the building stock in these files.

OEDI directories affected
- metadata_and_annual_results
- metadata_and_annual_results_aggregates

### Data Viewer Impacts

![](../../../assets/images/2025_2_known_issue.png)

In the dropdown to select which upgrade scenario you are viewing (shown above), selecting “Package 6, Demand Flexibility, Lighting + Thermostat Control, Load Shed for Daily Bldg Peak Reduction” will display the results from applying pkg_0006, and “Package 9, Hydronic GHP or Packaged GHP or Console GHP” will show results from pkg_0009.
All Data Viewer views (listed below) are impacted for both 2012 and 2018 weather releases.
- by_state
- by_puma_northeast
- by_puma_midwest
- by_puma_south
- by_puma_west

