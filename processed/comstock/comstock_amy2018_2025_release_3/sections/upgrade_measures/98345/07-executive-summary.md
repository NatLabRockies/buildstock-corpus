<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/98345.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/98345.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/98345.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/98345.md | section: Executive Summary | lines: 74-106 -->
## Executive Summary

Building on the 3-year End-Use Load Profiles project to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models, this work produces national datasets that enable cities, states, utilities, and other stakeholders to answer a broad range of questions regarding their commercial building stock.

ComStock is a highly granular, bottom-up model that uses various data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual sub-hourly energy consumption of the commercial building stock across the United States. The 'baseline' model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology of the baseline model is discussed in the ComStock Reference Documentation.

The goal of this work is to develop energy efficiency and demand flexibility measures that cover market-ready technologies and study their mass-adoption impact on the baseline building stock. 'Measures' refers to various 'what-if' scenarios that can be applied to buildings. The results for the baseline and measure scenario simulations are published in public datasets that provide insights into building stock characteristics, operational behaviors, utility bill impacts, and annual and sub-hourly energy usage by fuel type and end use.

This report describes the modeling methodology for a single ComStock measure scenario-Fan Static Pressure Reset for Multizone Variable Air Volume (VAV) Systems-and briefly introduces key results. The full public dataset can be accessed on the ComStock data lake or via the Data Viewer at comstock.nrel.gov. The public dataset enables users to create custom aggregations of results for their use case (e.g., filter to a specific county or building type).

Key modeling assumptions and technology details are summarized in Table ES-1.

Table ES-1. Summary of Key Modeling Specifications

| Technology Description   | • This measure implements a static pressure (SP) reset for air-handling unit fans in multizone VAV systems. An SP reset saves fan energy by allowing fans to operate at a lower SP setpoint during part-load conditions.                                                                                                                                                          |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Performance Assumptions  | • This measure emulates the effects of an SP reset by changing the fan power performance curve as a function of airflow. • The existing fan performance curve is replaced with a curve emulating a 'good' SP reset. The 'good' SP reset curve is used in OpenStudio® Standards for                                                                                                |
| Applicability            | • This measure is applicable to multizone VAV systems in which an SP reset is not already present. This measure is not applicable to fans in dedicated outdoor air systems.                                                                                                                                                                                                       |
|                          | • Currently, some multizone VAV systems in ComStock associated with a template of American Society of Heating, Refrigerating and Air-Conditioning Engineers (ASHRAE) 90.1 2004 or more recent are modeled with an SP reset, depending on fan input power and cooling capacity. No systems modeled with a template older than ASHRAE 90.1 2004 are currently modeled with a reset. |
| Release                  | 2025 Release 3: 2025/comstock_amy2018_release_3/                                                                                                                                                                                                                                                                                                                                  |

National annual results for site energy and energy bills are summarized in Table ES-2 and Table ES- 3.

Table ES-2. Summary of Key Results for Annual Site Energy Savings 'Applicable' buildings are those that receive the upgrade based on criteria defined for this study.

| Fuel Type   | Percentage Savings (All Buildings)   | Percentage Savings (Applicable Buildings Only)   |   Absolute Savings (trillion British thermal units [TBtu]) |
|-------------|--------------------------------------|--------------------------------------------------|------------------------------------------------------------|
| Natural gas | -1.0%                                | -4.5%                                            |                                                      -12.2 |
| Electricity | 3.0%                                 | 14%                                              |                                                        100 |
| Fuel oil    | -1.2%                                | -6.1%                                            |                                                      -0.63 |
| Propane     | -0.1%                                | -5.6%                                            |                                                      -0.04 |
| Total       | 1.9%                                 | 8.7%                                             |                                                       92.7 |

