<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86105.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86105.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86105.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/86105.md | section: Executive Summary | lines: 79-100 -->
## Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past several years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency, electrification, and demand flexibility enduse load shapes (electricity, gas, propane, or fuel oil) that cover most of the high-impact, marketready (or nearly market-ready) measures. 'Measures' refers to energy efficiency variables that can be applied to buildings during modeling.

An end-use savings shape is the difference in energy consumption between a baseline building and a building with an energy efficiency, electrification, or demand flexibility measure applied. It results in a time-series profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

This documentation focuses on a single end-use savings shape measure-air-side economizers. Economizers increase outdoor ventilation at times when the system requests cooling and the controls determine that the outdoor air is cold or dry enough to be beneficial. The measure adds economizer controls to air handling units (AHUs) that do not already have this functionality. The prevalence of economizers in ComStock baseline AHUs is based on the governing energy code (based on the vintage and age of the building) for each specific model. The type of economizer control added is based on the guidelines of ASHRAE 90.1. Furthermore, a common fault that is prevalent in economizers (i.e., a fully closed outdoor air damper ) is added with certain prevalence to reflect findings from a previous study [1]: less than 35% of randomly selected buildings with economizers have a malfunction that persists for one month.

The economizer measure applies to buildings that cover 66% of the total building stock floor area and shows 0.3% total site energy savings (14 trillion British thermal units [TBtu]) for the U.S. commercial building stock modeled in ComStock (Figure 10). The economizer measure shows that 1 million metric tons (MMT) of greenhouse gas emissions are avoided; a reduction of 0.2% -0.4% depending on the three grid electricity scenarios presented (Figure 11). The savings are mainly due to the following factors:

- 2.0% stock cooling electricity savings (13.6 TBtu)
- 1.5% stock district cooling savings (1.4 TBtu)
- 0.9% stock pump electricity savings (0.4 TBtu)
- -0.1% stock fan electricity savings (0.7 TBtu)
- -0.1% stock heating gas savings (0.7 TBtu).

As shown in the results sections, the savings potential of the economizer upgrade at the stock level is relatively low compared to other upgrades we have analyzed. Since the amount of savings depends not only on the weather but also on the cooling demand of the building, the outdoor air requirement, the heat gain in the return air stream, and the configuration of the economizer, the savings will also vary for many buildings with different configurations and conditions. Additionally, economizer requirements have long been included in energy codes in many climates, limiting the opportunity and extent of savings from buildings that are not eligible for this upgrade because they already have economizers. However, since the economizer can be a simple upgrade (to an existing infrastructure) with a relatively low investment cost, the overall impact including the return on investment (or simple payback period) should be derived with the cost information.

