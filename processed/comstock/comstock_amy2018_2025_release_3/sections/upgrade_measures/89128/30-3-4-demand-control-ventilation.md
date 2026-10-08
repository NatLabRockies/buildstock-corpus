<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89128.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89128.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89128.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/89128.md | section: 3.4 Demand Control Ventilation | lines: 589-594 -->
## 3.4 Demand Control Ventilation

This measure will cycle through the outdoor air loops in a model and enable DCV for air loops serving applicable space types. This will set the DCV field in the mechanical ventilation controller to 'Yes' from 'No.' As ComStock building models do not track CO2 levels, the models' occupancy schedules will be used to control the DCV.

For the EnergyPlus DCV function to work properly, a space needs both a per-person and perarea outdoor air rate specified. In OpenStudio Standards, some space types have either 100% per-person or 100% per-area outdoor air rates specified. For these spaces on applicable air loops, outdoor air rates are converted to a per-person rate of 10 CFM/person, and the remainder of the outdoor air requirement is assigned as per-area.

