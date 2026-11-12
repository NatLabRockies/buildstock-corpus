<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95034.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95034.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95034.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: upgrade_measures/measure_pdfs/95034.md | section: 2.3  Limitations and Concerns | lines: 698-706 -->
## 2.3  Limitations and Concerns

Some limitations unique to two-stage GHPs include:

1. The two-stage GHP uses EMS to account for energy consumption of the pump when modeled as operating below the lowest stage. A change to the EnergyPlus source code would be ideal and more widely accessible than the EMS-based approach used here, but source code changes can be complicated, time-consuming, and require expertise with the C++ based source code. Future runs will also use the bug fixed version of EnergyPlus, and the impact of the EMS workaround described here will need to be re-evaluated with the newer releases.
2. Desuperheater curves were not developed for two-stage equipment. Although data are available for desuperheater performance at both stages, adding a desuperheater to a GHP is relatively uncommon and assumed to not happen in ResStock when applying GHPs as an upgrade. This capability may be added to OpenStudio-HPXML in the future, which would make it available to be leveraged in ResStock for future runs.

Note that the limitations listed in the single-stage GHP measure documentation apply to all GHPs modeled in ResStock, particularly when it comes to modeling of the ground heat exchanger.

