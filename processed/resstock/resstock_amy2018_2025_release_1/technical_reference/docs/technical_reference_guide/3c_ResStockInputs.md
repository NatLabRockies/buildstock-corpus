<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 -->
# Water Heating, Appliances, Lighting, Plug Loads, Electric Vehicles, Electrical Panels, Household Characteristics

# Water Heating

Water heating describes the system that provides domestic hot water and distributes it for use at the fixtures or by appliances, such as dishwashers and clothes washers. This section covers water heaters, hot water distribution, and hot water use for fixtures and appliances. For building characterization, ResStock provides distributions for how many housing units have a standalone water heater vs. a shared central water heater (Water Heater In Unit: Section “Water Heater In Unit”), where the water heater is located (Water Heater Location: Section “Water Heater Location”), water heating fuel (Water Heater Fuel: Section “Water Heater Fuel”), and water heater specification (Water Heater Efficiency: Section “Water Heater Efficiency”). Additionally, ResStock characterizes the piping material and insulation level for distributing hot water to the fixtures (Hot Water Distribution: Section “Hot Water Distribution”), as well as the fixture usage and flow levels in the form of usage multipliers (Hot Water Fixtures: Section “Hot Water Fixtures”).

## Water Heaters

### Modeling Approach

A water heater can be a standalone in-unit appliance or a centrally located system that serves multiple units in a multifamily or single-family attached building. ResStock models different water heating technologies, heating fuels, installation locations, and storage options. ResStock defines the heating efficiency and location using probability distributions. ResStock relies on OpenStudio-HPXML default assumptions for other technical details. To this end, all water heaters are modeled with a setpoint of 125° F. All fuel water heaters with an energy factor less than 0.63 are assumed to have an open flue, which increases the housing unit’s air infiltration for water heaters located in conditioned space.

#### Tank Water Heaters

Conventional storage water heaters are modeled as mixed tanks without additional tank insulation. ResStock calculates the amount of tank losses and the burner efficiency using an energy factor and recovery efficiency (Maguire and Roberts 2020). The recovery efficiency is 0.98 for electric tanks by fiat. The tank volume and heating capacity are calculated based on the number of bedrooms and bathrooms, per Table 8 of the 2014 House Simulation Protocol (which is based upon guidance from the U.S. Department of Housing and Urban Development \[HUD\]).

#### Tankless Water Heaters

Tankless water heaters, unlike storage water heaters, are designed to produce hot water on demand. To this end, they are typically equipped with a burner or electric elements several times larger in capacity. They are also much more compact. In ResStock, their heating performance is defined using an energy factor, which is further derated by 8% to account for cycling (International Code Council 2019).

#### Heat Pump Water Heaters

Heat pump water heaters are storage water heaters that use a refrigerant cycle to extract heat from the surrounding air to produce hot water. Heat pump water heaters are modeled with a stratified tank model, rather than a mixed tank like conventional storage water heaters. ResStock defines their heating performance using a uniform energy factor and first hour rating. The tank volume is defined by a housing characteristic distribution. Heat pump water heaters are modeled to operate in a hybrid mode, meaning the electric resistance backup only turns on to supplement the heat pump.

#### Solar Thermal Water Heaters

A solar hot water heater is a system that uses the sun to heat water. Typically it has a rooftop collector to absorb solar energy, and water or antifreeze is circulated through the collector to a tank with a heat exchanger. The solar thermal model takes inputs that define the collector characteristics, such as system type, collector area, solar loop type, orientation, tilt, rated optical efficiency and thermal losses, and storage volume (for integrated collector storage units). In ResStock, all solar water heaters are integrated collector units with a secondary backup storage tank, i.e., two-tank systems. To model a typical solar water heater with a single tank that has backup heating elements, the secondary tank is given a R-6.2 jacket to reduce the standby loss of the secondary tank.

#### Other Water Heaters

ResStock does not model building-level shared water heaters. Instead, ResStock models shared water heaters as equivalent in-unit style water heaters located in a heated common space outside the unit. This is due to ResStock’s current approach of modeling multifamily as singular housing units rather than as buildings consisting of multiple units, which limits the modeling of any shared systems. The out-of-unit location ensures that these water heaters do not generate tank losses that a housing unit’s HVAC system must address. However, this proxy modeling approach does not account for the differences in piping and tank losses from central water heaters. In addition to systems shared by multiple units, ResStock does not model combination systems that provide other services such as space conditioning in addition to hot water.

### Water Heater Fuel

#### Description

The water heater fuel type.

#### Distribution Data Sources

- U.S. EIA 2020 RECS microdata

- Alaska-specific distribution is based on Alaska Retrofit Information System (2008 to 2022), maintained by Alaska Housing Finance Corporation.

#### Direct Conditional Dependencies

- Geometry Building Type RECS

- Heating Fuel

- State

#### Options

Water Heater Fuel has options of Electricity, Fuel Oil, Natural Gas, Solar Thermal, Wood, and Other Fuel. The characteristic does not set any ResStock arguments. Instead, it is a direct dependency for Water Heater Efficiency, where the heating fuel is assigned individually for each water heater option. Through this dependency, any changes to the distribution of water heater fuels will cascade to influence the water heater types. After conversations with EIA the Other Fuel water heater is typically composed of respondents saying they either do not have a water heater, coal, biomass, or district steam systems. ResStock models the energy associated with Other Fuel water heaters as coal energy consumption.

#### Distribution Assumptions

- Due to low sample sizes, fallback rules are applied, with lumping of:

  - State: Census Division RECS

  - Geometry building SF: Mobile, Single-family attached, Single-family detached

  - Geometry building MF: Multifamily with 2-4 Units, Multifamily with 5+ Units

  - State: Census Region

  - State: National

- For Alaska, we are using a field in ARIS that lumps multifamily 2-4 units and multifamily 5+ units buildings together. Data from the American Community Survey are used to distribute between these two building types.

- For Alaska, wood and coal heating is modeled as other fuel.

- For Alaska, when a building uses more than one fuel for water heating, the fuel with highest consumption is considered the water heater fuel and used to meet all loads.

### Water Heater In Unit

#### Description

Presence of an individual water heater in the housing unit that solely serves the specific housing unit.

#### Distribution Data Sources

- U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Geometry Building Type RECS

- State

- Vintage ACS

#### Options

In the ResStock baseline, all housing units have access to hot water and use energy for water heating. This characteristic has no ResStock arguments. Instead, it is used to separate water heating energy between in-unit versus shared designations. As a direct dependency to Water Heater Location, it ensures water heaters not in-unit are located appropriately and have no interaction with in-unit end-use loads.

#### Distribution Assumptions

- All water heaters for Single-Family Detached and Mobile Homes are in-unit (not shared).

- Single-Family Attached assumes the distribution from RECS 2009 because RECS 2020 does not have this breakdown.

- Due to low sample sizes, fallback rules are applied, with lumping of:

  - State: Census Division RECS

  - Vintage ACS: Combining Vintage pre-1960s and post-2000

  - State: Census Region.

### Water Heater Location

#### Description

Location of the water heater.

#### Distribution Data Sources

- U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Space Combination

- Vintage ACS

- Water Heater In Unit.

#### Options

The options are spaces where the water heater can be located (Table “Water Heater Location options and arguments that vary for each option”). The Conditioned Mechanical Room option is only used for multifamily units with shared water heating. This option assigns the `water_heater_location` ResStock argument.

<div id="table:hc_opt_water_heater_loc" data-source="3c_ResStockInputs.tex">

| Option name                 | `water_heater_location` |
|:----------------------------|:------------------------|
| Attic                       | attic                   |
| Conditioned Mechanical Room | other heated space      |
| Crawlspace                  | crawlspace              |
| Garage                      | garage                  |
| Heated Basement             | basement—conditioned    |
| Living Space                | conditioned space       |
| Outside                     | other exterior          |
| Unheated Basement           | basement—unconditioned  |

Water Heater Location options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Water Heater Location characteristic”. See the OpenStudio-HPXML [Water Heating Systems](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-water-heating-systems) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_water_heater_loc" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `water_heater_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, garage, attic, attic—vented, attic—unvented, crawlspace, crawlspace—vented, crawlspace—unvented, crawlspace—conditioned, other exterior, other housing unit, other heated space, other multifamily buffer space, other non-freezing space | The location of water heater. |

The ResStock argument definitions set in the Water Heater Location characteristic

</div>

#### Distribution Assumptions

- H2OMAIN = other is equally distributed among attic and crawlspace.

- H2OMAIN does not apply to multifamily, therefore Water heater location for multifamily with in-unit water heater is taken after the combined distribution of other building types.

- Out-of-unit water heater is assumed to be in Conditioned Mechanical Room. Per expert judgment, water heaters cannot be outside or in vented spaces for IECC Climate Zones 4-8 due to pipe-freezing risk.

- Where samples \< 10, data are aggregated in the following order:

  - Building Type lumped into single-family, multifamily, and mobile home.

  - 1 + Foundation Type combined.

  - 2 + Attic Type combined

  - 3 + Garage combined.

  - Single/Multifamily + Foundation combined + Attic combined + Garage combined.

  - 5 + pre-1960 combined.

  - 5 + pre-1960 combined/post-2020 combined.

  - 7 + IECC Climate Zone lumped into: 1-2+3A, 3B-3C, 4, 5, 6, 7 except AK, 7AK-8AK.

  - 7 + IECC Climate Zone lumped into: 1-2-3, 4-8.

### Water Heater Efficiency

#### Description

The efficiency and type of the water heater by heating fuel.

#### Distribution Sources

- U.S. EIA 2020 RECS microdata.

- Heat pump water heaters: 2016-17 RBSA II for WA and OR; Butzbaugh et al. ([2017](https://www.osti.gov/biblio/1433775)). *US HPWH Market Transformation: Where We’ve Been and Where to Go Next* for remainder of regions.

- Penetration of HPWH for Maine (6.71%) calculated based on total number of HPWH units (from AWHI Stakeholder Meeting 12/08/2022) and total housing units (from <https://www.census.gov/quickfacts/ME>).

#### Direct Conditional Dependencies

- State

- Water Heater Fuel

#### Options

Water Heater Efficiency options define the technical details of the standalone water heaters and solar thermal water heaters with storage backup, from fuel type to the presence of flue (Table “Water Heater Efficiency options and arguments that vary for each option of storage and tankless water heaters.”). The following arguments are constant across the non-solar standalone water heater options. The arguments for solar water heater options are available further down.

- `water_heater_backup_heating_capacity`: auto

- `water_heater_has_flue_or_chimney`: auto

- `water_heater_heating_capacity`: auto

- `water_heater_num_bedrooms_served`: auto

- `water_heater_operating_mode`: auto

- `water_heater_setpoint_temperature`: 125

- `water_heater_standby_loss`: 0

- `water_heater_jacket_rvalue`: 0

- `water_heater_tank_model_type`: auto

- `water_heater_usage_bin`: auto

- `water_heater_uses_desuperheater`: auto

- `solar_thermal_system_type`: none

- `solar_thermal_collector_area`: 40

- `solar_thermal_collector_loop_type`: liquid indirect

- `solar_thermal_collector_type`: single glazing black

- `solar_thermal_collector_azimuth`: 0

- `solar_thermal_collector_tilt`: 0

- `solar_thermal_collector_rated_optical_efficiency`: 0.77

- `solar_thermal_collector_rated_thermal_losses`: 0.793

- `solar_thermal_storage_volume`: auto

- `solar_thermal_solar_fraction`: 0

For heat pump water heaters the `water_heater_efficiency_type` UniformEnergyFactor is used; EnergyFactor is currently used for all other water heaters.

<div id="table:hc_opt_water_heater_eff" data-source="3c_ResStockInputs.tex">

| Option name | `water_heater_type` | `water_heater_fuel_type` | `water_heater_tank_volume` | `water_heater_efficiency_type` | `water_heater_recovery_efficiency` |
|:---|:---|:---|:---|:---|:---|
| Electric Heat Pump, 50 gal, 3.45 UEF | heat pump water heater | electricity | 50 | 3.45 | 0 |
| Electric Heat Pump, 66 gal, 3.35 UEF | heat pump water heater | electricity | 66 | 3.35 | 0 |
| Electric Heat Pump, 80 gal, 3.45 UEF | heat pump water heater | electricity | 80 | 3.45 | 0 |
| Electric Premium | storage water heater | electricity | auto | 0.95 | 0 |
| Electric Standard | storage water heater | electricity | auto | 0.92 | 0 |
| Electric Tankless | instantaneous water heater | electricity | 0 | 0.99 | 0 |
| FIXME Fuel Oil Indirect | storage water heater | fuel oil | auto | 0.62 | 0.78 |
| Fuel Oil Premium | storage water heater | fuel oil | auto | 0.68 | 0.9 |
| Fuel Oil Standard | storage water heater | fuel oil | auto | 0.62 | 0.78 |
| Natural Gas Premium | storage water heater | natural gas | auto | 0.67 | 0.78 |
| Natural Gas Standard | storage water heater | natural gas | auto | 0.59 | 0.76 |
| Natural Gas Tankless | instantaneous water heater | natural gas | 0 | 0.82 | 0 |
| Other Fuel | storage water heater | coal | auto | 0.59 | 0.76 |
| Propane Premium | storage water heater | propane | auto | 0.67 | 0.78 |
| Propane Standard | storage water heater | propane | auto | 0.59 | 0.76 |
| Propane Tankless | instantaneous water heater | propane | 0 | 0.82 | 0 |
| Wood | storage water heater | wood | auto | 0.59 | 0.76 |

Water Heater Efficiency options and arguments that vary for each option of storage and tankless water heaters.

</div>

Solar thermal water heaters are characterized by `solar_thermal_system_type=hot water`. The following arguments are constant across the solar water heater options:

- `water_heater_type`: storage water heater

- `water_heater_backup_heating_capacity`: auto

- `water_heater_has_flue_or_chimney`: auto

- `water_heater_heating_capacity`: auto

- `water_heater_num_bedrooms_served`: auto

- `water_heater_operating_mode`: auto

- `water_heater_setpoint_temperature`: 125

- `water_heater_standby_loss`: 0

- `water_heater_tank_model_type`: auto

- `water_heater_tank_volume`: auto

- `water_heater_usage_bin`: auto

- `water_heater_uses_desuperheater`: auto

- `solar_thermal_system_type`: hot water

- `solar_thermal_collector_area`: 40

- `solar_thermal_collector_loop_type`: liquid indirect

- `solar_thermal_collector_type`: single glazing black

- `solar_thermal_collector_rated_optical_efficiency`: 0.77

- `solar_thermal_collector_rated_thermal_losses`: 0.793

- `solar_thermal_storage_volume`: auto

- `solar_thermal_solar_fraction`: 0

The options for solar water heaters in ResStock are a combination of orientation and backup fuel, Table “Water Heater Efficiency options and arguments that vary for each option of solar water heaters.”.

<div id="table:hc_opt_solar_water_heater_eff" data-source="3c_ResStockInputs.tex">

| Option name | `solar_thermal_collector_azimuth` | `solar_thermal_collector_tilt` | `water_heater_fuel_type` | `water_heater_efficiency_type` | `water_heater_recovery_efficiency` | `water_heater_jacket_rvalue` |
|:---|:---|:---|:---|:---|:---|:---|
| Solar Thermal, 40 sqft, East, Roof Pitch, Electric Standard Backup | 90 | roofpitch | electricity | 0.97 | 0.98 | 6.2 |
| Solar Thermal, 40 sqft, North, Roof Pitch, Electric Standard Backup | 0 | roofpitch | electricity | 0.97 | 0.98 | 6.2 |
| Solar Thermal, 40 sqft, South, Roof Pitch, Electric Standard Backup | 180 | roofpitch | electricity | 0.97 | 0.98 | 6.2 |
| Solar Thermal, 40 sqft, South, Roof Pitch, Fuel Oil Standard Backup | 180 | roofpitch | fuel oil | 0.62 | 0.78 | 0 |
| Solar Thermal, 40 sqft, South, Roof Pitch, Natural Gas Standard Backup | 180 | roofpitch | natural gas | 0.59 | 0.76 | 0 |
| Solar Thermal, 40 sqft, South, Roof Pitch, Propane Standard Backup | 180 | roofpitch | propane | 0.59 | 0.76 | 0 |
| Solar Thermal, 40 sqft, West, Roof Pitch, Electric Standard Backup | 270 | roofpitch | electricity | 0.97 | 0.98 | 6.2 |

Water Heater Efficiency options and arguments that vary for each option of solar water heaters.

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Water Heater Efficiency characteristic” on storage and tankless water heaters and Table “The ResStock argument definitions set in the Solar Hot Water characteristic” on solar water heaters. See the OpenStudio-HPXML [Water Heating Systems](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-water-heating-systems) and [Solar Thermal](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-solar-thermal) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_water_heater_eff" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `water_heater_type` | true |  | Choice | none, storage water heater, instantaneous water heater, heat pump water heater, space-heating boiler with storage tank, space-heating boiler with tankless coil | The type of water heater. Use 'none' if there is no water heater. |
| `water_heater_fuel_type` | true |  | Choice | electricity, natural gas, fuel oil, propane, wood, coal | The fuel type of water heater. Ignored for heat pump water heater. |
| `water_heater_tank_volume` | false | gal | Double | auto | Nominal volume of water heater tank. If not provided, the OS-HPXML default (see [Conventional Storage](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#conventional-storage), [Heat Pump](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#heat-pump) is used.) |
| `water_backup_heaing_efficiency` | false | Btu/hr | Double | auto | Backup heating capacity for a heat pump water heater. If not provided, the OS-HPXML default (see [Heat Pump](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#heat-pump).) |
| `water_heater_efficiency_type` | true |  | Choice | EnergyFactor, UniformEnergyFactor | The efficiency type of water heater. Does not apply to space-heating boilers. |
| `water_heater_efficiency` | true |  | Double |  | Rated Energy Factor or Uniform Energy Factor. Does not apply to space-heating boilers. |
| `water_heater_usage_bin` | false |  | Choice | auto, very small, low, medium, high | The usage of the water heater. Only applies if Efficiency Type is UniformEnergyFactor and Type is not instantaneous water heater. Does not apply to space-heating boilers. |
| `water_heater_recovery_efficiency` | false | Frac | Double | auto | Ratio of energy delivered to water heater to the energy content of the fuel consumed by the water heater. Only used for non-electric storage water heaters. |
| `water_heater_heating_capacity` | false | Btu/hr | Double | auto | Heating capacity. Only applies to storage water heater and heat pump water heater (compressor). If not provided, the OS-HPXML default (see [Conventional Storage](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#conventional-storage), [Heat Pump](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#heat-pump) is used.) |
| `water_heater_standby_loss` | false | deg-F/hr | Double | auto | The standby loss of water heater. Only applies to space-heating boilers. |
| `water_heater_jacket_rvalue` | false | h-ft<sup>2</sup>-R/Btu | Double |  | The jacket R-value of water heater. Doesn't apply to instantaneous water heater or space-heating boiler with tankless coil. |
| `water_heater_setpoint_temperature` | false | deg-F | Double | auto | The setpoint temperature of water heater. |
| `water_heater_num_bedrooms_served` | false | \# | Integer |  | Number of bedrooms served (directly or indirectly) by the water heater. Only needed if single-family attached or apartment unit and it is a shared water heater serving multiple housing units. Used to apportion water heater tank losses to the unit. |
| `water_heater_uses_desuperheater` | false |  | Boolean | auto, true, false | Requires that the housing unit has a air-to-air, mini-split, or ground-to-air heat pump or a central air conditioner or mini-split air conditioner. If not provided, assumes no desuperheater. |
| `water_heater_tank_model_type` | false |  | Choice | auto, mixed, stratified | Type of tank model to use. The 'stratified' tank generally provide more accurate results, but may significantly increase run time. Applies only to storage water heater. |
| `water_heater_operating_mode` | false |  | Choice | auto, hybrid/auto, heat pump only | The water heater operating mode. The 'heat pump only' option only uses the heat pump, while 'hybrid/auto' allows the backup electric resistance to come on in high demand situations. This is ignored if a scheduled operating mode type is selected. Applies only to heat pump water heater. |
| `water_heater_has_flue_or_chimney` | true |  | String |  | Whether the water heater has a flue or chimney. |

The ResStock argument definitions set in the Water Heater Efficiency characteristic

</div>

<div id="table:hc_arg_def_solar_hot_water" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `solar_thermal_system_type` | true |  | Choice | none, hot water | The type of solar thermal system. Use 'none' if there is no solar thermal system. |
| `solar_thermal_collector_area` | true | ft<sup>2</sup> | Double |  | The collector area of the solar thermal system. |
| `solar_thermal_collector_loop_type` | true |  | Choice | liquid direct, liquid indirect, passive thermosyphon | The collector loop type of the solar thermal system. |
| `solar_thermal_collector_type` | true |  | Choice | evacuated tube, single glazing black, double glazing black, integrated collector storage | The collector type of the solar thermal system. |
| `solar_thermal_collector_azimuth` | true | degrees | Double |  | The collector azimuth of the solar thermal system. Azimuth is measured clockwise from north (e.g., North=0, East=90, South=180, West=270). |
| `solar_thermal_collector_tilt` | true | degrees | String |  | The collector tilt of the solar thermal system. Can also enter, e.g., RoofPitch, RoofPitch+20, Latitude, Latitude-15, etc. |
| `solar_thermal_collector_rated_optical_efficiency` | true | frac | Double |  | The collector rated optical efficiency of the solar thermal system. |
| `solar_thermal_collector_rated_thermal_losses` | true | Btu/hr-ft<sup>2</sup>-R | Double |  | The collector rated thermal losses of the solar thermal system. |
| `solar_thermal_storage_volume` | false | gal | Double | auto | The storage volume of the solar thermal system. |
| `solar_thermal_solar_fraction` | true | frac | Double |  | The solar fraction of the solar thermal system. If provided, overrides all other solar thermal inputs. |

The ResStock argument definitions set in the Solar Hot Water characteristic

</div>

#### Distribution Assumptions

- Water heater blanket is used as a proxy for premium storage tank water heaters.

- Heat Pump Water Heaters are added in manually as they are not in the survey; all have default efficiency: Electric Heat Pump, 50 gal, 3.45 UEF.

- Solar thermal water heaters: backup is informed by secondary water heater fuel type; electric backup is assumed if no secondary water heating. All collectors are assumed 40 sqft, roof pitch; collector orientation diversity is based on rooftop solar PV orientation for those with electric backup; for fuel backup, it is assumed south-facing.

- Due to low sample sizes, fallback rules are applied, with lumping of:

  - State: Census Division RECS

  - State: Census Region

  - State: National

## Hot Water Distribution

ResStock follows the OpenStudio-HPXML default assumptions when modeling hot water distribution, see the OpenStudio-HPXML [Hot Water Distribution](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-hot-water-distribution) documentation. Pipes are not explicitly modeled for any distribution systems, and correlations are instead used for determining the amount of hot water waste and heat gains in the living space depending on the hot water distribution system type and insulation. For a recirculation distribution system, the pipe length is calculated differently and additional inputs (e.g., power rating, control type) are used to specify the recirculation pump and pipe loop length. While recirculation options are available, all housing units in the baseline are assumed to have uninsulated trunk and branch hot water distribution system with copper pipes and without recirculation or drain water heat recovery. The inputs are captured in a single housing characteristic Hot Water Distribution.

### Hot Water Distribution

#### Description

Hot water piping material and insulation level.

#### Distribution Data Sources

- Engineering judgment.

#### Direct Conditional Dependencies

No dependencies.

#### Options

For the ResStock baseline baseline, all Hot Water Distribution is assumed to be “Uninsulated, trunk and branch, copper pipes.” This option specifies the following ResStock arguments.

- `hot_water_distribution_system_type` = standard

- `hot_water_distribution_recirc_control_type` = no control

- `dwhr_facilities_connected` = none

- `dwhr_equal_flow` = true

- `dwhr_efficiency` = 0.0.

For retrofit upgrades, other options are available and can be defined using the following arguments. For the argument definitions, see Table “The ResStock argument definitions set in the Hot Water Distribution characteristic”. See the OpenStudio-HPXML [Hot Water Distribution](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-hot-water-distribution) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hot_water_dist" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hot_water_distribution_system_type` | true |  | Choice | Standard, Recirculation | The type of the hot water distribution system. |
| `hot_water_distribution_standard_piping_length` | false | ft | Double | auto | If the distribution system is Standard, the length of the piping. |
| `hot_water_distribution_recirc_control_type` | false |  | Choice | auto, no control, timer, temperature, presence sensor demand control, manual demand control | If the distribution system is Recirculation, the type of hot water recirculation control, if any. |
| `hot_water_distribution_recirc_piping_length` | false | ft | Double | auto | If the distribution system is Recirculation, the length of the recirculation piping. |
| `hot_water_distribution_recirc_branch_piping_length` | false | ft | Double | auto | If the distribution system is Recirculation, the length of the recirculation branch piping. If not provided, the OS-HPXML default (see [Recirculation (In-Unit)](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#recirculation-in-unit)) is used. |
| `hot_water_distribution_recirc_pump_power` | false | W | Double | auto | If the distribution system is Recirculation, the recirculation pump power. |
| `hot_water_distribution_pipe_r` | false | h-ft<sup>2</sup>-R/Btu | Double | auto | Nominal R-value of the pipe insulation. |
| `dwhr_facilities_connected` | true |  | Choice | none, one, all | Which facilities are connected for the drain water heat recovery. Use 'none' if there is no drain water heat recovery system. |
| `dwhr_equal_flow` | false |  | Boolean | auto, true, false | Whether the drain water heat recovery has equal flow. |
| `dwhr_efficiency` | false | Frac | Double |  | The efficiency of the drain water heat recovery. |

The ResStock argument definitions set in the Hot Water Distribution characteristic

</div>

#### Distribution Assumptions

No assumptions are made.

## Hot Water Fixtures

Following the OpenStudio-HPXML default assumption, ResStock models hot water fixtures as 60% faucets and 40% showers and baths, operating at a mixed water temperature of 105° F for all housing units. None of the fixtures are assumed to be low-flow. However, low-flow options are available as upgrades.

The fraction of low-flow fixtures adjusts the demand to account for fixture efficiency. The demand is also multiplied by a fixture usage multiplier to add diversity. The hot water fixture usage multiplier is given by a log-normal distribution of values ranging from 40% to 200% (with mean at 80%[^1]) derived from the field data of 1,700 residential electric resistance water heaters in a demand management program in the U.S. Northeast census division.

### Hot Water Fixtures

#### Description

Hot water fixture usage and flow levels.

#### Distribution Data Sources

- Field data from a demand management program with 1,700 residential electric resistance water heaters in the Northeast U.S. census division.

#### Direct Conditional Dependencies

- Usage Level.

#### Options

The Hot Water Fixtures options are usage bins ranging from “50% Usage” to “200% Usage” at 10% increments. For the ResStock baseline, the options are log-normally distributed between 40% and 200%, with the peak at 80%. All options have both `water_fixtures_shower_low_flow` and `water_fixtures_sink_low_flow` set to false. `water_fixtures_usage_multiplier` is set according to their option names.

For the argument definitions, see Table “The ResStock argument definitions set in the Hot Water Fixtures characteristic”. See the OpenStudio-HPXML [Water Fixtures](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-water-fixtures) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hot_water_fix" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `water_fixtures_shower_low_flow` | true |  | Boolean | true, false | Whether the shower fixture is low flow. |
| `water_fixtures_sink_low_flow` | true |  | Boolean | true, false | Whether the sink fixture is low flow. |
| `water_fixtures_usage_multiplier` | false |  | Double | auto | Multiplier on the hot water usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Hot Water Fixtures characteristic

</div>

#### Distribution Assumptions

- A log-normal distribution was shown to match the distribution of annual energy consumption.

- The data shows appoximately a log-normal distribution. From the data, the average multiplier is 0.8 and the standard deviation is 0.2. The average multiplier was mean-shifted from 0.8 to 1 average usage.

- Low, Medium, and High usage is assigned based on the lower 25th percent, middle 50th percent, and upper 25th percent.

## Hot Water Appliances

For dishwashers and clothes washers, their daily demand for hot water (in gallons per day) is calculated according to ANSI/RESNET/ICC 301 standard. The standard uses the rated values from the product EnergyGuide label and the number of bedrooms to estimate the number of annual cycles, and thus, annual energy and hot water uses. The energy and hot water uses are further adjusted for the number of occupants in a home and multiplied by an appliance usage multiplier to add diversity, representing high-usage or low-usage occupants. These usage multipliers are given by a simple, manually created distribution of values ranging from 80% to 120%, with mean centered at 100%. The energy to heat the water and distribution losses are attributed to the water heater.

The stochastic occupant model is used to produce detailed schedule inputs from the hot water fixtures and appliances. The schedules are combined with the daily demands to calculate the peak flow rate (or design level) and peak-normalized schedules. In other words, the schedules are normalized and specify when hot water is used, not how much hot water is used; when multiplied by the peak flow rate, they aggregate to the total hot water demand calculated.

# Appliances

## Usage

### Modeling Approach

ResStock models the diversity of appliance usage in a couple of ways. The first way is through scaling the energy by usage multipliers. There are three usage levels—low, medium, and high—which are used to assign usage multipliers. The characteristics that use appliance-specific usage multipliers are clothes dryer, clothes washer, cooking range, dishwasher, hot water fixtures, plug load diversity, refrigerator, misc extra refrigerator, and misc freezer. See each of these subsections for the specific multipliers used to diversify their energy consumption.

The second way is through the number and timing of appliance events throughout the year, which is dealt with in the stochastic schedule generator. See Section “Schedule Creation” for more information about when and how long the events occur for different schedules.

### Usage Level

#### Description

Usage of major appliances relative to the national average.

#### Distribution Data Source(s)

Engineering judgment and calibration.

#### Direct Conditional Dependencies

None.

#### Options

The options are low, medium, and high. The distribution values are 25% for low, 50% for medium, and 25% for high. These options do not assign ResStock arguments.

#### Distribution Assumption(s)

None.

## Refrigeration

### Modeling Approach

Refrigeration energy is modeled for both refrigerators and standalone freezers. Each of these appliances is modeled by specifying the rated annual energy and a usage multiplier. There are primary refrigerators and, sometimes, a secondary refrigerator (misc extra refrigerator). Only up to two refrigerators and up to one standalone freezer are modeled. To account for additional refrigeration, correction factors derived using the count of refrigerators (which includes mini-fridges) and freezers from RECS 2020 are applied to each state. The timeseries schedules are handled by OpenStudio-HPXML. Currently, there are weekday and weekend schedules, and monthly multipliers.

### Refrigerator

#### Description

The presence and rated efficiency of the primary refrigerator.

#### Distribution Data Source(s)

Constructed using U.S. EIA 2020 RECS microdata. Age of refrigerator converted to efficiency levels using ENERGY STAR shipment-weighted efficiencies by year data from Home Energy Saver.[^2]

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- State

- Tenure

- Vintage.

#### Options

ResStock differentiates primary refrigerators based on their efficiency level. In the baseline stock, there are seven discrete efficiency levels ranging from EF 6.7 to EF 21.9, as well as a “None” option for housing units that do not have a refrigerator. The Refrigerator characteristic sets the `refrigerator_present`, `refrigerator_location`, and `refrigerator_rated_annual_kwh` arguments (Table “Refrigerator options and arguments that vary for each option”). The `refrigerator_location` argument is set to auto.

<div id="table:hc_opt_ref" data-source="3c_ResStockInputs.tex">

| Option name | `refrigerator_present` | `refrigerator_rated_annual_kwh` |
|:------------|:-----------------------|:--------------------------------|
| EF 6.7      | true                   | 1139                            |
| EF 10.2     | true                   | 748                             |
| EF 10.5     | true                   | 727                             |
| EF 15.9     | true                   | 480                             |
| EF 17.6     | true                   | 433                             |
| EF 19.9     | true                   | 383                             |
| EF 21.9     | true                   | 348                             |
| None        | false                  | 0                               |

Refrigerator options and arguments that vary for each option

</div>

For the argument definitions, see “The ResStock argument definitions set in the Refrigerator characteristic”. See the [OpenStudio-HPXML Refrigerators](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-refrigerators) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_refrigerator" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `refrigerator_present` | true |  | Boolean | true, false | Whether there is a refrigerator present. |
| `refrigerator_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, garage, other housing unit, other heated space, other multifamily buffer space, other non-freezing space | The space type for the refrigerator location. If not provided, the OS-HPXML default (see [HPXML Refrigerators](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-refrigerators)) is used. |
| `refrigerator_rated_annual_kwh` | false | kWh/yr | Double | auto | The EnergyGuide rated annual energy consumption for a refrigerator. |

The ResStock argument definitions set in the Refrigerator characteristic

</div>

#### Distribution Assumption(s)

The current year is assumed to be 2022. Currently, each year has its own distribution and then we average out the distributions to get the distribution for the age bins. The Energy Factor for all years are weighted equally when calculating the average distribution for the age bins. ENERGY STAR distributions from 2009 dependent on Geometry Building Type RECS, Federal Poverty Level, and Tenure are used to calculate efficiency distribution in RECS2020. ENERGY STAR Refrigerators are assumed to be 10% more efficient than standard. Due to the low sample count, the following coarsening rules are incorporated.

1.  State coarsened to Census Division RECS, with AK/HI separate.

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Vintage with Vintage ACS

5.  Vintage with combined 1960s

6.  Vintage with combined 1960s and post 2000s

7.  Federal Poverty Level coarsened every 100%

8.  Federal Poverty Level coarsened every 200%

9.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

10. Census Division RECS to Census Region

11. Census Region to National.

### Refrigerator Usage Level

#### Description

Refrigerator energy usage level multiplier.

#### Distribution Data Source(s)

- Not applicable—direct translation of the “Usage” Usage input file.

#### Direct Conditional Dependencies

- Usage Level.

#### Options

The refrigerator usage level is set based on the usage level characteristic. It is 95% Usage when the usage level is Low, 100% Usage when the usage level is Medium, and 105% Usage when the usage level is High. The characteristic sets the `refrigerator_usage_multiplier` argument (Table “Refrigerator options and arguments that vary for each option”).

<div id="table:hc_opt_ref_use" data-source="3c_ResStockInputs.tex">

| Option name | `refrigerator_usage_multiplier` |     |
|:------------|:--------------------------------|:----|
| 95% Usage   | 0.95                            |     |
| 100% Usage  | 1.0                             |     |
| 105% Usage  | 1.05                            |     |

Refrigerator options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Refrigerator Usage Level characteristic”.

<div id="table:hc_arg_def_refrigerator_usage_level" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `refrigerator_usage_multiplier` | false |  | Double | auto | Multiplier on the refrigerator energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Refrigerator Usage Level characteristic

</div>

#### Distribution Assumption(s)

None

### Misc Extra Refrigerator

#### Description

The presence and rated efficiency of the secondary refrigerator.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

- Age of refrigerator converted to efficiency levels using ENERGY STAR shipment-weighted efficiencies by year data from Home Energy Saver.[^3]

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- State

- Tenure

- Vintage.

#### Options

Extra refrigerators are specified using the same Energy Factor (EF) and annual rated kWh options as primary refrigerators. The characteristic set the `extra_refrigerator_present`, `extra_refrigerator_location`, `extra_refrigerator_rated_annual_kwh`, and `extra_refrigerator_usage_multiplier` ResStock arguments (Table “Misc Extra Refrigerator options and arguments that vary for each option”). If an extra refrigerator is present, the location is always set to auto. The usage multiplier varies by state and is set to account for the presence of teriary refrigerators and beyond, see “Misc Extra Refrigerator usage multiplier varies by state.”.

<div id="table:hc_opt_extra_ref" data-source="3c_ResStockInputs.tex">

| Option name | `extra_refrigerator_present` | `extra_refrigerator_rated_annual_kwh` |  |  |
|:---|:---|:---|:---|:---|
| EF 6.7 | true | 1139 |  |  |
| EF 10.2 | true | 748 |  |  |
| EF 10.5 | true | 727 |  |  |
| EF 15.9 | true | 480 |  |  |
| EF 17.6 | true | 433 |  |  |
| EF 19.9 | true | 383 |  |  |
| EF 21.9 | true | 348 |  |  |
| None | false | 0 |  |  |

Misc Extra Refrigerator options and arguments that vary for each option

</div>

<div id="table:hc_opt_extra_ref_usage_mult" data-source="3c_ResStockInputs.tex">

| State | `extra_refrigerator_usage_multiplier` |
|:------|:--------------------------------------|
| AK    | 1.80                                  |
| AL    | 1.76                                  |
| AR    | 1.90                                  |
| AZ    | 1.74                                  |
| CA    | 1.86                                  |
| CO    | 1.85                                  |
| CT    | 1.96                                  |
| DC    | 2.15                                  |
| DE    | 1.68                                  |
| FL    | 1.87                                  |
| GA    | 1.74                                  |
| HI    | 1.94                                  |
| IA    | 1.77                                  |
| ID    | 1.62                                  |
| IL    | 1.82                                  |
| IN    | 1.78                                  |
| KS    | 1.77                                  |
| KY    | 1.80                                  |
| LA    | 1.88                                  |
| MA    | 2.00                                  |
| MD    | 1.94                                  |
| ME    | 1.88                                  |
| MI    | 1.73                                  |
| MN    | 1.72                                  |
| MO    | 1.76                                  |
| MS    | 1.85                                  |
| MT    | 1.69                                  |
| NC    | 1.80                                  |
| ND    | 1.73                                  |
| NE    | 1.85                                  |
| NH    | 1.90                                  |
| NJ    | 1.81                                  |
| NM    | 1.90                                  |
| NV    | 1.87                                  |
| NY    | 1.91                                  |
| OH    | 1.81                                  |
| OK    | 1.86                                  |
| OR    | 1.84                                  |
| PA    | 1.73                                  |
| RI    | 1.91                                  |
| SC    | 1.83                                  |
| SD    | 1.83                                  |
| TN    | 1.86                                  |
| TX    | 1.84                                  |
| UT    | 1.78                                  |
| VA    | 1.80                                  |
| VT    | 1.82                                  |
| WA    | 1.76                                  |
| WI    | 1.74                                  |
| WV    | 1.68                                  |
| WY    | 1.80                                  |

Misc Extra Refrigerator usage multiplier varies by state.

</div>

For the argument definitions, see “The ResStock argument definitions set in the Refrigerator Usage Level characteristic”. See the [OpenStudio-HPXML Refrigerators](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-refrigerators) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_misc_extra_refrigerator" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `extra_refrigerator_present` | true |  | Boolean | true, false | Whether there is an extra refrigerator present. |
| `extra_refrigerator_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, garage, other housing unit, other heated space, other multifamily buffer space, other non-freezing space | The space type for the extra refrigerator location. |
| `extra_refrigerator_rated_annual_kwh` | false | kWh/yr | Double | auto | The EnergyGuide rated annual energy consumption for an extra refrigerator. |
| `extra_refrigerator_usage_multiplier` | false |  | Double | auto | Multiplier on the extra refrigerator energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Refrigerator Usage Level characteristic

</div>

#### Distribution Assumption(s)

The current year is assumed to be 2022. Currently, each year has its own distribution and then we average out the distributions to get the distribution for the age bins. EF for all years are weighted equally when calculating the average distribution for the age bins. ENERGY STAR distributions from 2009 dependent on Geometry Building Type RECS, Federal Poverty Level, and Tenure are used to calculate efficiency distribution in RECS 2020. ENERGY STAR refrigerators assumed to be 10% more efficient than standard. Due to the low sample count, the input file is constructed by downscaling a housing unit sub-input file with a household sub-input file. The sub-input files have the following dependencies: housing unit sub-input file: dependencies = Geometry Building Type RECS, State, and Vintage, with the following fallback coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Vintage with Vintage ACS

5.  Vintage with combined 1960s

6.  Vintage with combined 1960s and post 2000s

7.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

8.  Census Division RECS to Census Region.

Census Region to National Assumption: Household sub-input file : dependencies = Geometry Building Type RECS, State, Tenure, and Federal Poverty Level, with the following fallback coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

7.  Census Division RECS to Census Region

8.  Census Region to National.

In combining the housing unit sub-input file and household sub-input file, the conditional relationships are ignored across (Heating Fuel, \[Tenure, Federal Poverty Level\]).

### Misc Freezer

#### Description

The presence and rated efficiency of a standalone freezer.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- State

- Tenure.

#### Options

The Misc Freezer option in baseline has an EF of 12, intended to represent the national average. The characteristic sets the `freezer_present`, `freezer_location`, `freezer_rated_annual_kwh`, and `freezer_usage_multiplier` ResStock arguments (Table “Misc Freezer options and arguments that vary for each option”). The usage multiplier varies by state and is set to account for the presence of extra freezers, see “Misc Freezer usage multiplier varies by state.”.

<div id="table:hc_opt_freezer" data-source="3c_ResStockInputs.tex">

| Option name | `freezer_present` | `freezer_location` | `freezer_rated_annual_kwh` |
|:---|:---|:---|:---|
| EF 12, National Average | true | auto | 935 |
| None | false | auto | 0 |

Misc Freezer options and arguments that vary for each option

</div>

<div id="table:hc_opt_freezer_usage_mult" data-source="3c_ResStockInputs.tex">

| State | `freezer_usage_multiplier` |
|:------|:---------------------------|
| AK    | 1.27                       |
| AL    | 1.34                       |
| AR    | 1.25                       |
| AZ    | 1.09                       |
| CA    | 1.06                       |
| CO    | 1.06                       |
| CT    | 1.08                       |
| DC    | 1.21                       |
| DE    | 1.12                       |
| FL    | 1.04                       |
| GA    | 1.26                       |
| HI    | 1.21                       |
| IA    | 1.13                       |
| ID    | 1.38                       |
| IL    | 1.07                       |
| IN    | 1.25                       |
| KS    | 1.04                       |
| KY    | 1.19                       |
| LA    | 1.32                       |
| MA    | 1.06                       |
| MD    | 1.20                       |
| ME    | 1.09                       |
| MI    | 1.22                       |
| MN    | 1.27                       |
| MO    | 1.07                       |
| MS    | 1.34                       |
| MT    | 1.33                       |
| NC    | 1.10                       |
| ND    | 1.29                       |
| NE    | 1.19                       |
| NH    | 1.23                       |
| NJ    | 1.05                       |
| NM    | 1.17                       |
| NV    | 1.02                       |
| NY    | 1.06                       |
| OH    | 1.12                       |
| OK    | 1.26                       |
| OR    | 1.39                       |
| PA    | 1.18                       |
| RI    | 0.97                       |
| SC    | 1.13                       |
| SD    | 1.37                       |
| TN    | 1.25                       |
| TX    | 1.18                       |
| UT    | 1.20                       |
| VA    | 1.14                       |
| VT    | 1.25                       |
| WA    | 1.14                       |
| WI    | 1.20                       |
| WV    | 1.15                       |
| WY    | 1.32                       |

Misc Freezer usage multiplier varies by state.

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Refrigerator Usage Level characteristic”. See the [OpenStudio-HPXML Freezers](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-freezers) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_misc_freezer" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `freezer_present` | true |  | Boolean | true, false | Whether there is a freezer present. |
| `freezer_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, garage, other housing unit, other heated space, other multifamily buffer space, other non-freezing space | The space type for the freezer location. |
| `freezer_rated_annual_kwh` | false | kWh/yr | Double | auto | The EnergyGuide rated annual energy consumption for a freezer. |
| `freezer_usage_multiplier` | false |  | Double | auto | Multiplier on the freezer energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Refrigerator Usage Level characteristic

</div>

#### Distribution Assumption(s)

The national average EF is 12 based on the 2014 Building America house simulation protocols.

Due to the low sample count, the input file is constructed with the following coarsening order.

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

7.  Census Division RECS to Census Region

8.  Census Region to National.

## Cooking

### Modeling Approach

ResStock models all cooking units as ranges with an integrated (non-convection) oven located in the conditioned space. Housing units can have no cooking units. The fuel options include electric induction, electric resistance, gas, and propane, although more fuel options are available in OpenStudio-HPXML, see [Cooling Range/Oven](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-cooking-range-oven). The annual energy used for cooking is calculated per the Energy Rating Rated Home in ANSI/RESNET/ICC 301-2019 ((International Code Council 2019)) and is further adjusted by a Cooking Range Usage Level multiplier; see Section “Cooking Range Usage Level”. The annual energy is multiplied with a stochastically generated detailed cooking schedule based on ATUS to produce the cooking end-use load profile. See Section “Schedule Creation” for details on schedule generation.

ResStock also models the use of a range hood for cooking. However, the range hood operation does not use the cooking schedule. Instead, the range operates for one hour every day with a starting hour sampled by the Range Spot Vent Hour characteristic distribution; see Section “Range Spot Vent Hour”.

The next sections describe the building stock distributions for cooking, their assumptions, data sources, and argument assignment.

### Cooking Range

#### Description

Presence and fuel type of the cooking range.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- Heating Fuel

- State

- Tenure

- Vintage.

#### Options

ResStock baseline has four cooking range options, which include electric induction, electric resistance, natural gas, and propane, as well as a “none” option. The characteristic assigns the `cooking_range_oven_present`, `cooking_range_oven_location`, `cooking_range_oven_fuel_type`, `cooking_range_oven_is_induction`, `cooking_range_oven_is_convection` ResStock arguments (Table “Cooking Range options and arguments that vary for each option”). The `cooking_range_oven_is_convection` and `cooking_range_oven_location` is always set to auto.

<div id="table:hc_opt_cooking" data-source="3c_ResStockInputs.tex">

| Option name | `cooking_range_oven_present` | `cooking_range_oven_fuel_type` | `cooking_range_oven_is_induction` |
|:---|:---|:---|:---|
| Electric Induction | true | electricity | true |
| Electric Resistance | true | electricity | false |
| Gas | true | natural gas | false |
| None | false | natural gas | false |
| Propane | true | propane | false |

Cooking Range options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Cooking Range characteristic”. See the OpenStudio-HPXML [Cooking Range/Oven](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-cooking-range-oven) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_cooking_range" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `cooking_range_oven_present` | true |  | Boolean | true, false | Whether there is a cooking range/oven present. |
| `cooking_range_oven_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, garage, other housing unit, other heated space, other multifamily buffer space, other non-freezing space | The space type for the cooking range/oven location. |
| `cooking_range_oven_fuel_type` | true |  | Choice | electricity, natural gas, fuel oil, propane, wood, coal | Type of fuel used by the cooking range/oven. |
| `cooking_range_oven_is_induction` | false |  | Boolean | auto, true, false | Whether the cooking range is induction. |
| `cooking_range_oven_is_convection` | false |  | Boolean | auto, true, false | Whether the oven is convection. |

The ResStock argument definitions set in the Cooking Range characteristic

</div>

#### Distribution Assumption(s)

For Dual Fuel Range, the distribution is split equally between Electric and Natural Gas.

Due to low sample count, the input file is constructed by downscaling a housing unit sub-input file with a household sub-input file. The sub-input files have the following dependencies: housing unit sub-input file: deps = ‘Geometry Building Type RECS’, ‘State’, ‘Heating Fuel’, and ‘Vintage,’ with the following fallback coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Heating Fuel coarsened to Other Fuel, Wood and Propane combined

3.  Heating Fuel coarsened to Fuel Oil, Other Fuel, Wood and Propane combined

4.  Geometry Building Type RECS coarsened to SF/MF/MH

5.  Geometry Building Type RECS coarsened to SF and MH/MF

6.  Vintage coarsened to every 20 years before 2000 and every 10 years subsequently

7.  Vintage homes built before 1960 coarsened to pre-1960

8.  Vintage homes built after 2000 coarsened to 2000-20

9.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

10. Census Division RECS to Census Region

11. Census Region to National.

Household sub-input file : deps = ‘Geometry Building Type RECS’, ‘State’ ‘Tenure’, ‘Federal Poverty Level,’ with the following fallback coarsening order

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

7.  Census Division RECS to Census Region

8.  Census Region to National.

In combining the housing unit sub-input file and household sub-input file, the conditional relationships are ignored across ‘Heating Fuel’ and ‘Vintage’, as well as for ‘Tenure’ and ‘Federal Poverty Level’.

### Cooking Range Usage Level

#### Description

Cooking range energy usage level multiplier.

#### Distribution Data Source(s)

- Not applicable—direct translation of the Usage Level input file; see Section “Usage”.

#### Direct Conditional Dependencies

- Usage Level.

#### Options

The cooking range usage level is set based on the usage level characteristic (Section “Usage”). It is 80% Usage when the usage level is Low, 100% Usage when the usage level is Medium, and 120% Usage when the usage level is High. The characteristic sets the `cooking_range_oven_usage_multiplier` ResStock argument.

<div id="table:hc_opt_cooking" data-source="3c_ResStockInputs.tex">

| Option name | `cooking_range_oven_usage_multiplier` |
|:------------|:--------------------------------------|
| 80% Usage   | 0.8                                   |
| 100% Usage  | 1.0                                   |
| 120% Usage  | 1.2                                   |

Cooking Range Usage Level options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Cooking Range characteristic”. See the [OpenStudio-HPXML Refrigerators](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-refrigerators) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_cooking_range_usage_level" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `cooking_range_oven_usage_multiplier` | false |  | Double | auto | Multiplier on the cooking range/oven energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Cooking Range characteristic

</div>

#### Distribution Assumption(s)

None.

## Dishwasher

### Modeling Approach

ResStock models all dishwashers as a standalone appliance located in the conditioned space with hot water supplied by the water heater. Housing units can have no dishwasher. Dishwasher performance is defined by rated annual kWh along with other EnergyGuide label information, including place setting capacity assumed to be 12, label usage (cycles per week), electric and gas rate, and annual gas cost. The number of cycles is used to calculate the annual energy and hot water use for dishwasher per the Energy Rating Rated Home in ANSI/RESNET/ICC 301-2019 Addendum A ((International Code Council 2019)). The total energy and hot water use are further adjusted by a Dishwasher Usage Level multiplier (Section “Dishwasher Usage Level”) for added diversity.

The energy estimate is multiplied with a stochastically generated appliance schedule to produce the dishwasher end-use load profile. Similarly, the total hot water use is paired with a stochastic schedule to produce an appliance hot water draw schedule for the water heater. The appliance schedule and the hot water draw schedule line up in terms of the event onset, which comes from ATUS, but not the duration or magnitude, which are sampled from data from the RBSA survey ((Northwest Energy Efficiency Alliance 2024)). See Section “Schedule Creation” for details on schedule generation. The hot water energy for dishwasher is attributed to the hot water end use rather than the appliance.

The following subsections describe the characteristics, distributions, data sources, and arguments assigned for the dishwasher.

### Dishwasher

#### Description

The presence and rated efficiency of the dishwasher.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- State

- Tenure

- Vintage.

#### Options

The ResStock baseline has two dishwasher options, one at 290 rated kWh and one at 318 rated kWh, along with a “None” option.[^4] Both dishwasher options have arguments of true for `dishwasher_present`, auto for `dishwasher_location`, RatedAnnualkWh for `dishwasher_efficiency_type`, 0.12 for `dishwasher_label_electric_rate`, 1.09 for `dishwasher_label_gas_rate`, 4 for `dishwasher_label_usage`, and 12 for `dishasher_place_setting_capacity`; see Table “Dishwasher options and arguments that vary for each option”.

<div id="table:hc_opt_dish" data-source="3c_ResStockInputs.tex">

| Option name   | `dishwasher_efficiency` | `dishwasher_label_annual_gas_cost` |
|:--------------|:------------------------|:-----------------------------------|
| 290 Rated kWh | 290                     | 23                                 |
| 318 Rated kWh | 318                     | 25                                 |
| None          | 0                       | 0                                  |

Dishwasher options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Dishwasher characteristic”. See the OpenStudio-HPXML [Dishwasher](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-dishwasher) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_dishwasher" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `dishwasher_present` | true |  | Boolean | true, false | Whether there is a dishwasher present. |
| `dishwasher_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, garage, other housing unit, other heated space, other multifamily buffer space, other non-freezing space | The space type for the dishwasher location. |
| `dishwasher_efficiency_type` | true |  | Choice | RatedAnnualkWh, EnergyFactor | The efficiency type of dishwasher. |
| `dishwasher_efficiency` | false | RatedAnnualkWh or EnergyFactor | Double | auto | The efficiency of the dishwasher. |
| `dishwasher_label_electric_rate` | false | \$/kWh | Double | auto | The label electric rate of the dishwasher. |
| `dishwasher_label_gas_rate` | false | \$/therm | Double | auto | The label gas rate of the dishwasher. |
| `dishwasher_label_annual_gas_cost` | false | \$ | Double | auto | The label annual gas cost of the dishwasher. |
| `dishwasher_label_usage` | false | cyc/wk | Double | auto | The dishwasher loads per week. |
| `dishwasher_place_setting_capacity` | false | \# | Integer | auto | The number of place settings for the unit. Data obtained from manufacturer’s literature. |

The ResStock argument definitions set in the Dishwasher characteristic

</div>

#### Distribution Assumption(s)

The 2020 RECS survey does not contain ENERGY STAR rating of dishwashers. ENERGY STAR efficiency distributions with Geometry Building Type, Census Division RECS, Federal Poverty Level, and Tenure as dependencies are imported from RECS 2009.

Due to the low sample count, the input file is constructed with the following coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  Vintage coarsened to every 20 years before 2000 and every 10 years subsequently

7.  Vintage homes built before 1960 coarsened to pre-1960

8.  Vintage homes built after 2000 coarsened to 2000-20

9.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

10. Census Division RECS to Census Region.

### Dishwasher Usage Level

#### Description

Dishwasher energy usage level multiplier.

#### Distribution Data Source(s)

- Not applicable—direct translation of Usage Level; see Section “Usage”.

#### Direct Conditional Dependencies

- Usage Level.

#### Options

The dishwasher usage level is set based on the usage level characteristic; see Section “Usage”. It is 80% Usage when the usage level is Low, 100% Usage when the usage level is Medium, and 120% Usage when the usage level is High. The characteristic sets the `dishwasher_usage_multiplier` ResStock argument (Table “Dishwasher Usage Level options and arguments that vary for each option”).

<div id="table:hc_opt_dish_use" data-source="3c_ResStockInputs.tex">

| Option name | `dishwasher_usage_multiplier` |
|:------------|:------------------------------|
| 80% Usage   | 0.8                           |
| 100% Usage  | 1.0                           |
| 120% Usage  | 1.2                           |

Dishwasher Usage Level options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Dishwasher Usage Level characteristic”.

<div id="table:hc_arg_def_dishwasher_usage_level" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `dishwasher_usage_multiplier` | false |  | Double | auto | Multiplier on the dishwasher energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Dishwasher Usage Level characteristic

</div>

#### Distribution Assumption(s)

None.

## Clothes Washer

### Modeling Approach

ResStock models all clothes washers as a standalone appliance located in the conditioned space with hot water supplied by the water heater. Clothes Washer Presence defines whether the appliance is present in the housing unit and is created to influence the Clothes Dryer (Section “Clothes Dryer”) presence as a dependency. Clothes washer performance is defined by integrated modified Energy Factor along with other EnergyGuide label information, including rated annual kWh, capacity (volume), label usage (cycles per week), electric and gas rate, and annual gas cost.

The number of cycles is used to calculate the annual energy and hot water use for clothes washer per the Energy Rating Rated Home in ANSI/RESNET/ICC 301-2019 Addendum A ((International Code Council 2019)). The total energy and hot water use are further adjusted by a Clothes Washer Usage Level multiplier for added diversity.

The energy estimate is multiplied with a stochastically generated laundry schedule to produce the clothes washer end-use load profile. Similarly, the total hot water use is paired with a stochastic schedule to produce an appliance hot water draw schedule for the water heater. The appliance schedule and the hot water draw schedule line up in terms of the event onset, which comes from ATUS, but not the duration or magnitude, which are sampled from data from the RBSA survey ((Northwest Energy Efficiency Alliance 2024)). See Section “Schedule Creation” for details on schedule generation. The hot water energy for clothes washer is attributed to the hot water end use rather than the appliance.

The following subsections describe the characteristics, the distributions, assumptions, data sources, options, and argument assignments for clothes washers.

### Clothes Washer

#### Description

Presence and rated efficiency of the clothes washer.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Clothes Washer Presence

- Federal Poverty Level

- Geometry Building Type RECS

- Tenure

- Vintage.

#### Options

ResStock has two clothes washer options in baseline, along with a “None” option. Both clothes washer options have a `clothes_washer_location` of *auto*, a `clothes_washer_efficiency_type` of *IntegratedModifiedEnergyFactor*, a `clothes_washer_label_electric_rate` of 0.1065, a `clothes_washer_gas_rate` of 1.218, and a `clothes_washer_label_usage` of 7.538462. The arguments that differ between the two options are shown in Table “Clothes Washer options and arguments that vary for each option”.

<div id="table:opt_def_clothes washer" data-source="3c_ResStockInputs.tex">

| Option name | `clothes_washer_efficiency` | `clothes_washer_rated_annual_kwh` | `clothes_washer_label_annual_gas_cost` | `clothes_washer_capacity` |
|:---|:---|:---|:---|:---|
| ENERGY STAR | 2.07 | 123 | 9 | 3.68 |
| None | 0 | 0 | 0 | 0 |
| Standard | 0.95 | 387 | 24 | 3.5 |

Clothes Washer options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Clothes Washer characteristic”. See the OpenStudio-HPXML [Clothes Washer](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-clothes-washer) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_clothes washer" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `clothes_washer_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, garage, other housing unit, other heated space, other multifamily buffer space, other non-freezing space | The space type for the clothes washer location. |
| `clothes_washer_efficiency_type` | true |  | Choice | ModifiedEnergyFactor, IntegratedModifiedEnergyFactor | The efficiency type of the clothes washer. |
| `clothes_washer_efficiency` | false | ft<sup>3</sup>/kWh-cyc | Double | auto | The efficiency of the clothes washer. |
| `clothes_washer_rated_annual_kwh` | false | kWh/yr | Double | auto | The annual energy consumed by the clothes washer, as rated, obtained from the EnergyGuide label. This includes both the appliance electricity consumption and the energy required for water heating. If not provided, the OS-HPXML default (see [HPXML Clothes Washer](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-clothes-washer)) is used. |
| `clothes_washer_label_electric_rate` | false | \$/kWh | Double | auto | The annual energy consumed by the clothes washer, as rated, obtained from the EnergyGuide label. This includes both the appliance electricity consumption and the energy required for water heating. |
| `clothes_washer_label_gas_rate` | false | \$/therm | Double | auto | The annual energy consumed by the clothes washer, as rated, obtained from the EnergyGuide label. This includes both the appliance electricity consumption and the energy required for water heating. If not provided, the OS-HPXML default (see [HPXML Clothes Washer](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-clothes-washer)) is used. |
| `clothes_washer_label_annual_gas_cost` | false | \$ | Double | auto | The annual cost of using the system under test conditions. Input is obtained from the EnergyGuide label. |
| `clothes_washer_label_usage` | false | cyc/wk | Double | auto | The clothes washer loads per week. |
| `clothes_washer_capacity` | false | ft^3 | Double | auto | Volume of the washer drum. Obtained from the ENERGY STAR website or the manufacturer’s literature. |

The ResStock argument definitions set in the Clothes Washer characteristic

</div>

#### Distribution Assumption(s)

The 2020 RECS survey does not contain ENERGY STAR rating of clothes washers. ENERGY STAR efficiency distributions with Geometry Building Type, Federal Poverty Level, and Tenure as dependencies are imported from RECS 2009. Due to low sample count, the input file is constructed by downscaling a housing unit sub-input file with a household sub-input file. The sub-input files have the following dependencies: housing unit sub-input file: dependencies = Geometry Building Type RECS, State, Clothes Washer Presence, and Vintage, with the following coarsening order:

1.  Geometry Building Type RECS coarsened to SF/MF/MH

2.  Geometry Building Type RECS coarsened to SF and MH/MF

3.  Vintage coarsened to every 20 years before 2000 and every 10 years subsequently

4.  Vintage homes built before 1960 coarsened to pre-1960

5.  Vintage homes built after 2000 coarsened to 2000-20.

Household sub-input file: dependencies = Geometry Building Type RECS, State, Tenure, and Federal Poverty Level, with the following coarsening order:

1.  Geometry Building Type RECS coarsened to SF/MF/MH

2.  Geometry Building Type RECS coarsened to SF and MH/MF

3.  Federal Poverty Level coarsened every 100%

4.  Federal Poverty Level coarsened every 200%.

In combining the housing unit sub-input file and household sub-input file, the conditional relationships are ignored across Clothes Washer Presence and Vintage, as well as for Tenure and Federal Poverty Level.

### Clothes Washer Presence

#### Description

The presence of a clothes washer in the housing unit.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- State

- Tenure

- Vintage.

#### Options

This characteristic determines whether there is a clothes washer present in the housing unit. The characteristic sets the `clothes_washer_present` ResStock argument (Table “Clothes Washer Presence options and arguments that vary for each option”).

<div id="table:opt_def_clothes_washer" data-source="3c_ResStockInputs.tex">

| Option name | `clothes_washer_present` |
|:------------|:-------------------------|
| None        | false                    |
| Yes         | true                     |

Clothes Washer Presence options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Clothes Washer Presence characteristic”.

<div id="table:hc_arg_def_clothes_washer_presence" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `clothes_washer_present` | true |  | Boolean | true, false | Whether there is a clothes washer present. |

The ResStock argument definitions set in the Clothes Washer Presence characteristic

</div>

#### Distribution Assumption(s)

Due to the low sample count, the input file is constructed by downscaling a housing unit sub-input file with a household sub-input file. The sub-input files have the following dependencies. Housing unit sub-input file: dependencies = Geometry Building Type RECS, State, Heating Fuel, and Vintage, with the following coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Vintage coarsened to every 20 years before 2000 and every 10 years subsequently

5.  Vintage homes built before 1960 coarsened to pre-1960

6.  Vintage homes built after 2000 coarsened to 2000-20

7.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

8.  Census Division RECS to Census Region

9.  Census Region to National.

Household sub-input file: dependencies = Geometry Building Type RECS, State, Tenure, and Federal Poverty Level, with the following coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

7.  Census Division RECS to Census Region

8.  Census Region to National.

In combining the housing unit sub-input file and household sub-input file, the conditional relationships are ignored across Geometry Building Type RECS and Vintage, as well as for Tenure and Federal Poverty Level.

### Clothes Washer Usage Level

#### Description

Clothes washer energy usage level multiplier.

#### Distribution Data Source(s)

Not applicable.

#### Direct Conditional Dependencies

- Usage Level.

#### Options

The clothes washer usage level is set based on the usage level (Section “Usage”) characteristic. It is 80% Usage when the usage level is Low, 100% Usage when the usage level is Medium, and 120% Usage when the usage level is High. The characteristic sets the `clothes_washer_usage_multiplier` ResStock argument (Table “Clothes Washer Usage Level options and arguments that vary for each option”).

<div id="table:opt_def_clothes_washer_use" data-source="3c_ResStockInputs.tex">

| Option name | `clothes_washer_usage_multiplier` |
|:------------|:----------------------------------|
| 80% Usage   | 0.8                               |
| 100% Usage  | 1.0                               |
| 120% Usage  | 1.2                               |

Clothes Washer Usage Level options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Clothes Washer Usage Level characteristic”.

<div id="table:hc_arg_def_clothes_washer_usage_level" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `clothes_washer_usage_multiplier` | false |  | Double | auto | Multiplier on the clothes washer energy and hot water usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Clothes Washer Usage Level characteristic

</div>

#### Distribution Assumption(s)

- Engineering judgment.

## Clothes Dryer

### Modeling Approach

A clothes dryer is an in-unit residential appliance for drying clothes. Clothes dryers impact energy through the direct use of running the appliance. Clothes dryers in shared spaces and common areas of multifamily buildings are not currently captured in ResStock. Vented clothes dryers will result in increased infiltration to the conditioned space during dryer operation.

ResStock models clothes dryers with different heating fuels (Natural Gas, Electric, and Propane). Uses the *CombinedEnergyFactor* in OpenStudio-HPXML to specify the performance of each fuel.

The schedule of the clothes dryer usage is based on the American Time Use Survey data. The clothes dryer is scheduled to start immediately after the clothes washer ends its cycle. The duration of the clothes dryer is based on distributions from RBSA ((Northwest Energy Efficiency Alliance 2024)). See Section “Schedule Creation” for details on schedule generation.

ResStock provides distributions for what housing units have a clothes dryer, the fuel of the dryer, and clothes dryer energy multiplier in the “Clothes Dryer” and “Clothes Dryer Usage Level” characteristics.

### Clothes Dryer

#### Description

The presence, rated efficiency, and fuel type of the clothes dryer in a housing unit.

#### Distribution Data Source(s)

Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Clothes Washer Presence

- Federal Poverty Level

- Geometry Building Type RECS

- Heating Fuel

- State

- Tenure.

#### Options

The ResStock baseline includes three dryer options: an electric dryer, a natural gas dryer, and a propane dryer. There is also a “None” option. Certain arguments are common across all three dryer options: auto for `clothes_dryer_location`, CombinedEnergyFactor for `clothes_dryer_efficiency_type`, and auto for `clothes_dryer_vented_flow_rate`. The arguments that differ across options are shown in Table “Clothes Dryer options and arguments that vary for each option”.

<div id="table:opt_def_clothes dryer" data-source="3c_ResStockInputs.tex">

| Option name | `clothes_dryer_present` | `clothes_dryer_fuel_type` | `clothes_dryer_efficiency` |
|:---|:---|:---|:---|
| Electric | true | electricity | 2.70 |
| Gas | true | natural gas | 2.39 |
| None | false | natural gas | 2.70 |
| Propane | true | propane | 2.39 |

Clothes Dryer options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Clothes Dryer characteristic”. See the OpenStudio-HPXML [Clothes Dryer](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-clothes-dryer) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_clothes_dryer" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `clothes_dryer_present` | true |  | Boolean | true, false | Whether there is a clothes dryer present. |
| `clothes_dryer_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, garage, other housing unit, other heated space, other multifamily buffer space, other non-freezing space | The space type for the clothes dryer location. |
| `clothes_dryer_fuel_type` | true |  | Choice | electricity, natural gas, fuel oil, propane, wood, coal | Type of fuel used by the clothes dryer. |
| `clothes_dryer_efficiency_type` | true |  | Choice | EnergyFactor, CombinedEnergyFactor | The efficiency type of the clothes dryer. |
| `clothes_dryer_efficiency` | false | lb/kWh | Double | auto | The efficiency of the clothes dryer. |
| `clothes_dryer_vented_flow_rate` | false | CFM | Double | auto | The exhaust flow rate of the vented clothes dryer. |

The ResStock argument definitions set in the Clothes Dryer characteristic

</div>

#### Distribution Assumption(s)

Clothes dryer option is “None” if the clothes washer is not present.

Due to the low sample count, the input file is constructed by downscaling a housing unit sub-input file with a household sub-input file. The sub-input files have the following dependencies: housing unit sub-input file: dependencies = Geometry Building Type RECS, State, Heating Fuel, and Clothes Washer Presence, with the following fallback coarsening order:

1.  State coarsened to Census Division RECS without AK, HI

2.  Heating Fuel coarsened to Other Fuel, Wood and Propane combined

3.  Heating Fuel coarsened to Fuel Oil, Other Fuel, Wood and Propane combined

4.  Geometry Building Type RECS coarsened to SF/MF/MH

5.  Geometry Building Type RECS coarsened to SF and MH/MF

6.  State coarsened to Census Division RECS

7.  State coarsened to Census Region

8.  State coarsened to National.

Household sub-input file: dependencies = Geometry Building Type RECS, Tenure, and Federal Poverty Level, with the following fallback coarsening order:

1.  State coarsened to Census Division RECS without AK, HI

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  State coarsened to Census Division RECS

7.  State coarsened to Census Region

8.  State coarsened to National.

In combining the housing unit sub-input file and household sub-input file, the conditional relationships are ignored across Heating Fuel and Clothes Washer Presence, as well as across Tenure and Federal Poverty Level.

### Clothes Dryer Usage Level

#### Description

Clothes dryer energy usage level multiplier.

#### Distribution Data Source(s)

Not applicable—direct mapping of usage level (Section “Usage”).

#### Direct Conditional Dependencies

- Usage Level.

#### Options

The clothes dryer usage level is set based on the usage level (Section “Usage”) characteristic. It is 80% Usage when the usage level is Low, 100% Usage when the usage level is Medium, and 120% Usage when the usage level is High. The characteristic assigns the `clothes_dryer_usage_multiplier` ResStock argument (Table “Clothes Dryer Usage Level options and arguments that vary for each option”).

<div id="table:hc_opt_clothes_dryer" data-source="3c_ResStockInputs.tex">

| Option name | `clothes_dryer_usage_multiplier` |
|:------------|:---------------------------------|
| 80% Usage   | 0.8                              |
| 100% Usage  | 1.0                              |
| 120% Usage  | 1.2                              |

Clothes Dryer Usage Level options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Clothes Dryer Usage Level characteristic”. See the [OpenStudio-HPXML Refrigerators](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-refrigerators) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_clothes_dryer_usage_level" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `clothes_dryer_usage_multiplier` | false |  | Double | auto | Multiplier on the clothes dryer energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Clothes Dryer Usage Level characteristic

</div>

#### Distribution Assumption(s)

None.

## Ceiling Fan

### Modeling Approach

ResStock models all ceiling fan options as a single fan operating at medium speed periodically throughout the year. The efficiency of the fans is specified at this speed and used to calculate the annual ceiling fan energy per the Energy Rating Rated Home in ANSI/RESNET/ICC 301-2019 ((International Code Council 2019)). The annual energy is multiplied with a stochastically generated detailed schedule to produce the ceiling fan end-use load profile. The ceiling fan schedule is created as a submetered reference schedule from RBSAM prorated by a separate occupancy schedule based on ATUS. See Section “Schedule Creation” for details on schedule generation. In the characteristic distribution, while ResStock distinguishes between the options “None” (no ceiling fan) and “Standard Efficiency, No Usage,” both options lead to zero energy consumption.

Ceiling fans are characterized in a single housing characteristic. The distribution, data sources, assumptions, and argument assignment are discussed in the next subsection.

### Ceiling Fan

#### Description

Presence and efficiency of ceiling fans.

#### Distribution Data Source(s)

Building America House Simulation Protocols ((Wilson et al. 2014)); national average used as saturation.

#### Direct Conditional Dependencies

- Vacancy Status.

#### Options

ResStock has three options for the ceiling fan characteristic: a standard efficiency ceiling fan, a standard efficiency ceiling fan that is not used, and “None.” For the standard efficiency ceiling fan that is not used, as well as the “None” option, the `ceiling_fan_present` argument is set to false and the `ceiling_fan_quantity` is set to 0. The `ceiling_fan_cooling_setpoint_offset` argument is 0 for all options. The remaining arguments set by ResStock are shown in Table “Ceiling Fan options and arguments that vary for each option”.

<div id="table:opt_def_ceiling_fans" data-source="3c_ResStockInputs.tex">

| Option name | `ceiling_fan_label_energy_use` | `ceiling_fan_efficiency` |
|:---|:---|:---|
| None | 0 | 0 |
| Standard Efficiency | auto | 70.4 |
| Standard Efficiency, No usage | auto | 0 |

Ceiling Fan options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Ceiling Fan characteristic”. See the OpenStudio-HPXML [Ceiling Fans](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-ceiling-fans) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ceiling_fans" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `ceiling_fan_present` | true |  | Boolean | true, false | Whether there are any ceiling fans. |
| `ceiling_fan_label_energy_use` | false | W | Double | auto | The label average energy use of the ceiling fan(s). If neither Efficiency nor Label Energy Use provided, the OS-HPXML default (see [HPXML Ceiling Fans](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-ceiling-fans)) is used. |
| `ceiling_fan_efficiency` | false | CFM/W | Double | auto | The efficiency rating of the ceiling fan(s) at medium speed. Only used if Label Energy Use not provided. If neither Efficiency nor Label Energy Use provided, the OS-HPXML default (see [HPXML Ceiling Fans](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-ceiling-fans)) is used. |
| `ceiling_fan_quantity` | false | \# | Integer | auto | Total number of ceiling fans. |
| `ceiling_fan_cooling_setpoint_temp_offset` | false | deg-F | Double | auto | The cooling setpoint temperature offset during months when the ceiling fans are operating. Only applies if ceiling fan quantity is greater than zero. |

The ResStock argument definitions set in the Ceiling Fan characteristic

</div>

#### Distribution Assumption(s)

If the unit is vacant, there is no ceiling fan energy.

## Pool and Hot Tub

### Modeling Approach

ResStock models pools and hot tubs/spas that are connected to the home’s electric panel (i.e., not community/building pools). The saturation of pool, pool pump, pool heater, and hot tub/spa come from RECS 2020. The hot tub/spa pump is not modeled in ResStock. As pools in multifamily buildings are often for common use, the presence of pools are excluded from multifamily building types. All pools are assumed to have a pool pump. Hot tubs can be standalone or integrated as a bathroom fixture and therefore exist in all building types for units with hot tubs. The modeling of pool heaters, pool pumps, and hot tub/spa heaters in ResStock mostly relies on default OpenStudio-HPXML assumptions. Their annual energy is estimated using a reference calculation based on conditioned floor area and number of bedrooms, adjusted for occupants, using an equation from Hendron and Engebrecht (2010), and can be adjusted by a usage multiplier. The annual energy is then multiplied by a default simple schedule to produce the end-use load profile.

In OpenStudio-HPXML, pool and hot tub/spa heater options are electric resistance, gas-fired, and heat pump. Therefore, heaters for pools or spas using “Other Fuel” do not have any modeled energy consumption. Heat pump heaters are assumed to be five times more efficient than electric resistance. The use of pool cover or heating setpoint is approximated using a usage multiplier.

The building stock characterization distributions, data sources, assumptions, and argument assignment of pools and hot tubs are discussed in the next subsections.

### Misc Pool

#### Description

The presence of a pool.

#### Distribution Data Source(s)

Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- State

- Tenure

- Vintage.

#### Options

The options for the Misc Pool characteristic are “Has Pool” and “None.” The characteristic assigns the `pool_present` ResStock argument (Table “Misc Pool options and arguments that vary for each option”).

<div id="table:opt_def_pool" data-source="3c_ResStockInputs.tex">

| Option name | `pool_present` |     |
|:------------|:---------------|:----|
| Has Pool    | true           |     |
| None        | false          |     |

Misc Pool options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Misc Pool characteristic”. See the OpenStudio-HPXML [Pools](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-pools) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_pool" data-source="3c_ResStockInputs.tex">

| Name           | Required | Units | Type    | Choices     | Description              |
|:---------------|:---------|:------|:--------|:------------|:-------------------------|
| `pool_present` | true     |       | Boolean | true, false | Whether there is a pool. |

The ResStock argument definitions set in the Misc Pool characteristic

</div>

#### Distribution Assumption(s)

The only valid option for multifamily homes is None, because the pool is most likely to be part of the common load and not associated with a specific unit.

Due to the low sample count, the input file is constructed with the following fallback coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  Vintage coarsened to every 20 years before 2000 and every 10 years subsequently

7.  Vintage homes built before 1960 coarsened to pre-1960

8.  Vintage homes built after 2000 coarsened to 2000-20

9.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

10. Census Division RECS to Census Region

11. Census Region to National.

### Misc Pool Heater

#### Description

The heating fuel of the pool heater if there is a pool.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

- Constructed using the California Energy Commission 2019 Residential Appliance Saturation Study (RASS) microdata

#### Direct Conditional Dependencies

- Heating Fuel

- Misc Pool.

#### Options

There are five options for pool heaters: Electricity, Electric Heat Pump, Natural Gas, None, and Other Fuel. The Electricity option defines a traditional electric resistance pool heater, whereas the Electric Heat Pump option uses heat pump technology for heating the pool. The “Other Fuel” pool heater option currently is currently not modeled in ResStock. The ResStock arguments assigned for each of these options is given in Table “Pool Heater options and arguments that vary for each option”.

<div id="table:opt_def_pool_heat" data-source="3c_ResStockInputs.tex">

| Option name | `pool_heater_type` | `pool_heater_annual_kwh` | `pool_heater_annual_therm` | `pool_heater_usage_multiplier` |
|:---|:---|:---|:---|:---|
| Electric Heat Pump | heat pump | auto | 0 | 1.0 |
| Electricity | electric resistance | auto | 0 | 1.0 |
| Electric Heat Pump | heat pump | auto | 0 | 1.0 |
| Natural Gas | gas fired | 0 | auto | 1.0 |
| None | none | 0 | 0 | 0 |
| Other Fuel | none | 0 | 0 | 0 |

Pool Heater options and arguments that vary for each option

</div>

The “Other Fuel” option is assigned the same arguments as “None,” and will result in no energy consumption.

For the argument definitions, see Table “The ResStock argument definitions set in the Pool Heater characteristic”. See the OpenStudio-HPXML [Pool Heater](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#pool-heater) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_pool_heat" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `pool_heater_type` | true |  | Choice | none, electric resistance, gas fired, heat pump | The type of pool heater. Use 'none' if there is no pool heater. |
| `pool_heater_annual_kwh` | false | kWh/yr | Double | auto | The annual energy consumption of the electric resistance pool heater. |
| `pool_heater_annual_therm` | false | therm/yr | Double | auto | The annual energy consumption of the gas fired pool heater. |
| `pool_heater_usage_multiplier` | false |  | Double | auto | Multiplier on the pool heater energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Pool Heater characteristic

</div>

#### Distribution Assumption(s)

- Within electric pool heaters, proportion of heat pump electric pool heating vs. non-heat pump electric pool heating was derived from RASS 2019.

### Misc Pool Pump

#### Description

Presence and size of pool pump.

#### Distribution Data Source(s)

Building America House Simulation Protocols ((Wilson et al. 2014)); national average fraction used for saturation.

#### Direct Conditional Dependencies

- Misc Pool.

#### Options

The options for Misc Pool Pump are None and 1.0 horsepower (HP) Pump. If there is a pool, then the 1.0 HP Pump option is assigned. The characteristic assigns the `pool_pump_annual_kwh` and `pool_pump_usage_multiplier` ResStock arguments, Table “Misc Pool Pump options and arguments that vary for each option”.

<div id="table:opt_def_pool_pump" data-source="3c_ResStockInputs.tex">

| Option name | `pool_pump_annual_kwh` | `pool_pump_usage_multiplier` |     |
|:------------|:-----------------------|:-----------------------------|:----|
| None        | 0                      | 0                            |     |
| 1.0 HP Pump | auto                   | 1.0                          |     |

Misc Pool Pump options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Misc Pool Pump characteristic”. See the OpenStudio-HPXML [ Pool Pump](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#pool-pump) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_pool_pump" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `pool_pump_annual_kwh` | false | kWh/yr | Double | auto | The annual energy consumption of the pool pump. |
| `pool_pump_usage_multiplier` | false |  | Double | auto | Multiplier on the pool pump energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Misc Pool Pump characteristic

</div>

#### Distribution Assumption(s)

None

### Misc Hot Tub Spa

#### Description

The presence and heating fuel of a hot tub/spa at the housing unit.

#### Distribution Data Source(s)

Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- Heating Fuel

- State

- Tenure.

#### Options

The options for the Misc Hot tub Spa characteristic are the heating fuel of the hot tub heater: Electricity, Natural gas, and Other Fuel. The None option is used when the housing unit does not have a hot tub. The characteristic assigns the `permanent_spa_present` `permanent_spa_heater_type`, `permanent_spa_pump_usage_multiplier`, `permanent_spa_heater_usage_multiplier`, `permanent_spa_pump_annual_kwh`, `permanent_spa_heater_annual_kwh`, and `permanent_spa_heater_annual_therm` ResStock arguments. The following arguments are set for the options:

- `permanent_spa_pump_usage_multiplier` is 1.0 for "Electricity" and "Natural Gas" and 0 for everything else.

- `permanent_spa_heater_usage_multiplier` is 1.0 for "Electricity" and "Natural Gas" and 0 for everything else.

- `permanent_spa_pump_annual_kwh` is auto for "Electricity" and "Natural Gas" and 0 for everything else.

- `permanent_spa_heater_annual_kwh` is auto for "Electricity" and 0 for everything else.

- `permanent_spa_heater_annual_therm` is auto for "Natural Gas" and 0 for everything else.

As shown, the “Other Fuel” option is assigned the same arguments as “None,” and will result in no energy consumption. The other arguments that vary across the arguments are in Table “Misc Hot Tub Spa options and arguments that vary for each option”.

<div id="table:opt_def_hot_tub" data-source="3c_ResStockInputs.tex">

| Option name | `permanent_spa_present` | `permanent_spa_heater_type` |
|:------------|:------------------------|:----------------------------|
| Electricity | true                    | electric resistance         |
| Natural Gas | true                    | gas fired                   |
| None        | false                   | none                        |
| Other Fuel  | false                   | none                        |

Misc Hot Tub Spa options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Misc Hot Tub Spa characteristic”. See the OpenStudio-HPXML [Permanent Spas](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-permanent-spas) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hot_tub" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `permanent_spa_present` | true |  | Boolean | true, false | Whether there is a permanent spa. |
| `permanent_spa_pump_annual_kwh` | false | kWh/yr | Double | auto | The annual energy consumption of the permanent spa pump. If not provided, the OS-HPXML default (see [Permanent Spa Pump](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#permanent-spa-pump)) is used. |
| `permanent_spa_pump_usage_multiplier` | false |  | Double | auto | Multiplier on the permanent spa pump energy usage that can reflect, e.g., high/low usage occupants. |
| `permanent_spa_heater_type` | true |  | Choice | none, electric resistance, gas fired, heat pump | The type of permanent spa heater. Use 'none' if there is no permanent spa heater. |
| `permanent_spa_heater_annual_kwh` | false | kWh/yr | Double | auto | The annual energy consumption of the electric resistance permanent spa heater. |
| `permanent_spa_heater_annual_therm` | false | therm/yr | Double | auto | The annual energy consumption of the gas fired permanent spa heater. |
| `permanent_spa_heater_usage_multiplier` | false |  | Double | auto | Multiplier on the permanent spa heater energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Misc Hot Tub Spa characteristic

</div>

#### Distribution Assumption(s)

Due to the low sample count, the input file is constructed by downscaling a housing unit sub-input file with a household sub-input file. The sub-input files have the following dependencies:

housing unit sub-input file dependencies = Geometry Building Type RECS, State, and Heating Fuel, with the following fallback coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Heating Fuel coarsened to Other Fuel, Wood and Propane combined

3.  Heating Fuel coarsened to Fuel Oil, Other Fuel, Wood and Propane combined

4.  Geometry Building Type RECS coarsened to SF/MF/MH

5.  Geometry Building Type RECS coarsened to SF and MH/MF

6.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

7.  Census Division RECS to Census Region

8.  Census Region to National.

Household sub-input file: dependencies = Geometry Building Type RECS, State, Tenure, and Federal Poverty Level, with the following fallback coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

7.  Census Division RECS to Census Region

8.  Census Region to National.

In combining the housing unit sub-input file and household sub-input file, the conditional relationships are ignored across Heating Fuel, as well as across Tenure and Federal Poverty Level.

## Well Pump

### Modeling Approach

Well pumps are used to extract potable water from a well. The 2017-2019 American Housing Surveys ((U.S. Census 2022)) estimated that 11% of US homes have a well pump, and that data is used to construct the characteristic distribution, which has a dependency to Census Division, PUMA Metro Status, and Geometry Building Type Height. Well pumps are also more common outside the metro areas than in metro areas, particularly within a principal city. A well pump in ResStock is modeled as a type of plug load that does not provide any latent or sensible heat to the housing units. The annual energy for well pumping is estimated based on conditioned floor area and number of bedrooms converted from occupants using an equation from 2014 Building America House Simulation Protocols (BAHSP) ((Wilson et al. 2014)) and can be adjusted by a usage multiplier. The annual energy is then multiplied by a default simple schedule to produce the end-use load profile.

### Misc Well Pump

#### Description

Presence of well pump according to the use of well for domestic water source.

#### Distribution Data Source(s)

- 2017 and 2019 American Housing Survey (AHS) microdata.

- Core Based Statistical Area (CBSA) data based on the Feb 2013 CBSA delineation file.

#### Direct Conditional Dependencies

- Census Division

- PUMA Metro Status

- Geometry Building Type Height

#### Options

The options for the Misc Well Pump characteristic are Typical Efficiency if there is a well pump and None if there is no well pump. The characteristic sets the `misc_plug_loads_well_pump_present`, `misc_plug_loads_well_pump_usage_multiplier`, `misc_plug_loads_well_pump_2_usage_multiplier`, and `misc_plug_loads_well_pump_annual_kwh` ResStock arguments (Table “Misc Well Pump options and arguments that vary for each option”).

The `misc_plug_loads_well_pump_usage_multiplier` argument is 1.0 for “Typical Efficiency” and 0 for “None.” The `misc_plug_loads_well_pump_2_usage_multiplier` argument is 1.0 for “Typical Efficiency” and 0 for “None.”

<div id="table:hc_opt_def_well_pump" data-source="3c_ResStockInputs.tex">

| Option name | `misc_plug_loads_well_pump_present` | `misc_plug_loads_well_pump_annual_kwh` |
|:---|:---|:---|
| Typical Efficiency | true | auto |
| None | false | 0 |

Misc Well Pump options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Misc Well Pump characteristic”. See the OpenStudio-HPXML [Misc Loads](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-misc-loads) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_well_pump" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `misc_plug_loads_well_pump_present` | true |  | Boolean | true, false | Whether there is a well pump. |
| `misc_plug_loads_well_pump_annual_kwh` | false | kWh/yr | Double | auto | The annual energy consumption of the well pump plug loads. |
| `misc_plug_loads_well_pump_usage_multiplier` | false |  | Double | auto | Multiplier on the well pump energy usage that can reflect, e.g., high/low usage occupants. |
| `misc_plug_loads_well_pump_2_usage_multiplier` | true |  | Double |  | Additional multiplier on the well pump energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Misc Well Pump characteristic

</div>

#### Distribution Assumption(s)

- All well pumps are assumed to have typical efficiency.

- Where the number of samples \< 10, the Census Division is aggregated up to Census Region.

- AHS has data for buildings up to 7 stories tall. Buildings with 8 or more stories are assumed not to have a well pump.

## Miscellaneous Gas Uses

### Modeling Approach

ResStock models miscellaneous gas loads including fireplaces, grills, and lighting. ResStock randomly assigns these gas appliances to housing units based on saturation estimated by Wilson et al. (2014). Gas grill and gas lighting are assumed to be outdoor and therefore do not generate internal gains for the housing unit. For each gas appliance, the annual energy is estimated based on conditioned floor area and number of bedrooms converted from occupants using an equation from Hendron and Engebrecht (2010) and can be adjusted by a usage multiplier. The annual energy is then multiplied by a default simple schedule to produce the end-use load profile. The gas lighting characteristic distribution is in Section “Miscellaneous Gas Lighting”.

### Misc Gas Fireplace

#### Description

Presence of a gas fireplace.

#### Distribution Data Source(s)

Building America House Simulation Protocols ((Wilson et al. 2014)); national average fraction used for saturation.

#### Direct Conditional Dependencies

None.

#### Options

The options for the Misc Gas Fireplace characteristic are either “Gas Fireplace” if the housing unit has a gas fireplace or “None” if there is no gas fireplace in the unit. The characteristic assigns the `misc_fuel_loads_fireplace_present`, `misc_fuel_loads_fireplace_frac_sensible`, `misc_fuel_loads_fireplace_frac_latent`, `misc_fuel_loads_fireplace_annual_therm`, and `misc_fuel_loads_fireplace_usage_multiplier` ResStock arguments (Table “Misc Gas Fireplace options and arguments that vary for each option”).

The `misc_fuel_loads_fireplace_fuel_type` argument is set to natural gas. The `misc_fuel_loads_fireplace_frac_sensible` and `misc_fuel_loads_fireplace_frac_latent` arguments are set to auto.

<div id="table:hc_opt_def_gas_fireplace" data-source="3c_ResStockInputs.tex">

| Option name | `misc_fuel_loads_fireplace_present` | `misc_fuel_loads_fireplace_annual_therm` | `misc_fuel_loads_fireplace_usage_multiplier` |
|:---|:---|:---|:---|
| Gas Fireplace | true | auto | 1.0 |
| None | false | 0 | 0 |

Misc Gas Fireplace options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Misc Gas Fireplace characteristic”. See the OpenStudio-HPXML [Fireplace](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hvac-heating-fireplaces) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_gas_fireplace" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `misc_fuel_loads_fireplace_present` | true |  | Boolean | true, false | Whether there is fuel loads fireplace. |
| `misc_fuel_loads_fireplace_fuel_type` | true |  | Choice | natural gas, fuel oil, propane, wood, wood pellets | The fuel type of the fuel loads fireplace. |
| `misc_fuel_loads_fireplace_annual_therm` | false | therm/yr | Double | auto | The annual energy consumption of the fuel loads fireplace. |
| `misc_fuel_loads_fireplace_frac_sensible` | false | Frac | Double | auto | Fraction of fireplace residual fuel loads’ internal gains that are sensible. If not provided, the OS-HPXML default (see [HPXML Fuel Loads](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-fuel-loads)) is used. |
| `misc_fuel_loads_fireplace_frac_latent` | false | Frac | Double | auto | Fraction of fireplace residual fuel loads’ internal gains that are latent. |
| `misc_fuel_loads_fireplace_usage_multiplier` | false |  | Double | auto | Multiplier on the fuel loads fireplace energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Misc Gas Fireplace characteristic

</div>

#### Distribution Assumption(s)

None.

### Misc Gas Grill

#### Description

Presence of a gas grill.

#### Distribution Data Source(s)

Building America House Simulation Protocols ((Wilson et al. 2014)); national average fraction used for saturation.

#### Direct Conditional Dependencies

None.

#### Options

The options for Misc Gas Grill are “Gas Grill” if the housing unit has a gas grill or “None” if the housing unit does not have a gas grill. The characteristic sets the `misc_fuel_loads_grill_present`, `misc_fuel_loads_grill_fuel_type`, `misc_fuel_loads_grill_annual_therm`, and `misc_fuel_loads_grill_usage_multiplier` ResStock arguments (Table “Misc Gas Grill options and arguments that vary for each option”). The `misc_fuel_loads_grill_fuel_type` is always set to natural gas.

<div id="table:hc_opt_def_gas_grill" data-source="3c_ResStockInputs.tex">

| Option name | `misc_fuel_loads_grill_present` | `misc_fuel_loads_grill_annual_therm` | `misc_fuel_loads_grill_usage_multiplier` |  |
|:---|:---|:---|:---|:---|
| Gas Grill | true | auto | 1.0 |  |
| None | false | 0 | 0 |  |

Misc Gas Grill options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Misc Gas Grill characteristic”. See the OpenStudio-HPXML [Fuel Loads](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-fuel-loads) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_gas_grill" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `misc_fuel_loads_grill_present` | true |  | Boolean | true, false | Whether there is a fuel loads grill. |
| `misc_fuel_loads_grill_fuel_type` | true |  | Choice | natural gas, fuel oil, propane, wood, wood pellets | The fuel type of the fuel loads grill. |
| `misc_fuel_loads_grill_annual_therm` | false | therm/yr | Double | auto | The annual energy consumption of the fuel loads grill. |
| `misc_fuel_loads_grill_usage_multiplier` | false |  | Double | auto | Multiplier on the fuel loads grill energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Misc Gas Grill characteristic

</div>

#### Distribution Assumption(s)

None.

## PV

### Modeling Approach

ResStock models residential photovoltaic (PV) solar panels based on data from Lawrence Berkeley National Laboratory’s (LBNL) 2020 Tracking the Sun report ((Barbose and Darghouth 2019)) and a 2020 PV report by Wood Mackenzie ((Woods Mackenzie 2020)). However, the data excludes Alaska and Hawaii, the latter of which has one of the largest number of solar installations by state. Therefore, the PV penetration in Hawaii is added based on 2023’s [EIA form 861](https://www.eia.gov/electricity/data/eia861/). ResStock only models rooftop solar for occupied single-family detached homes. This means ResStock does not model ground-mounted solar or solar installed in other building types, such as community solar shared among multifamily units, although that modeling capability exists in OpenStudio-HPXML. This also means ResStock, which estimates the rooftop solar penetration at less than 1% of all housing units, is most likely underestimating the total installed capacity nationally. In addition to the presence of rooftop solar (Section “Has PV”), ResStock also characterizes the orientation (Section “PV Orientation”) and system capacity (Section “PV System Size”), using LBNL’s 2020 Tracking the Sun report. The system size or modeled capacity does not necessarily align with the available roof space of the housing units.

The PV modeling capability and default inputs are primarily adopted from NREL’s [PVWatts model](https://pvwatts.nrel.gov/index.php). ResStock calculates the energy production based on the solar irradiation information in the weather file and the characteristics of the PV array. In the ResStock baseline, all PV systems are modeled as roof-mounted, fixed-axis standard modules tilted at roof pitch with a 14% overall derate factor and a 96% inverter efficiency. The derate factor encompasses loss from soiling, shading, wiring, mismatch, degradation, and more according to the PVWatts documentation ((Dobos 2014)).

### Has PV

#### Description

Presence of a rooftop photovoltaic system.

#### Distribution Data Source(s)

Constructed using ACS population and data from [dGen](https://www.nrel.gov/analysis/dgen/) on PV installation that combines LBNL’s 2020 Tracking the Sun ((Barbose and Darghouth 2019)) and Wood Mackenzie’s 2020 Q4 PV report ((Woods Mackenzie 2020); prepared on Jun 22, 2021). The PV penetration in Hawaii is from [EIA form 861](https://www.eia.gov/electricity/data/eia861/).

#### Direct Conditional Dependencies

- County

- Geometry Building Type RECS

- Vacancy Status.

#### Options

The options for Has PV are “Yes” if the housing unit has a rooftop PV system and “No” if the housing unit does not have a rooftop PV system.

#### Distribution Assumption(s)

Imposed an upper bound of 14 kWDC, which contains 95% of all installations. Counties with source_count \<10 are backfilled with aggregates at the state level. Distribution based on all installations is applied only to occupied single-family detached homes; actual distribution for single-family detached homes may be higher. PV is not modeled in AK. No data have been identified.

For Hawaii, EIA Form 861 reports the number of residential utility customers with rooftop PV in $`Net_Metering_2023.xlsx`$ worksheet and the total number of residnetial utility customers in $`Sales_Ult_Cust_2023.xlsx`$. Taking the ratio of these two gives us the fraction of homes with rooftop PV. We place the additional constraint that all of these rooftop PV customers are in single-family detached homes. Because Hawaii is composed of multiple islands, the four electric utilities in Hawaii (and which report to EIA Form 861) approximately align with the county boundaries with Hawaii, Honolulu, and Kauai having one county for one electric utility, and both Maui and Kalawao mapping to the same electric utility, so we we develop distinct PV saturation rates for each county in Hawaii (note Kalawao has population 81 people and is located on the island of Maui).

### PV Orientation

#### Description

The orientation of the PV system.

#### Distribution Data Source(s)

Constructed using LBNL’s 2020 Tracking the Sun report (Barbose and Darghouth 2019).

#### Direct Conditional Dependencies

- Has PV.

#### Options

The options for PV orientation are the cardinal and subcardinal directions and “None” for housing units that do not have PV systems. The characteristic sets the `pv_system_array_azimuth` and `pv_system_2_array_azimuth` arguments (Table “PV Orientation options and arguments that vary for each option”). The `pv_system_2_array_azimuth` argument is always set to 0.

<div id="table:hc_opt_def_pv_orient" data-source="3c_ResStockInputs.tex">

| Option name   | `pv_system_array_azimuth` |
|:--------------|:--------------------------|
| East          | 90                        |
| None          | 180                       |
| North         | 0                         |
| Northeast     | 45                        |
| Northwest     | 315                       |
| South         | 180                       |
| Southeast 135 |                           |
| Southwest     | 225                       |
| West          | 270                       |

PV Orientation options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the PV Orientation characteristic”. See the OpenStudio-HPXML [Photovoltaics](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-photovoltaics) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_pv_orient" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `pv_system_array_azimuth` | true | degrees | Double | Array azimuth of the PV system. Azimuth is measured clockwise from north (e.g., North=0, East=90, South=180, West=270). |
| `pv_system_2_array_azimuth` | true | degrees | Double | Array azimuth of the second PV system. Azimuth is measured clockwise from north (e.g., North=0, East=90, South=180, West=270). |

The ResStock argument definitions set in the PV Orientation characteristic

</div>

#### Distribution Assumption(s)

- PV orientation mapped based on the azimuth angle of the primary array (180° is south-facing).

- The orientation is not aligned with the roof deck’s normal directions from the Orientation characteristic (Section “Orientation”).

### PV System Size

#### Description

The size of the PV system.

#### Distribution Data Source(s)

Constructed using LBNL’s 2020 Tracking the Sun report (Barbose and Darghouth 2019).

#### Direct Conditional Dependencies

- Has PV

- State.

#### Options

The options for the PV System Size characteristic are a set of PV system sizes ranging from 1-13 kWDC. The characteristic assigns the `pv_system_present`, `pv_system_module_type`, `pv_system_location`, `pv_system_tracking`, `pv_system_array_tilt`, `pv_system_max_power_output`, `pv_system_inverter_efficiency`, `pv_system_system_losses_fraction`, `pv_system_2_present`, `pv_system_2_module_type`, `pv_system_2_location`, `pv_system_2_tracking`, `pv_system_2_array_tilt`, and `pv_system_2_max_power_output` ResStock arguments (Table “PV System Size options and arguments that vary for each option”).

The following arguments are set to auto: `pv_system_module_type`, `pv_system_tracking`, `pv_system_max_power_output`, `pv_system_inverter_efficiency`, `pv_system_system_losses_fraction`, `pv_system_2_module_type`, `pv_system_2_tracking`, and `pv_system_2_max_power_output`. The `pv_system_location` and `pv_system_2_location` are set to roof. `pv_system_array_tilt` and `pv_system_2_array_tilt` are always set to roofpitch. `pv_system_2_present` is always false. `pv_system_2_max_power_output` is always 0.

<div id="table:hc_opt_def_pv_size" data-source="3c_ResStockInputs.tex">

| Option name | `pv_system_present` | `pv_system_max_power_output` |
|:------------|:--------------------|:-----------------------------|
| 1.0 kWDC    | true                | 100                          |
| 3.0 kWDC    | true                | 3,000                        |
| 5.0 kWDC    | true                | 5,000                        |
| 7.0 kWDC    | true                | 7,000                        |
| 9.0 kWDC    | true                | 9,000                        |
| 11.0 kWDC   | true                | 11,000                       |
| 13.0 kWDC   | true                | 13,000                       |
| None        | false               | 0                            |

PV System Size options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the PV System Size characteristic”. See the OpenStudio-HPXML [Photovoltaics](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-photovoltaics) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_pv_size" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `pv_system_present` | true |  | Boolean | true, false | Whether there is a PV system present. |
| `pv_system_module_type` | false |  | Choice | auto, standard, premium, thin film | Module type of the PV system. |
| `pv_system_location` | false |  | Choice | auto, roof, ground | Location of the PV system. |
| `pv_system_tracking` | false |  | Choice | auto, fixed, 1-axis, 1-axis backtracked, 2-axis | Type of tracking for the PV system. |
| `pv_system_array_tilt` | true | degrees | String |  | Array tilt of the PV system. Can also enter, e.g., RoofPitch, RoofPitch+20, Latitude, Latitude-15, etc. |
| `pv_system_max_power_output` | true | W | Double |  | Maximum power output of the PV system. For a shared system, this is the total building maximum power output. |
| `pv_system_inverter_efficiency` | false | Frac | Double | auto | Inverter efficiency of the PV system. If there are two PV systems, this will apply to both. |
| `pv_system_system_losses_fraction` | false | Frac | Double | auto | System losses fraction of the PV system. If there are two PV systems, this will apply to both. |
| `pv_system_2_present` | true |  | Boolean | true, false | Whether there is a second PV system present. |
| `pv_system_2_module_type` | false |  | Choice | auto, standard, premium, thin film | Module type of the second PV system. |
| `pv_system_2_location` | false |  | Choice | auto, roof, ground | Location of the second PV system. |
| `pv_system_2_tracking` | false |  | Choice | auto, fixed, 1-axis, 1-axis backtracked, 2-axis | Type of tracking for the second PV system. |
| `pv_system_2_array_tilt` | true | degrees | String |  | Array tilt of the second PV system. Can also enter, e.g., RoofPitch, RoofPitch+20, Latitude, Latitude-15, etc. |
| `pv_system_2_max_power_output` | true | W | Double |  | Maximum power output of the second PV system. For a shared system, this is the total building maximum power output. |

The ResStock argument definitions set in the PV System Size characteristic

</div>

#### Distribution Assumption(s)

Installations of unknown mount type are assumed to be rooftop. States without data are backfilled with aggregates at the Census Region. “East South Central” assumed the same distribution as “West South Central.” PV is not modeled in AK. The Option=None is set so that an error is thrown if PV is modeled as an argument.

## Additional Capabilities

This section describes the additional modeling capabilities in OpenStudio-HPXML/ResStock that are not yet fully deployed in the ResStock baseline. These include batteries and dehumidifiers. These loads at present are not available in the baseline but can be modeled as upgrade measures. This is because their characteristic distribution is not yet fully characterized but is instead set to 100% None.

### Modeling Approach

Batteries in ResStock use a standalone Lithium-ion battery model whose performance is characterized by voltage rating, power rating, installed capacity, usable capacity, round trip efficiency, and installed location. The battery can charge and discharge based on a detailed schedule input or be controlled to capture net solar production and modulate whole-home load in a home with PV.

A dehumidifier is a device used to maintain a reasonable relative humidity in the home. ResStock models a dehumidifier as a portable device located in the conditioned space of the home. Other inputs to this model include capacity, rated efficiency, and relative humidity setpoint. The dehumidifier model is not intended to handle, e.g., a wet basement or crawlspace where there is significant moisture from the ground.

### Battery

#### Description

Presence, size, location, and efficiency of an on-site battery.

#### Distribution Data Source(s)

Not applicable.

#### Direct Conditional Dependencies

Not applicable.

#### Options

Currently only the option “None” is defined in the ResStock baseline. This option is nullified by setting the `battery_present` to 0. Other options are available for use in an upgrade measure, and the argument table shows how the options can be defined (Table “The ResStock argument definitions set in the Battery characteristic”). The characteristic assigns the `battery_location`, `battery_power`, `battery_capacity`, and `battery_round_trip_efficiency` ResStock arguments.

<div id="table:hc_arg_def_battery" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
|  | true |  | Boolean | true, false | Whether there is a lithium ion battery present. |
| `battery_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, crawlspace, crawlspace—vented, crawlspace—unvented, crawlspace—conditioned, attic, attic—vented, attic—unvented, garage, outside | The space type for the lithium ion battery location. |
| `battery_power` | false | W | Double | auto | The rated power output of the lithium ion battery. |
| `battery_capacity` | false | kWh | Double | auto | The nominal capacity of the lithium ion battery. |
| `battery_usable_capacity` | false | kWh | Double | auto | The usable capacity of the lithium ion battery. |
| `battery_round_trip_efficiency` | false | Frac | Double | auto | The round trip efficiency of the lithium ion battery. |

The ResStock argument definitions set in the Battery characteristic

</div>

#### Distribution Assumption(s)

Not applicable.

### Dehumidifier

#### Description

Presence, water removal rate, and humidity setpoint of the dehumidifier.

#### Distribution Data Source(s)

Not applicable.

#### Direct Conditional Dependencies

Not applicable.

#### Options

Currently only the option “None” is defined in the ResStock baseline. This option is nullified by setting the `dehumidifier_efficiency` to 0. Other options are available for use in an upgrade measure, and the argument table shows how the options can be defined (Table “The ResStock argument definitions set in the Dehumidifier characteristic”). The characteristic sets the `dehumidifier_type`, `dehumidifier_efficiency_type`, `dehumidifier_efficiency`, `dehumidifier_capacity`, `dehumidifier_rh_setpoint`, and `dehumidifier_fraction_dehumidification_load_served` ResStock arguments.

<div id="table:hc_arg_def_dehumid" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `dehumidifier_type` | true |  | Choice | none, portable, whole-home | The type of dehumidifier. |
| `dehumidifier_efficiency_type` | true |  | Choice | Energy Factor, IntegratedEnergyFactor | The efficiency type of dehumidifier. |
| `dehumidifier_efficiency` | true | L/kWh | Double |  | The efficiency of the dehumidifier. |
| `dehumidifier_capacity` | true | pint/day | Double |  | The capacity (water removal rate) of the dehumidifier. |
| `dehumidifier_rh_setpoint` | true | Frac | Double |  | The relative humidity setpoint of the dehumidifier. |
| `dehumidifier_fraction_dehumidification_load_served` | true | Frac | Double |  | The dehumidification load served fraction of the dehumidifier. |

The ResStock argument definitions set in the Dehumidifier characteristic

</div>

#### Distribution Assumption(s)

Not applicable

# Lighting

Lighting in ResStock covers interior lighting within the housing unit, and for single-family homes, attached garage and exterior lighting that is metered at the home. Multifamily common space, parking garage, and exterior lighting are excluded from ResStock.

## Modeling Approach

Five ResStock input files provide the options and arguments for lighting, but only two are currently in use:

- Lighting—Electric lighting: interior, exterior, and garage

- Misc Gas Lighting—Exterior natural gas lighting

- Holiday Lighting—Not used

- Lighting Interior Use—Not used

- Lighting Other Use—Not used.

ResStock models three lighting technologies: light-emitting diodes (LEDs), incandescent bulbs, and compact florescent (CFL) bulbs. The technologies are represented as a fraction of the number of light bulbs in the home covered by each technology.

Separately, outside these input files, ResStock provides schedules for lighting based on the occupancy schedule generator (Section “Schedule Creation”).

## Lighting Characteristics

### Lighting

#### Description

Specifies the type of lighting technology used in the housing unit.

#### Distribution Data Source(s)

- U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- State

- Geometry Building Type RECS.

#### Options

In ResStock there are three options available for lighting: *100% CFL*, *100% LED*, and *100% Incandescent*. The assumption in ResStock is that all lighting within a home is of the same technology, both interior and exterior. Across all three options, the argument *lighting_present = true*. Each ResStock option specifies the corresponding ResStock arguments for interior, exterior, and garage of the building. All non-specified arguments in the table below for other technologies are set to zero. In OpenStudio-HPXML, all lighting that is not specified as one of the set technologies (e.g., CFL or LED) is assumed to be incandescent, so the *100% Incandescent* option has all technology options set to 0 (i.e., there is no explicit incandescent option in OpenStudio-HPXML).

| Option name | Interior argument | Exterior argument | Garage argument |
|:---|:---|:---|:---|
| 100% CFL | *lighting_interior_fraction_cfl* = 1 | *lighting_exterior_fraction_cfl* = 1 | *lighting_garage_fraction_cfl* = 1 |
| 100% Incandescent | all arguments = 0 | all arguments = 0 | all arguments = 0 |
| 100% LED | *lighting_interior_fraction_led* = 1 | *lighting_exterior_fraction_led* = 1 | *lighting_garage_fraction_led* = 1 |

Lighting options and arguments that vary for each option

For the argument definitions, see Table “The ResStock arguments set in the Lighting characteristic”. See the OpenStudio-HPXML [Lighting](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-lighting) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_lighting" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `lighting_present` | true |  | Boolean | true, false | Whether there is lighting energy use. |
| `lighting_interior_fraction_cfl` | true | Double |  |  | Fraction of all lamps (interior) that are compact fluorescent. Lighting not specified as CFL, LFL, or LED is assumed to be incandescent. |
| `lighting_interior_fraction_lfl` | true | Double |  |  | Fraction of all lamps (interior) that are linear fluorescent. Lighting not specified as CFL, LFL, or LED is assumed to be incandescent. |
| `lighting_interior_fraction_led` | true | Double |  |  | Fraction of all lamps (interior) that are light emitting diodes. Lighting not specified as CFL, LFL, or LED is assumed to be incandescent. |
| `lighting_exterior_fraction_cfl` | true | Double |  |  | Fraction of all lamps (exterior) that are compact fluorescent. Lighting not specified as CFL, LFL, or LED is assumed to be incandescent. |
| `lighting_exterior_fraction_lfl` | true | Double |  |  | Fraction of all lamps (exterior) that are linear fluorescent. Lighting not specified as CFL, LFL, or LED is assumed to be incandescent. |
| `lighting_exterior_fraction_led` | true | Double |  |  | Fraction of all lamps (exterior) that are light emitting diodes. Lighting not specified as CFL, LFL, or LED is assumed to be incandescent. |
| `lighting_garage_fraction_cfl` | true | Double |  |  | Fraction of all lamps (garage) that are compact fluorescent. Lighting not specified as CFL, LFL, or LED is assumed to be incandescent. |
| `lighting_garage_fraction_lfl` | true | Double |  |  | Fraction of all lamps (garage) that are linear fluorescent. Lighting not specified as CFL, LFL, or LED is assumed to be incandescent. |
| `lighting_garage_fraction_led` | true | Double |  |  | Fraction of all lamps (garage) that are light emitting diodes. Lighting not specified as CFL, LFL, or LED is assumed to be incandescent. |

The ResStock arguments set in the Lighting characteristic

</div>

#### Distribution Assumption(s)

- Qualitative lamp type fractions in each household surveyed are distributed to three options representing 100% incandescent, 100% CFl, and 100% LED lamp type options.

- Qualitative portion of inside light bulbs in 2020 RECS microdata is mapped to quantative percentage as: None: 0%; Some: 20%; About half: 50%; Most: 80%; All: 100%. Then the sum of three types of lighting options is normalized to 100%.

### Miscellaneous Gas Lighting

#### Description

Presence of exterior natural gas lighting.

#### Distribution Data Source(s)

- Building America House Simulation Protocols ((Wilson et al. 2014)); national average fraction used for saturation.

#### Direct Conditional Dependencies

None.

#### Options

ResStock has two options for Misc Gas Lighting (Table “Misc Gas Lighting options and arguments that vary for each option”): *None* or *Gas Lighting*. For both of these options, the *misc_fuel_loads_lighting_fuel_type* ResStock argument is set to *natural gas*.

<div id="table:hc_opt_def_misc_gas_light" data-source="3c_ResStockInputs.tex">

| Option name | Stock saturation | `misc_fuel_loads_lighting_present` | `misc_fuel_loads_lighting_annual_therm` | `misc_fuel_loads_lighting_usage_multiplier` |
|:---|:---|:---|:---|:---|
| Gas Lighting | 1.2% | true | auto | 1.0 |
| None | 98.8% | false | 0 | 0 |

Misc Gas Lighting options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock arguments set in the Misc Gas Lighting characteristic”. See the OpenStudio-HPXML [Misc Fuel Loads](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-fuel-loads) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_misc_gas_light" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `misc_fuel_loads_lighting_present` | true |  | Boolean | true, false | Whether there is fuel loads lighting. |
| `misc_fuel_loads_lighting_fuel_type` | true |  | Choice | natural gas, fuel oil, propane, wood, wood pellets | The fuel type of the fuel loads lighting. |
| `misc_fuel_loads_lighting_annual_therm` | false | therm/yr | Double | auto | The annual energy consumption of the fuel loads lighting. |
| `misc_fuel_loads_lighting_usage_multiplier` | false |  | Double | auto | Multiplier on the fuel loads lighting energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock arguments set in the Misc Gas Lighting characteristic

</div>

#### Distribution Assumption(s)

None.

### Holiday Lighting

#### Description

Holiday lighting presence and use. Not currently used in ResStock.

#### Distribution Data Source(s)

Not applicable.

#### Direct Conditional Dependencies

None.

#### Options

The *No Exterior Use* option is assigned to all buildings in ResStock (Table “The ResStock arguments set in the Holiday Lighting characteristic”).

<div id="table:hc_arg_def_holiday_light" data-source="3c_ResStockInputs.tex">

| Option name | `holiday_lighting_present` | `holiday_lighting_daily_kwh` | `holiday_lighting_period` |
|:---|:---|:---|:---|
| No Exterior Use | false | 0 | auto |

The ResStock arguments set in the Holiday Lighting characteristic

</div>

For the argument definitions, see Table “The ResStock arguments set in the Holiday Lighting characteristic”. See the OpenStudio-HPXML [Exterior Holiday Lighting](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#exterior-holiday-lighting) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_holiday_light" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `holiday_lighting_present` | true |  | Boolean | true, false | Whether there is holiday lighting. |
| `holiday_lighting_daily_kwh` | false | kWh/day | Double | auto | The daily energy consumption for holiday lighting (exterior). |
| `holiday_lighting_period` | false |  | String | auto | Enter a date like 'Nov 25–Jan 5'. |

The ResStock arguments set in the Holiday Lighting characteristic

</div>

#### Distribution Assumption(s)

None.

### Lighting Interior Use

#### Description

Interior lighting usage relative to the national average. Sampled for buildings, but no longer used for ResStock models. Instead, lighting use schedules are controlled by the ResStock schedule generator.

#### Distribution Data Source(s)

Not applicable.

#### Direct Conditional Dependencies

None.

#### Options

All buildings are assigned the option *100% Usage*, which sets the ResStock argument *lighting_interior_usage_multiplier* to 1 (the OpenStudio-HPXML default) (Table “The ResStock arguments set in the Lighting Interior Use characteristic”).

<div id="table:hc_arg_def_light_int_use" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `lighting_interior_usage_multiplier` | false |  | Double | auto | Multiplier on the lighting energy usage (interior) that can reflect, e.g., high/low usage occupants. |

The ResStock arguments set in the Lighting Interior Use characteristic

</div>

#### Distribution Assumption(s)

- This parameter for adding diversity to lighting usage patterns is not currently used.

### Lighting Other Use

#### Description

Exterior and garage lighting usage relative to the national average. Sampled for buildings, but no longer used for ResStock models. Instead, lighting use schedules are controlled by the ResStock schedule generator.

#### Distribution Data Source(s)

Not applicable.

#### Direct Conditional Dependencies

None.

#### Options

All buildings are assigned the option *100% Usage*, which sets the ResStock arguments *lighting_exterior_usage_multiplier* and *lighting_garage_usage_multiplier* to 1 (the OS-HPXML default).

For the argument definitions, see Table “The ResStock arguments set in the Lighting Interior Use characteristic”. See the OpenStudio-HPXML [Lighting](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-lighting) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_light_oth_use" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `lighting_exterior_usage_multiplier` | false |  | Double | auto | Multiplier on the lighting energy usage (exterior) that can reflect, e.g., high/low usage occupants. |
| `lighting_garage_usage_multiplier` | false |  | Double | auto | Multiplier on the lighting energy usage (garage) that can reflect, e.g., high/low usage occupants. |

The ResStock arguments set in the Lighting Interior Use characteristic

</div>

#### Distribution Assumption(s)

- This parameter for adding diversity to lighting usage patterns is not currently used.

# Plug Loads

In ResStock, plug loads capture electric loads in the home that are not explicitly modeled on their own. Examples of plug loads includes things like microwaves, garbage disposals, toasters, fish tanks, cell phones, televisions, and portable humidifiers. Most of these items are not modeled explicitly under the plug loads modeling in ResStock, but instead are captured through a regression equation from RECS applied to ResStock homes, with some additional variability inserted on top to mimic the real-world variation and diversity that exist within these loads. These regressions form the usage multipliers that are applied to the default OpenStudio-HPXML calculations for plug loads. Based on ANSI/RESNET/ICC 301-2019, the plug load calculation estimates TV load based on the number of bedrooms converted from occupants and other load based on conditioned floor area. Two input files control plug loads in ResStock: Plug Loads and Plug Load Diversity.

## Plug Loads

### Description

Plug load usage level as a percentage of the national average.

### Distribution Data Source(s)

- U.S. EIA 2015 RECS microdata.

### Direct Conditional Dependencies

- Census Division RECS

- Geometry Building Type RECS.

### Options

ResStock provides a range of percentages for plug load usage that are multipliers compared to national average plug load energy use (Table “The ResStock arguments set in the Plug Loads characteristic”). Several ResStock arguments are constant across all options:

- `misc_plug_loads_television_present` = true

- `misc_plug_loads_television_annual_kwh` = auto

- `misc_plug_loads_other_annual_kwh` = auto

- `misc_plug_loads_other_frac_sensible` = 0.93

- `misc_plug_loads_other_frac_latent` = 0.021.

<div id="table:hc_opt_plug_load" data-source="3c_ResStockInputs.tex">

| Option name | `misc_plug_loads_television_usage_multiplier` | `misc_plug_loads_other_usage_multiplier` |
|:---|:---|:---|
| 78% | 0.78 | 0.78 |
| 79% | 0.79 | 0.79 |
| 82% | 0.82 | 0.82 |
| 84% | 0.84 | 0.84 |
| 85% | 0.85 | 0.85 |
| 86% | 0.86 | 0.86 |
| 89% | 0.89 | 0.89 |
| 91% | 0.91 | 0.91 |
| 94% | 0.94 | 0.94 |
| 95% | 0.95 | 0.95 |
| 96% | 0.96 | 0.96 |
| 97% | 0.97 | 0.97 |
| 99% | 0.99 | 0.99 |
| 100% | 1.0 | 1.0 |
| 101% | 1.01 | 1.01 |
| 102% | 1.02 | 1.02 |
| 103% | 1.03 | 1.03 |
| 104% | 1.04 | 1.04 |
| 105% | 1.05 | 1.05 |
| 106% | 1.06 | 1.06 |
| 108% | 1.08 | 1.08 |
| 110% | 1.1 | 1.1 |
| 113% | 1.13 | 1.13 |
| 119% | 1.19 | 1.19 |
| 121% | 1.21 | 1.21 |
| 123% | 1.23 | 1.23 |
| 134% | 1.34 | 1.34 |
| 137% | 1.37 | 1.37 |
| 140% | 1.4 | 1.4 |
| 144% | 1.44 | 1.44 |
| 166% | 1.66 | 1.66 |

The ResStock arguments set in the Plug Loads characteristic

</div>

For the argument definitions, see Table “The ResStock arguments set in the Plug Loads Use characteristic”. See the OpenStudio-HPXML [Plug Loads](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-plug-loads) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_plug_load" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `misc_plug_loads_television_present` | true |  | Boolean | true, false | Whether there are televisions. |
| `misc_plug_loads_television_annual_kwh` | false | kWh/yr | Double | auto | The annual energy consumption of the television plug loads. |
| `misc_plug_loads_television_usage_multiplier` | false |  | Double | auto | Multiplier on the television energy usage that can reflect, e.g., high/low usage occupants. |
| `misc_plug_loads_other_annual_kwh` | false | kWh/yr | Double | auto | The annual energy consumption of the other residual plug loads. |
| `misc_plug_loads_other_frac_sensible` | false | Frac | Double | auto | Fraction of other residual plug loads’ internal gains that are sensible. |
| `misc_plug_loads_other_frac_latent` | false | Frac | Double | auto | Fraction of other residual plug loads’ internal gains that are latent. |
| `misc_plug_loads_other_usage_multiplier` | false |  | Double | auto | Multiplier on the other energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock arguments set in the Plug Loads Use characteristic

</div>

### Distribution Assumption(s)

- Multipliers are based on ratio of the ResStock miscellaneous electric loads (MELS) regression equations and the MELS modeled in RECS.

## Plug Load Diversity

### Description

Plug load diversity multiplier intended to add additional variation in plug load profiles across all simulations.

### Distribution Data Source(s)

- Engineering judgment, calibration.

### Direct Conditional Dependencies

- Usage Level.

### Option(s)

Three different levels of plug load diversity are added on top of the regional multipliers from the Plug Loads input file (Table “The ResStock arguments set in the Plug Loads Diversity characteristic”).

<div id="table:hc_opt_plug_load_diversity" data-source="3c_ResStockInputs.tex">

| Option name | `misc_plug_loads_television_2_usage_multiplier` | `misc_plug_loads_other_2_usage_multiplier` |
|:---|:---|:---|
| 50% | 0.5 | 0.5 |
| 100% | 1.0 | 1.0 |
| 200% | 2.0 | 2.0 |

The ResStock arguments set in the Plug Loads Diversity characteristic

</div>

For the argument definitions, see Table “The ResStock arguments set in the Plug Load Diversity Use characteristic”. See the OpenStudio-HPXML [Plug Loads](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-plug-loads) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_plug_load_diversity" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `misc_plug_loads_television_2_usage_multiplier` | true |  | Double |  | Additional multiplier on the television energy usage that can reflect, e.g., high/low usage occupants. |
| `misc_plug_loads_other_2_usage_multiplier` | true |  | Double |  | Additional multiplier on the other energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock arguments set in the Plug Load Diversity Use characteristic

</div>

### Distribution Assumption(s)

None.

# Electric Vehicles

## Modeling Approach

The electric vehicle (EV) capabilities in ResStock were largely created under a joint project to ensure consistency between model inputs and outputs for ResStock and Transportation Energy & Mobility Pathway Options Model[^5] (TEMPO), (Muratori et al. 2021). The EV model in ResStock uses an EnergyPlus battery object to simulate the charging and discharging. Since a battery is typically associated with being attached to the building and not being driven around, the energy being discharged is ignored in the energy reporting as the electric vehicle is assumed to only draw energy from the dwelling unit. No vehicle-to-building energy exhange is considered in the baseline model. ResStock specifies if a specific unit has an electric vehicle, the percent of energy provided by the home charger, the electric vehicle battery type that provides the battery capacity and efficiency, the charge rate of the EV charger, and the vehicle miles traveled per year. Units without an EV are also assigned a percent vehicle charge at home, an electric vehicle battery description, and a vehicle miles traveled so that they do not need to be sampled when applying an EV upgrade. While the charge rate is fixed in the model, the discharge rate is dynamically set using the miles traveled, vehicle efficiency, and a constant driving speed of 22 MPH ((Federal Highway Administration 2017)), which is then scaled at each timestep based on the ambient temperature using a curve derived from emprical data ((Yip et al. 2023)). Degredation of the battery over time is not considered. The schedules of charging and discharging are stochastic. The charging and discharging schedules are based on a single occupant in the dwelling unit assigned to the vehicle. Vehicle discharge events occur when the occupant leaves the unit and returns to the unit. The total duration of the discharging events is dependent on the annual vehicle miles traveled and the duration of individual events is proportional to the length of each away period. Charging is assumed to start when the occupant arrives back to the dwelling unit and the battery charges until a maximum state of charge is achived or the next trip occurs. The model draws data mainly from the TEMPO model, EIA RECS 2020 ((U.S. Energy Information Administration 2020)), the National Household Travel Survey ((Federal Highway Administration 2017, 2022)), registration data from Experian ((Experian 2023)), the No Place Like Home Study ((Ge et al. 2021)), and Autonomie model ((Argonne National Laboratory 2025)).

## Electric Vehicle Characteristics

### Electric Vehicle Ownership

#### Description

The dwelling unit owns an electric vehicle.

#### Distribution Data Source(s)

- EV Registration Data from Experian 2023.

- 2019-5yrs Public Use Microdata Samples (PUMS). IPUMS USA, University of Minnesota, www.ipums.org.

- U.S. EIA 2020 Residential Energy Consumption Survey (RECS) microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- PUMA

- Tenure

#### Options

The options for Electric Vehicle Ownership characteristic determine if other arguments for the EV are used. The characteristic sets the `vehicle_type` ResStock argument. The argument definition is found in Table “The ResStock argument definitions set in the Electric Vehicle Ownership characteristic”.

<div id="table:hc_arg_def_ev_ownership" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `vehicle_type` | false |  | String |  | The type of vehicle present at the home. |

The ResStock argument definitions set in the Electric Vehicle Ownership characteristic

</div>

The options and their ResStock arguments values can be found in Table “Electric Vehicle Ownership options and arguments that vary for each option”. The Void option is used for impossible dependency conditions and is not sampled.

<div id="table:hc_opt_ev_ownership" data-source="3c_ResStockInputs.tex">

| Option name | `vehicle_type`         |
|:------------|:-----------------------|
| No          |                        |
| Void        |                        |
| Yes         | BatteryElectricVehicle |

Electric Vehicle Ownership options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

- Due to low sample sizes, coarsening rules applied in the following order.

  1.  Federal Poverty Level lumped every 100%

  2.  Federal Poverty Level lumped every 200%

  3.  Building type is consolidated into three bins 1) single-family, 2) multi-family, and 3) mobile home

  4.  Building type is consolidated into two bins 1) single-family and 2) multi-family and mobile home

- PUMA level battery EV saturation is calculated using a weighted average of the County level Experian data and ResStock unit counts for each County and PUMA.

- The RECS 2020 satuations for each segment in a given PUMA are scaled to match the Experian PUMA weighted averaged battery EV saturation using the segment unit counts from PUMS 2019-5yrs survey.

### Electric Vehicle Battery

#### Description

The type of electric vehicle and battery range in miles.

#### Distribution Data Source(s)

- The 2023 Vehicle Stock Projection Data from NREL’s TEMPO model

- EV Registration Data from Experian 2023

#### Direct Conditional Dependencies

No direct conditional dependencies.

#### Options

The options for Electric Vehicle Battery characteristic is a set of electric vehicle types and battery range in miles. These options do not specifiy if the unit has a vehicle, but rather the preference of the vehicle type and battery range if the household owned an electric vehicle. Every unit is assigned one of these options so that the vehicle type and battery range does not need to be sampled during an electric vehicle upgrade. The housing units at which an electric vehicle is modeled are specified by the Electric Vehicle Ownership characteristic. The characteristic sets the `vehicle_battery_usable_capacity`, `vehicle_fuel_economy_units`, `vehicle_fuel_economy_combined`, `ev_average_mph`, and `ev_efficiency_percent_increase` ResStock arguments. The argument definitions are found in Table “The ResStock argument definitions set in the Electric Vehicle Battery characteristic”.

<div id="table:hc_arg_def_ev_battery" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `vehicle_battery_usable_capacity` | false | kWh | Double | auto | The usable capacity of the vehicle battery, only applies to electric vehicles. If not provided, the OS-HPXML default (see [HPXML Vehicles](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-vehicles)) is used. |
| `vehicle_fuel_economy_units` | false |  | Choice | auto, kWh/mile, mile/kWh, mpge, mpg | The combined fuel economy units of the vehicle. Only ’kWh/mile’, ’mile/kWh’, or ’mpge’ are allow for electric vehicles. If not provided, the OS-HPXML default (see [HPXML Vehicles](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-vehicles>)) is used. |
| `vehicle_fuel_economy_combined` | false |  | Double | auto | The combined fuel economy of the vehicle. If not provided, the OS-HPXML default (see [HPXML Vehicles](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-vehicles>)) is used. |
| `ev_average_mph` | false | miles/hour | Double |  | The average miles/hour driven by the vehicle. |
| `ev_efficiency_percent_increase` | false | Frac | Double |  | The increase (fraction) in efficiency of the electric vehicle. |

The ResStock argument definitions set in the Electric Vehicle Battery characteristic

</div>

The options and their ResStock argument values can be found in Table “Electric Vehicle Battery options and arguments that vary for each option”. The Experian dataset is used to characterize the distribution of electric vehicles and associated battery sizes in the vehicle stock. We used the latest available data for the year 2023, which ensures that our analysis is based on the most current information regarding the electric vehicle battery stock. Although the vehicle data included information on internal combustion engine vehicles in addition to the battery electric vehicles, we filtered the dataset to focus exclusively on personal light-duty battery electric vehicles. In the dataset, there are four different categories of light-duty vehicles, including (a) Compact, (b) Midsize, (c) Sport Utility Vehicle (SUV), and (d) Pickup truck. Additionally, the dataset includes information on two total mileage ranges for the battery: (a) 200-mile range and (b) 300-mile range.

Then, for each electric vehicle type, we draw from Argonne National Laboratory’s Autonomie20[^6] vehicle powertrain simulation model for the electric vehicle energy consumption (`vehicle_fuel_economy_combined`) and battery capacity (`vehicle_battery_usable_capacity`). The units for the combined fuel economy (`vehicle_fuel_economy_units`) are always kWh/mile. The average driving speed is sourced from the 2017 NHTS which summarizes U.S. travel behavior ((Federal Highway Administration 2017)). We assume that the average speed of electric vehicles is the same as the average speed of all vehicles. A scaling factor is applied to increase the efficiency of electric vehicles (`ev_efficiency_percent_increase`). This value is 0.0 for the ResStock baseline meaning that the efficiency is equal to `vehicle_fuel_economy_combined`, but it is exposed so that scenarios of EV efficiency improvements can be modeled.

<div id="table:hc_opt_ev_battery" data-source="3c_ResStockInputs.tex">

| Option name | `vehicle_battery_usable_capacity` | `vehicle_fuel_economy_combined` | `ev_average_mph` | `vehicle_fuel_economy_units` | `ev_efficiency_percent_increase` |
|:---|:---|:---|:---|:---|:---|
| Compact, Battery Electric Vehicle, 200 mile range | 40.168 | 0.209901 | 22 | kWh/mile | 0.0 |
| Compact, Battery Electric Vehicle, 300 mile range | 63.433 | 0.220020 | 22 | kWh/mile | 0.0 |
| Midsize, Battery Electric Vehicle, 200 mile range | 41.978 | 0.219174 | 22 | kWh/mile | 0.0 |
| Midsize, Battery Electric Vehicle, 300 mile range | 65.441 | 0.229449 | 22 | kWh/mile | 0.0 |
| Pickup, Battery Electric Vehicle, 200 mile range | 67.738 | 0.357648 | 22 | kWh/mile | 0.0 |
| Pickup, Battery Electric Vehicle, 300 mile range | 105.946 | 0.373794 | 22 | kWh/mile | 0.0 |
| SUV, Battery Electric Vehicle, 200 mile range | 53.503 | 0.267513 | 22 | kWh/mile | 0.0 |
| SUV, Battery Electric Vehicle, 300 mile range | 83.680 | 0.278934 | 22 | kWh/mile | 0.0 |

Electric Vehicle Battery options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

- Vehicle stock data starts with the Experian registration data and then is projected by TEMPO to 2023.

- If the household does not have an electric vehicle, the options represent the household preference.

### Electric Vehicle Charge At Home

#### Description

The percentage a household would or does charge their electric vehicle at home.

#### Distribution Data Source(s)

U.S. EIA 2020 Residential Energy Consumption Survey (RECS) microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

#### Options

The options for the Electric Vehicle Charge At Home characteristic is a set of percentages that determine how much of the electric vehicle’s energy shows up on the residential meter vs charging at work or at public chargers. Every unit in the baseline is assigned one of these options so that the home charging fraction does not need to be sampled during an electric vehicle upgrade. The units with an electric vehicle are specified by the Electric Vehicle Ownership characteristic. The characteristic sets the `vehicle_fraction_charged_home` ResStock argument. The argument definition is found in Table “The ResStock argument definitions set in the Electric Vehicle Charge At Home characteristic”.

<div id="table:hc_arg_def_ev_charge_at_home" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `vehicle_fraction_charged_home` | false |  | Double | auto | The fraction of charging energy provided by the at-home charger to the vehicle, only applies to electric vehicles. If not provided, the OS-HPXML default (see [HPXML Vehicles](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-vehicles)) is used. |

The ResStock argument definitions set in the Electric Vehicle Charge At Home characteristic

</div>

The options and their ResStock arguments values can be found in Table “Electric Vehicle Charge At Home options and arguments that vary for each option”.

<div id="table:hc_opt_ev_charge_at_home" data-source="3c_ResStockInputs.tex">

| Option name | `vehicle_fraction_charged_home` |
|:------------|:--------------------------------|
| 0-19%       | 0.1                             |
| 20-39%      | 0.3                             |
| 40-59%      | 0.5                             |
| 60-79%      | 0.7                             |
| 80-99%      | 0.9                             |
| 100%        | 1.0                             |

Electric Vehicle Charge At Home options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

- Due to a low sample count, the distributions are constructed by downscaling a dwelling unit sub-tsv with a household sub-tsv. The two sub-tsvs have the following dependencies: tsv1 dependency=\[’Geometry Building Type RECS’\], tsv2 dependency=\[’Federal Poverty Level’\], In combining tsv1 and tsv2, the conditional relationships are ignored across (’Geometry Building Type RECS’ and ’Federal Poverty Level’).

### Electric Vehicle Charger

#### Description

Presence and type of electric vehicle charger used at the dwelling unit.

#### Distribution Data Source(s)

U.S. EIA 2020 Residential Energy Consumption Survey (RECS) microdata.

#### Direct Conditional Dependencies

- Electrical Vehicle Ownership

- Federal Poverty Level

- Geometry Building Type RECS

- Tenure

#### Options

The options for the Electric Vehicle Charger characteristic describe the type of charger used by an electric vehicle owner at home. The characteristic sets the `ev_charger_present`, `ev_charger_power`, and `ev_charger_location` ResStock arguments. The argument definition is found in Table “The ResStock argument definitions set in the Electric Vehicle Charger characteristic”. If `ev_charger_present` is set to "true", then the other arguments are required otherwise the power and location arguments will not be used. In the baseline stock the `ev_charger_location` argument is set to "auto", meaning it takes the default OpenStudio-HPXML value (see OpenStudio-HPXML [Electric Vehicle Charger](https://openstudio-hpxml.readthedocs.io/en/latest/workflow_inputs.html#hpxml-electric-vehicle-chargers)).

<div id="table:hc_arg_def_ev_charger" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `ev_charger_present` | false |  | Boolean | auto, true, false | Whether there is an electric vehicle charger present. |
| `ev_charger_power` | false | W | Double | auto | The rated power output of the EV charger. If not provided, the OS-HPXML default (see HPXML [Electric Vehicle Chargers](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-electric-vehicle-chargers>)) is used. |
| `ev_charger_location` | false |  | Choice | auto, garage, outside | The space type for the EV charger. If not provided, the OS-HPXML default (see HPXML [Electric Vehicle Chargers](<https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-electric-vehicle-chargers>)) is used. |

The ResStock argument definitions set in the Electric Vehicle Charger characteristic

</div>

The options and their ResStock arguments values can be found in Table “Electric Vehicle Charger options and arguments that vary for each option”. The Void option will not be sampled but indicates when an impossible combination of dependencies are listed.

<div id="table:hc_opt_ev_charger" data-source="3c_ResStockInputs.tex">

| Option name | `ev_charger_present` | `ev_charger_power` | `ev_charger_location` |
|:---|:---|:---|:---|
| Level 1 charger | true | 1600 | auto |
| Level 2 charger | true | 5690 | auto |
| None | false |  |  |
| Void | false |  |  |

Electric Vehicle Charger options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

Dwelling units with an electric vehicle need to have at least a Level 1 charger. Due to low sample sizes, coarsening of the dependencies are applied in the following order.

1.  Federal Poverty Level lumped every 100%

2.  Federal Poverty Level lumped every 200%

3.  Building type is consolidated into three bins 1) single-family detached and 2) multi-family with 5+ units, and 3) mobile homes, multi-family 2-4 units, and single-family attached

4.  Building type is consolidated into two bins 1) single-family detached and 2) all other building types

5.  Federal Poverty Level is combined into 400%+ and \<400% bins

### Electric Vehicle Miles Traveled

#### Description

The number of miles an electric vehicle is driven in a year if the unit owns an electric vehicle.

#### Distribution Data Source(s)

The 2022 U.S. Federal Highway Administration National Household Travel Survey (NHTS) microdata.

#### Direct Conditional Dependencies

No direct conditional dependencies.

#### Options

The options for Electric Vehicle Miles Traveled characteristic are a set of miles traveled by the electric vehicle. These options do not specifiy if the unit has a vehicle, but rather the amount of miles the EV travels if the dwelling unit has an electric vehicle. Every unit is assigned one of these options so that the vehicle miles traveled does not need to be sampled during an electric vehicle upgrade. The units with an electric vehicle is specified by the Electric Vehicle Ownership characteristic. The characteristic sets the `vehicle_miles_driven_per_year` ResStock argument. The argument definition is found in Table “The ResStock argument definitions set in the Electric Vehicle Miles Traveled characteristic”.

<div id="table:hc_arg_def_ev_vmt" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `vehicle_miles_driven_per_year` | false | miles | Double | auto | The annual miles the vehicle is driven. If not provided, the OS-HPXML default (see HPXML [Vehicles](<https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-vehicles>)) is used. |

The ResStock argument definitions set in the Electric Vehicle Miles Traveled characteristic

</div>

The options and their ResStock arguments values can be found in Table “Electric Vehicle Vehicle Miles Traveled options and arguments that vary for each option”. The options range between 1,000 miles and 22,500 miles.

<div id="table:hc_opt_ev_vmt" data-source="3c_ResStockInputs.tex">

| Option name | `vehicle_miles_driven_per_year` |
|:------------|:--------------------------------|
| 1000        | 1000                            |
| 3000        | 3000                            |
| 5000        | 5000                            |
| 7000        | 7000                            |
| 9000        | 9000                            |
| 11000       | 11000                           |
| 13000       | 13000                           |
| 15000       | 15000                           |
| 17000       | 17000                           |
| 19000       | 19000                           |
| 22500       | 22500                           |

Electric Vehicle Vehicle Miles Traveled options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

No assumptions are made.

### Electric Vehicle Outlet Access

#### Description

The unit has an outlet within 20 feet of vehicle parking.

#### Distribution Data Source(s)

U.S. EIA 2020 Residential Energy Consumption Survey (RECS) microdata.

#### Direct Conditional Dependencies

- Electric Vehicle Charger

- Federal Poverty Level

- Geometry Building Type RECS

- Tenure

- Vinteage ACS

#### Options

The options for Electric Vehicle Outlet Access characteristic indicate whether the unit has charging within 20 ft of the vehicle parking. This characteristic does not assign any ResStock arguments. The options are Yes, No, and Void. The Void option is assigned to impossible dependency combinations.

#### Distribution Assumption(s)

- RECS 2020 has Multi-Family 5+ units marked as Not Applicable. These units are replaced by data from the No Place Like Home Study (https://www.nrel.gov/docs/fy22osti/81065.pdf) Table 1 Scenario 2. Multi-Family 5+ units owners is assumed for 12% units having electrical access. This fraction is based on the average of mid-capacity apartment and high-capacity apartment. Multi-Family 5+ units owners is assumed for 28% units having electrical access.

- Units reported to have a Level 1 or Level 2 charger in the field EVCHRGTYPE are assumed to have outlet access.

- Level 1 chargers without outlet access are units with EVs, but report no outlet access within 20 ft of vehicle parking.

- Due to low sample count, the tsv is constructed by downscaling a dwelling unit sub-tsv with a household sub-tsv. The sub-tsvs have the following dependencies:

  - Dwelling unit sub-tsv : deps=\[’Geometry Building Type RECS’, ’Vintage ACS’, ’Electric Vehicle Charger’\] with the following fallback coarsening order: 1) Vintage ACS to the National distribution and 2) combining Geometry Building Type RECS together into two bins a) single-family detached, mobile homes, and single family attached and b) multi-family with 2 - 4 units and multi-family with 5+ units

  - Household sub-tsv : deps=\[’Geometry Building Type RECS’, ’State’ ’Tenure’, ’Federal Poverty Level’\]

  - In combining the dwelling unit sub-tsv and household sub-tsv, the conditional relationships are ignored across (\[’Vintage ACS’, ’Electric Vehicle Charger’\], \[’Tenure’, ’Federal Poverty Level’\]).

## Electric Vehicle Charging and Discharging Schedules

Charging and discharging schedules provide the time periods when the EV can charge or discharge energy. The charging and discharging schedules are connected to the stochastic occupancy model (based on American Time Use Survey data) in OpenStudio-HPXML. Each unit with an EV has an occupant assigned as the sole driver. The schedule generator takes EV vehicle miles traveled and the average speed to calculate the total hours driven per year. The total hours driven per year is used as an input to the EV schedule generator and produces the charging and discharging schedule, while the battery model takes care of the actual power draw during the charging and discharging period. Figure “Illustration of EV battery discharge schedule generation.” shows an example of a generated discharging schedule. This schedule shows that during an “away period” for the occupant, the vehicle is discharged immediately after the occupant leaves and just before they arrive back home, proportional to the length of the away period. The charging schedule is similarly based on occupancy, where the baseline behavior assumes the vehicle is plugged in when the occupant arrives home, and remains plugged in for the full occupied period.

<figure id="fig:ev_discharge">
<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/technical_reference/docs/technical_reference_guide/3c_ResStockInputs.yaml
     source: images/Example EV Discharging Schedule.png
     method: vision-description
     described: 2026-11-11 -->

<img alt="Annotated step chart of an occupant schedule and the EV battery discharge schedule built from it" src="images/Example EV Discharging Schedule.png" style="width:100.0%" />

Annotated step chart for January 7, 2007, from 04:00 to about 21:00, with values from 0 to 1. A blue line is the occupant schedule, 1 when the occupant is home, and an orange line the discharge schedule. Two away periods are marked, a long one from about 06:00 to 17:00 and a short one in the evening. Discharge occurs at the start and end of each away period, for a duration proportional to its length; a value below 1 means discharge does not last the full 15-minute timestep. A printed note says total discharge duration in a year equals total driving hours in a year.

<figcaption>Illustration of EV battery discharge schedule generation.</figcaption>
</figure>

# Electrical Panels

The electrical panel is a breaker box that distributes power from the utility pole to the connected appliances and receptacles while protecting them from overload, short circuit, or ground fault. Inside the panel, electric appliances are organized into branch circuits that are each protected by an overcurrent protection device (A.K.A. breaker). Two bus bars each carrying 120V service along with a neutral bus bar run down the breaker slots to supply power at either 120V or 240V. 120V circuits use single-pole breakers that take up one space while 240V require two-space double-pole breakers to draw the 240V potential between the two hot wires. Some breakers, such as tandem breakers, can serve multiple circuits without taking up more space. The panel service rating refers to the maximum amps of current the panel can safely handle to power the circuits. This is often the same as the ampacity rating of the service entrance disconnect, which limits the amount of power entering the panel, though it is possible to have a panel rated larger than its service disconnect, and vice versa.

## Overview

The electrical panel service load and breaker space calculations are used to assess whether the electrical panel has a capacity and a space constraint, respectively, during a home electrification. As new electric loads are introduced into the home, the panel may need to be reconfigured, extended, or replaced due to insufficient capacity or insufficient breaker space. For example, homes that are not already using electricity for heating and cooking are more likely to have capacity constraints, thus requiring an upgrade, load controls, or other interventions. A panel with all slots occupied cannot accommodate new circuits unless space-saving breakers are used, or a subpanel is added. When the panel is being upsized for capacity, an electrical service upgrade may also be required to upsize the service entrance wiring from the pole to the service disconnect. By estimating the panel capacity constraints, the service load calculation can serve as an upper bound estimate for service upgrades when applied to the housing stock.

To evaluate potential panel constraints, we first characterize the panel service rating and the number of available breaker spaces on the panels for the US housing stock using best available data. Then we perform service load calculations based on code to get the required capacity for a given upgrade scenario. The calculated value is compared with the rating of the panel to determine the capacity constraint. For the breaker space calculation, the number of occupied breaker spaces on the panel is estimated by tabulating from each appliance for a given modeled home. This pre-upgrade occupied space estimate is combined with the available breaker space input to determine the rated total number of spaces on the panel. Then the number of occupied breaker spaces is calculated for the modeled home post-upgrade and subtracted from the rated number of spaces to determine the space constraint for a given upgrade scenario. The following sections provide more detail on each of the two calculations. The electrical panel outputs can be found in Section “Electrical Panels”.

## Input Characteristics

We derived the electrical panel service rating (A) and the breaker space headroom using a limited set of survey data. For single-family attached and detached dwellings, the data was used to train machine-learning models, which were then used to generate the distribution of the panel attributes. For multi-family, the characteristic distributions were derived directly from the data due to insufficient samples to support model training. As the dataset does not contain high-fidelity samples for mobile homes, we use the distributions for single-family detached to approximate mobile homes.

79% of the survey data comes from the Pacific regions via: TECH Clean California, Bay Area Renewable Energy Network, Home Energy Analytics, and Northwest Energy Efficiency Alliance Residential Building Stock Assessment, while 20% comes from the Minnesota Center for Energy and the Environment and 1% from LBL Citizen Science survey, which is administered nationally. Due to the data bias towards the Pacific states, where gas heating is dominant, separate model is used for electrically heated and fuel heated single-family dwellings. Table “Dependencies for the distributions of electrical panel service rating and breaker space.” outlines the dependencies for each of the distributions generated for assigning the panel characteristics. The field values for electrical panel service rating (A) are: \<100, 100, 101-124, 125, 126-199, 200, 201+. The availale breaker space options (count) range from 0 to 31.

<div id="tab:panel_deps" data-source="3c_ResStockInputs.tex">

| **Electrical Panel Input** | **Housing Segment** | **Dependencies** |
|:---|:---|:---|
| Service rating | Single-Family, electric heat | Building type, floor area, vintage, water heater fuel, cooling type, clothes dryer, cooking range |
| Service rating | Single-Family, fuel heat | Building type, floor area, vintage |
| Service rating | Multi-Family | Floor area, vintage, heating fuel |
| Breaker space headroom | Single-Family | Service rating, major electric load count, floor area |
| Breaker space headroom | Multi-Family | Service rating, major electric load count |

Dependencies for the distributions of electrical panel service rating and breaker space.

</div>

## Service Load Calculations

The service and feeder load calculation refers to a type of load calculation used to size the service entrance wires (between the utility poles and the meter or service disconnect) or the feeder wires (between panels, such as those between a building’s main panel and subpanel in each apartment unit) according to Section 220 of the National Electrical Code (NEC). This calculation also applies to the sizing of panels to ensure electrical safety. The NEC updates every three years, and the adoption of NEC varies by municipality. Instead of capturing every NEC version currently in practice, which is impractical, we implemented the load calculations per the latest NEC release, 2023, which represents the best practice adoptable. For 2023, the service load calculation is different for new constructions and existing buildings undergoing an upgrade. Two methods are available for existing buildings, and both are implemented in ResStock: load-based and metered-based. The calculated loads (W) represent the total occuied load from installed electrical equipment and are converted to total occupied capacity (A) by dividing by 240V, the panel voltage. The occupied capacity is compared with the panel service rating to calculate headroom capacity and assess NEC compliance.

### Load-based Method

The service rating of the panel is generally not the sum of individual branch circuit ratings because not all equipment is expected to be operating at full load simultaneously. Instead, there is some diversity in the loads expected to make up the coincidence peak, even at a worst-case scenario. Following this idea, NEC Section 220.83 provides guidance on estimating this peak from the bottom-up to assess whether a panel has sufficient capacity to serve new loads. Table “Summary of load-based method per 2023 NEC 220.83” below summarizes the load-based method, and the assumptions made in ResStock to perform this calculation.

<div id="tab:panel_load_method" data-source="3c_ResStockInputs.tex">

<table>
<caption>Summary of load-based method per 2023 NEC 220.83</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Load Type</strong></th>
<th style="text-align: left;"><strong>Load Amount</strong></th>
<th style="text-align: left;"><strong>ResStock Assumptions</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">General lighting / receptacle load</td>
<td style="text-align: left;">3 W/sqft</td>
<td style="text-align: left;">Uses conditioned floor area</td>
</tr>
<tr>
<td style="text-align: left;">Kitchen small appliance circuits</td>
<td style="text-align: left;">Min two branches at 1500 W each</td>
<td style="text-align: left;">Two branches per dwelling unit</td>
</tr>
<tr>
<td style="text-align: left;">Laundry circuits</td>
<td style="text-align: left;">Min one branch at 1500 W</td>
<td style="text-align: left;">One branch per dwelling unit</td>
</tr>
<tr>
<td style="text-align: left;">Major electric loads</td>
<td style="text-align: left;"><p>Nameplate rating of:</p>
<ul>
<li><p>HVAC (larger of heating and cooling)</p></li>
<li><p>Water heaters</p></li>
<li><p>Clothes dryers (not already on laundry circuits)</p></li>
<li><p>Cooking ranges/ovens</p></li>
<li><p>All other appliances that are "fastened in place, permanently connected, or located to be on a specific circuit"</p></li>
</ul></td>
<td style="text-align: left;"><p>All other appliances include:</p>
<ul>
<li><p>Hot tub/spa</p></li>
<li><p>Pool heaters and pumps</p></li>
<li><p>Well pumps</p></li>
<li><p>Electric vehicle supply equipment (EVSE)</p></li>
<li><p>Dishwashers</p></li>
<li><p>Spot ventilations</p></li>
<li><p>Selected plug loads: microwaves, garbage disposal, garage doors</p></li>
<li><p>Low-power (120V) appliances: water heaters, cooktops (not yet modeled)</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;">Demand factors and summation</td>
<td style="text-align: left;"><p>Demand factors apply to both existing and new loads, depends on whether new HVAC is being installed:</p>
<ul>
<li><p>(a) If not adding new HVAC, take the first 8 kVA of all loads at 100% and remainder loads at 40%.</p></li>
<li><p>(b) If adding new HVAC, take HVAC load at 100%, first 8 kVA of all other loads at 100%, and remainder loads at 40%.</p></li>
</ul></td>
<td style="text-align: left;">Total occupied capacity in the baseline is calculated using (a)</td>
</tr>
</tbody>
</table>

</div>

Of note, we accounted for selected plug loads in the load-based calculation that we do not explicitly model in terms of energy for which plug loads is a single end use category. We assumed all dwelling units have a microwave, 52% homes have a garage disposal (per AHS 2013), and one garage door opener for homes with an attached garage. Additionally, the demand factors applied to sum up the loads vary depending on whether new HVAC load is being introduced by an upgrade. If all or part of the HVAC load is considered new, a more conservative approach (part (b)) is taken by taking the HVAC load (maximum of either heating or cooling) at 100% instead of lumping it with all other loads to undergo adjustment by demand tiers. For the baseline load calculation, the total occupied load is calculated using part (a) as no new load is introduced yet.

### Meter-based Method

The second method, metered-based, is a top-down approach by using the metered electricity peak of the preceding year to baseline the existing loading of the panel. Per NEC section 220.87, the total capacity needed for an upgrade is calculated as 1.25 of the baseline peak electricity plus any new loads at 100%. In ResStock, the annual electricity peak is used in place of the metered data and the new loads that are counted are the same as those outlined in the load-based method.

For a given upgrade, the load-based method is generally more conservative than the metered-based at estimating the number of homes with a panel capacity constraint. However, this may not be the case for homes that have high equipment utilization factors or setpoints that drive up HVAC use. Additionally, as the metered-based method does not account for the removal of any legacy loads, the method may be more conservative for certain upgrade scenarios. For example, for a home that is upgrading an electric boiler to a heat pump with integrated heat strip, the heating load is being counted twice, from the incumbent equipment as part of the annual electric peak and the new equipment.

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

## Income

The ACS reports both household and family incomes in continuous values, which are then binned in ResStock. Income in ResStock represents the household income, or the total income of all household members age 15 or higher standardized to 2019 dollars. From income a variety of secondary income parameters are derived. Income RECS2015 and Income RECS2020 are binned variations that align with the reported bins from RECS 2015 and 2020, respectively. Federal poverty level (FPL) standardizes the household income according to the 2019 U.S. federal poverty guidelines, which vary based on household size and differ for the contiguous United States, Hawaii, and Alaska. Table “2019 federal poverty guidelines (aspe_2019_fpl)” shows the poverty lines by household size for the lower 48 states including D.C., for Hawaii, and for Alaska.

<div id="tab:fpl" data-source="3c_ResStockInputs.tex">

|        Household size        | Contiguous U.S. |  Hawaii  |  Alaska  |
|:----------------------------:|:---------------:|:--------:|:--------:|
|              1               |    \$12,490     | \$14,380 | \$15,600 |
|              2               |    \$16,910     | \$19,460 | \$21,130 |
|              3               |    \$21,330     | \$24,540 | \$26,660 |
|              4               |    \$25,750     | \$29,620 | \$32,190 |
|              5               |    \$30,170     | \$34,700 | \$37,720 |
|              6               |    \$34,590     | \$39,780 | \$43,250 |
|              7               |    \$39,010     | \$44,860 | \$48,780 |
|              8               |    \$43,430     | \$49,940 | \$54,310 |
| Per additional person over 8 |     \$4,420     | \$5,080  | \$5,530  |

2019 federal poverty guidelines ((Assistant Secretary For Planning and Evaluation n.d.a))

</div>

Per Table “2019 federal poverty guidelines (aspe_2019_fpl)”, the poverty line is \$25,750 for a household of four in the contiguous U.S. A household of the same size making \$40,000 per year in Colorado is therefore at 150%–200% of FPL (40,000/25,750\*100% = 155%). However, that exact household would be considered 100%–150% of FPL if living in Hawaii instead (40,000/29,620\*100% = 135%). FPL is used to determine eligibility for several federal assistance programs, including Low-Income Home Energy Assistance Program (LIHEAP) and Weatherization Assistance for Low-Income Persons ((Assistant Secretary For Planning and Evaluation n.d.b)).

Similar to FPL, Area Median Income in ResStock is household income standardized as a percentage of the [2019 Income Limits](https://www.huduser.gov/portal/datasets/il.html#data_2019), which are annually updated by HUD. The Income Limits are means-testing metrics intended to determine financial assistance eligibility, such as Section 8 housing, based on family income ((Department of Housing and Urban Development 2019)). Since ResStock does not model multiple families sharing a single housing unit, household income is treated the same as family income, and household income is used to calculate percent Area Median Income instead. Like FPL, the income limits vary by family size. But unlike FPL, they adjust for local housing costs and vary by county subdivisions. Generally, 0%–80% Area Median Income is regarded as Low-to-Moderate Income and the threshold for receiving most types of financial assistance. Sometimes 80%–150% Area Median Income households are eligible for partial financial assistance, such as in Section 50122 of the Inflation Reduction Act ((U.S. Congress 2022)) for home electrification rebates.

State Metro Median Income (SMMI) is a variant of Area Median Income. As the name suggests, SMMI standardizes the household income based on 2019 Income Limits set at the state level while differentiating between metropolitan and non-metropolitan areas. This metric is created primarily for the integration of socio-demographically differentiated time-use schedules from the American Time Use Survey, which tags respondents by state and metro status.

## Energy Burden

Energy burden can be calculated using the energy bills and income information from ResStock simulation summary results. Energy burden is defined as the percent of household income spent on energy bills. A household spending 6% or more of their income on energy is generally regarded as highly energy burdened and 10% or more as severely burdened ((Drehobl et al. 2020)). For this calculation, the income bins can be converted to representative income values using a series of lookup tables derived from the ACS data. The lookup tables tabulate the weighted median income over the cross sections of income bin, occupants, FPL, tenure, building type, and different geographic resolutions, starting with the intersection of PUMA and county. The income bin gets converted to a numerical value for each housing sample by matching the mapping characteristics in the lookup table. The conversion starts with the highest geographic resolution lookup and moves to the next highest resolution if the lookup value is missing until all housing samples are converted. Finally, since negative and zero income are reported in ACS, any representative income at zero or less is adjusted to one so that the energy burden can be approximated.

## Vacant Units

ResStock models just over 12% of housing units as vacant nationally, reflecting the data in PUMS 2019. In PUMS, a housing unit is considered vacant if it is not occupied at the time of the survey. This includes housing units being prepared for rent or sale, units rented or sold but not yet occupied, or units for seasonal, occasional, or migratory use. The portion of housing units that are vacant is dependent on the building type and PUMA (i.e., location). While the vacancy saturation includes samples that are only vacant part time, ResStock models all vacant units as vacant for an entire calendar year.

In most cases ResStock models vacant units using the same characteristic distributions as occupied units. For example, RECS, where all of the respondents are unit occupants, does not have unoccupied units included in its survey. Tenure is a dependency in many of the appliance characteristics derived from RECS. In those characteristics distributions, Tenure=Not Available is analogous to vacant units and their distributions are based on the full dataset (i.e., the occupied units regardless of tenure). The distribution of Geometry Floor Area, however, which comes from 2017-2019 American Housing Survey, has a real distinction between renter-occupied, owner-occupied, and vacant units, as the survey records both tenure and vacancy information.

The differences between our modeling of occupied units and vacant units are currently confined to these areas: heating setpoint, schedule-driven loads and ceiling fans, PV, and demographics.

Vacant units are set to have a heating setpoint characteristic of 55° F, intended as a “don’t freeze the pipes” approach. Vacancy status is not in the dependency tree for the heating setpoint offset characteristics, so many vacant housing units are modeled with heating setpoint offsets from that 55° F.

Reflecting a lack of occupants, vacant units are modeled without any schedule-driven appliance usage. This results in no energy consumption for the following end uses across all fuels:

- Ceiling fan (albeit through a different mechanism)

- Clothes dryer

- Clothes washer

- Dishwasher

- Fireplace

- Grill

- Lighting (all types)

- Mechanical ventilation

- Well pump

- Plug loads

- Range/oven

- TVs.

There are also no PV systems modeled for vacant units. Because vacant units have no associated household—no set of people that live in them—their *occupants* characteristic is 0 and they do not have household-based characteristics such as *income* or *tenure*. All other characteristics, modeling approaches, and end uses are independent of vacancy status; that is, if the housing unit had the same characteristics and was occupied, it would have the same results.

## Other Household Attributes

Occupants is the household size or the number of residents living together in a housing unit. Occupant is zero for vacant units and 10+ is modeled as 11. This assumption is used when converting household income to FPL, Area Median Income, or SMMI. Tenure defines whether a housing unit is renter- or owner-occupied. A unit occupied without rent payment is considered renter-occupied under the assumption that the occupants cannot easily update the property without the ownership. “Household Has Tribal Persons” is derived from the person samples to indicate whether a household has at least one person identified as American Indian or from one of the American Tribes. These household characteristics are either zero or not available for vacant units.

The details of each household characteristics are found in the next section.

### Income

#### Description

Income of the household occupying the housing unit.

#### Distribution Data Sources

- 2019 5-year PUMS from the University of Minnesota.

#### Direct Conditional Dependencies

- Geometry Building Type RECS

- PUMA

- Tenure

- Vintage ACS.

#### Options

The Income options are a set of income bins ranging from 10,000 to 199,999. The two end bins are \<10,000 and 200,000+. This characteristic has no ResStock arguments. Instead, it is used to construct other income characteristics and influences the distribution of housing characteristics as an indirect dependency.

#### Distribution Assumptions

- In ACS, Income and Tenure are reported for occupied units only. Because we assume vacant units share the same Tenure distribution as occupied units, by extension, we assume this Income distribution applies to all units regardless of Vacancy Status. For reference, 57445 / 140160 rows have sampling_probability \>= 1/550,000.[^7] Of those rows, 2961 (5%) were replaced due to low samples in the following process: Where sample counts are less than 10 (79145 / 140160 relevant rows), the Census Division by PUMA Metro Status average distribution has been inserted first (76864), followed by Census Division by ‘Metro’/‘Non-metro’ average distribution (1187), followed by Census Region by PUMA Metro Status average distribution (282), followed by Census Region by ‘Metro’/‘Non-metro’ average distribution (112).

### Income RECS2015

#### Description

Income of the household occupying the housing unit that are aligned with the 2015 U.S. Energy Information Administration Residential Energy Consumption Survey.

#### Distribution Data Sources

- 2019 5-year PUMS from the University of Minnesota.

#### Direct Conditional Dependencies

- Income.

#### Options

The Income RECS2015 option are bins mapped from the Income characteristic to align with the RECS 2015 income bins. The characteristic does not set any ResStock arguments.

#### Distribution Assumptions

- The income in 2019 USD are consolidated to align with those of RECS 2015 without inflation adjustment.

### Income RECS2020

#### Description

Income of the household occupying the housing unit that are aligned with the 2020 U.S. Energy Information Administration Residential Energy Consumption Survey.

#### Distribution Data Sources

- 2019 5-year PUMS from the University of Minnesota.

#### Direct Conditional Dependencies

- Income.

#### Options

The Income RECS2020 options are bins mapped from the Income characteristic to align with the RECS 2020 income bins. The characteristic does not set any ResStock arguments.

#### Distribution Assumptions

- The income in 2019 USD are consolidated to align with those of RECS 2020 without inflation adjustment.

### Federal Poverty Level

#### Description

Income as a percent of the federal poverty line of the household occupying the housing unit.

#### Distribution Data Sources

- Income from 2019 5-year PUMS from the University of Minnesota.

- 2019 federal poverty guidelines from [Office of the Assistant Secretary for Planning and Evaluation within the U.S. Department of Health and Human Services](https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines/prior-hhs-poverty-guidelines-federal-register-references/2019-poverty-guidelines).

#### Direct Conditional Dependencies

- Income

- Occupants.

#### Options

The Federal Poverty Level options are the following bins: %0-100%, 100%–150%, 150%–200%, 200%–300%, 300%–400%, and 400%+. The Not Available option is for vacant units. The Federal Poverty Level options do not set any ResStock arguments.

#### Distribution Assumptions

- Percent Federal Poverty Level is calculated using annual household income in 2019 USD (continuous, not binned) from 2019 5-year PUMS data and 2019 Federal Poverty Lines for contiguous U.S., where the FPL threshold for 1-occupant household is \$12,490 and \$4,420 for every additional person in the household.

### Area Median Income

#### Description

Income as a percent of area median income of the household occupying the housing unit.

#### Distribution Data Sources

- Income from 2019 5-year PUMS from the University of Minnesota.

- Area Median Income definitions based on [2019 Income Limits from HUD](https://www.huduser.gov/portal/datasets/il.html#data_2019).

#### Direct Conditional Dependencies

- Income

- Occupants

- PUMA.

#### Options

The Area Median Income options are the following bins: 0%–30%, 30%–60%, 60%–80%, 80%–100%, 100%–120%, 120%–150%, and 150+%. The Not Available option is for vacant units. The Area Median Income options do not set any ResStock arguments.

#### Distribution Assumptions

1.  Percent Area Median Income is calculated using annual household income in 2019 USD (continuous, not binned) from 2019 5-year PUMS data and 2019 income limits from HUD. These limits adjust for household size AND local housing costs (i.e., fair market rents). Income limits reported at county subdivisions are consolidated to County using a [crosswalk](https://mcdc.missouri.edu/applications/geocorr2014.html) generated from Missouri Census Data Center’s geocorr (2014), which has 2010 ACS housing unit count.

2.  For the 478 counties available in PUMS (60%), the county-level income limits are used. For all others (40%), PUMA-level income limits are used, which are converted from county-level using 2010 ACS housing unit count.

### State Metro Median Income

#### Description

State Metro Median Income of the household occupying the housing unit. This is different from State Median Income in that the Income Limits are differentiated by metro and nonmetro regions of the state.

#### Distribution Data Sources

- Income from 2019 5-year PUMS from the University of Minnesota.

- Income Limits derived from 2019 5-year PUMS from the University of Minnesota and 2019 median income by state and metro/nonmetro area from HUD.

#### Direct Conditional Dependencies

- Area Median Income

- County Metro Status

- State.

#### Options

The State Metro Median Income options are the following bins: 0%–30%, 30%–60%, 60%–80%, 80%–100%, 100%–120%, 120%–150%, and 150+%. The Not Available option is for vacant units. The State Metro Median Income options do not set any ResStock arguments.

#### Distribution Assumptions

- Percent State Metro Median Income is calculated using annual household income in 2019 USD (continuous, not binned) from 2019 5-year PUMS data and 2019 median income by state and metro/nonmetro area from HUD. A County Metro Status-differentiated Income Limits table is derived from the median income table by adjusting for household size, which is consistent with the method of generating state income limits by HUD.

### Occupants

#### Description

The number of occupants living in the housing unit.

#### Distribution Data Sources

- 2019 5-year PUMS from the University of Minnesota.

#### Direct Conditional Dependencies

- Bedrooms

- Census Division

- Geometry Building Type RECS

- Income RECS2015

- PUMA Metro Status

- Tenure.

#### Options

The Occupants options range from 0 to 10+ for the the ResStock baseline baseline (Table “The ResStock arguments set in the Occupants characteristic”). This characteristic assigns value to `geometry_unit_num_occupants` accordingly, with `geometry_unit_num_occupants`=11 for Occupants=10+. Occupants=0 corresponds to vacant units. `general_water_use_usage_multiplier` is auto-calculated from occupants.

<div id="table:hc_arg_def_occupants" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_unit_num_occupants` | false | \# | Double |  | The number of occupants in the unit. If not provided, an *asset* calculation is performed assuming standard occupancy, in which various end-use defaults (e.g., plug loads, appliances, and hot water usage) are calculated based on Number of Bedrooms and Conditioned Floor Area per ANSI/RESNET/ICC 301-2019. If provided, an *operational* calculation is instead performed in which the end-use defaults are adjusted using the relationship between Number of Bedrooms and Number of Occupants from RECS 2015. |
| `general_water_use_usage_multiplier` | false |  | Double | auto | Multiplier on internal gains from general water use (floor mopping, shower evaporation, water films on showers, tubs & sinks surfaces, plant watering, etc.) that can reflect, e.g., high/low usage occupants. |

The ResStock arguments set in the Occupants characteristic

</div>

#### Distribution Assumptions

- Option=10+ has a (weighted) representative value of 11. In ACS, Income, Tenure, and Occupants are reported for occupied units only. Because we assume vacant units share the same Income and Tenure distributions as occupied units, by extension, we assume this Occupants distribution applies to all units regardless of Vacancy Status. Where sample counts are less than 10 (6,243 / 18,000 rows), the Census Region average distribution has been inserted first (2,593), followed by national average distribution (2,678), followed by national + ‘MF’/‘SF’ average distribution (252), followed by national + ‘MF’/‘SF’ + ‘Metro’/‘Non-metro’ average distribution (315), followed by national + ‘MF’/‘SF’ + ‘Metro’/‘Non-metro’ + Vacancy Status average distribution (657).

### Vacancy Status

#### Description

The vacancy status (occupied or vacant) of the housing unit.

#### Distribution Data Sources

- 2019 5-year PUMS from the University of Minnesota.

#### Direct Conditional Dependencies

- Geometry Building Type RECS

- PUMA.

#### Options

The Vacancy Status options are either Occupied or Vacant. The options assign the vacancy periods through the `schedules_vacancy_periods` ResStock argument (Table “The ResStock arguments set in the Vacancy Status characteristic”). Vacant units are assumed to be vacant for the full calendar year.

<div id="table:hc_opt_vacancy" data-source="3c_ResStockInputs.tex">

| Option name | `schedules_vacancy_periods` |
|:------------|:----------------------------|
| Occupied    |                             |
| Vacant      | Jan 1–Dec 31                |

The ResStock arguments set in the Vacancy Status characteristic

</div>

The argument definition of the arguments set in the Vacancy Status characteristic can be found in Table “The ResStock arguments set in the Vacancy Status characteristic”.

<div id="table:hc_arg_def_vacancy" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `schedules_vacancy_periods` | false |  | String |  | Specifies the vacancy periods. Enter a date like “Dec 15–Jan 15.” Optionally, can enter hour of the day like “Dec 15 2–Jan 15 20” (start hour can be 0 through 23 and end hour can be 1 through 24). If multiple periods, use a comma-separated list. |

The ResStock arguments set in the Vacancy Status characteristic

</div>

#### Distribution Assumptions

- Where sample counts are less than 10 (434 / 11,680 rows), the State average distribution has been inserted. ‘Mobile Home’ does not exist in D.C. and is replaced by ‘Single-Family Detached.’

### Tenure

#### Description

The tenancy (owner or renter) of the household occupying the housing unit.

#### Distribution Data Sources

- 2019 5-year PUMS from the University of Minnesota.

#### Direct Conditional Dependencies

- Geometry Building Type RECS

- PUMA

- Vacancy Status.

#### Options

The Tenure options are Owner, Renter, and Not Available. The not applicable option is for vacant units.

#### Distribution Assumptions

- In ACS, Tenure is reported for occupied units only. By excluding Vacancy Status as a dependency, we assume vacant units share the same Tenure distribution as occupied units. Where sample counts are less than 10 (464 / 11,680 rows), the Census Division by PUMA Metro Status average distribution has been inserted. ‘Mobile Home’ does not exist in D.C. and is replaced by ‘Single-Family Detached.’

### Household Has Tribal Persons

#### Description

The household occupying the housing unit has at least one Tribal person in the household.

#### Distribution Data Sources

- 2019 5-year PUMS from the University of Minnesota.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- PUMA.

#### Options

The Household Has Tribal Persons options are Yes, No, and Not Available. The Not Available option is for Vacant Units.

#### Distribution Assumptions

- 2,188 / 2,336 PUMA has \<10 samples and are falling back to state -level aggregated values. D.C. Mobile Homes do not exist and are replaced with Single-Family Detached.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-AUTONOMIE" class="csl-entry">

Argonne National Laboratory. 2025. *Autonomie*. <https://vms.taps.anl.gov/tools/autonomie/full_version/>.

</div>

<div id="ref-aspe_2019_fpl" class="csl-entry">

Assistant Secretary For Planning and Evaluation. n.d.a. *Office of the Assistant Secretary for Planning and Evaluation: 2019 Poverty Guidelines*. <https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines/prior-hhs-poverty-guidelines-federal-register-references/2019-poverty-guidelines>.

</div>

<div id="ref-aspe_fpl_use" class="csl-entry">

Assistant Secretary For Planning and Evaluation. n.d.b. *Office of the Assistant Secretary for Planning and Evaluation: Frequently Asked Questions Related to the Poverty Guidelines and Poverty*. <https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines/frequently-asked-questions-related-poverty-guidelines-poverty>.

</div>

<div id="ref-LBNLTTS2019" class="csl-entry">

Barbose, Galen, and Niam Darghouth. 2019. *<span class="nocase">Tracking the Sun: Pricing and Design Trends for Distributed Photovoltaic Systems in the United States</span>*. Lawrence Berkeley National Laboratory. <https://live-lbl-eta-publications.pantheonsite.io/sites/default/files/tracking_the_sun_2019_report.pdf>.

</div>

<div id="ref-hud2019_inc_lim_method" class="csl-entry">

Department of Housing and Urban Development. 2019. *Department of Housing and Urban Development: Methodology for Determining Section 8 Income Limits*. <https://www.huduser.gov/portal/datasets/il//il19/IncomeLimitsMethodology-FY19.pdf>.

</div>

<div id="ref-pvwatts_doc" class="csl-entry">

Dobos, Aron. 2014. *PVWatts Version 5 Manual*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy14osti/62641.pdf>.

</div>

<div id="ref-drehobl2020_energy_burden" class="csl-entry">

Drehobl, Ariel, Lauren Ross, and Roxana Ayala. 2020. “How High Are Household Energy Burdens? An Assessment of National and Metropolitan Energy Burden Across the United States.” *ACEEE*. <https://www.aceee.org/sites/default/files/pdfs/u2006.pdf>.

</div>

<div id="ref-EXPERIAN2023" class="csl-entry">

Experian. 2023. *Auto Registration Database*. [https://www.experian.com/automotive/auto-vehicle-data ](https://www.experian.com/automotive/auto-vehicle-data ).

</div>

<div id="ref-NHTS2017" class="csl-entry">

Federal Highway Administration. 2017. *2017 National Household Travel Survey*.

</div>

<div id="ref-NHTS2022" class="csl-entry">

Federal Highway Administration. 2022. *2022 National Household Travel Survey*.

</div>

<div id="ref-NPLH2021" class="csl-entry">

Ge, Yanbo, Christina Simeone, Andrew Duvall, and Eric Wood. 2021. *There’s No Place Like Home: Residential Parking, Electrical Access, and Implications for the Future of Electric Vehicle Charging Infrastructure*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy22osti/81065.pdf>.

</div>

<div id="ref-bahsp_2010" class="csl-entry">

Hendron, Robert, and Cheryn Engebrecht. 2010. *Building America House Simulation Protocols*. US DOE: Office of Energy Efficiency; Renewable Energy. <https://www1.eere.energy.gov/buildings/publications/pdfs/building_america/house_simulation.pdf>.

</div>

<div id="ref-ansi_resnet_301_2019" class="csl-entry">

International Code Council. 2019. *2019 ANSI/RESNET/ICC 2301 Standard for the Calculation and Labeling of the Energy Performance of Dwelling and Sleeping Units Using an Energy Rating Index*. International Code Council. <https://codes.iccsafe.org/content/RESNET3012019P1>.

</div>

<div id="ref-tank_model_parameters" class="csl-entry">

Maguire, Jeff, and David Roberts. 2020. “Deriving SimulationParameters for Storage-Type Water Heaters Using Ratings Data Produced from the Uniform Energy Factor Test Procedure.” *Building Performance Analysis Conference & SimBuild*. <https://www.nrel.gov/docs/fy21osti/71633.pdf>.

</div>

<div id="ref-MURATORI2021102967" class="csl-entry">

Muratori, Matteo, Paige Jadun, Brian Bush, et al. 2021. “Exploring the Future Energy-Mobility Nexus: The Transportation Energy & Mobility Pathway Options (TEMPO) Model.” *Transportation Research Part D: Transport and Environment* 98: 102967. https://doi.org/<https://doi.org/10.1016/j.trd.2021.102967>.

</div>

<div id="ref-RBSA" class="csl-entry">

Northwest Energy Efficiency Alliance. 2024. *2022 Residential Building Stock Assessment - Methods Report*. <https://neea.org/img/documents/2022-Residential-Building-Stock-Assessment-Methods-Report.pdf>.

</div>

<div id="ref-AHS" class="csl-entry">

U.S. Census. 2022. *American Housing Survey*. <https://www.census.gov/programs-surveys/ahs.html>.

</div>

<div id="ref-2022IRA" class="csl-entry">

U.S. Congress. 2022. *Inflation Reduction Act of 2022, Pub. L. No. 117-169, §50122.* <https://www.congress.gov/bill/117th-congress/house-bill/5376/text>.

</div>

<div id="ref-RECS2020" class="csl-entry">

U.S. Energy Information Administration. 2020. *Residential Buildings Energy Consumption Survey (RECS), 2020*. U.S. Energy Information Administration. <https://www.eia.gov/consumption/residential/data/2020/>.

</div>

<div id="ref-Wilson2014" class="csl-entry">

Wilson, E., C. Engebrecht Metzger, S. Horowitz, and R. Hendron. 2014. *2014 Building America House Simulation Protocols*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy14osti/60988.pdf>.

</div>

<div id="ref-WoodsMackenzie2020" class="csl-entry">

Woods Mackenzie. 2020. *<span class="nocase">Solar PV module technology market report 2020</span>*. <https://www.woodmac.com/reports/power-markets-solar-pv-module-technology-market-report-2020-443274/>.

</div>

<div id="ref-YIP2023" class="csl-entry">

Yip, Arthur, Christopher Hoehne, Paige Jadun, Catherine Ledna, Elaine Hale, and Matteo Muratori. 2023. *Highly Resolved Projections of Passenger Electric Vehicle Charging Loads for the Contiguous United States: Results from and Methods Behind Bottom-up Simulations of County-Specific Household Electric Vehicle Charging Load (Hourly 8760) Profiles Projected Through 2050 for Differentiated Household and Vehicle Types*. National Renewable Energy Laboratory (NREL), Golden, CO (United States). <https://doi.org/10.2172/1984452>.

</div>

</div>

[^1]: The 80% average multiplier resulted in a lower than expected water usage and is addressed in a later version of ResStock.

[^2]: For more information, see http://hes-documentation.lbl.gov/.

[^3]: For more information, see http://hes-documentation.lbl.gov/.

[^4]: ResStock currently does not account for hand washing of dishes in hot water in cases where no dishwasher is present.

[^5]: https://www.nrel.gov/transportation/tempo-model.html

[^6]: Autonomie is the source of TEMPO’s inputs about electric vehicle characteristics for both current day and future scenarios

[^7]: 550,000 is the typical sample size for ResStock, indicating that these rows are likely to get sampled.
