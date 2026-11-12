<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Breaker Space Calculations | lines: 3306-3377 -->
## Breaker Space Calculations

The breaker space calculation is broken out into two parts. First the total rated breaker space is determined for the panel in the baseline home. This is done by summing the number of available breaker spaces (probabilistically assigned based on housing characteristics) and the estimated total occupied spaces by major electric equipment. Table “Default voltage and breaker space by load type.” below lists the electric equipment considered and their associated voltage and breaker space requirement. Generally 120V-rated equipment take up one breaker space and 240V-rated equipment take up two spaces in order to make contact with two live bus bars to get the 240V service. While space-saving breakers, such as tandem, tri, and quad breakers, are available, they are not currently modeled in ResStock.

<div id="tab:breaker_spaces" data-source="3c_ResStockInputs.tex">

| **Load Name** | **Voltage** | **Breaker Spaces** | **Notes** |
|:---|:---|:---|:---|
| lighting | 120 | 2 |  |
| kitchen | 120 | 2 | Two kitchen small appliance circuits. |
| laundry | 120 | 1 | One laundry circuit. |
| electric vehicle charging | 120 | 1 | Level 1 - 120V EV charger. Assumes dedicated circuit. |
| electric vehicle charging | 240 | 2 | Level 2 - 240V EV charger. |
| well pump | 240 | 2 |  |
| pool pump | 240 | 2 | 2 HP pool pump capacity. |
| pool heater | 240 | 6 | Electric resistance pool heater. Three 50A circuit breaker. |
| pool heater | 240 | 2 | Heat pump pool heater. |
| permanent spa heater | 240 | 2 | Electric resistance hot tub heater. |
| permanent spa heater | 240 | 2 | Heat pump hot tub heater. |
| permanent spa pump | 240 | 2 | Hot tub pump. |
| clothes dryer | 240 | 2 | Electric clothes dryer. |
| clothes dryer | 120 | 1 | 120V heat pump clothes dryer. |
| clothes dryer | 240 | 2 | 240V heat pump clothes dryer. |
| dishwasher | 120 | 1 | Dishwasher. |
| range/oven | 120 | 1 | 120V range-oven. |
| range/oven | 240 | 2 | 240V range-oven. |
| hot water | 240 | 4 | Tankless water heater - one bathroom. The default power rating is 1800W. Two 50A circuit breaker. |
| hot water | 240 | 4 | Tankless water heater - two bathrooms. The default power rating is 2400W. Two 50A circuit breaker. |
| hot water | 240 | 6 | Tankless water heater - three or more bathrooms. The default power rating is 3600W. Three 50A circuit breaker. |
| hot water | 240 | auto | Storage water heater. The default power rating is auto sized. The number of breaker space = 2\*(power rating in W/240V/50A).ceil. |
| hot water | 120 | auto | 120V heat pump water heater. Assumes dedicated circuit. The default power rating is auto sized. The number of breaker space = (power rating in W/240V/15A).ceil. |
| hot water | 240 | auto | 240V heat pump water heater. The default power rating is auto sized. The number of breaker space = 2\*(power rating in W/240V/50A).ceil. |
| heating | 240 | auto | The default power rating is auto sized and includes auxiliary devices such as air handler and hydronic pump. The number of breaker space depends on the HVAC configuration, but generally = 2\*(power rating in W/240V/50A).ceil. |
| cooling | 240 | auto | The default power rating is auto sized and includes auxiliary devices such as air handler and hydronic pump. The number of breaker space depends on the HVAC configuration, but generally = 2\*(power rating in W/240V/50A).ceil. |
| mechanical ventilation | 120 | 1 |  |
| other | 120 | 1 | Only assumes 1 garage door opener if a garage is present and does not account for other permanent appliances (e.g. garbage disposal). |

Default voltage and breaker space by load type.

</div>

Determining the breaker space requirement for heat pump is a bit complicated - it depends on whether the system is ducted, dual-fuel, or has backup, and ultimately how the subsystems are electrically configured. For ducted systems, for example, the indoor unit (IDU, or air handler) and the outdoor unit (ODU, or compressor) can be on the same circuit (with a disconnect switch) or they can be on separate circuits, in which case, more spaces are required. The air handler is typically 240V to allow for the installation of heat strip backup on the same circuit, in which case, the ODU must be on a second circuit. For dual-fuel systems, the air handler can be 120V. Table “Default voltage and breaker space by heat pump systems.” below summarizes the breaker space requirement implemented in ResStock.

<div id="tab:breaker_spaces_hp" data-source="3c_ResStockInputs.tex">

| **Heat Pump System** | **Circuits** | **Breaker Spaces** |
|:---|:---|:---|
| Air-to-air, ducted, dual-fuel |  |  |
| ckt 2: 120V, IDU |  |  |
| ckt 2: 1 |  |  |
| Air-to-air, ducted, no backup |  |  |
| ckt 2: 240V, IDU |  |  |
| ckt 2: 2 |  |  |
| Air-to-air / mini-split, ducted, electric backup |  |  |
| ckt 2: 240V, IDU + backup |  |  |
| ckt 2: 2\*(IDU + backup power rating in W/240V/50A).ceil |  |  |
| Mini-split, ductless, no backup | ckt 1: 240V, ODU | ckt 1: 2\*(ODU power rating in W/240V/50A).ceil |
| Mini-split, ductless, electric backup |  |  |
| ckt 2: 240V, backup |  |  |
| ckt 2: 2\*(backup power rating in W/240V/50A).ceil |  |  |
| Mini-split, ducted, no backup | ckt 1: 240V, ODU + IDU | ckt 1: 2\*(ODU + IDU power rating in W/240V/50A).ceil |

Default voltage and breaker space by heat pump systems.

</div>

Once the total rated breaker space is calculated, it is used to calculate the headroom breaker space in an upgrade simulation by subtracting from it the new total spaces occupied by electric loads in the upgraded home. Note, although the headroom breaker space for the baseline is an input characteristic, all space-related metrics are listed as output metrics to avoid confusion.

# Household Characteristics

In addition to the physical characteristics of the housing units, ResStock defines the saturation of some attributes of the households. They are income and derivatives of income, tenure (renter/owner status), occupants, presence of Tribal persons, and vacancy status. All household attributes come from the 2019 5-year American Community Survey (ACS) Public Use Microdata Samples. The ACS is the premier census data source on the American population in addition to housing information. The survey collects data on all residents of sampled housing unit addresses. This means housing data such as building type and vacancy are tabulated by *household_id*, while population attributes such as age, race, and gender are tabulated by *person_id*. The ACS is also used to develop DOE’s [Low-Income Energy Affordability Data](https://www.energy.gov/scep/slsc/lead-tool) tool.

