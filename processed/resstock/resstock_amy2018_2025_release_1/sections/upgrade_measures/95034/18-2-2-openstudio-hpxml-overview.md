<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95034.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95034.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95034.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95034.md | section: 2.2  OpenStudio-HPXML Overview | lines: 226-251 -->
## 2.2  OpenStudio-HPXML Overview

For the two-stage GHP, the same ResStock building energy model and OpenStudio-HPXML workflow is used as for the single-stage GHP (Maguire et al. 2025).

OpenStudio-HPXML's apply\_ground\_to\_air\_heat\_pump() 2  method in OpenStudio-HPXML is used to assign two-stage levels (and their corresponding performance curves) to water-to-air coil objects that support variable speeds:

- CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit
- CoilHeatingWaterToAirHeatPumpVariableSpeedEquationFit.

[1  https://NatLabRockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide\_2025\_1.pdf](https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf)

[2  https://github.com/NatLabRockies/OpenStudio-](https://github.com/NatLabRockies/OpenStudio-HPXML/blob/v1.9.1/HPXMLtoOpenStudio/resources/hvac.rb#L549)

[HPXML/blob/v1.9.1/HPXMLtoOpenStudio/resources/hvac.rb#L549](https://github.com/NatLabRockies/OpenStudio-HPXML/blob/v1.9.1/HPXMLtoOpenStudio/resources/hvac.rb#L549)

This method sets the performance curve models and applies them to the total cooling/heating capacity and energy input ratio (EIR) as functions of:

- Temperature
- Airflow rate
- Water flow rate.

To convert design-condition loads to rated-condition sizes:

- Cooling: Performance curve values, sensible heat ratio, and sensible cooling capacity at design conditions (used to determine airflow rates) are calculated using a similar approach as air-source heat pumps. This differs from single-stage GHPs because their performance curves have a different structure.
- Heating: Performance curve values for heating capacity at design conditions are calculated to ensure proper sizing based on the climate. This also follows the approach used by air-source heat pumps.

