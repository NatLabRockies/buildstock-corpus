<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86103.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/86103.md | section: DOAS Fan Power | lines: 608-615 -->
## DOAS Fan Power

The DOAS requires a fan system to provide outdoor ventilation air to the building, including overcoming the heat/energy recovery heat exchanger. The pressure drop is modeled as 3.6 inches of total static pressure for the supply and exhaust fan together. This is an assumption to meet the 'very high efficiency' DOAS requirement for units having a fan of 60% efficiency and 92% motor efficiency [33]. The formula for calculating fan power is shown below.

Fan Power(watts) = (746 * total static pressure * airflow cfm) / (6345 * fan efficiency * fan motor efficiency)

The static pressure values for the fan objects in EnergyPlus are not informed by the bypass status of heat exchanger objects. This ignores the reduced static pressure that occurs when bypassing the heat exchanger. To account for this, the additional fan power is added directly to the heat exchanger objects in the form of motor energy for the enthalpy wheel. This is preferred since the power for the wheel object does modulate based on heat exchanger bypass status, so the additional static pressure due to the heat exchanger will be removed when the system is bypassing the heat exchanger. Note that additional fan power will therefore be reflected in the 'energy recovery' end use rather than the 'fans' end use because of this workaround.

