<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86103.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/86103.md | section: 6.1.2 Example Building in a Moderate Climate | lines: 768-809 -->
## 6.1.2 Example Building in a Moderate Climate

Table 8 shows an example building in a moderate climate region before and after the upgrade. Similar trends are shown compared to the cooling-dominant example, however in this case, heating with a gas boiler in the baseline model is replaced with VRF. Additionally, because simultaneous heating and cooling is more frequent in this building, the heat recovery (i.e., extract heat from cooling zones and utilize recovered heat to heating zones) supports a large portion of heating demand resulting in reduced electricity used for VRF heating. Additionally, three air loops in a packaged VAV system is replaced with a single DOAS and the fraction of VRF backup heating against heat pump heating is small (1%).

Table 8. Single Building Example Results: Moderate Climate

| Parameter                                             | Baseline Results            | Upgrade Results   |
|-------------------------------------------------------|-----------------------------|-------------------|
| ASHRAE IECC climate zone 2006                         | 3C                          | 3C                |
| Building America climate zone                         | Marine                      | Marine            |
| ComStock building type                                | MediumOffice                | MediumOffice      |
| HVAC system type                                      | PVAV with gas boiler reheat | VRF DOAS          |
| floor area [ft 2 ]                                    | 75,000                      | 75,000            |
| state name                                            | California                  | California        |
| electricity cooling energy consumption [kWh]          | 141,042                     | 65,289            |
| electricity fans energy consumption [kWh]             | 266,914                     | 68,717            |
| electricity heat recovery energy consumption [kWh]    | 0                           | 16,283            |
| electricity heating energy consumption [kWh]          | 0                           | 75                |
| electricity total energy consumption [kWh]            | 959,517                     | 700,972           |
| electricity total peak demand [kW]                    | 189                         | 161               |
| natural gas heating energy consumption [kWh]/[therms] | 166,914/5,697               | 0                 |
| area fraction with heat recovery                      | 0.00                        | 1.00              |
| area fraction with motorized outdoor air damper       | 1.00                        | 0.00              |
| boiler capacity [kBtu/hr]                             | 773                         | 0                 |
| DX cooling capacity tons [tons]                       | 116                         | 47                |
| furnace capacity [kBtu/hr]                            | 0                           | 0                 |
| hours cooling setpoint not met [hr]                   | 0                           | 21                |
| hours heating setpoint not met [hr]                   | 0                           | 0                 |
| num air loops                                         | 3                           | 1                 |
| VRF weighted/maximum vertical piping height [m]       | 0.00                        | -5.49             |
| VRF weighted/maximum piping length [m]                | 0.00                        | 61.16             |
| VRF cooling design cop                                | 0.00                        | 3.97              |
| VRF heating design cop                                | 0.00                        | 4.14              |
| VRF heating fraction supplemental                     | 0.000                       | 0.011             |
| VRF indoor unit count                                 | 0                           | 36                |
| VRF outdoor unit count                                | 0                           | 3                 |
| VRF total cooling load [J]                            | 0                           | 877,025,378,395   |
| VRF total heat recovery [J]                           | 0                           | 408,701,408       |
| VRF total heating load [J]                            | 0                           | 470,196,158       |
| VRF total outdoor unit cooling capacity [W]           | 0                           | 270,507           |
| site energy total energy consumption [kWh]            | 1,163,686                   | 738,233           |

