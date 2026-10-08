<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/92618.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/92618.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/92618.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/92618.md | section: 3.4  Utility Bills | lines: 297-320 -->
## 3.4  Utility Bills

ComStock provides utility bill estimates for several fuel types in buildings: electricity, natural gas, propane, and fuel oil. The current implementation represents utility bills circa 2022, which is the most current year of utility data available from the Energy Information Administration (EIA). This section provides a high-level overview of the methodology behind utility bills in ComStock, but more detailed information is available in the ComStock documentation [2]. Summary statistics from this implementation are shown in Table 3. Note that ComStock does not currently estimate utility bills for district heating and cooling - however, this measure package does not apply to buildings with district heating or cooling.

Table 3. Summary Statistics of Utility Bill Implementation in ComStock by Fuel Type

| Fuel Type   | Minimum Price ($)   | Average Price ($)   | Maximum Price ($)   |
|-------------|---------------------|---------------------|---------------------|
| Natural gas | $0.070/kBtu         | $0.012/KBtu         | $0.048/kBtu         |
| Propane     | $0.022/kBtu         | $0.032/kBtu         | $0.052/kBtu         |
| Fuel oil    | $0.027/kBtu         | $0.033/kBtu         | $0.036/kBtu         |

Natural gas bills are estimated using 2022 EIA averages by state. Also, 2022 U.S. EIA natural gas prices (commercial price) and U.S. EIA heat content of natural gas delivered to consumers are used to create an energy price in dollars per kBtu [9].

Propane and fuel oil bills are estimated using 2022 EIA averages by state. Residential No. 2 distillate prices by sales type and U.S. EIA residential weekly heating oil and propane prices (October -March) and EIA assumed heat content for these fuels are used to create an energy price in dollars per kBtu [10]. Residential prices are used because commercial prices are only available at the national resolution. Additionally, most commercial buildings using these fuels are assumed to be smaller buildings where a residential rate is likely realistic. For states where state-level pricing was available, these prices are used directly. For other states, average pricing from the Petroleum Administration for Defense District- is used. For states where this level of pricing is not available, national average pricing is used.

The primary resource for ComStock electric utility rates is the Utility Rate Database (URDB), which includes rate structures for about 85% of the buildings and 85% of the floor area in ComStock [11]. The URDB rates include detailed cost features such as time-of-use pricing, demand charges, ratchets and so on. ComStock only uses URDB rates that were entered starting in 2013, and a cost adjustment factor is applied such that the rates reflect 2022 U.S. dollars.

URDB rates are assigned to ComStock models at the census tract level. The URDB can include several rate structures for a census tract. Instead of attempting to presume any single rate, multiple rates from the model's census tract are simulated; the ComStock dataset includes the minimum, median, mean, and maximum simulated rates for each model.

Many precautions are implemented to prevent less reasonable rates from being applied. This includes removing noncommercial rates, rates with nonbuilding-load keywords (e.g., security light, irrigation, snow, cotton gin), rates where the load profile does not follow any potential min/max demand or energy consumption qualifiers, and rates that cause suspiciously low (&lt;$0.01/kWh) or high (&gt;$0.45/kWh) blended averages. Additionally, any bill that is lower than 25% of the median or higher than 200% of the median is eliminated to avoid extreme bills.

For buildings with no URDB electric utility assigned, or for buildings where none of the stored rates apply, the annual bill is estimated using the 2022 EIA Form-861 average prices based on the state each model is located [12]. While this method does not reflect the detailed rate structures and demand charges, it is a fallback for the 15% of buildings in ComStock with no utility assigned.

