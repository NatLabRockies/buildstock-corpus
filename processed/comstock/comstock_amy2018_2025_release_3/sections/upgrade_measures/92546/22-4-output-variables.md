<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/92546.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/92546.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/92546.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/92546.md | section: 4  Output Variables | lines: 256-268 -->
## 4  Output Variables

Table 2 includes a list of output variables that are calculated in ComStock. These variables are important in terms of understanding the differences between buildings with and without the Ideal Thermal Air Loads measure applied. These output variables can also be used for understanding the economics of the upgrade (e.g., return on investment) if cost information (e.g., material, labor, and maintenance costs for technology implementation) is available.

EnergyPlus meters the Ideal Thermal Air Loads measure under the district heating and district cooling end uses for heating and cooling loads, respectively. Therefore, the ideal thermal loads implemented in this measure scenario are reported under these fuel types, as shown in Table 2.

Table 2. Output Variables Calculated from the Measure Application

| Variable Name                                        | Description                                                                                                                                     |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| out.district_cooling.cooling.energy_consumption..kwh | Building annual district cooling energy consumption for cooling end use. The ideal air loads measure scenario reports loads under this end use. |
| out.district_heating.heating.energy_consumption..kwh | Building annual district heating energy consumption for heating end use. The ideal air loads measure scenario reports loads under this end use. |

