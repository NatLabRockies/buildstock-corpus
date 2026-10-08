<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/92546.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/92546.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/92546.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/92546.md | section: 2  ComStock Baseline Approach | lines: 198-211 -->
## 2  ComStock Baseline Approach

This measure scenario replaces all HVAC equipment with ideal thermal air loads objects for every model in the ComStock baseline. All other features of the baseline models (e.g., thermostat setpoints, schedules, envelope, internal loads) remain the same. Virtually all ComStock model inputs will impact the resulting ideal thermal air loads produced by this work, which are documented extensively in the ComStock Reference Documentation [2]. This includes features such as:

- Envelope type and insulation
- Schedules
- Equipment loads
- Outdoor air requirements
- Thermostat setpoints and setbacks
- Lighting type and power
- Building shape and orientation.

One notable consideration is that ComStock does not currently model active dehumidification controls with humidity limits. HVAC systems in ComStock do provide some degree of dehumidification, but only to the extent that naturally occurs to meet cooling thermostat setpoints; ComStock HVAC systems use a cooling supply air temperature of around 55°F or higher coupled with a sensible heat ratio. The Ideal Thermal Air Loads measure used in this work operates similarly to the methodology used in the ComStock baseline regarding humidity control: the simulation determines a supply air temperature, generally above 55°F, which is coupled with a constant sensible heat ratio of 0.75.

