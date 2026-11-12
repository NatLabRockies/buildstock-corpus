<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95036.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95036.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95036.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95036.md | section: 2.2  OpenStudio-HPXML Overview | lines: 234-254 -->
## 2.2  OpenStudio-HPXML Overview

For the variable-speed GHP, the same ResStock building energy model and OpenStudio ® -HPXML workflow are used as for the single- and two-stage GHPs.

OpenStudio-HPXML's apply\_ground\_to\_air\_heat\_pump() 3 method is used to apply multiple sets of speeds (and their respective performance curves) to water-to-air coil objects that support various speed levels:

- CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit
- CoilHeatingWaterToAirHeatPumpVariableSpeedEquationFit.

New performance curves, representing variable-speed equipment, were developed and used to calculate the cooling/heating total capacity/energy input ratio (EIR) 4 as a function of temperature, as a function of airflow rate, and as a function of water flow rate. Updates were also made to an EnergyPlus ® EMS program controlling the flow rate of water though the heat pump and ground heat exchanger.

2  https://NatLabRockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide\_2025\_1.pdf

3  https://github.com/NatLabRockies/OpenStudio-

HPXML/blob/v1.9.1/HPXMLtoOpenStudio/resources/hvac.rb#L549

4 The EIR is defined as the inverse of the coefficient of performance (1/COP)

For the variable-speed GHP equipment model in ResStock, data were taken from the latest WaterFurnace Series 7 variable-speed GHP unit. 5

