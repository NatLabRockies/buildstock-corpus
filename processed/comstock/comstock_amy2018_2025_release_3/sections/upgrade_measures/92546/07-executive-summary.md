<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/92546.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/92546.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/92546.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/92546.md | section: Executive Summary | lines: 52-72 -->
## Executive Summary

Building on a 3-year effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models, the ComStock Standard Dataset Release produces national datasets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of questions regarding their commercial building stock.

The goal of this work is to develop energy efficiency and demand flexibility end-use load shapes that cover high-impact, market-ready (or nearly market-ready) measures. 'Measures' refers to various 'what-if' scenarios that can be applied to buildings.

An end-use savings shape is the difference in energy consumption between a baseline building (or collection of buildings) and a building in which an energy efficiency or demand flexibility measure has been applied. The result is a time-series profile broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step, as well as annual aggregates.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project and the ComStock Reference Documentation.

This report describes the modeling methodology for a single end-use savings shape measureIdeal Thermal Air Loads-and briefly presents key results. The full public dataset can be accessed on the ComStock™ data lake or via the Data Viewer at comstock.nrel.gov. The public dataset enables users to create custom aggregations of results for their use case (e.g., filter to a specific county).

Key modeling assumptions and technology details are summarized in Table 1.

Table 1 . Summary of Key Modeling Specifications

| Technology Description   | • This study provides hypothetical thermal heating and cooling loads for ComStock models representing the U.S. commercial building stock. This measure scenario removes all HVAC models from the baseline ComStock building model and instead uses 'ideal air' to meet loads.                                                                                              |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                          | • 'Ideal air' functions like an HVAC unit that mixes zone exhaust air with the required outdoor air, then adjusts heat and moisture with 100% efficiency to provide supply air at the desired conditions.                                                                                                                                                                  |
|                          | • The resulting ideal thermal loads are represented under the 'district' fuel type for both heating and cooling and can be found in both annual and time-series results in the ComStock public dataset. This measure scenario does not represent any real technology or improvement, but rather, serves as a resource for thermal heating and cooling loads for buildings. |

