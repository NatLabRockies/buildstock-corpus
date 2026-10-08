<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/98346.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/98346.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/98346.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/98346.md | section: Executive Summary | lines: 73-121 -->
## Executive Summary

Building on the 3-year End-Use Load Profiles project to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models, this work produces national datasets that enable cities, states, utilities, and other stakeholders to answer a broad range of questions regarding their commercial building stock.

ComStock is a highly granular, bottom-up model that uses various data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual sub-hourly energy consumption of the commercial building stock across the United States. The 'baseline' model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology of the baseline model is discussed in the ComStock Reference Documentation.

The goal of this work is to develop energy efficiency and demand flexibility measures that cover market-ready technologies and study their mass-adoption impact on the baseline building stock. 'Measures' refers to various 'what-if' scenarios that can be applied to buildings. The results for the baseline and measure scenario simulations are published in public datasets that provide insights into building stock characteristics, operational behaviors, utility bill impacts, and annual and sub-hourly energy usage by fuel type and end use.

This report describes the modeling methodology for a single ComStock measure scenarioThermostat Setbacks During Unoccupied Periods-and briefly introduces key results. The full public dataset can be accessed on the ComStock data lake or via the Data Viewer at comstock.nrel.gov. The public dataset enables users to create custom aggregations of results for their use cases (e.g., filter to a specific county or building type).

Key modeling assumptions and technology details are summarized in Table ES-1.

Table ES-1. Summary of Key Modeling Specifications

| Technology Description   | • This measure implements thermostat setbacks during unoccupied periods in zones where they are not already present. Thermostat setbacks save heating and cooling energy (and in some cases fan energy) by reducing thermal loads during unoccupied periods.                                                                                                                                |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Performance Assumptions  | • This measure implements thermostat setbacks of 10°F in heating and 5°F in cooling during unoccupied periods and an optimum start over a 3-hour period before occupancy. Minimum (55°F) and maximum (82°F) values on unoccupied heating and cooling setpoints are also imposed.                                                                                                            |
|                          | • An optimum start gradually ramps setpoints from their unoccupied to occupied values for greater thermal comfort once occupancy begins.                                                                                                                                                                                                                                                    |
|                          | • The setback ranges, minimum and maximum setpoint values, and optimum start duration are based on a literature review.                                                                                                                                                                                                                                                                     |
| Applicability            | • The measure is applicable to spaces that do not currently have thermostat setbacks or an operational requirement for continuous space conditioning at fixed setpoints (such as data centers, laboratory spaces, and patient-serving areas for medical care). Hotel guest rooms are also exempted from this measure because of the method by which their occupancy is modeled in ComStock. |
|                          | • 41% stock floor area applicable                                                                                                                                                                                                                                                                                                                                                           |
| Release                  | 2025 Release 3: 2025/comstock_amy2018_release_3/                                                                                                                                                                                                                                                                                                                                            |

National annual results for site energy and energy bills are summarized in Table ES-2 and Table ES-3

Table ES-2. Summary of Key Results for Annual Site Energy Savings

'Applicable' buildings are those that receive the upgrade based on criteria defined for this study.

| End Use/Fuel Type   | Percent Site Energy Savings (All Buildings)   | Percent Site Energy Savings (Applicable Buildings Only)   |   Absolute Site Energy Savings (trillion British thermal units [TBtu]) |
|---------------------|-----------------------------------------------|-----------------------------------------------------------|------------------------------------------------------------------------|
| Natural gas         | 4.8%                                          | 12%                                                       |                                                                   68.6 |
| Electricity         | 1.2%                                          | 2.7%                                                      |                                                                   39.4 |
| Fuel oil            | 3.9%                                          | 11%                                                       |                                                                   2.04 |
| Propane             | 6.6%                                          | 11%                                                       |                                                                   2.81 |
| Total               | 2.3%                                          | 5.6%                                                      |                                                                    116 |

Table ES-3. Summary of Key Results for Annual Utility Bill Savings

Electricity bill savings in this table are calculated using the mean available electricity rate available for each building. Other electricity rate structures are available in this report and in the public dataset. 'Applicable' buildings are those that receive the upgrade based on criteria defined for this study.

| End Use/Fuel Type   | Percent Savings (All Buildings)   | Percent Savings (Applicable Buildings Only)   | Absolute Savings (million USD, 2022)   |
|---------------------|-----------------------------------|-----------------------------------------------|----------------------------------------|
| Electricity         | 0.9%                              | 1.9%                                          | $957                                   |
| Natural gas         | 5.6%                              | 14%                                           | $911                                   |
| Fuel oil            | 3.9%                              | 12%                                           | $69                                    |
| Propane             | 6.9%                              | 12%                                           | $85                                    |
| Total               | 1.6%                              | 3.4%                                          | $2,022                                 |

