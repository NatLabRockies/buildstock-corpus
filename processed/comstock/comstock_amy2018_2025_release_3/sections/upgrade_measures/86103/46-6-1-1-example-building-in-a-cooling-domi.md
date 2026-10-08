<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86103.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/86103.md | section: 6.1.1  Example Building in a Cooling-Dominant Climate | lines: 723-765 -->
## 6.1.1  Example Building in a Cooling-Dominant Climate

Table 7 shows an example building in a cooling-dominated region before and after the upgrade. The baseline building uses electricity for space cooling and natural gas furnace for space heating. Leveraging the higher cooling COP of the VRF system reduces electricity used for cooling. Replacing gas furnace heating with VRF heating removes gas usage but adds electricity used for heating. Decoupling ventilation with a DOAS reduced fan energy with indoor unit fans only operating based on sensible cooling needs. Annual electricity peak demand decreases as the efficient cooling with VRF drives the peak demand. In this table, the DX unit (this is a cooling only DX unit) shown in the table does not get completely removed because the space type served by that system is not applicable for VRF upgrade. It is also shown in the table how VRF systems are configured. Even though this building is in hot and humid region, a very small percentage (0.6%) of VRF supplemental/backup heating (with electric resistance heating) supported the heating demand.

Table 7. Single Building Example Results: Cooling Dominant Climate

| Parameter                                          | Baseline Results     | Upgrade Results   |
|----------------------------------------------------|----------------------|-------------------|
| ASHRAE IECC climate zone 2006                      | 3A                   | 3A                |
| Building America climate zone                      | Hot-Humid            | Hot-Humid         |
| ComStock building type                             | Outpatient           | Outpatient        |
| HVAC system type                                   | PSZ-AC with gas coil | VRF DOAS          |
| floor area [ft 2 ]                                 | 17,500               | 17,500            |
| state name                                         | Texas                | Texas             |
| electricity cooling energy consumption [kWh]       | 108,992              | 84,203            |
| electricity fans energy consumption [kWh]          | 68,778               | 45,486            |
| electricity heat recovery energy consumption [kWh] | 0                    | 7,553             |
| electricity heating energy consumption [kWh]       | 0                    | 30,256            |
| electricity total energy consumption [kWh]         | 350,992              | 340,719           |
| electricity total peak demand [kW]                 | 142                  | 113               |
| natural gas heating energy consumption             | 33,453/1,142         | 0                 |
| [kWh]/[therms]                                     |                      |                   |
| area fraction with heat recovery                   | 0.00                 | 0.88              |
| area fraction with motorized outdoor air damper    | 1.00                 | 0.00              |
| boiler capacity [kBtu/hr]                          | 0                    | 0                 |
| DX cooling capacity tons [tons]                    | 74                   | 12                |
| furnace capacity [kBtu/hr]                         | 1,911                | 0                 |
| hours cooling setpoint not met [hr]                | 705                  | 12                |
| hours heating setpoint not met [hr]                | 31                   | 77                |
| num air loops                                      | 33                   | 1                 |
| VRF weighted/maximum vertical piping height [m]    | 0.00                 | -4.57             |
| VRF weighted/maximum piping length [m]             | 0.00                 | 26.34             |
| VRF cooling design cop                             | 0.00                 | 4.05              |
| VRF heating design cop                             | 0.00                 | 4.21              |
| VRF heating fraction supplemental                  | 0.000                | 0.006             |
| VRF indoor unit count                              | 0                    | 33                |
| VRF outdoor unit count                             | 0                    | 3                 |
| VRF total cooling load [J]                         | 0                    | 642,348,791,242   |
| VRF total heat recovery [J]                        | 0                    | 2,437,127,218     |
| VRF total heating load [J]                         | 0                    | 67,586,808,164    |
| VRF total outdoor unit cooling capacity [W]        | 0                    | 231,668           |
| site energy total energy consumption [kWh]         | 415,769              | 372,044           |

