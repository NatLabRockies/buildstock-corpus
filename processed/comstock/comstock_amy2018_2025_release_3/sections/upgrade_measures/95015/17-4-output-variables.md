<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95015.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95015.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95015.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/95015.md | section: 4  Output Variables | lines: 475-497 -->
## 4  Output Variables

Table 6 includes a list of output variables that are calculated in ComStock. These variables are important in terms of understanding the differences between buildings with and without the electric resistance boiler measure applied. These output variables can also be used for understanding the economics of the upgrade (e.g., return on investment) if cost information (i.e., material, labor, and maintenance costs for technology implementation) is available.

Table 6. Output Variables Calculated From the Measure Application

| Variable Name                                   | Description                                                                   |
|-------------------------------------------------|-------------------------------------------------------------------------------|
| out.params.boiler_average_efficiency            | Load weighted average thermal efficiency                                      |
| out.params.boiler_cap_weight_efficiency         | Capacity weighted nominal thermal efficiency                                  |
| out.params.boiler_load_weight_efficiency        | Load weighted nominal thermal efficiency                                      |
| out.params.boiler_capacity..kbtu_per_hr         | Sum of boiler capacity                                                        |
| out.params.boiler_load..j                       | Total boiler heating load served                                              |
| out.params.boiler_electric..j                   | Total boiler electric use                                                     |
| out.params.boiler_gas..j                        | Total boiler gas use                                                          |
| out.params.boiler_other_fuel..j                 | Total boiler other fuel use                                                   |
| out.params.hot_water_loop_load..j               | Heating load provided by boilers and heat pumps                               |
| out.params.hot_water_loop_boiler_fraction       | Heating load provided by boilers divided by total hot water loop heating load |
| out.params.hvac_count_boilers                   | Count of boilers                                                              |
| out.params.hvac_count_boilers_0_to_300_kbtuh    | Count of boilers in size range 0-300 kBTUh                                    |
| out.params.hvac_count_boilers_300_to_2500_kbtuh | Count of boilers in size range 300-2,500 kBTUh                                |
| out.params.hvac_count_boilers_2500_plus_kbtuh   | Count of boilers in size range >2,500 kBTUh                                   |

