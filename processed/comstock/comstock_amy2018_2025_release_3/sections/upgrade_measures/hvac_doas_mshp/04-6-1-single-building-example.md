<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/hvac_doas_mshp.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/hvac_doas_mshp.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/hvac_doas_mshp.html | corpus_version: 0a2f61f | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/hvac_doas_mshp.md | section: 6.1 Single Building Example | lines: 251-287 -->
## 6.1 Single Building Example

The operation behavior of a small office building in Chicago is described in this section. Figure 9 illustrates how the multi-speed object functions. As the sensible load increases, either positive for heating load or negative for cooling load, the airflow rate generally increases. Speeds 1 through 4 are prevalent at different airflow bins. Speed 0 represents a timestep where the part load ratio, and therefore the speed level, is below 1, meaning the unit is cycling. Cycling operation is subject to efficiency losses, per Figure 4. In general, the MSHP operates at expected.

![Chart Description automatically generated](./media/0764e6c6-4878-4267-a31f-8adfc29d3946.png)

Figure 9. Comparison of MSHP speed level, airflow rate, and predicted load

Table 5 summarizes the heating energy and electricity consumption of various components in the MSHP and DOAS. The average COP of the compressor is calculated at 5.10, but adding in energy for defrost and supplemental heat brings this value down to 4.11. The Typical Meteorological Year (TMY) weather file never drops below the −15°F compressor cutoff temperature, so the compressor is never locked out. The electric heating coil in the DOAS accounts for 7% of the heating load (not considering ERV/HRV impacts) but 25% of the electricity consumed. The large increase in the percentage of heating load to the percentage of heating electricity for the DOAS heating coil is because the COP of the DOAS heating coil is lower than that of the MSHP.

Table 5. Summary of MSHP and DOAS Operation for Sample Small Office in Chicago

|  | **Small Office** |
|---|---|
| Zone HP Heating Energy (kWh) |
| 7702 |
| Zone HP Electricity (kWh) | 1510 |
| Zone HP Raw COP | 5.10 |
| Zone HP Load-Weighted Average Speed | 1.62 |
| Zone HP Supp. Heating Energy (kWh) | 38 |
| Zone HP Supp. Electricity (kWh) | 38 |
| Zone HP Supp. COP | 1.00 |
| Zone HP Defrost Electricity (kWh) | 334 |
| System Total Heating Load (kWh) | 7741 |
| System Total Electricity (kWh) | 1882 |
| Zone HP System Effective COP | 4.11 |
| Fraction Heating Energy HP | 1.00 |
| Fraction Heating Energy Supp | 0.00 |
| Fraction Electricity HP | 0.80 |
| Fraction Electricity Supp | 0.02 |
| Fraction Electricity Defrost | 0.18 |
| DOAS Heating Energy (kWh) | 624 |
| DOAS Heating Electricity (kWh) | 624 |
| DOAS Heating COP | 1.00 |
| Fraction Heating Energy DOAS | 0.07 |
| Fraction Electricity DOAS | 0.25 |

