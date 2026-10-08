<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/87570.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/87570.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/87570.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/87570.md | section: Executive Summary | lines: 150-172 -->
## Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past 3 years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency, electrification, and demand flexibility enduse load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) measures. 'Measures' refers to energy efficiency variables that can be applied to buildings during modeling.

An end-use savings shape is the difference in energy consumption between a baseline building and a building with an energy efficiency, electrification, or demand flexibility measure applied. It results in a time-series profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

This documentation focuses on a single end-use savings shape measure-heat pump rooftop units (HP-RTUs) with supplemental heat that matches the original fuel type of the replaced system. If the existing system used electric resistance heating, the supplemental heating source is electric resistance. If the existing system used a natural gas furnace, the supplemental system is modeled as natural gas. This is a modification to the 'HP-RTU With Electric Supplemental Heat' measure from the Commercial End-Use Savings Shapes 2023 Release 1 data set. This document will primarily discuss the supplemental heating change for the HP-RTU measure. 0d of the HP-RTU measure, including performance curves and other key assumptions, please review the documentation for the original HP-RTU With Electric Supplemental Heat.

The HP-RTU measure replaces gas furnace and electric resistance rooftop units (RTUs) with high-efficiency HP-RTUs. The HP-RTUs are intended to be top-of-the-line, including highefficiency fans and heat pump systems. The fans are variable speed, allowing the HP-RTUs to operate as single-zone variable air volume systems. The heat pumps are also variable speed, allowing for high part load performance. The minimum temperature for heat pump operation is set to 0°F, and the units are sized based on the design cooling load, with supplemental heating addressing any remaining heating loads. For this version of the measure, the supplemental heating fuel type matches the fuel type of the system being replaced (electric resistance or gas furnace). All schedules in the existing RTUs are transferred to the new HP-RTUs for consistency. Furthermore, any energy efficiency features in the existing baseline RTUs, such as energy recovery or economizers, are also transferred to the new HP-RTUs for consistency. This measure is applicable to approximately 36% of the ComStock floor area.

The HP-RTU measure with original fuel supplemental heat demonstrates 8.5% total site energy savings (396 trillion British thermal units [TBtu]) for the U.S. commercial building stock modeled in ComStock (Figure 4). The savings are primarily attributed to:

- 27% stock heating gas savings (226 TBtu)
- -22% stock heating electricity savings (-43 TBtu)
- 11% stock cooling electricity savings (81 TBtu)
- 19% stock fan electricity savings (112 TBtu).

The HP-RTU measure demonstrates between 3.5 and 14.3 million metric tons (MMT) CO2 equivalent (CO2e) of greenhouse gas emissions avoided for the three grid electricity scenarios presented, as well as 15.1 MMT of greenhouse gas emissions avoided for on-site natural gas consumption.

