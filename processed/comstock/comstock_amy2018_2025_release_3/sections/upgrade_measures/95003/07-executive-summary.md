<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95003.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95003.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95003.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/95003.md | section: Executive Summary | lines: 58-123 -->
## Executive Summary

Building on a 3-year effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models, this work produces national datasets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of questions regarding their commercial building stock.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual energy consumption (at a subhourly resolution) of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

The goal of this work is to develop energy efficiency and demand flexibility end-use load shapes that cover high-impact, market-ready (or nearly market-ready) measures. 'Measures' refers to various 'what-if' scenarios that can be applied to buildings.

An end-use savings shape is the difference in energy consumption between a baseline building (or collection of buildings) and a building with an energy efficiency or demand flexibility measure applied. It results in a time-series profile broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step, as well as annual aggregations.

This report describes the modeling methodology for a single end-use savings shape measure -chiller replacement -and briefly introduces key results. The full public dataset can be accessed on the ComStock™ data lake or via the Data Viewer at comstock.nrel.gov. The public dataset enables users to create custom aggregations of results for their use case (e.g., filter to a specific county).

Key modeling assumptions and technology details are summarized in Table ES-1.

| Technology Description   | • This study investigates replacing existing chillers (air-cooled and water- cooled) with new chillers that reflect the latest performance (i.e., average of medium- to high-performance chillers) in the current market. Also, variable speed pumps and chilled/condenser water temperature resets are applied if not available.   |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Performance Assumptions  | • Manufacturer data are gathered from public resources (e.g., manufacturer websites), processed to derive average full-load performances (e.g., full- load energy efficiency ratio [EER]) between configurations (e.g., air-cooled versus water-cooled), and applied to building models with chillers.                              |
|                          | • Part-load performances (e.g., Integrated Part-Load Value [IPLV] EER) of chillers are also derived from manufacturer data and used in a software tool (i.e., Copper) to create EnergyPlus ® -compatible performance maps.                                                                                                          |
|                          | • Data collected for air-cooled chillers cover (1) cooling tonnage between 11 and 547, (2) full-load EER between 9 and 15, and (3) IPLV EER between 13 and 23.                                                                                                                                                                      |
|                          | • Data collected for water-cooled chillers cover (1) cooling tonnage between 30 and 4,000, (2) full-load EER between 15 and 25, and (3) IPLV EER between 20 and 25.                                                                                                                                                                 |
|                          | • These data are collected from public resources (e.g., webpages) from six different manufacturers: Aermec, Carrier, Daikin, LG Electronics, Trane, and York.                                                                                                                                                                       |
| Applicability            | • Heating, ventilating, and air-conditioning systems including either air-cooled or water-cooled chillers.                                                                                                                                                                                                                          |
|                          | • 21% of the stock floor area.                                                                                                                                                                                                                                                                                                      |
| Release                  | 2025 Release 1: 2025/comstock_amy2018_release_1/                                                                                                                                                                                                                                                                                    |

National annual results for site energy, energy bills, and carbon emissions equivalent are summarized in Table ES-2 to Table ES-3.

Table ES-2. Key Results for Annual Site Energy Savings

| Fuel Type   |   Absolute Savings (TBtu) |   Baseline Total (All Buildings, TBtu) |   Percent Savings (All Buildings) |   Baseline Total (Applicable Buildings Only, TBtu) |   Percent Savings (Applicable Buildings Only) |
|-------------|---------------------------|----------------------------------------|-----------------------------------|----------------------------------------------------|-----------------------------------------------|
| Natural Gas |                      15.5 |                                 1524.1 |                               1.0 |                                              380.3 |                                           4.1 |
| Electricity |                      44.8 |                                 3173.4 |                               1.4 |                                              595.5 |                                           7.5 |

Table ES-3. Key Results for Annual Utility Cost Savings

| Fuel Type   |   Absolute Savings (Billion USD, 2022) |   Baseline Total (All Buildings, Billion USD, 2022) |   Percent Savings (All Buildings) |   Baseline Total (Applicable Buildings Only, Billion USD, 2022) |   Percent Savings (Applicable Buildings Only) |
|-------------|----------------------------------------|-----------------------------------------------------|-----------------------------------|-----------------------------------------------------------------|-----------------------------------------------|
| Natural Gas |                                    0.2 |                                                17.4 |                               1.2 |                                                             4.5 |                                           4.5 |
| Electricity |                                    1.7 |                                               107.7 |                               1.6 |                                                            20.1 |                                           8.4 |
| Fuel Oil    |                                    0.0 |                                                 0.7 |                               0.3 |                                                             0.1 |                                           2.7 |
| Propane     |                                    0.0 |                                                 1.0 |                               0.0 |                                                             0.0 |                                           0.0 |
| Total       |                                    1.9 |                                               126.8 |                               1.5 |                                                            24.6 |                                           7.7 |

Electricity cost savings in this table are calculated using the mean available electricity rate available for each building. Other electricity rate structures are available in this report and in the public dataset.

Table ES-4. Key Results for Annual Carbon Emissions Equivalent Savings

| Fuel Type   |   Absolute Savings (MMT CO 2 e) |   Baseline Total (All Buildings, MMT CO 2 e) |   Percent Savings (All Buildings) |   Baseline Total (Applicable Buildings Only, MMT CO 2 e) |   Percent Savings (Applicable Buildings Only) |
|-------------|---------------------------------|----------------------------------------------|-----------------------------------|----------------------------------------------------------|-----------------------------------------------|
| Natural Gas |                             1.0 |                                        101.8 |                               1.0 |                                                     25.4 |                                           4.1 |
| Electricity |                             3.1 |                                        239.6 |                               1.3 |                                                     42.1 |                                           7.4 |
| Fuel Oil    |                             0.0 |                                          1.7 |                               0.3 |                                                      0.2 |                                           2.7 |
| Propane     |                             0.0 |                                          2.7 |                               0.0 |                                                      0.0 |                                           0.0 |
| Total       |                             4.2 |                                        345.9 |                               1.2 |                                                     67.7 |                                           6.1 |

Electricity emissions avoided in this table are calculated using Cambium Long-Run Marginal Emissions Rate (LRMER) High Renewable Energy (RE) Cost 15-Year grid scenario. Other grid scenarios are presented in this report and in the public dataset.

While this report presents the impacts of various upgrade options (based on reduced stock models) for the overall chilled water system, the final results and dataset-representing the full stock models-include four specific upgrades: chiller replacement, chilled water temperature reset, condenser water temperature reset, and pump upgrades.

Upgrading to more efficient chillers-whether air-cooled or water-cooled-results in electricity savings, primarily through reduced chiller energy consumption. The bulk of these savings come from replacing older, less efficient units with newer models. Additionally, as chillers operate more efficiently, they reject less heat through the condenser, leading to reduced operation of cooling tower fans and, consequently, lower fan energy use. Improved pump motor efficiency and better control strategies, such as differential pressure reset, also contribute to overall energy reductions by optimizing pump power usage.

Another important benefit comes from strategies like chilled water supply temperature setpoint reset based on outdoor air temperature. By raising the chilled water supply temperature earlier in the day, chillers operate in more favorable part-load conditions, enhancing energy efficiency. However, this temperature increase reduces the temperature difference (∆T) between supply and return water, which in turn requires a higher flow rate to maintain the same cooling output. Despite this, systems with reheat capabilities-especially in multi-zone central air systems-see heating energy savings due to less reheat being required when the air temperature at the evaporator outlet is higher.

These efficiency measures not only benefit traditional variable air volume systems but also affect systems like fan coil units with dedicated outdoor air systems and water-source heat pumps, all of which rely on chillers. Because chillers typically serve large heating, ventilating, and airconditioning systems, the energy and operational improvements from this upgrade have a pronounced impact on large buildings such as hospitals, schools, and office buildings. Enhanced control settings that adapt to weather conditions further optimize heat rejection, contributing to additional cooling tower energy savings not always visible in standard performance figures.

