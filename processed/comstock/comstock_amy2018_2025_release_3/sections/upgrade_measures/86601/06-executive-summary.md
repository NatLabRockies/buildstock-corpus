<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86601.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86601.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86601.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/86601.md | section: Executive Summary | lines: 138-161 -->
## Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past 3 years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency, electrification, and demand flexibility enduse load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) upgrade measures, or upgrades. 'Measures' refers to energy efficiency variables that can be applied to buildings during modeling.

An end-use savings shape is the difference in energy consumption between a baseline building and a building with an energy efficiency, electrification, or demand flexibility upgrade applied. It results in a time-series profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

An upgrade package applies one or more End-Use Savings Shapes upgrades to a single building model simulation. Since ComStock is a bottom-up physics-based model, an upgrade package will go beyond aggregating or summing the individual upgrade results and produce novel results by simulating interactions between the upgrades. For example, pairing an envelope upgrade with an electrification upgrade would likely result in higher savings results than the sum of these upgrades individually, and the size of the heating, ventilating, and air conditioning (HVAC) equipment may be reduced if the envelope upgrade reduces the loads significantly.

This documentation focuses on an upgrade package of three End-Use Savings Shapes upgrades- Light Emitting Diode (LED) Lighting, Heat Pump Rooftop Unit (HP-RTU), and AirSource Heat Pump (ASHP) Boiler, which we will refer to collectively as the 'Interior Lighting and Heat Pump' package. HP-RTUs are applied to buildings with gas or electric RTUs, while the HP Boiler measure is applied to buildings with existing boilers systems. They are not applied together in this study. More details on the individual upgrades can be found on the ComStock Measures Documentation page. This combination of measures was selected to model together because both LEDs and HPs are commercially available products and common energy efficiency and electrification measures.

The LED Lighting, HP-RTU and HP Boiler measures were applicable to 65%, 36%, and 33% of the stock floor area, respectively, resulting in the Interior Lighting and Heat Pump package being applicable to 89% of the total stock floor area. This package demonstrates 19.9% total site energy savings (922 trillion British thermal units [TBtu]) for the U.S. commercial building stock modeled in ComStock (Figure 3). The savings are primarily attributed to:

- 94.2% stock heating gas savings (778.5 TBtu)
- -132% stock heating electricity savings (-260.7 TBtu).
- 36.5% stock interior lighting electricity savings (164.9 TBtu)
- 20.1% stock fan electricity savings (118.8 TBtu)
- 14.3% stock cooling electricity savings (104 TBtu).

The Interior Lighting and Heat Pump package demonstrates between -1.9 and 10.7 million metric tons (MMT CO2e) of greenhouse gas emissions avoided for the three grid electricity scenarios presented, as well as 52.1 MMT CO2e of greenhouse gas emissions avoided for on-site natural gas consumption.

