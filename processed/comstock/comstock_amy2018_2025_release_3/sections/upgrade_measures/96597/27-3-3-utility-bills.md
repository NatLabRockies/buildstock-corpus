<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/96597.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96597.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96597.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/96597.md | section: 3.3  Utility Bills | lines: 452-476 -->
## 3.3  Utility Bills

ComStock provides utility bill estimates for several fuel types in buildings: electricity, natural gas, propane, and fuel oil. The current implementation represents utility bills circa 2022, which is the most current year of utility data available from the U.S. Energy Information Administration (EIA). This section provides a high-level overview of the methodology behind utility bills in ComStock, but more detailed information is available in the ComStock Reference Documentation [3]. Summary statistics from this implementation are shown in Table 5. Note that ComStock does not currently estimate utility bills for district heating and cooling.

Table 5. Summary Statistics of Utility Bill Implementation in ComStock by Fuel Type

| Fuel Type   | Minimum Price ($)                                     | Average Price ($)         | Maximum Price ($)         |
|-------------|-------------------------------------------------------|---------------------------|---------------------------|
| Natural Gas | $0.007/kilo British thermal unit (kBtu) ($0.70/therm) | $0.012/kBtu ($1.20/therm) | $0.048/kBtu ($4.80/therm) |
| Propane     | $0.022/kBtu ($2.20/therm)                             | $0.032/kBtu ($3.20/therm) | $0.052/kBtu ($5.20/therm) |
| Fuel Oil    | $0.027/kBtu ($2.70/therm)                             | $0.033/kBtu ($3.30/therm) | $0.036/kBtu ($3.60/therm) |
| Electricity | $0.003/kBtu ($0.01/kilowatt- hour [kWh])              | $0.035/kBtu ($0.12/kWh)   | $3.530/kBtu ($12.04/kWh)  |

Natural gas bills are estimated using 2022 EIA averages by state. 2022 EIA Natural Gas Prices Commercial Price and EIA Heat Content of Natural Gas Delivered to Consumers are used to create an energy price in dollars per kilo British thermal unit (kBtu) [13].

Propane and fuel oil bills are estimated using 2022 EIA averages by state. Residential No. 2 Distillate Prices by Sales Type and EIA residential Weekly Heating Oil and Propane Prices (October - March) and EIA assumed heat content for these fuels are used to create an energy price in dollars per kBtu [14]. Residential prices are used because commercial prices are only available at the national resolution. Additionally, most commercial buildings using these fuels are assumed to be smaller buildings where a residential rate is likely realistic. For states where state-level pricing was available, these prices were used directly. For other states, PetroleumAdministration-for-Defense-District-average pricing is used. For states where that level of pricing is not available, national average pricing is used.

The primary resource for ComStock electric utility rates is the Utility Rate Database (URDB) [15], which includes rate structures for about 85% of the buildings and 85% of the floor area in ComStock [3]. The URDB rates include detailed cost features such as time-of-use pricing, demand charges, ratchets, etc. ComStock only uses URDB rates that were entered starting in 2013, and a cost adjustment factor is applied such that the rates reflect 2022 U.S. dollars.

URDB rates are assigned to ComStock models at the census tract level. The URDB can include several rate structures for a census tract. Instead of attempting to presume any single rate, multiple rates from the model's census tract are simulated; the ComStock dataset includes the minimum, median, mean, and maximum simulated rates for each model.

Many precautions are implemented to prevent less reasonable rates from being applied. This includes removing noncommercial rates, rates with nonbuilding-load keywords (e.g., Security Light, Irrigation, Snow, Cotton Gin), rates where the load profile does not follow any potential min/max demand or energy consumption qualifiers, and rates that cause suspiciously low (&lt;$0.01/kWh) or high (&gt;$0.45/kWh) blended averages. Additionally, any bill that is lower than 25% of the median or higher than 200% of the median is eliminated to avoid extreme bills.

For buildings with no URDB electric utility assigned, or for buildings where none of the stored rates are applicable, the annual bill is estimated using the 2022 EIA Form-861 average prices based on the state each model is located in [16]. While this method does not reflect the detailed rate structures and demand charges, it is a fallback for the 15% of buildings in ComStock with no utility assigned.

