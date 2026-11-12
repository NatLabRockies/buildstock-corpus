<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/3b_ResStockInputs_HVAC.md | section: Shared Systems | lines: 891-1221 -->
## Shared Systems

### Modeling Approach

Shared systems in ResStock are heating and cooling systems that provide heating or cooling to more than one housing unit in a single-family attached or multifamily building. The types of systems that we model are boiler baseboard and fan coil systems. This is an area flagged for future improvement since more complex systems exist in reality, including systems that provide both heating and hot water. The shared systems currently in ResStock can provide heating, cooling, or heating and cooling to the unit. The boiler baseboard systems are heating-only systems. Fan coil systems that only provide cooling are modeled as a mini-split heat pump in ResStock. In reality, these systems are fan coils connected to central chillers. Fan coils that provide heating and cooling are modeled as a shared boiler with a ductless fan coil in ResStock. Currently, in ResStock these shared systems are modeled as equivalent in-unit systems (with adjusted efficiencies), not shared systems connected to multiple housing units (this may change in the future). As a result central distribution losses associated with supplying the water to multiple units are not currently captured in ResStock’s shared system modeling.

Four input files determine the options and arguments for ResStock shared systems:

- HVAC Has Shared System

- HVAC Shared Efficiencies

- HVAC System is Faulted

- HVAC System is Scaled.

### HVAC Has Shared System

#### Description

The presence of an HVAC system shared by multiple housing units.

#### Distribution Data Source(s)

- The sample counts and sample weights are constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Geometry Building Type RECS

- HVAC Cooling Type

- HVAC Heating Type

- Vintage.

#### Options

Homes can be assigned to have shared cooling, shared heating, shared both heating and cooling, or no shared systems. No ResStock arguments are assigned based on this input file, but these options are used as dependencies in other ResStock input files, such as HVAC Shared Efficiencies, where arguments are assigned.

#### Distribution Assumption(s)

- Due to low sample sizes, the fallback rules are applied in following order:

  1.  Vintage: Vintage ACS 20-year bin

  2.  HVAC Cooling Type: Lump (1) Central AC and Ducted Heat Pump, and (2) Non-Ducted Heat Pump and None

  3.  HVAC Heating Type: Lump (1) Ducted Heating and Ducted Heat Pump, and (2) Non-Ducted Heat Pump and None

  4.  HVAC Cooling Type: Lump (1) Central AC and Ducted Heat Pump, and (2) Non-Ducted Heat Pump, Non-Ducted Heating, and None

  5.  HVAC Heating Type: Lump (1) Ducted Heating and Ducted Heat Pump, and (2) Non-Ducted Heat Pump, None, and Room AC

  6.  Vintage: Vintage pre-1960s and post 2000

  7.  Vintage: All vintages

- Ducted Heat Pump option (a non-shared system) assigned for both heating and cooling

- Non-Ducted Heat Pump option (a non-shared system) assigned for both heating and cooling.

### HVAC Shared Efficiencies

#### Description

The efficiency of a shared HVAC system.

#### Distribution Data Source(s)

- The sample counts and sample weights are constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Heating Fuel

- HVAC Has Shared System

#### Options

For homes with shared systems, ResStock models one option for Cooling-Only shared systems (Fan Coil, Cooling Only); two options for heating-only shared systems (Boiler Baseboards Heating Only, Electricity; and Boiler Baseboards Heating Only, Fuel); and two options for homes that have both heating and cooling shared (Fan Coil Heating and Cooling, Electricity; Fan Coil Heating and Cooling, Fuel). 89% of homes have no shared system.

For homes that have only a cooling shared system (and in-unit heating or no heating), this in nominally labeled as Fan Coil, Cooling only. However, ResStock currently approximates this as a mini-split heat pump instead of modeling a Fan Coil. The ResStock arguments for the placeholder are:

- `cooling_system_type`: mini-split

- `cooling_system_cooling_efficiency_type`: SEER

- `cooling_system_cooling_efficiency`: 13

- `cooling_system_cooling_capacity`: auto

- `cooling_system_cooling_autosizing_limit`: false

- `cooling_system_cooling_efficiency_type`: auto

- `cooling_system_is_ducted`: false

For homes with only heating shared (with cooling either in-unit or not installed), ResStock models two shared boilers with different fuel types (note: the `heating_system_fuel` argument is set by the Heating Fuel input file, which is why it’s not listed here).

The following arguments are constant across both options:

- `heating_system_heating_capacity`: auto

- `heating_system_heating_autosizing_limit`: auto

- `heating_system_fraction_heat_load_served`: 1

- `heating_system_has_flue_or_chimney`: auto.

Additionally, the shared heating system doesn’t use an air-source or geothermal heat pump, or a heat pump backup, but the following arguments are supplied since they are required arguments:

- `heat_pump_heating_efficiency_type`: none

- `heat_pump_heating_efficiency`: HSPF

- `heat_pump_cooling_efficiency_type`: 0

- `heat_pump_cooling_efficiency`: SEER

- `heat_pump_heating_capacity`: 0

- `heat_pump_heating_autosizing_limit`: auto

- `heat_pump_cooling_capacity`: auto

- `heat_pump_cooling_autosizing_limit`: auto

- `heat_pump_fraction_heat_load_served`: 1

- `heat_pump_fraction_cool_load_served`: 1

- `heat_pump_backup_type`: none

- `heat_pump_backup_heating_autosizing_limit`: auto

- `heat_pump_backup_fuel`: electricity

- `heat_pump_backup_heating_efficiency`: 1

- `heat_pump_backup_heating_capacity`: auto

- `heat_pump_sizing_methodology`: ACCA

- `heat_pump_backup_sizing_methodology`: auto

- `geothermal_loop_configuration`: none

- `geothermal_loop_borefield_configuration`: auto

- `geothermal_loop_loop_flow`: auto

- `geothermal_loop_boreholes_count`: auto

- `geothermal_loop_boreholes_length`: auto

- `geothermal_loop_boreholes_spacing`: auto

- `geothermal_loop_boreholes_diameter`: auto

- `geothermal_loop_grout_type`: auto

- `geothermal_loop_pipe_type`: auto

- `geothermal_loop_pipe_diameter`: auto.

<div id="table:hc_arg_def_hvac_shared_eff_heat" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `heating_system_type` | `heating_system_heating_efficiency` |
|:---|:---|:---|
| Boiler Baseboards Heating Only, Electricity | Shared Boiler w/ Baseboard | 1 |
| Boiler Baseboards Heating Only, Fuel | Shared Boiler w/ Baseboard | 0.78 |

The ResStock argument definitions set in the HVAC Shared Efficiencies characteristic for Shared Heating

</div>

For homes that have both heating and cooling shared, the arguments are a combination of the homes with shared cooling and the homes with shared heating. These options are labeled Fan Coil Heating and Cooling, but they are modeled as a central boiler and a mini-split heat pump. The following options are constant across both options:

Heating arguments:

- `heating_system_heating_capacity`: auto

- `heating_system_heating_autosizing_limit`: auto

- `heating_system_fraction_heat_load_served`: 1

- `heating_system_has_flue_or_chimney`: auto.

Cooling arguments:

- `cooling_system_type` mini-split

- `cooling_system_cooling_efficiency_type` SEER

- `cooling_system_cooling_efficiency` 13

- `cooling_system_cooling_capacity` auto

- `cooling_system_cooling_autosizing_limit` false

- `cooling_system_is_ducted` none.

Required but unused heating arguments:

- `heat_pump_type`: HSPF

- `heat_pump_heating_efficiency_type`: 0

- `heat_pump_heating_efficiency`: SEER

- `heat_pump_cooling_efficiency_type`: 0

- `heat_pump_cooling_efficiency`: auto

- `heat_pump_heating_capacity`: auto

- `heat_pump_heating_autosizing_limit`: auto

- `heat_pump_cooling_capacity`: auto

- `heat_pump_cooling_autosizing_limit`: auto

- `heat_pump_fraction_heat_load_served`: 1

- `heat_pump_fraction_cool_load_served`: 1

- `heat_pump_backup_type`: none

- `heat_pump_backup_heating_autosizing_limit`: auto

- `heat_pump_backup_fuel`: electricity

- `heat_pump_backup_heating_efficiency`: 1

- `heat_pump_backup_heating_capacity`: auto

- `heat_pump_sizing_methodology`: ACCA

- `heat_pump_backup_sizing_methodology`: auto

- `geothermal_loop_configuration`: none

- `geothermal_loop_borefield_configuration`: auto

- `geothermal_loop_loop_flow`: auto

- `geothermal_loop_boreholes_count`: auto

- `geothermal_loop_boreholes_length`: auto

- `geothermal_loop_boreholes_spacing`: auto

- `geothermal_loop_boreholes_diameter`: auto

- `geothermal_loop_grout_type`: auto

- `geothermal_loop_pipe_type`: auto

- `geothermal_loop_pipe_diameter`: auto.

<div id="table:hc_arg_def_hvac_shared_eff_both" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | Stock saturation | `heating_system_type` | `heating_system_heating_efficiency` |
|:---|:---|:---|:---|
| Fan Coil Heating and Cooling, Electricity | 1.3% | Shared Boiler w/ Ductless Fan Coil | 1 |
| Fan Coil Heating and Cooling, Fuel | 1.1% | Shared Boiler w/ Ductless Fan Coil | 0.78 |

The ResStock argument definitions set in the HVAC Shared Efficiencies characteristic for Shared Heating and Cooling

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC Shared Efficiencies characteristic”. See the OpenStudio-HPXML [Boiler-Shared](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#boiler-shared) or [Mini-Split Heat Pumps](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#mini-split-heat-pump) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_shared_eff" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `heating_system_type` | true |  | Choice | none, Furnace, WallFurnace, FloorFurnace, Boiler, ElectricResistance, Stove, SpaceHeater, Fireplace, Shared Boiler w/ Baseboard, Shared Boiler w/ Ductless Fan Coil | The type of heating system. Use 'none' if there is no heating system or if there is a heat pump serving a heating load. |
| `heating_system_heating_efficiency` | true | Frac | Double |  | The rated heating efficiency value of the heating system. |
| `heating_system_heating_capacity` | false | Btu/hr | Double |  | The output heating capacity of the heating system. |
| `heating_system_heating_autosizing_limit` | false | Btu/hr | Double |  | The maximum capacity limit applied to the auto-sizing methodology. If not provided, no limit is used. |
| `heating_system_fraction_heat_load_served` | true | Frac | Double |  | The heating load served by the heating system. |
| `cooling_system_type` | true |  | Choice | none, central air conditioner, room air conditioner, evaporative cooler, mini-split, packaged terminal air conditioner | The type of cooling system. Use 'none' if there is no cooling system or if there is a heat pump serving a cooling load. |
| `cooling_system_cooling_efficiency_type` | true |  | Choice | SEER, SEER2, EER, CEER | The efficiency type of the cooling system. System types central air conditioner and mini-split use SEER or SEER2. System types room air conditioner and packaged terminal air conditioner use EER or CEER. Ignored for system type evaporative cooler. |
| `cooling_system_cooling_efficiency` | true |  | Double |  | The rated efficiency value of the cooling system. Ignored for evaporative cooler. |
| `cooling_system_cooling_capacity` | false | Btu/hr | Double |  | The output cooling capacity of the cooling system. |
| `cooling_system_cooling_autosizing_limit` | false | Btu/hr | Double |  | The maximum capacity limit applied to the auto-sizing methodology. If not provided, no limit is used. |
| `cooling_system_is_ducted` | false |  | Boolean | auto, true, false | Whether the cooling system is ducted or not. Only used for mini-split and evaporative cooler. It’s assumed that central air conditioner is ducted, and room air conditioner and packaged terminal air conditioner are not ducted. |
| `heat_pump_type` | true |  | Choice | none, air-to-air, mini-split, ground-to-air, packaged terminal heat pump, room air conditioner with reverse cycle | The type of heat pump. Use 'none' if there is no heat pump. |
| `heat_pump_heating_efficiency_type` | true |  | Choice | HSPF, HSPF2, COP | The heating efficiency type of heat pump. System types air-to-air and mini-split use HSPF or HSPF2. System types ground-to-air, packaged terminal heat pump, and room air conditioner with reverse cycle use COP. |
| `heat_pump_heating_efficiency` | true |  | Double |  | The rated heating efficiency value of the heat pump. |
| `heat_pump_cooling_efficiency_type` | true |  | Choice | SEER, SEER2, EER, CEER | The cooling efficiency type of heat pump. System types air-to-air and mini-split use SEER or SEER2. System types ground-to-air, packaged terminal heat pump and room air conditioner with reverse cycle use EER. |
| `heat_pump_cooling_efficiency` | true |  | Double |  | The rated cooling efficiency value of the heat pump. |
| `heat_pump_heating_capacity` | false | Btu/hr | Double |  | The output heating capacity of the heat pump. |
| `heat_pump_heating_autosizing_limit` | false | Btu/hr | Double |  | The maximum capacity limit applied to the auto-sizing methodology. If not provided, no limit is used. |
| `heat_pump_cooling_capacity` | false | Btu/hr | Double |  | The output cooling capacity of the heat pump. |
| `heat_pump_cooling_autosizing_limit` | false | Btu/hr | Double |  | The maximum capacity limit applied to the auto-sizing methodology. If not provided, no limit is used. |
| `heat_pump_fraction_heat_load_served` | true | Frac | Double |  | The heating load served by the heat pump. |
| `heat_pump_fraction_cool_load_served` | true | Frac | Double |  | The cooling load served by the heat pump. |
| `heat_pump_backup_type` | true |  | Choice | none, integrated, separate | The backup type of the heat pump. If 'integrated', represents, e.g., built-in electric strip heat or dual-fuel integrated furnace. If 'separate', represents, e.g., electric baseboard or boiler based on the Heating System 2 specified below. Use 'none' if there is no backup heating. |
| `heat_pump_backup_heating_autosizing_limit` | false | Btu/hr | Double |  | The maximum capacity limit applied to the auto-sizing methodology if Backup Type is 'integrated'. If not provided, no limit is used. If Backup Type is 'separate', use Heating System 2: Heating Autosizing Limit. |
| `heat_pump_backup_fuel` | true |  | Choice | electricity, natural gas, fuel oil, propane | The backup fuel type of the heat pump. Only applies if Backup Type is 'integrated'. |
| `heat_pump_backup_heating_efficiency` | true |  | Double |  | The backup rated efficiency value of the heat pump. Percent for electricity fuel type. AFUE otherwise. Only applies if Backup Type is 'integrated'. |
| `heat_pump_backup_heating_capacity` | false | Btu/hr | Double |  | The backup output heating capacity of the heat pump. Only applies if Backup Type is 'integrated'. |
| `heat_pump_sizing_methodology` | false |  | Choice | auto, ACCA, HERS, MaxLoad | The auto-sizing methodology to use when the heat pump capacity is not provided. |
| `heat_pump_backup_sizing_methodology` | false |  | Choice | auto, emergency, supplemental | The auto-sizing methodology to use when the heat pump backup capacity is not provided. |
| `geothermal_loop_configuration` | false |  | Choice | auto, none, vertical | Configuration of the geothermal loop. Only applies to ground-to-air heat pump type. |
| `geothermal_loop_borefield_configuration` | false |  | Choice | auto, rectangle, open rectangle, C, L, U, lopsided U | Borefield configuration of the geothermal loop. Only applies to ground-to-air heat pump type. |
| `geothermal_loop_loop_flow` | false | gpm | Double |  | Water flow rate through the geothermal loop. Only applies to ground-to-air heat pump type. |
| `geothermal_loop_boreholes_count` | false | \# | Integer |  | Number of boreholes. Only applies to ground-to-air heat pump type. |
| `geothermal_loop_boreholes_length` | false | ft | Double |  | Average length of each borehole (vertical). Only applies to ground-to-air heat pump type. |
| `geothermal_loop_boreholes_spacing` | false | ft | Double | auto | Distance between bores. Only applies to ground-to-air heat pump type. |
| `geothermal_loop_boreholes_diameter` | false | in | Double | auto | Diameter of bores. Only applies to ground-to-air heat pump type. |
| `geothermal_loop_grout_type` | false |  | Choice | auto, standard, thermally enhanced | Grout type of the geothermal loop. Only applies to ground-to-air heat pump type. |
| `geothermal_loop_pipe_type` | false |  | Choice | auto, standard, thermally enhanced | Pipe type of the geothermal loop. Only applies to ground-to-air heat pump type. |
| `geothermal_loop_pipe_diameter` | false | in | Choice | auto, 3/4" pipe, 1" pipe, 1-1/4" pipe | Pipe diameter of the geothermal loop. Only applies to ground-to-air heat pump type. |
| `heating_system_has_flue_or_chimney` | true |  | String |  | Whether the heating system has a flue or chimney. |

The ResStock argument definitions set in the HVAC Shared Efficiencies characteristic

</div>

#### Distribution Assumption(s)

- Assume that all Heating and Cooling shared systems are fan coils in each housing unit served by a central chiller and boiler.

- Assume all Heating Only shared systems are hot water baseboards in each housing unit served by a central boiler.

- Assume all Cooling Only shared systems are fan coils in each housing unit served by a central chiller.

