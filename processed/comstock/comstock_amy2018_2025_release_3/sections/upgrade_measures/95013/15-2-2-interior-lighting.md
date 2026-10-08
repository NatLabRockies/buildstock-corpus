<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95013.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95013.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95013.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/95013.md | section: 2.2  Interior Lighting | lines: 233-281 -->
## 2.2  Interior Lighting

This measure modifies the existing model (interior) lighting schedules during the daily peak demand windows (specifically on-peak periods) only. For times outside of the event, the existing lighting schedules in the model are unchanged. The details of the lighting schedules, technology, and power in the existing ComStock models can be found in Section 4.2: Hours of Operation and Occupancy and Section 4.5.1: Interior Lighting in the ComStock documentation [1] for default schedules, and Section 3.3.4: Interior Lighting Schedule Magnitude Variability in the End-Use Load Profiles project report [2] for base-to-peak variation applied to the default lighting schedules.

ComStock interior lighting is determined by a lighting technology generation approach, with each generation representing a collection of lighting technologies typically installed during a given time period. ComStock assumes four categories of lighting: general (overhead lighting), task (lights focused on specific areas), supplemental (supplemental lighting), and wall wash (illuminates vertical surfaces). The lighting technologies used in each category across the ComStock lighting generations are listed in Table 1. Generations 4-8 represent varying efficacy levels of light-emitting diodes (LEDs), with Generation 4 being the first LED technology to market, and Generation 8 being the estimated technology level in 2035.

Table 1. Lighting Generations and Associated Technologies for Each Category

| Lighting Generation   | General Lighting Technology   | General Lighting (High-Bay) Technology       | Task Lighting Technology   | Supplemental Lighting Technology   | Wall Wash Lighting Technology   |
|-----------------------|-------------------------------|----------------------------------------------|----------------------------|------------------------------------|---------------------------------|
| Gen 1                 | T12 linear fluorescent        | High-intensity discharge (HID) mercury vapor | Incandescent A-shape       | Incandescent decorative            | Incandescent decorative         |
| Gen 2                 | T8 linear fluorescent         | HID metal halide                             | Halogen A-shape            | Halogen decorative                 | Halogen decorative              |
| Gen 3                 | T5 linear fluorescent         | HID metal halide                             | Compact fluorescent screw  | Compact fluorescent pin            | Compact fluorescent pin         |
| Gen 4-8               | LED linear                    | LED high-bay luminaire                       | LED general purpose        | LED decorative                     | LED directional                 |

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

Specifically, the lighting generations and corresponding lighting power densities were assigned to each building model during the sampling process, based on a validated distribution data (Figure 1), and introduced uncertainty representing realistic installation trends of different generations and impacts of building sizes. Default interior lighting schedules come from the OpenStudio Standards U.S. Department of Energy prototype building models [3]. The schedules are then adjusted with variational base-to-peak ratios to incorporate the impacts from characteristics such as building types and operating hours.

Figure 1. 'Truth' lighting generation distribution (0-1) from validated data and comparison of 2017 and 2020 ComStock sampling results

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95013.yaml
     source: 95013_images/image_000002_64a643c2b505836850c4e8210a7e3e929647aeaac1683f7f01ea61dc9448f40e.png
     method: vision-description
     described: 2026-08-20 -->

![Stacked column chart of the fractional lighting technology (generation) mix over time, comparing actual 'Truth' stock to ComStock 'Sampling'](95013_images/image_000002_64a643c2b505836850c4e8210a7e3e929647aeaac1683f7f01ea61dc9448f40e.png)

Figure 1. Stacked column chart of the fractional interior-lighting technology mix (each column sums to 1.0), y-axis 0 to 1. Columns are labeled by year and source: Truth 2015, Truth 2017, Sampling 2017, Truth 2020, Sampling 2020, Truth 2025, Truth 2030, Truth 2035; a highlight box marks the 2017 and 2020 columns where 'Truth' (actual stock) is compared to ComStock 'Sampling'. Segments are lamp generations per the legend (gen1_t12_incandescent, gen2_t8_halogen, gen3_t5_cfl, gen4_led, gen5_led, gen6_led, gen7_led, gen8_led). Legible fractions: Truth 2015 is dominated by gen2_t8_halogen 0.660 with gen1 0.215, gen3 0.065, gen4 0.060. Truth 2017 gen1 0.159 / gen2 0.488 / gen3 0.048 / gen4 0.274 vs Sampling 2017 gen1 0.187 / gen2 0.480 / gen3 0.046 / gen4 0.264. Truth 2020 gen1 0.121 / gen2 0.371 / gen4 0.330 / gen5 0.141 vs Sampling 2020 gen1 0.081 / gen2 0.370 / gen4 0.336 / gen5 0.175. Later Truth years shift toward LED generations (2025 gen4 0.371 / gen5 0.334; 2035 dominated by gen4/gen5/gen6 LEDs). Shows the stock transitioning from T12/T8 fluorescent and halogen toward successive LED generations, and that ComStock sampling reproduces the Truth distribution closely in 2017 and 2020. (Dense small labels -- flag exact fractions for QA.)

