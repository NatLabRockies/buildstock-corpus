<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86599.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86599.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86599.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/86599.md | section: Executive Summary | lines: 64-86 -->
## Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past 3 years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency, electrification, and demand flexibility enduse load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) upgrade measures, or upgrades. 'Measures' refers to energy efficiency variables that can be applied to buildings during modeling.

An end-use savings shape is the difference in energy consumption between a baseline building and a building with an energy efficiency, electrification, or demand flexibility upgrade applied. It results in a time-series profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

An upgrade package applies one or more End-Use Savings Shapes upgrades to a single building model simulation. Because ComStock is a bottom-up physics-based model, an upgrade package will go beyond aggregating or summing the individual upgrade results and produce novel results by simulating interactions between the upgrades. For example, pairing an envelope upgrade with an electrification upgrade would likely result in higher savings results than the sum of these upgrades individually, and the size of the heating, ventilating, and air conditioning (HVAC) equipment may be reduced if the envelope upgrade reduces the loads significantly.

This documentation focuses on an upgrade package of three end-use savings shapes upgradesWindow Replacement, Exterior Wall Insulation, and Roof Insulation, which we will refer to collectively as the 'High-Efficiency Envelope' package. Depending on applicability criteria, this package will upgrade window, wall, and roof thermal properties to align with those specified in ASHRAE's Advanced Energy Design Guide (AEDG), respective of the model's particular climate zone. More details on the individual upgrades can be found on the ComStock Measures Documentation page.

The High-Efficiency Envelope upgrade package is applicable to 100% of the total stock floor area, meaning one or more of the measures are applicable to all buildings in the stock. The package demonstrates 7.2% total site energy savings (332 trillion British thermal units [TBtu]) for the U.S. commercial building stock modeled in ComStock (Figure 2). The savings are primarily attributed to natural gas heating and electricity cooling due to wall and roof insulation improvements and reduced heat gain through windows:

- 17.6% stock heating gas savings (146 TBtu)
- 22.5% stock heating electricity savings (44.3 TBtu)
- 11.7% stock cooling electricity savings (84.8 TBtu)
- 3.6% stock fan electricity savings (21.1 TBtu).

The High-Efficiency Envelope package demonstrates between 7.9 and 16.9 million metric tons (CO2e) of greenhouse gas emissions avoided for the three grid electricity scenarios presented, as well as 9.8 million metric tons of greenhouse gas emissions avoided for on-site natural gas consumption.

