<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_Lighting Control for Emission Reduction.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/3b69decb4e5f7bb3d6cc24f6224b318c921fd45f/assets/files/ComStock%20Measure%20Doc_Lighting%20Control%20for%20Emission%20Reduction.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_Lighting%20Control%20for%20Emission%20Reduction.pdf | corpus_version: e7ffee7a | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_Lighting Control for Emission Reduction.md | section: 2 ComStock Baseline Approach | lines: 169-241 -->
## 2 ComStock Baseline Approach

This measure modifies the existing model interior lighting schedules during the daily peak demand windows (on-peak periods) only. For times outside of the event, the existing lighting schedules in the model are unchanged. The details of the lighting schedules, technology, and power in the existing ComStock models can be found in Section 4.2 'Hours of Operation and Occupancy' and Section 4.5.1 ' Interior Lighting ' in the ComStock Reference Documentation [30] for default schedules, as well as Section 3.3.4 'Interior Lighting Schedule Magnitude Variability' in the End-Use Load Profiles project report [31] for base-to-peak variation applied to the default lighting schedules.

ComStock interior lighting is determined by a lighting technology generation approach, with each generation representing a collection of lighting technologies typically installed during a given time period. ComStock assumes four categories of lighting: general (overhead lighting), task (lights focused on specific areas), supplemental (supplemental lighting), and wall wash (illuminates vertical surface). The lighting technologies used in each category across the ComStock lighting generations are listed in Table. Generations 4 -8 represent varying efficacy levels of LEDs, with Generation 4 being the first LED technology to market, and Generation 8 being the estimated technology level in 2035.

Table 1. Lighting Generations and Associated Technologies for Each Category

| Lighting Generation   | General Lighting Technology   | General Lighting (High Bay) Technology       | Task Lighting Technology   | Supplemental Lighting Technology   | Wall Wash Lighting Technology   |
|-----------------------|-------------------------------|----------------------------------------------|----------------------------|------------------------------------|---------------------------------|
| 1                     | T12 linear fluorescent        | High-intensity discharge (HID) mercury vapor | Incandescent A-shape       | Incandescent decorative            | Incandescent decorative         |
| 2                     | T8 linear fluorescent         | HID metal halide                             | Halogen A-shape            | Halogen decorative                 | Halogen decorative              |
| 3                     | T5 linear fluorescent         | HID metal halide                             | Compact fluorescent screw  | Compact fluorescent pin            | Compact fluorescent pin         |
| 4 - 8                 | LED linear                    | LED high bay luminaire                       | LED general purpose        | LED decorative                     | LED directional                 |

ComStock uses a similar approach to the ASHRAE 90.1 Lighting Subcommittee for determining the lighting power density allowance for a given space type. Table provides the average installed building-level lighting power densities in ComStock by building type and lighting generation.

Table 2. Average Building-Level Lighting Power Density (W/ft 2 ) by Lighting Generation and Building Type

|                         |   Lighting Generation |   Lighting Generation |   Lighting Generation |   Lighting Generation |   Lighting Generation |
|-------------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| Building Type           |                     1 |                     2 |                     3 |                     4 |                     5 |
| full_service_restaurant |                  1.51 |                  0.96 |                  0.45 |                  0.43 |                  0.39 |
| hospital                |                  1.59 |                  1.07 |                  0.63 |                  0.58 |                  0.52 |

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

Specifically, the lighting generations and corresponding technologies were assigned to each building model during the sampling process, based on validated distribution data (Figure 1), and introduced with variability representing realistic installation trends of different generations and impact of building sizes. Default interior lighting schedules come from the OpenStudioStandards U.S. Department of Energy prototype building models [32]. The schedules are then adjusted with varying base-to-peak ratios to incorporate impact from characteristics such as building types and operating hours.

Figure 1. 'Truth' lighting generation distribution (01) and comparison of 2017 and 2020 ComStock sampling results

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Lighting Control for Emission Reduction.yaml
     source: ComStock_Measure_Doc_Lighting_Control_for_Emission_Reduction_images/image_000001_11b29adf94dffe70c8cf60330cee58e62344ca70a3e892540ca3ebf7bae80b96.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 1: stacked bars of lighting generation shares, truth versus ComStock sampling, 2015 to 2035](ComStock_Measure_Doc_Lighting_Control_for_Emission_Reduction_images/image_000001_11b29adf94dffe70c8cf60330cee58e62344ca70a3e892540ca3ebf7bae80b96.png)

Figure 1: stacked bar chart of lighting generation shares (y, 0 to 1) with bars for Truth 2015,
Truth and Sampling 2017, Truth and Sampling 2020 (boxed), and Truth 2025, 2030 and 2035; legend
gen1_t12_incandescent through gen8_led. The 2017 and 2020 sampled shares track their truth bars
within a few hundredths (gen2 0.488 vs 0.480 in 2017); LED generations dominate by 2035. See
Table 1 and Table 2.

Figure 2 shows two sets of example weekday lighting default schedules versus the corresponding base-to-peak ratio-adjusted schedules for large and small office buildings in the ComStock baseline models.

Figure 2. Example weekday lighting schedules (fractional factor to fully ON)

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Lighting Control for Emission Reduction.yaml
     source: ComStock_Measure_Doc_Lighting_Control_for_Emission_Reduction_images/image_000002_25cd7e09da1026abe7306b1a8552789d163dfc0564fe156756e58921ac1aad75.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 2: example weekday lighting schedules, default versus base-to-peak-ratio adjusted, large and small office](ComStock_Measure_Doc_Lighting_Control_for_Emission_Reduction_images/image_000002_25cd7e09da1026abe7306b1a8552789d163dfc0564fe156756e58921ac1aad75.png)

Figure 2: line chart of weekday lighting schedule fraction (y, 0 to 1) against hour of day (x,
0:00 to 24:00). Large office default (dashed orange) and BPR adjusted (solid orange) rise from
about 0.05 at night to about 0.85 midday; small office default (dashed blue) spans a wider
daytime plateau, and its BPR-adjusted schedule (solid blue) is nearly flat near 0.8 to 0.85 all
day.

