<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96414.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96414.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96414.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96414.md | section: 3.2.1 ResStock Inputs for the Dual Fuel Heating System | lines: 336-364 -->
## 3.2.1 ResStock Inputs for the Dual Fuel Heating System

Inputs from ResStock that describe the Dual Fuel Heating System are listed in the table below. Descriptions of each of these arguments can be found in Table 81 of the ResStock Technical Reference Documentation (Reyna, et al. 2025).

Table 4. ResStock Argument Values for the Dual Fuel Heating System Upgrade

| ResStock Argument                                          | Dual Fuel Heating System                | Calculated by OpenStudio- HPXML?   |
|------------------------------------------------------------|-----------------------------------------|------------------------------------|
| heat_pump_type                                             | air-to-air                              | No                                 |
| heat_pump_heating_efficiency_type                          | HSPF2                                   | No                                 |
| heat_pump_heating_efficiency                               | 7.8                                     | No                                 |
| heat_pump_cooling_efficiency_type                          | SEER2                                   | No                                 |
| heat_pump_cooling_efficiency                               | 15.1                                    | No                                 |
| heat_pump_sizing_methodology                               | ACCA                                    | No                                 |
| heat_pump_heating_capacity                                 | auto                                    | Yes                                |
| heat_pump_fraction_heat_load_served                        | 1                                       | No                                 |
| heat_pump_cooling_capacity                                 | auto                                    | Yes                                |
| heat_pump_fraction_cool_load_served                        | 1                                       | No                                 |
| heat_pump_backup_type                                      | integrated                              | No                                 |
| heat_pump_backup_fuel                                      | natural gas                             | No                                 |
| heat_pump_backup_heating_efficiency                        | 0.950/0.925 (depending on climate zone) | No                                 |
| heat_pump_backup_heating_capacity                          | auto                                    | Yes                                |
| heat_pump_heating_capacity_retention_fraction              | 0.5                                     | No                                 |
| heat_pump_heating_capacity_retention_fraction_temper ature | 5°F                                     | No                                 |
| heat_pump_is_ducted                                        | TRUE                                    | No                                 |
| heat_pump_cooling_compressor_type                          | single stage                            | No                                 |
| heat_pump_backup_heating_lockout_temp                      | 35°F                                    | No                                 |
| heat_pump_compressor_lockout_temp                          | 35°F                                    | No                                 |

