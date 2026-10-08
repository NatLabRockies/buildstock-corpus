<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_ext_secondary_window.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_ext_secondary_window.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_ext_secondary_window.html | corpus_version: b5faf42 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_ext_secondary_window.md | section: 3.1  Window Construction Type | lines: 68-178 -->
## 3.1  Window Construction Type

Data from the National Fenestration Rating Council (NFRC) Commercial Fenestration Market Study was used to develop the modeling approach for windows in ComStock. This study, conducted by Guidehouse in collaboration with NFRC, characterized the national commercial window stock through data collection and analysis. Six primary data sources representing all regions of the United States were used in the study---a 2020 Guidehouse survey, Northwest Energy Efficiency Alliance (NEEA) commercial building stock assessment (CBSA), DOE Code Study, California End Use Survey (CAEUS), Commercial Buildings Energy Consumption Survey (CBECS), and Residential Energy Consumption Survey (RECS). A variety of window properties were collected, including the window-to-wall ratio, number of panes, frame material, glazing type, low-E coating, gas fill, SHGC, U-factor, and many others. In total, the database contained approximately 16,000 samples, each with an appropriate weighting factor based on the coverage, completeness, and fidelity of each data source. The window-to-wall ratio data was already incorporated into the ComStock baseline during the End-Use Load Profiles project. Some of the other key window properties, such as thermal performance, were then used to create the new baseline window constructions and distributions discussed later in this section. A summary of the data sources and their associated information is shown in Table 2.

Table 2. Window Property Data Sources

<!-- table recovered from ./media/50c87ca1-cdd0-4a78-abec-9ca69ee5fa0f.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_ext_secondary_window.yaml
     method: vision-transcription -->

| Source | Data Collection Year | Samples | Regions | Window Area | Panes | Glazing Type | Frame/Thermal Break | Low-E Coating | Retrofit/New | Window Vintage | U-Factor/SHGC | Gas Fill |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Guidehouse Survey | 2020 | 800 | National | P | P | P | P | P | P | P | P | P |
| NEEA CBSA | 2014, 2018 | 1,996 | WA, OR, MT, ID | P | P | P | P | P | P | P | P |  |
| DOE Code Study | 2016–2019 | 104 | FL, IA, IL, NE | P | P | P | P | P |  |  | P |  |
| CAEUS | 2006 | 5,862 | California |  | P | P | P | P |  |  |  |  |
| EIA CBECS | 2012 | 6,721 | National |  | P | P |  |  | P |  |  |  |
| EIA RECS | 2015 | 858 | National (Multifamily) | P | P |  | P | P |  |  |  |  |
| Programs | 2020 | 30 | TX, CO, WA | P | P |  | P |  | P |  | P |  |
| Other | 2019 | 6 | WA, TN | P | P | P | P | P |  |  |  | P |
| AAMA | 2017 | Summary Level | National (Sales) | P | P | P | P | P | P |  |  |  |
| Manufacturer Data | 2019 | 3,000+ | National (Sales) |  | P | P | P | P | P |  |  |  |
| Guidehouse Market Size Estimates | 2020 | Summary Level | National |  |  |  |  |  |  |  |  |  |

P = Present in Data Source

![A picture containing table Description automatically generated](./media/c1dbe272-0b99-4cab-993a-a044485ea2b6.png)

Figure 2. Window characteristics

Four window properties---number of panes, glazing type, frame material, and low-E coating---were used to create the baseline window configurations. These four parameters were selected based on which characteristics have the most impact on window performance, which have the most data available from the various data sources, and which inputs we trust from the average building owner or survey recipient. The options for each property are shown in Figure 2.

Modeling every combination of these four properties would result in 36 different window configurations, which would add significant complexity to the sampling process. Instead, we selected 12 combinations to be modeled, based on which combinations are most common and most realistic. There are four single-pane, six double-pane, and two triple-pane configurations. The unrealistic/uncommon combinations that were eliminated include:

-   Single pane with thermally broken aluminum frame

-   Single pane with low-E coating

-   Double pane with wood frame

-   Triple pane with no low-E coating

-   Triple pane without thermally broken aluminum frame

-   Thermally broken double or triple pane without low-E coating.

The 12 remaining window configurations are shown in Table 3.

Table 3. Window Configurations

| **Number of Panes** | **Glazing Type**  | **Frame Material**          | **Low-E Coating** |
|---------------------|-------------------|-----------------------------|-------------------|
| Single              | Clear             | Aluminum                    | No                |
| Single              | Tinted/Reflective | Aluminum                    | No                |
| Single              | Clear             | Wood                        | No                |
| Single              | Tinted/Reflective | Wood                        | No                |
| Double              | Clear             | Aluminum                    | No                |
| Double              | Tinted/Reflective | Aluminum                    | No                |
| Double              | Clear             | Aluminum                    | Yes               |
| Double              | Clear             | Aluminum With Thermal Break | Yes               |
| Double              | Tinted/Reflective | Aluminum                    | Yes               |
| Double              | Tinted/Reflective | Aluminum With Thermal Break | Yes               |
| Triple              | Clear             | Aluminum With Thermal Break | Yes               |
| Triple              | Tinted/Reflective | Aluminum With Thermal Break | Yes               |

We created a sampling distribution for the new window constructions for the entire country using the initial data set. Overall, single-pane windows make up approximately 54% of the stock, double-pane windows make up 46%, and triple-pane windows make up \<1%. Initially, we created distributions based on census division to incorporate geographic location into the sampling. Upon further analysis, we found that it was also necessary to incorporate the energy codes into distributions to prevent scenarios where a single-pane window was sampled for a certain location, but, according to the energy code for that location, a double-pane window was required. For this reason, we modified the sampling distribution to include two dependencies---climate_zone and energy_code_followed_during_last_window_replacement.

To generate these sampling distributions, we used the maximum U-values specified for each climate zone in each version of ASHRAE 90.1. For each combination of climate zone and energy code, the 12 window configurations were evaluated to determine which were both realistic and met code (i.e., had a U-value lower than the code maximum U-value). For the older energy codes, we made several assumptions about technology adoption to determine which window configurations were realistic:

-   Low-E coating---not adopted until DOE Ref 1980--2004

-   Thermally broken aluminum frame---not adopted until 90.1-2004

-   Triple pane---not adopted until 90.1-2004.

Each combination of climate zone and energy code included 2--12 window configurations that met the criteria. After limiting the distributions to these configurations, we renormalized the percentages from the national distribution to 100%. This kept the percentages from the national distribution while also incorporating intelligent assumptions based on climate zone and energy code. Table 4 provides an example of the window configurations that were sampled for each code year in climate zone 4A.

Table 4. Window Distribution Assumptions Example From Climate Zone 4A

<!-- table recovered from ./media/1225d411-9c12-4555-b633-bcbd69a6bfbd.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_ext_secondary_window.yaml
     method: vision-transcription -->

**Allowable assembly maximums by the energy code followed during the last windows replacement**

| Allowable Assembly Maximum | Pre-1980 | 1980-2004 | 90.1-2004 | 90.1-2007 | 90.1-2010 | 90.1-2013 |
|---|---|---|---|---|---|---|
| U-Value | 1.22 | 0.59 | 0.57 | 0.55 | 0.55 | 0.42 |
| SHGC | 0.54 | 0.36 | 0.39 | 0.4 | 0.4 | 0.4 |

**Window types that meet each code minimum (X = this window type meets code minimums)**

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

As can be seen in Table 4, for DOE Ref Pre-1980, the only windows that met code and are realistic are single-pane or double-pane windows with no low-E coating. For DOE Ref 1980--2004, the maximum U-value dropped significantly, such that single-pane aluminum windows no longer met code. However, double-pane low-E windows became available on the market at that time. For 90.1-2004 through 90.1-2010, code required a U-value equivalent to double-pane low-E or better, and in 90.1-2013, the code improved again, meaning that double-pane low-E with a thermal break or better was required. This type of logic was applied to all combinations of climate zone and energy code. Then, we converted the data into the distributions used in sampling.

A small adjustment was made to the final distributions because some states and localities do not follow or enforce energy codes strictly. Following the code exactly would likely overestimate window performance. Therefore, in scenarios where single-pane windows were technically below code, we assumed that 5% of all windows in the stock would still have the worst-performing single-pane windows installed. The distributions were adjusted accordingly by subtracting 5% total from the double-pane configurations and adding to the single-pane aluminum configurations. After making this manual adjustment, the new distributions had the same overall breakdown as the national distribution generated from the Guidehouse data---54% single-pane and 46% double-pane.

