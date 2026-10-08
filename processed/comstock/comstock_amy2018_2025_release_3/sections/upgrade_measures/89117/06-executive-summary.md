<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89117.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89117.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89117.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/89117.md | section: Executive Summary | lines: 114-133 -->
## Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past 3 years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency, electrification, and demand flexibility enduse load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) measures. 'Measures' refers to energy efficiency variables that can be applied to buildings during modeling.

An end-use savings shape is the difference in energy consumption between a baseline building and a building with an energy efficiency, electrification, or demand flexibility measure applied. It results in a time-series profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

This documentation focuses on a single end-use savings shape measure-advanced rooftop unit control. This measure implements variable-speed control of rooftop unit (RTU) fans that are currently constant-speed, and includes options for demand-controlled ventilation and air-side economizing. These features are like the functions offered by advanced rooftop unit control (ARC) retrofit kits. This measure is expected to result in fan energy savings from the multi-speed fan control, fan savings from demand-controlled ventilation, and cooling energy savings economizing, respectively. This measure is applicable to about 39% of the floor area modeled in ComStock.

The Advanced RTU Control measure demonstrates 4.2% total site energy savings (182 trillion British thermal units [TBtu]) for the U.S. commercial building stock modeled in ComStock (Figure 8). The savings are primarily attributed to:

- 26% stock fan electricity savings (137 TBtu)
- 4% stock cooling electricity savings (24 TBtu)
- 2% stock heating gas savings (18 TBtu).

The Advanced RTU Control measure demonstrates between 7 and 17 million metric tons (MMT) of greenhouse gas emissions avoided for the three grid electricity scenarios presented, as well as one MMT of greenhouse gas emissions avoided for on-site natural gas consumption. This constitutes a reduction in greenhouse gas emissions of 4% across all grid scenarios. The levels of energy savings by end use in applicable buildings are in line with past modeling and field studies of ARC.

