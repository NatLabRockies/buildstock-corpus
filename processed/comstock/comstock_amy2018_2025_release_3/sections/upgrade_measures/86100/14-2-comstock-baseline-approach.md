<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86100.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86100.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86100.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/86100.md | section: 2  ComStock Baseline Approach | lines: 170-231 -->
## 2  ComStock Baseline Approach

ComStock interior lighting is determined using a lighting generation approach, with each generation representing a collection of lighting technologies typically installed during a given time period. ComStock assumes four categories of lighting: General (overhead lighting), Task (lights focused on specific areas), Supplemental (supplemental lighting), and Wall Wash (illuminates vertical surface). The lighting technologies used in each category across the ComStock lighting generations are listed in Table 1. Generations 4-8 represent varying efficacy levels of LEDs, with Generation 4 being the first LED technology to market, and Generation 8 being the estimated technology level in 2035.

Table 1. Lighting Generations and Associated Technologies for Each Category

| Lighting Generation   | General Lighting Technology   | General Lighting (High Bay) Technology       | Task Lighting Technology   | Supplemental Lighting Technology   | Wall Wash Lighting Technology   |
|-----------------------|-------------------------------|----------------------------------------------|----------------------------|------------------------------------|---------------------------------|
| Gen 1                 | T12 Linear Fluorescent        | High Intensity Discharge (HID) Mercury Vapor | Incandescent A-Shape       | Incandescent Decorative            | Incandescent Decorative         |
| Gen 2                 | T8 Linear Fluorescent         | HID Metal Halide                             | Halogen A-Shape            | Halogen Decorative                 | Halogen Decorative              |
| Gen 3                 | T5 Linear Fluorescent         | HID Metal Halide                             | Compact Fluorescent Screw  | Compact Fluorescent Pin            | Compact Fluorescent Pin         |
| Gen 4-8               | LED Linear                    | LED High Bay Luminaire                       | LED General Purpose        | LED Decorative                     | LED Directional                 |

ComStock uses a similar approach to the ASHRAE 90.1 Lighting Subcommittee for determining the lighting power density (LPD) allowance for a given space type. Equation 1 calculates the LPD for a space using target illuminance levels as defined by the ASHRAE 90.1 Lighting Subcommittee, and lighting technology properties. Table 2 provides the average installed building-level LPDs in ComStock by building type and lighting generation.

LPD =  General Lighting  +  Task Lighting  +  Supplemental Lighting  +  Wall Wash Lighting (1)

- % LS 𝑥𝑥 = the percent of the horizontal illuminance met by a specific lighting system
- fc = the target horizontal illuminance value
- RSDD = room surface dirt depreciation, an estimate of how much surface dirt on ceilings and walls reduces light from reaching the horizontal surface
- TF 𝑥𝑥 = total lighting factor = Source luminous efficacy  ×  Coefficient of utilization  × LLF
- o Source luminous efficacy = the lumens per watt for a specific lighting technology

- o Coefficient of utilization = a term that capture how many of the lumens generated from the lighting system reaches the horizontal plane
- o LLF = Lighting loss factor = Luminaire Dirt Depreciation (LDD) × Lamp Lumen Depreciation (LLD)

Table 2. Average Building-Level Lighting Power Densities (W/ft 2 ) by Lighting Generation and Building Type

| building type            |   gen1 |   gen2 |   gen3 |   gen4 |   gen5 |
|--------------------------|--------|--------|--------|--------|--------|
| full_service_restaurant  |   1.51 |   0.96 |   0.45 |   0.43 |   0.39 |
| hospital                 |   1.59 |   1.07 |   0.63 |   0.58 |   0.52 |
| large_hotel              |   1.31 |   0.80 |   0.29 |   0.23 |   0.21 |
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

Lighting generations are assigned to each building model during sampling based on the year of last interior lighting replacement and the energy code in force during that year. Probability distributions were generated using a Gaussian distribution based on an approximate start and end year for each lighting generation. The probability distributions were duplicated for each energy code in force and further modified to ensure they were realistic (i.e., not let Generation 1 be installed in a ComStock 90.1-2019 building), using a cutoff generation for each energy code in force. Each of the lighting generations were also assigned an arbitrary weight to scale the distributions to represent realistic installation trends. For example, while the installation years of Generation 2 and Generation 3 overlapped, Generation 2 was far more popular and was therefore assigned a higher weight than Generation 3 in the model.

Additionally, small commercial buildings (&lt;50,000 ft 2 ) tend to retrofit their lighting technology less frequently than large commercial buildings (&gt;50,000 ft 2 ). To capture this, the interior lighting lifespan values were changed so that large buildings updated their lighting every seven years on average, with small buildings updating their lighting on average every 13 years.

These distributions were validated using data from the 2015 U.S. Lighting Market Characterization study [1] and the 2019 Solid-State Lighting report [2]. The 2018 distribution of lighting generations by building type is given in Figure 1.

Figure 1. Installed lighting generation by building type for 2018 simulation year (count-based distribution)

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86100.yaml
     source: 86100_images/image_000002_3bd2084c271928fadf9c324e0ed43667a704843d4bca0e61f76aebe16b0120eb.png
     method: vision-description
     described: 2026-08-20 -->

![Stacked bar chart of interior lighting generation share by building type for 2018 (count-based)](86100_images/image_000002_3bd2084c271928fadf9c324e0ed43667a704843d4bca0e61f76aebe16b0120eb.png)

Stacked bar chart titled Count of in.interior_lighting_generation, y-axis from 0 to 1 (fraction of models) and x-axis of ComStock building types (FullServiceRestaurant, Hospital, LargeHotel, LargeOffice, MediumOffice, Outpatient, PrimarySchool, QuickServiceRestaurant, RetailStandalone, RetailStripmall, SecondarySchool, SmallHotel, SmallOffice, Warehouse). Each bar sums to 1 and is segmented by lighting generation per the legend: gen1_t12_incandescent, gen2_t8_halogen, gen3_t5_cfl, gen4_led, gen5_led. Across building types gen2_t8_halogen is the largest share, with gen1 and gen3 smaller and only thin gen4_led/gen5_led caps.

