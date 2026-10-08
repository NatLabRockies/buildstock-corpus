<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_window_film.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_window_film.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_window_film.html | corpus_version: 267e3ea | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_window_film.md | section: Window Film | lines: 2-102 -->
# Window Film

Authors: Janghyun Kim, Chris CaraDonna and Andrew Parker

# Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy’s ResStock™ and ComStock™ models over the past three years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency and demand flexibility end-use load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) measures. “Measures” refers to energy efficiency variables that can be applied to buildings during modeling.

An *end-use savings shape* is the difference in energy consumption between a baseline building and a building with an energy efficiency or demand flexibility measure applied. It results in a timeseries profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each timestep.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the [End-Use Load Profiles](https://www.nlr.gov/buildings/end-use-load-profiles.html) project.

This documentation focuses on a single end-use savings shape measure—window film. The window film studied in this analysis, called solar control film, is a passive retrofit solution for windows that does not involve window replacement. This type of film is composed of transparent, tinted, or metalized laminated polyester layers and can be attached to an existing window surface (either on the exterior or interior side of the window). The properties of the window film are designed to shift the thermal and optical performances of the overall glazing system in order to serve various needs the customer would have (e.g., heat, glare).

While the practical goal of purchasing and installing a window film varies widely in the real market, this study only focuses on the goal of energy savings. Other important aspects that customers typically consider include visual comfort, privacy, aesthetics, ultraviolet protection, etc. Thus, in practice, customers often choose a window film product not only to save energy (or cost) but also to mitigate issues around glare, excessive light, daytime privacy, or inconsistent appearance of the building.

Window film products that were modeled in this analysis significantly reduced the solar heat gain coefficient of the overall glazing system, resulting in better energy savings for buildings in hot climate regions. However, significantly reducing the solar heat gain coefficient that can block unfavorable heat during the summer can actually harm blocking favorable heat during the winter. By applying window films on a stock of buildings covering various load and weather conditions, this analysis highlights when (e.g., time of day) and where (e.g., geospacial location) we can save energy with window films.

# Acknowledgments

The authors would like to acknowledge the valuable guidance and input provided by Shanti Pless at NLR and Jennifer Daly at 3M.

# 1.  Introduction

This documentation covers window film upgrade methodology and briefly discusses key results. Results can be accessed on the ComStock data lake “[end-use-load-profiles-for-us-building-stock](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F)” or via the Data Visewer at [comstock.nlr.gov](https://comstock.nlr.gov/).

| **Measure Title**  | Window Film                                                                                                                                                            |
| **Measure Definition** | This measure applies new performance of the overall glazing system reflecting a scenario when an applicable window film is attached to the original (“baseline”) window.   |
| **Applicability**      | Certain window film (based on real products in the market) is paired with (1) baseline window type and (2) climate zone.                                                   |
| **Not Applicable**     | Triple pane windows are considered not applicable for buildings in any climate zone. Double pane windows in buildings in very cold regions are considered not applicable.  |
| **Release**            | EUSS 2023 Release 1                                                                                                                                                        |

# 2.  Technology Summary

Window films, especially solar control films (SCFs), are a passive retrofit solution for windows that does not require a full window replacement. Following is a summary of SCF technology from a 2022 literature review published in *Applied Sciences* [1].

-   SCF—composed of transparent, tinted, or metalized laminated polyester layers—is designed to shift thermal and solar optical properties of the overall glazing system by differently (compared to window without film) reflecting or absorbing part of the incident solar radiation. SCF promotes the improvement of the thermal and luminous performance of building glazing while reducing potential glare and the transmittance of ultraviolet radiation. The manufacturers of window films offer a wide range of performances depending on different use cases (e.g., energy savings, mitigating glare, controlling occupant’s view, protecting privacy).
-   Figure 1 shows different film positions (e.g., Class A to D) with respect to typical insulated glass units (IGUs). While indoor films are more common than outdoor films in the current market, some of the latest outdoor films provide better energy performance when applied on relatively high-performing windows (e.g., double pane low-E), and some of those products are currently being studied in real applications [2].

![Graphical user interface, diagram Description automatically generated](media/02c6603fedbd847b2ee2f48f7878b12e.png)

Figure 1. Different installation positions of window films for (a) single pane, (b) double pane, and (c) triple pane windows

Figure from [1]

-   Types of SCFs can vary, driven by different use cases:
    -   Reflective type
        -   Has reflective properties on both sides
        -   Mitigates high heat, glare, and ultraviolet control
        -   Has a silvery/mirrored look to the glazing when viewed with indoor lighting or outdoor daylight.
    -   Dual-reflective type
        -   Has reflective outside-facing layer with a subtler inside-facing layer
        -   Mitigates significant solar control during the day
        -   Maintains clear outside view at night.
    -   Neutral type
        -   Controls solar gains through the glass
        -   Maintains original appearance of the glazing system.
    -   Low emissivity type
        -   Reduces the thermal transmittance coefficient (U-value) of the glazing system
        -   Increases thermal insulation and heat rejection properties
        -   Suitable for temperate regions.
    -   Spectrally selective type
        -   Offers an excellent heat rejection with a virtually invisible appearance
        -   Blocks specific regions of the solar spectrum associated with solar heat gains
        -   Does not penalize transmittance of daylight through the glazing.
    -   Ceramic type
        -   Offers solar control without a metal layer
        -   Maintains low visible reflectivity and high resistance to corrosion
        -   Suitable for coastal areas.
    -   Safety and protection type
        -   Controls excessive solar heat gains
        -   Increases the resistance of the glass pane to intentional or accidental impacts
        -   Reduces amount and dimension of potential glass fragments
        -   Offers higher resistance to the glass to support shock waves from explosions and/or ballistic attacks.
-   Manufacturers provide standardized data for SCFs through the National Fenestration Rating Council’s guidelines and the International Glazing Database, which can be used for additional analysis such as building energy modeling. Figure 2 shows the number of SCF models in the International Glazing Database (v72.0). Models included in the International Glazing Database can be imported to Lawrence Berkeley National Laboratory’s (LBNL) WINDOW[^1] software for either calculating (1) simplified (center-of-glass) properties (e.g., solar heat gain coefficient, U-value, visual light transmittance) or (2) detailed properties (e.g., varying solar heat gain coefficient by solar angular dependence) that can be also used in EnergyPlus™ for building energy simulations.

[^1]: For more information, see <https://windows.lbl.gov/software/window>.

![](media/dfade3dd9e578a753615d0914e6acc3e.png)

Figure 2. Number and type of SCFs in the International Glazing Database

Figure from [1]

SCF products are available from various manufacturers covering various ranges of thermal (e.g., U-value, SHGC) and optical (e.g., transmittance and reflectance of light) performances as shown in Figure 3. Plots shown in Figure 3 indicate performance (i.e., U-value, SHGC, visual light transmittance, and visual light reflectance) of windows when certain window film (i.e., All Season to Prestige Exterior Series) is applied on four different baseline windows (i.e., clear single pane, tinted single pane, clear double pane, and tinted double pane). Multiple markers in each row represent different models (e.g., Low E 20, Low E 35) in a series (e.g., All Season) with varying tint levels. These window performance calculations were performed by the manufacturer using LBNL’s WINDOW software. As shown in Figure 3, customers can select from a wide range of products based on various needs between thermal goals (e.g., summer heat gain is too high) and visual goals (e.g., glare inside of the building is too much).

![](media/07dbaafddba985c1385ee2be2c2569f7.png)

Figure 3. Performance characteristics and variations of SCFs from 3M

# 3.  ComStock Baseline Approach

The current baseline building stock in ComStock has 12 different window configurations. Figure 4 shows the breakdown of windows by total floor area. In total, single pane windows represent about 53% of the floor area, double pane 47%, and triple pane \<1%. The window film measure is applicable to all buildings that currently have single or double pane windows, which is nearly 100% of the stock. The very small fraction of buildings that already have triple pane windows do not receive this upgrade in our modeling.

![](media/ef66baba09af36d8baff8deeda6ccc10.png)

Figure 4. Floor area portion of different baseline window types across the entire building stock in ComStock

# 4.  Modeling Approach
