<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86897.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86897.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86897.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/86897.md | section: Executive Summary | lines: 106-126 -->
## Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past 3 years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency, electrification, and demand flexibility enduse load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) measures. 'Measures' refers to energy efficiency variables that can be applied to buildings during modeling.

An end-use savings shape is the difference in energy consumption between a baseline building and a building with an energy efficiency, electrification, or demand flexibility measure applied. It results in a time-series profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

This documentation focuses on a single end-use savings shape measure-demand control ventilation (DCV). DCV can save energy by reducing the rate at which outdoor air is delivered during periods of less-than-design occupancy. This measure will enable DCV for air loops using applicable HVAC system types (all except dedicated outdoor air systems [DOAS], packaged systems, or that have an energy recovery ventilator [ERV]) and serving applicable space types (all except kitchens, dining areas, patient spaces, mechanical rooms, stairwells and corridors, or high exhaust space types) using model occupancy schedules to control the DCV. The measure is applicable to approximately 73% of the stock floor area. As office buildings in ComStock are modeled using a single, whole-building space type, DCV is not applied to these building types.

The DCV measure demonstrates 2.6% total site energy savings (119 trillion British thermal units [TBtu]) for the U.S. commercial building stock modeled in ComStock (Figure 1). The savings are primarily attributed to:

- 8.8% stock heating gas savings (72.5 TBtu)
- 9.3% stock heating electricity savings (18.3 TBtu)
- 2.1% stock cooling electricity savings (15.2 TBtu)
- 0.1% stock fan electricity savings (0.7 TBtu).

The DCV measure demonstrates between 2.0 and 3.8 million metric tons (MMT CO2e) of greenhouse gas emissions avoided for the three grid electricity scenarios presented, as well as 4.9 MMT CO2e of greenhouse gas emissions avoided for on-site natural gas consumption.

