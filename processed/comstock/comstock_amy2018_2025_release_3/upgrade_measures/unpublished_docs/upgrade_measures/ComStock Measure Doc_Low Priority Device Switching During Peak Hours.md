<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/3b69decb4e5f7bb3d6cc24f6224b318c921fd45f/assets/files/ComStock%20Measure%20Doc_Low%20Priority%20Device%20Switching%20During%20Peak%20Hours.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_Low%20Priority%20Device%20Switching%20During%20Peak%20Hours.pdf | corpus_version: f6dcd301 -->
# Low Priority Device Switching During Peak Hours

## Measure Documentation: Low Priority Device Switching During Peak Hours

<!-- decorative image omitted: image_000000 (wordmark; no description by the figure standard) -->
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

This report describes the modeling methodology for a single end-use savings shape measure -low priority device switching during peak hours - and briefly introduces key results. The full public data set can be accessed on the ComStock ™ data lake or via the Data Viewer at comstock.nrel.gov. The public data set enables users to create custom aggregations of results for their use case (e.g., filter to a specific county).

The low priority device switching during peak hours measure is a measure represented in the Building Standard Scenarios (BSS) Demand Flexibility (DF) dataset. The project aims to estimate hourly demand flexibility potential of building stock by measures targeting various end uses. This measure switches off low-priority devices (e.g., unused PCs, office equipment) during peak hours in the commercial building to reduce the plug load in office-like spaces. It is flexible and allows users to define the start and end time for the peak period, as well as the percentage reduction of the plug load. For this study, the peak period is identified by the state-level projected 2050 grid system net load profile, indicating the time period when the grid system needs demand flexibility most. By default, the measure reduces the electric equipment load by 20% during the peak period.

The demand flexibility measure is applied on each day, not taking actual dispatch strategies into consideration. The daily percentage electric equipment load reduction (D3) is calculated during the peak period, and the 75th percentile will be used for further DR analysis in another tool DRPath. The 75 th percentile of daily D3 ranges from 4% to 14% across states, depending on the fraction of applicable space area in each state. The object of the measure is demand flexibility and the applicable spaces are limited, so the impact on annual site energy consumption is expected to be trivial, as 0.13% for the whole commercial stock. Apart from the savings in the electric equipment electricity consumption, the heating load is increased and the cooling load is decreased due to the internal load reduction.

## Acknowledgments

The work described in this study was funded by the U.S. Department of Energy's Building Technologies Office (BTO) under Lawrence Berkeley National Laboratory Contract No. DEAC02-05CH11231 and National Renewable Energy Laboratory Contract No. DE-AC3608GO28308. The authors would like to thank Amir Roth and Sydney Applegate (BTO) for their support of this work. The authors would also like to acknowledge the valuable guidance and input provided by [ANYONE WHO HELPED YOU WITH THE MEASURE OR INDUSTRY FOLK WHO GAVE YOU DATA]. Any remaining errors or omissions are our own.

## Table of Contents

| List of Acronyms Executive Summary                                                                                                                                | ........................................................................................................... 3 ...................................................................................................... 4 Acknowledgments......................................................................................................... 5   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Table of Contents                                                                                                                                                 | .......................................................................................................... 6                                                                                                                                                                                                                                        |
| List                                                                                                                                                              | 7                                                                                                                                                                                                                                                                                                                                                   |
| of Figures ...............................................................................................................                                        |                                                                                                                                                                                                                                                                                                                                                     |
| List of Tables .................................................................................................................                                  | 7                                                                                                                                                                                                                                                                                                                                                   |
| 1. Technology Summary .............................................................................................                                               | 1                                                                                                                                                                                                                                                                                                                                                   |
| 1. Technology Summary .............................................................................................                                               | ....................................................................................................................... 1 1                                                                                                                                                                                                                         |
| 1.1. Project Background 1.2. Plug Load Reduction for Demand Flexibility ...............................................................................           |                                                                                                                                                                                                                                                                                                                                                     |
| 2. ComStock Baseline Approach                                                                                                                                     | ................................................................................ 2                                                                                                                                                                                                                                                                  |
| 3.1. Applicability 3.2. Technology Specifics .................................................................................................................... | .................................................................................................................................. 2                                                                                                                                                                                                                |
| 3.1. Applicability 3.2. Technology Specifics .................................................................................................................... | 3 4                                                                                                                                                                                                                                                                                                                                                 |
| 3.3. Limitations and Concerns ..............................................................................................................                      |                                                                                                                                                                                                                                                                                                                                                     |
| 4. Output Variables ......................................................................................................                                        | 5                                                                                                                                                                                                                                                                                                                                                   |
| 5. Results ......................................................................................................................                                 | 5                                                                                                                                                                                                                                                                                                                                                   |
| 5. Results ......................................................................................................................                                 | ................................................................................................................ 6                                                                                                                                                                                                                                  |
| 5.1. Individual Building Test                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                     |
| 5.2. Demand Flexibility Performance ..................................................................................................                            | 7                                                                                                                                                                                                                                                                                                                                                   |

## List of Figures

| Figure 1. Building Standard Scenarios Demand Flexibility Project Workflow ............................................ 1                                                                                                                              |                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Figure 2. Default 4-hour peak (load shedding) period of each season and each state for the measures ....... 4                                                                                                                                         |                                                                                                                                                                              |
| Figure 3. Electric equipment end use for applicable and non-applicable spaces within building on August 1st, comparing the baseline result and the results applied.                                                                                   | a large office after this measure is ..................................................................................................................................... 6 |
| Figure 4. Electricity consumption for a large office building in California in winter, summer and intermediate season respectively. ............................................................................................. 7                   |                                                                                                                                                                              |
| Figure 5. Aggregated electric equipment electricity load profile for California for an example day in winter, summer and intermediate season .................................................................................                        | 8                                                                                                                                                                            |
| Figure 6. Distribution of daily percentage electric equipment load reduction during the peak period for each state .................................................................................................................................. | 9                                                                                                                                                                            |
| Figure 7. End uses comparison for applicable buildings (left) and all buildings (right) ............................. 10                                                                                                                              |                                                                                                                                                                              |
| Figure 8. Distributions of stock-level site energy savings by end use types ...............................................                                                                                                                           | 11                                                                                                                                                                           |
| Figure 9. Distributions of stock-level site energy savings by climate zone ................................................                                                                                                                           | 12                                                                                                                                                                           |

## List of Tables

Table 1. Major Changes in End Uses for Applicable Buildings ................................................................. 10

## 1. Technology Summary

## 1.1. Project Background

This measure is represented in the Building Standard Scenarios (BSS) Demand Flexibility (DF) project, which aims to provide credible estimates of the current and future DF potential for both commercial and residential building stocks. For commercial building analysis and to inform assumptions of the fraction of commercial building enduse load that can shed or shift ('DF fractions'), demand flexibility measures developed by LBNL in the OpenStudio-GEB gem [1] are integrated in ComStock. The OpenStudio-GEB gem provides modeling of technologies and controls to evaluate demand flexibility and electrification of grid-interactive efficient buildings (GEB). The gem includes existing OpenStudio measures from Building Technologies Office (BTO) funded GEB projects with revision and update, as well as new measures developed by LBNL based on priority. Currently the gem has 24 measures covering upgrades for HVAC systems, envelopes, internal loads, electric vehicles, etc., and it is actively updated to expand the coverage.

The simulation outputs from ComStock inform further analysis by LBNL's DR -Path model. In addition to DF fractions for load shedding and shifting, DR-Path also incorporates assumptions about technology fixed and variable costs, and probability of a system operator dispatching the DF events to produce estimates of the technical, economic, and achievable (market) demand response potential for a given end-use/technology, building/customer type, and geographic locations [2]. Figure 1 depicts the BSS DF workflow.

Figure 1. Building Standard Scenarios Demand Flexibility Project Workflow

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.yaml
     source: ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000001_088bd75f7bea12775ad8a2afad0938802c3563c1cfbe66bd94b5bb75c722e55e.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 1: workflow diagram of the Building Standard Scenarios demand flexibility project and its data sources](ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000001_088bd75f7bea12775ad8a2afad0938802c3563c1cfbe66bd94b5bb75c722e55e.png)

Figure 1: flow diagram of the Building Standard Scenarios (BSS) demand flexibility workflow.
Three input rows (disaggregated building end-use load; end-use fraction capable of load shedding
or shifting; grid need and dispatch of demand response) feed boxes naming the data sources and
steps: BuildStock, Scout, DR-Path, updated DF fractions from EnergyPlus modeling, exogenous
dispatch (Cambium, aggregated BSS demand) and endogenous dispatch (ReEDS).

## 1.2. Plug Load Reduction for Demand Flexibility

Plug loads represent a significant and growing component of commercial energy profiles, averaging approximately 30% of electricity use in office settings. While they may account for up to 25% of total energy consumption in minimally code-compliant buildings, their relative impact often increases in high-efficiency structures, where they can account for more than 50% of total energy consumption. This challenge is forecasted to intensify, as the United States Energy Information Administration predicts that commercial end use for office equipment will grow by 44% by 2040, significantly outpacing the 28% growth projected for other uses [3]. A large portion of it can be attributed to parasitic loads (or the power draw of a plug-load that is not performing useful work) [4]. To counter this, common strategies to reduce plug load include

- using advanced power strips (APS) with occupancy sensors or foot pedals
- using computer power management that automatically puts computers into low-power states during inactivity, which is particularly effective in office environments
- deploying behavioral interventions, such as education campaigns and competitions
- using scheduled timers and smart outlets to turn off devices such as coffee makers, printers that are often left on during non-operational hours

Demand response strategies that integrate plug load control have shown significant potential for reducing peak demand, proven by many case studies. For example, the study [5] characterizes electricity consumption of plug load devices in two recently LEED-certified buildings in California, and reached a plug load energy reduction of 17% in the library and 46% in the small office through low-cost strategies. Another study in a LEED Gold certified office building showed the automated control system reduced energy use by 21%, with competitions contributing an additional 6% [6]. A case study implemented in 8 office buildings in Minnesota found the most effective strategy is computer power management, saving an average of 29% of average workstation energy [7].  All these studies used automated energy management systems to turn off idle equipment, or used information feedback programs to ask occupants to choose which equipment to turn off, which ensured the reduction was from the idle equipment.

## 2. ComStock Baseline Approach

ComStock uses an equipment power density (EPD) value for each space type, in watts per square foot. The EPDs are derived from the DOE prototype buildings with some adjustments during the end-use load profiles calibration process. The details of the electric equipment modeling in the existing ComStock models can be found at Section 4.6 in ComStock documentation [8].

## 3. Modeling Approach

## 3.1. Applicability

This measure is only applicable to office-like space types, where there is significant load from electric devices that can be turned off or adjusted for demand response, such as offices, conference rooms, etc. The full list of applicable standard space types in each building type is shown below.

DOE prototypes:

- SecondarySchool - Office
- PrimarySchool - Office
- SmallOffice - ClosedOffice
- SmallOffice - Conference

- SmallOffice - OpenOffice
- MediumOffice - Classroom
- MediumOffice - ClosedOffice
- MediumOffice - Conference
- MediumOffice - OpenOffice
- LargeOffice - BreakRoom
- LargeOffice - Classroom
- LargeOffice - ClosedOffice
- LargeOffice - Conference
- LargeOffice - OpenOffice
- SmallHotel - Meeting
- SmallHotel - Office
- Hospital - Office
- Outpatient - Conference
- Outpatient - Office
- Warehouse - Office
- WholeBuilding - Sm Office
- WholeBuilding - Md Office
- WholeBuilding - Lg Office

## DEER prototypes

- OfficeGeneral
- OfficeOpen
- Conference
- OfficeSmall

## 3.2. Technology Specifics

The measure aims to evaluate the fraction of end use load that potentially can be reduced during the system-level peak period within the commercial building sector. The default system-level peak periods are identified for each state using the 2050 net load profile from 2023 Cambium dataset, Mid-case scenario [9]. Cambium dataset is the projection of hourly select supply- and demand-side metrics including gross demand, VRE generation, and operational costs for multiple demand futures. The peak period for this load shedding measure is defined as the four hours including the peak hour with the highest average electricity load during each season. The whole year is categorized into three seasons as summer season (June to September), winter season (December to March) and intermediate season (all other months). The identified fourhour peak periods for each state are illustrated in Figure 2. The detailed start and end time can be found in the appendix. Note that Cambium dataset does not include system load profiles for Alaska and Hawaii, and the buildings of these two states are not within the scope of the BSS DF project. However, to facilitate the ComStock simulation, Alaska and Hawaii are assigned with peak periods from the state with the similar climate zones.

Figure 2. Default 4-hour peak (load shedding) period of each season and each state for the measures

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.yaml
     source: ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000002_382887ed6903a5baa80f0789b84475869a21429c0169aee857df426f858c2244.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 2: grid of 48 state panels marking the default 4-hour peak period by season and hour of day](ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000002_382887ed6903a5baa80f0789b84475869a21429c0169aee857df426f858c2244.png)

Figure 2: small-multiples grid, one panel per state (48 panels), x-axis hour of day 0 to 24.
Colored bars mark the default 4-hour load-shedding window for winter (blue), summer (red) and
intermediate season (green). Most windows fall in the late afternoon and evening, roughly hours
16 to 21, with the season-to-season shift differing by state.

This measure will loop through all the interior electric equipment objects and clone their schedules for each season if the equipment belongs to an applicable space type (listed in the previous section). The state of the building is identified from the additionalProperties object and the measure will adjust the equipment schedule on each day during the corresponding peak period of the state and the season. During the peak period, the electric equipment loads are reduced by 20% for applicable spaces. The 20% occupied reduction threshold represents the low end of the range found by previous studies in offices [6], [7]. For times outside of the peak period, the existing schedules in the model stays unchanged. The reduction is applied daily, and the expected outcome of the simulation is the distribution of daily percentage reduction of the end use load by the measure. The detailed demand response event dispatch strategy will be considered outside the ComStock simulation by DR-Path.

It is worth noting that the measure offers the flexibility for users to specify the start and end date and time of multiple peak periods when the electric equipment schedule is adjusted, as well as the percentage of the equipment load reduction. If no user inputs are provided, the aforementioned default values will be used.

## 3.3. Limitations and Concerns

Several limitations and concerns of the measure are identified as follows.

- The measure assumes that low-priority devices are controllable (either via deviceintegrated controls or via communication with BAS), which is idealistic and dependent on the adoption of these control technologies.
- The plug load reduction event is applied for every day throughout the year. In reality, demand response programs are structured to limit events to a small number of days and total hours, but the dispatch strategy is not part of this study and will be analyzed in postprocessing by another tool.
- The start of the peak period is defined by the seasonal peak hour of the aggregated state-

level load profile from Cambium data, which does not necessarily align with the peak hour of a particular electricity system or individual building. Besides, any demand-side improvements on building energy consumption is not reflected in the Cambium loads, so if these improvements are significant enough to alter the peak timings, it's not captured in the dispatch assumptions.

- The measure can only be applicable to those schedules in scheduleRuleSet format, but this is likely to cover all models in ComStock.

## 4. Output Variables

Since the measure is implemented under the BSS DF project, the outputs from ComStock simulation will be used for further processing to calculate the demand decrease percentage during peak period (D3), aggregated at state level. The D3 metric is defined in the equation below.

Where 𝑠𝑝 is the shedding (peak) period of the day, 𝐸𝑏𝑎𝑠𝑒 and 𝐸𝑚𝑒𝑎𝑠𝑢𝑟𝑒 are the baseline and postmeasure electricity demand for the specific end use targeted by the measure, which is electric equipment electricity use in this case. The denominator of the equation should include all the buildings with the target end use type, which is all commercial buildings for the lighting measure.

To generate the metric, the building-level ComStock timeseries are aggregated into state-level timeseries load profiles during post-processing. Since the ComStock sampling method can use one building model to represent buildings across multiple states, the identified peak period from the model to apply change can be different from the peak period used for the state to calculate D3, which impairs the effectiveness of the measure. To keep most of the useful models while reducing the noise in results as much as possible, when aggregating the state-level load, buildings from states with a peak period shifted by more than 1 hour are excluded. The D3 value is calculated for each day, and the 75 th percentile of the annual distribution of D3 will be used in the following analysis of DR-Path.

## 5. Results

In this section, results are presented both for individual buildings and at stock level through distributions. Individual building result is used for quality assurance/quality control and to showcase the mechanism of the measure. Stock-level results include the combined impact of all the analyzed buildings in ComStock, including buildings that are not applicable to this measure. Therefore, they do not necessarily represent the energy savings of a particular or average building. Stock level results should not be interpreted as the average savings that a building might realize by implementing the measure. Apart from the metrics related to total energy use, the stock level results focus on the demand flexibility metrics.

## 5.1. Individual Building Test

The intent of this section is to demonstrate the impact of the measure on a sample model. Multiple models of different building types and states were tested. Here the result of a large office building in California is used to illustrate the effect of the measure. In this sample building, the space type 'OfficeOpen' and 'OfficeSmall' are applicable for this measure, while other spaces 'LobbyWaiting' and 'MechElecRoom' are not applicable as per our space type applicability assumptions. The reduction of the plug load is 20%, and the demand response event is dispatched everyday throughout the year for 4 hours, determined by the state and season. Figure 3 confirms that the interior equipment electricity rate is only changed for office spaces but not the other two space types.

Figure 3. Electric equipment end use for applicable and non-applicable spaces within a large office building on August 1st, comparing the baseline result and the results after this measure is applied.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.yaml
     source: ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000003_8b97c75a880632690b40690a716a51404cd3e5339a8d4030930f2268efe029ea.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 3: electric equipment power for applicable and non-applicable space types of a California large office](ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000003_8b97c75a880632690b40690a716a51404cd3e5339a8d4030930f2268efe029ea.png)

Figure 3: two line panels of electric equipment electricity rate in W over 08/01 to 08/03 for a
large office in California. Top panel: applicable space types OfficeOpen and OfficeSmall,
baseline versus measure, with the measure dropping during the green-shaded evening shed windows.
Bottom panel: non-applicable LobbyWaiting and MechElecRoom, where baseline and measure coincide.

As shown in Figure 4, the electricity load is reduced during the shedding period, which is 17:0021:00, 18:00-22:00, and 17:00-21:00 for California in winter, summer, and intermediate season respectively. Since the peak period was identified from the grid-level net load, it does not necessarily coincide with the single-building peak period. Therefore, the maximum load value is not necessarily reduced for any single building.

Figure 4. Electricity consumption for a large office building in California in winter, summer and intermediate season respectively.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.yaml
     source: ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000004_bb896f2b1288aee3ac43dcbfcb12d97541c24af4207383dd8de7c62bbf8fb15a.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 4: whole-building net electricity of a California large office on three days, baseline versus DF plug measure](ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000004_bb896f2b1288aee3ac43dcbfcb12d97541c24af4207383dd8de7c62bbf8fb15a.png)

Figure 4: three stacked line charts of whole-building net electricity consumption in W for a
large office in California on 01/01, 08/01 and 05/01. Baseline (blue) and DF plug measure
(orange) overlap except in the green-shaded shed period in the late afternoon and evening, where
the measure line runs slightly below the baseline.

## 5.2. Demand Flexibility Performance

The simulation for the 10k samples is used to demonstrate the aggregated results. Figure 5 illustrates a daily electric equipment electricity load for each season to show that the load was reduced during the corresponding peak period. The peak periods do not necessarily coincide with the simulated peaks from ComStock, because they were identified from the projected grid-side net load shape including sectors other than commercial buildings. Besides, there can also be a gap between the ComStock baseline load shape and the real load shape from the utility AMI data For each day the measure is applied, a D3 value (percentage decrease) for the electric equipment end use is calculated, and the distribution of the daily D3 values for each state is illustrated in Figure 6 for the 10k samples, sorted by the 75 th percentile, which is used to represent the demand flexibility potential of the measure in DR-Path. The measure reduces electric equipment load by 20% but it only applies to office-like spaces. The ratio of applicable space types in each applicable building type is different. For example, only 5% of the floor area in small hotels and warehouses are applicable for the Plug Load measure, while 63% of primary schools is applicable. Among all applicable building types, SmallHotel, Warehouse, Hospital, and Outpatient have smaller ratios of applicable spaces. Among all applicable building types, by weighted sqft, DC only has 8% of these four building types with lower ratios, while WV has 42%, which leads to the D3 differences across states.

Figure 5. Aggregated electric equipment electricity load profile for California for an example day in winter, summer and intermediate season

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.yaml
     source: ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000005_ff5640d3cdb2a11560ac1a261cee2d531995d43c99841e5ad0e7745fb2bda408.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 5: aggregated California electric equipment load profiles for three seasons, baseline versus post-measure](ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000005_ff5640d3cdb2a11560ac1a261cee2d531995d43c99841e5ad0e7745fb2bda408.png)

Figure 5: three stacked line panels (winter, summer, intermediate) of aggregated electric
equipment electricity in MWh (y, about 250,000 to 950,000) over one example day for California.
Baseline (blue) and post-measure (orange) overlap until about hour 17, where the post-measure
profile steps down for the 4-hour shed window and rejoins the baseline at about hour 21.

Figure 6. Distribution of daily percentage electric equipment load reduction during the peak period for each state

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.yaml
     source: ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000006_33b521abd4e24c3577da3b586d71e7778662affc58577e64cab2e7163cb75198.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 6: box plot by state of daily percentage electric equipment load reduction during the peak period](ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000006_33b521abd4e24c3577da3b586d71e7778662affc58577e64cab2e7163cb75198.png)

Figure 6: box plot of daily percentage electric equipment load reduction during the peak period
(y, 0 to 14%) for each state (x), median as a dashed line and 75th percentile in red. DC is
highest near 14%, MA and NJ near 10%; most states fall between about 4 and 9%, declining toward
WV at the right.

## 5.3. Stock Energy Impacts

The object of the measure is demand flexibility and the applicable spaces are limited , so it's expected that the total site energy impact is not prominent. The total annual site energy was decreased by 0.20% for applicable commercial buildings and 0.13% for the whole commercial stock, shown in Figure 7. The decrease is primarily attributed to savings from interior equipment and cooling energy, despite the increase in heating energy due to the reduction in internal load.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.yaml
     source: ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000007_45c2152641edc489e26734e8b9e159f3fe668db4fd8626238212bf0a724a5700.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 7: stock annual energy by end use and fuel, baseline versus GEB_DF_Plug, applicable buildings and all buildings](ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000007_45c2152641edc489e26734e8b9e159f3fe668db4fd8626238212bf0a724a5700.png)

Figure 7: two stacked bar panels of annual energy consumption in TBtu, left for applicable
buildings (Baseline 2965 vs GEB_DF_Plug 2959) and right for all buildings (4865 vs 4859),
segmented by end use and fuel per the legend. The interior equipment electricity segment shrinks
slightly while heating segments grow. See Table 1.

Figure 7. End uses comparison for applicable buildings (left) and all buildings (right) Table 1. Major Changes in End Uses for Applicable Buildings

| End Use Type                    |   Saving (TBtu) |   Percentage Saving (%) |
|---------------------------------|-----------------|-------------------------|
| Interior Equipment, Electricity |            7.18 |                    0.97 |
| Cooling, Electricity            |            0.91 |                    0.13 |
| Fans, Electricity               |            0.23 |                    0.04 |
| Heating, Electricity            |           -0.60 |                   -0.23 |
| Heating, Natural Gas            |           -1.46 |                   -0.15 |
| Heating, District Heating       |           -0.16 |                   -0.39 |

The interior equipment electricity use is reduced by around 1% due to turning off electric devices during the DF periods. The heating end uses are increased in most buildings due to the reduced internal loads from turning off electric devices, which also leads to the decrease in cooling load. Minimal changes to other end uses are observed (e.g. fans and pumps), reflecting the internal load changes caused by electric equipment load reduction.

Figure 8. Distributions of stock-level site energy savings by end use types

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.yaml
     source: ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000008_4e9f710f61b340d29d76c756b01ffda85f2a3f87d04d483f7d06c0794c931304.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 8: distributions of percent site energy savings by end use for the GEB_DF_Plug upgrade](ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000008_4e9f710f61b340d29d76c756b01ffda85f2a3f87d04d483f7d06c0794c931304.png)

Figure 8: horizontal distribution plot of percent site energy savings by end use (x, -100 to
40%), one row per end use and fuel with its model count n, for Upgrade 34.0 GEB_DF_Plug
(unweighted). Electricity interior equipment sits slightly positive, natural gas heating and
electricity heating spread widest around zero, and the remaining end uses center on zero. See
Table 1.

The measure is applicable to all climate zones, and the demand flexibility measure is not related to weather conditions. Therefore, the site energy saving is not correlated with climate zones, as shown in Figure 9.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.yaml
     source: ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000009_88c43c8d1abbf2dac265a7beb61f0d0c10e651a234fef91eb463d38e246f621e.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 9: distributions of percent site energy savings by ASHRAE climate zone for the GEB_DF_Plug upgrade](ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000009_88c43c8d1abbf2dac265a7beb61f0d0c10e651a234fef91eb463d38e246f621e.png)

Figure 9: horizontal violin plot of percent site energy savings (x, -3 to 6%) by climate zone 1A
through 8 with the model count n per zone, for Upgrade 34.0 GEB_DF_Plug (unweighted). Every zone
centers a few tenths of a percent above zero with long thin tails; there is no visible trend
with climate zone.

## Figure 9. Distributions of stock-level site energy savings by climate zone

## References

- [1] S. Kaiyu, Z. Wanni, M. Nathan, and F. Katherine, OpenStudio GEB Gem . Lawrence Berkeley National Laboratory. [Online]. Available: https://github.com/LBNL-ETA/Openstudio-GEB-gem
- [2] B. Gerke et al. , 'The California Demand Response Potential Study, Phase 4: Report on Shed and Shift Resources Through 2050,' 2024.
- [3] C. Angela, 'Flexible Control Strategies for Plug Loads to Mitigate Electricity Waste and Support Demand Response,' Electric Power Research Institute, Mar. 2023. [Online]. Available: https://www.energy.ca.gov/sites/default/files/2023-03/CEC-500-2023-001.pdf
- [4] C. Lobato, M. Sheppy, L. Brackney, S. Pless, and P. Torcellini, 'Selecting a Control Strategy for Plug and Process Loads,' NREL/TP -5500-51708, 1051936, Sept. 2012. doi: 10.2172/1051936.
- [5] M. Catherine and M. Laura, 'COMMERCIAL OFFICE PLUG LOAD SAVINGS AND ASSESSMENT,' New Buildings Institute, Dec. 2011.
- [6] I. Metzger, A. Kandt, and O. VanGeet, 'Plug Load Behavioral Change Demonstration Project,' NREL/TP-7A40-52248, 1023720, Aug. 2011. doi: 10.2172/1023720.
- [7] H. Scott, P. Chris, C. Maureen, and M. Greg, 'Impacts of Office Plug Load Reduction Strategies,' Minnesota Department of Commerce, Oct. 2016.
- [8] A. Parker et al. , 'ComStock Reference Documentation: 2024 Release,' National Renewable Energy Laboratory, 2024.
- [9]  P. Gagnon et al. , 'Cambium 2023 Scenario Descriptions and Documentation,' 2024.

## Appendix

The table lists the default peak period for each season for each state, determined from the power system net load profile from Cambium dataset (Mid-case scenario in 2050). The default length of load shedding is four hours.

| State   | Summer Peak Start   | Summer Peak End   | Winter Peak Start   | Winter Peak End   | Intermediate Peak Start   | Intermediate Peak End   |
|---------|---------------------|-------------------|---------------------|-------------------|---------------------------|-------------------------|
| IA      | 8/28/50 17:00       | 8/28/50 21:00     | 1/19/50 17:00       | 1/19/50 21:00     | 11/4/50 17:00             | 11/4/50 21:00           |
| WV      | 7/18/50 16:00       | 7/18/50 20:00     | 1/18/50 17:00       | 1/18/50 21:00     | 5/29/50 16:00             | 5/29/50 20:00           |
| MA      | 6/22/50 17:00       | 6/22/50 21:00     | 12/14/50 17:00      | 12/14/50 21:00    | 10/18/50 17:00            | 10/18/50 21:00          |
| VT      | 7/12/50 18:00       | 7/12/50 22:00     | 12/25/50 18:00      | 12/25/50 22:00    | 11/28/50 17:00            | 11/28/50 21:00          |
| WI      | 7/6/50 18:00        | 7/6/50 22:00      | 12/19/50 17:00      | 12/19/50 21:00    | 11/8/50 17:00             | 11/8/50 21:00           |
| CT      | 6/22/50 17:00       | 6/22/50 21:00     | 12/7/50 17:00       | 12/7/50 21:00     | 5/30/50 17:00             | 5/30/50 21:00           |
| TN      | 6/30/50 17:00       | 6/30/50 21:00     | 1/18/50 17:00       | 1/18/50 21:00     | 5/28/50 17:00             | 5/28/50 21:00           |
| NY      | 7/6/50 18:00        | 7/6/50 22:00      | 1/20/50 17:00       | 1/20/50 21:00     | 11/16/50 17:00            | 11/16/50 21:00          |
| UT      | 8/8/50 18:00        | 8/8/50 22:00      | 12/29/50 17:00      | 12/29/50 21:00    | 11/13/50 17:00            | 11/13/50 21:00          |
| VA      | 7/7/50 18:00        | 7/7/50 22:00      | 12/29/50 16:00      | 12/29/50 20:00    | 11/27/50 16:00            | 11/27/50 20:00          |
| DC      | 7/7/50 18:00        | 7/7/50 22:00      | 12/29/50 16:00      | 12/29/50 20:00    | 11/27/50 16:00            | 11/27/50 20:00          |
| SD      | 6/29/50 15:00       | 6/29/50 19:00     | 12/26/50 16:00      | 12/26/50 20:00    | 4/17/50 18:00             | 4/17/50 22:00           |
| OH      | 7/7/50 17:00        | 7/7/50 21:00      | 1/3/50 17:00        | 1/3/50 21:00      | 11/28/50 17:00            | 11/28/50 21:00          |

| SC            | 7/28/50 19:00   | 7/28/50 23:00   | 2/9/50 18:00   | 2/9/50 22:00   | 10/5/50 17:00   | 10/5/50 21:00   |
|---------------|-----------------|-----------------|----------------|----------------|-----------------|-----------------|
| 9/25/50 17:00 | 9/25/50 21:00   | 1/18/50 18:00   | 1/18/50 22:00  | 10/6/50 19:00  | 10/6/50 23:00   | MT              |
| 7/30/50 18:00 | 7/30/50 22:00   | 1/18/50 17:00   | 1/18/50 21:00  | 5/28/50 18:00  | 5/28/50 22:00   | MS              |
| 8/9/50 18:00  | 8/9/50 22:00    | 3/11/50 17:00   | 3/11/50 21:00  | 10/31/50 17:00 | 10/31/50 21:00  | NM              |
| 7/6/50 17:00  | 7/6/50 21:00    | 12/7/50 17:00   | 12/7/50 21:00  | 5/31/50 17:00  | 5/31/50 21:00   | NJ              |
| 6/30/50 18:00 | 6/30/50 22:00   | 1/3/50 18:00    | 1/3/50 22:00   | 5/26/50 18:00  | 5/26/50 22:00   | GA              |
| 8/14/50 18:00 | 8/14/50 22:00   | 12/14/50 17:00  | 12/14/50 21:00 | 10/2/50 17:00  | 10/2/50 21:00   | CA              |
| 7/7/50 18:00  | 7/7/50 22:00    | 12/29/50 16:00  | 12/29/50 20:00 | 11/8/50 16:00  | 11/8/50 20:00   | IL              |
| 8/9/50 18:00  | 8/9/50 22:00    | 3/30/50 18:00   | 3/30/50 22:00  | 10/3/50 17:00  | 10/3/50 21:00   | AZ              |
| 8/28/50 18:00 | 8/28/50 22:00   | 12/12/50 17:00  | 12/12/50 21:00 | 10/3/50 17:00  | 10/3/50 21:00   | TX              |
| 8/9/50 17:00  | 8/9/50 21:00    | 12/7/50 17:00   | 12/7/50 21:00  | 11/28/50 17:00 | 11/28/50 21:00  | NH              |
| 6/30/50 17:00 | 6/30/50 21:00   | 12/7/50 17:00   | 12/7/50 21:00  | 11/27/50 17:00 | 11/27/50 21:00  | DE              |
| 8/17/50 17:00 | 8/17/50 21:00   | 1/12/50 17:00   | 1/12/50 21:00  | 10/25/50 17:00 | 10/25/50 21:00  | WA              |
| 9/18/50 17:00 | 9/18/50 21:00   | 1/12/50 17:00   | 1/12/50 21:00  | 10/26/50 16:00 | 10/26/50 20:00  | OR              |
| 7/7/50 17:00  | 7/7/50 21:00    | 3/2/50 18:00    | 3/2/50 22:00   | 11/21/50 17:00 | 11/21/50 21:00  | MI              |
| 7/15/50 17:00 | 7/15/50 21:00   | 12/12/50 17:00  | 12/12/50 21:00 | 11/4/50 16:00  | 11/4/50 20:00   | MN              |
| 9/18/50 18:00 | 9/18/50 22:00   | 2/7/50 8:00     | 2/7/50 12:00   | 10/26/50 8:00  | 10/26/50 12:00  | WY              |
| 7/7/50 18:00  | 7/7/50 22:00    | 12/28/50 17:00  | 12/28/50 21:00 | 11/14/50 17:00 | 11/14/50 21:00  | IN              |
| 9/6/50 15:00  | 9/6/50 19:00    | 2/14/50 4:00    | 2/14/50 8:00   | 11/17/50 3:00  | 11/17/50 7:00   | OK              |
| 7/11/50 18:00 | 7/11/50 22:00   | 12/29/50 17:00  | 12/29/50 21:00 | 5/17/50 18:00  | 5/17/50 22:00   | NV              |
| 8/1/50 18:00  | 8/1/50 22:00    | 1/17/50 17:00   | 1/17/50 21:00  | 11/1/50 17:00  | 11/1/50 21:00   | KS              |
| 6/22/50 17:00 | 6/22/50 21:00   | 1/3/50 17:00    | 1/3/50 21:00   | 5/29/50 17:00  | 5/29/50 21:00   | PA              |
| 7/6/50 18:00  | 7/6/50 22:00    | 12/29/50 8:00   | 12/29/50 12:00 | 11/16/50 16:00 | 11/16/50 20:00  | MO              |
| 8/10/50 17:00 | 8/10/50 21:00   | 2/15/50 17:00   | 2/15/50 21:00  | 11/28/50 16:00 | 11/28/50 20:00  | ME              |
| 7/7/50 19:00  | 7/7/50 23:00    | 12/12/50 17:00  | 12/12/50 21:00 | 11/29/50 17:00 | 11/29/50 21:00  | KY              |
| 8/9/50 18:00  | 8/9/50 22:00    | 12/26/50 18:00  | 12/26/50 22:00 | 11/27/50 16:00 | 11/27/50 20:00  | CO              |
| 8/16/50 18:00 | 8/16/50 22:00   | 12/29/50 17:00  | 12/29/50 21:00 | 11/30/50 17:00 | 11/30/50 21:00  | NC              |
| 7/24/50 18:00 | 7/24/50 22:00   | 1/3/50 18:00    | 1/3/50 22:00   | 5/26/50 18:00  | 5/26/50 22:00   | AL              |
| 7/31/50 19:00 | 7/31/50 23:00   | 12/26/50 19:00  | 12/26/50 23:00 | 4/17/50 18:00  | 4/17/50 22:00   | ND              |

| AR   | 9/6/50 17:00   | 9/6/50 21:00   | 12/12/50 17:00   | 12/12/50 21:00   | 5/30/50 18:00   | 5/30/50 22:00   |
|------|----------------|----------------|------------------|------------------|-----------------|-----------------|
| FL   | 7/27/50 18:00  | 7/27/50 22:00  | 1/3/50 18:00     | 1/3/50 22:00     | 5/31/50 18:00   | 5/31/50 22:00   |
| ID   | 8/5/50 19:00   | 8/5/50 23:00   | 1/12/50 17:00    | 1/12/50 21:00    | 11/15/50 18:00  | 11/15/50 22:00  |
| LA   | 6/29/50 18:00  | 6/29/50 22:00  | 12/12/50 17:00   | 12/12/50 21:00   | 5/30/50 18:00   | 5/30/50 22:00   |
| MD   | 7/6/50 17:00   | 7/6/50 21:00   | 1/9/50 16:00     | 1/9/50 20:00     | 5/26/50 17:00   | 5/26/50 21:00   |
| NE   | 7/15/50 15:00  | 7/15/50 19:00  | 3/16/50 17:00    | 3/16/50 21:00    | 10/31/50 16:00  | 10/31/50 20:00  |
| RI   | 7/28/50 18:00  | 7/28/50 22:00  | 12/7/50 17:00    | 12/7/50 21:00    | 10/18/50 18:00  | 10/18/50 22:00  |
| HI   | 7/27/50 18:00  | 7/27/50 22:00  | 1/3/50 18:00     | 1/3/50 22:00     | 5/31/50 18:00   | 5/31/50 22:00   |
| AK   | 7/15/50 17:00  | 7/15/50 21:00  | 12/12/50 17:00   | 12/12/50 21:00   | 11/4/50 16:00   | 11/4/50 20:00   |
