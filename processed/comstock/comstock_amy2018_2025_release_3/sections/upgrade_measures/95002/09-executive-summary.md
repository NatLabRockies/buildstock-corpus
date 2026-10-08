<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95002.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95002.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95002.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/95002.md | section: Executive Summary | lines: 64-96 -->
## Executive Summary

Building on the 3-year effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models, this work produces national datasets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of questions regarding their commercial building stock.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model represents the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

The goal of this work is to develop energy efficiency and demand flexibility end-use load shapes that cover high-impact, market-ready (or nearly market-ready) measures. 'Measures' refers to various 'what-if' scenarios that can be applied to buildings.

An end-use savings shape is the difference in energy consumption between a baseline building (or collection of buildings) and a building with an energy efficiency or demand flexibility measure applied. It results in a time-series profile broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step, as well as annual aggregations.

This report describes the modeling methodology for a single measure scenario-Reduced Thermostat Setbacks for Heat Pumps-and briefly introduces key results. The full public dataset can be accessed on the ComStock data lake or via the Data Viewer at comstock.nrel.gov. The public dataset enables users to create custom aggregations of results for their use case (e.g., filter to a specific county).

Key modeling assumptions and technology details are summarized in Table ES-1.

Table ES-1. Summary of Key Modeling Specifications

| Technology Description   | • This measure scenario couples a 2°F unoccupied thermostat setback with the Heat Pump Rooftop Unit measure. • The intent is to implement more mild thermostat setbacks when using heat pumps,   |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Performance Assumptions  | • Measure will be applied in conjunction with the Standard Performance Heat Pump Rooftop Unit measures • A setback of 2°F will be implemented during unoccupied periods, which is generally      |
| Applicability            | • Applied to buildings eligible for the Standard Performance Heat Pump Rooftop Unit                                                                                                              |
|                          | measure (36%).                                                                                                                                                                                   |
| Release                  | 2025 Release 1: 2025/comstock_amy2018_release_1                                                                                                                                                  |

National annual results for site energy, energy bills, and carbon emissions equivalent (CO2e) are summarized in Table ES-2-Table ES-4.

Table ES-2. Summary of Key Results for Annual Site Energy Savings

| Fuel Type   |   Absolute Savings (TBtu) |   Baseline Total (All Buildings, TBtu) | Percent Savings (All Buildings)   | Baseline Total (Applicable Buildings Only,   | Percent Savings (Applicable   |
|-------------|---------------------------|----------------------------------------|-----------------------------------|----------------------------------------------|-------------------------------|
|             |                           |                                        |                                   | TBtu)                                        | Buildings Only)               |
| Natural gas |                     320.0 |                                 1524.1 | 20.1%                             | 627.4                                        | 51.0%                         |
| Electricity |                      -0.3 |                                 3173.4 | 0.0%                              | 1219.9                                       | -1.7%                         |

