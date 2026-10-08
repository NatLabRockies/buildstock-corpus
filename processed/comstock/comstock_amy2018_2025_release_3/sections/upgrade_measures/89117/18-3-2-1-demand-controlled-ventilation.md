<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89117.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89117.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89117.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/89117.md | section: 3.2.1 Demand-Controlled Ventilation | lines: 364-367 -->
## 3.2.1 Demand-Controlled Ventilation

To implement DCV, this measure iterates through air loops and enables DCV through the option on the Controller:MechanicalVentilation object in EnergyPlus, if the zone's space type is appropriate for DCV (see Applicability section). Note that in this control approach, occupancy schedules are used as a proxy for carbon dioxide concentration to control ventilation, since EnergyPlus does not separately calculate carbon dioxide levels.

