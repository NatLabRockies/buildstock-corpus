<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/92502.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy26osti/92502.pdf | publication_url: https://www.nlr.gov/docs/fy26osti/92502.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/92502.md | section: 2  ComStock Baseline Approach | lines: 258-325 -->
## 2  ComStock Baseline Approach

This measure modifies the existing model interior lighting schedules during the daily peak demand windows (on-peak periods) only. For times outside of the event, the existing lighting schedules in the model are unchanged. The details of the lighting schedules, technology, and power in the existing ComStock models can be found in Section 4.2 'Hours of Operation and Occupancy' and Section 4.5.1 'Interior Lighting' in the ComStock Reference Documentation [30] for default schedules, and Section 3.3.4 'Interior Lighting Schedule Magnitude Variability' in the End-Use Load Profiles project report [31] for base-to-peak variation applied to the default lighting schedules.

ComStock interior lighting is determined by a lighting technology generation approach, with each generation representing a collection of lighting technologies typically installed during a given time period. ComStock assumes four categories of lighting: general (overhead lighting), task (lights focused on specific areas), supplemental (supplemental lighting), and wall wash (illuminates vertical surface). The lighting technologies used in each category across the ComStock lighting generations are listed in Table 1. Generations 4-8 represent varying efficacy levels of LEDs, with Generation 4 being the first LED technology to market, and Generation 8 being the estimated technology level in 2035.

Table 1. Lighting Generations and Associated Technologies for Each Category

| Lighting Generation   | General Lighting Technology   | General Lighting (High Bay) Technology       | Task Lighting Technology   | Supplemental Lighting Technology   | Wall Wash Lighting Technology   |
|-----------------------|-------------------------------|----------------------------------------------|----------------------------|------------------------------------|---------------------------------|
| 1                     | T12 Linear Fluorescent        | High Intensity Discharge (HID) Mercury Vapor | Incandescent A-Shape       | Incandescent Decorative            | Incandescent Decorative         |
| 2                     | T8 Linear Fluorescent         | HID Metal Halide                             | Halogen A-Shape            | Halogen Decorative                 | Halogen Decorative              |
| 3                     | T5 Linear Fluorescent         | HID Metal Halide                             | Compact Fluorescent Screw  | Compact Fluorescent Pin            | Compact Fluorescent Pin         |
| 4-8                   | LED Linear                    | LED High Luminaire                           | LED General Purpose        | LED Decorative                     | LED Directional                 |
|                       |                               | Bay                                          |                            |                                    |                                 |

ComStock uses a similar approach to the ASHRAE 90.1 Lighting Subcommittee for determining the lighting power density (LPD) allowance for a given space type. Table 2 provides the average installed building-level LPDs in ComStock by building type and lighting generation.

Table 2. Average Building-Level LPD (W/ft 2 ) by Lighting Generation and Building Type

|                         |   Lighting Generation |   Lighting Generation |   Lighting Generation |   Lighting Generation |   Lighting Generation |
|-------------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| Building Type           |                     1 |                     2 |                     3 |                     4 |                     5 |
| full_service_restaurant |                  1.51 |                  0.96 |                  0.45 |                  0.43 |                  0.39 |
| hospital                |                  1.59 |                  1.07 |                  0.63 |                  0.58 |                  0.52 |
| large_hotel             |                  1.31 |                  0.80 |                  0.29 |                  0.23 |                  0.21 |
| large_office            |                  1.18 |                  0.80 |                  0.50 |                  0.53 |                  0.47 |

|                          |   Lighting Generation |   Lighting Generation |   Lighting Generation |   Lighting Generation |   Lighting Generation |
|--------------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| Building Type            |                     1 |                     2 |                     3 |                     4 |                     5 |
| medium_office            |                  1.18 |                  0.80 |                  0.50 |                  0.53 |                  0.47 |
| outpatient               |                  1.27 |                  0.85 |                  0.53 |                  0.52 |                  0.47 |
| primary_school           |                  0.73 |                  0.56 |                  0.48 |                  0.47 |                  0.42 |
| quick_service_restaurant |                  1.73 |                  1.11 |                  0.56 |                  0.52 |                  0.47 |
| retail                   |                  1.17 |                  0.75 |                  0.54 |                  0.47 |                  0.42 |
| secondary_school         |                  0.88 |                  0.58 |                  0.48 |                  0.45 |                  0.40 |
| small_hotel              |                  1.08 |                  0.63 |                  0.28 |                  0.25 |                  0.22 |
| small_office             |                  1.18 |                  0.79 |                  0.50 |                  0.52 |                  0.47 |
| strip_mall               |                  1.59 |                  1.07 |                  0.65 |                  0.64 |                  0.59 |
| warehouse                |                  0.83 |                  0.40 |                  0.39 |                  0.30 |                  0.27 |

Specifically, the lighting generations and corresponding technologies were assigned to each building model during the sampling process, based on validated distribution data (Figure 1), and introduced with variability representing realistic installation trends of different generations and impact of building sizes. Default interior lighting schedules come from the OpenStudioStandards DOE prototype building models [32]. The schedules are then adjusted with varying base-to-peak ratios (BPRs) to incorporate impact from characteristics such as building types and operating hours.

Figure 1. 'Truth' lighting generation distribution (0-1) from validated data and comparison of 2017 and 2020 ComStock sampling results

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/92502.yaml
     source: 92502_images/image_000002_103ac927eb5129d70c7ce62f93522cbcf99be1f4601d2261956d231b4de91fda.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 1. Stacked column chart of the fractional distribution of eight lighting generations across the ComStock stock, comparing validated truth data for 2015, 2017, 2020, 2025, 2030 and 2035 against ComStock sampling results for 2017 and 2020](92502_images/image_000002_103ac927eb5129d70c7ce62f93522cbcf99be1f4601d2261956d231b4de91fda.png)

Stacked column chart of lighting generation shares, each column summing to 1.0, used to validate ComStock's lighting sampling against a validated truth distribution. Columns are grouped by year: Truth 2015; a boxed pair Truth 2017 and Sampling 2017; a second pair Truth 2020 and Sampling 2020; then Truth 2025, Truth 2030 and Truth 2035. The legend lists eight generations: gen1_t12_incandescent, gen2_t8_halogen, gen3_t5_cfl, gen4_led, gen5_led, gen6_led, gen7_led, gen8_led. Truth 2015 is gen1 0.215, gen2 0.660, gen3 0.065, gen4 0.060. The 2017 validation pair matches closely: Truth gen1 0.159, gen2 0.488, gen3 0.048, gen4 0.274, gen5 0.030 versus Sampling 0.187, 0.480, 0.046, 0.264, 0.023. The 2020 pair likewise: Truth 0.121, 0.371, 0.037, 0.330, 0.141 versus Sampling 0.081, 0.370, 0.038, 0.336, 0.175. Agreement within a few percentage points on every generation is the point of the figure. The forward-looking 2025, 2030 and 2035 truth columns show gen1 and gen2 shrinking toward zero while successive LED generations (gen4 through gen8) take over, with gen8_led first appearing only in 2035. Lighting generation drives lighting power density and therefore the load available to shed.

The following figure shows two sets of example weekday lighting default schedules versus the corresponding BPR-adjusted schedules for large and small office buildings in the ComStock baseline models.

Figure 2. Example weekday lighting schedules (fractional factor to fully ON)

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/92502.yaml
     source: 92502_images/image_000003_826913aa728d37fda344d75cc64125ea8276231088e4590af1a27989f204ffb4.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 2. Line chart of example weekday interior lighting schedules over a 24-hour day for large and small office models, comparing the OpenStudio prototype default schedule against the base-to-peak-ratio adjusted schedule used in ComStock](92502_images/image_000003_826913aa728d37fda344d75cc64125ea8276231088e4590af1a27989f204ffb4.png)

Line chart of example weekday interior lighting schedules, plotted as a fractional factor relative to fully ON on a y-axis from 0 to 1, against a 24-hour x-axis running 0:00 to 0:00 in three-hour ticks. Four series are drawn: Large office default (dashed orange), Large office BPR adjusted (solid orange), Small office default (dashed blue), and Small office BPR adjusted (solid blue). The two large-office traces overlay each other closely, holding near 0.05 overnight, climbing steeply from about 06:00 to a peak near 0.85 around 09:00, staying high through midday, then dropping sharply at about 13:30 back to roughly 0.05 by 15:00. The small-office default rises from 06:00 to a broad plateau near 0.85 held from about 09:00 to 15:00, then decays through the evening. The Small office BPR adjusted trace is the outlier: it is essentially flat at about 0.80 to 0.85 across the entire 24 hours, with no overnight setback. Base-to-peak ratios are applied to the prototype defaults to reflect building type and operating hours, and this figure shows the adjustment can substantially raise the base of the schedule relative to its peak.

