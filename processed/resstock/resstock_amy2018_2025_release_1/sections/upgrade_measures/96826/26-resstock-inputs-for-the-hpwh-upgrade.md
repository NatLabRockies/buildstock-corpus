<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96826.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96826.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96826.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96826.md | section: ResStock Inputs for the HPWH Upgrade | lines: 456-489 -->
## ResStock Inputs for the HPWH Upgrade

Table 5 summarizes the inputs associated with the HPWH upgrade in ResStock. These inputs are used by OpenStudio-HPXML to create the HPXML file. As shown, ResStock relies heavily on default assumptions from OpenStudio-HPXML for miscellaneous details such as water heater heating and backup heating capacity.

Table 6 lists the default values assigned by OpenStudio-HPXML. The efficiency values were average of models from two major U.S. HPWH manufacturers.

Table 5. ResStock Argument Values for the Electric HPWH Options Note all three tank volume options are listed below.

<!-- table recovered from measure_pdfs/96826.pdf p.18
     overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/96826.yaml
     method: extracted grid, with the cells named in `why` corrected from the PDF text layer
     supersedes the extractor's own table here (values 5c9967c96956…):
       Every value is right, but two argument names and one option value carry a space where the PDF wraps them inside a cell ('water_heater_backup_heating_cap acity', 'water_heater_num_bedrooms_serv ed', 'UniformEn ergyFactor'), so a search for the real name misses them. The header 'OpenStudio-HPXML?' and the two unit strings had the same spacing. The cell text is the extractor's own with those joined as the PDF text layer has them. -->

| ResStock Argument | Electric Heat Pump, 50 gal, 3.78 UEF | Electric Heat Pump, 66 gal, 3.95 UEF | Electric Heat Pump, 80 gal, 3.98 UEF | Calculated by OpenStudio-HPXML? |
|---|---|---|---|---|
| water_heater_type | HPWH | HPWH | HPWH | No |
| water_heater_fuel_type | Electricity | Electricity | Electricity | No |
| water_heater_tank_volume [gal] | 50 | 66 | 80 | No |
| water_heater_efficiency_type | UniformEnergyFactor | UniformEnergyFactor | UniformEnergyFactor | No |
| water_heater_efficiency | 3.78 | 3.95 | 3.98 | No |
| water_heater_recovery_efficiency | N/A | N/A | N/A | No |
| water_heater_standby_loss | Auto | Auto | Auto | Yes |
| water_heater_jacket_rvalue (add-on) [ft2⋅°F⋅h/btu] | 0 | 0 | 0 | No |
| water_heater_setpoint_temperature [°F] | 125 | 125 | 125 | No |
| water_heater_heating_capacity | Auto | Auto | Auto | Yes |
| water_heater_backup_heating_capacity | Auto | Auto | Auto | Yes |
| water_heater_has_flue_or_chimney | Auto | Auto | Auto | Yes |
| water_heater_num_bedrooms_served | Auto | Auto | Auto | Yes |
| water_heater_operating_mode | Auto | Auto | Auto | Yes |
| water_heater_tank_model_type | Auto | Auto | Auto | Yes |
| water_heater_usage_bin | Medium | Medium | High | No |
| water_heater_uses_desuperheater | Auto | Auto | Auto | Yes |

