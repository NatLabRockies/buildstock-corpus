<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89239.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89239.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89239.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/89239.md | section: Appendix C. Ground Temperatures and Soil Conductivity Assumptions | lines: 741-798 -->
## Appendix C. Ground Temperatures and Soil Conductivity Assumptions

Table C-1. Summary of GHEDesigner Input Assumptions

| Input (Units):                                               | Notes/Comments (based on subject matter expert input and GHEDesigner recommended                                                                                                                          | ComStock Model Assumptions:                                                                                                                               |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Borehole diameter (meters)                                   | defaults): Often drilled with 6' drilling equipment, so 6' or 15 cm are common values.                                                                                                                    | 0.15                                                                                                                                                      |
| Borehole burial depth (meters)                               | This can be anywhere from 2-10 ft, depending on how deep the header piping is when connecting to the boreholes. 2m is a commonly used value.                                                              | 2.0                                                                                                                                                       |
| Pipe inner/outer radius (meters)                             | 3/4', 1', and 1-1/4' standard dimension ratio (SDR)-11 high-density polyethylene (HDPE) piping is what is typically used. SDR = ratio of outer diameter to thickness of walls. HDPE dimension guide: [17] | 0.032                                                                                                                                                     |
| Pressure rating                                              | SDR-11 pressure rating for the commonly used HDPE pipe. [17]                                                                                                                                              | SDR-11                                                                                                                                                    |
| Pipe conductivity (w/m- K)                                   | Unless using a thermally enhanced pipe, the value for conductivity is typically 0.4 W/m-K.                                                                                                                | 0.4                                                                                                                                                       |
| Pipe volumetric heat capacity (J/K-m 3 )                     | 1,500,000 J/K-m 3 is common.                                                                                                                                                                              | 1,542,000                                                                                                                                                 |
| Pipe spacing (meters)                                        | Distance between the pipes within the borehole. Assume placed evenly within the borehole.                                                                                                                 | 0.0323                                                                                                                                                    |
| Pipe roughness (meters)                                      | HDPE is smooth, so 1e-6 m is a common value.                                                                                                                                                              | 0.000001                                                                                                                                                  |
| Soil thermal conductivity (W/m-K)                            | Varies by location. Distributions of soil conductivity values were generated for each climate zone and applied to the model. See Figure B-1 for distributions.                                            | Uses the Southern Methodist University Geothermal Laboratory dataset. [18] Soil conductivity varies by climate zone using distributions from the dataset. |
| Soil volumetric heat capacity (J/K-m 3 )                     | Typical 1.3-2.8 M/K-m 3 for unconsolidated ground material [19]                                                                                                                                           | 2,343,493                                                                                                                                                 |
| Grout conductivity. (W/m-K)                                  | 1 W/m-K is common. Not assuming thermally enhanced grouts.                                                                                                                                                | climate zone. [20] 1.3                                                                                                                                    |
| Grout volumetric heat capacity (J/K-m 3 )                    | 3.9e6 is a common value.                                                                                                                                                                                  | 3,901,000                                                                                                                                                 |
| Antifreeze mixture type                                      | Propylene glycol most commonly used. Antifreeze concentration: only as much as is needed to prevent freezing; 10-20% would be normal.                                                                     | 20% propylene glycol                                                                                                                                      |
| Max/min ground heat exchanger exiting fluid temperature (°C) | Should be based on practical limits of heat pump operating ranges. For cooling dominated applications, 5-35°C is generally appropriate. In heating applications, bottom limit could be lowered to -5°C.   | Min = 5.0 Max = 35.0                                                                                                                                      |

| Input (Units):                                                                      | Notes/Comments (based on subject matter expert input and GHEDesigner recommended defaults):                                                                                                                 | ComStock Model Assumptions:   |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| Polygonal area to fill, or specified ground heat exchanger shape, or unconstrained. | ComStock does not contain any data around land area/shape, therefore these will be unconstrained, meaning the field is allowed to grow as big as is needed to meet the loads without any shape constraints. | Unconstrained, near square    |
| Max/min borehole depth. (meters)                                                    | The tool will initially use the max depth to compute the number of boreholes required, then adjust the depth to meet the design temperatures.                                                               | Min = 60 Max = 135            |

Table C-2. Average Undisturbed Ground Temperatures by IECC 2012 Climate Zone According to the Simplified Design Model and Site Locations [20].

| 2012 IECC Climate zone   |   Annual average undisturbed ground temperature (C) |
|--------------------------|-----------------------------------------------------|
| 1A                       |                                                25.9 |
| 2A                       |                                                20.9 |
| 2B                       |                                                25.0 |
| 3A                       |                                                17.9 |
| 3B                       |                                                19.7 |
| 3C                       |                                                17.0 |
| 4A                       |                                                14.7 |
| 4B                       |                                                16.3 |
| 4C                       |                                                13.3 |
| 5A                       |                                                11.5 |
| 5B                       |                                                12.9 |
| 6A                       |                                                 9.0 |
| 6B                       |                                                 9.3 |
| 7A                       |                                                 7.0 |
| 7AK                      |                                                 5.4 |
| 7B                       |                                                 6.5 |
| 8AK                      |                                                 2.3 |

Figure C-1. Soil Conductivity Distributions by Climate Zone (W/m-K)

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89239.yaml
     source: 89239_images/image_000030_e53e2b6cb747db6e39dfafe136a8c7a2cf8b80730fd1e53734e329b474706e72.png
     method: vision-description
     described: 2026-08-21 -->

![Grid of 17 histograms of soil thermal conductivity by climate zone, W per m-K](89239_images/image_000030_e53e2b6cb747db6e39dfafe136a8c7a2cf8b80730fd1e53734e329b474706e72.png)

Figure C-1: grid of seventeen small histograms, one per climate zone from 1A through 8AK, each plotting soil thermal conductivity in W/m-K on an x-axis of 0 to 4 against sample count. Most zones concentrate between about 1.5 and 2.5 W/m-K in a single dominant bin; 3C and 7B are visibly more dispersed. Table C-1 lists the GHEDesigner input assumptions.
