<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89131.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89131.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89131.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/89131.md | section: Executive Summary | lines: 79-102 -->
## Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past 3 years, the objective of this work is to produce national datasets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency, electrification, and demand flexibility enduse load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) measures.

An end-use savings shape is the difference in energy consumption between a baseline building and a building with an energy efficiency, electrification, or demand flexibility measure applied. It results in a time series profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual sub-hourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018.

This documentation focuses on a single measure, involving the retrofit of single-zone packaged rooftop units with packaged rooftop water-to-air geothermal heat pumps (GHP), tied to a common condenser loop coupled with a ground heat exchanger. Rooftop units are the most prominent commercial building heating, ventilating, and air-conditioning system type and therefore should be prioritized for decarbonization solutions. Additional energy efficiency measures, including the enhancement of air-side economizing, demand-controlled ventilation, and the implementation of energy recovery ventilators, can also be considered in conjunction with this retrofit. This measure is applicable to approximately 45% of the ComStock floor area.

The Packaged GHP upgrade demonstrates 11.7% total site energy savings (507 trillion British thermal units [TBtu]) for the U.S. commercial building stock modeled in ComStock (Figure 7). For applicable buildings only, the total site energy savings was 20.6%. The measure was successfully applied to 56% of the ComStock floor area. The measure replaces all PSZ and packaged VAV systems with packaged GHPs, resulting in changes to several HVAC end uses:

| End Use   | Percent Savings (All Buildings)   |   Percent Savings (Applicable Buildings Only) | Absolute Savings (TBtu)   |
|-----------|-----------------------------------|-----------------------------------------------|---------------------------|
| 53.2%     | 89.6%                             |                                         455.2 | Heating Natural Gas       |
| -43.2%    | -62.5%                            |                                         -75.6 | Heating Electricity       |
| 19.9%     | 36.8%                             |                                         132.6 | Cooling Electricity       |
| -58.9%    | -2281.8%                          |                                         -25.1 | Pump Electricity          |
| -4.3%     | -6.8%                             |                                         -22.4 | Fan Electricity           |

Three electricity grid scenarios are presented to compare the emissions of the ComStock baseline and the Packaged GHP measure. Two scenarios-Long-Run Marginal Emissions Rate (LRMER) High Renewable Energy (RE) Cost 15-Year and LRMER Low RE Cost 15-Year-use the Cambium data set, and the last uses the Emissions &amp; Generation Resource Integrated Database (eGRID) data set [1], [2]. Across the three electricity grid scenarios presented, electricity emissions increased by 0.6-5.9% (2-9 MMT CO2e). Natural gas emissions decreased by 38.3% (31 MMT CO2e), resulting in an overall reduction in greenhouse gas emissions across all fuel types of 8-10% (25-32 MMT CO2e) depending on the grid scenario.

