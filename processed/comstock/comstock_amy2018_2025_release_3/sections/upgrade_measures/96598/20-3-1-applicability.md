<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/96598.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96598.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96598.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/96598.md | section: 3.1  Applicability | lines: 562-573 -->
## 3.1  Applicability

The measure has three components: wall insulation, roof insulation, and windows. The measure will cycle through each component and upgrade any building whose energy code for those systems is lagging the current code adopted by the state where that building resides. In practice, this means that for each building simulated, the measure will load the following model inputs:

- energy\_code\_followed\_during\_latest\_walls\_replacement
- energy\_code\_followed\_during\_latest\_roof\_replacement
- energy\_code\_followed\_during\_latest\_windows\_replacement.

These inputs are determined during the model distribution sampling process and are a function of a building's location, the year of original construction, and the equipment EUL assumptions. The measure will also load a new input called 'current\_energy\_code\_in\_force', which is a function of the building's location. This new input will determine whether a building's existing wall, roof, or window codes are lagging the current code in force in that state. If the current code in force is newer than the building's current code for any of these three building systems, the energy code will be updated; hence, a model is considered 'applicable' if one or more of the wall, roof, or window codes are updated in the measure.

This measure is applicable to 100% of the floor area in ComStock.

