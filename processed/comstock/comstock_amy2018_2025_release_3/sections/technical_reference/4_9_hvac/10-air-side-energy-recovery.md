<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: fadc83e | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: Air-Side Energy Recovery | lines: 536-566 -->
## Air-Side Energy Recovery

Energy recovery ventilators (ERVs) in AHUs reduce energy consumption by pre-conditioning the incoming outdoor air using the system exhaust air, which reduces the heating and cooling energy required to condition the air. Energy recovery is especially effective in systems serving spaces with high outdoor air ventilation loads.

ERVs are included in ComStock model HVAC systems only when required by the governing energy code for the specific system. This determination is made using OpenStudio-Standards, where the necessary ComStock model properties are gathered to determine whether an ERV is required for each system. These properties include the climate zone, percent outdoor air, and design supply airflow rate, aligning with ASHRAE-90.1 Table 6.5.6.1 for the respective energy code year followed. A summary of the floor area served by systems with energy recovery is shown in Table <a href="#tab:energy_recovery_prev" data-reference-type="ref" data-reference="tab:energy_recovery_prev">10</a>.

<div id="tab:energy_recovery_prev">

| **Building Type** | **Pre-1980** | **1980-2004** | **90.1-2004** | **90.1-2007** | **90.1-2010** | **90.1-2013** | **DEER All Years** |
|:---|:---|:---|:---|:---|:---|:---|:---|
| FullServiceRestaurant | 0 | 0 | 0.051 | 0.027 | 0.347 | 0.392 | 0 |
| Hospital | 0 | 0 | 0.457 | 0.442 | 0.613 | 0.871 | 0 |
| LargeHotel | 0 | 0 | 0.109 | 0.09 | 0.267 | 0.245 | 0 |
| LargeOffice | 0 | 0 | 0.028 | 0.035 | 0.139 | 0.519 | 0 |
| MediumOffice | 0 | 0 | 0.007 | 0.016 | 0.093 | 0.306 | 0 |
| Outpatient | 0 | 0 | 0.087 | 0.078 | 0.095 | 0.246 | 0 |
| PrimarySchool | 0 | 0 | 0.376 | 0.41 | 0.597 | 0.639 | 0 |
| QuickServiceRestaurant | 0 | 0 | 0 | 0 | 0.088 | 0.063 | 0 |
| RetailStandalone | 0 | 0 | 0.027 | 0.022 | 0.029 | 0.306 | 0 |
| RetailStripmall | 0 | 0 | 0.115 | 0.111 | 0.191 | 0.435 | 0 |
| SecondarySchool | 0 | 0 | 0.540 | 0.530 | 0.675 | 0.725 | 0 |
| SmallHotel | 0 | 0 | 0.186 | 0 | 0.092 | 0 | 0 |
| SmallOffice | 0 | 0 | 0 | 0 | 0.044 | 0.050 | 0 |
| Warehouse | 0 | 0 | 0.065 | 0.053 | 0.069 | 0.083 | 0 |

Fraction of Floor Area Served by HVAC Systems With Energy Recovery by Building Type and Code Year

</div>

An enthalpy wheel ERV system (rotary) is added to the HVAC systems in ComStock models where an ERV is determined to be required. The effectiveness of the system is 50% for all conditions, aligning with the requirements of ASHRAE-90.1. Economizer lockout and supply air bypass for temperature control are included. The defrost type is exhaust only, which temporarily bypasses the supply side of the heat exchanger to allow warmer exhaust air to remove frost uninhibited when needed.

