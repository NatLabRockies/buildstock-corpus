<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/92502.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy26osti/92502.pdf | publication_url: https://www.nlr.gov/docs/fy26osti/92502.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/92502.md | section: 3.3  Utility Bills | lines: 372-396 -->
## 3.3  Utility Bills

ComStock provides utility bill estimates for several fuel types in buildings: electricity, natural gas, propane, and fuel oil. The current implementation represents utility bills circa 2022, which is the most current year of utility data available from the EIA. This section provides a high-level overview of the methodology behind utility bills in ComStock, but more detailed information is available in the ComStock Reference Documentation [30]. Summary statistics from this implementation are shown in Table 3. Note that ComStock does not currently estimate utility bills for district heating and cooling.

Table 3. Summary Statistics of Utility Bill Implementation in ComStock by Fuel Type

| Fuel Type   | Minimum Price ($)   | Average Price ($)   | Maximum Price ($)   |
|-------------|---------------------|---------------------|---------------------|
| Natural Gas | $0.070/kBtu         | $0.012/KBtu         | $0.048/kBtu         |
| Propane     | $0.022/kBtu         | $0.032/kBtu         | $0.052/kBtu         |
| Fuel Oil    | $0.027/kBtu         | $0.033/kBtu         | $0.036/kBtu         |
| Electricity | $0.003/kBtu         | $0.035/kBtu         | $3.530/kBtu         |

Natural gas bills are estimated using 2022 EIA averages by state. 2022 U.S. EIA Natural Gas Prices - Commercial Price and U.S. EIA Heat Content of Natural Gas Delivered to Consumers are used to create an energy price in dollars per kBtu [34].

Propane and fuel oil bills are estimated using 2022 EIA averages by state. Residential No. 2 Distillate Prices by Sales Type and U.S. EIA residential Weekly Heating Oil and Propane Prices (October - March) and EIA assumed heat content for these fuels are used to create an energy price in dollars per kBtu [35]. Residential prices are used because commercial prices are only available at the national resolution. Additionally, most commercial buildings using these fuels are assumed to be smaller buildings where a residential rate is likely realistic. For states where state-level pricing was available, these prices are used directly. For other states, Petroleum Administration for Defense District (PADD)-average pricing is used. For states where PADDlevel pricing is not available, national average pricing is used.

The primary resource for ComStock electric utility rates is the Utility Rate Database (URDB), which includes rate structures for about 85% of the buildings and 85% of the floor area in ComStock [36]. The URDB rates include detailed cost features such as time-of-use pricing, demand charges, ratches, etc. ComStock only uses URDB rates that were entered starting in 2013, and a cost adjustment factor is applied such that the rates reflect 2022 U.S. dollars.

URDB rates are assigned to ComStock models at the census tract-level. The URDB can include several rate structures for a census tract. Instead of attempting to presume any single rate, multiple rates from the model's census tract are simulated; the ComStock dataset includes the minimum, median, mean, and maximum simulated rates for each model.

Many precautions are implemented to prevent less reasonable rates from being applied. This includes removing non-commercial rates, rates with non-building-load keywords (e.g. Security Light, Irrigation, Snow, Cotton Gin), rates where the load profile does not follow any potential min/max demand or energy consumption qualifiers, and rates that cause suspiciously low (&lt;$0.01/kWh) or high (&gt;$0.45/kWh) blended averages. Additionally, any bill that is lower than 25% of the median or higher than 200% of the median is eliminated to avoid extreme bills.

For buildings with no URDB electric utility assigned, or for buildings where none of the stored rates are applicable, the annual bill is estimated using the 2022 EIA Form-861 average prices based on the state each model is located in [37]. While this method does not reflect the detailed rate structures and demand charges, it is a fallback for the 15% of buildings in ComStock with no utility assigned.

