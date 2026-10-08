<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95015.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95015.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95015.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/95015.md | section: Executive Summary | lines: 134-189 -->
## Executive Summary

Building on the three-year effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models, this work produces national datasets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of questions regarding their commercial building stock.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

The goal of this work is to develop energy efficiency and demand flexibility end-use load shapes that cover high-impact, market-ready (or nearly market-ready) measures. Measures refer to various 'what-if' scenarios that can be applied to buildings.

An end-use savings shape is the difference in energy consumption between a baseline building (or collection of buildings) and a building with an energy efficiency or demand flexibility measure applied. It results in a time-series profile broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step as well as annual aggregations.

This report describes the modeling methodology for a single end-use savings shape measureelectric resistance boilers-and briefly introduces key results. The full public dataset can be accessed on the ComStock data lake or via the Data Viewer at comstock.nrel.gov. The public dataset enables users to create custom aggregations of results for their use case (e.g., filter to a specific county).

Key modeling assumptions and technology details are summarized in Table ES-1. National annual results for site energy, utility bills, and carbon emissions equivalent (CO2e) are summarized in Table ES-2, Table ES-3, and Table ES-4.

Table ES-1. Key Modeling Specifications

| Measure Title           | Electric Resistance Boilers                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Technology description  | This measure study investigates the impacts of replacing existing natural gas-fired boilers with electric resistance boilers. Data is provided for all geographical regions of the U.S. Electric boilers use electric resistance elements to heat water, which can be used for space heating in buildings. Compared to electric heat pumps, they are generally considered to have a relatively lower first cost but also lower performance. |
| Performance assumptions | This measure assumes a nominal thermal efficiency of 1.0 (100%) to represent electric resistance heating efficiency. This compares to traditional atmospheric gas- fired boilers, which operate at around 75%-85% efficiency. Performance curves from the MASControl database are implemented. The curve used is a linear curve, in which the electric input ratio scales linearly from 98% to                                              |
| Applicability           | This measure is applicable to buildings served by hot water boiler systems, which represent 26% of the baseline stock floor area. It is not applicable to buildings served by district heating hot water.                                                                                                                                                                                                                                   |
| Release                 | 2025 Release 2: 2025/comstock_amy2018_release_2/                                                                                                                                                                                                                                                                                                                                                                                            |

Table ES-2. Key Results for Annual Site Energy Savings

| Fuel Type    |   Absolute Savings (TBtu) |   Baseline Total, All Buildings (TBtu) | Percent Savings, All Buildings (%)   |   Baseline Total, Applicable Buildings Only (TBtu) | Percent Savings, Applicable Buildings Only (%)   |
|--------------|---------------------------|----------------------------------------|--------------------------------------|----------------------------------------------------|--------------------------------------------------|
| Natural gas  |                     542.0 |                                 1524.1 | 35.6%                                |                                              670.4 | 80.8%                                            |
| Electricity  |                    -426.0 |                                 3173.4 | -13.4%                               |                                              754.5 | -56.5%                                           |
| Other fuel a |                       6.6 |                                   53.7 | 12.3%                                |                                                6.7 | 98.0%                                            |
| Total        |                     122.6 |                                 4751.2 | 2.5%                                 |                                             1431.7 | 8.6%                                             |

Table ES-3. Key Results for Annual Bill Savings

| Fuel Type   |   Absolute Savings (Billion USD, 2022) |   Baseline Total, All Buildings (Billion USD, 2022) | Percent Savings, All Buildings (%)   |   Baseline Total, Applicable Buildings Only (Billion USD, 2022) | Percent Savings, Applicable Buildings Only (%)   |
|-------------|----------------------------------------|-----------------------------------------------------|--------------------------------------|-----------------------------------------------------------------|--------------------------------------------------|
| Natural gas |                                    6.2 |                                                17.4 | 35.5%                                |                                                             7.7 | 79.7%                                            |
| Electricity |                                  -13.3 |                                               107.7 | -12.4%                               |                                                            26.0 | -51.1%                                           |
| Fuel oil    |                                    0.2 |                                                 0.7 | 33.4%                                |                                                             0.2 | 98.0%                                            |
| Propane     |                                    0.0 |                                                 1.0 | 0.0%                                 |                                                             0.0 | 0.0%                                             |
| Total       |                                   -6.9 |                                               126.8 | -5.4%                                |                                                            34.0 | -20.3%                                           |

Electricity bill savings in this table are calculated using the mean electricity rate available for each building. Other electricity rate structures are available in this report and in the public dataset.

Table ES-4. Key Results for Annual Emissions Savings

| Fuel Type   |   Absolute Savings (MMT CO 2 e) |   Baseline Total, All Buildings (MMT CO 2 e) | Percent Savings, All Buildings (%)   |   Baseline Total, Applicable Buildings Only (MMT CO 2 e) | Percent Savings, Applicable Buildings Only (%)   |
|-------------|---------------------------------|----------------------------------------------|--------------------------------------|----------------------------------------------------------|--------------------------------------------------|
| Natural gas |                            36.2 |                                        101.8 | 35.6%                                |                                                     44.8 | 80.8%                                            |
| Electricity |                           -34.3 |                                        239.6 | -14.3%                               |                                                     53.4 | -64.2%                                           |
| Fuel oil    |                             0.6 |                                          1.7 | 33.5%                                |                                                      0.6 | 98.0%                                            |
| Propane     |                             0.0 |                                          2.7 | 0.0%                                 |                                                      0.0 | 0.0%                                             |
| Total       |                             2.5 |                                        345.9 | 0.7%                                 |                                                     98.8 | 2.5%                                             |

Electricity emissions avoided in this table are calculated using the Cambium Long-Run Marginal Emissions Rate (LRMER) High Renewable Energy (RE) Cost 15-Year grid scenario. Other grid scenarios are presented in this report and in the public dataset.

