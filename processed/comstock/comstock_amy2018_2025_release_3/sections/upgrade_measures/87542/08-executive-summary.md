<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/87542.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/87542.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/87542.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/87542.md | section: Executive Summary | lines: 174-197 -->
## Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past 3 years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency, electrification, and demand flexibility enduse load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) measures. 'Measures' refers to energy efficiency variables that can be applied to buildings during modeling.

An end-use savings shape is the difference in energy consumption between a baseline building and a building with an energy efficiency, electrification, or demand flexibility measure applied. It results in a time-series profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

This documentation focuses on a single end-use savings shape measure-adding exhaust air heat/energy recovery. This measure adds exhaust air energy recovery or heat recovery to existing air handling units (AHUs) with outdoor air. Systems that already have energy/heat recovery are not modified. Food service building types are also not modified by this measure due to the added complication of integrating cooking hood exhaust, which could cause heat exchanger fouling. In total, this measure is applicable to airloops serving ~70% of the floor area in ComStock. In practice, energy/heat recovery systems can be retrofitted to existing air delivery systems by including them as separate systems that provide outdoor air to the AHUs or by directly integrating them into an AHU; the modeling approach used in this study is agnostic of the energy recovery implementation method and simply accounts for recovery effectiveness, added static pressure, and other controls, which are described further in this document. Energy recovery with sensible and latent exchange gets added in humid climate zones, whereas heat recovery with sensible-only exchange gets added in drier climate zones. Energy recovery is modeled as a fixed membrane plate counterflow heat exchanger, and heat recovery is modeled as a sensible-only fixed aluminum plate counterflow heat exchanger. Both systems include a bypass (for temperature control and economizer lockout) and an electric resistance preheat coil for frost prevention.

The heat/energy recovery measure demonstrates 7% total site energy savings (304 trillion British thermal units [TBtu]) for the U.S. commercial building stock modeled in ComStock. The savings are primarily attributed to:

- 23% stock heating savings (268 TBtu)

- 10% stock cooling savings (82 TBtu)
- -8% stock combined fan and heat recovery savings ( -46 TBtu)
- o Note that the heat recovery end use includes the additional fan energy associated with the static pressure increase of the new energy recovery systems, plus the fan energy and motor power associated with the energy recovery systems and enthalpy wheels in the existing building stock.

Comprehensive greenhouse gas emissions avoided (one electricity grid scenario plus all on-site combustion fuels) range between 5% (21.4 million metric tons [MMT] CO2 equivalent [CO2e]; eGRID 2021) and 7% (17.7 MMT CO2e; Cambium Low Renewable Energy Cost 15 year), depending on the grid scenario chosen. The emissions avoided are due to reduced electricity consumption from the cooling and heating end uses, but also include the increase in electricity from the heat recovery (added fan power) end use.

Future work can include adding heat/energy recovery solutions specifically for kitchen spaces, which were not included in this work.

