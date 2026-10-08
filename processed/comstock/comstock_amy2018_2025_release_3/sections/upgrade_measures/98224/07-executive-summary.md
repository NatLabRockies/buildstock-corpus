<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/98224.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/98224.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/98224.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/98224.md | section: Executive Summary | lines: 74-124 -->
## Executive Summary

Building on the 3-year End-Use Load Profiles project to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models, this work produces national datasets that enable cities, states, utilities, and other stakeholders to answer a broad range of questions regarding their commercial building stock.

ComStock is a highly granular, bottom-up model that uses various data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual sub-hourly energy consumption of the commercial building stock across the United States. The 'baseline' model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology of the baseline model is discussed in the ComStock Reference Documentation.

The goal of this work is to develop energy efficiency and demand flexibility measures that cover market-ready technologies and study their mass-adoption impact on the baseline building stock. 'Measures' refers to various 'what-if' scenarios that can be applied to buildings. The results for the baseline and measure scenario simulations are published in public datasets that provide insights into building stock characteristics, operational behaviors, utility bill impacts, and annual and sub-hourly energy usage by fuel type and end use.

This report describes the modeling methodology for a single ComStock measure scenarioHigh-Efficiency Rooftop Unit (RTU)-and briefly introduces key results. The full public dataset can be accessed on the ComStock data lake or via the Data Viewer at comstock.nlr.gov. The public dataset enables users to create custom aggregations of results for their use case (e.g., filter to a specific county or building type).

Key modeling assumptions and technology details are summarized in Table ES-1.

Table ES-1. Summary of Key Modeling Specifications

| Technology Description   | • This study considers the mass-adoption scenario of replacing existing RTUs with high-efficiency RTUs for the U.S. commercial building stock. • 'High-efficiency' refers to top-of-the-line products currently available in the United States (as of July 2025). • The high-efficiency RTUs considered in this study provide cooling via direct expansion units and heating with either a gas furnace or electric resistance,   |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Performance Assumptions  | • The high-efficiency RTUs considered in this study have rated cooling capacities (at 95°F) ranging from 65 to 705 thousand British thermal units per hour (kBtu/h; 5-59 tons).                                                                                                                                                                                                                                                  |
| Performance Assumptions  | • Their rated energy efficiency ratios (EER at 95°F) range from 10.0 to 14.6, representing products that exceed the performance requirements of the American Society of Heating, Refrigerating and Air-Conditioning Engineers (ASHRAE) 90.1-2016 standard used in ComStock.                                                                                                                                                      |
| Performance Assumptions  | • Their rated integrated energy efficiency ratios (IEER) range from 12.2 to 25.6, representing products that exceed the performance requirements of the ASHRAE 90.1-2016 standard used in ComStock.                                                                                                                                                                                                                              |
| Performance Assumptions  | • Rated performance data (EER/IEER) were collected from the Air-Conditioning, Heating, and Refrigeration Institute (AHRI) Certification Directory, covering 2,847 models from 35 manufacturers.                                                                                                                                                                                                                                  |
| Performance Assumptions  | • Performances under various operating conditions (different outdoor/indoor temperatures and airflow rates) were extracted and averaged using detailed data from one manufacturer, enabling translation into EnergyPlus/OpenStudio formats.                                                                                                                                                                                      |
| Applicability            | • The high-efficiency RTU measure is applicable to ComStock models with either gas furnace RTUs ('PSZ-AC [packaged single-zone air conditioner] with gas coil'), electric resistance RTUs ('PSZ-AC with electric coil'), gas boilers ('PSZ- AC with gas boiler'), or district heating ('PSZ-AC with district hot water').                                                                                                        |
| Applicability            | • Buildings that do not contain gas-fired or electric resistance RTUs are not applicable. Also, the measure is not applicable to kitchen spaces.                                                                                                                                                                                                                                                                                 |
|                          | • This accounts for about 42% of the ComStock buildings floor area.                                                                                                                                                                                                                                                                                                                                                              |

National annual results for site energy and energy bills are summarized in Table ES-2 and Table ES-3.

Table ES-2. Summary of Key Results for Annual Site Energy Savings

'Applicable' buildings are those that receive the upgrade based on criteria defined for this study.

Table ES-3. Summary of Key Results for Annual Utility Bill Savings

| Fuel Type   | Percent Savings (All Buildings)   | Percent Savings (Applicable Buildings Only)   | Absolute Savings (trillion British thermal units [TBtu])   |
|-------------|-----------------------------------|-----------------------------------------------|------------------------------------------------------------|
| Natural gas | -0.93%                            | -1.9%                                         | -13.4 1                                                    |
| Electricity | 9.3%                              | 19.3%                                         | 309                                                        |
| Fuel oil    | -1.3%                             | -2.6%                                         | -0.71                                                      |
| Propane     | -0.61%                            | -0.81%                                        | -0.26                                                      |
| Total       | 6.1%                              | 12.4%                                         | 294                                                        |

Electricity bill savings in this table are calculated using the mean available electricity rate available for each building. Other electricity rate structures are available in this report and in the public dataset. 'Applicable' buildings are those that receive the upgrade based on criteria defined for this study.

| End Use/Fuel Type   | Percent Savings (All Buildings)   | Percent Savings (Applicable Buildings Only)   |   Absolute Savings (billion USD, 2022) |
|---------------------|-----------------------------------|-----------------------------------------------|----------------------------------------|
| Natural gas         | -0.68%                            | -1.4%                                         |                                  -0.11 |
| Electricity         | 9.2%                              | 19.1%                                         |                                   10.2 |
| Fuel oil            | -1.3%                             | -2.6%                                         |                                 -0.024 |
| Propane             | -0.25%                            | -0.33%                                        |                                -0.0031 |
| Total               | 7.8%                              | 16%                                           |                                   10.1 |

