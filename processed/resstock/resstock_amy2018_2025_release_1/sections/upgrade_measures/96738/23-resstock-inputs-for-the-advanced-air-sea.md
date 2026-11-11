<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96738.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy27osti/96738.pdf | publication_url: https://docs.nlr.gov/docs/fy27osti/96738.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96738.md | section: ResStock Inputs for the Advanced Air Sealing Upgrade | lines: 378-392 -->
## ResStock Inputs for the Advanced Air Sealing Upgrade

Table 6 summarizes the inputs associated with the infiltration upgrade (advanced air sealing) in ResStock. These inputs are passed to OS-HPXML to generate the corresponding HPXML files for the simulation. In cases where infiltration details (ACH50) are not explicitly defined in ResStock, default values (Table 6) are assigned by OS-HPXML based on building characteristics.

Table 6. ResStock Argument Values for Infiltration Options

| ResStock Argument                 | All ACH    | Calculated by OpenStudio-HPXML?   |
|-----------------------------------|------------|-----------------------------------|
| air_leakage_units                 | ACH        | No                                |
| air_leakage_house_pressure        | 50         | No                                |
| air_leakage_value                 | 2.5 to 50  | No                                |
| air_leakage_type                  | Unit Total | No                                |
| site_shielding_of_home            | Normal     | No                                |
| air_leakage_leakiness_description | Auto       | Yes                               |

