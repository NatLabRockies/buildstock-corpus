<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/2_ResStockStructureAndSampling.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/2_ResStockStructureAndSampling.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/2_ResStockStructureAndSampling.md | section: Sampling | lines: 37-53 -->
## Sampling

ResStock does not model actual buildings (for example: the apartment complex at 123 Main Street). Instead, the housing characteristic distributions are sampled hundreds of thousands of times—typically 550,000—to create a synthetic stock representation of U.S. housing units. Each sampled housing unit is assigned an option for each of the ResStock housing characteristics. Within the ResStock workflow the full set of sampled housing units and their associated characteristics is referred to as the `buildstock.csv`. An illustrative example of some characteristics of a ResStock model is shown in Figure “An illustrative example of a representative housing unit sample from ResStock (does not show all characteristics available in ResStock)”. More information about how the sampling is performed can be found in Section “Sampling Methodology”. Each of the 550,000 representative samples in the `buildstock.csv` can be thought of as an archetype residential housing unit description, meaning that each synthetic building represents approximately 250 real U.S. housing units.

<figure id="fig:illustrative_sample">
<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/technical_reference/docs/technical_reference_guide/2_ResStockStructureAndSampling.yaml
     source: images/illustrative_sample.png
     method: vision-description
     described: 2026-11-11 -->

<img alt="Table shown as a picture: the characteristics of one illustrative ResStock housing unit sample" src="images/illustrative_sample.png" style="width:100.0%" />

A table shown as a picture, listing one illustrative housing unit sample in three pairs of columns. IECC climate zone 5A; city Cleveland, OH; building type single-family detached; occupants 3; vintage <1940; floor area bin 1500-1999; bedrooms 3; stories 2. Heating: natural gas furnace, 80% AFUE; cooling: central AC, SEER 13; setpoints: heating 70°F, cooling 72°F; setpoint offsets: heating 3°F, cooling 2°F; refrigerator EF 17.6; clothes washer EnergyStar, 123 rated kWh; dishwasher 290 rated kWh; cooking range gas. Wall type wood stud; wall insulation uninsulated; attic type vented attic; attic insulation uninsulated; infiltration 8 ACH50; foundation type unheated basement; ducts 10% leakage, uninsulated; windows double, clear, non-metal, air.

<figcaption>An illustrative example of a representative housing unit sample from ResStock (does not show all characteristics available in ResStock)</figcaption>
</figure>

