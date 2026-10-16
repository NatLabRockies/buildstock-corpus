<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_PV with Roof Insulation.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/2036a73dc9b7a5dccb8b62fe835cdcbc777175fa/assets/files/ComStock%20Measure%20Doc_PV%20with%20Roof%20Insulation.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_PV%20with%20Roof%20Insulation.pdf | corpus_version: comstock_amy2018_2025_release_3-v3 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_PV with Roof Insulation.md | section: Executive Summary | lines: 57-147 -->
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

