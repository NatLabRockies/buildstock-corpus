<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_PV with Roof Insulation.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/2036a73dc9b7a5dccb8b62fe835cdcbc777175fa/assets/files/ComStock%20Measure%20Doc_PV%20with%20Roof%20Insulation.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_PV%20with%20Roof%20Insulation.pdf | corpus_version: comstock_amy2018_2025_release_3-v3 -->
# Photovoltaics With 40% Rooftop Coverage With Roof Insulation

## ComStock Measure Scenario Documentation: Photovoltaics With 40% Rooftop Coverage With Roof Insulation

Chris CaraDonna, Lauren Adams, Marlena Praprost

<!-- decorative image omitted: image_000000 (wordmark; no description by the figure standard) -->
## List of Acronyms

AEDG

Advanced Energy Design Guide

ASHRAE

American Society of Heating, Refrigerating, and Air Conditioning

Engineers

CBECS

Commercial Buildings Energy Consumption Survey

DC and AC

direct current and alternating current

EIA

U.S. Energy Information Administration

HVAC

heating, ventilating, and air conditioning

NLR

National Laboratory of the Rockies

PADD

Petroleum Administration for Defense District

PV

photovoltaics

TBtu

trillion British thermal units

URDB

Utility Rate Database

## Executive Summary

Building on the 3-year End-Use Load Profiles project to calibrate and validate the U.S. Department of Energy's ResStock ™ and ComStock ™ models, this work produces national datasets that enable cities, states, utilities, and other stakeholders to answer a broad range of questions regarding their commercial building stock, such as the mass adoption of rooftop solar photovoltaics (PV) and improved rooftop insulation.

ComStock is a highly granular, bottom-up model that uses various data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The ' baseline ' model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology of the baseline model is discussed in the ComStock Reference Documentation.

The goal of this work is to develop energy efficiency and demand flexibility measures that cover market-ready technologies and study their mass adoption impact on the baseline building stock. 'Measures' refers to various 'what -if' scenarios that can be applied to buildings. The results for the baseline and measure scenario simulations are published in public datasets that provide insights into building stock characteristics, operational behaviors, utility bill impacts, and annual and subhourly energy usage by fuel type and end use.

This report describes the modeling methodology for a single ComStock measure scenario -PV With 40% Rooftop Coverage With Roof Insulation -and briefly introduces key results. The full public dataset can be accessed on the ComStock ™ data lake or via the Data Viewer at comstock.nlr.gov. The public dataset enables users to create custom aggregations of results for their use case (e.g., filter to a specific county or building type).

Key modeling assumptions and technology details are summarized in Table 1.

Table 1. Summary of Key Modeling Specifications

<!-- table recovered from assets/files/ComStock Measure Doc_PV with Roof Insulation.pdf p.3
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_PV with Roof Insulation.yaml
     method: pdf-text-layer (cell text, pages iv-v) + vision (row layout from the page renders)
     supersedes the extractor's own table here (values 6462c26d005b…):
       The table spans the page break between pages iv and v. docling emitted only the three
       rows on page iv and shifted their text: the Technology Description cell stops mid-bullet
       and the Performance Assumptions cell opens with the tail of that bullet, then stops after
       its second bullet. The Applicability and Release rows, and the last two Performance
       Assumptions bullets, fell out of the grid as loose lines below it. This entry restores
       the five-row table as printed; the loose lines are left in place. The table is
       decomposed into three blank-line-separated groups, each repeating the Package Title
       header row, so no single paragraph exceeds the chunker's 1400-character limit. -->

| Package Title: | Photovoltaics With 40% Rooftop Coverage With Roof Insulation |
|---|---|
| Technology Description | • This study investigates the impact of adding 40% rooftop PV coverage to the U.S. commercial building stock and improves rooftop insulation. • The purpose is to couple 40% rooftop PV coverage with improved roof insulation to investigate the combined effect. • Net metering impacts on calculated utility bills are not included in this study. For these metrics, the PV panels simply reduce the electricity demand on the building meter at the time of generation with no resale back to the utility. However, the ComStock public dataset includes excess PV generation, enabling users to estimate these impacts as needed. |

| Package Title: | Photovoltaics With 40% Rooftop Coverage With Roof Insulation |
|---|---|
| Performance Assumptions | • This scenario package combines two existing ComStock measures: PV with 40% rooftop coverage and improved rooftop insulation. See these documents for a more comprehensive overview of assumptions and interpretations. This document highlights some key points. • Panels are modeled as higher performance with 21% rated efficiency, 96% inverter efficiency, 1.10 direct current/alternating current (DC/AC) ratio, 14% system losses, and azimuth/tilt angles that vary by location. • Total panel area is modeled at 40% of the roof area for each model. Total rated PV power for a building is based on the calculated total panel area and the assumed efficiency of 21%. • The roof insulation measure increases the R-value of the existing building to align with the recommended values from the Advanced Energy Design Guide (AEDG) for Small to Medium Office Buildings: 50% Energy Savings [1]. Target R-values range between R-21 and R-38 for climate zones 1-8, respectively. |

| Package Title: | Photovoltaics With 40% Rooftop Coverage With Roof Insulation |
|---|---|
| Applicability | • The addition of 40% rooftop coverage is applied to all ComStock models. • The rooftop insulation measure is applied only to models where the existing roof insulation is less than the values recommended in the Advanced Energy Design Guide. |
| Release | • 2025 Release 2: 2025/comstock_amy2018_release_2/ |

<!-- text repaired by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_PV with Roof Insulation.yaml
     docling promoted the Applicability row label of Table 1, which fell out of the grid at
     the page break, to a level-2 heading. The chunker is heading-aware, so the rest of the
     executive summary (Tables 2 and 3) was filed under a section named "Applicability". -->

Applicability

Release

- Total panel area is modeled at 40% of the roof area for each model. Total rated PV power for a building is based on the calculated total panel area and the assumed efficiency of 21%.
- The roof insulation measure increases the R-value of the existing building to align with the recommended values from the Advanced Energy Design Guide (AEDG) for Small to Medium Office Buildings: 50% Energy Savings [1]. Target R-values range between R-21 and R-38 for climate zones 1-8, respectively.
- The addition of 40% rooftop coverage is applied to all ComStock models.
- The rooftop insulation measure is applied only to models where the existing roof insulation is less than the values recommended in the Advanced Energy Design Guide.
- 2025 Release 2: 2025/comstock\_amy2018\_release\_2/

National annual results for site energy and energy bills are summarized in Table 2 and Table 3. This report highlights key findings to introduce and help interpret the data. For more comprehensive results, refer to the full public dataset.

Table 2. Summary of Key Results for Annual Site Energy Savings

<!-- table recovered from assets/files/ComStock Measure Doc_PV with Roof Insulation.pdf p.4
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_PV with Roof Insulation.yaml
     method: pdf-text-layer
     supersedes the extractor's own table here (values e08b1d1611d4…):
       docling emitted this grid below the Table 3 caption instead of its own, so a reader
       sees "Summary of Key Results for Annual Utility Bill Savings" followed by TBtu figures.
       The values are correct and identical to Table 8 in the Results chapter, which is why
       the fingerprint alone matches two tables and the entry also names the caption the
       misplaced grid sits under. Table 3's own grid follows its note and is left alone. -->

| Fuel Type | Percent Savings (All Buildings) | Percent Savings (Applicable Buildings Only) | Absolute Savings (TBtu) |
|---|---|---|---|
| Natural Gas | 5.7% | 5.7% | 81.6 |
| Electricity (Purchased) | 33.8% | 33.8% | 1,123.5 |
| Propane | 7.7% | 7.7% | 3.2 |
| Fuel Oil | 8.6% | 8.6% | 4.5 |
| Total | 24.9% | 24.9% | 1,212.9 |

'Applicable' buildings are those that receive the upgrade based on criteria defined for this study.

Table 3. Summary of Key Results for Annual Utility Bill Savings

Electricity bill savings in this table are calculated using the mean available electricity rate available for each building. Other electricity rate structures are available in this report and in the public dataset. 'Applicable' buildings are those that receive the upgrade based on criteria defined for this study.

| End Use / Fuel Type   | Percent Savings (All Buildings)   | Percent Savings (Applicable Buildings Only)   |   Absolute Savings (Billion USD, 2022) |
|-----------------------|-----------------------------------|-----------------------------------------------|----------------------------------------|
| Natural Gas           | 5.4%                              | 5.4%                                          |                                    0.9 |
| Electricity           | 30.6%                             | 30.6%                                         |                                   33.9 |
| Propane               | 7.7%                              | 7.7%                                          |                                    0.1 |
| Fuel Oil              | 8.6%                              | 8.6%                                          |                                    0.2 |
| Total                 | 27.0%                             | 27.0%                                         |                                   35.0 |

## Acknowledgments

The authors would like to acknowledge the valuable guidance and input provided by Eric Bonnema and Eric Ringold. In addition, the authors would like to thank the developers of PVWatts, which was used for this analysis.

## Table of Contents

| Executive 1 2                                                                                                                                                | Summary ................................................................................................................................... iv Introduction ........................................................................................................................................... 2 ComStock Baseline Approach ............................................................................................................ 4   |    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|
| Modeling Approach ..................................................................................................................................... 5    | Modeling Approach ..................................................................................................................................... 5                                                                                                                                                                                                                                                                                             |    |
| 2.1                                                                                                                                                          | PV with 40% Rooftop Coverage ................................................................................................... 5                                                                                                                                                                                                                                                                                                                    |    |
| 2.1                                                                                                                                                          | 2.1.1 Modeling Approach.......................................................................................................... 5                                                                                                                                                                                                                                                                                                                   |    |
| 2.1                                                                                                                                                          | 2.1.2 Applicability .....................................................................................................................                                                                                                                                                                                                                                                                                                             |  5 |
| 2.2                                                                                                                                                          | Rooftop Insulation .........................................................................................................................                                                                                                                                                                                                                                                                                                          |  5 |
| 2.2                                                                                                                                                          | 2.2.1 Modeling Approach.......................................................................................................... 5                                                                                                                                                                                                                                                                                                                   |    |
| 2.2                                                                                                                                                          | 2.2.2 Applicability .....................................................................................................................                                                                                                                                                                                                                                                                                                             |  6 |
| 2.3                                                                                                                                                          | Utility Bills .................................................................................................................................... 6                                                                                                                                                                                                                                                                                                  |    |
| 2.4 3                                                                                                                                                        | Limitations and Concerns ..............................................................................................................                                                                                                                                                                                                                                                                                                               |  7 |
|                                                                                                                                                              | Variables ...................................................................................................................................                                                                                                                                                                                                                                                                                                         |  9 |
| Output                                                                                                                                                       | Output                                                                                                                                                                                                                                                                                                                                                                                                                                                | 10 |
| 4 Results .................................................................................................................................................  | 4 Results .................................................................................................................................................                                                                                                                                                                                                                                                                                           | 10 |
| 4.1                                                                                                                                                          | Stock Energy Impacts ..................................................................................................................                                                                                                                                                                                                                                                                                                               |    |
| 4.2                                                                                                                                                          | Stock Utility Bill Impacts ............................................................................................................                                                                                                                                                                                                                                                                                                               | 12 |
| 4.3                                                                                                                                                          | Energy Savings by State ..............................................................................................................                                                                                                                                                                                                                                                                                                                | 14 |
| 4.4                                                                                                                                                          | Utility Bill Savings Distributions ................................................................................................                                                                                                                                                                                                                                                                                                                   | 15 |
| References ................................................................................................................................................. | References .................................................................................................................................................                                                                                                                                                                                                                                                                                          | 18 |

## List of Figures

| Figure 1. Comparison of annual site energy consumption between the PV 40% + Roof Insulation (Package_12) measure                                                                                                                                                                                                                  | the ComStock baseline, PV 40%, and scenarios .......................................... 11      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Figure 2. Annual utility bill impacts using the max, mean, and minimum bills across available rate structures for buildings for both the PV 40 % and PV 40% + Roof Insulation measure scenarios ................................................................................................................................. | 13 ..................................................                                           |
| Figure 3. Median percent total site energy consumption savings by state                                                                                                                                                                                                                                                           | 14                                                                                              |
| Figure 4. Median percent net site energy consumption savings by                                                                                                                                                                                                                                                                   | state .................................................... 15                                   |
| Figure 5. Percent annual utility bill savings distribution for ComStock                                                                                                                                                                                                                                                           | models with the PV 40% + Roof                                                                   |
| Insulation measure scenario by fuel type ...............................................................................                                                                                                                                                                                                          | 16                                                                                              |
| Figure 6. Percent annual utility bill savings distribution for ComStock models Insulation measure scenario by climate zone                                                                                                                                                                                                        | with PV-40% + Roof ......................................................................... 17 |
| List of                                                                                                                                                                                                                                                                                                                           |                                                                                                 |
| Tables Table 1. Summary of Key Modeling Specifications                                                                                                                                                                                                                                                                            | .................................................................................... iv         |
| Table 3. Summary of Key Results for Annual Utility Bill Savings Table 4. Assumptions for PV Modeling .......................................................................................................                                                                                                                      | .............................................................. v 5                              |
| Table 5. AEDG Overall Target Roof Assembly Performance Characteristics by Climate Zone                                                                                                                                                                                                                                            | ................. 6                                                                             |
| Table 7. Output Variables Calculated From the Measure Application .........................................................                                                                                                                                                                                                       |                                                                                                 |
| Table 6. Summary Statistics of Utility Bill Implementation in ComStock by Fuel Type ............................                                                                                                                                                                                                                  | 6                                                                                               |
| 9. Summary of Key Results for Annual Utility Bill Savings                                                                                                                                                                                                                                                                         |                                                                                                 |
| Table 8. Summary of Key Results for Annual Site Energy Savings                                                                                                                                                                                                                                                                    |                                                                                                 |
| ..........................................................                                                                                                                                                                                                                                                                        | 9                                                                                               |
|                                                                                                                                                                                                                                                                                                                                   | 11                                                                                              |
| Table                                                                                                                                                                                                                                                                                                                             | 13                                                                                              |
| ............................................................                                                                                                                                                                                                                                                                      |                                                                                                 |

## 1 Introduction

Photovoltaics (PV) are an energy generation technology that has widespread adoption. The cost of panels has come down while efficiency has increased [2]. State-of-the-art modules are approaching nearly 25% efficiency, compared to less than 10% efficiency in the 1980s [3].

Despite increased overall PV adoption, commercial buildings still use PV at relatively low rates. According to the 2018 Commercial Buildings Energy Consumption Survey (CBECS), fewer than 2% of commercial buildings have on-site PV [4]. This statistic may have increased since the survey was conducted.

Commercial buildings generally have flat roofs, with fewer than 10% of the building stock having a pitched roof [4]. Ballasted PV panels can be placed on flat roofs at the locationdependent preferred tilt and azimuth angle to maximize energy and/or cost reduction. Pitched roofs generally require a system that mounts onto the roof; however, these systems are not modeled in ComStock. Some commercial buildings use a portion of the roof for heating, ventilating, and air conditioning (HVAC) equipment, so PV panels would have to work around these constraints. Rooftops can also be used for occupant space, such as patios, so these areas would need to be avoided as well. Additionally, with any configuration, proper access pathways and fire escapes need to be maintained. Thus, although there is notable commercial building rooftop area available, some of these areas would not be applicable for PV panels.

Roof insulation mitigates heat loss through a building's exterior roof surfaces. For the purposes of this document, a roof is defined as sky-facing exterior horizontal surfaces sloped within 60 degrees of sky-facing horizontal. The most common roof construction methods are covered in [5] and can be aligned to nominal thermal characteristics:

1. Roof with insulation entirely above deck (IEAD) refers to a roof with all insulation:
1. Installed above (outside of) the roof structure
2. Continuous (i.e., uninterrupted by framing members)
2. Metal building roof refers to a roof that:
1. Is constructed with a metal, structural, weathering surface
2. Has no ventilated cavity
3. Has the insulation entirely below deck (i.e., does not include composite concrete and metal deck construction nor a roof framing system that is separated from the superstructure by a wood substrate) and whose structure consists of one or more of the following configurations:
1. Metal roofing in direct contact with the steel framing members
2. Metal roofing separated from the steel framing members
3. Insulated metal roofing panels installed as described in subitems (a) or (b).
3. Attic and other roofs refers to all other roofs, including roofs with insulation entirely below (inside of) the roof structure (i.e., attics, cathedral ceilings, and single-rafter ceilings), roofs with insulation both above and below the roof structure, and roofs without insulation but excluding metal building roofs.

1. Single-rafter roof is a subcategory of attic roofs where the roof above and the ceiling below are both attached to the same wood rafter, and insulation is located in the space between these wood rafters.

Roof insulation is applied to many existing commercial buildings. Continuous insulation is included as a requirement for all climate zones with roofs that have insulation entirely above deck according to ASHRAE 90.1 2019 [5], noting that many existing roof systems were installed according to much older energy code requirements (or none at all) due to the long turnover rate of architectural elements. Problems with insulation performance tend to stem from improper water management design or installation; for this measure, and for the ComStock baseline models in general, those issues are assumed to be handled properly.

This study combines two existing ComStock measure scenarios as a package to understand the combined impact: PV with 40% rooftop coverage and improved rooftop insulation. This measure package was evaluated because roof insulation upgrades and PV upgrades can often be coordinated during planned roof replacement or renovation projects. For a more comprehensive review of the individual measure scenarios comprising this package, reference their individual documentation.

## 2 ComStock Baseline Approach

The following subsections provide high-level summaries of the ComStock baseline approach for PV with 40% rooftop coverage and improved roof insulation. For more details about how these systems are modeled in the ComStock baseline, including data sources, reference the ComStock documentation [6].

ComStock assumes all roofs to be flat. Flat roofs are not required for commercial PV, but the roof style can impact the panel mounting type and possibly the panel angle. This work does not consider these potential constraints and assumes any panel angle can be used on every roof. Additionally, ComStock does not currently include shading from neighboring buildings and trees. Although many commercial buildings do not have notable shading limitations, this analysis may overestimate the potential of PV for those that do. This may be particularly impactful for buildings with lower heights than their neighbors or surrounding wooded areas.

## Modeling Approach

The following subsections briefly summarize the modeling approach and applicability for the PV with 40% rooftop coverage and rooftop insulation measure scenarios included in this upgrade package. For more detailed review, refer to the individual upgrade documentation.

## 2.1  PV with 40% Rooftop Coverage

## 2.1.1  Modeling Approach

This study leverages the PVWatts ®  EnergyPlus ®  objects. PVWatts is a National Laboratory of the Rockies (NLR) tool that estimates the energy production of PV systems [7]. The workflow takes the baseline ComStock energy models and applies PVWatts objects with total power levels corresponding to 40% of each model's roof area , multiplied by a 21% panel efficiency. The panels are fixed with no tracking. This workflow is repeated for all ComStock models. The individual performance assumptions for the PV modules are summarized in Table 4 and described further in the individual upgrade documentation.

Table 4. Assumptions for PV Modeling

| Parameter                | Value            |
|--------------------------|------------------|
| Inverter Efficiency      | 96%              |
| DC/AC Ratio              | 1.10             |
| System Losses            | 14%              |
| Panel Related Efficiency | 21%              |
| Panel Area               | 40% of roof area |
| Title and Azimuth        | Varies           |

## 2.1.2 Applicability

The rooftop PV measure scenario is applicable to all models in the ComStock baseline. In practice, some commercial buildings may be less suitable for rooftop PV (e.g., the roof does not have 40% of the area available for PV), which these applicability criteria do not consider. In addition, as mentioned, the ComStock baseline does not currently include any PV installation (which, according to CBECS, may be present in roughly 2% of commercial buildings [4]). Therefore, these results may be slightly overestimating technical potential.

## 2.2  Rooftop Insulation

## 2.2.1  Modeling Approach

The roof insulation upgrade increases the insulation value of modeled roof surfaces such that the final applied insulation thickness meets the specified R-value, determined from the Zero Energy Small/Medium Office AEDG: 50% Energy Savings [1], target assembly performance for each climate zone (Table 5), skipping roof surfaces that already meet or exceed these values. To better align with how insulation is often sold, the applied thickness of additional insulation is rounded up to the nearest inch, which may cause some buildings to slightly exceed the AEDG values. The upgrade assumes extruded polystyrene (XPS) insulation with a thermal resistance of R-5/inch.

Table 5. AEDG Overall Target Roof Assembly Performance Characteristics by Climate Zone

<!-- table recovered from assets/files/ComStock Measure Doc_PV with Roof Insulation.pdf p.12
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_PV with Roof Insulation.yaml
     method: pdf-text-layer
     supersedes the extractor's own table here (values 1192c29776d5…):
       docling dropped the first data column: the extracted grid runs climate zones 2 to 8 and
       omits zone 1 and its R-21 target. The text layer and the page render both carry eight
       zones, 1 to 8, with R-values 21, 26, 26, 33, 33, 33, 37, 37. -->

| ASHRAE Climate Zone | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| R-Value (hr ft² F/British thermal unit) | 21 | 26 | 26 | 33 | 33 | 33 | 37 | 37 |

## 2.2.2 Applicability

The roof insulation upgrade applies to all roof assemblies with R-values below the target AEDG R-values. For ComStock, only roofs that follow ComStock 90.1-2013 or newer energy code during the last roof replacement (or installation) have R-values that meet or exceed the AEDG recommendation.

## 2.3  Utility Bills

ComStock provides utility bill estimates for several fuel types in buildings: electricity, natural gas, propane, and fuel oil. The current implementation represents utility bills circa 2022, which is the most current year of utility data available from the U.S. Energy Information Administration (EIA). This section provides a high-level overview of the methodology behind utility bills in ComStock, but more detailed information is available in the ComStock Reference Documentation [6]. Summary statistics from this implementation are shown in Table 6. Note that ComStock does not currently estimate utility bills for district heating and cooling.

Table 6. Summary Statistics of Utility Bill Implementation in ComStock by Fuel Type

| Fuel Type   | Minimum Price ($)         | Average Price ($)         | Maximum Price ($)         |
|-------------|---------------------------|---------------------------|---------------------------|
| Natural gas | $0.007/kBtu ($0.70/therm) | $0.012/kBtu ($1.20/therm) | $0.048/kBtu ($4.80/therm) |
| Propane     | $0.022/kBtu ($2.20/therm) | $0.032/kBtu ($3.20/therm) | $0.052/kBtu ($5.20/therm) |
| Fuel oil    | $0.027/kBtu ($2.70/therm) | $0.033/kBtu ($3.30/therm) | $0.036/kBtu ($3.60/therm) |
| Electricity | $0.003/kBtu ($0.01/kWh)   | $0.035/kBtu ($0.12/kWh)   | $3.530/kBtu ($12.04/kWh)  |

Natural gas bills are estimated using 2022 EIA averages by state. 2022 U.S. EIA Natural Gas Prices -Commercial Price and U.S. EIA Heat Content of Natural Gas Delivered to Consumers are used to create an energy price in dollars per kBtu [8].

Propane and fuel oil bills are estimated using 2022 EIA averages by state. Residential No. 2 Distillate Prices by Sales Type and U.S. EIA residential Weekly Heating Oil and Propane Prices (October -March) and EIA assumed heat content for these fuels are used to create an energy price in dollars per kBtu [9]. Residential prices are used because commercial prices are only available at the national resolution. Additionally, most commercial buildings using these fuels are assumed to be smaller buildings where a residential rate is likely realistic. For states where state-level pricing was available, these prices are used directly. For other states, Petroleum Administration for Defense District (PADD)-average pricing is used. For states where PADD-level pricing is not available, national average pricing is used.

The primary resource for ComStock electric utility rates is the Utility Rate Database (URDB) [10], which includes rate structures for about 85% of the buildings and 85% of the floor area in ComStock [6]. The URDB rates include detailed cost features such as time-of-use pricing, demand charges, ratchets, etc. ComStock only uses URDB rates that were entered starting in 2013, and a cost adjustment factor is applied such that the rates reflect 2022 U.S. dollars.

URDB rates are assigned to ComStock models at the census tract level. The URDB can include several rate structures for a census tract. Instead of attempting to presume any single rate, multiple rates from the model's census tract are simulated; the ComStoc k dataset includes rates that result in the minimum, median, mean, and maximum bills for each model.

Many precautions are implemented to prevent less reasonable rates from being applied. This includes removing non-commercial rates, rates with non-building-load keywords (e.g., Security Light, Irrigation, Snow, Cotton Gin), rates where the load profile does not follow any potential min/max demand or energy consumption qualifiers, and rates that cause suspiciously low (&lt;$0.01/kWh) or high (&gt;$0.45/kWh) blended averages. Additionally, any bill that is lower than 25% of the median or higher than 200% of the median is eliminated to avoid unrealistic bills.

For buildings with no URDB electric utility assigned, or for buildings where none of the stored rates are applicable, the annual bill is estimated using the 2022 EIA Form-861 average prices based on the state each model is located in [11]. While this method does not reflect the detailed rate structures and demand charges, it is a fallback for the 15% of buildings in ComStock with no utility assigned.

## 2.4  Limitations and Concerns

The PV 40% measure comes with some modeling limitations, described below. There are no notable limitations or concerns with the increased roof insulation measure.

- This study assumes that all roofs have 40% unshaded area available for a PV array, which may not be the case for all buildings. For example, a 2016 NLR report suggests smaller values in some cases (e.g., buildings under 5,000 ft 2 average only 26% area) [12]. This may overestimate the potential of PV in some cases. Alternatively, some buildings show negative net metered electricity usage with PV covering 40% of the roof area. This can suggest an oversized PV system in some cases.
- The ComStock baseline does not include any PV. CBECS 2018 estimates that ~2% of commercial buildings use PV, so this study may slightly overestimate the impact of mass adoption of PV.
- The PV assumptions in this work primarily follow the defaults used in the PVWatts tool. Although these are meant to be reasonable, real PV systems designs may vary, which can impact performance.
- The PVWatts module used in this analysis does not consider roof shading from the PV panels. Shading could affect the solar heat gain on the roof. The overall impact of this potential roof shading is likely minimal, especially in the context of larger multistory commercial buildings. However, it could have some impact on heating and cooling loads.

- This study uses a DC-to-AC size ratio of 1.1, which is the default assumption in PVWatts. This is a conservative estimate, with other sources suggesting higher values of 1.2 -1.3. A higher value can increase the prevalence of clipping, where PV output beyond what the inverter can handle is lost. However, a higher ratio can be more economical for some projects [13].
- Net metering impacts on utility bills are not included in this study; the PV panels simply reduce the electricity demand on the building meter at the time of generation, with no resale back to the utility. This may underestimate the savings presented in this report and in the ComStock public dataset. However, PV energy that is generated but not used by the building is reported in the public dataset, enabling users to account for excess generation as needed.

## 3 Output Variables

Table 7 includes a list of output variables that are calculated in ComStock. These variables are important in terms of understanding the differences between buildings with and without the measure package applied. These output variables can also be used for understanding the economics of the upgrade (e.g., return on investment) if cost information (i.e., material, labor, and maintenance costs for technology implementation) is available.

Table 7. Output Variables Calculated From the Measure Application

| Upgrade         | Variable Name                                              | Description                                                                                                                                                                       |
|-----------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Roof Insulation | Energy Code Followed During Last Roof Replacement          | The energy code followed during the last roof replacement (or installation) for a building model, which dictates the roof performance properties for the ComStock baseline models |
|                 | Average Roof Absorptance                                   | The average absorptance of all roof surfaces for a building model                                                                                                                 |
|                 | Average Roof U-Value (Btu/ft2-F-hr)                        | Average thermal conductivity of all roof surfaces for a building model                                                                                                            |
|                 | Roof Area (m2)                                             | The exterior roof area for a building model                                                                                                                                       |
| 40% PV Rooftop  | com_stock_sensitivity_reports.com_report_pv_system_size_kw | Total photovoltaic design capacity in kW                                                                                                                                          |
| Coverage        | simulation_output_report.electricity_pv_kwh                | Annual PV electricity energy consumption in kWh, where negative values indicate generation                                                                                        |
|                 | simulation_output_report.purchased_site_electricity_kwh    | Annual purchased electricity following any on-site generation                                                                                                                     |
|                 | simulation_output_report.net_site_electricity_kwh          | Annual net electricity energy consumption in kWh, with negative values indicating excess on-site electricity generation sent back to the grid                                     |
|                 | simulation_output_report.total_site_electricity_kwh        | Building annual total site electricity energy consumption; does not include impacts of PV                                                                                         |

## 4 Results

In this section, results are presented both at the stock level and for individual buildings through savings distributions. Stock-level results include the combined impact of all the analyzed buildings in ComStock, including buildings that are not applicable to this measure. Therefore, they do not necessarily represent the energy savings of a particular or average building. Stocklevel results should not be interpreted as the savings that a building might realize by implementing the measure.

Total site energy savings are also presented in this section. Total site energy savings can be a useful metric, especially for quality assurance/quality control, but this metric on its own can have limitations for drawing conclusions. Further context should be considered, as site energy savings alone do not necessarily translate proportionally to savings for a particular fuel type (e.g., gas or electricity), source energy savings, or cost savings. This is especially important when a measure impacts multiple fuel types or causes decreased consumption of one fuel type and increased consumption of another. Many factors should be considered when analyzing the impact of an energy efficiency strategy, depending on the use case.

## 4.1  Stock Energy Impacts

The PV 40% + Roof Insulation measure results in 1,043 trillion British thermal units (TBtu) of PV electricity used on-site annually across the modeled U.S. commercial building stock, with an additional 883 TBtu of excess generation exported to the grid (Figure 1). This corresponds to a total PV production of 1,925 TBtu nationally. PV electricity used on-site accounts for approximately 33% of the annual electricity usage modeled in ComStock. In the ComStock public dataset, PV generation is represented as negative electricity consumption.

In addition, the increased roof insulation contributes a 3.1% (154 TBtu) reduction in total site energy consumption. These savings are primarily observed in heating, cooling, and fan end uses, as improved roof insulation enhances thermal retention and reduces HVAC loads. The breakdown of site energy consumption by end use and fuel type is illustrated in Figure 1, which includes both the standalone PV 40% measure and the PV 40% + Roof Insulation measure for comparison.

While the total PV generation between the PV 40% measure and the PV 40% + Roof Insulation measure is identical, the fraction of electricity used on-site versus exported to the grid differs. The added roof insulation slightly alters buildings load profiles and the timing of demand, affecting how much PV electricity is consumed on-site at each timestep. Because the increased roof insulation reduces on-site electricity demand, the PV 40% + Roof Insulation measure results in more excess generation exported to the grid compared to the standalone PV 40% measure.

Table 8 summarizes the absolute and percent energy savings by fuel for the PV 40% + Roof Insulation measure. Savings for the full stock and 'applicable buildings only' are identical, as this package is applicable to 100% of buildings. At the stock level, natural gas, propane, and fuel oil observe 5% -9% savings, driven by reduced heating loads resulting from improved roof insulation. Purchased electricity across the stock is reduced by 34%, largely because PV generation offsets approximately one-third of on-site electricity consumption. A smaller portion of the electricity reduction is attributable to lower cooling demand from the improved roof insulation.

Figure 1. Comparison of annual site energy consumption between the ComStock baseline, PV 40%, and the PV 40% + Roof Insulation (Package\_12) measure scenarios

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_PV with Roof Insulation.yaml
     source: ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000001_7a6ab579800d3a7e4b9f7bf9ed3ef30cf0282cd6d2a2a0959ca2cba4ce6c570e.png
     method: vision-description
     described: 2026-10-16 -->

![Figure 1: stacked bar chart of annual site energy by end use and fuel for Baseline, Add_PV_40pct and Package_12](ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000001_7a6ab579800d3a7e4b9f7bf9ed3ef30cf0282cd6d2a2a0959ca2cba4ce6c570e.png)

Figure 1: stacked bar chart of annual energy consumption in TBtu (y, -2000 to 5000) for three
scenarios: Baseline, Add_PV_40pct and Package_12. Stacks above zero are end use by fuel (heating,
cooling, interior equipment, lighting, fans, water systems); below zero, photovoltaics used on
site and excess exported. Totals above zero fall from 4,987 to 4,833 TBtu with the package. See
Table 8 for savings by fuel.

Energy consumption is categorized both by fuel type and end use.

## Table 8. Summary of Key Results for Annual Site Energy Savings

'Applicable' buildings are those which receive the upgrade based on criteria defined for this study.

| Fuel Type               | Percent Savings (All Buildings)   | Percent Savings (Applicable Buildings Only)   |   Absolute Savings (TBtu) |
|-------------------------|-----------------------------------|-----------------------------------------------|---------------------------|
| Natural Gas             | 5.7%                              | 5.7%                                          |                      81.6 |
| Electricity (Purchased) | 33.8%                             | 33.8%                                         |                   1,123.5 |
| Propane                 | 7.7%                              | 7.7%                                          |                       3.2 |
| Fuel Oil                | 8.6%                              | 8.6%                                          |                       4.5 |
| Total                   | 24.9%                             | 24.9%                                         |                   1,212.9 |

## 4.2  Stock Utility Bill Impacts

The PV 40% + Roof Insulation measure scenario demonstrates 26% -28% ($29 -$41 billion USD, 2022) in utility bill savings for the U.S. commercial building stock modeled in ComStock, depending on the electricity rate structure (Figure 2). This report reviews utility bill results for the maximum, mean, and minimum electricity rate structures available for each building.

Bill savings are solely due to reducing purchased grid electricity by using generated on-site PV electricity. This bill analysis does not consider excess PV electricity sent back to the grid. While customers may receive monetary payments or bill credits for excess electricity through net metering or other utility programs, these mechanisms vary widely by utility and jurisdiction and are therefore difficult to model consistently. However, excess PV generation is reported in the ComStock public dataset if users want to include it in their analysis. For example, users could assume and apply a $/kWh for electricity sold back to the grid. Doing so would increase bill savings further.

As expected, most of the savings come from electricity bills, as these are heavily offset by PV electricity generation. Natural gas bills show $1 billion in savings across the stock, which is due to the increased roof insulation reducing heating demand. Propane and fuel oil bills show minor reductions but make up a negligible portion of total bills at the national level.

Figure 2 also shows the incremental bill savings for the PV 40% + Roof Insulation measure compared with the standalone PV 40% measure. The increased roof insulation demonstrates $2 -$3 billion in additional savings due to the added insulation benefits. These additional bill savings are seen in both electricity and natural gas bills, as the insulation reduces both heating and cooling end uses.

Table 9 summarizes the absolute and percent utility bill savings by fuel for the PV 40% + Roof Insulation package. At the stock level, natural gas, propane, and fuel oil bills are reduced by 5% -9%, driven by lower heating demand from improved roof insulation. Electricity bills are reduced by 31%, leading to total annual utility bill savings of 27% across the modeled stock. PV generation offsets a substantial portion of on-site electricity consumption, while reduced HVAC loads from the increased roof insulation provide additional bill reductions. Overall, pairing PV with increased roof insulation substantially decreases the amount of electricity customers must purchase from the utility. Utility bill savings for individual buildings may vary greatly depending on electricity rates, rate structures, and utility programs for excess generation.

Figure 2. Annual utility bill impacts using the max, mean, and minimum bills across available rate structures for buildings for both the PV 40 % and PV 40% + Roof Insulation measure scenarios

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_PV with Roof Insulation.yaml
     source: ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000002_5cde5663cc81c26927b3e86f9f152bfb32eb59eaaf1b8777e55a692108d6d96f.png
     method: vision-description
     described: 2026-10-16 -->

![Figure 2: three-panel stacked bars of annual utility bills under max, mean and min electricity rates, three scenarios](ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000002_5cde5663cc81c26927b3e86f9f152bfb32eb59eaaf1b8777e55a692108d6d96f.png)

Figure 2: three stacked bar panels (max, mean and min electricity rate) of annual utility bill in
billion USD 2022 (y, 0 to about 150), bars for Baseline, Add_PV_40pct and Package_12, stacked by
electricity, natural gas, propane and fuel oil. Under the mean rate the bill falls from 129 to 97
(-25%) with PV alone and to 94 (-27%) with the package. See Table 9.

Includes buildings not applicable to the heat pump rooftop unit (HP-RTU) measure scenarios.

## Table 9. Summary of Key Results for Annual Utility Bill Savings

Electricity bill savings in this table are calculated using the mean available electricity rate available for each building. Other electricity rate structures are available in this report and in the public dataset. 'Applicable' buildings are those which receive the upgrade based on criteria defined for this study.

| End Use / Fuel Type   | Percent Savings (All Buildings)   | Percent Savings (Applicable Buildings Only)   |   Absolute Savings (Billion USD, 2022) |
|-----------------------|-----------------------------------|-----------------------------------------------|----------------------------------------|
| Natural Gas           | 5.4%                              | 5.4%                                          |                                    0.9 |
| Electricity           | 30.6%                             | 30.6%                                         |                                   33.9 |
| Propane               | 7.7%                              | 7.7%                                          |                                    0.1 |
| Fuel Oil              | 8.6%                              | 8.6%                                          |                                    0.2 |
| Total                 | 27.0%                             | 27.0%                                         |                                   35.0 |

## 4.3  Energy Savings by State

Figure 3 shows the median percent total site energy consumption savings by state. These values do not account for on-site PV generation and therefore reflect savings attributable solely to the roof insulation upgrade. The results show a clear geographic trend, in which colder regions experience the highest savings (3% -4%), while warmer regions experience lower savings (1% -3%). The improved roof insulation has the greatest impact in cold regions where heat loss during winter is most significant. The highest savings are observed in Kansas and Missouri (3.9%), while the lowest savings occur in Hawaii (0.7%), California (1.3%), and Florida (1.3%).

Figure 3. Median percent total site energy consumption savings by state

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_PV with Roof Insulation.yaml
     source: ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000003_0a2ec7227f3aa826ca6cd6b6d8f2ccce053c74c83d8d179c45bd6bd5da648586.png
     method: vision-description
     described: 2026-10-16 -->

![Figure 3: choropleth map of median percent total site energy savings by state, Package_12](ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000003_0a2ec7227f3aa826ca6cd6b6d8f2ccce053c74c83d8d179c45bd6bd5da648586.png)

Figure 3: choropleth map of the contiguous United States shading each state by median percent
total site energy savings for the PV plus roof insulation package, darker green for higher. Values
run from about 1.3% (Florida, California) to about 3.9% in the central and upper Midwest; most
northern states sit between 3% and 4%, Gulf and Southwest states between 1% and 3%.

Alaska: 3.0%, Hawaii: 0.7%

Figure 4 shows the median percent net site energy consumption savings by state, which do account for on-site PV generation. States with the highest savings are concentrated in the Southwest, where solar irradiance and PV production potential are the highest [14]. In addition to high solar resource availability, net site energy savings are influenced by the temporal alignment between commercial building loads and PV generation. In warmer regions, high cooling demands during peak afternoon hours increase the amount of PV generation that can be directly offset on-site, especially when energy storage is not present. New Mexico, Arizona, and California showed the highest net site energy savings of 55% or more, while Hawaii and New York show the lowest savings of 16% and 24%, respectively.

Figure 4. Median percent net site energy consumption savings by state

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_PV with Roof Insulation.yaml
     source: ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000004_87e5a988403848531ea1aec554317ef7036ff5946342da09fde4c9fa866bab50.png
     method: vision-description
     described: 2026-10-16 -->

![Figure 4: choropleth map of median percent net site energy savings by state, Package_12](ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000004_87e5a988403848531ea1aec554317ef7036ff5946342da09fde4c9fa866bab50.png)

Figure 4: choropleth map of the contiguous United States shading each state by median percent
net site energy savings (purchased electricity after on-site PV), darker green for higher. The
Southwest leads, roughly 50% to 60% in New Mexico, California and Arizona; the Northeast and
upper Midwest are lowest at roughly 24% to 31%. Net savings exceed total site savings (Figure 3)
because exported PV counts against purchases.

Alaska: 15.9%, Hawaii: 30.0%

## 4.4  Utility Bill Savings Distributions

Figure 5 shows the distribution of utility bill savings for all ComStock models across fuel types. The median building shows approximately 30% total bill savings using the mean electricity bill. This is due to reductions in purchased electricity, as well as reduced overall energy consumption due to the increased roof insulation. Electricity bills are reduced by 30% or more in most buildings.

Electricity is the only fuel whose bills are affected by PV generation. Energy from on-site combustion fuels (natural gas, propane, fuel oil) cannot be offset by PV, therefore bill savings for these fuels are solely attributable to the increased roof insulation. Median savings for combustion fuel bills are in the range of 5% -10% due to the added roof insulation reducing heating loads. The results show a small number of outliers in the distribution with negative combustion fuel savings. After investigation, most instances of negative natural gas bill savings occur in warehouses. Although rare, it is possible that the added roof insulation reduced beneficial solar heat gains in winter, leading to increased HVAC system runtime or cycling. This effect is plausible in warehouses, which typically have low internal gains and are therefore sensitive to internal gain fluctuation.

Some buildings (mostly outliers in the distribution) show negative electricity bill savings (increased bills) when adding PV and the increased roof insulation. This is primarily caused by ComStock's current electric utility rate selection scheme. ComStock selects applicable rates from the URDB, sometimes based on demand limits. Adding PV sometimes reduces these demand limits, which can change the included rates for a building. Therefore, these bill increases are generally caused by differences in the applicable electric rate structures or charges for a model, rather than a real increase in any single bill.

Figure 5. Percent annual utility bill savings distribution for ComStock models with the PV 40% + Roof Insulation measure scenario by fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_PV with Roof Insulation.yaml
     source: ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000005_cce74eced9d2a6d3283836452852af2824b503d0ab1ab99b55efe490e7dbd9bc.png
     method: vision-description
     described: 2026-10-16 -->

![Figure 5: violin and box plots of percent annual utility bill savings by fuel type for Package_12 (unweighted)](ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000005_cce74eced9d2a6d3283836452852af2824b503d0ab1ab99b55efe490e7dbd9bc.png)

Figure 5: horizontal violin plots with inset box plots of percent annual utility bill savings
(x, -160 to 100) for the package, one row per bill: propane state average (n=3,383), fuel oil state
average (n=1,486), natural gas state average (n=60,495), electricity with mean rate (n=124,410)
and bill mean (n=124,424). Electricity and total-bill medians sit near 30% to 35%; fuel bills near
5% to 10%, with long negative tails. See Table 9.

Results shown in this plot are the savings for the average available utility rate per building. The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of unweighted ComStock models that were applicable for energy savings for the fuel type category.

Figure 6 shows the distribution of total utility bill savings by climate zone, based on the mean electric rate. Warmer climates generally exhibit greater savings due to higher solar resource availability and a larger share of electric end uses that PV can offset (e.g., more cooling and electric heating, less gas heating). Outliers with increased utility bills are caused by the same factors discussed in Figure 5.

Figure 6. Percent annual utility bill savings distribution for ComStock models with PV-40% + Roof Insulation measure scenario by climate zone

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_PV with Roof Insulation.yaml
     source: ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000006_3d8c581165937f1795693d8820fab71f381c9e386b2d2fea60f998a806a81610.png
     method: vision-description
     described: 2026-10-16 -->

![Figure 6: violin and box plots of percent annual utility bill savings by ASHRAE climate zone for Package_12](ComStock_Measure_Doc_PV_with_Roof_Insulation_images/image_000006_3d8c581165937f1795693d8820fab71f381c9e386b2d2fea60f998a806a81610.png)

Figure 6: horizontal violin plots with inset box plots of percent annual utility bill savings
(x, -100 to 80) for the package, one row per ASHRAE climate zone from 1A to 8 with model counts
(n=669 in zone 8 to n=19,709 in 4A). Medians fall between about 20% and 40%, highest in the hot
zones 2A, 2B and 3B and lowest in the cold zones 6A, 7 and 8. Distributions skew negative.

Results shown in this plot are the savings for the average available utility rate per building. The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of unweighted ComStock models that were applicable for energy savings for the fuel type category.

## References

- [1] ASHRAE, Achieving Zero Energy - Advanced Energy Design Guide for Small to Medium Office Buildings . Atlanta, Georgia: ASHRAE.
- [2] U.S. Energy Information Administration, 'Average U.S. construction costs drop for solar, rise for wind and natural gas generators,' https://www.eia.gov/todayinenergy/detail.php?id=54519.
- [3] U.S. Energy Information Administration, 'Solar explained: Photovoltaics and electricity,' https://www.eia.gov/energyexplained/solar/photovoltaics-and-electricity.php.
- [4] U.S. Energy Information Administration, 'Commercial Buildings Energy Consumption Survey (CBECS) .' [Online]. Available: https://www.eia.gov/consumption/commercial/.
- [5] ASHRAE, 'ANSI/ASHRAE/IES Standard 90.1 -2019: Energy Standard Residential Buildings Except LowRise for Buildings,' Atlanta, Georgia, 2019.
- [6] A. Parker et al. , ComStock Reference Documentation: Version 1 . Golden: National Renewable Energy Laboratory.
- [7] National Laboratory of the Rockies, 'PVWatts Calculator,' 2025, National Laboratory of the Rockies, Golden, Colorado : 8.5.
- [8] U.S. Energy Information Administration, 'Use of natural gas - U.S. Energy Information Administration (EIA).' Accessed: May 22, 2024. [Online]. Available: https://www.eia.gov/energyexplained/natural-gas/use-of-natural-gas.php
- [9] U. S. Energy Information Administration, 'Weekly Heating Oil and Propane Prices.' [Online]. Available:
10. https://www.eia.gov/dnav/pet/pet\_pri\_wfr\_a\_EPD2F\_PRS\_dpgal\_w.htm.
- [10] U.S. Energy Information Administration, 'Utility Rate Database.' [Online]. Available: https://openei.org/wiki/Utility\_Rate\_Database.
- [11] U.S. Energy Information Administration, 'Monthly Energy Review,' https://www.eia.gov/totalenergy/data/monthly/.
- [12] Pieter Gagnon, Robert Margolis, Jennifer Melius, Caleb Phillips, and Ryan Elmore, 'Rooftop Solar Photovoltaic Technical Potential in the United States: A Detailed Assessment,' Golden, Colorado, Jan. 2016.
- [13] Paul Grana, 'Solar inverters and clipping: What DC/AC inverter load ratio is ideal?,' https://www.solarpowerworldonline.com/2016/07/solar-inverters-clipping-dcac-inverterload-ratio-ideal/.
- [14] energydata.info, "Global Solar Atlas," [Online]. Available: https://globalsolaratlas.info/map.
