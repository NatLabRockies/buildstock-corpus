<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_ext_window_replacement.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_ext_window_replacement.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_ext_window_replacement.html | corpus_version: fadc83e | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_ext_window_replacement.md | section: Window Replacement | lines: 2-103 -->
# Window Replacement

Authors: Chris CaraDonna and Andrew Parker

#  Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past three years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency, and demand flexibility end-use load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) measures. "Measures" refers to energy efficiency variables that can be applied to buildings during modeling.

An *end-use savings shape* is the difference in energy consumption between a baseline building and a building with an energy efficiency or demand flexibility measure applied. It results in a timeseries profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each timestep.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the [End-Use Load Profiles](https://www.nlr.gov/buildings/end-use-load-profiles.html) project.

This documentation focuses on a single end-use savings shape measure---window replacement. This measure replaces windows in the baseline building stock with windows that have properties aligning with ASHRAE's *Advanced Energy Design Guide* (AEDG). The measure is applicable to all windows in the ComStock baseline that are not triple pane, as these are already very high-performing widows. Altogether, the measure is applicable to over \>99% of the ComStock floor area, representing over 350 million m<sup>2</sup> of window area replaced. Results show \~2% aggregate stock site energy savings (89 TBtu), primarily from heating, cooling, and fan end uses.

# 1.  Introduction

This documentation covers window replacement upgrade methodology and briefly discusses key results. Results can be accessed on the ComStock™ data lake at "[end-use-load-profiles-for-us-building-stock](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F)" or via the Data Viewer at [comstock.nlr.gov](https://comstock.nlr.gov/).

| **Measure Title** | Window Replacement |
| **Measure Definition** | This measure replaces existing windows with new windows that align with the properties proposed in the Advanced Energy Design Guide (AEDG) for each climate zone. |
| **Applicability** | The measure is applicable to all windows with assembly U-values greater than those proposed in the AEDG, and all windows with solar heat gain coefficients (SHGCs) greater than those proposed in the AEDG. This includes most commercial buildings.  |
| **Not Applicable** | The measure is not applicable to windows that already exceed the properties proposed in the AEDG, for each climate zone.  |
| **Release** | 2023 Release 1 |

# 2.  Technology Summary

Many commercial buildings use older window systems \[1\]. These are often single pane, clear glass, and in a minimally insulated aluminum frame. These characteristics create a system with a low insulation value (R-value), which can increase heating and cooling loads, and high solar gains, which can increase cooling loads. Beyond energy considerations, thermal and visual comfort can also be reduced for building occupants.

Newer window systems improve on old designs with features such as the addition of thermal breaking in the frame to increase insulation values, double or triple pane glass to increase insulation values, and coatings to reduce glare and heat gain in the space \[2\]. This measure models the replacement of older, lower-performing windows in the stock with higher-performing windows. The ideal choice of window will vary based on climate zone and perhaps other building characteristics, such as orientation. Generally, colder climates require higher insulation values to reduce space conditioning loads, whereas warmer climates require lower solar heat gain coefficients (SHGCs) to reduce cooling loads and often to improve visual comfort.

# 3.  ComStock Baseline Approach

The ComStock baseline uses a mix of wood-framed and aluminum-framed windows with or without a thermal break. They range from single pane to triple pane, and can be clear/tinted or low-emissivity (low-e). The properties were informed by a variety of data sources, described in the ComStock documentation and shown in Table 1 \[1\].

Table 1. ComStock Baseline Window Properties

| **Number of Panes** | **Glazing Type** | **Frame Material** | **Low-E Coating** | **Assembly U-Factor IP (Btu/h-ft2-F)** | **SHGC** | **VLT*** |
|---|---|---|---|---|---|---|
| Single | Clear | Aluminum | No | 1.178 | 0.744 | 0.754 |
| Single | Tinted/Reflective | Aluminum | No | 1.178 | 0.579 | 0.455 |
| Single | Clear | Wood | No | 0.910 | 0.683 | 0.723 |
| Single | Tinted/Reflective | Wood | No | 0.910 | 0.525 | 0.436 |
| Double | Clear | Aluminum | No | 0.746 | 0.646 | 0.671 |
| Double | Tinted/Reflective | Aluminum | No | 0.749 | 0.484 | 0.411 |
| Double | Clear | Aluminum | Yes | 0.559 | 0.386 | 0.591 |
| Double | Clear | Aluminum With Thermal Break | Yes | 0.499 | 0.378 | 0.591 |
| Double | Tinted/Reflective | Aluminum | Yes | 0.557 | 0.274 | 0.359 |
| Double | Tinted/Reflective | Aluminum | Yes | 0.496 | 0.266 | 0.359 |
| Triple | Clear | Aluminum | Yes | 0.300 | 0.328 | 0.527 |
| Triple | Tinted/Reflective | Aluminum | Yes | 0.299 | 0.224 | 0.320 |

\*VLT stands for visible light transmission

Each ComStock model is assigned a window type from Table 1 through a sampling process. Each window type has a probability for which it will be assigned to a model. These probabilities are primarily informed by the National Fenestration Rating Council (NFRC) Commercial Fenestration Market Study, which was conducted by Guidehouse in collaboration with NFRC, with input from various other sources \[1\]. Triple pane windows will not be considered for replacement in this measure because they are already high-performing. An example of the available window options for a model in climate zone 4 for various energy codes is shown in Table 2.

Table 2. Example of Available Window Assignment Options for Climate Zone 4 Based on the Energy Code Followed During the Last Window Replacement

Table from \[1\]

<!-- table recovered from ./media/af2de490-bde0-40ce-b9d9-b48fb43e822e.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_ext_window_replacement.yaml
     method: vision-transcription -->

**Allowable assembly maximums by the energy code followed during the last windows replacement**

| Allowable Assembly Maximum | Pre-1980 | 1980-2004 | 90.1-2004 | 90.1-2007 | 90.1-2010 | 90.1-2013 |
|---|---|---|---|---|---|---|
| U-Value | 1.22 | 0.59 | 0.57 | 0.55 | 0.55 | 0.42 |
| SHGC | 0.54 | 0.36 | 0.39 | 0.4 | 0.4 | 0.4 |

**Window types that meet each code minimum**

| Window Type | Pre-1980 | 1980-2004 | 90.1-2004 | 90.1-2007 | 90.1-2010 | 90.1-2013 |
|---|---|---|---|---|---|---|
| Single - No LowE - Clear - Aluminum U-1.178 SHGC-0.744 | X |  |  |  |  |  |
| Single - No LowE - Tinted/Reflective - Aluminum U-1.178 SHGC-0.579 | X |  |  |  |  |  |
| Single - No LowE - Clear - Wood U-0.91 SHGC-0.683 | X | X |  |  |  |  |
| Single - No LowE - Tinted/Reflective - Wood U-0.91 SHGC-0.525 | X | X |  |  |  |  |
| Double - No LowE - Tinted/Reflective - Aluminum U-0.749 SHGC-0.484 | X | X |  |  |  |  |
| Double - No LowE - Clear - Aluminum U-0.746 SHGC-0.646 | X | X |  |  |  |  |
| Double - LowE - Clear - Aluminum U-0.559 SHGC-0.386 |  | X | X | X | X |  |
| Double - LowE - Tinted/Reflective - Aluminum U-0.557 SHGC-0.274 |  | X | X | X | X |  |
| Double - LowE - Clear - Thermally Broken Aluminum U-0.499 SHGC-0.378 |  |  | X | X | X | X |
| Double - LowE - Tinted/Reflective - Thermally Broken Aluminum U-0.496 SHGC-0.266 |  |  | X | X | X | X |
| Triple - LowE - Clear - Thermally Broken Aluminum U-0.3 SHGC-0.328 |  |  | X | X | X | X |
| Triple - LowE - Tinted/Reflective - Thermally Broken Aluminum U-0.299 SHGC-0.224 |  |  | X | X | X | X |

X = This window type meets code minimums

<br>
<br>

![Chart Description automatically generated](./media/47136bf3-e1c4-4846-82b5-180466f15416.png)

Figure 1*.* Percentage of stock floor area assigned to each window type in the ComStock baseline

# 4.  Modeling Approach

This measure replaces the windows of a model with new windows with thermal and tinting properties that align with the properties specified in the AEDG. The measure will first identify the existing window properties for each ComStock baseline model. In cases where the U-value (thermal transmittance) and SHGC underperform those specified in the AEDG, the windows will be replaced with AEDG-compliant windows.

