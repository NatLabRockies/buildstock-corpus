<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_roof_insulation.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_roof_insulation.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_roof_insulation.html | corpus_version: fadc83e | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_roof_insulation.md | section: Roof Insulation | lines: 2-25 -->
# Roof Insulation

Authors: Lauren Adams and Chris CaraDonna

# Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy’s ResStock™ and ComStock™ models over the past three years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency and demand flexibility end-use load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) measures. “Measures” refers to energy efficiency variables that can be applied to buildings during modeling.

An *end-use savings shape* is the difference in energy consumption between a baseline building and a building with an energy efficiency or demand flexibility measure applied. It results in a timeseries profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each timestep.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the [End-Use Load Profiles](https://www.nlr.gov/buildings/end-use-load-profiles.html) project.

This documentation focuses on a single end-use savings shape measure—roof insulation. The roof insulation measure increases the building model’s roof insulation R-value to align with those specified in ASHRAE’s *Advanced Energy Design Guide* (AEDG), respective of the model’s particular climate zone. This could represent either replacing a building’s roof insulation completely or adding additional insulation. The insulation added to achieve the target value is rounded up to the nearest inch to better represent the options for which insulation products, such as extruded polystyrene, are typically sold. This measure is only applicable to roof surfaces with insulation R-values below the AEDG target values and does not impact roof insulation that already meets or exceeds these targets. For this ComStock analysis, the roof insulation measure was applicable to \>99% of buildings, suggesting that most commercial building are not already meeting the AEDG targets.

The roof insulation measure demonstrates 3% (112 TBtu) aggregate site energy savings, combined for all fuel types, across the modeled U.S. commercial building stock. The savings are primarily attributed to:

-   11% (50 TBtu) natural gas heating site energy savings
-   12% (28 TBtu) electricity heating site energy savings
-   3% (21 TBtu) electricity cooling site energy savings
-   1% (5 TBtu) electricity fan site energy savings.

# 1.  Roof Insulation
