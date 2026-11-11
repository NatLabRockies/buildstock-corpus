<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/5_ResStockOutputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/5_ResStockOutputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/5_ResStockOutputs.md | section: Electrical Panels | lines: 426-481 -->
## Electrical Panels

For electrical panel, occupied capacity and breaker spaces are tabulated by end use. The total occupied capacity and spaces are calculated as well as their headroom, or the amount of capacity or space left unused. In public ResStock datasets, these fields are prefixed with “out.electric_panel“ and described in “ResStock electrical panel output field names, units, and descriptions”. For capacity, the total occupied load (W) can be calculated using different methods and will be labeled accordingly. In the public datasets, results are available for the 2023 load-based (NEC 220.83) method only for existing dwellings. See Section “Electrical Panels” for the method description. The occupied capacity (A) is converted from occupied load (W) by dividing by 240V, the panel voltage, and then subtracted from the input field “in.electrical_panel_service_rating“” (A) to get the headroom capacity (A). The headroom capacity is used to determine capacity constraint – the panel is considered capacity-constrained if headroom is negative and unconstrained otherwise. This outcome is useful to account for any additional costs needed to resolve the constraint, such as through an electrical panel or service upgrade, or by using lower power appliances as an alternative. Users are encouraged to calculate the capacity constraint on their own to reflect their desired margin of error.

For breaker space, total rated count is labeled as an input metric in table “ResStock building characteristic output field names and descriptions”. This is actually derived from the breaker space headroom, which is probabilistically assigned based on the panel ampacity rating and other housing characteristics, and a tabulation of electrical equipment in the baseline home. In the upgrade simulations, the total breaker space count is carried over from the baseline simulation and the headroom count is recalculated according to the content of the upgrade package. See Section “Electrical Panels” for details. For ease of interpretation by mirroring the structure of the capacity metrics, total breaker space count is labeled as an input just like the panel service rating. All occupied and headroom tabulations are labeled as outputs. Breaker space headroom is used to calculate the space constraint, which exists when the headroom count is negative. The overall panel constraint is summarized into "no constraint", "space constrained only", "capacity constrained only", or "capacity and space constrained".

All results should be interpreted with uncertainty in mind, even if they look reasonable. The prediction of the panel service rating and headroom space do not account for all electrical and connected loads in the model. As a result, the capacity headroom can be negative for a model in the baseline, although it is uncommon. This can be interpreted as the house already being constrained prior to any upgrade and is consistent with anecdotal observations that some houses do trip their breakers often, an indication of a capacity shortfall. On the otherhand, the breaker space headroom in the baseline can never be negative because our modeling approach prevents this by sampling a non-negative headroom count directly. This is also consistent with the physical constraint of breaker space.

<div id="tab:panels" data-source="5_ResStockOutputs.tex">

| **Field Name** | **Units** | **Field Description** |
|:---|:---|:---|
| out.panel.load.total_load.\<method\>.w | W | Total service feeder load calculated per selected NEC method |
| out.panel.load.occupied_capacity.\<method\>.a | A | Total capacity occupied on the panel, calculated as total load (W) divided by panel voltage (240V) |
| out.panel.load.headroom_capacity.\<method\>.a | A | Available capacity on the panel, calculated as panel service rating (A) minus total occupied capacity (A) |
| out.panel.load.heating.w | W | Sum of space heating system and heat pump heating electric loads. For the load calculation, only the max of heating or cooling is used, not both |
| out.panel.load.cooling.w | W | Sum of space cooling system and heat pump cooling electric loads. For the load calculation, only the max of heating or cooling is used, not both |
| out.panel.load.hot_water.w | W | Sum of water heating system electric loads, for electric only |
| out.panel.load.clothes_dryer.w | W | Sum of clothes dryer electric loads, for electric only |
| out.panel.load.dishwasher.w | W | Sum of dishwasher electric loads |
| out.panel.load.range_oven.w | W | Sum of range/oven electric loads, for electric only |
| out.panel.load.mech_vent.w | W | Sum of mechanical ventilation electric loads |
| out.panel.load.permanent_spa_heat.w | W | Sum of permanent spa heater electric load, for electric only |
| out.panel.load.permanent_spa_pump.w | W | Sum of permanent spa pump electric loads |
| out.panel.load.pool_heater.w | W | Sum of pool heater electric loads |
| out.panel.load.pool_pump.w | W | Sum of pool pump electric loads |
| out.panel.load.well_pump.w | W | Sum of well pump electric loads |
| out.panel.load.ev_charging.w | W | Sum of electric vehicle charging equipment electric loads |
| out.panel.load.other.w | W | Sum of other electric loads, including but not limited to lighting/general receptacles at 3 W/sqft, refrigerator, microwave, and garbage disposal |
| out.panel.breaker_space.occupied.count | count | Total number of occupied spaces on the panel |
| out.panel.breaker_space.headroom.count | count | Available spaces, calculated as total rated spaces minus occupied spaces |
| out.panel.breaker_space.heating.count | count | Sum of heating system and heat pump heating occupied spaces |
| out.panel.breaker_space.cooling.count | count | Sum of cooling system and heat pump cooling occupied spaces |
| out.panel.breaker_space.hot_water.count | count | Sum of water heating system occupied spaces |
| out.panel.breaker_space.clothes_dryer.count | count | Sum of clothes dryer occupied spaces |
| out.panel.breaker_space.dishwasher.count | count | Sum of dishwasher occupied spaces |
| out.panel.breaker_space.range_oven.count | count | Sum of range/oven occupied spaces |
| out.panel.breaker_space.mech_vent.count | count | Sum of mechanical ventilation occupied spaces |
| out.panel.breaker_space.permanent_spa_heat.count | count | Sum of permanent spa heater occupied spaces |
| out.panel.breaker_space.permanent_spa_pump.count | count | Sum of permanent spa pump occupied spaces |
| out.panel.breaker_space.pool_heater.count | count | Sum of pool heater occupied spaces |
| out.panel.breaker_space.pool_pump.count | count | Sum of pool pump occupied spaces |
| out.panel.breaker_space.well_pump.count | count | Sum of well pump occupied spaces |
| out.panel.breaker_space.ev_charging.count | count | Sum of electric vehicle charging occupied spaces |
| out.panel.breaker_space.other.count | count | Sum of other electric load occupied spaces |
| out.panel.constraint.capacity.\<method\> | bool | Whether electric panel is capacity-constrained per the given method, defined as when out.panel.load.headroom_capacity.\<method\>.a \< 0 |
| out.panel.constraint.breaker_space | bool | Whether electric panel is space-constrained, defined as when out.panel.breaker_space.headroom.count \< 0 |
| out.panel.constraint.overall.\<method\> | categorical | Summarize overall electric panel constraint per the given method as "no constraint", "space constrained only", "capacity constrained only", or "capacity and space constrained" |
| out.panel.load.total_load.\<method\>.w.savings | W | For an upgrade measure only, total service feeder load reduced per selected NEC method |
| out.panel.load.occupied_capacity.\<method\>.a.savings | A | For an upgrade measure only, total occupied capacity reduced per selected NEC method |
| out.panel.breaker_space.occupied.count.savings | count | For an upgrade measure only, total number of occupied spaces reduced |

ResStock electrical panel output field names, units, and descriptions

</div>

