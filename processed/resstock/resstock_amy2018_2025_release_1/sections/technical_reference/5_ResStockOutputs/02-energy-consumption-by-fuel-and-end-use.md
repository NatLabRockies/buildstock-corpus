<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/5_ResStockOutputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/5_ResStockOutputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/5_ResStockOutputs.md | section: Energy Consumption by Fuel and End Use | lines: 222-287 -->
## Energy Consumption by Fuel and End Use

The ResStock workflow models each housing unit sample in OpenStudio and EnergyPlus to produce energy consumption of each model at subhourly time steps and then processes the results into ResStock outputs. These outputs are produced by fuel type (e.g., electricity, natural gas) and end use (e.g., lighting, heating). Totals are calculated for each fuel and for all fuels combined. For electricity and all fuels combined, net totals are also calculated, which incorporate the impacts of on-site photovoltaics. The full list of energy consumption outputs from the ResStock workflow is available in Table “ResStock energy output field names, units, and descriptions”. Note that to date, ResStock has included only consumption of electricity, natural gas, propane, and fuel oil—excluding on-site consumption, wood, coal, or other fuels in its modeling, although the workflow is set up to include these additional fuels. Future releases will likely include wood.

As an output, the energy consumption results are all preceded with an “out.” prefix, followed by either the fuel type (e.g., “out.electricity.”) or “total.” if it is an aggregate of all fuel types, and then the end use, “net.” or “total.” if it is an aggregate of all end uses in that fuel type.

<div id="table:results_output_fields" data-source="5_ResStockOutputs.tex">

| **Field Name** | **Units** | **Field Description** |
|:---|:---|:---|
| out.electricity.ceiling_fan.energy_consumption.kwh | kWh | Electricity consumed by ceiling fans |
| out.electricity.clothes_dryer.energy_consumption.kwh | kWh | Electricity consumed by clothes dryers |
| out.electricity.clothes_washer.energy_consumption.kwh | kWh | Electricity consumed by clothes washers |
| out.electricity.cooling.energy_consumption.kwh | kWh | Electricity consumed by cooling systems; excludes usage by fans/pumps |
| out.electricity.cooling_fans_pumps.energy_consumption.kwh | kWh | Electricity consumed by supply fan (air distribution) or circulating pump (geothermal loop) during cooling |
| out.electricity.dishwasher.energy_consumption.kwh | kWh | Electricity consumed by dishwashers |
| out.electricity.electric_vehicle_charging.energy_consumption.kwh | kWh | Electricity consumed by charging electric vehicles |
| out.electricity.freezer.energy_consumption.kwh | kWh | Electricity consumed by standalone freezers |
| out.electricity.heating.energy_consumption.kwh | kWh | Electricity consumed by heating systems; excludes usage by fans/pumps |
| out.electricity.heating_fans_pumps.energy_consumption.kwh | kWh | Electricity consumed by supply fan (air distribution) or circulating pump (hydronic distribution or geothermal loop) during heating |
| out.electricity.heating_hp_bkup.energy_consumption.kwh | kWh | Electricity consumed by heat pump backup; excludes usage by heat pump backup fans/pumps |
| out.electricity.heating_hp_bkup_fa.energy_consumption.kwh | kWh | Electricity consumed by supply fan (air distribution) or circulating pump (hydronic distribution) during heat pump backup |
| out.electricity.hot_water.energy_consumption.kwh | kWh | Electricity consumed by hot water system excludes recirculation pump and solar thermal pump |
| out.electricity.lighting_exterior.energy_consumption.kwh | kWh | Electricity consumed by exterior lighting |
| out.electricity.lighting_garage.energy_consumption.kwh | kWh | Electricity consumed by lighting in the garage |
| out.electricity.lighting_interior.energy_consumption.kwh | kWh | Electricity consumed by interior lighting |
| out.electricity.mech_vent.energy_consumption.kwh | kWh | Electricity consumed by mechanical ventilation system |
| out.electricity.net.energy_consumption.kwh | kWh | Total electricity consumed subtracts any power produced by PV or generators |
| out.electricity.permanent_spa_heat.energy_consumption.kwh | kWh | Electricity consumed by spa heating |
| out.electricity.permanent_spa_pump.energy_consumption.kwh | kWh | Electricity consumed by spa pump |
| out.electricity.plug_loads.energy_consumption.kwh | kWh | Electricity consumed by plug loads not elsewhere accounted for |
| out.electricity.pool_heater.energy_consumption.kwh | kWh | Electricity consumed by pool heaters |
| out.electricity.pool_pump.energy_consumption.kwh | kWh | Electricity consumed by pool pumps |
| out.electricity.pv.energy_consumption.kwh | kWh | Energy produced by rooftop PV systems. Negative value for any power produced. |
| out.electricity.range_oven.energy_consumption.kwh | kWh | Electricity consumed by range and oven |
| out.electricity.refrigerator.energy_consumption.kwh | kWh | Electricity consumed by refrigerators |
| out.electricity.total.energy_consumption.kwh | kWh | Total electricity consumed |
| out.natural_gas.clothes_dryer.energy_consumption.kwh | kWh | Natural gas consumed by natural gas clothes dryers |
| out.natural_gas.fireplace.energy_consumption.kwh | kWh | Natural gas consumed by natural gas fireplaces |
| out.natural_gas.grill.energy_consumption.kwh | kWh | Natural gas consumed by natural gas grills |
| out.natural_gas.heating.energy_consumption.kwh | kWh | Natural gas consumed by natural gas heating systems |
| out.natural_gas.heating_hp_bkup.energy_consumption.kwh | kWh | Natural gas consumed by heat pump backup |
| out.natural_gas.hot_water.energy_consumption.kwh | kWh | Natural gas consumed by natural gas hot water systems |
| out.natural_gas.lighting.energy_consumption.kwh | kWh | Natural gas consumed by natural gas lighting |
| out.natural_gas.permanent_spa_heat.energy_consumption.kwh | kWh | Natural gas consumed by spa heating |
| out.natural_gas.permanent_spa_pump.energy_consumption.kwh | kWh | Natural gas consumed by spa pump |
| out.natural_gas.pool_heater.energy_consumption.kwh | kWh | Natural gas consumed by natural gas pool heaters |
| out.natural_gas.range_oven.energy_consumption.kwh | kWh | Natural gas consumed by natural gas range and oven |
| out.natural_gas.total.energy_consumption.kwh | kWh | Total natural gas consumed |
| out.params.size_cooling_system_primary_k_btu_h | kBtu/h | Size of primary cooling system |
| out.params.size_heat_pump_backup_primary_k_btu_h | kBtu/h | Size of primary heat pump backup |
| out.params.size_heating_system_primary_k_btu_h | kBtu/h | Size of primary heating system |
| out.params.size_heating_system_secondary_k_btu_h | kBtu/h | Size of secondary heating system |
| out.propane.clothes_dryer.energy_consumption.kwh | kWh | Propane consumed by propane clothes dryers |
| out.propane.heating.energy_consumption.kwh | kWh | Propane consumed by propane heating systems |
| out.propane.heating_hp_bkup.energy_consumption.kwh | kWh | Propane consumed by heat pump backup |
| out.propane.hot_water.energy_consumption.kwh | kWh | Propane consumed by propane hot water systems |
| out.propane.range_oven.energy_consumption.kwh | kWh | Propane consumed by propane range and oven |
| out.propane.total.energy_consumption.kwh | kWh | Total propane energy consumed |
| out.site_energy.net.energy_consumption.kwh | kWh | Total site energy consumed subtracts any power produced by PV or generators |
| out.site_energy.total.energy_consumption.kwh | kWh | Total site energy consumed |

ResStock energy output field names, units, and descriptions

</div>

