<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3b_ResStockInputs_HVAC.md | section: Primary Heating | lines: 6-402 -->
## Primary Heating

### Modeling Approach

In ResStock, many characteristics assign arguments for the primary heating systems. The first characteristic assigned is the Heating Fuel. ResStock currently models electricity, natural gas, propane, fuel oil, wood heating, and homes without heating systems. The next characteristic that drives most of the other heating characteristics is HVAC Heating Type, where the system is specified as ducted (example: forced air furnace), non-ducted (example: baseboard boiler) systems, ducted heat pump, and non-ducted heat pumps (example: mini-splits). ResStock models the following heating systems: a ducted air-source heat pump (ASHP), electric baseboard, boilers, furnaces, wall/floor furnaces, and mini-split heat pumps (MSHPs). For most of these systems there are also a range of efficiency levels (example: an 96% AFUE gas furnace and an 80% AFUE gas furnace; note that AFUE stands for Annual Fuel Utilization Efficiency).

For housing units in multifamily and single-family attached buildings, ResStock also has models for heating systems that are shared between 2 or more units. For heating systems that serve multiple housing units, see Section “Shared Systems”. For discussion about heating setpoints see Section “Setpoints”.

Six input files specify the characteristics of the primary heating system:

- Heating Fuel

- HVAC Heating Type

- HVAC Heating Type and Fuel

- HVAC Heating Efficiency

- HVAC Has Zonal Electric Heating

- HVAC Heating Autosizing Factor.

The following sections discuss the characteristic distributions, data sources, conditional dependencies, options, assumptions, arguments, and argument values.

### Heating Fuel

#### Description

The fuel used for primary heating of the housing unit.

#### Distribution Data Source(s)

- 2019 5-year PUMS

- Alaska-specific distribution is based on Alaska Retrofit Information System (2008 to 2022), maintained by Alaska Housing Finance Corporation.

#### Direct Conditional Dependencies

- County and PUMA

- Geometry Building Type RECS

- Vintage.

#### Options

The Heating Fuel characteristic options are Electricity, Natural Gas, Propane, Fuel Oil, None, Other Fuel, and Wood. Other Fuel is currently modeled as wood energy. However, although ResStock simulates wood energy consumption for heating, current datasets do not publish data on heating with wood. The characteristic sets the `heating_system_fuel` ResStock argument (Table “Heating Fuel options and arguments that vary for each option”). The argument definition for the `heating_system_fuel` argument is in Table “The ResStock argument definitions set in the Heating Fuel characteristic”.

See the OpenStudio-HPXML [Heating Systems](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-heating-systems) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hf" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `heating_system_fuel` | true |  | Choice | electricity, natural gas, fuel oil, propane, wood, wood pellets, coal | The fuel type of the heating system. Ignored for ElectricResistance. |

The ResStock argument definitions set in the Heating Fuel characteristic

</div>

<div id="table:hc_opt_hf" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `heating_system_fuel` |
|:------------|:----------------------|
| Electricity | electricity           |
| Fuel Oil    | fuel oil              |
| Natural Gas | natural gas           |
| None        | natural gas           |
| Other Fuel  | wood                  |
| Propane     | propane               |
| Wood        | wood                  |

Heating Fuel options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

- In ACS, Heating Fuel is reported for occupied units only. By excluding Vacancy Status as a dependency, we assume vacant units share the same Heating Fuel distribution as occupied units. Where sample counts are less than 10, the State average distribution has been inserted. Prior to insertion, the following adjustments have been made to the state distribution so all rows have sample count \> 10: 1. Where sample counts \< 10 (which consists of Mobile Home and Single-Family Attached only), the Vintage ACS distribution is used instead of Vintage: \[CT, DE, ID, MD, ME, MT, ND, NE, NH, NV, RI, SD, UT, VT, WY\].

- Remaining Mobile Homes \< 10 are replaced by Single-Family Detached + Mobile Homes combined: \[DE, RI, SD, VT, WY, and all DC\].

- For Alaska, we are using a field in ARIS that lumps multifamily 2-4 units and multifamily 5+ units buildings together. Data from the American Community Survey are used to distribute between these two building types.

- For Alaska, all wood is modeled as cord wood.

- For Alaska, when heating uses more than one fuel, the fuel with highest consumption is considered the primary (heating) fuel, and fuel with second highest usage (provided it is at least 10% of total energy use across all fuels) is considered secondary (heating) fuel—except in case of electric heating, which is always assumed as primary. The rest of the fuels are ignored.

### HVAC Heating Type

#### Description

The presence and type of the primary heating system in the housing unit.

#### Distribution Data Source(s)

- U.S. EIA 2020 RECS microdata

- Alaska-specific distribution is based on Alaska Retrofit Information System (2008 to 2022), maintained by Alaska Housing Finance Corporation.

#### Direct Conditional Dependencies

- Geometry Building Type RECS

- Heating Fuel

- State

- Vintage.

#### Options

The options for the HVAC Heating Type characteristic are Ducted Heat Pump, Ducted Heating, Non-Ducted Heat Pump, Non-Ducted Heating, and None. No ResStock arguments are assigned based upon these options; instead the HVAC Heating Type informs other HVAC inputs (such as HVAC Heating Efficiency) that do have related ResStock arguments.

#### Distribution Assumption(s)

- Due to low sample sizes, fallback rules lumped together the following: (1) Heating fuel lump: Fuel oil, Propane, Wood, and Other Fuel, (2) Geometry building SF: Mobile, Single-family attached, Single-family detached, (3) Geometry building MF: Multifamily with 2-4 Units, Multifamily with 5+ Units, and (4) Vintage Lump: 20-yr bins.

- For Alaska, we are using a field in ARIS that lumps multifamily 2-4 units and multifamily 5+ units buildings together. Data from the American Community Survey are used to distribute between these two building types.

### HVAC Heating Type and Fuel

#### Description

The presence, type, and fuel of primary heating system.

#### Distribution Data Source(s)

- Calculated directly from other distributions.

#### Direct Conditional Dependencies

- Heating Fuel

- HVAC Heating Efficiency.

#### Options

The options are a combination of the specific heating systems in HVAC Heating Efficiency characteristic and the Heating Fuel characteristic. The dependency combinations are directly mapped to the options in this characteristic. There are no ResStock arguments assigned directly from this input.

#### Distribution Assumption(s)

No assumptions were made.

### HVAC Heating Efficiency

#### Description

The presence and efficiency of the primary heating system in the housing unit. This is the main input that determines the modeled heating system.

#### Distribution Data Source(s)

- The sample counts and sample weights are constructed using U.S. EIA 2020 RECS microdata.

- Shipment data based on ENERGY STAR ASHP shipments data and ENERGY STAR furnace shipments data. Efficiency data from Home Energy Saver are combined with age of equipment data from RECS.

- Alaska-specific distribution is based on Alaska Retrofit Information System (2008 to 2022), maintained by Alaska Housing Finance Corporation.

#### Direct Conditional Dependencies

- Custom State

- Heating Fuel

- HVAC Has Shared System

- HVAC Heating Type

- Vintage.

#### Options

The options of the HVAC Heating Efficiency characteristic assigns the heating system type and efficiency of the heating system. The system types are ducted ASHPs, electric baseboard, electric boiler, electric furnace, electric wall furnace, fuel boiler, fuel furnace, fuel wall/floor furnace, MSHPs, none, and shared heating. The Shared Systems option does not specify any arguments. Shared Systems designate heating systems that serve multiple housing units in a multifamily building, and they have their own characteristics that set the arguments; see Section “Shared Systems”. The HVAC Heating Efficiency characteristic sets the arguments listed in the argument definition table (Table “The ResStock argument definitions set in the HVAC Heating Efficiency characteristic”). See the OpenStudio-HPXML [Heating System](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-heating-systems) documentation for the available HPXML schema elements, default values, and constraints.

The following arguments are always set to “auto” for all systems:

- `heating_system_heating_capacity`

- `heating_system_heating_autosizing_limit`

- `heat_pump_heating_capacity`

- `heat_pump_heating_autosizing_limit`

- `heat_pump_cooling_capacity`

- `heat_pump_cooling_autosizing_limit`

- `heat_pump_backup_heating_autosizing_limit`

- `heat_pump_backup_heating_capacity`

- `heat_pump_backup_sizing_methodology`

- `geothermal_loop_borefield_configuration`

- `geothermal_loop_loop_flow`

- `geothermal_loop_boreholes_count`

- `geothermal_loop_boreholes_length`

- `geothermal_loop_boreholes_spacing`

- `geothermal_loop_boreholes_diameter`

- `geothermal_loop_grout_type`

- `geothermal_loop_pipe_type`

- `geothermal_loop_pipe_diameter` and

- `heating_system_has_flue_or_chimney`.

The `heating_system_fraction_heat_load_served`, `heat_pump_fraction_heat_load_served`, `heat_pump_fraction_cool_load_served`, and `heat_pump_backup_heating_efficiency` arguments are always set to 1 for all systems.

The `heat_pump_heating_efficiency_type` is always HSPF (Heating Seasonal Performance Factor) for all systems. The `heat_pump_cooling_efficiency_type` is always SEER (Seasonal Energy Efficiency Ratio) for all systems. The `heat_pump_sizing_methodology` is always ACCA (Air Conditioning Contractors of America) for all systems in the ResStock baseline.

The `heat_pump_backup_use_existing_system` and `heat_pump_sizing_is_duct_limited` arguments are applicable for heat pump upgrades only. They are not used in baseline models.

<div id="table:hc_arg_def_ht_eff" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `heating_system_type` | true |  | Choice | None, Furnace, WallFurnace, FloorFurnace, Boiler, ElectricResistance, Stove, SpaceHeater, Fireplace, Shared Boiler w/ Baseboard, Shared Boiler w/ Ductless Fan Coil | The type of heating system. Use 'none' if there is no heating system or if there is a heat pump serving a heating load. |
| `heating_system_heating_efficiency` | true | Frac | Double |  | The rated heating efficiency value of the heating system. |
| `heating_system_heating_capacity` | false | Btu/hr | Double |  | The output heating capacity of the heating system. |
| `heating_system_heating_autosizing_limit` | false | Btu/hr | Double |  | The maximum capacity limit applied to the auto-sizing methodology. If not provided, no limit is used. |
| `heating_system_fraction_heat_load_served` | true | Frac | Double |  | The heating load served by the heating system. |
| `heating_system_pilot_light` | false | Btuh | Double |  | The fuel usage of the pilot light. Applies only to Furnace, WallFurnace, FloorFurnace, Stove, Boiler, and Fireplace with non-electric fuel type. If not provided, assumes no pilot light. |
| `heat_pump_type` | true |  | Choice | none, air-to-air, mini-split, ground-to-air, packaged terminal heat pump, room air conditioner with reverse cycle | The type of heat pump. Use 'none' if there is no heat pump. |
| `heat_pump_heating_efficiency_type` | true |  | Choice | HSPF, HSPF2, coefficient of performance (COP) | The heating efficiency type of heat pump. System types air-to-air and mini-split use HSPF or HSPF2. System types ground-to-air, packaged terminal heat pump, and room air conditioner with reverse cycle use COP. |
| `heat_pump_heating_efficiency` | true |  | Double |  | The rated heating efficiency value of the heat pump. |
| `heat_pump_cooling_efficiency_type` | true |  | Choice | SEER, SEER2, energy efficiency ratio (EER), combined energy efficiency ratio (CEER) | The cooling efficiency type of heat pump. System types air-to-air and mini-split use SEER or SEER2. System types ground-to-air, packaged terminal heat pump and room air conditioner with reverse cycle use EER. |
| `heat_pump_cooling_efficiency` | true |  | Double |  | The rated cooling efficiency value of the heat pump. |
| `heat_pump_cooling_compressor_type` | false |  | Choice | auto, single stage, two stage, variable speed | The compressor type of the heat pump. Only applies to air-to-air and mini-split. If not provided, the OS-HPXML default (see [Air-to-Air Heat Pump](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#air-to-air-heat-pump), [Mini-Split Heat Pump](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#mini-split-heat-pump)) is used. |
| `heat_pump_cooling_sensible_heat_fraction` | false | Frac | Double | auto | The sensible heat fraction of the heat pump. If not provided, the OS-HPXML default (see [Air-to-Air Heat Pump](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#air-to-air-heat-pump), [Mini-Split Heat Pump](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#mini-split-heat-pump), [Packaged Terminal Heat Pump](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#packaged-terminal-heat-pump), [Room Air Conditioner w/ Reverse Cycle](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#room-air-conditioner-w-reverse-cycle), [Ground-to-Air Heat Pump](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#ground-to-air-heat-pump)) is used. |
| `heat_pump_heating_capacity` | false | Btu/hr | Double |  | The output heating capacity of the heat pump. |
| `heat_pump_heating_autosizing_limit` | false | Btu/hr | Double |  | The maximum capacity limit applied to the auto-sizing methodology. If not provided, no limit is used. |
| `heat_pump_heating_capacity_retention_fraction` | false | Frac | Double | auto | The output heating capacity of the heat pump at a user-specified temperature (e.g., 17° F or 5° F) divided by the above nominal heating capacity. Applies to all heat pump types except ground-to-air. |
| `heat_pump_heating_capacity_retention_temp` | false | deg-F | Double |  | The user-specified temperature (e.g., 17° F or 5° F) for the above heating capacity retention fraction. Applies to all heat pump types except ground-to-air. Required if the Heating Capacity Retention Fraction is provided. |
| `heat_pump_cooling_capacity` | false | Btu/hr | Double |  | The output cooling capacity of the heat pump. |
| `heat_pump_cooling_autosizing_limit` | false | Btu/hr | Double |  | The maximum capacity limit applied to the auto-sizing methodology. If not provided, no limit is used. |
| `heat_pump_fraction_heat_load_served` | true | Frac | Double |  | The heating load served by the heat pump. |
| `heat_pump_fraction_cool_load_served` | true | Frac | Double |  | The cooling load served by the heat pump. |
| `heat_pump_compressor_lockout_temp` | false | deg-F | Double | auto | The temperature below which the heat pump compressor is disabled. If both this and Backup Heating Lockout Temperature are provided and use the same value, it essentially defines a switchover temperature (for, e.g., a dual-fuel heat pump). Applies to all heat pump types other than ground-to-air. |
| `heat_pump_backup_type` | true |  | Choice | none, integrated, separate | The backup type of the heat pump. If 'integrated', represents e.g., built-in electric strip heat or dual-fuel integrated furnace. If 'separate', represents e.g., electric baseboard or boiler based on the Heating System 2 specified below. Use 'none' if there is no backup heating. |
| `heat_pump_backup_heating_autosizing_limit` | false | Btu/hr | Double |  | The maximum capacity limit applied to the auto-sizing methodology if Backup Type is 'integrated'. If not provided, no limit is used. If Backup Type is 'separate', use Heating System 2: Heating Autosizing Limit. |
| `heat_pump_backup_fuel` | true |  | Choice | electricity, natural gas, fuel oil, propane | The backup fuel type of the heat pump. Only applies if Backup Type is 'integrated'. |
| `heat_pump_backup_heating_efficiency` | true |  | Double |  | The backup rated efficiency value of the heat pump. Percent for electricity fuel type. AFUE otherwise. Only applies if Backup Type is 'integrated'. |
| `heat_pump_backup_heating_capacity` | false | Btu/hr | Double |  | The backup output heating capacity of the heat pump. If not provided, the OS-HPXML autosized default (see [Backup](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#backup)) is used. Only applies if Backup Type is 'integrated'. |
| `heat_pump_backup_heating_lockout_temp` | false | deg-F | Double | auto | The temperature above which the heat pump backup system is disabled. If both this and Compressor Lockout Temperature are provided and use the same value, it essentially defines a switchover temperature (for, e.g., a dual-fuel heat pump). Applies for both Backup Type of 'integrated' and 'separate'. |
| `heat_pump_backup_use_existing_system` | false |  | Boolean | true, false | Whether the heat pump uses the existing system as backup. This argument is only applicable for heat pump upgrades. |
| `heat_pump_sizing_methodology` | false |  | Choice | auto, ACCA, HERS, MaxLoad | The auto-sizing methodology to use when the heat pump capacity is not provided. |
| `heat_pump_sizing_is_duct_limited` | false |  | Boolean | true, false | Whether the (ducted) heat pump has an upper limit for autosized heating/cooling capacities and an adjusted blower fan (W/CFM) efficiency value. This argument is only applicable for heat pump upgrades. |
| `heat_pump_backup_sizing_methodology` | false |  | Choice | auto, emergency, supplemental | The auto-sizing methodology to use when the heat pump backup capacity is not provided. |
| `heat_pump_is_ducted` | false |  | Boolean | auto, true, false | Whether the heat pump is ducted or not. Only used for mini-split. It is assumed that air-to-air and ground-to-air are ducted, and packaged terminal heat pump and room air conditioner with reverse cycle are not ducted. If not provided, assumes not ducted. |
| `heat_pump_crankcase_heater_watts` | false | W | Double | auto | Heat pump crankcase heater power consumption in watts. Applies only to air-to-air, mini-split, packaged terminal heat pump, and room air conditioner with reverse cycle. |
| `geothermal_loop_configuration` | false |  | Choice | auto, none, vertical | Configuration of the geothermal loop. Only applies to ground-to-air heat pump type. |
| `geothermal_loop_borefield_configuration` | false |  | Choice | auto, rectangle, open rectangle, C, L, U, lopsided U | Borefield configuration of the geothermal loop. Only applies to ground-to-air heat pump type. |
| `geothermal_loop_loop_flow` | false | gpm | Double |  | Water flow rate through the geothermal loop. Only applies to ground-to-air heat pump type. |
| `geothermal_loop_boreholes_count` | false | \# | Integer |  | Number of boreholes. Only applies to ground-to-air heat pump type. If not provided, the OS-HPXML autosized default (see [HPXML Geothermal Loops](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-geothermal-loops)) is used. |
| `geothermal_loop_boreholes_length` | false | ft | Double |  | Average length of each borehole (vertical). Only applies to ground-to-air heat pump type. |
| `geothermal_loop_boreholes_spacing` | false | ft | Double | auto | Distance between bores. Only applies to ground-to-air heat pump type. |
| `geothermal_loop_boreholes_diameter` | false | in | Double | auto | Diameter of bores. Only applies to ground-to-air heat pump type. |
| `geothermal_loop_grout_type` | false |  | Choice | auto, standard, thermally enhanced | Grout type of the geothermal loop. Only applies to ground-to-air heat pump type. |
| `geothermal_loop_pipe_type` | false |  | Choice | auto, standard, thermally enhanced | Pipe type of the geothermal loop. Only applies to ground-to-air heat pump type. |
| `geothermal_loop_pipe_diameter` | false | in | Choice | auto, 3/4" pipe, 1" pipe, 1-1/4" pipe | Pipe diameter of the geothermal loop. Only applies to ground-to-air heat pump type. |
| `heating_system_has_flue_or_chimney` | true |  | String |  | Whether the heating system has a flue or chimney. |

The ResStock argument definitions set in the HVAC Heating Efficiency characteristic

</div>

For heat pump options and arguments that vary across the heat pump options, see Table “HVAC Heating Efficiency heat pump options and arguments that vary for each option”. The `heating_system_type` argument is none, `heating_system_heating_efficiency` is 0 and not used. The `heat_pump_backup_type` is set to integrated. The `heating_system_pilot_light` argument is not specified. The `heat_pump_cooling_compressor_type`, `heat_pump_cooling_sensible_heat_fraction`, `heat_pump_heating_capacity`, `heat_pump_heating_autosizing_limit`, `heat_pump_compressor_lockout_temp`, `heat_pump_backup_heating_lockout_temp`, and `heat_pump_crankcase_heater_watts` are set to “auto.”

<div id="table:hc_opt_ht_eff_hp" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `heat_pump_type` | `heat_pump_heating_efficiency` | `heat_pump_cooling_efficiency` | `heat_pump_heating_capacity_retention_fraction` | `heat_pump_heating_capacity_retention_temp` | `heat_pump_is_ducted` |
|:---|:---|:---|:---|:---|:---|:---|
| ASHP, SEER 10, 6.2 HSPF | air-to-air | 6.2 | 10 | auto | auto |  |
| ASHP, SEER 13, 7.7 HSPF | air-to-air | 7.7 | 13 | auto | auto |  |
| ASHP, SEER 15, 8.5 HSPF | air-to-air | 8.5 | 15 | auto | auto |  |
| MSHP, SEER 14.5, 8.2 HSPF | mini-split | 8.2 | 14.5 | 0.25 | -5 | false |
| MSHP, SEER 29.3, 14 HSPF | mini-split | 14 | 29.3 | 0.5 | -15 | false |

HVAC Heating Efficiency heat pump options and arguments that vary for each option

</div>

For other heating systems the options and arguments that vary across these options, see Table “HVAC Heating Efficiency non-heat pump heating system options and arguments that vary for each option”. The `heat_pump_type` and the `heat_pump_backup_type` arguments are set to none. The `heat_pump_heating_efficiency` and `heat_pump_cooling_efficiency` arguments are set to 0 and are not used. The `heat_pump_cooling_compressor_type`, `heat_pump_cooling_sensible_heat_fraction`, `heat_pump_heating_capacity_retention_fraction`, `heat_pump_heating_capacity_retention_temp`, `heat_pump_compressor_lockout_temp`, `heat_pump_backup_heating_lockout_temp`, `heat_pump_is_ducted`, and `heat_pump_crankcase_heater_watts` are not set.

<div id="table:hc_opt_ht_eff_oth" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `heating_system_type` | `heating_system_heating_efficiency` | `heating_system_pilot_light` |
|:---|:---|:---|:---|
| Electric Baseboard, 100% Efficiency | ElectricResistance | 1 |  |
| Electric Boiler, 100% AFUE | Boiler | 1 |  |
| Electric Furnace, 100% AFUE | Furnace | 1 |  |
| Electric Wall Furnace, 100% AFUE | WallFurnace | 1 |  |
| Fuel Boiler, 76% AFUE | Boiler | 0.76 | auto |
| Fuel Boiler, 80% AFUE | Boiler | 0.8 | auto |
| Fuel Boiler, 90% AFUE | Boiler | 0.9 | auto |
| Fuel Furnace, 60% AFUE | Furnace | 0.6 | auto |
| Fuel Furnace, 76% AFUE | Furnace | 0.76 | auto |
| Fuel Furnace, 80% AFUE | Furnace | 0.8 | auto |
| Fuel Wall/Floor Furnace, 60% AFUE | WallFurnace | 0.6 | auto |
| Fuel Wall/Floor Furnace, 68% AFUE | WallFurnace | 0.68 | auto |
| None | none | 0 |  |

HVAC Heating Efficiency non-heat pump heating system options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

- If a house has a wall furnace with fuel other than natural gas, the efficiency level based on natural gas from the Home Energy Saver weighted shipment efficiencies data is assigned.

- If a house has a heat pump with fuel other than electricity (presumed dual-fuel heat pump), the heating type is assumed to be furnace and not heat pump.

- The ENERGY STAR shipment volume for boiler was not available, so ENERGY STAR shipment volume for furnaces was used instead.

- Due to low sample size for some categories, the HVAC Has Shared System categories ‘Cooling Only’ and ‘None’ are combined for the purpose of querying Heating Efficiency distributions.

- For ‘other’ heating system types, we assign them to Electric Baseboard if fuel is Electric, and assign them to Wall/Floor Furnace if fuel is natural gas, fuel oil, or propane.

- For Other Fuel and Wood, the lowest efficiency systems are assumed.

- For Alaska, we are using a field in ARIS that lumps multifamily 2-4 units and multifamily 5+ units buildings together. Data from the American Community Survey are used to distribute between these two building types.

- For Alaska, electric space heaters are modeled as electric baseboards.

- For Alaska, Toyo/monitor direct-vent devices and other fuel space heaters are not modeled.

- For Alaska, fireplace and stoves are not modeled.

- For Alaska, all heat pumps (including geothermal) are assumed to be non-ducted ASHPs.

### HVAC Has Zonal Electric Heating

#### Description

Presence of electric baseboard heating.

#### Distribution Data Source(s)

- This characteristic is a direct mapping from the HVAC Heating Efficiency characteristic.

#### Direct Conditional Dependencies

- HVAC Heating Efficiency.

#### Options

The options for the HVAC Heating Efficiency are “Yes” and “No.” The system that is assigned the “Yes” option is Electric Baseboard, 100% Efficiency. All other systems are assigned the “No” option. No ResStock arguments are directly assigned from this input file.

#### Distribution Assumption(s)

No assumptions are made. The characteristic options are a direct map from the HVAC Heating Efficiency characteristic.

### HVAC Heating Autosizing Factor

#### Description

The heating capacity and airflow scaling factor applied to the auto-sizing methodology. This is not currently used in baseline.

#### Distribution Data Source(s)

- Engineering judgment.

#### Direct Conditional Dependencies

- HVAC Heating Efficiency

- HVAC System is Scaled.

#### Options

There are two options in the baseline: “None” and “40% Oversized.” Only the “None” option is used. HVAC sizing follows ACCA Manual J and Manual S. There is no additional oversizing or undersizing the capacity and airflow of the HVAC system. This capability is not currently being used in ResStock. The characteristic assigns the `heating_system_heating_autosizing_factor`, `heat_pump_heating_autosizing_factor`, `heat_pump_backup_heating_autosizing_factor`, and `heating_system_2_heating_autosizing_factor` ResStock arguments. All are left blank for the “None” option and are not used. For argument definitions see Table “The ResStock argument definitions set in the HVAC Heating Autosizing Factor characteristic”.

<div id="table:hc_arg_def_ht_auto_size" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `heating_system_heating_autosizing_factor` | false |  | Double |  | The capacity scaling factor applied to the auto-sizing methodology. If not provided, 1.0 is used. |
| `heat_pump_heating_autosizing_factor` | false |  | Double |  | The capacity scaling factor applied to the auto-sizing methodology. If not provided, 1.0 is used. |
| `heat_pump_backup_heating_autosizing_factor` | false |  | Double |  | The capacity scaling factor applied to the auto-sizing methodology if Backup Type is 'integrated'. If not provided, 1.0 is used. If Backup Type is 'separate', use Heating System 2: Heating Autosizing Factor. |
| `heating_system_2_heating_autosizing_factor` | false |  | Double |  | The capacity scaling factor applied to the auto-sizing methodology. If not provided, 1.0 is used. |

The ResStock argument definitions set in the HVAC Heating Autosizing Factor characteristic

</div>

#### Distribution Assumption(s)

No assumptions are made. The capability is not used.

