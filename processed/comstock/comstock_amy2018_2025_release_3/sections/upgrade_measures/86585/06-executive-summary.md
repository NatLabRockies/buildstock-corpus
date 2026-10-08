<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86585.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86585.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86585.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/86585.md | section: Executive Summary | lines: 130-152 -->
## Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past 3 years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency, electrification, and demand flexibility enduse load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) measures. 'Measures' refers to energy efficiency variables that can be applied to buildings during modeling.

An end-use savings shape is the difference in energy consumption between a baseline building and a building with an energy efficiency, electrification, or demand flexibility measure applied. It results in a time-series profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

This documentation focuses on a single end-use savings shape measure-heat pump rooftop units.

The heat pump rooftop units (RTUs) measure replaces gas furnace and electric resistance RTUs with high-efficiency heat pump rooftop units (HP-RTUs). The HP-RTUs are intended to be topof-the line, including high-efficiency fans and heat pump systems. The fans are variable speed, allowing the HP-RTUs to operate as single-zone variable air volume systems. The heat pumps are also variable speed, allowing for high part load performance. All schedules in the existing RTUs are transferred to the new HP-RTUs for consistency. Furthermore, any energy efficiency features in the existing baseline RTUs such as energy recovery or economizers are also transferred to the new HP-RTUs for consistency. This measure is applicable to approximately 45% of the ComStock floor area.

The HP-RTU measure demonstrates 10.3% total site energy savings (449 trillion British thermal units [TBtu]) for the U.S. commercial building stock modeled in ComStock (Figure 10). The savings are primarily attributed to:

- 42% stock heating gas savings (190 TBtu)
- -3% stock heating electricity savings ( -6 TBtu)
- 16% stock cooling electricity savings (109 TBtu)
- 24% stock fan electricity savings (144 TBtu)

The HP-RTU measure demonstrates between 19 and 28 million metric tons (MMT) of greenhouse gas emissions avoided for the three grid electricity scenarios presented, as well as 13 MMT of greenhouse gas emissions avoided for on-site natural gas consumption.

