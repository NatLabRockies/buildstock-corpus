<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Water Heaters | lines: 8-411 -->
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

