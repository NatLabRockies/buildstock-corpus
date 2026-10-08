<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95004.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95004.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95004.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/95004.md | section: Executive Summary | lines: 134-190 -->
## Executive Summary

Building on the 3-year effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models, this work produces national datasets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of questions regarding the U.S. commercial building stock, such as the mass adoption of rooftop solar photovoltaics (PV), the focus of this report.

ComStock is a highly granular, bottom-up model that uses various data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The 'baseline' model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology of the baseline model is discussed in the ComStock Reference Documentation.

The goal of this work is to develop energy efficiency and demand flexibility measures that cover market-ready technologies and study their mass adoption impact on the baseline building stock. 'Measures' refers to various 'what-if' scenarios that can be applied to buildings. The results for the baseline and measure scenario simulations are published in public data sets that provide insights into building stock characteristics, operational behaviors, utility bill impacts, carbon emissions equivalent (CO2e), and annual and sub-hourly energy usage by fuel type and end use.

This report describes the modeling methodology for a single end-use savings shape measurePV With 40% Rooftop Coverage-and briefly introduces key results. The full ComStock public dataset can be accessed via the ComStock data lake or the data viewer at comstock.nrel.gov. The public dataset enables users to create custom aggregations of results for their use cases (e.g., filtering to a specific county).

Key modeling assumptions and technology details are summarized in Table ES-1.

Table ES-1. Summary of Key Modeling Specifications

| Measure Scenario        | • This study investigates the impact of adding 40% rooftop PV coverage to the U.S. commercial building stock. This amounts to ~385 GW of installed rated PV capacity.                                                                                                                                                                                                         |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | • Net metering impacts on calculated utility bill or CO 2 e are not included in this study. For these metrics, the PV panels simply reduce the electricity demand on the building meter at the time of generation with no resale back to the utility. However, the ComStock public dataset includes excess PV generation, enabling users to estimate these impacts as needed. |
| Performance Assumptions | • Panels are modeled as higher performance with 21% rated efficiency, 96% inverter efficiency, 1.10 direct current/alternating current (DC/AC) ratio,14% system losses, and azimuth/tilt angles that vary by location.                                                                                                                                                        |
| Applicability           | This measure is applied to all ComStock models.                                                                                                                                                                                                                                                                                                                               |
| Release                 | 2025 Release 1: 2025/comstock_amy2018_release_1/                                                                                                                                                                                                                                                                                                                              |

National annual results for site energy, energy bills, and CO2e are summarized in Table ES-2 through Table ES-4.

Table ES-2. Summary of Key Results for Annual Site Energy Savings

'Applicable' buildings are those that receive the upgrade based on the criteria defined for this study. TBtu = trillion British thermal units.

Table ES-3. Summary of Key Results for Annual Utility Bill Savings

| Fuel Type               |   Absolute Savings [TBtu] |   Baseline Total (All Buildings) [TBtu] | Percent Savings (All Buildings)   |   Baseline Total (Applicable Buildings Only) [TBtu] | Percent Savings (Applicable Buildings Only)   |
|-------------------------|---------------------------|-----------------------------------------|-----------------------------------|-----------------------------------------------------|-----------------------------------------------|
| Natural Gas             |                         0 |                                    1524 | 0%                                |                                                1524 | 0%                                            |
| Electricity (Purchased) |                      1039 |                                    3173 | 33%                               |                                                3173 | 33%                                           |
| Other Fuel              |                         0 |                                      54 | 0%                                |                                                  54 | 0%                                            |

Electricity bill savings in this table are calculated using the mean available electricity rate available for each building. Other electricity rate structures are available in this report and in the public dataset. 'Applicable' buildings are those that receive the upgrade based on the criteria defined for this study. USD = U.S. dollars.

Table ES-4. Summary of Key Results for Annual CO2e Savings

| End Use/Fuel Type   |   Absolute Savings [Billion USD, 2022] |   Baseline Total (All Buildings) [Billion USD, 2022] | Percent Savings (All Buildings)   |   Baseline Total (Applicable Buildings Only) [Billion USD, 2022] | Percent Savings (Applicable Buildings Only)   |
|---------------------|----------------------------------------|------------------------------------------------------|-----------------------------------|------------------------------------------------------------------|-----------------------------------------------|
| Natural Gas         |                                      0 |                                                   17 | 0%                                |                                                               17 | 0%                                            |
| Electricity         |                                     32 |                                                  108 | 30%                               |                                                              108 | 30%                                           |
| Fuel Oil            |                                      0 |                                                    1 | 0%                                |                                                                1 | 0%                                            |
| Propane             |                                      0 |                                                    1 | 0%                                |                                                                1 | 0%                                            |
| Total               |                                     32 |                                                  127 | 25%                               |                                                              127 | 25%                                           |

Electricity emissions avoided in this table are calculated using the Cambium Long-Run Marginal Emissions Rate (LRMER) High Renewable Energy Cost 15-Year grid scenario. Other grid scenarios are presented in this report and in the public dataset. 'Applicable' buildings are those that receive the upgrade based on the criteria defined for this study. MMT = million metric tons; CO2e = carbon dioxide equivalent.

| Fuel Type   |   Absolute Savings [MMT CO 2 e] |   Baseline Total (All Buildings) [MMT CO 2 e] | Percent Savings (All Buildings)   |   Baseline Total (Applicable Buildings Only) [MMT CO 2 e] | Percent Savings (Applicable Buildings Only)   |
|-------------|---------------------------------|-----------------------------------------------|-----------------------------------|-----------------------------------------------------------|-----------------------------------------------|
| Natural gas |                               0 |                                           102 | 0%                                |                                                       102 | 0%                                            |
| Electricity |                              63 |                                           240 | 26%                               |                                                       240 | 26%                                           |
| Fuel Oil    |                               0 |                                             2 | 0%                                |                                                         2 | 0%                                            |
| Propane     |                               0 |                                             3 | 0%                                |                                                         3 | 0%                                            |
| Total       |                              63 |                                           346 | 18%                               |                                                       346 | 18%                                           |

