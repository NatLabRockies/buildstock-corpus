<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89481.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89481.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89481.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89481.md | section: Executive Summary | lines: 108-133 -->
## Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past several years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency, electrification, and demand flexibility enduse load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) measures. 'Measures' refers to energy efficiency, load flexibility, and electrification strategies that can be applied to buildings during modeling.

An end-use savings shape is the difference in energy consumption between a set of baseline buildings and a building(s) with an energy efficiency, electrification, or demand flexibility measure applied. It results in a time-series profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

This documentation focuses on a package of two end-use savings shape measures-Heat Pump Rooftop Unit (HP-RTU) and Exhaust Air Heat/Energy Recovery. This study combines the modeling methodologies from the 'HP-RTU With Electric Supplemental Heat' measure from the Commercial End-Use Savings Shapes 2023 Release 1 data set and the 'Add Exhaust Air Heat/Energy Recovery' measure from the 2023 Release 2 data set. This document will primarily discuss the addition of heat/energy recovery to the HP-RTU system. For a more comprehensive understanding of the background and modeling methodology of the HP-RTU or Heat/Energy Recovery measures, please refer to the respective documents dedicated to each measure.

This measure replaces gas furnace and electric resistance rooftop units with high-efficiency variable-speed HP-RTUs that include exhaust air heat or energy recovery. Energy recovery with sensible and latent exchange gets added in humid climate zones, whereas heat recovery with sensible-only exchange gets added in drier climate zones. Energy recovery is modeled as a fixed membrane plate counterflow heat exchanger, and heat recovery is modeled as a sensible-only fixed aluminum plate counterflow heat exchanger. Both systems include a bypass (for temperature control and economizer lockout) and minimum exhaust air temperature control for frost prevention.

The measure uses the same assumptions and technology as the variable-speed HP-RTU measure from the End-Use Savings Shapes 2023 release 1, but adds energy recovery to precondition outdoor ventilation air to reduce HVAC loads. The HP-RTU compressor lockout temperature is modeled as 0°F; below this temperature, the heat pump is set to shut off. The unit is sized based on the design cooling loads, with backup electric resistance heating addressing any remaining loads including heating hours below the compressor lockout temperature when there is no heat pump heating.

The HP-RTU with heat/energy recovery measure is applicable to buildings comprising 33% of the stock floor area and demonstrates 9% total site energy savings (382 trillion British thermal units [TBtu]) for the U.S. commercial building stock modeled in ComStock. The savings are primarily attributed to:

- 28% stock heating gas savings (235 TBtu)
- -22% stock heating electricity savings (-39 TBtu)
- 13% stock cooling electricity savings (85 TBtu)
- 15% stock fan + heat recovery savings (81 TBtu)
- o Fan static pressure increases due to heat/energy recovery are categorized under the 'heat recovery' end use.

The HP-RTU with heat/energy recovery measure shows 7%-9% annual greenhouse gas emissions avoided (219 to 372 MMT CO2e) against the baseline building stock depending on the electricity grid scenario.

