<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/92546.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/92546.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/92546.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/92546.md | section: Release | lines: 77-101 -->
## Release

- Heating and cooling loads are met by air conditioned at 100% efficiency and supplied directly to the zone.
- The measure application is agnostic of the HVAC system type found in original building model. Impacts of system-specific operation, such as simultaneous heating and cooling (reheat), are not considered in this study.
- Outdoor air is introduced to the ideal air supply for conditioning per design outdoor air specifications with schedules aligning to zone occupancy.
- A constant cooling sensible heat ratio of 0.75 is applied.
- Fan energy and its corresponding impacts to heating and cooling loads are not modeled in this study.
- Active humidity control is not applied, aligning with current ComStock baseline assumptions.
- This measure is applicable to every ComStock model, comprising 100% of the floor area modeled in ComStock. No ComStock models are excluded.

2025 Release 1: 2025/comstock\_amy2018\_release\_1/

Note that results for impacts on metrics like greenhouse gas emissions and energy bills are not presented for this measure scenario since this study is only intended to provide thermal heating and cooling loads for ComStock models. This measure scenario should only be used as a resource to analyze building thermal loads and does not represent an actual technology study. Figure 1 shows the application of this measure on annual stock site energy between the ComStock baseline and the Ideal Thermal Air Loads scenario, where heating and cooling energy of all fuel types are converted to district heating and district cooling sources, respectively.

Figure 1 . Comparison of annual site energy consumption between the ComStock baseline and the Ideal Thermal Air Loads scenario. Energy consumption is categorized both by fuel type and end use.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/92546.yaml
     source: 92546_images/image_000002_543a3e3d13c7a6e6cb9fad1e0a136486212cba88db21e5fd895a0c86c5594d83.png
     method: vision-description
     described: 2026-08-20 -->

![Stacked column chart of annual stock site energy consumption by end use and fuel, Baseline vs Ideal Thermal Air Loads](92546_images/image_000002_543a3e3d13c7a6e6cb9fad1e0a136486212cba88db21e5fd895a0c86c5594d83.png)

Figure 1. Stacked column chart comparing annual stock site energy consumption (TBtu), y-axis 0 to about 5000, for two scenarios: ComStock Baseline (total 4763) and Ideal Thermal Air Loads (total 5049). Each column is segmented by end use and fuel per the legend (Interior Equipment, Fans, Cooling, Interior Lighting, Water Systems, Heating, Heat Recovery, Heat Rejection, Pumps, Refrigeration across Electricity, Natural Gas, District Heating, District Cooling, and Other Fuel). Interior Equipment (726.4 Electricity, 305.6 Natural Gas) is identical in both. In the baseline, legible segments include Fans Electricity 557.4, Cooling Electricity 704.5, and Heating Natural Gas 574.5. In the Ideal Thermal Air Loads scenario, heating and cooling are re-metered as district energy: a large District Cooling segment 1876.3 and a District Heating segment near 1610.6, while Fans Electricity drops to essentially zero. The takeaway: converting all HVAC to 100%-efficient ideal air roughly triples cooling energy (COP 1 vs baseline DX COP 3-4), slightly increases heating, and eliminates supply/return fan energy.

