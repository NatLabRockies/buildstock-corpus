<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/99816.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/99816.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/99816.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: upgrade_measures/measure_pdfs/99816.md | section: ResStock Inputs for the Light Air Sealing Upgrade | lines: 250-264 -->
## ResStock Inputs for the Light Air Sealing Upgrade

Table 3 summarizes the inputs associated with the infiltration upgrade (air sealing) in ResStock (Phoung, Lou and White 2026). These inputs are passed to OS-HPXML to generate the corresponding HPXML files for the simulation. In cases where infiltration details (ACH50) are not explicitly defined in ResStock, default values (Table 3) are assigned by OS-HPXML based on building characteristics.

Table 3. ResStock Argument Values for Infiltration Options

| ResStock Argument                 | All ACH         | Calculated by OpenStudio-HPXML?   |
|-----------------------------------|-----------------|-----------------------------------|
| air_leakage_units                 | ACH             | No                                |
| air_leakage_house_pressure        | 50 pascals (Pa) | No                                |
| air_leakage_value                 | 1 to 50         | No                                |
| air_leakage_type                  | Unit Total      | No                                |
| site_shielding_of_home            | Normal          | No                                |
| air_leakage_leakiness_description | Auto            | Yes                               |

