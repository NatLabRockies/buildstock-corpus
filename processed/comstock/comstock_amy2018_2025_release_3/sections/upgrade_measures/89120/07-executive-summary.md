<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89120.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89120.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89120.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/89120.md | section: Executive Summary | lines: 70-96 -->
## Executive Summary

Building on the successful effort to calibrate and validate the U.S. Department of Energy's ResStock ™  and ComStock models over the past 3 years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency, electrification, and demand flexibility enduse load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) measures. 'Measures' refers to energy efficiency variables that can be applied to buildings during modeling.

An end-use savings shape is the difference in energy consumption between a baseline building and a building with an energy efficiency, electrification, or demand flexibility measure applied. It results in a time-series profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles (https://www.nrel.gov/buildings/end-use-load-profiles.html) project.

This documentation focuses on a single end-use savings shape measure-Improved Fan Scheduling and Unoccupied Outdoor Air Control.

This measure shuts off outdoor air supply for ventilation during periods when buildings are unoccupied for an extended time (i.e., overnight), as well as aligning fan operating schedules with the occupancy of the zones that the fans serve. Air-side economizing can still take place, but no minimum outdoor air requirement is enforced. This saves energy through reduction in fan speed and the avoidance of thermal loads to condition outdoor air. This measure is applicable to air handling unit (AHU)-based systems that do not currently have ventilation scheduled off during unoccupied times.

Note that some buildings with ventilation scheduled off at night in their primary heating, ventilating, and air conditioning (HVAC) systems have dedicated systems serving other spaces (such as data centers) that have constant schedules applied to their minimum outdoor air levels. These secondary system schedules were changed to reflect building occupancy as part of this measure, but because the minimum outdoor air levels for these spaces was generally set to zero, this schedule change did not affect actual operations and produced only a minor (&lt;0.01%) change in site energy use.

The Improved Fan Scheduling and Outdoor Air Control measure demonstrates 3.5% total site energy savings (150 TBtu) for the U.S. commercial building stock modeled in ComStock (Figure 4). The savings are primarily attributed to:

- 5.6% stock heating gas savings (50 TBtu)

- 3.3% stock cooling electricity savings (24 TBtu)
- 14.5% stock fan electricity savings (87 TBtu).

The Improved Fan Scheduling and Outdoor Air Control measure demonstrates between 7 and 9 MMT of greenhouse gas emissions avoided for the three grid electricity scenarios presented, as well as 3 MMT of greenhouse gas emissions avoided for on-site natural gas consumption. This constitutes a reduction in greenhouse gas emissions of 3%-4% depending on the scenario.

Energy savings associated with this measure are highly dependent on baseline conditions regarding AHU scheduling and outdoor air control.

