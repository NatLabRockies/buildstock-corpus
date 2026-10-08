<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89130.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89130.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89130.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/89130.md | section: Executive Summary | lines: 71-91 -->
## Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past three years, the objective of this work is to produce national datasets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency, electrification, and demand flexibility enduse load shapes (electricity, gas, propane, or fuel oil) that cover most of the high-impact, marketready (or nearly market-ready) measures. 'Measures' refers to energy efficiency variables that can be applied to buildings during modeling.

An end-use savings shape is the difference in energy consumption between a baseline building and a building with an energy efficiency, electrification, or demand flexibility measure applied. It results in a time series profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual sub-hourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

This documentation focuses on a single end-use savings shape measure-Electric Cooking Equipment. This measure replaces gas-fired commercial cooking equipment with electric equipment where applicable. The cooking appliances modified in this measure include broilers, fryers, griddles, ovens, ranges, and steamers. The scope of this study does not include commercial dishwashing equipment. This measure only affects ComStock building types with kitchens. This includes hospitals, large hotels, schools, strip malls, and restaurants.

This measure was applicable to 37.5% of the ComStock floor area. This measure demonstrates 2.0% total site energy savings (86 TBtu) for the U.S. commercial building stock modeled in ComStock (Figure 10). The savings are primarily attributed to:

- 88.2% stock interior equipment, natural gas savings (187.0 TBtu)
- -14.1% stock interior equipment, electricity savings ( -104.1 TBtu)
- -0.2% stock natural gas heating savings ( -1.7 TBtu)
- 0.6% stock cooling electricity savings (4.1 TBtu).

Three electricity grid scenarios are presented to compare the emissions of the ComStock baseline and the Electric Cooking Equipment upgrade. Two scenarios-Long-Run Marginal Emissions Rate (LRMER) High Renewable Energy (RE) Cost 15-Year and LRMER Low RE Cost 15Year-use the Cambium data set, and the last uses the Emissions &amp; Generation Resource Integrated Database (eGRID) data set [1], [2]. Across the three electricity grid scenarios presented, electricity emissions increased by 2.6-3.5% (4-11 MMT CO2e), while natural gas emissions dropped by 14.8% (12 MMT CO2e), resulting in an overall greenhouse gas emissions reduction across all fuel types of 0.5-3.3% depending on grid scenarios.

