<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96636.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96636.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96636.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96636.md | section: 2 Applicability | lines: 218-250 -->
## 2 Applicability

This upgrade replaces space heating and cooling equipment in homes with existing ductwork with units that meet minimum efficiency standards reflective of circa-2025 requirements. It includes:

- Replacement of ducted fuel furnaces with a minimum of 80% -83% AFUE (92.5% AFUE for like-for-like replacements at higher efficiency).
- Replacement of air-source heat pumps with equipment rated at 14.3 SEER2 and 7.5 HSPF2.
- Replacement of central air conditioners (ACs) with units rated at 14.3 SEER2 in the South region and 13.4 SEER2 in the North region, with higher efficiency replacements (e.g., SEER2 15) applied where applicable.
- Replacement of ducted electric resistance furnaces with baseline 100% efficiency electric options for costing consistency.

In homes that have existing ductwork that is used for air conditioning but not heating, the nonducted heating systems are also replaced:

- Replacement of fuel boilers with a minimum of 80% -83% AFUE (90% AFUE for likefor-like replacements at higher efficiency).
- Replacement of non-ducted electric resistance heating systems (boiler, baseboard, wall furnace) with baseline 100% efficiency electric options for costing consistency.

In homes that have existing ductwork that is used for heating but not central air conditioning, the non-ducted air conditioning systems are also replaced:

- Replacement of room ACs with models meeting an EER of 12.0.

Where a dwelling 's existing cooling equipment already meets or exceeds these ratings, a like -for-like replacement at the higher efficiency is modeled instead. No changes to building infiltration or duct losses are assumed as part of the upgrades.

This upgrade applies to all dwelling units that have existing ductwork and a heating fuel that is natural gas, electricity, fuel oil, or propane. For consistency with other upgrades, it excludes any homes that do not have existing ductwork, do not use heating, or that heat with wood. It applies to about 5% of homes that have non-ducted heating (electric resistance baseboard, boilers, or wall/floor furnaces) but have ducts used for air conditioning. This includes a small number (&lt;1%) of multifamily dwelling units that have a whole-building shared heating system but that have individual ducted air conditioning systems serving each unit. It covers a wide range of heating technologies (furnaces, boilers, electric resistance) and cooling technologies (central AC, heat pumps, room ACs). With these applicability constraints, the measure upgrade applies to 75.2% of the existing dwelling units. The application logic is presented in Table 1.

Table 1. Summarized Apply Logic for Reference Space Heating and Air Conditioning Upgrade Circa 2025

| Heating Fuel                                    | HVAC Has Ducts   | Shared Cooling   | HVAC Heating Type                                  | HVAC Cooling Type                                   | Upgrade Applied?    | Stock Saturation (%)   |
|-------------------------------------------------|------------------|------------------|----------------------------------------------------|-----------------------------------------------------|---------------------|------------------------|
| Electricity, Natural Gas, Fuel Oil, and Propane | Yes              | No               | Ducted Heating Ducted Heat Pump Non-Ducted Heating | Central AC Room AC None Ducted Heat Pump Central AC | Yes Yes Yes Yes Yes | 43% 6% 5% 16% 5%       |
| Electricity, Natural Gas, Fuel Oil, and Propane | No               | Yes All options  | Ducted Heating All options                         | Central AC All options                              | No No               | 1% 21%                 |
| None, Wood                                      | Yes              | All options      | All options                                        | All options                                         | No                  | 1%                     |
|                                                 | No               | All options      | All options                                        | All options                                         | No                  | 2%                     |

Keep in mind that the upgrade improves less efficient efficiencies to meet 2025 minimum heating and cooling efficiencies identified in the following sections. HVAC heating and cooling systems remain constant (i.e., no fuel or system switching).

