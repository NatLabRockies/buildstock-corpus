<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_PV with Battery Storage.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/assets/files/ComStock%20Measure%20Doc_PV%20with%20Battery%20Storage.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_PV%20with%20Battery%20Storage.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_PV with Battery Storage.md | section: 4  Output Variables | lines: 282-300 -->
## 4  Output Variables

Table 6 includes a list of output variables that are calculated in ComStock. These variables are important in terms of understanding the differences between buildings with and without the 40% PV measure applied. These output variables can also be used to understand the economics of the upgrade (e.g., return on investment) if cost information (i.e., material, labor, and maintenance costs for technology implementation) is available.

Table 6. Output Variables Calculated From the Measure Application

| Variable Name                                              | Description                                                                                                                          |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| com_stock_sensitivity_reports.com_report_pv_system_size_kw | Total photovoltaic design capacity in kW                                                                                             |
| simulation_output_report.electricity_pv_kwh                | Annual PV electricity energy consumption in kWh, where negative values indicate generation                                           |
| simulation_output_report.purchased_site_electricity_kwh    | Annual purchased electricity following any on-site generation                                                                        |
| simulation_output_report.net_site_electricity_kwh          | Annual net electricity energy consumption in kWh, with negative values indicating excess on-site electricity generation sent back to |
| simulation_output_report.total_site_electricity_kwh        | Building annual total site electricity energy consumption; does not include impacts of PV                                            |
| out.params.battery_capacity_kwh..kWh                       | Installed battery energy capacity                                                                                                    |
| out.params.battery_max_charge_kw..kW                       | Installed battery power capacity used for charging                                                                                   |
| out.params.battery_max_discharge_kw..kW                    | Installed battery power capacity used for discharging                                                                                |

PRE-PUBLICATION

