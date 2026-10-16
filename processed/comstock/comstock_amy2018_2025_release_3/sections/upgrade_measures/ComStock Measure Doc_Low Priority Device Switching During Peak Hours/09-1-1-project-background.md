<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/3b69decb4e5f7bb3d6cc24f6224b318c921fd45f/assets/files/ComStock%20Measure%20Doc_Low%20Priority%20Device%20Switching%20During%20Peak%20Hours.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_Low%20Priority%20Device%20Switching%20During%20Peak%20Hours.pdf | corpus_version: comstock_amy2018_2025_release_3-v2 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.md | section: 1.1. Project Background | lines: 111-131 -->
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

