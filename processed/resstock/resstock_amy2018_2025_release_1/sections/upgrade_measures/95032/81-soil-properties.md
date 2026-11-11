<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95032.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95032.md | section: Soil Properties | lines: 1476-1483 -->
## Soil Properties

At the start of the project, the soil properties defaulted to a conductivity of 1.73 W/m-K, a density of 920 kg/m 3 , a specific heat capacity of 3.5 kJ/kg-K, and a thermal diffusivity of 5.37x10 -7 m 2 /s. Conductivity values have been updated as described above, with others still used in the existing workflow by default. The undisturbed deep ground temperature was originally modeled using the Kusuda/Achenbach model (T. A. Kusuda 1965) as implemented in EnergyPlus, although as noted the annual average dry-bulb temperature is used instead in some calculations (U.S. DOE 2022). The detailed description of the ground temperature model implemented in (Xing 2014) above is currently used in ResStock. Inputs for ground properties have been added to the HPXML schema, meaning users can now overwrite the default values if measured characteristics are available. However, our default assumptions have not changed.

Figure B-2: Number of ineligible dwellings by county due to low ground thermal conductivity (below 1.4 W/m-K, 7.6% of dwelling units represented in Restock).

![Image](95032_images/image_000045_30957a2dcd6e1c3c973b3010465432cb86333364f9757ceb38057815d2ca1045.png)

