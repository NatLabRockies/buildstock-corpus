<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89481.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89481.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89481.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/89481.md | section: 3.2.5  Energy Recovery Controls | lines: 408-413 -->
## 3.2.5  Energy Recovery Controls

The energy recovery system is modeled with a bypass for economizer lockout operation. The system also includes wheel speed modulation for increased discharge temperature control.

Defrost operation is modeled by controlling the exhaust temperature of air leaving the energy recovery system. This ensures the exhaust air from the outlet of the heat exchanger is above the temperature that permits frost formation. For this modeling, the default EnergyPlus value of 35°F was chosen as the minimum exhaust temperature. When the temperature is at or below this point, the system redirects some of the incoming air around the recovery system (bypass). This reduces heat transfer between air streams which maintains the exhaust air temperature above the minimum setpoint.

