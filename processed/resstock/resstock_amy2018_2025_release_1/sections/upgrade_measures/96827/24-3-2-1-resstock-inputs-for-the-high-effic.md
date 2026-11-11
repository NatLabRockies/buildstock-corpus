<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96827.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96827.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96827.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96827.md | section: 3.2.1 ResStock Inputs for the High-Efficiency Gas Water Heater Upgrade | lines: 235-260 -->
## 3.2.1 ResStock Inputs for the High-Efficiency Gas Water Heater Upgrade

Table 4 summarizes the inputs associated with the high-efficiency condensing natural gas tankless water heater in ResStock. These inputs are used by OpenStudio-HPXML to create the HPXML file. As shown, ResStock heavily relies on the default assumptions from OpenStudioHPXML for miscellaneous details, such as water heater heating and backup heating capacity. Table 5 lists the default values assigned by OpenStudio-HPXML.

Table 4. ResStock Argument Values for the Natural Gas Tankless Water Heater

| ResStock Argument                        | High-Efficiency Natural Gas Tankless Water Heater, Condensing   | Calculated by OpenStudio- HPXML?   |
|------------------------------------------|-----------------------------------------------------------------|------------------------------------|
| water_heater_type                        | Instantaneous water heater                                      | No                                 |
| water_heater_fuel_type                   | Natural gas                                                     | No                                 |
| water_heater_tank_volume                 | N/A                                                             | No                                 |
| water_heater_efficiency_type             | UEF                                                             | No                                 |
| water_heater_efficiency                  | 0.98                                                            | No                                 |
| water_heater_recovery_efficiency         | N/A                                                             | No                                 |
| water_heater_standby_loss                | N/A                                                             | No                                 |
| water_heater_jacket_rvalue               | N/A                                                             | No                                 |
| water_heater_setpoint_temperature [ ° F] | 125                                                             | No                                 |
| water_heater_heating_capacity            | Auto                                                            | Yes                                |
| water_heater_backup_heating_capacity     | Auto                                                            | Yes                                |
| water_heater_has_flue_or_chimney         | Auto                                                            | Yes                                |
| water_heater_num_bedrooms_served         | Auto                                                            | Yes                                |
| water_heater_operating_mode              | Auto                                                            | Yes                                |
| water_heater_tank_model_type             | Auto                                                            | Yes                                |
| water_heater_usage_bin                   | Auto                                                            | Yes                                |
| water_heater_uses_desuperheater          | Auto                                                            | Yes                                |

