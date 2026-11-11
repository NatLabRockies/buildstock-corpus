<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/99816.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/99816.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/99816.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/99816.md | section: 3.1  OpenStudio-HPXML Overview | lines: 234-245 -->
## 3.1  OpenStudio-HPXML Overview

ResStock relies heavily on the OpenStudio-HPXML workflow, and the general steps are as follows:

- -Step 1: Build probability distributions for housing characteristics in the energy model
- -Step 2: Apply custom ResStock model arguments to the energy model
- -Step 3: Fill in energy model assumptions using BuildResidentialHPXML
- -Step 4: Fill in appliance and occupant schedule assumptions using BuildResidentialScheduleFile
- -Step 5: Use the OpenStudio-HPXML workflow to change the building energy model to a HPXML file and then model the dwelling unit

For in-depth information about the ResStock modeling workflow, including repository version tags, housing characteristic distribution examples, sampling descriptions, and model articulation, see the Version History and the Workflow sections of the Technical Reference Guide from the ResStock 2025 Release 1, which is unchanged for this ResStock 2025 Release 2 (Reyna, et al. 2025).

