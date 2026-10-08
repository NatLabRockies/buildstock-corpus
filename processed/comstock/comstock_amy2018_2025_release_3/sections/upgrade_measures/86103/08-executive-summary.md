<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86103.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/86103.md | section: Executive Summary | lines: 87-113 -->
## Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past 3 years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency, electrification, and demand flexibility enduse load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) measures. 'Measures' refers to energy efficiency variables that can be applied to buildings during modeling.

An end-use savings shape is the difference in energy consumption between a baseline building and a building with an energy efficiency, electrification, or demand flexibility measure applied. It results in a time-series profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

This documentation focuses on a single heating, ventilation, and air-conditioning (HVAC) enduse savings shape measure-a variable refrigerant flow with heat recovery (VRF HR) heating and cooling system coupled with a dedicated outdoor air system (DOAS) for ventilation.

This measure replaces existing multizone variable air volume (VAV) systems or single-zone rooftop units (RTU) with a VRF HR system coupled with a DOAS that includes an energy/heat recovery ventilator (E/HRV). The VRF HR system is a heat pump system that employs variable speed compressors. Typically, this system involves a single outdoor unit connected to multiple indoor units and independently controlling refrigerant flow to each indoor unit.

A DOAS, 100% outdoor air ventilation system, with an E/HRV is used to provide required outside air to spaces since ventilation air is generally not supplied by a VRF HR system. An exhaust air energy recovery ventilator (ERV) with sensible and latent heat exchange is added to humid climates, while a heat recovery ventilator (HRV) with sensible-only exchange is added to drier climates. The ERV is modeled as a fixed membrane plate counterflow heat exchanger, and the HRV is modeled as a sensible-only fixed aluminum plate counterflow heat exchanger. Both systems include a bypass (for temperature control and economizer lockout) and minimum exhaust temperature control for frost prevention.

The measure covers 53% of the existing building stock's floor area and is not applicable to HVAC system types using district heating or cooling, or buildings/spaces that include highventilation spaces such as kitchens where the amount of exhaust air is large. The VRF (HR) with DOAS measure demonstrates 16% total site energy savings (729 trillion British thermal units

[TBtu]) for the U.S. commercial building stock modeled in ComStock (Figure 14). The savings are primarily attributed to:

- 18% stock cooling electricity savings (128 TBtu)
- 53% stock heating natural gas savings (438 TBtu)
- 30% stock fan electricity savings (178 TBtu)
- -24% stock heating electricity savings (-48 TBtu).

The VRF (HR) with DOAS measure demonstrates between 41 (16% reduction for LRMER Low RE Cost 15 scenario) and 56 (13% reduction for eGRID 2021 scenario) million metric tons (MMT) of greenhouse gas emissions avoided (from all fuel types) for the three grid electricity scenarios presented.

