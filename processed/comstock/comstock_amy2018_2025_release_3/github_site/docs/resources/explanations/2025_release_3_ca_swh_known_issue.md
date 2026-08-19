<!-- comstock comstock_amy2018_2025_release_3 | github_site | docs/resources/explanations/2025_release_3_ca_swh_known_issue.md -->
# California Service Water Heating in ComStock 2025 Release 3

# Issue Report: California Service Water Heating in ComStock 2025 Release 3

## Summary of Issue
In ComStock 2025 Release 3, service water heating (SWH) was not modeled in any California buildings. SWH fields will show zero energy, even when we expect the model to have SWH loads.

## Status
Impacts all models with SWH in the state of California in ComStock 2025 Release 3. We are working to address this issue in future dataset releases.

## Details
Due to a workflow error, SWH in California models was not modeled in ComStock 2025 Release 3. In both the metadata and annual results and timeseries files on the Open Energy Data Initiative (OEDI) data lake and the Data Viewer, SWH fields will show zero energy, even when we expect the model to have SWH loads.

## Recommendations
This issue is likely to have minimal impact on national-scale analyses. However, it may be more consequential for more targeted studies, such as California statewide aggregate analyses. The impact is greatest for analyses focused on energy consumption and energy use intensity (EUI) in building types with high SWH demand, such as hotels and restaurants. For these use cases, we do not recommend using ComStock 2025 Release 3 and instead recommend using the previous release, ComStock 2025 Release 2.
