<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/96597.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96597.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96597.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/96597.md | section: Executive Summary | lines: 73-124 -->
## Executive Summary

Building on the 3-year End-Use Load Profiles project to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models, this work produces national datasets that enable cities, states, utilities, and other stakeholders to answer a broad range of questions regarding their commercial building stock.

ComStock is a highly granular, bottom-up model that uses various data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The 'baseline' model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology of the baseline model is discussed in the ComStock Reference Documentation.

The goal of this work is to develop energy efficiency and demand flexibility measures that cover market-ready technologies and study their mass adoption impact on the baseline building stock, utility bill affordability, and grid reliability. 'Measures' refers to various 'what-if' scenarios that can be applied to buildings. The results for the baseline and measure scenario simulations are published in public datasets that provide insights into building stock characteristics, operational behaviors, utility bill impacts, and annual and subhourly energy usage by fuel type and end use.

This report describes the modeling methodology for a single ComStock measure scenario -Interior Lighting Controls -and briefly introduces key results. The full public dataset can be accessed on the ComStock data lake or via the Data Viewer at comstock.nrel.gov. The public dataset enables users to create custom aggregations of results for their use case (e.g., filter to a specific county or building type).

Key modeling assumptions and technology details are summarized in Table ES-1.

Table ES-1. Summary of Key Modeling Specifications

| Package Title           | Interior Lighting Controls                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Technology Description  | This measure applies interior lighting controls (daylighting sensors and occupancy sensors) to the model. Daylighting sensors detect the amount of natural light in a space and reduce artificial lighting in the space to maintain a desired brightness level. Occupancy sensors detect the presence of occupants in a space and turn off the lights if no one is present. |
| Performance Assumptions | • Daylighting sensors are applied to the model using EnergyPlus built-in daylighting controls objects. Some checks are applied to ensure that the size of the window and the size of the space is appropriate for daylighting controls per the International Code Council regulations for Interior Lighting Controls.                                                       |
|                         | • Occupancy sensors are modeled as a percent lighting power density reduction based on the space type. The percent reduction in lighting power density was derived from ASHRAE 90.1-2019 'Performance Rating Method Lighting Power Density Allowances and Occupancy Sensor Reductions Using the Space-by-Space Method.'                                                     |

| Package Title   | Interior Lighting Controls                                                                                                                                                              |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Applicability   | • All buildings in the stock will end up getting daylighting controls or occupancy controls in at least one space in the model. Many spaces will get both types of controls.            |
|                 | • Some individual spaces may not receive lighting controls if they a) already have daylighting or occupancy controls, or b) the space does not meet the criteria for lighting controls. |
| Release         | • 100% stock floor area applicable                                                                                                                                                      |
|                 | 2025 Release 2: 2025/comstock_amy2018_release_2/                                                                                                                                        |

National annual results for site energy and utility bills are summarized in Table ES-2 and Table ES-3.

Table ES-2. Summary of Key Results for Annual Site Energy Savings

'Applicable' buildings are those that receive the upgrade based on criteria defined for this study.

| Fuel Type   | Percent Savings (All Buildings)   | Percent Savings (Applicable Buildings Only)   |   Absolute Savings (Trillion British Thermal Units) |
|-------------|-----------------------------------|-----------------------------------------------|-----------------------------------------------------|
| Natural Gas | -1.5%                             | -1.5%                                         |                                               -24.0 |
| Electricity | 3.6%                              | 3.6%                                          |                                               118.3 |
| Other Fuel* | -1.7%                             | -1.7%                                         |                                                -0.9 |
| Total       | 1.9%                              | 1.9%                                          |                                                93.4 |

Table ES-3. Summary of Key Results for Annual Utility Bill Savings

Electricity bill savings in this table are calculated using the mean available electricity rate available for each building. Other electricity rate structures are available in this report and in the public dataset. 'Applicable' buildings are those that receive the upgrade based on criteria defined for this study.

| End Use/Fuel Type   | Percent Savings (All Buildings)   | Percent Savings (Applicable Buildings Only)   | Absolute Savings (Billion USD, 2022)   |
|---------------------|-----------------------------------|-----------------------------------------------|----------------------------------------|
| Natural Gas         | -1.5%                             | -1.5%                                         | -0.3                                   |
| Electricity         | 3.5%                              | 3.5%                                          | 3.9                                    |
| Fuel Oil            | -2.5%                             | -2.5%                                         | <0.0                                   |
| Propane             | -1.2%                             | -1.2%                                         | <0.0                                   |
| Total               | 2.8%                              | 2.8%                                          | 3.6                                    |

