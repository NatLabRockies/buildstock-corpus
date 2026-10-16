<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_Dim Lighting During Peak Hours.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/3b69decb4e5f7bb3d6cc24f6224b318c921fd45f/assets/files/ComStock%20Measure%20Doc_Dim%20Lighting%20During%20Peak%20Hours.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_Dim%20Lighting%20During%20Peak%20Hours.pdf | corpus_version: e7ffee7a -->
# Dim Lighting During Peak Hours

## Measure Documentation: Dim Lighting During Peak Hours

<!-- decorative image omitted: image_000000 (cover art; no description by the figure standard) -->
## List of Acronyms

HVAC

heating, ventilating, and air conditioning

kW

kilowatt

GWh

gigawatt hour

NREL

National Renewable Energy Laboratory

LBNL

Lawrence Berkeley National Laboratory

DF

demand flexibility

DR

demand response

GEB

grid-interactive efficient building

ASHRAE

American Society of Heating, Refrigerating and Air-Conditioning

Engineers

BSS

Building Standard Scenarios

## Executive Summary

Building on the 3year effort to calibrate and validate the U.S. Department of Energy's ResStock ™ and ComStock ™ models, this work produces national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of questions regarding their commercial building stock.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the End-Use Load Profiles project.

The goal of this work is to develop energy efficiency, electrification, and demand flexibility enduse load shapes that cover high-impact, market-ready (or nearly market-ready) measures. 'Measures' refers to various 'what -if' scenarios that can be applied to buildings.

An end-use savings shape is the difference in energy consumption between a baseline building (or collection of buildings) and a building with an energy efficiency, electrification, or demand flexibility measure applied. The end-use savings shape is represented asIt results in a time-series profile broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each time step, as well as annual aggregations.

This report describes the modeling methodology for a single end-use savings shape measure -dim lighting during peak hours - and briefly introduces key results. The full public data set can be accessed on the ComStock ™ data lake or via the Data Viewer at comstock.nrel.gov. The public data set enables users to create custom aggregations of results for their use case (e.g., filter to a specific county).

The dim lighting during peak hours measure is a load-shedding measure represented in the Building Standard Scenarios (BSS) Demand Flexibility (DF) dataset. The project aims to estimate hourly demand flexibility potential of building stock by measures targeting various end uses. This measure reduces the lighting load during the provided peak periods by adjusting the lighting schedules. It is flexible and allows users to define the start and end time for the peak period, as well as the percentage reduction of the lighting. For this study, the peak period is identified by the state-level projected 2050 grid system net load profile, indicating the time period when the grid system needs demand flexibility most. Different peak periods are identified for winter, summer, and intermediate seasons respectively. The percentage reduction for occupied spaces and unoccupied spaces are 30% and 60% respectively. This measure is applicable to all commercial buildings, except spaces with critical loads that are not feasible for demand response.

The demand flexibility measure is applied on each day, not taking actual dispatch strategies into consideration. The daily percentage lighting load reduction is calculated during the peak period, and the 75 th percentile will be used for further DR analysis in another tool DR-Path. The object of the measure is demand flexibility, so the impact on annual site energy consumption is expected to be trivial, as 0.39%. Apart from the savings in the lighting electricity consumption, the heating load is increased and the cooling load is decreased due to the internal load reduction from lighting. Therefore, the end use by heating and cooling are also affected as well.

## Acknowledgments

The work described in this study was funded by the U.S. Department of Energy's Building Technologies Office (BTO) under Lawrence Berkeley National Laboratory Contract No. DEAC02-05CH11231 and National Renewable Energy Laboratory Contract No. DE-AC3608GO28308. The authors would like to thank Amir Roth and Sydney Applegate (BTO) for their support of this work. The authors would also like to acknowledge the valuable guidance and input provided by [ANYONE WHO HELPED YOU WITH THE MEASURE OR INDUSTRY FOLK WHO GAVE YOU DATA]. Any remaining errors or omissions are our own.

## Table of Contents

| List of Acronyms Executive Summary                                                                                                                           | ........................................................................................................... 3 ...................................................................................................... 4                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5                                                                                                                                                            | Acknowledgments.........................................................................................................                                                                                                                                 |
| Table of Contents                                                                                                                                            | .......................................................................................................... 6 7                                                                                                                                           |
| List of Figures ...............................................................................................................                              |                                                                                                                                                                                                                                                          |
| List of Tables .................................................................................................................                             | 7                                                                                                                                                                                                                                                        |
| 1. Technology                                                                                                                                                | Summary ............................................................................................. 1                                                                                                                                                  |
| 1.1. Project Background Lighting Control                                                                                                                     | ....................................................................................................................... 1 Strategies for Demand                                                                                                          |
| 1.2. 2. ComStock Baseline Approach ................................................................................ 2                                        | Flexibility ..................................................................... 1                                                                                                                                                                      |
| Approach                                                                                                                                                     | ................................................................................................. 3                                                                                                                                                      |
| 3. Modeling 3.1. Applicability                                                                                                                               | .................................................................................................................................. 3                                                                                                                     |
| 3.2. Technology Specifics 3.3. Limitations and Concerns                                                                                                      | .................................................................................................................... 4                                                                                                                                   |
| ..............................................................................................................                                               | 5                                                                                                                                                                                                                                                        |
| 4. Output Variables                                                                                                                                          | 5                                                                                                                                                                                                                                                        |
|                                                                                                                                                              | ......................................................................................................                                                                                                                                                   |
| 5. Results                                                                                                                                                   | ...................................................................................................................... 6 ............................................................................................................................. 6 |
| 5.1. Individual Tests 5.2. Demand Flexibility Performance .................................................................................................. | 7                                                                                                                                                                                                                                                        |
| 5.3. Stock Site Energy Impacts                                                                                                                               | ............................................................................................................ 9                                                                                                                                           |
| References ...................................................................................................................                               | 12                                                                                                                                                                                                                                                       |
| Appendix ...................................................................................................................... 12                           |                                                                                                                                                                                                                                                          |

| List of Figures                                                                                                                                                                                                                                   | List of Figures   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Figure 1. Building Standard Scenarios Demand Flexibility Project Workflow ............................................ 1                                                                                                                          |                   |
| Figure 2. Noticeable and Acceptable dimming of lighting in different literatures from [7] ......................... 2                                                                                                                             |                   |
| Figure 3. Default 4-hour peak (load shedding) period of each season and each state for the measures ....... 4                                                                                                                                     |                   |
| Figure 4. Site electricity use on 08/01 for a small office in California ......................................................... 7                                                                                                              |                   |
| Figure 5. Aggregated lighting electricity load profile for California for an example day in winter, summer and intermediate season ........................................................................................................... 8  |                   |
| Figure 6. Distribution of daily percentage lighting load reduction during the peak period for                                                                                                                                                     | each state .... 9 |
| Figure 7. Stock-level site energy use comparison by end use types .............................................................                                                                                                                   | 9                 |
| Figure 8. Distributions of stock-level site energy savings by end use types ...............................................                                                                                                                       | 10                |
| Figure 9. Distributions of building-level site energy savings by climate zone ...........................................                                                                                                                         | 11                |
| List of Tables                                                                                                                                                                                                                                    | and               |
| Table 1. Average Building-Level Lighting Power Densities (W/ft2) by Lighting Generation Building Type ......................................................................................................................................... 2 |                   |
| Table 2. Annual electricity end use breakdown comparison for baseline and the measure ..........................                                                                                                                                  |                   |
| 7                                                                                                                                                                                                                                                 |                   |
| 3. Major Changes in End Uses .......................................................................................................... 10                                                                                                        |                   |
| Table                                                                                                                                                                                                                                             |                   |

## 1. Technology Summary

## 1.1. Project Background

This measure is represented in the Building Standard Scenarios (BSS) Demand Flexibility (DF) project, which aims to provide credible estimates of the current and future DF potential for both commercial and residential building stocks. For commercial building analysis and to inform assumptions of the fraction of commercial building enduse load that can shed or shift ('DF fractions'), demand flexibility measures developed by LBNL in the OpenStudio-GEB gem [1] are integrated in ComStock. The OpenStudio-GEB gem provides modeling of technologies and controls to evaluate demand flexibility and electrification of grid-interactive efficient buildings (GEB). The gem includes existing OpenStudio measures from Building Technologies Office (BTO) funded GEB projects with revision and update, as well as new measures developed by LBNL based on priority. Currently the gem has 24 measures covering upgrades for HVAC systems, envelopes, internal loads, electric vehicles, etc., and it is actively updated to expand the coverage.

The simulation outputs from ComStock inform further analysis by LBNL's DR -Path model. In addition to DF fractions for load shedding and shifting, DR-Path also incorporates assumptions about technology fixed and variable costs, and probability of a system operator dispatching the DF events to produce estimates of the technical, economic, and achievable (market) demand response potential for a given end-use/technology, building/customer type, and geographic locations [2]. Figure 1 depicts the BSS DF project workflow.

Figure 1. Building Standard Scenarios Demand Flexibility Project Workflow

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Dim Lighting During Peak Hours.yaml
     source: ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000001_986f35b8fe32bfc7f6194a170d61199d86a0b5513debce157c61d4ab9140eb27.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 1: workflow diagram of the Building Standard Scenarios demand flexibility project and its data sources](ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000001_986f35b8fe32bfc7f6194a170d61199d86a0b5513debce157c61d4ab9140eb27.png)

Figure 1: flow diagram of the Building Standard Scenarios (BSS) demand flexibility workflow.
Three input rows (disaggregated building end-use load; end-use fraction capable of load shedding
or shifting; grid need and dispatch of demand response) feed boxes naming the data sources and
steps: BuildStock, Scout, DR-Path, updated DF fractions from EnergyPlus modeling, exogenous
dispatch (Cambium, aggregated BSS demand) and endogenous dispatch (ReEDS).

## 1.2. Lighting Control Strategies for Demand Flexibility

Based on CBECS 2018 [3], the lighting load accounts for approximately 17 % of the total annual electricity consumption of commercial buildings. Multiple previous studies have suggested that it is acceptable to reduce the lighting levels without occupants detecting it (noticeable), or without causing any significant visual discomfort (acceptable). Besides, the lighting use patterns are generally irrelevant to climate regions, so lighting load can be a good candidate to provide consistent demand side flexibility service.

Studies [4], [5] found that a reduction of 17 % and 15 -25 %, respectively from the initial base illuminance value of 1095 lux and 500 lux, is barely detectable. Study [6] did the experiment in an office laboratory with 33 participants and found that with no daylight, relatively low prevailing daylight, and high prevailing daylight, the level of dimming not noticed by occupants was 20%, 40 % and 60% respectively. The level of dimming still acceptable was 40% with no or low daylight, and 80% with high prevailing daylight.

The 'noticeable' and 'acceptable' levels from other studies are summarized by paper [7] as the Figure 2 below. The paper also modeled the grid-level peak load reduction for the MISO (Midcontinent Independent System Operator) region, using prototype building models, with different levels of LED lighting fixture adoption and availability of control technology. It was estimated that 0.21 to 0.39 % flexibility of peak load can be provided by dimming of 20 % from the base illumination level, in a future case with 100 % LED fixtures and 30 % technology penetration for smart lighting controls.

Figure 2. Noticeable and Acceptable dimming of lighting in different literatures from [7]

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Dim Lighting During Peak Hours.yaml
     source: ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000002_39d1cdd8d646572d7b2d401fa25c0120c2b659e52e6047e751da70ef89977096.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 2: bubble plot of detectable and acceptable lighting dimming percentages versus starting illuminance](ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000002_39d1cdd8d646572d7b2d401fa25c0120c2b659e52e6047e751da70ef89977096.png)

Figure 2: bubble plot of percent reduction from base lighting level (y, 0 to 45%) against
starting illuminance in lux (x, 0 to 1300), one bubble per study (Hu 2016, Newsham 2008,
Kryszczuk 2002, Akashi and Neches 2004, Kim 2016, Tenner 1997, Shikakura 2003). Yellow marks the
detectable percentage of dimming, mostly 10 to 20%; orange marks the acceptable percentage,
reaching roughly 20 to 40%.

## 2. ComStock Baseline Approach

ComStock uses a similar approach to the ASHRAE 90.1 Lighting Subcommittee for determining the lighting power density (LPD) allowance for a given space type. Table 1 provides the average installed building-level LPDs in ComStock by building type and lighting generation. The detailed lighting modeling method in baseline can be found in ComStock Documentation at Section 4.5.

Table 1. Average Building-Level Lighting Power Densities (W/ft2) by Lighting Generation and Building Type

| Building type           |   gen1 |   gen2 |   gen3 |   gen4 |   gen5 |
|-------------------------|--------|--------|--------|--------|--------|
| full_service_restaurant |   1.51 |   0.96 |   0.45 |   0.43 |   0.39 |
| hospital                |   1.59 |   1.07 |   0.63 |   0.58 |   0.52 |

| large_hotel              |   1.31 |   0.80 |   0.29 |   0.23 |   0.21 |
|--------------------------|--------|--------|--------|--------|--------|
| large_office             |   1.18 |   0.80 |   0.50 |   0.53 |   0.47 |
| medium_office            |   1.18 |   0.80 |   0.50 |   0.53 |   0.47 |
| outpatient               |   1.27 |   0.85 |   0.53 |   0.52 |   0.47 |
| primary_school           |   0.73 |   0.56 |   0.48 |   0.47 |   0.42 |
| quick_service_restaurant |   1.73 |   1.11 |   0.56 |   0.52 |   0.47 |
| retail                   |   1.17 |   0.75 |   0.54 |   0.47 |   0.42 |
| secondary_school         |   0.88 |   0.58 |   0.48 |   0.45 |   0.40 |
| small_hotel              |   1.08 |   0.63 |   0.28 |   0.25 |   0.22 |
| small_office             |   1.18 |   0.79 |   0.50 |   0.52 |   0.47 |
| strip_mall               |   1.59 |   1.07 |   0.65 |   0.64 |   0.59 |
| warehouse                |   0.83 |   0.40 |   0.39 |   0.30 |   0.27 |

## 3. Modeling Approach

## 3.1. Applicability

The applicability of this measure is defined by space type instead of building type. Except some space types with strict requirements for illuminance level and are not suitable for demand response events, other spaces should all have potential for load reduction by dimming lights. The list of excluded space types in ComStock is as follows.

## DOE Prototypes

- Hospital:

- ER\_Exam

- ER\_NurseStn

- ER\_Trauma

- ER\_Triage

- ICU\_NurseStn

- ICU\_Open

- ICU\_PatRm

- Lab

- OR

- Outpatient:

- Anesthesia

- BioHazard

- Exam

- MedGas

- OR

- PACU

- PreOp

- ProcedureRoom

- Laboratory:

- Lab with fume hood

## DEER Prototypes

- Hsp:

- HspSurgOutptLab

## 3.2. Technology Specifics

The measure aims to evaluate the fraction of end use load that potentially can be reduced during the system-level peak period within the commercial building sector. The default system-level peak periods are identified for each state using the 2050 net load profile from 2023 Cambium dataset, Mid-case scenario [8]. Cambium dataset is the projection of hourly select supply- and demand-side metrics including gross demand, VRE generation, and operational costs for multiple demand futures. The peak period for this load shedding measure is defined as the four hours including the peak hour with the highest average electricity load during each season. The whole year is categorized into three seasons as summer season (June to September), winter season (December to March) and intermediate season (all other months). The identified fourhour peak periods for each state are illustrated in Figure 3. The detailed start and end time can be found in the appendix. Note that Cambium dataset does not include system load profiles for Alaska and Hawaii, and the buildings of these two states are not within the scope of the BSS DF project. However, to facilitate the ComStock simulation, Alaska and Hawaii are assigned with peak periods from the state with the similar climate zones.

Figure 3. Default 4-hour peak (load shedding) period of each season and each state for the measures

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Dim Lighting During Peak Hours.yaml
     source: ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000003_5d3921936fe736eb8bc2462c5242fc6a16255d32c84f8f1844cac7aea9c8e39a.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 3: grid of 48 state panels marking the default 4-hour peak period by season and hour of day](ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000003_5d3921936fe736eb8bc2462c5242fc6a16255d32c84f8f1844cac7aea9c8e39a.png)

Figure 3: small-multiples grid, one panel per state (48 panels), x-axis hour of day 0 to 24.
Colored bars mark the default 4-hour load-shedding window for winter (blue), summer (red) and
intermediate season (green). Most windows fall in the late afternoon and evening, roughly hours
16 to 21, with the season-to-season shift differing by state.

This measure will loop through all the interior lighting objects and clone their lighting schedules for each season if the space is applicable. The state of the building is identified from the additionalProperties object and the measure will adjust the lighting schedule on each day during the corresponding peak period of the state and the season. During the peak period, the lighting load is reduced by 30% for occupied spaces and 60% for unoccupied spaces during the peak hours. Unoccupied spaces are those spaces with no occupant all the time, e.g. storage rooms and mechanical rooms. According to the literature reviewed, 30% is the level of li ght dimming that's generally not noticeable, and 60% is the acceptable level of dimming. When there's no occupant to be affected, the dimming level can be higher for maximum load reduction. The reduction is applied daily, and the expected outcome of the simulation is the distribution of daily percentage reduction of the end use load by the measure. The detailed demand response event dispatch strategy will be considered outside the ComStock simulation by DR-Path. It is worth noting that the measure offers the flexibility for users to specify the start and end date and time of multiple peak periods when the lighting schedule is adjusted, as well as the percentage of the lighting load reduction. If no user inputs are provided, the aforementioned default values will be used.

## 3.3. Limitations and Concerns

Several limitations and concerns of the measure are identified as follows.

- The percentage reduction of the lighting load is universal among different commercial building types, without identifying the detailed space types. The assumption is made based on the judgment of what might be possible, because the aim of the study is to show the load shedding potential, but not necessarily the real-world operations.
- The measure also assumes that the lighting fixtures are controllable (either via deviceintegrated controls or via communication with BAS), which is idealistic and might not be true for older buildings.
- The measure can only be applicable to those lighting schedules in scheduleRuleSet format, but this is likely to cover all models in ComStock.
- The lighting load reduction event is applied for every day throughout the year. In reality, demand response programs are structured to limit events to a small number of days and total hours, but the DR event dispatch strategy is not part of this study but a task in postprocessing by another tool.
- The start of the peak period is defined by the seasonal peak hour of the aggregated statelevel load profile from Cambium dataset, which does not necessarily align with the peak hour of a particular electricity system or individual building. Besides, any demand-side improvements on building energy consumption is not reflected in the Cambium loads. If these improvements are significa nt enough to alter the peak timings, it's not captured in the dispatch assumptions.

## 4. Output Variables

Since the measure is implemented under the BSS DF project, the outputs from ComStock simulation will be used for further processing to calculate the demand decrease percentage during peak period (D3 [9]), aggregated at state level. The D3 metric is defined in the equation below.

Where 𝑠𝑝 is the shedding (peak) period of the day, 𝐸𝑏𝑎𝑠𝑒 and 𝐸𝑚𝑒𝑎𝑠𝑢𝑟𝑒 are the baseline and postmeasure electricity demand for the specific end use targeted by the measure, which is lighting electricity use in this case. The denominator of the equation should include all the buildings with the target end use type, which is all commercial buildings for the lighting measure. To generate the metric, the building-level ComStock timeseries are aggregated into state-level timeseries load profiles during post-processing. Since the ComStock sampling method can use one building model to represent buildings across multiple states, the identified peak period from the model to apply change can be different from the peak period used for the state to calculate D3, which impairs the effectiveness of the measure. To keep most of the useful models while reducing the noise in results as much as possible, when aggregating the state-level load, buildings from states with a peak period shifted by more than 1 hour are excluded. The D3 value is calculated for each day, and the 75 th percentile of the annual distribution of D3 will be used in the following analysis of DR-Path.

## 5. Results

In this section, results are presented both for individual buildings and at stock level through distributions. Individual building result is used for quality assurance/quality control and to showcase the mechanism of the measure. Stock-level results include the combined impact of all the analyzed buildings in ComStock, including buildings that are not applicable to this measure. Therefore, they do not necessarily represent the energy savings of a particular or average building. Stock level results should not be interpreted as the average savings that a building might realize by implementing the measure. Apart from the metrics related to total energy use, the stock level results focus on the demand flexibility metrics.

## 5.1. Individual Tests

Multiple models of different building types and states were tested. Here the result of a small office building in California is used to illustrate the effect of the measure. The percentage light dimming was 30% for occupied spaces and 60% for unoccupied spaces. All spaces in the model are applicable in this example. Figure 4 shows the reduction of total electricity load for one day during the shedding period, which is 18:00-22:00 for California in summer.      Since the peak period was identified from the grid-level net load, it does not necessarily coincide with the single-building peak period. Therefore, the peak load of each month was not necessarily reduced for a single building.

Figure 4. Site electricity use on 08/01 for a small office in California

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Dim Lighting During Peak Hours.yaml
     source: ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000004_9d3039df5515e761d809b2b31dfd4835110c635d3049eca20e30f5f4226809b6.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 4: whole-building net electricity on 08/01 for a California small office, baseline versus upgrade](ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000004_9d3039df5515e761d809b2b31dfd4835110c635d3049eca20e30f5f4226809b6.png)

Figure 4: line chart of whole-building net electricity consumption in W (y, 0 to about 100,000)
over the hours of 08/01 for a small office in California. Baseline (blue) and upgrade (orange)
coincide until the green-shaded shed period in the late afternoon and evening, where the upgrade
line drops slightly below the baseline before the two rejoin.

Table 2 compares the annual electricity end uses between baseline and the measure. Except for the reduction in interior lighting, the heating end use was increased and the cooling end was decreased, because of the reduction of the internal load from the lighting. The electricity consumption of fans was also changed due to the change of the heating and cooling load.

Table 2. Annual electricity end use breakdown comparison for baseline and the measure

|                           |   Baseline | Upgrade            |
|---------------------------|------------|--------------------|
| 221.15                    |     223.62 | Heating            |
| 339.41                    |     338.45 | Cooling            |
| 82.67                     |      74.77 | Interior Lighting  |
| Lighting 58.01            |      58.01 | Exterior           |
| Interior Equipment 131.48 |     131.48 |                    |
| 0                         |          0 | Exterior Equipment |
| 321.08                    |     320.58 | Fans               |
| 0                         |          0 | Pumps              |
| Water Systems             |         25 | 25                 |

## 5.2. Demand Flexibility Performance

The simulation for the 10k samples is used to demonstrate the aggregated results. Figure 5 illustrates a daily lighting electricity load for each season to show that the load was reduced during the corresponding peak period. The peak periods do not necessarily coincide with the simulated peaks from ComStock, because they were identified from the projected grid-side net load shape including sectors other than commercial buildings. Besides, there can also be a gap between the ComStock baseline load shape and the real load shape from the utility AMI data [10]

Figure 5. Aggregated lighting electricity load profile for California for an example day in winter, summer and intermediate season

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Dim Lighting During Peak Hours.yaml
     source: ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000005_df7a4d58b8966e560bbfe77ca83d0a1930ae4c2962a4ff303a6a7c01517259f3.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 5: aggregated California lighting load profiles for a winter, summer and intermediate day, baseline vs measure](ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000005_df7a4d58b8966e560bbfe77ca83d0a1930ae4c2962a4ff303a6a7c01517259f3.png)

Figure 5: three stacked line panels (winter, summer, intermediate) of aggregated lighting
electricity in MWh (y, about 200,000 to 700,000) over one example day for California. Baseline
(blue) and post-measure (orange) overlap until about hour 17, where the post-measure profile
drops sharply for the 4-hour shed window and rebounds to the baseline at about hour 21.

For each day the measure is applied, a D3 value (percentage decrease) for the lighting end use is calculated, and the distribution of the daily D3 values for each state is illustrated in Figure 6 for the 10k samples, sorted by the 75 th percentile, which is used to represent the demand flexibility potential of the measure in DR-Path. The difference of D3 across states is mainly attributed to the different fraction of unoccupied spaces (such as warehouses) and inapplicable spaces (such as operation rooms) within each state.

Figure 6. Distribution of daily percentage lighting load reduction during the peak period for each state

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Dim Lighting During Peak Hours.yaml
     source: ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000006_12d0d4c8f67c44866e01f09e41a0d3fea74af9eee471619758eade06b0c0be4c.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 6: box plot by state of daily percentage lighting load reduction during the peak period](ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000006_12d0d4c8f67c44866e01f09e41a0d3fea74af9eee471619758eade06b0c0be4c.png)

Figure 6: box plot of daily percentage lighting load reduction during the peak period (y, 0 to
40%) for each state (x), with the median as a dashed line and the 75th percentile marked in red.
Reductions cluster between about 30 and 37% for most states; KS is highest near 40% and the
right-hand states trend toward 30%.

## 5.3. Stock Site Energy Impacts

Figure 7. Stock-level site energy use comparison by end use types

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Dim Lighting During Peak Hours.yaml
     source: ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000007_85c5f6bd32cbbc53887ea6773b29f1505c15522cff53aff29ff843d5e3df8e45.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 7: stacked bar chart of stock annual energy consumption by end use and fuel, baseline vs GEB_DF_Lighting](ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000007_85c5f6bd32cbbc53887ea6773b29f1505c15522cff53aff29ff843d5e3df8e45.png)

Figure 7: stacked bar chart of stock annual energy consumption in TBtu (y, 0 to 5000) for
Baseline and GEB_DF_Lighting, segmented by end use and fuel per the legend (interior equipment,
fans, cooling, interior lighting electricity, heating by fuel, water systems, refrigeration,
exterior lighting, pumps, heat recovery and rejection). Totals fall from 4865 to 4847 TBtu, the
interior lighting segment carrying the change. See Table 3.

The measure is used for demand flexibility implementation, so it's expected that the total site energy impact is not prominent. The total annual site energy was decreased by 0.39%, primarily attributed to savings from interior lighting and cooling, despite slightly increased heating energy due to the reduction in internal load.

Table 3. Major Changes in End Uses

| End Use Type                   |   Saving (TBtu) |   Percentage Saving (%) |
|--------------------------------|-----------------|-------------------------|
| Interior Lighting, Electricity |           22.35 |                    5.08 |
| Cooling, Electricity           |            2.92 |                    0.40 |
| Fans, Electricity              |            0.55 |                    0.10 |
| Heating, Electricity           |           -1.83 |                   -0.70 |
| Heating, Natural Gas           |           -4.98 |                   -0.52 |
| Heating, District Heating      |           -0.16 |                   -0.39 |

Figure 8 shows the distribution of end use changes. The most prominent difference is in interior lighting where the median buildings saves around 5% electricity due to the light dimming during the daily peak periods. Heating energy consumption in many buildings were increased due to the reduced internal loads from dimming lights. Cooling electricity decreased in many buildings for the same reason. Changes to other end uses are observed (e.g. fans and pumps) but they are fairly minimal and reflect the internal loads changes from lighting turndowns.

Figure 8. Distributions of stock-level site energy savings by end use types

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Dim Lighting During Peak Hours.yaml
     source: ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000008_ebbd6bb105cbd0a020e02b057a5c9b6b59b37faef45d11eedc8ff00f5a3bd82f.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 8: distributions of percent site energy savings by end use for the GEB_DF_Lighting upgrade](ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000008_ebbd6bb105cbd0a020e02b057a5c9b6b59b37faef45d11eedc8ff00f5a3bd82f.png)

Figure 8: horizontal distribution plot of percent site energy savings by end use (x, -140 to
100%), one row per end use and fuel with its model count n, for Upgrade 35.0 GEB_DF_Lighting
(unweighted). Electricity interior lighting sits a few percent positive; heating rows spread
widest around zero; the remaining end uses are centered on zero. See Table 3.

The measure is applicable to all climate zones, and the demand flexibility measure is not related to weather conditions. Therefore, the site energy saving is not correlated with climate zones, as shown in Figure 9.

Figure 9. Distributions of stock-level site

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Dim Lighting During Peak Hours.yaml
     source: ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000009_e9c956f6dfca4294512a05402b9c87b695c2ce0a472d4aaaa23a6658ee43be1f.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 9: distributions of percent site energy savings by ASHRAE climate zone for the GEB_DF_Lighting upgrade](ComStock_Measure_Doc_Dim_Lighting_During_Peak_Hours_images/image_000009_e9c956f6dfca4294512a05402b9c87b695c2ce0a472d4aaaa23a6658ee43be1f.png)

Figure 9: horizontal violin plot of percent site energy savings (x, -7 to 7%) by climate zone 1A
through 8 with the model count n per zone, for Upgrade 35.0 GEB_DF_Lighting (unweighted). Every
zone centers just above zero, roughly 0.3%, with long thin tails; there is no visible trend with
climate zone.

energy savings by climate zone

## References

- [1]  S. Kaiyu, Z. Wanni, M. Nathan, and F. Katherine, OpenStudio GEB Gem . Lawrence Berkeley National Laboratory. [Online]. Available: https://github.com/LBNLETA/Openstudio-GEB-gem
- [2]  B. Gerke et al. , 'The California Demand Response Potential Study, Phase 4: Report on Shed and Shift Resources Through 2050,' 2024.
- [3] U.S. Energy Information Administration, 'Commercial Buildings Energy Consumption Survey (CBECS).' https://www.eia.gov/consumption/commercial/data/2018/, 2018. [Online]. Available: https://www.eia.gov/consumption/commercial/data/2018/
- [4] K. M. Kryszczuk and P. R. Boyce, 'Detection of Slow Light Level Reduction,' J. Illum. Eng. Soc. , vol. 31, no. 2, pp. 3 -10, July 2002, doi: 10.1080/00994480.2002.10748387.
- [5] Y. Akashi and J. Neches, 'Detectability and Acceptability of Illuminance Reduction for Load Shedding,' J. Illum. Eng. Soc. , vol. 33, no. 1, pp. 3 -13, Jan. 2004, doi: 10.1080/00994480.2004.10748422.
- [6] G. R. Newsham, S. Mancini, and R. G. Marchand, 'Detection and Acceptance of Demand -Responsive Lighting in Offices with and without Daylight,' LEUKOS , vol. 4, no. 3, pp. 139 -156, Jan. 2008, doi: 10.1582/LEUKOS.2007.004.03.001.
- [7] S. Vanage, K. Cetin, J. McCalley, and Y. Wang, 'Grid -scale demand-side flexibility services using commercial buildings lighting loads,' Energy Build. , vol. 300, p. 113631, Dec. 2023, doi: 10.1016/j.enbuild.2023.113631.
- [8]  P. Gagnon et al. , 'Cambium 2023 Scenario Descriptions and Documentation,' 2024.
- [9]  J. Liu et al. , 'Defining and applying an electricity demand flexibility benchmarking metrics framework for gridinteractive efficient commercial buildings,' Adv. Appl. Energy , vol. 8, p. 100107, Dec. 2022, doi: 10.1016/j.adapen.2022.100107.
- [10] N. M. Frick et al. , 'End -Use Load Profiles for the U.S. Building Stock: Market Needs, Use Cases, and Data Gaps.'

## Appendix

The table lists the default peak period for each season for each state, determined from the power system net load profile from Cambium dataset (Mid-case scenario in 2050). The default length of load shedding is four hours.

| State   | Summer Peak Start   | Summer Peak End   | Winter Peak Start   | Winter Peak End   | Intermediate Peak Start   | Intermediate Peak End   |
|---------|---------------------|-------------------|---------------------|-------------------|---------------------------|-------------------------|
| IA      | 8/28/50 17:00       | 8/28/50 21:00     | 1/19/50 17:00       | 1/19/50 21:00     | 11/4/50 17:00             | 11/4/50 21:00           |
| WV      | 7/18/50 16:00       | 7/18/50 20:00     | 1/18/50 17:00       | 1/18/50 21:00     | 5/29/50 16:00             | 5/29/50 20:00           |
| MA      | 6/22/50 17:00       | 6/22/50 21:00     | 12/14/50 17:00      | 12/14/50 21:00    | 10/18/50 17:00            | 10/18/50 21:00          |
| VT      | 7/12/50 18:00       | 7/12/50 22:00     | 12/25/50 18:00      | 12/25/50 22:00    | 11/28/50 17:00            | 11/28/50 21:00          |
| WI      | 7/6/50 18:00        | 7/6/50 22:00      | 12/19/50 17:00      | 12/19/50 21:00    | 11/8/50 17:00             | 11/8/50 21:00           |

| CT   | 6/22/50 17:00   | 6/22/50 21:00   | 12/7/50 17:00   | 12/7/50 21:00   | 5/30/50 17:00   | 5/30/50 21:00   |
|------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| TN   | 6/30/50 17:00   | 6/30/50 21:00   | 1/18/50 17:00   | 1/18/50 21:00   | 5/28/50 17:00   | 5/28/50 21:00   |
| NY   | 7/6/50 18:00    | 7/6/50 22:00    | 1/20/50 17:00   | 1/20/50 21:00   | 11/16/50 17:00  | 11/16/50 21:00  |
| UT   | 8/8/50 18:00    | 8/8/50 22:00    | 12/29/50 17:00  | 12/29/50 21:00  | 11/13/50 17:00  | 11/13/50 21:00  |
| VA   | 7/7/50 18:00    | 7/7/50 22:00    | 12/29/50 16:00  | 12/29/50 20:00  | 11/27/50 16:00  | 11/27/50 20:00  |
| DC   | 7/7/50 18:00    | 7/7/50 22:00    | 12/29/50 16:00  | 12/29/50 20:00  | 11/27/50 16:00  | 11/27/50 20:00  |
| SD   | 6/29/50 15:00   | 6/29/50 19:00   | 12/26/50 16:00  | 12/26/50 20:00  | 4/17/50 18:00   | 4/17/50 22:00   |
| OH   | 7/7/50 17:00    | 7/7/50 21:00    | 1/3/50 17:00    | 1/3/50 21:00    | 11/28/50 17:00  | 11/28/50 21:00  |
| SC   | 7/28/50 19:00   | 7/28/50 23:00   | 2/9/50 18:00    | 2/9/50 22:00    | 10/5/50 17:00   | 10/5/50 21:00   |
| MT   | 9/25/50 17:00   | 9/25/50 21:00   | 1/18/50 18:00   | 1/18/50 22:00   | 10/6/50 19:00   | 10/6/50 23:00   |
| MS   | 7/30/50 18:00   | 7/30/50 22:00   | 1/18/50 17:00   | 1/18/50 21:00   | 5/28/50 18:00   | 5/28/50 22:00   |
| NM   | 8/9/50 18:00    | 8/9/50 22:00    | 3/11/50 17:00   | 3/11/50 21:00   | 10/31/50 17:00  | 10/31/50 21:00  |
| NJ   | 7/6/50 17:00    | 7/6/50 21:00    | 12/7/50 17:00   | 12/7/50 21:00   | 5/31/50 17:00   | 5/31/50 21:00   |
| GA   | 6/30/50 18:00   | 6/30/50 22:00   | 1/3/50 18:00    | 1/3/50 22:00    | 5/26/50 18:00   | 5/26/50 22:00   |
| CA   | 8/14/50 18:00   | 8/14/50 22:00   | 12/14/50 17:00  | 12/14/50 21:00  | 10/2/50 17:00   | 10/2/50 21:00   |
| IL   | 7/7/50 18:00    | 7/7/50 22:00    | 12/29/50 16:00  | 12/29/50 20:00  | 11/8/50 16:00   | 11/8/50 20:00   |
| AZ   | 8/9/50 18:00    | 8/9/50 22:00    | 3/30/50 18:00   | 3/30/50 22:00   | 10/3/50 17:00   | 10/3/50 21:00   |
| TX   | 8/28/50 18:00   | 8/28/50 22:00   | 12/12/50 17:00  | 12/12/50 21:00  | 10/3/50 17:00   | 10/3/50 21:00   |
| NH   | 8/9/50 17:00    | 8/9/50 21:00    | 12/7/50 17:00   | 12/7/50 21:00   | 11/28/50 17:00  | 11/28/50 21:00  |
| DE   | 6/30/50 17:00   | 6/30/50 21:00   | 12/7/50 17:00   | 12/7/50 21:00   | 11/27/50 17:00  | 11/27/50 21:00  |
| WA   | 8/17/50 17:00   | 8/17/50 21:00   | 1/12/50 17:00   | 1/12/50 21:00   | 10/25/50 17:00  | 10/25/50 21:00  |
| OR   | 9/18/50 17:00   | 9/18/50 21:00   | 1/12/50 17:00   | 1/12/50 21:00   | 10/26/50 16:00  | 10/26/50 20:00  |
| MI   | 7/7/50 17:00    | 7/7/50 21:00    | 3/2/50 18:00    | 3/2/50 22:00    | 11/21/50 17:00  | 11/21/50 21:00  |
| MN   | 7/15/50 17:00   | 7/15/50 21:00   | 12/12/50 17:00  | 12/12/50 21:00  | 11/4/50 16:00   | 11/4/50 20:00   |
| WY   | 9/18/50 18:00   | 9/18/50 22:00   | 2/7/50 8:00     | 2/7/50 12:00    | 10/26/50 8:00   | 10/26/50 12:00  |
| IN   | 7/7/50 18:00    | 7/7/50 22:00    | 12/28/50 17:00  | 12/28/50 21:00  | 11/14/50 17:00  | 11/14/50 21:00  |
| OK   | 9/6/50 15:00    | 9/6/50 19:00    | 2/14/50 4:00    | 2/14/50 8:00    | 11/17/50 3:00   | 11/17/50 7:00   |
| NV   | 7/11/50 18:00   | 7/11/50 22:00   | 12/29/50 17:00  | 12/29/50 21:00  | 5/17/50 18:00   | 5/17/50 22:00   |
| KS   | 8/1/50 18:00    | 8/1/50 22:00    | 1/17/50 17:00   | 1/17/50 21:00   | 11/1/50 17:00   | 11/1/50 21:00   |

| PA   | 6/22/50 17:00   | 6/22/50 21:00   | 1/3/50 17:00   | 1/3/50 21:00   | 5/29/50 17:00   | 5/29/50 21:00   |
|------|-----------------|-----------------|----------------|----------------|-----------------|-----------------|
| MO   | 7/6/50 18:00    | 7/6/50 22:00    | 12/29/50 8:00  | 12/29/50 12:00 | 11/16/50 16:00  | 11/16/50 20:00  |
| ME   | 8/10/50 17:00   | 8/10/50 21:00   | 2/15/50 17:00  | 2/15/50 21:00  | 11/28/50 16:00  | 11/28/50 20:00  |
| KY   | 7/7/50 19:00    | 7/7/50 23:00    | 12/12/50 17:00 | 12/12/50 21:00 | 11/29/50 17:00  | 11/29/50 21:00  |
| CO   | 8/9/50 18:00    | 8/9/50 22:00    | 12/26/50 18:00 | 12/26/50 22:00 | 11/27/50 16:00  | 11/27/50 20:00  |
| NC   | 8/16/50 18:00   | 8/16/50 22:00   | 12/29/50 17:00 | 12/29/50 21:00 | 11/30/50 17:00  | 11/30/50 21:00  |
| AL   | 7/24/50 18:00   | 7/24/50 22:00   | 1/3/50 18:00   | 1/3/50 22:00   | 5/26/50 18:00   | 5/26/50 22:00   |
| ND   | 7/31/50 19:00   | 7/31/50 23:00   | 12/26/50 19:00 | 12/26/50 23:00 | 4/17/50 18:00   | 4/17/50 22:00   |
| AR   | 9/6/50 17:00    | 9/6/50 21:00    | 12/12/50 17:00 | 12/12/50 21:00 | 5/30/50 18:00   | 5/30/50 22:00   |
| FL   | 7/27/50 18:00   | 7/27/50 22:00   | 1/3/50 18:00   | 1/3/50 22:00   | 5/31/50 18:00   | 5/31/50 22:00   |
| ID   | 8/5/50 19:00    | 8/5/50 23:00    | 1/12/50 17:00  | 1/12/50 21:00  | 11/15/50 18:00  | 11/15/50 22:00  |
| LA   | 6/29/50 18:00   | 6/29/50 22:00   | 12/12/50 17:00 | 12/12/50 21:00 | 5/30/50 18:00   | 5/30/50 22:00   |
| MD   | 7/6/50 17:00    | 7/6/50 21:00    | 1/9/50 16:00   | 1/9/50 20:00   | 5/26/50 17:00   | 5/26/50 21:00   |
| NE   | 7/15/50 15:00   | 7/15/50 19:00   | 3/16/50 17:00  | 3/16/50 21:00  | 10/31/50 16:00  | 10/31/50 20:00  |
| RI   | 7/28/50 18:00   | 7/28/50 22:00   | 12/7/50 17:00  | 12/7/50 21:00  | 10/18/50 18:00  | 10/18/50 22:00  |
| HI   | 7/27/50 18:00   | 7/27/50 22:00   | 1/3/50 18:00   | 1/3/50 22:00   | 5/31/50 18:00   | 5/31/50 22:00   |
| AK   | 7/15/50 17:00   | 7/15/50 21:00   | 12/12/50 17:00 | 12/12/50 21:00 | 11/4/50 16:00   | 11/4/50 20:00   |
