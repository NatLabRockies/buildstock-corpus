<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95013.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95013.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95013.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/95013.md | section: Executive Summary | lines: 60-110 -->
## Executive Summary

Building on a three-year effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models, this work produces national datasets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of questions regarding their commercial building stock.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

The goal of this work is to develop energy efficiency and demand flexibility end-use load shapes that cover high-impact, market-ready (or nearly market-ready) measures. Measures refer to various 'what-if' scenarios that can be applied to buildings.

An end-use savings shape is the difference in energy consumption between a baseline building (or collection of buildings) and a building with an energy efficiency or demand flexibility measure applied. It results in a time-series profile broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step as well as annual aggregations.

This report describes an upgrade package of three ComStock measures-thermostat control for load shedding, lighting control for load shedding, and photovoltaics (PV) with 40% rooftop coverage-and briefly introduces key results. The full public dataset can be accessed on the ComStock data lake or via the Data Viewer at comstock.nrel.gov. The public dataset enables users to create custom aggregations of results for their use case (e.g., filter to a specific county).

Key modeling assumptions and technology details are summarized in Table ES-1. More details on the individual upgrades can be found on the ComStock upgrade measures webpage.

Table ES-1. Summary of Key Modeling Specifications

| Package Title           | Thermostat and Lighting Control for Load Shedding + PV With 40% Rooftop Coverage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Technology description  | • This package combines three measure scenarios: thermostat control for load shedding, lighting control for load shedding, and PV with 40% rooftop coverage. It relaxes thermostat set points (heating and cooling) and reduces lighting levels to reduce the building's daily electricity peak demand during demand flexibility events, and it installs PV on the rooftop covering 40% of the roof area for on-site power generation.                                                                                                                                                                |
| Performance assumptions | peak loads. • The thermostat set points are adjusted - 2°C and +2°C for heating and cooling, respectively, for the dispatch window and the ramp back to the original set points over two hours after the window for rebound control. • The lighting level (the corresponding power) is reduced 30% for the dispatch window, and it resumes to the original value after the window. • Control decisions of the two measures are made independently, without considering the integration of the HVAC and lighting systems (e.g., internal heat gain from lighting equipment impacting HVAC operations). |
| Applicability           | • The individual measures share the same applicability for building types, which cover large, medium, and small offices; warehouses; and primary and secondary schools.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Applicability           | • The thermostat control measure is applicable electric HVAC (electric heating or cooling or both) systems, which corresponds to 67.26% of the stock floor area.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Release                 | • 2025 Release 1: 2025/comstock_amy2018_release_1/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

National annual results for site energy, energy bills, and demand flexibility are summarized in Table ES-2 to Table ES-4. Note that the summary table for energy bills uses one of many respective scenarios. Other scenarios are discussed later in the report, with further scenarios available in the ComStock public dataset.

Table ES-2. Summary of Key Results for Annual Site Energy Savings

| Fuel Type   | Percent Savings (All Buildings)   | Percent Savings (Applicable Buildings Only)   |   Absolute Savings (trillion British thermal units [TBtu]) |
|-------------|-----------------------------------|-----------------------------------------------|------------------------------------------------------------|
| Natural gas | -0.32%                            | -0.75%                                        |                                                       -4.9 |
| Electricity | 19.88%                            | 39.64%                                        |                                                      630.0 |

Table ES-3. Summary of Key Results for Annual Utility Bill Savings

Electricity bill savings in this table are calculated using the mean available electricity rate available for each building. Other electricity rate structures are available in this report and in the public dataset. Bill savings summary is present with individual peak load reduction objective.

| End Use/ Fuel Type   | Percent Savings (All Buildings)   | Percent Savings (Applicable Buildings Only)   |   Absolute Savings (Million USD, 2022) |
|----------------------|-----------------------------------|-----------------------------------------------|----------------------------------------|
| Electricity          | 18.5%                             | 35.5%                                         |                                     20 |
| Natural gas          | 0.0%                              | 0.0%                                          |                                      0 |
| Fuel oil             | 0.0%                              | 0.0%                                          |                                      0 |
| Propane              | 0.0%                              | 0.0%                                          |                                      0 |
| Total                | 15.7%                             | 30.7%                                         |                                     20 |

Table ES-4. Summary of Key Results for Monthly Peak Savings

| Median Percent Savings (Applicable Buildings Only)   | Jan.   | Feb.   | March   | April   | May   | June   | July   | Aug.   | Sept.   | Oct.   | Nov.   | Dec. 12.6%   |
|------------------------------------------------------|--------|--------|---------|---------|-------|--------|--------|--------|---------|--------|--------|--------------|
| Mean Daily Peak of the Month                         | 13.1%  | 15.4%  | 17.5%   | 22.9%   | 30.6% | 30.6%  | 31.8%  | 29.8%  | 25.3%   | 19.7%  | 14.6%  |              |

