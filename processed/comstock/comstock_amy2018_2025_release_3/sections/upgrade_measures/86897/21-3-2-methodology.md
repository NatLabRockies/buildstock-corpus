<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86897.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86897.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86897.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/86897.md | section: 3.2  Methodology | lines: 400-403 -->
## 3.2  Methodology

This measure will cycle through the outdoor air loops in a model and enable DCV for air loops serving applicable space types using the EnergyPlus ®  function 'air\_loop\_hvac\_enable\_demand\_control\_ventilation.' This will set the DCV field in the mechanical ventilation controller to 'Yes' from 'No.' As ComStock building models do not track CO2 levels, the models' occupancy schedules will be used to control the DCV.

