<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89040.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89040.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89040.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89040.md | section: Executive Summary | lines: 100-126 -->
## Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past several years, the objective of this work is to produce national datasets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency, electrification, and demand flexibility enduse load shapes (electricity, gas, propane, or fuel oil) that cover most of the high-impact, marketready (or nearly market-ready) measures. 'Measures' refer to energy efficiency variables that can be applied to buildings during modeling.

An end-use savings shape is the difference in energy consumption between a baseline building and a building with an energy efficiency, electrification, or demand flexibility measure applied. It results in a time-series profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

This documentation focuses on a single end-use savings shape upgrade-a variable refrigerant flow (VRF) with heat recovery (HR) heating and cooling system coupled with a dedicated outdoor air system (DOAS) for ventilation, where 25% upsizing (or 125% of the original size) is allowed for heating in colder climates (i.e., heating-dominant regions). This document primarily discusses the additional changes to the sizing algorithm and modeling approach; a comprehensive overview of the fundamental modeling methodology and background of the VRF (HR) DOAS upgrade, including applicability and other key assumptions, can be found in the original documentation: Variable Refrigerant Flow with Heat Recovery and Dedicated Outdoor Air System.

To provide high-level context on the 25% upsizing algorithm, if a thermal zone is cooling dominant, the indoor unit capacity of the VRF heat pump is sized based on the design cooling load. However, if the thermal zone is heating dominant, it is allowed for the 25% upsizing allowance. Once the 25% upsizing is allowed, if the 25% upsized capacity (or 125% from the original size) represented with the design condition exceeds the design heating load, the design heating load is used to calculate the rated capacity of the indoor unit. If the 25% upsized capacity represented with the design condition does not exceed the design heating load, the 25% upsized capacity represented with the rated condition is used for the capacity of the indoor unit, while the remaining heating load is handled with the supplemental/backup electric resistance coil. The outdoor unit capacity is calculated by summing all indoor unit capacities. More detailed description of the upsizing algorithm is presented in Section 3.2.2.

The VRF DOAS with 25% upsizing allowance upgrade demonstrates 13% total site energy savings (576 trillion British thermal units [TBtu]) for the U.S. commercial building stock modeled in ComStock (Figure 7). It also demonstrates between 33 and 44 million metric tons of greenhouse gas emissions avoided for the three grid electricity scenarios presented, as well as 23 million metric tons of greenhouse gas emissions avoided for on-site natural gas consumption. The savings are primarily attributed to:

- 41% stock heating natural gas savings (348 TBtu)
- 27% stock fan electricity savings (139 TBtu)
- 16% stock cooling electricity savings (109 TBtu)
- 46% stock heating other fuel savings (36 TBtu)
- 19% stock pump electricity savings (8 TBtu)
- 13% stock district heating savings (6 TBtu)
- -274% stock heat recovery electricity savings ( -17 TBtu)
- -31% stock heating electricity savings ( -54 TBtu).

Compared to the VRF DOAS analysis with original sizing we performed previously, the 25% upsizing allowance did not perform noticeably better. While the upsized unit handled more heating load with heat pumps and resulted in less usage of backup electric resistance heating (compared to the original sizing scenario), the upsized units also suffered with slightly decreased rated coefficients of performance (COP) based on the regression fittings we extracted from the products as shown in Figure 12 of the previous report. We acknowledge that there can be a better design practice to avoid 'lower COP for larger units' as described in Section 2.4, and future analysis can explore this aspect. To assess the impact of this upgrade more comprehensively, other factors such as return on investment and utility bill cost reflecting demand charges should also be considered.

