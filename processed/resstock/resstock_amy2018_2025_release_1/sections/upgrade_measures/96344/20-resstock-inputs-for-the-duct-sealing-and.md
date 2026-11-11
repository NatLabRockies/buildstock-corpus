<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96344.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96344.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96344.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96344.md | section: ResStock Inputs for the Duct Sealing and Insulation Upgrades | lines: 191-208 -->
## ResStock Inputs for the Duct Sealing and Insulation Upgrades

Table 2 summarizes the inputs related to duct sealing and insulation in ResStock. OS-HPXML uses these inputs to create the HPXML file. As shown in Table 2, ResStock relies heavily on default assumptions from OS-HPXML for miscellaneous details. Table 3 lists the default values assigned by OS-HPXML.

Table 2. ResStock Argument Values for the Duct Sealing and Insulation Upgrades

| ResStock Argument                     | 5% Leakage to Outside, R-6   | 5% Leakage to Outside, R-8   | Calculated by OpenStudio- HPXML   |
|---------------------------------------|------------------------------|------------------------------|-----------------------------------|
| ducts_leakage_units                   | Percent                      | Percent                      | No                                |
| ducts_supply_leakage_to_outside_value | 0.033                        | 0.033                        | No                                |
| ducts_return_leakage_to_outside_value | 0.016                        | 0.016                        | No                                |
| ducts_supply_insulation_r             | 6                            | 8                            | No                                |
| ducts_return_insulation_r             | 6                            | 8                            | No                                |
| ducts_supply_buried_insulation_level  | auto                         | auto                         | Yes                               |
| ducts_return_buried_insulation_level  | auto                         | auto                         | Yes                               |
| ducts_supply_fraction_rectangular     | auto                         | auto                         | Yes                               |
| ducts_return_fraction_rectangular     | auto                         | auto                         | Yes                               |

