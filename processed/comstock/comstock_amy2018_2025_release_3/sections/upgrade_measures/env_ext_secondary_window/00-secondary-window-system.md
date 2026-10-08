<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_ext_secondary_window.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_ext_secondary_window.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_ext_secondary_window.html | corpus_version: b5faf42 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_ext_secondary_window.md | section: Secondary Window System | lines: 2-49 -->
# Secondary Window System

Authors: Andrew Parker and Amy LeBar

# Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past three years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency and demand flexibility end-use load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) measures. "Measures" refers to energy efficiency variables that can be applied to buildings during modeling.

An *end-use savings shape* is the difference in energy consumption between a baseline building and a building with an energy efficiency or demand flexibility measure applied. It results in a timeseries profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each timestep.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the [End-Use Load Profiles](https://www.nlr.gov/buildings/end-use-load-profiles.html) project.

This documentation focuses on a single end-use savings shape measure---secondary window systems. This measure adds secondary windows to the inside of existing windows, decreasing the U-value, solar heat gain coefficient (SHGC), and visual light transmittance (VLT) by a specified amount. The measure is applicable to all windows in the ComStock baseline that are not triple pane, as these are already very high-performing windows. Altogether, the measure is applicable to over \>99% of the ComStock floor area, representing over 350 million m<sup>2</sup> of window area replaced. Results show \~1% aggregate stock site energy savings (60 TBtu), primarily from heating, cooling, and fan end uses.

# Acknowledgments

The authors would like to acknowledge the valuable guidance and input provided by the Lawrence Berkeley National Laboratory WINDOW software team.

# 1.  Introduction

This documentation covers secondary window systems upgrade methodology and briefly discusses key results. Results can be accessed on the ComStock data lake "[end-use-load-profiles-for-us-building-stock](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F)" or via the Data Viewer at [comstock.nlr.gov](https://comstock.nlr.gov).

| **Measure Title**  | Secondary Window System                                                                                                            |
| **Measure Definition** | This measure adds secondary windows to the inside of existing windows, decreasing the U-value, SHGC, and VLT by a specified amount. |
| **Applicability**      | The measure is applicable to all single- and double-pane windows.                                                                   |
| **Not Applicable**     | The measure is not applicable to triple-pane windows.                                                                               |
| **Release**            | EUSS 2023 Release 1                                                                                                                 |

# 2.  Technology Summary

Secondary windows, also referred to as interior windows, storm windows, glazing retrofit systems, and by various manufacturer-specific names, are "retrofit products that enhance the performance of an existing window without a full replacement or reglazing. They can be added to existing windows with poor energy performance to mitigate air infiltration, energy loss, or unwanted solar gain, while also offering non-energy benefits to building occupants, thereby offering a lower cost alternative to window replacement." \[1\]

There are roughly 20 manufacturers who advertise secondary windows for commercial applications in the United States \[1\]. Manufacturer terminology varies, but a review of the publicly available information from all 20 manufacturers shows that the products come in several general configurations:

-   **Frame-within-frame or reveal** are windows with aluminum or vinyl frames that are attached to the existing window frame, with either exterior or interior (most common) application. In some cases, such as where the existing window frame is too shallow, the secondary window may be installed in the existing window reveal instead of inside the frame. Glass may be glass or acrylic, single- or double-pane, may have various coatings and gas fills (for double-pane), and may or may not have a thermal break in the frame. Secondary frames may be permanently attached or removable. This configuration has the most manufacturers.

-   **Glued to existing glass** are systems where the secondary glass is attached to spacers that are glued to the existing glass. They may have various coatings, and some products are designed for interior application while others are designed for exterior application. This approach appears to generally be targeted toward curtainwall applications, which are found on many newer buildings with a high window-to-wall ratio.

-   **Attached to existing frame** are systems where the secondary glass is in a thin frame that is attached to the existing window frame with glue or mechanical fasteners. Either exterior or interior (most common) application are possible. Glass may be glass or acrylic with various coatings.

These configurations are illustrated in Figure 1. One important note about this technology is that with most of the installation configurations, any thermal bridge through the existing frame is still present after installation. An exception is the frame-within-reveal configuration, which may include an air gap or spacer between the secondary and existing window frame. The most common configurations across manufacturers appear to be the frame-within-frame and frame-within-reveal configurations, which can often be covered by the same product.

![Diagram Description automatically generated](./media/f489d707-a0d4-469f-b91d-6dcf7235fc59.png)

Figure 1. Secondary window system types

