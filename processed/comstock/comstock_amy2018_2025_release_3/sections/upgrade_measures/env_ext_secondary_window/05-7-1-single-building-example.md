<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_ext_secondary_window.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_ext_secondary_window.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_ext_secondary_window.html | corpus_version: b5faf42 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_ext_secondary_window.md | section: 7.1  Single Building Example | lines: 424-446 -->
## 7.1  Single Building Example

The percent changes in U-value, SHGC, and VLT were determined from the WINDOW model and assigned to each building in ComStock based on the existing window construction and the climate zone. Table 10 shows the U-value and SHGCs for each window configuration before and after the secondary window upgrade was applied. As expected, the U-value and SHGC percent decreases align with the performance changes in Table 7. VLT is not currently an output variable, but we assume that the VLT decrease was also applied properly because it was applied in the exact same manner as the U-value and SHGC performance changes.

Table 10. U-Value and SHGC Comparison Before and After the Measure Was Applied

<!-- table recovered from ./media/e4cd0292-c3cc-4911-b1dd-de678a3b9970.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_ext_secondary_window.yaml
     method: vision-transcription -->

| Build Existing Model.Baseline Window Type | U-Value Before (SI) | SHGC Before | U-Value After (SI) | SHGC After | U-Value % Decrease | SHGC % Decrease |
|---|---|---|---|---|---|---|
| Single - No LowE - Clear - Aluminum | 5.724 | 0.744 | 2.992 | 0.541 | 0.477 | 0.273 |
| Single - No LowE - Tinted/Reflective - Aluminum | 5.724 | 0.579 | 2.992 | 0.422 | 0.477 | 0.271 |
| Single - No LowE - Tinted/Reflective - Wood | 5.164 | 0.525 | 2.099 | 0.373 | 0.594 | 0.290 |
| Single - No LowE - Clear - Wood | 5.164 | 0.683 | 2.099 | 0.486 | 0.594 | 0.288 |
| Double - No LowE - Tinted/Reflective - Aluminum | 4.256 | 0.488 | 3.466 | 0.417 | 0.186 | 0.145 |
| Double - No LowE - Clear - Aluminum | 4.239 | 0.650 | 3.457 | 0.538 | 0.184 | 0.172 |
| Double - LowE - Clear - Aluminum | 3.178 | 0.381 | 2.870 | 0.344 | 0.097 | 0.097 |
| Double - LowE - Tinted/Reflective - Aluminum | 3.167 | 0.271 | 2.863 | 0.254 | 0.096 | 0.063 |
| Double - LowE - Clear - Thermally Broken Aluminum | 2.837 | 0.373 | 2.529 | 0.339 | 0.109 | 0.091 |
| Double - LowE - Tinted/Reflective - Thermally Broken Aluminum | 2.820 | 0.265 | 2.520 | 0.246 | 0.106 | 0.072 |

