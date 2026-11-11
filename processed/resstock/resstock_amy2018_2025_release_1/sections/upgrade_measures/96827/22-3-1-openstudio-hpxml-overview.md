<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96827.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96827.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96827.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96827.md | section: 3.1  OpenStudio-HPXML Overview | lines: 225-230 -->
## 3.1  OpenStudio-HPXML Overview

The ResStock building stock energy model contains conditional probability distributions of building characteristics that are representative of the U.S. residential building stock. These are sampled to create a synthetic stock where each sample has an assigned option for each characteristic for each dwelling unit to be simulated. ResStock uses the OpenStudio-HPXML workflow to translate these dwelling characteristics into building models ready to be simulated via OpenStudio ® and EnergyPlus ®  through an HPXML file. For reference, OpenStudio-HPXML v1.10.0 was used to produce the ResStock 2025 Release 1 dataset.

1 'Water Heater in Unit' is a misnomer because the parameter denotes whether the water heater is centralized and shared rather than the status of the water heater's physical location.

