<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/92504.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/92504.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/92504.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/92504.md | section: 2.2  Interior Lighting | lines: 227-275 -->
## 2.2  Interior Lighting

This measure modifies the existing model (interior) lighting schedules during the daily peak demand windows (specifically on-peak periods) only. For times outside of the event, the existing lighting schedules in the model are unchanged. The details of the lighting schedules, technology, and power in the existing ComStock models can be found in Section 4.2 'Hours of Operation and Occupancy' and Section 4.5.1 'Interior Lighting' in the ComStock Documentation [1] for default schedules, and Section 3.3.4 'Interior Lighting Schedule Magnitude Variability' in the End-Use Load Profiles project report [2] for base-to-peak variation applied to the default lighting schedules.

ComStock interior lighting is determined by a lighting technology generation approach, with each generation representing a collection of lighting technologies typically installed during a given time period. ComStock assumes four categories of lighting: general (overhead lighting), task (lights focused on specific areas), supplemental (additional lighting), and wall wash (illuminates vertical surfaces). The lighting technologies used in each category across the ComStock lighting generations are listed in Table 1. Generations 4-8 represent varying efficacy levels of LEDs, with Generation 4 being the first LED technology to market, and Generation 8 being the estimated technology level in 2035.

Table 1. Lighting Generations and Associated Technologies for Each Category

| Lighting Generation   | General Lighting Technology   | General Lighting (High Bay) Technology   | Task Lighting Technology   | Supplemental Lighting Technology   | Wall Wash Lighting Technology   |
|-----------------------|-------------------------------|------------------------------------------|----------------------------|------------------------------------|---------------------------------|
| Gen 1                 | T12 linear fluorescent        | High-intensity discharge mercury vapor   | Incandescent A- shape      | Incandescent decorative            | Incandescent decorative         |
| Gen 2                 | T8 linear fluorescent         | High-intensity discharge metal halide    | Halogen A-shape            | Halogen decorative                 | Halogen decorative              |
| Gen 3                 | T5 linear fluorescent         | High-intensity discharge metal halide    | Compact fluorescent screw  | Compact fluorescent pin            | Compact fluorescent pin         |
| Gen 4-8               | LED linear                    | LED high bay luminaire                   | LED general purpose        | LED decorative                     | LED directional                 |

ComStock uses a similar approach to the ASHRAE 90.1 Lighting Subcommittee for determining the lighting power density allowance for a given space type. Table 2 provides the average installed building-level lighting power densities in ComStock by building type and lighting generation.

Table 2. Average Building-Level Lighting Power Density (W/ft 2 ) by Lighting Generation and Building Type

| Building Type            |   Gen 1 |   Gen 2 |   Gen 3 |   Gen 4 |   Gen 5 |
|--------------------------|---------|---------|---------|---------|---------|
| full_service_restaurant  |    1.51 |    0.96 |    0.45 |    0.43 |    0.39 |
| hospital                 |    1.59 |    1.07 |    0.63 |    0.58 |    0.52 |
| large_hotel              |    1.31 |    0.80 |    0.29 |    0.23 |    0.21 |
| large_office             |    1.18 |    0.80 |    0.50 |    0.53 |    0.47 |
| medium_office            |    1.18 |    0.80 |    0.50 |    0.53 |    0.47 |
| outpatient               |    1.27 |    0.85 |    0.53 |    0.52 |    0.47 |
| primary_school           |    0.73 |    0.56 |    0.48 |    0.47 |    0.42 |
| quick_service_restaurant |    1.73 |    1.11 |    0.56 |    0.52 |    0.47 |
| retail                   |    1.17 |    0.75 |    0.54 |    0.47 |    0.42 |
| secondary_school         |    0.88 |    0.58 |    0.48 |    0.45 |    0.40 |
| small_hotel              |    1.08 |    0.63 |    0.28 |    0.25 |    0.22 |
| small_office             |    1.18 |    0.79 |    0.50 |    0.52 |    0.47 |
| strip_mall               |    1.59 |    1.07 |    0.65 |    0.64 |    0.59 |
| warehouse                |    0.83 |    0.40 |    0.39 |    0.30 |    0.27 |

Specifically, the lighting generations and corresponding lighting power densities were assigned to each building model during the sampling process, based on a validated distribution data (Figure 1), and introduced uncertainty representing realistic installation trends of different generations and impact of building sizes. Default interior lighting schedules come from the OpenStudio-standards U.S. Department of Energy prototype building models [3]. The schedules are then adjusted with variational base-to-peak ratios to incorporate impact from characteristics such as building types and operating hours.

Figure 1. 'Truth' lighting generation distribution (0-1) from validated data and comparison of 2017 and 2020 ComStock sampling results

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/92504.yaml
     source: 92504_images/image_000002_ffc6129323e2c96949de6c85dd4a39ce88f584367e5e3bd6c240e395914de716.png
     method: vision-description
     described: 2026-08-20 -->

![Stacked bar chart of the modeled share of eight lighting generations across eight stock vintages, from Truth 2015 through Truth 2035, with the 2017 and 2020 truth-versus-sampling pairs boxed](92504_images/image_000002_ffc6129323e2c96949de6c85dd4a39ce88f584367e5e3bd6c240e395914de716.png)

Figure 1 is a stacked bar chart of the fraction of lighting stock belonging to each lighting generation. Eight columns run left to right: Truth 2015, Truth 2017, Sampling 2017, Truth 2020, Sampling 2020, Truth 2025, Truth 2030 and Truth 2035. A black rectangle is drawn around the four middle columns (Truth 2017, Sampling 2017, Truth 2020, Sampling 2020), where sampled shares can be compared against truth data. Every segment carries a printed label and every column sums to 1.000. Reading each column bottom to top over the series gen1_t12_incandescent, gen2_t8_halogen, gen3_t5_cfl, gen4_led, gen5_led, gen6_led, gen7_led, gen8_led: Truth 2015 = 0.215, 0.660, 0.065, 0.060; Truth 2017 = 0.159, 0.488, 0.048, 0.274, 0.030; Sampling 2017 = 0.187, 0.480, 0.046, 0.264, 0.023; Truth 2020 = 0.121, 0.371, 0.037, 0.330, 0.141; Sampling 2020 = 0.081, 0.370, 0.038, 0.336, 0.175; Truth 2025 = 0.059, 0.181, 0.018, 0.371, 0.334, 0.037; Truth 2030 = 0.025, 0.077, 0.008, 0.267, 0.401, 0.134, 0.089; Truth 2035 = 0.015, 0.046, 0.005, 0.093, 0.187, 0.374, 0.187, 0.093. The three pre-LED generations fall from 94% of the stock in 2015 to 6.6% by 2035, and generations 6 through 8 appear only from 2025 onward.

