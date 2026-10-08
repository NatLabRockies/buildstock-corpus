<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_ext_window_replacement.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_ext_window_replacement.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_ext_window_replacement.html | corpus_version: 267e3ea | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_ext_window_replacement.md | section: 4.3  Limitations and Concerns | lines: 120-138 -->
## 4.3  Limitations and Concerns

Window assembly U-value is often a function of the ratio of frame area to glass area. ComStock currently uses the simple glazing object, which accepts a constant U-value input regardless of window size and therefore does not capture U-value differences with window size. Furthermore, ComStock does not differentiate between punched windows, curtainwall, storefront, etc., which can have different performance characteristics. Neither of these limitations are expected to impact stock-level analysis in a substantial way.

# 5.  Output Variables

Table 5 includes a list of window-related output variables that are calculated in ComStock. These variables are important in terms of understanding the differences between buildings with and without the window measure applied. These output variables can also be used to understand the economics of the upgrade (e.g., return on investment) if cost information (i.e., material, labor, and maintenance costs for technology implementation) is available.

Table 5*.* Window-Related Property Output Variables From ComStock Simulations

| **Variable Name** | **Description** |
|---|---|
| Window to Wall Ratio | Ratio of window area to exterior wall area for the building model. |
| Window Type | Name of window type, as described in Table 1. |
| Average Window SHGC | Average solar heat gain coefficient of all the windows in the building model. |
| Average Window U-Value (Btu/h-ft2-F) | Average thermal conductance of all the windows in the building model. |

# 6.  Results

