<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 -->
# HVAC

Heating, ventilating, and air conditioning (HVAC) is the leading driver of residential energy use in the United States. System configurations for providing these space-conditioning services vary, but can be related. The same equipment can provide both heating and cooling, there can be separate systems, or there can be multiple pieces of equipment providing the same service. In ResStock the input relationships between these files are complex because of these nuances and because of the structure of the surveys they’re built upon. In this section, we’ll cover the major HVAC types modeled in ResStock by service/component: Primary Heating, Secondary Heating, Cooling, Shared Systems, Setpoints, Ducts, HVAC Installation Quality, and Ventilation.

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

## Secondary Heating

### Modeling Approach

Many homes use a secondary heating source in addition to their primary heating source. Common examples include electric space heaters or a wood stove. ResStock has the capability to include these secondary heating sources in upgrade scenarios. Currently only Alaska is modeled with any use of secondary heating in the baseline. At any given time step the heating load needs to be met. A fraction of this load is assigned to the secondary system. This approach has some limitations. The secondary system is typically a second system supplying heating. They are often turned on during the coldest times of the coldest periods and may be off for a good portion of the year. We currently do not model this behavior in ResStock.

The next sections discuss the building stock characteristic distributions, their options, assumptions, conditional dependencies, arguments, and argument values assigned in these characteristics.

### HVAC Secondary Heating Type

#### Description

The efficiency and type of the secondary heating system.

#### Distribution Data Source(s)

- Alaska-specific distribution is based on Alaska Retrofit Information System (2008 to 2022), maintained by the Alaska Housing Finance Corporation. Not implemented in baseline for other states.

#### Direct Conditional Dependencies

- Custom State

- Geometry Building Type RECS

- HVAC Heating Type

- HVAC Secondary Heating Fuel

- Vintage.

#### Options

Only homes in Alaska have secondary heating, so most housing units receive a “None” assignment. No ResStock arguments are assigned from this input file.

#### Distribution Assumption(s)

- For Alaska, we are using a field in ARIS that lumps multifamily 2-4 units and multifamily 5+ units buildings together. Data from the American Community Survey are used to distribute between these two building types.

- Ducted heating or heat pump cannot have ducted secondary heating.

- For Alaska, all heat pumps are assumed to be non-ducted mini-splits.

- For Alaska, electricity cannot be a secondary heating fuel, therefore no secondary heating type.

### HVAC Secondary Heating Fuel

#### Description

Secondary Heating Fuel for the housing unit.

#### Distribution Data Source(s)

- Alaska-specific distribution is based on Alaska Retrofit Information System (2008 to 2022), maintained by Alaska Housing Finance Corporation. Secondary heating is not currently implemented in baseline for other states.

#### Direct Conditional Dependencies

- County

- Geometry Building Type RECS

- Vintage

#### Options

The options for the secondary heating fuel are the fuels used in the secondary HVAC system (Table “HVAC Secondary Heating Fuel options and arguments that vary for each option”).

<div id="table:hc_opt_hvac_sec_heat_fuel" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `heating_system_2_fuel` |
|:------------|:------------------------|
| Electricity | electricity             |
| Fuel Oil    | fuel oil                |
| Natural Gas | natural gas             |
| None        | electricity             |
| Other Fuel  | wood                    |
| Propane     | propane                 |
| Wood        | wood                    |

HVAC Secondary Heating Fuel options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC Secondary Heating Fuel characteristic”. See the OpenStudio-HPXML [heating systems](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-heating-systems) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_sec_heat_fuel" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Type | Choices | Description |
|:---|:---|:---|:---|:---|
| `heating_system_2_fuel` | true | Choice | electricity, natural gas, fuel oil, propane, wood, wood pellets, coal | The fuel type of the second heating system. Ignored for ElectricResistance. |

The ResStock argument definitions set in the HVAC Secondary Heating Fuel characteristic

</div>

#### Distribution Assumption(s)

- For Alaska, we are using a field in ARIS that lumps multifamily 2-4 units and multifamily 5+ units buildings together. Data from the American Community Survey are used to distribute between these two building types.

- For Alaska, all wood is modeled as cord wood.

- For Alaska, when heating uses more than one fuel, the fuel with highest consumption is considered the primary (heating) fuel, and fuel with second highest usage (provided it is at least 10% of total energy use across all fuels) is considered secondary (heating) fuel—except in case of electric heating, which is always assumed as primary (i.e., secondary heating fuel cannot be electricity). The rest of the fuels are ignored.

### HVAC Secondary Heating Efficiency

#### Description

The efficiency of the secondary heating system.

#### Distribution Data Source(s)

- Alaska-specific distribution is based on Alaska Retrofit Information System (2008 to 2022), maintained by Alaska Housing Finance Corporation. Secondary heating is not currently implemented in baseline for other states.

#### Direct Conditional Dependencies

- Custom State

- Geometry Building Type RECS

- HVAC Secondary Heating Fuel

- Vintage.

#### Options

The options of the HVAC Secondary Heating Efficiency are the secondary heating system efficiency (Table “HVAC Secondary Heating Efficiency options and arguments that vary for each option”). The Shared Heating option is used for Shared Heating. The “None” option is used for systems without secondary heating systems. The characteristic sets the following ResStock arguments to “auto”: `heating_system_2_heating_capacity`, `heating_system_2_heating_autosizing_limit`, and `heating_system_2_has_flue_or_chimney`.

<div id="table:hc_opt_hvac_sec_eff" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `heating_system_2_type` | `heating_system_2_heating_efficiency` |
|:---|:---|:---|
| Fuel Boiler, 76% AFUE | Boiler | 0.76 |
| Fuel Boiler, 80% AFUE | Boiler | 0.8 |
| Fuel Boiler, 90% AFUE | Boiler | 0.90 |
| Fuel Furnace, 60% AFUE | Furnace | 0.6 |
| Fuel Furnace, 76% AFUE | Furnace | 0.76 |
| Fuel Furnace, 80% AFUE | Furnace | 0.8 |
| Fuel Furnace, 92.5% AFUE | Furnace | 0.925 |
| None | none | 0 |
| Shared Heating | none | 0 |

HVAC Secondary Heating Efficiency options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC Secondary Heating Efficiency characteristic”. See the OpenStudio-HPXML [Heating Systems](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-heating-systems) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_sec_eff" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `heating_system_2_type` | true |  | Choice | None, Furnace, WallFurnace, FloorFurnace, Boiler, ElectricResistance, Stove, SpaceHeater, Fireplace | The type of the second heating system. If a heat pump is specified and the backup type is ’separate’, this heating system represents ’separate’ backup heating. For ducted heat pumps where the backup heating system is a ’Furnace’, the backup would typically be characterized as ’integrated’ in that the furnace and heat pump share the same distribution system and blower fan; a ’Furnace’ as ’separate’ backup to a ducted heat pump is not supported. |
| `heating_system_2_heating_efficiency` | true | Frac | Double |  | The rated heating efficiency value of the second heating system. |
| `heating_system_2_heating_capacity` | false | Btu/hr | Double |  | The output heating capacity of the second heating system. |
| `heating_system_2_heating_autosizing_limit` | false | Btu/hr | Double |  | The maximum capacity limit applied to the auto-sizing methodology. If not provided, no limit is used. |
| `heating_system_2_has_flue_or_chimney` | true |  | String |  | Whether the second heating system has a flue or chimney. |

The ResStock argument definitions set in the HVAC Secondary Heating Efficiency characteristic

</div>

#### Distribution Assumption(s)

- For Alaska, we are using a field in ARIS that lumps multifamily 2-4 units and multifamily 5+ units buildings together. Data from the American Community Survey are used to distribute between these two building types.

- For Alaska, electricity cannot be a secondary heating fuel, therefore no secondary heating efficiency.

- For Alaska, Toyo/monitor direct-vent devices and other fuel space heaters are not modeled.

- For Alaska, fireplace and stoves are not modeled.

### HVAC Secondary Heating Partial Space Conditioning

#### Description

The fraction of heating load served by secondary heating system. The remainder is served by the primary heating system.

#### Distribution Data Source(s)

- Alaska-specific distribution is based on Alaska Retrofit Information System (2008 to 2022), maintained by Alaska Housing Finance Corporation. Secondary heating partial space conditioning is not currently implemented in baseline for other states.

#### Direct Conditional Dependencies

- Custom State

- HVAC Secondary Heating Fuel

- HVAC Secondary Heating Type

- Vintage.

#### Options

The options are the fraction of the load served for the secondary heating system (Table “HVAC Secondary Heating Partial Space Conditioning options and arguments that vary for each option”). The characteristic sets the `heating_system_2_fraction_heat_load_served` ResStock argument.

<div id="table:hc_opt_hvac_sec_par" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `heating_system_2_fraction_heat_load_served` |
|:------------|:---------------------------------------------|
| 0%          | 0                                            |
| 10%         | 0.1                                          |
| 20%         | 0.2                                          |
| 30%         | 0.3                                          |
| 40%         | 0.4                                          |
| 49%         | 0.49                                         |

HVAC Secondary Heating Partial Space Conditioning options and arguments that vary for each option

</div>

For the argument definitions, see Table “HVAC Secondary Heating Partial Space Conditioning options and arguments that vary for each option”. See the OpenStudio-HPXML [Heating Systems](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-heating-systems) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:arg_def_hvac_sec_par" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `heating_system_2_fraction_heat_load_served` | true | Frac | Double | The heat load served fraction of the second heating system. Ignored if this heating system serves as a backup system for a heat pump. |

HVAC Secondary Heating Partial Space Conditioning options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

- For Alaska, we are using a field in ARIS that lumps multifamily 2-4 units and multifamily 5+ units buildings together. Data from the American Community Survey are used to distribute between these two building types.

- For Alaska, the fraction of the load served by the secondary heating system is calculated as the ratio of annual energy used by secondary fuel and annual energy used by secondary and primary fuel.

## Cooling

### Modeling Approach

ResStock models various cooling equipment such as central air conditioners, room air conditioners, and heat pumps. Evaporative (swamp) coolers are an option as a cooling type but are not currently modeled. In ResStock, the cooling system is assigned after the heating system, so that if the heating system is a heat pump, the cooling system is also set to a heat pump. Central air conditioners are ducted systems; room air conditioners are equipment that often are in a window or mounted on the wall. Both room air conditioners and central air conditioners sometimes cool only a fraction of the floor area (more common with room air conditioners). This is represented by assigning a fraction of the cooling load to the cooling system. Heat pumps are assumed to serve the 100% of the cooling load. ResStock also varies the efficiency of the cooling system to represent newer, more efficient systems along with older, less efficient systems.

Three input files inform cooling system selection in ResStock:

- HVAC Cooling Type

- HVAC Cooling Efficiency

- HVAC Cooling Partial Space Conditioning.

Additionally, HVAC Cooling Autosizing Factor is related to cooling, but is not currently used in the ResStock baseline.

### HVAC Cooling Type

#### Description

The presence and type of primary cooling system in the housing unit.

#### Distribution Data Source(s)

- U.S. EIA 2020 RECS microdata.

- Alaska-specific distribution is based on Alaska Retrofit Information System (2008 to 2022), maintained by Alaska Housing Finance Corporation.

#### Direct Conditional Dependencies

- Geometry Building Type RECS

- HVAC Heating Type

- State

- Vintage ACS.

#### Options

The options of HVAC Cooling Type are Central AC, Ducted Heat Pump, Evaporative or Swamp Cooler, Non-Ducted Heat Pump, None, and Room AC. The options do not assign any ResStock arguments but are used as dependencies in other characteristics.

#### Distribution Assumption(s)

- Due to low sample sizes, fallback rules were applied, with coarsening of (1) HVAC Heating type: Non-ducted heating and None, (2) Geometry building SF: Mobile, Single-family attached, Single-family detached, (3) Geometry building MF: Multifamily with 2-4 Units, Multifamily with 5+ Units, (4) Vintage Lump: 20-yr bins.

- Homes having ducted heat pump for heating and electricity fuel are assumed to have ducted heat pump for cooling (separating from central AC category).

- Homes having non-ducted heat pump for heating are assumed to have non-ducted heat pump for cooling.

- For Hawaii, central air conditioning saturation is from RECS 2020 by heating type, ignoring all other dependencies

- For Hawaii, Non-Ducted Heat Pump saturation is underestimated because ResStock does not currently allow cooling-only Non-Ducted Heat Pumps. These samples are modeled as Room ACs

- For Alaska, we are using a field in ARIS that lumps multifamily 2-4 units and multifamily 5+ units buildings together. Data from the American Community Survey are used to distribute between these two building types.

- For Alaska, we are not modeling any central and room AC.

- For Alaska, cooling systems are never shared.

- Hawaii does not follow the same fallback rules. All distributions are custom adjusted so that state-level central air-conditioning saturation matches the state-level saturation in RECS2020.

### HVAC Cooling Efficiency

#### Description

The presence and efficiency of primary cooling system in the housing unit. In the assumptions heat pumps (both ducted and non ducted) are assumed to serve for both heating and cooling. In the RECS2020 survey that cooling and heating technologies are based on, it was recently discoved that some samples reported None for heating, but heat pump for cooling (especialy non-ducted heat pumps). This is especially prevalent in hot climates with low cooling saturation. In ResStock, those samples with None heating and non ducted heat pump cooling in the survey are currently not being counted as having heat pumps. This is a known issue that will be addressed in a future release. In Hawaii, where this issue is most prevalent, the Room AC saturation has been increased to account for the undercounting of non-ducted heat pumps.

#### Distribution Data Source(s)

- The sample counts and sample weights are constructed using U.S. EIA 2020 RECS microdata

- Efficiency data based on ENERGY STAR shipment and Home Energy Saver data combined with age of equipment data from RECS 2020.

#### Direct Conditional Dependencies

- HVAC Cooling Type

- HVAC Has Shared System

- Vintage.

#### Options

ResStock includes four options for central air conditioners and four options for room air conditioners (Table “HVAC Cooling Efficiency options and arguments that vary for each option”). If a building has a heat pump, it is assumed that the heat pump is serving both the heating and cooling load. Buildings with heat pumps assigned in the HVAC Heating input files are flagged, but no ResStock arguments are passed to those building based on this file. Similarly, homes with a shared cooling system for the building are flagged, but the ResStock arguments for that system are assigned in the HVAC Shared Systems Efficiencies characteristic.

Across options with ResStock arguments, many are the same and set to *auto*:

- `cooling_system_cooling_compressor_type`

- `cooling_system_cooling_sensible_heat_fraction`

- `cooling_system_cooling_capacity`

- `cooling_system_cooling_autosizing_limit`

- `cooling_system_crankcase_heater_watts`

- `cooling_system_integrated_heating_system_fuel`

- `cooling_system_integrated_heating_system_efficiency_percent`

- `cooling_system_integrated_heating_system_capacity`

- `cooling_system_integrated_heating_system_fraction_heat_load_served`.

Additionally, `cooling_system_is_ducted` is set to false since ducts are defined in separate input files, and mini-split heat pumps will not be assigned ducts.

<div id="table:hc_opt_hvac_cool_eff" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `cooling_system_type` | `cooling_system_cooling_efficiency_type` | `cooling_system_cooling_efficiency` |
|:---|:---|:---|:---|
| AC, SEER 8 | central air conditioner | SEER | 8 |
| AC, SEER 10 | central air conditioner | SEER | 10 |
| AC, SEER 13 | central air conditioner | SEER | 13 |
| AC, SEER 15 | central air conditioner | SEER | 15 |
| Ducted Heat Pump | none | SEER | 0 |
| Non-Ducted Heat Pump | none | SEER | 0 |
| None | none | SEER | 0 |
| Room AC, EER 8.5 | room air conditioner | EER | 8.5 |
| Room AC, EER 9.8 | room air conditioner | EER | 9.8 |
| Room AC, EER 10.7 | room air conditioner | EER | 10.7 |
| Room AC, EER 12.0 | room air conditioner | EER | 12 |
| Shared Cooling |  |  |  |

HVAC Cooling Efficiency options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC Cooling Efficiency characteristic”. See the OpenStudio-HPXML [Cooling Systems](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-cooling-systems) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_cool_eff" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `cooling_system_type` | true |  | Choice | none, central air conditioner, room air conditioner, evaporative cooler, mini-split, packaged terminal air conditioner | The type of cooling system. Use 'none' if there is no cooling system or if there is a heat pump serving a cooling load. |
| `cooling_system_cooling_efficiency_type` | true |  | Choice | SEER, SEER2, EER, CEER | The efficiency type of the cooling system. System types central air conditioner and mini-split use SEER or SEER2. System types room air conditioner and packaged terminal air conditioner use EER or CEER. Ignored for system type evaporative cooler. |
| `cooling_system_cooling_efficiency` | true |  | Double |  | The rated efficiency value of the cooling system. Ignored for evaporative cooler. |
| `cooling_system_cooling_compressor_type` | false |  | Choice | auto, single stage, two stage, variable speed | The compressor type of the cooling system. Only applies to central air conditioner and mini-split. |
| `cooling_system_cooling_sensible_heat_fraction` | false | Frac | Double | auto | The sensible heat fraction of the cooling system. Ignored for evaporative cooler. |
| `cooling_system_cooling_autosizing_limit` | false | Btu/hr | Double |  | The maximum capacity limit applied to the auto-sizing methodology. If not provided, no limit is used. |
| `cooling_system_is_ducted` | false |  | Boolean | auto, true, false | Whether the cooling system is ducted or not. Only used for mini-split and evaporative cooler. It’s assumed that central air conditioner is ducted, and room air conditioner and packaged terminal air conditioner are not ducted. |
| `cooling_system_crankcase_heater_watts` | false | W | Double | auto | Cooling system crankcase heater power consumption in watts. Applies only to central air conditioner, room air conditioner, packaged terminal air conditioner and mini-split. |
| `cooling_system_integrated_heating_system_fuel` | false |  | Choice | auto, electricity, natural gas, fuel oil, propane, wood, wood pellets, coal | The fuel type of the heating system integrated into cooling system. Only used for packaged terminal air conditioner and room air conditioner. |
| `cooling_system_integrated_heating_system_efficiency_percent` | false | Frac | Double |  | The rated heating efficiency value of the heating system integrated into cooling system. Only used for packaged terminal air conditioner and room air conditioner. |
| `cooling_system_integrated_heating_system_capacity` | false | Btu/hr | Double |  | The output heating capacity of the heating system integrated into cooling system. |
| `cooling_system_integrated_heating_system_fraction_heat_load_served` | false | Frac | Double |  | The heating load served by the heating system integrated into cooling system. Only used for packaged terminal air conditioner and room air conditioner. |

The ResStock argument definitions set in the HVAC Cooling Efficiency characteristic

</div>

#### Distribution Assumption(s)

None

### HVAC Cooling Partial Space Conditioning

#### Description

The fraction of cooling load served by the cooling system. This is approximately equal to the fraction of finished floor area served by the cooling system. Cooling load must be met at every time step for the portion of floor area covered, and does not represent intermittent cooling overtime.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2009 RECS microdata.

- Hawaii constructed using U.S. EIA 2020 Residential Energy Consumption Survey (RECS) microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004—Sub-CZ Split

- Geometry Building Type RECS

- Geometry Floor Area Bin

- HVAC Cooling Type.

#### Options

Six different levels of percent of floor area cooled are provided, plus an option for homes that have no cooling (Table “HVAC Cooling Partial Space Conditioning options and arguments that vary for each option”).

<div id="table:hc_opt_hvac_cool_par" data-source="3b_ResStockInputs_HVAC.tex">

| Option name       | `cooling_system_fraction_cool_load_served` |
|:------------------|:-------------------------------------------|
| \<10% Conditioned | 0.1                                        |
| 20% Conditioned   | 0.2                                        |
| 40% Conditioned   | 0.4                                        |
| 60% Conditioned   | 0.6                                        |
| 80% Conditioned   | 0.8                                        |
| 100% Conditioned  | 1                                          |
| None              | 0                                          |

HVAC Cooling Partial Space Conditioning options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC Cooling Partial Conditioning characteristic”. See the OpenStudio-HPXML [Cooling-Systems](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-cooling-systems) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_cool_par" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Description |  |
|:---|:---|:---|:---|:---|:---|
| `cooling_system_fraction_cool_load_served` | true | Frac | Double | The cooling load served by the cooling system. |  |

The ResStock argument definitions set in the HVAC Cooling Partial Conditioning characteristic

</div>

#### Distribution Assumption(s)

- Central AC systems need to serve at least 60% of the floor area.

- Heat pumps serve 100% of the floor area because the system serves 100% of the heated floor area, except in Hawaii.

- Due to low sample count, this input is constructed by downscaling a core sub-input file with 3 sub-input files of different dependencies. The sub-input files have the following dependencies:

  - input1 : ‘HVAC Cooling Type’, ‘ASHRAE IECC Climate Zone 2004—Sub-CZ Split’

  - input2 : ‘HVAC Cooling Type’, ‘Geometry Floor Area Bin’

  - input3 : ‘HVAC Cooling Type’, ‘Geometry Building Type RECS’

### HVAC Cooling Autosizing Factor

#### Description

The cooling capacity and airflow scaling factor applied to the auto-sizing methodology. Not currently used in baseline.

#### Distribution Data Source(s)

- N/A.

#### Direct Conditional Dependencies

- HVAC Cooling Efficiency

- HVAC System is Scaled.

#### Options

Since this input file is not currently used, all homes are set to an option of “None.”

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC Cooling Autosizing Factor characteristic”. See the OpenStudio-HPXML [Cooling Systems](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-cooling-systems) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_cool_auto" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Type | Description |
|:---|:---|:---|:---|
| `cooling_system_cooling_autosizing_factor` | false | Double | The capacity scaling factor applied to the auto-sizing methodology. If not provided, 1.0 is used. |
| `heat_pump_cooling_autosizing_factor` | false | Double | The capacity scaling factor applied to the auto-sizing methodology. If not provided, 1.0 is used. |

The ResStock argument definitions set in the HVAC Cooling Autosizing Factor characteristic

</div>

#### Distribution Assumption(s)

HVAC sizing follows ACCA Manual J and Manual S. There is no additional oversizing or undersizing the capacity and airflow of the HVAC system.

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

## Setpoints

### Setpoints Modeling Approach

There are a set of characteristics that assign heating and cooling setpoint schedules in ResStock. The characteristics assign the setpoint, whether there is a setpoint offset, the magnitude of the setpoint offset, and the offset period. The heating and cooling setpoints determine the temperature past which heating and cooling systems run to condition the home. They can vary over time as occupants change their thermostat settings, often choosing different settings overnight or when they are away from home. The setpoint offset specifies whether there is a change in the setpoint at any point during the day. An example would be a heating setback where the heating setpoint temperature is decreased during the day when no one is home. The offset magnitude is the number of degrees of the offset. The offset period determines what hours of the day the offset applies.

Every housing unit is assigned a heating setpoint and cooling setpoint, regardless of whether it has a heating system or a cooling system. If a sampled heating setpoint is greater than the cooling setpoint, the values are averaged and kept constant across heating and cooling seasons. Every housing unit is also assigned heating setpoint offsets, cooling setpoint offsets, or neither, and an offset magnitude and time period for any offsets it is assigned. The reason for the assignment of setpoint schedules for housing units without either heating or cooling systems is mainly for upgrades, as a diverse set of setpoint schedules can be applied to the unit without complicated upgrade apply logic. Another interpretation is that these setpoint schedules would be the preference of the housing units if they had a heating or cooling system.

The following describes the building stock characteristic distributions, their data sources, options, argument values, and assumptions.

### Heating Setpoint

#### Description

Base heating setpoint (prior to any offset applied).

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Building Type RECS

- HVAC Has Zonal Electric Heating

- HVAC Heating Type

- Tenure.

#### Options

The options for the housing unit heating setpoint range between 55° F and 80° F (Table “Heating Setpoint options and arguments that vary for each option”). All setpoints that are assigned 55° F are vacant units. The heating setpoint characteristic sets the `hvac_control_heating_season_period`, `hvac_control_heating_weekday_setpoint_temp`, `hvac_control_heating_weekend_setpoint_temp`, and `use_auto_heating_season` arguments. Argument definitions are in Table “The ResStock argument definitions set in the Heating Setpoint characteristic”. The `hvac_control_heating_season_period` is always set to “auto,” and the `use_auto_heating_season` argument is always set to “false,” meaning the heating system will run as needed year-round. The heating set points are the same for weekdays and weekends.

<div id="table:hc_opt_ht_stp" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `hvac_control_heating_weekday_setpoint_temp` | `hvac_control_heating_weekend_setpoint_temp` |
|:---|:---|:---|
| 55F | 55 | 55 |
| 60F | 60 | 60 |
| 62F | 62 | 62 |
| 65F | 65 | 65 |
| 67F | 67 | 67 |
| 68F | 68 | 68 |
| 70F | 70 | 70 |
| 72F | 72 | 72 |
| 75F | 75 | 75 |
| 76F | 76 | 76 |
| 78F | 78 | 78 |
| 80F | 80 | 80 |

Heating Setpoint options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_ht_stp" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hvac_control_heating_season_period` | false |  | String | auto | Enter a date like 'Nov 1 - Jun 30'. Can also provide 'BuildingAmerica' to use automatic seasons from the Building America House Simulation Protocols. |
| `hvac_control_heating_weekday_setpoint_temp` | true | deg-F | Double |  | Specify the weekday heating setpoint temperature. |
| `hvac_control_heating_weekend_setpoint_temp` | true | deg-F | Double |  | Specify the weekend heating setpoint temperature. |
| `use_auto_heating_season` | true |  | Boolean | true, false | Specifies whether to automatically define the heating season based on the weather file. |

The ResStock argument definitions set in the Heating Setpoint characteristic

</div>

#### Distribution Assumption(s)

- For dependency conditions with low samples, the dependency values are lumped together in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, (2) lump buildings into Single-Family and Multifamily only, and lump nearby climate zones within A/B regions and separately 7AK and 8AK, and (3) lump all building types together, and lump climate zones within A/B regions and separately 7AK and 8AK.

- Heating type dependency is always lumped into Heat pump/Non-heat pumps.

- For vacant units (for which Tenure = ‘Not Available’), the heating setpoint is set to 55° F.

### Heating Setpoint Has Offset

#### Description

Presence of a heating setpoint offset.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Building Type RECS

- HVAC Has Zonal Electric Heating.

#### Options

The options are either “Yes” or “No.” The options do not assign any ResStock arguments.

#### Distribution Assumption(s)

- For dependency conditions with low samples, the following dependency values are lumped together in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, and (2) lump all building types together.

### Heating Setpoint Offset Magnitude

#### Description

The magnitude of the heating setpoint offset.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Building Type RECS

- Heating Setpoint Has Offset

- HVAC Has Zonal Electric Heating.

#### Options

The options for Heating Setpoint Offset Magnitude are 0F, 3F, 6F, and 12F (Table “Heating Setpoint Offset Magnitude options and arguments that vary for each option”). The options are the ° F that the heating setpoint is decreased if a heating setpoint offset is selected. The heating offset magnitude is the same for weekdays and weekends. The Heating Setpoint Offset Magnitude characteristic sets the `hvac_control_heating_weekday_setpoint_offset_magnitude` and `hvac_control_heating_weekend_setpoint_offset_magnitude` arguments. Argument definitions are in Table “The ResStock argument definitions set in the Heating Setpoint Offset Magnitude characteristic”.

<div id="table:hc_opt_ht_stp_mag" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `hvac_control_heating_weekday_setpoint_offset_magnitude` | `hvac_control_heating_weekend_setpoint_offset_magnitude` |
|:---|:---|:---|
| 0F | 0 | 0 |
| 3F | 3 | 3 |
| 6F | 6 | 6 |
| 12F | 12 | 12 |

Heating Setpoint Offset Magnitude options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_ht_stp_mag" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hvac_control_heating_weekday_setpoint_offset_magnitude` | true | deg-F | Double |  | Specify the weekday heating offset magnitude. |
| `hvac_control_heating_weekend_setpoint_offset_magnitude` | true | deg-F | Double |  | Specify the weekend heating offset magnitude. |

The ResStock argument definitions set in the Heating Setpoint Offset Magnitude characteristic

</div>

#### Distribution Assumption(s)

- For dependency conditions with low samples, the following dependency values are lumped together in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, (2) lump buildings into Single-Family and Multifamily only, and lump nearby climate zones within A/B regions and separately 7AK and 8AK, and (3) lump all building types together and lump climate zones within A/B regions and separately 7AK and 8AK.

### Heating Setpoint Offset Period

#### Description

The time period(s) for the housing unit’s heating setpoint offset.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Building Type RECS

- Heating Setpoint Has Offset

- HVAC Has Zonal Electric Heating.

#### Options

The options are a combination of day and night offset periods (Table “Heating Setpoint Offset Period options and arguments that vary for each option.”). The default for the day is from 9 AM to 5 PM and for the night is 10 PM to 7 AM. The options then shift these periods randomly up to 5 hours in either direction. The shifting of the periods is mainly to avoid the synchronization of HVAC systems across the housing stock from all turning on and off at the same time. The characteristic sets the `hvac_control_heating_weekday_setpoint_schedule` and `hvac_control_heating_weekend_setpoint_schedule` ResStock arguments. The values for the arguments are 24-hour arrays for when the setback occurs (a value of -1) and when the setback does not occur (a value of 0). The argument definitions are in Table “The ResStock argument definitions set in the Heating Setpoint Offset Period characteristic”.

<div id="table:hc_opt_ht_stp_per" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `hvac_control_heating_weekday_setpoint_schedule` | `hvac_control_heating_weekend_setpoint_schedule` |
|:---|:---|:---|
| Day | 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day -1h | 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day -2h | 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day -3h | 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day -4h | 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day -5h | 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day +1h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day +2h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day +3h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day +4h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day +5h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day and Night | -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1 | -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1 |
| Day and Night -1h | -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1 | -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1 |
| Day and Night -2h | -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1 | -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1 |
| Day and Night -3h | -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 | -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 |
| Day and Night -4h | -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 | -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 |
| Day and Night -5h | -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 | -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 |
| Day and Night +1h | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1 | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1 |
| Day and Night +2h | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0 | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day and Night +3h | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0 | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day and Night +4h | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0 | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day and Night +5h | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0 | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night | -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1 | -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1 |
| Night -1h | -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1 | -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1 |
| Night -2h | -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1 | -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1 |
| Night -3h | -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 | -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 |
| Night -4h | -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 | -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 |
| Night -5h | -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 | -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 |
| Night +1h | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1 | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1 |
| Night +2h | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night +3h | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night +4h | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night +5h | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| None | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |

Heating Setpoint Offset Period options and arguments that vary for each option.

</div>

<div id="table:hc_arg_def_ht_stp_per" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hvac_control_heating_weekday_setpoint_schedule` | true |  | String |  | Specify the 24-hour comma-separated weekday heating schedule of 0s and 1s. |
| `hvac_control_heating_weekend_setpoint_schedule` | true |  | String |  | Specify the 24-hour comma-separated weekend heating schedule of 0s and 1s. |

The ResStock argument definitions set in the Heating Setpoint Offset Period characteristic

</div>

#### Distribution Assumption(s)

- For dependency conditions with low samples, the following dependency values are lumped in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, (2) lump buildings into Single-Family and Multifamily only, and lump nearby climate zones within A/B regions and separately 7AK and 8AK, and (3) lump all building types together and lump climate zones within A/B regions and separately 7AK and 8AK.

### Cooling Setpoint

#### Description

Baseline cooling setpoint (prior to any offset applied).

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Building Type RECS

- HVAC Cooling Type

- Tenure.

#### Options

The options for the Cooling Setpoint characteristic range between 60° F and 80° F (Table “Cooling Setpoint options and arguments that vary for each option”). The Cooling Setpoint characteristic sets the `hvac_control_cooling_season_period`, `hvac_control_cooling_weekday_setpoint_temp`, `hvac_control_cooling_weekend_setpoint_temp`, and `use_auto_cooling_season` ResStock arguments. The `hvac_control_cooling_season_period` argument is always set to “auto.” The `use_auto_cooling_season` argument is always set to “false.” These arguments allow the cooling system to run all year as needed. Argument definitions are in Table “The ResStock argument definitions set in the Cooling Setpoint characteristic”.

<div id="table:hc_opt_cl_stp" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `hvac_control_cooling_weekday_setpoint_temp` | `hvac_control_cooling_weekend_setpoint_temp` |
|:---|:---|:---|
| 60F | 60 | 60 |
| 62F | 62 | 62 |
| 65F | 65 | 65 |
| 67F | 67 | 67 |
| 68F | 68 | 68 |
| 70F | 70 | 70 |
| 72F | 72 | 72 |
| 75F | 75 | 75 |
| 76F | 76 | 76 |
| 78F | 78 | 78 |
| 80F | 80 | 80 |

Cooling Setpoint options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_cl_stp" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hvac_control_cooling_season_period` | false |  | String | auto | Enter a date like 'Jun 1 - Oct 31'. Can also provide 'BuildingAmerica' to use automatic seasons from the Building America House Simulation Protocols. |
| `hvac_control_cooling_weekday_setpoint_temp` | true | deg-F | Double |  | Specify the weekday cooling setpoint temperature. |
| `hvac_control_cooling_weekend_setpoint_temp` | true | deg-F | Double |  | Specify the weekend cooling setpoint temperature. |
| `use_auto_cooling_season` | true |  | Boolean | true, false | Specifies whether to automatically define the cooling season based on the weather file. |

The ResStock argument definitions set in the Cooling Setpoint characteristic

</div>

#### Distribution Assumption(s)

- For dependency conditions with low samples, the following dependency values are lumped together in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, (2) lump buildings into Single-Family and Multifamily only, and lump nearby climate zones within A/B regions and separately 7AK and 8AK, (3) lump all building types together and lump climate zones within A/B regions and separately 7AK and 8AK, and (4) Owner and Renter are lumped together, which at this point only modifies AK distributions. Vacant units (for which Tenure = ‘Not Available’) are assumed to follow the same distribution as occupied units.

### Cooling Setpoint Has Offset

#### Description

Presence of a cooling setpoint offset.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Building Type RECS.

#### Options

The options of the Cooling Setpoint Has Offset characteristic are “Yes” and “No.” An example of the offset for cooling is when the occupants leave the housing unit (e.g., commute to work), the cooling setpoint temperature is set up to a warmer temperature.

#### Distribution Assumption(s)

- For dependency conditions with low samples, the following dependency values are lumped in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, and (2) lump all building types together and lump climate zones within A/B regions and separately 7AK and 8AK.

### Cooling Setpoint Offset Magnitude

#### Description

The magnitude of cooling setpoint offset.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Cooling Setpoint Has Offset

- Geometry Building Type RECS.

#### Options

The options of the Cooling Setpoint Offset Magnitude characteristic are 0° F, 2° F, 5° F, and 9° F (Table “Cooling Setpoint Offset Magnitude options and arguments that vary for each option”). The characteristic set the `hvac_control_cooling_weekday_setpoint_offset_magnitude` and `hvac_control_cooling_weekend_setpoint_offset_magnitude` ResStock arguments. A zero degree offset corresponds to the setpoint not having an offset. Argument definitions are in Table “The ResStock argument definitions set in the Cooling Setpoint Offset Magnitude characteristic”.

<div id="table:hc_arg_def_cl_stp_mag" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hvac_control_cooling_weekday_setpoint_offset_magnitude` | true | deg-F | Double |  | Specify the weekday cooling offset magnitude. |
| `hvac_control_cooling_weekend_setpoint_offset_magnitude` | true | deg-F | Double |  | Specify the weekend cooling offset magnitude. |

The ResStock argument definitions set in the Cooling Setpoint Offset Magnitude characteristic

</div>

<div id="table:hc_opt_cl_stp_mag" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `hvac_control_cooling_weekday_setpoint_offset_magnitude` | `hvac_control_cooling_weekend_setpoint_offset_magnitude` |
|:---|:---|:---|
| 0F | 0 | 0 |
| 2F | 2 | 2 |
| 5F | 5 | 5 |
| 9F | 9 | 9 |

Cooling Setpoint Offset Magnitude options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

- For dependency conditions with low samples, the following dependency values are lumped in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, (2) lump buildings into Single-Family and Multifamily only, and lump nearby climate zones within A/B regions and separately 7AK and 8AK, and (3) lump all building types together and lumping climate zones within A/B and separately 7AK and 8AK regions.

### Cooling Setpoint Offset Period

#### Description

The time period(s) for the housing unit’s heating setpoint offset.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Cooling Setpoint Has Offset

- Geometry Building Type RECS.

#### Options

The options combine day and night offset periods (Table “Cooling Setpoint Offset Period options and arguments that vary for each option”). The default for the day is from 9 AM to 5 PM and for the night is 10 PM to 7 AM. The options then shift these periods randomly up to 5 hours in either direction. The shifting of the periods is mainly to avoid the synchronization of HVAC systems all turning on and off simultaneously. The characteristic set the `hvac_control_cooling_weekday_setpoint_schedule` and `hvac_control_cooling_weekdend_setpoint_schedule` ResStock arguments. The values for the arguments are hourly arrays for when the setup occurs (a value of 1), a setback (a value of -1), and when the setup or setback does not occur (a value of 0). The argument definitions are in Table “The ResStock argument definitions set in the Cooling Setpoint Offset Period characteristic”.

<div id="table:hc_opt_cl_stp_per" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `hvac_control_cooling_weekday_setpoint_schedule` | `hvac_control_cooling_weekend_setpoint_schedule` |
|:---|:---|:---|
| Day and Night Setup | 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1,1, 1, 0, 0, 0, 0, 0, 1, 1 | 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 |
| Day and Night Setup -1h | 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1 | 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1 |
| Day and Night Setup -2h | 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1 | 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 |
| Day and Night Setup -3h | 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 | 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 |
| Day and Night Setup -4h | 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1 | 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1 |
| Day and Night Setup -5h | 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1 | 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1 |
| Day and Night Setup +1h | 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1 | 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 |
| Day and Night Setup +2h | 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day and Night Setup +3h | 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0 | 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day and Night Setup +4h | 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0 | 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day and Night Setup +5h | 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0 | 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup | 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup -1h | 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup -2h | 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup -3h | 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup -4h | 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup -5h | 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup +1h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup +2h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup +3h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup +4h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup +5h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup and Night Setback | -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, -1 | -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1 |
| Day Setup and Night Setback -1h | -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, -1, -1 | -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1 |
| Day Setup and Night Setback -2h | -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, -1, -1, -1 | -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1 |
| Day Setup and Night Setback -3h | -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 | -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 |
| Day Setup and Night Setback -4h | -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 | -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 |
| Day Setup and Night Setback -5h | -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 | -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 |
| Day Setup and Night Setback +1h | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1 | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1 |
| Day Setup and Night Setback +2h | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0 | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup and Night Setback +3h | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0 | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup and Night Setback +4h | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0 | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup and Night Setback +5h | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0 | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setback | -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1 | -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1 |
| Night Setback -1h | -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1 | -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1 |
| Night Setback -2h | -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1 | -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1 |
| Night Setback -3h | -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 | -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 |
| Night Setback -4h | -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 | -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 |
| Night Setback -5h | -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 | -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 |
| Night Setback +1h | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1 | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1 |
| Night Setback +2h | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setback +3h | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setback +4h | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setback +5h | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setup | 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 | 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 |
| Night Setup -1h | 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1 | 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1 |
| Night Setup -2h | 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 | 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 |
| Night Setup -3h | 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 | 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 |
| Night Setup -4h | 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1 | 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1 |
| Night Setup -5h | 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1 | 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1 |
| Night Setup +1h | 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 | 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 |
| Night Setup +2h | 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setup +3h | 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setup +4h | 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setup +5h | 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| None | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |

Cooling Setpoint Offset Period options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_cl_per" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hvac_control_cooling_weekday_setpoint_schedule` | true |  | String |  | Specify the 24-hour comma-separated weekday cooling schedule of 0s and 1s. |
| `hvac_control_cooling_weekend_setpoint_schedule` | true |  | String |  | Specify the 24-hour comma-separated weekend cooling schedule of 0s and 1s. |

The ResStock argument definitions set in the Cooling Setpoint Offset Period characteristic

</div>

#### Distribution Assumption(s)

- For dependency conditions with low samples, the following dependency values are lumped in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, (2) lump buildings into Single-Family and Multifamily only, and lump nearby climate zones within A/B regions and separately 7AK and 8AK, and (3) lump all building types together and lump climate zones within A/B and separately 7AK and 8AK regions.

## Ducts

### Modeling Approach

ResStock assigns three characteristics related to air distribution ductwork for each housing unit: whether there are ducts present, where the ducts are located, and a combined characteristic that includes the level of duct insulation and the amount of leakage from the ducts to unconditioned space. The location of the ductwork depends on the building type, the foundation type, the attic type, and presence of an attached garage, and if the housing unit has ducts. This is a direct map for each space combination. Air leakage and heat gains and losses are calculated for the fraction of the ductwork outside conditioned space. OpenStudio-HPXML assigns the fraction of the duct area in the conditioned space. Currently, in single-family homes, if the number of floors above grade is one, 100% of the duct surface area is outside the conditioned space. If the number of floors above grade is greater than one, then 75% of the duct surface area is outside the conditioned space. OpenStudio-HPXML also assigns fractions of supply/return ducts with a rectangular and circular cross-section, which affects the effective R-value for a given nominal duct insulation R-value.

ResStock has three inputs that control specify the primary ductwork arguments in the model:

- HVAC Has Ducts

- Duct Location

- Duct Leakage and Insulation.

### HVAC Has Ducts

#### Description

The presence of ducts in the housing unit.

#### Distribution Data Source(s)

- The sample counts and sample weights are constructed using RECS 2020 microdata.

#### Direct Conditional Dependencies

- HVAC Cooling Type

- HVAC Has Shared System

- HVAC Heating Type

- HVAC Secondary Heating Type.

#### Options

Two options are available for this input characteristic: yes or no. The presence of ductwork is dependent upon the heating and cooling systems. Both duct options set the `hvac_blower_fan_watts_per_cfm` argument to auto.

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC Has Ducts characteristic”. See the OpenStudio-HPXML [Air Distribution](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#air-distribution) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_has_duct" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hvac_blower_fan_watts_per_cfm` | false | W/CFM | Double | auto | The blower fan efficiency at maximum fan speed. Applies only to split (not packaged) systems (i.e., applies to ducted systems as well as ductless mini-split systems). |

The ResStock argument definitions set in the HVAC Has Ducts characteristic

</div>

#### Distribution Assumption(s)

- Ducted Heat Pump HVAC type assumed to have ducts.

- Non-Ducted Heat Pump HVAC type assumed to have no ducts.

- There could be homes with non-ducted heat pump having ducts (Central AC with non-ducted heat pump), but due to structure of ResStock we are not accounting for those homes.

- None of the shared system options currently modeled (in HVAC Shared Efficiencies) are ducted, therefore where there are discrepancies between HVAC Heating Type, HVAC Cooling Type, and HVAC Has Shared System, HVAC Has Shared System takes precedence (e.g., Central AC + Ducted Heating + Shared Heating and Cooling = No (Ducts)). (This is a temporary fix and will change when ducted shared system options are introduced.)

### Duct Leakage and Insulation

#### Description

Duct insulation and leakage to outside for the portion of ducts in unconditioned spaces.

#### Distribution Data Source(s)

- Duct insulation as a function of location: IECC 2009

- Leakage distribution: Lucas and Cole ([2009](https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-18545.pdf)). *Impacts of the 2009 IECC for Residential Buildings at State Level*.

#### Direct Conditional Dependencies

- Duct location

- Vintage.

#### Options

ResStock uses 13 combinations of insulation and air leakage from ducts (Table “Duct Leakage and Insulation options and arguments that vary for each option”). The following ResStock arguments are constant across all options:

- `ducts_leakage_units`: percent

- `ducts_supply_buried_insulation_level`: auto

- `ducts_supply_fraction_rectangular`: auto

- `ducts_return_buried_insulation_level`: auto

- `ducts_return_fraction_rectangular`: auto.

<div id="table:hc_opt_duct_leak" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `ducts_supply_leakage_to_outside_value` | `ducts_supply_insulation_r` | `ducts_return_leakage_to_outside_value` | `ducts_return_insulation_r` |
|:---|:---|:---|:---|:---|
| 0% Leakage to Outside, Uninsulated | 0 | 0 | 0 | 0 |
| 10% Leakage to Outside, R-4 | 0.067 | 4 | 0.033 | 4 |
| 10% Leakage to Outside, R-6 | 0.067 | 6 | 0.033 | 6 |
| 10% Leakage to Outside, R-8 | 0.067 | 8 | 0.033 | 8 |
| 10% Leakage to Outside, Uninsulated | 0.067 | 0 | 0.033 | 0 |
| 20% Leakage to Outside, R-4 | 0.133 | 4 | 0.067 | 4 |
| 20% Leakage to Outside, R-6 | 0.133 | 6 | 0.067 | 6 |
| 20% Leakage to Outside, R-8 | 0.133 | 8 | 0.067 | 8 |
| 20% Leakage to Outside, Uninsulated | 0.133 | 0 | 0.067 | 0 |
| 30% Leakage to Outside, R-4 | 0.200 | 4 | 0.100 | 4 |
| 30% Leakage to Outside, R-6 | 0.200 | 6 | 0.100 | 6 |
| 30% Leakage to Outside, R-8 | 0.200 | 8 | 0.100 | 8 |
| 30% Leakage to Outside, Uninsulated | 0.200 | 0 | 0.100 | 0 |
| None | 0 | 0 | 0 | 0 |

Duct Leakage and Insulation options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Duct Leakage and Insulation characteristic”. See the OpenStudio-HPXML [Air Distribution](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#air-distribution) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_duct_leak" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `ducts_leakage_units` | true |  | Choice | CFM25, CFM50, Percent | The leakage units of the ducts. |
| `ducts_supply_leakage_to_outside_value` | true |  | Double |  | The leakage value to outside for the supply ducts. |
| `ducts_supply_insulation_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | The nominal insulation r-value of the supply ducts excluding air films. Use 0 for uninsulated ducts. |
| `ducts_supply_buried_insulation_level` | false |  | Choice | auto, not buried, partially buried, fully buried, deeply buried | Whether the supply ducts are buried in, e.g., attic loose-fill insulation. Partially buried ducts have insulation that does not cover the top of the ducts. Fully buried ducts have insulation that just covers the top of the ducts. Deeply buried ducts have insulation that continues above the top of the ducts. |
| `ducts_supply_fraction_rectangular` | false | frac | Double | auto | The fraction of supply ducts that are rectangular (as opposed to round); this affects the duct effective R-value used for modeling. |
| `ducts_return_leakage_to_outside_value` | true |  | Double |  | The leakage value to outside for the return ducts. |
| `ducts_return_insulation_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | The nominal insulation r-value of the return ducts excluding air films. Use 0 for uninsulated ducts. |
| `ducts_return_buried_insulation_level` | false |  | Choice | auto, not buried, partially buried, fully buried, deeply buried | Whether the return ducts are buried in, e.g., attic loose-fill insulation. Partially buried ducts have insulation that does not cover the top of the ducts. Fully buried ducts have insulation that just covers the top of the ducts. Deeply buried ducts have insulation that continues above the top of the ducts. |
| `ducts_return_fraction_rectangular` | false | frac | Double | auto | The fraction of return ducts that are rectangular (as opposed to round); this affects the duct effective R-value used for modeling. |

The ResStock argument definitions set in the Duct Leakage and Insulation characteristic

</div>

#### Distribution Assumption(s)

Ducts entirely in conditioned spaces will not have any leakage to outside. Ducts with R-4/R-8 insulation were previously assigned to Geometry Foundation Type = Ambient or Slab. They now correspond to those with Duct Location = Garage, Unvented Attic, or Vented Attic.

### Duct Location

#### Description

Primary location of duct system. As described earlier, a fraction of the ducts will also be assumed to be in conditioned space for homes with multiple stories.

#### Distribution Data Source(s)

- OpenStudio-HPXML v1.6.0 and Building America House Simulation Protocols ((E. Wilson et al. 2014a)).

#### Direct Conditional Dependencies

- Geometry Space Combination

- HVAC Has Ducts.

#### Options

The duct location is a direct mapping of spaces from the hierarchical assignment in OpenStudio-HPXML. This is done to expose the duct location as an output in ResStock. The spaces available for the ducts are in Table “Duct Location options and arguments that vary for each option”. The “None” option is used for ducts that are located completely in the conditioned space. For all options of Duct Location, the following arguments are the same:

- `ducts_supply_surface_area`: auto

- `ducts_supply_surface_area_fraction`: auto

- `ducts_return_surface_area`: auto

- `ducts_return_surface_area_fraction`: auto.

<div id="table:hc_opt_duct_loc" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `ducts_supply_location` | `ducts_return_location` | `ducts_number_of_return_registers` |
|:---|:---|:---|:---|
| Attic | attic | attic | auto |
| Crawlspace | crawlspace | crawlspace | auto |
| Garage | garage | garage | auto |
| Heated Basement | basement—conditioned | basement—conditioned | auto |
| Living Space | conditioned space | conditioned space | auto |
| Unheated Basement | basement—unconditioned | basement—unconditioned | auto |
| None | conditioned space | conditioned space | 0 |

Duct Location options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Duct Location characteristic”. See the OpenStudio-HPXML [Air Distribution](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-air-distribtuion) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_duct_loc" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `ducts_supply_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, crawlspace, crawlspace—vented, crawlspace—unvented, crawlspace—conditioned, attic, attic—vented, attic—unvented, garage, exterior wall, under slab, roof deck, outside, other housing unit, other heated space, other multifamily buffer space, other non-freezing space, manufactured home belly | The location of the supply ducts. |
| `ducts_supply_surface_area` | false | ft<sup>2</sup> | Double | auto | The supply ducts surface area in the given location. |
| `ducts_supply_surface_area_fraction` | false | frac | Double | auto | The fraction of supply ducts surface area in the given location. Only used if Surface Area is not provided. If the fraction is less than 1, the remaining duct area is assumed to be in conditioned space. |
| `ducts_return_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, crawlspace, crawlspace—vented, crawlspace—unvented, crawlspace—conditioned, attic, attic—vented, attic—unvented, garage, exterior wall, under slab, roof deck, outside, other housing unit, other heated space, other multifamily buffer space, other non-freezing space, manufactured home belly | The location of the return ducts. |
| `ducts_return_surface_area` | false | ft<sup>2</sup> | Double | auto | The return ducts surface area in the given location. |
| `ducts_return_surface_area_fraction` | false | frac | Double | auto | The fraction of return ducts surface area in the given location. Only used if Surface Area is not provided. If the fraction is less than 1, the remaining duct area is assumed to be in conditioned space. |
| `ducts_number_of_return_registers` | false | \# | Integer | auto | The number of return registers of the ducts. Only used to calculate default return duct surface area. |

The ResStock argument definitions set in the Duct Location characteristic

</div>

#### Distribution Assumption(s)

Based on default duct location assignment in OpenStudio-HPXML: the first present space type in the order of: basement—conditioned, basement—unconditioned, crawlspace—conditioned, crawlspace—vented, crawlspace—unvented, attic—vented, attic—unvented, garage, or living space.

## Unavailable HVAC Periods

### Modeling Approach

Periods when the HVAC system is unavailable, either due to a system malfunction or because the household cannot afford to operate it, are modeled in ResStock. These periods are assigned using the availability schedules in OpenStudio-HPXML. Separate unavailability periods are defined for heating and cooling. The length of these periods can range from 0 days (indicating the HVAC system is always available) to a single day, or up to the entire year. If the "Year Round" option is sampled, the unavailability period is set to "Jan 1 - Dec 31." For a partial-year unavailability (e.g., 1, 7, 14 days, etc.), a randomly selected n-day period (where n is the duration of the unavailability) is chosen to start during the Building America heating or cooling months, as defined in the Building America House Simulation Protocols (E. Wilson et al. 2014b). In locations without Building America heating or cooling months (e.g., Hawaii has no heating months), the heating season is assumed to be December through February, and the cooling season is assumed to be June through August. If the number of unavailable days exceeds the length of the Building America season, the unavailability period extends beyond the defined season. To ensure deterministic simulations, the `building_id` is used as the seed for random date selection. There are two characteristics that sets the number of days the heating and cooling system is unavailable 1) Cooling Unavailable Days and 2) Heating Unavailable Days.

### Cooling Unavailable Days

#### Description

Number of days in a year the cooling system is unavailable.

#### Distribution Data Source(s)

- U.S. EIA 2020 Residential Energy Consumption Survey (RECS) microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- Tenure

#### Options

The options of Cooling Unavailable Days characteristic are a number of days the cooling system is unavailable. The characteristic sets the `schedules_space_cooling_unavailable_days` argument. The argument definition can be found in Table “The ResStock argument definitions set in the Cooling Unavailable Days characteristic”.

<div id="table:hc_arg_def_cooling_unavailable_days" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `schedules_space_cooling_unavailable_days` | false |  | Integer | Number of days space cooling equipment is unavailable. |

The ResStock argument definitions set in the Cooling Unavailable Days characteristic

</div>

The options range between 0 days (Never) to the whole year (year round). The Void option is for impossible combinations that are not sampled.

<div id="table:hc_opt_cooling_unavailable_days" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `schedules_space_cooling_unavailable_days` |
|:------------|:-------------------------------------------|
| Never       | 0                                          |
| 1 day       | 1                                          |
| 3 days      | 3                                          |
| 1 week      | 7                                          |
| 2 weeks     | 14                                         |
| 1 month     | 30                                         |
| 3 months    | 90                                         |
| Year round  | 365                                        |
| Void        |                                            |

Cooling Unavailable Days options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

None

### Heating Unavailable Days

#### Description

Number of days in a year the heating system is unavailable.

#### Distribution Data Source(s)

- U.S. EIA 2020 Residential Energy Consumption Survey (RECS) microdata.

#### Direct Conditional Dependencies

- Cooling Unavailable Days

- Federal Poverty Level

- Geometry Building Type RECS

#### Options

The options of Heating Unavailable Days characteristic are a number of days the cooling system is unavailable. The characteristic sets the `schedules_space_heating_unavailable_days` argument. The argument definition can be found in Table “The ResStock argument definitions set in the Heating Unavailable Days characteristic”.

<div id="table:hc_arg_def_heating_unavailable_days" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `schedules_space_heating_unavailable_days` | false |  | Integer | Number of days space heating equipment is unavailable. |

The ResStock argument definitions set in the Heating Unavailable Days characteristic

</div>

The options range between 0 days (Never) to the whole year (year round). The Void option is for impossible combinations that are not sampled.

<div id="table:hc_opt_heating_unavailable_days" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `schedules_space_heating_unavailable_days` |
|:------------|:-------------------------------------------|
| Never       | 0                                          |
| 1 day       | 1                                          |
| 3 days      | 3                                          |
| 1 week      | 7                                          |
| 2 weeks     | 14                                         |
| 1 month     | 30                                         |
| 3 months    | 90                                         |
| Year round  | 365                                        |
| Void        |                                            |

Heating Unavailable Days options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

- Where samples are less than 10, the data is aggregated in the following order until there are no rows with less than 10 samples:

  - The Federal Poverty Level dependency is aggregated every 100% bins

  - The Federal Poverty Level dependency is aggregated every 200% bins

  - The Geometry Building Type RECS dependency is aggregated into single-family, multi-family, and mobile home bins.

  - The Cooling Unavailable Days dependency is aggregated into days, weeks, month, and year round bins.

  - The Cooling Unavailable Days dependency is removed.

## HVAC Installation Quality

### Modeling Approach

ResStock includes features that allow users to account for the quality of HVAC installation. Two key factors that impact installation quality are the refrigeration charge and the airflow rate.

ResStock specifies the installed refrigerant charge as a percentage of the system’s design charge for each option. It also sets the actual airflow rate per ton of cooling capacity, which may differ from the design airflow rate.

These variables, refrigerant charge fractions and airflow rates, can be adjusted for single-speed air conditioners and air-source heat pumps. However, despite these capabilities, ResStock currently does not make use of these options in the baseline model.

### HVAC System Single-Speed ASHP Airflow

#### Description

Single-speed ASHP actual airflow rates for faulted systems. This input file is currently not used since ResStock is still lacking data on faults.

#### Distribution Data Source(s)

- *Impact of installation faults in air conditioners and heat pumps in single-family homes on U.S. energy usage* ((Winkler et al. 2020)).

#### Direct Conditional Dependencies

- HVAC Heating Efficiency

- HVAC System is Faulted.

#### Options

Thirteen options are available in ResStock, but currently none are used, and all homes as set to “None” (Table “HVAC System Single-Speed ASHP Airflow options and arguments that vary for each option”). The `cooling_system_rated_cfm_per_ton` for all 13 options is 400.0.

<div id="table:hc_opt_hvac_single_speed" data-source="3b_ResStockInputs_HVAC.tex">

| Option name   | `cooling_system_actual_cfm_per_ton` |
|:--------------|:------------------------------------|
| 154.8 cfm/ton | 154.8                               |
| 204.4 cfm/ton | 204.4                               |
| 254.0 cfm/ton | 254.0                               |
| 303.5 cfm/ton | 303.5                               |
| 353.1 cfm/ton | 353.1                               |
| 402.7 cfm/ton | 402.7                               |
| 452.3 cfm/ton | 452.3                               |
| 501.9 cfm/ton | 501.9                               |
| 551.5 cfm/ton | 551.5                               |
| 601.0 cfm/ton | 601.0                               |
| 650.6 cfm/ton | 650.6                               |
| 700.2 cfm/ton | 700.2                               |
| None          |                                     |

HVAC System Single-Speed ASHP Airflow options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC System Single-Speed ASHP characteristic”. See the OpenStudio-HPXML [Air-to-Air Heat Pump](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#air-to-air-heat-pump) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_single_speed" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `cooling_system_rated_cfm_per_ton` | false | cfm/ton | Double | The rated cfm per ton of the cooling system. |
| `cooling_system_actual_cfm_per_ton` | false | cfm/ton | Double | The actual cfm per ton of the cooling system. |

The ResStock argument definitions set in the HVAC System Single-Speed ASHP characteristic

</div>

#### Distribution Assumption(s)

None

### HVAC System Single-Speed ASHP Charge

#### Description

ASHP deviation between design/installed charge. Not currently used because of lack of data on faulted HVAC.

#### Distribution Data Source(s)

- *Impact of installation faults in air conditioners and heat pumps in single-family homes on U.S. energy usage* ((Winkler et al. 2020)).

#### Direct Conditional Dependencies

- HVAC Heating Efficiency

- HVAC System is Faulted.

#### Options

Seven different options are available for faulted ASHP charges, but none are currently in use (Table “HVAC System Single-Speed ASHP options and arguments that vary for each option”).

<div id="table:hc_opt_ss_hp_charge" data-source="3b_ResStockInputs_HVAC.tex">

| Option name       | `heat_pump_frac_manufacturer_charge` |
|:------------------|:-------------------------------------|
| 0.570 Charge Frac | 0.570                                |
| 0.709 Charge Frac | 0.709                                |
| 0.848 Charge Frac | 0.848                                |
| 0.988 Charge Frac | 0.988                                |
| 1.127 Charge Frac | 1.127                                |
| 1.266 Charge Frac | 1.266                                |
| 1.405 Charge Frac | 1.405                                |
| None              |                                      |

HVAC System Single-Speed ASHP options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC Secondary Heating characteristic”. See the OpenStudio-HPXML [Air-to-Air Heat Pumps](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#air-to-air-heat-pump) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ss_hp_charge" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `heat_pump_frac_manufacturer_charge` | false | Frac | Double | The fraction of manufacturer recommended charge of the heat pump. |

The ResStock argument definitions set in the HVAC Secondary Heating characteristic

</div>

### HVAC System Single-Speed AC Airflow

#### Description

Single-speed central and room air conditioner actual air flow rates for faulted systems. Not currently used since ResStock lacks data on faulted systems.

#### Distribution Data Source(s)

- *Impact of installation faults in air conditioners and heat pumps in single-family homes on U.S. energy usage* ((Winkler et al. 2020)).

#### Direct Conditional Dependencies

- HVAC Cooling Efficiency

- HVAC System is Faulted.

#### Options

Twelve options are given for real airflow, but none are currently in use (Table “HVAC System Single-Speed AC Airflow options and arguments that vary for each option”). The `heat_pump_rated_cfm_per_ton` argument is set to 400 for all options.

<div id="table:hc_opt_hvac_ss_ac_airflow" data-source="3b_ResStockInputs_HVAC.tex">

| Option name   | `heat_pump_actual_cfm_per_ton` |
|:--------------|:-------------------------------|
| 154.8 cfm/ton | 154.8                          |
| 204.4 cfm/ton | 204.4                          |
| 254.0 cfm/ton | 254.0                          |
| 303.5 cfm/ton | 303.5                          |
| 353.1 cfm/ton | 353.1                          |
| 402.7 cfm/ton | 402.7                          |
| 452.3 cfm/ton | 452.3                          |
| 501.9 cfm/ton | 501.9                          |
| 551.5 cfm/ton | 551.5                          |
| 601.0 cfm/ton | 601.0                          |
| 650.6 cfm/ton | 650.6                          |
| 700.2 cfm/ton | 700.2                          |
| None          | 100%                           |

HVAC System Single-Speed AC Airflow options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC System Single-Speed AC Airflow characteristic”. See the OpenStudio-HPXML [Central Air Conditioner](-https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#central-air-conditioner) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_ss_ac_airflow" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type s | Description |
|:---|:---|:---|:---|:---|
| `heat_pump_rated_cfm_per_ton` | false | cfm/ton | Double | The rated cfm per ton of the heat pump. |
| `heat_pump_actual_cfm_per_ton` | false | cfm/ton | Double | The actual cfm per ton of the heat pump. |

The ResStock argument definitions set in the HVAC System Single-Speed AC Airflow characteristic

</div>

#### Distribution Assumption(s)

None

### HVAC System Single-Speed AC Charge

#### Description

Central and room air conditioner deviation between design/installed charge.

#### Distribution Data Source(s)

- *Impact of installation faults in air conditioners and heat pumps in single-family homes on U.S. energy usage* ((Winkler et al. 2020)).

#### Direct Conditional Dependencies

- HVAC Cooling Efficiency

- HVAC System is Faulted.

#### Options

Seven different options are available for faulted AC charges, but none are currently in use (Table “HVAC System Single-Speed AC Charge options and arguments that vary for each option”).

<div id="table:hc_opt_ss_ac_charge" data-source="3b_ResStockInputs_HVAC.tex">

| Option name       | `cooling_system_frac_manufacturer_charge` |
|:------------------|:------------------------------------------|
| 0.570 Charge Frac | 0.570                                     |
| 0.709 Charge Frac | 0.709                                     |
| 0.848 Charge Frac | 0.848                                     |
| 0.988 Charge Frac | 0.988                                     |
| 1.127 Charge Frac | 1.127                                     |
| 1.266 Charge Frac | 1.266                                     |
| 1.405 Charge Frac | 1.405                                     |
| None              |                                           |

HVAC System Single-Speed AC Charge options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC System Single-Speed AC Charge”. See the OpenStudio-HPXML [Air Distribution](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-air-distribution) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_ss_ac_charge" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `cooling_system_frac_manufacturer_charge` | false | Frac | Double | The fraction of manufacturer recommended charge of the cooling system. |

The ResStock argument definitions set in the HVAC System Single-Speed AC Charge

</div>

#### Distribution Assumption(s)

None.

#### Distribution Assumption(s)

None.

### HVAC System is Scaled

#### Description

Whether the HVAC system has been undersized or oversized (not used in baseline) compared to what was autosized using ACCA Manual J and Manual S.

#### Distribution Data Source(s)

This is currently a capability that is not used. ResStock assumes no oversizing or undersizing, until we have the data necessary to characterize all types of systems.

#### Direct Conditional Dependencies

None.

#### Options

All buildings assigned an option of “No” with no associated ResStock arguments.

#### Distribution Assumption(s)

None.

### HVAC System is Faulted

#### Description

The presence of an HVAC system giving a fault or error. Note: this is a capability but is not used in baseline ResStock.

#### Distribution Data Source(s)

N/A.

#### Direct Conditional Dependencies

None.

#### Options

All homes currently set to “No” with no associated ResStock arguments.

#### Distribution Assumption(s)

None.

## Ventilation

### Modeling Approach

Mechanical ventilation, natural ventilation, and local ventilation fans (bath fan, range fan) can be modeled in ResStock. There is currently no mechanical ventilation in the baseline. The bath fan and range fan operate for one hour a day according to the daily hourly schedule specified in the Bathroom Spot Vent Hour and Range Spot Vent Hour characteristics. In aggregate, the distributions of the Bathroom Spot Vent Hour and Range Spot Vent Hour characteristics provide an average schedule for a group of housing units. For default, constraints, and notes about the modeling approach see [OpenStudio-HPXML Local Ventilation Fans](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-local-ventilation-fans) documentation. Natural ventilation (through opening the windows) is allowed during the Cooling Season under certain outside conditions set by the 2010 House Simulation Protocols ((Hendron and Engebrecht 2010)). When ventilating, 1/3 of the operable windows are open for natural ventilation ((Hendron and Engebrecht 2010)).

Four different input files influence ventilation in ResStock:

- Mechanical Ventilation

- Natural Ventilation

- Bathroom Spot Vent Hour

- Range Spot Vent Hour.

Mechanical ventilation is currently not used in the baseline, and natural ventilation has a single option assigned to all homes. Bathroom Spot Vent Hour and Range Spot Vent Hour provide diversity in the schedules of operation of localized bathroom and cooking ventilation, respectively.

### Mechanical Ventilation

#### Description

Mechanical ventilation type and efficiency.

#### Distribution Data Source(s)

Engineering judgment.

#### Direct Conditional Dependencies

None.

#### Options

In the baseline, no homes are assigned mechanical ventilation, so only the option “None” is used and all arguments are set to None or 0:

- `mech_vent_fan_type`: none

- `mech_vent_flow_rate`: 0

- `mech_vent_hours_in_operation`: 0

- `mech_vent_recovery_efficiency_type`: unadjusted

- `mech_vent_total_recovery_efficiency`: 0

- `mech_vent_sensible_recovery_efficiency`: 0

- `mech_vent_fan_power`: 0

- `mech_vent_num_units_served`: 0

- `mech_vent_shared_frac_recirculation`: auto

- `mech_vent_shared_preheating_fuel`: auto

- `mech_vent_shared_preheating_efficiency`: auto

- `mech_vent_shared_preheating_fraction_heat_load_served`: auto

- `mech_vent_shared_precooling_fuel`: auto

- `mech_vent_shared_precooling_efficiency`: auto

- `mech_vent_shared_precooling_fraction_cool_load_served`: auto

- `mech_vent_2_fan_type` : none

- `mech_vent_2_flow_rate`: 0

- `mech_vent_2_hours_in_operation`: 0

- `mech_vent_2_recovery_efficiency_type`: unadjusted

- `mech_vent_2_total_recovery_efficiency`: 0

- `mech_vent_2_sensible_recovery_efficiency`: 0

- `mech_vent_2_fan_power`: 0

- `whole_house_fan_present`: false

- `whole_house_fan_flow_rate`: 0

- `whole_house_fan_power`: 0.

For the argument definitions, see Table “The ResStock argument definitions set in the Mechanical Ventilation characteristic”. See the OpenStudio-HPXML [Mechanical Ventilation Fans](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-[https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-mechanical-ventilation-fans]) and [Local Ventilation Fans](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-local-ventilation-fans) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_mech_vent" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `mech_vent_fan_type` | true |  | Choice | none, exhaust only, supply only, energy recovery ventilator, heat recovery ventilator, balanced, central fan integrated supply | The type of the mechanical ventilation. Use 'none' if there is no mechanical ventilation system. |
| `mech_vent_flow_rate` | false | CFM | Double | auto | The flow rate of the mechanical ventilation. |
| `mech_vent_hours_in_operation` | false | hrs/day | Double | auto | The hours in operation of the mechanical ventilation. |
| `mech_vent_recovery_efficiency_type` | true |  | Choice | Unadjusted, Adjusted | The total recovery efficiency type of the mechanical ventilation. |
| `mech_vent_total_recovery_efficiency` | true | Frac | Double |  | The Unadjusted or Adjusted total recovery efficiency of the mechanical ventilation. Applies to energy recovery ventilator. |
| `mech_vent_sensible_recovery_efficiency` | true | Frac | Double |  | The Unadjusted or Adjusted sensible recovery efficiency of the mechanical ventilation. Applies to energy recovery ventilator and heat recovery ventilator. |
| `mech_vent_fan_power` | false | W | Double | auto | The fan power of the mechanical ventilation. |
| `mech_vent_num_units_served` | true | \# | Integer |  | Number of housing units served by the mechanical ventilation system. Must be 1 if single-family detached. Used to apportion flow rate and fan power to the unit. |
| `mech_vent_shared_frac_recirculation` | false | Frac | Double |  | Fraction of the total supply air that is recirculated, with the remainder assumed to be outdoor air. The value must be 0 for exhaust only systems. Required for a shared mechanical ventilation system. |
| `mech_vent_shared_preheating_fuel` | false |  | Choice | auto, electricity, natural gas, fuel oil, propane, wood, wood pellets, coal | Fuel type of the preconditioning heating equipment. Only used for a shared mechanical ventilation system. If not provided, assumes no preheating. |
| `mech_vent_shared_preheating_efficiency` | false | COP | Double |  | Efficiency of the preconditioning heating equipment. Only used for a shared mechanical ventilation system. If not provided, assumes no preheating. |
| `mech_vent_shared_preheating_fraction_heat_load_served` | false | Frac | Double |  | Fraction of heating load introduced by the shared ventilation system that is met by the preconditioning heating equipment. If not provided, assumes no preheating. |
| `mech_vent_shared_precooling_fuel` | false |  | Choice | auto, electricity | Fuel type of the preconditioning cooling equipment. Only used for a shared mechanical ventilation system. If not provided, assumes no precooling. |
| `mech_vent_shared_precooling_efficiency` | false | COP | Double |  | Efficiency of the preconditioning cooling equipment. Only used for a shared mechanical ventilation system. If not provided, assumes no precooling. |
| `mech_vent_shared_precooling_fraction_cool_load_served` | false | Frac | Double |  | Fraction of cooling load introduced by the shared ventilation system that is met by the preconditioning cooling equipment. If not provided, assumes no precooling. |
| `mech_vent_2_fan_type` | true |  | Choice | none, exhaust only, supply only, energy recovery ventilator, heat recovery ventilator, balanced | The type of the second mechanical ventilation. Use 'none' if there is no second mechanical ventilation system. |
| `mech_vent_2_flow_rate` | true | CFM | Double |  | The flow rate of the second mechanical ventilation. |
| `mech_vent_2_hours_in_operation` | true | hrs/day | Double |  | The hours in operation of the second mechanical ventilation. |
| `mech_vent_2_recovery_efficiency_type` | true |  | Choice | Unadjusted, Adjusted | The total recovery efficiency type of the second mechanical ventilation. |
| `mech_vent_2_total_recovery_efficiency` | true | Frac | Double |  | The Unadjusted or Adjusted total recovery efficiency of the second mechanical ventilation. Applies to energy recovery ventilator. |
| `mech_vent_2_sensible_recovery_efficiency` | true | Frac | Double |  | The Unadjusted or Adjusted sensible recovery efficiency of the second mechanical ventilation. Applies to energy recovery ventilator and heat recovery ventilator. |
| `mech_vent_2_fan_power` | true | W | Double |  | The fan power of the second mechanical ventilation. |
| `whole_house_fan_present` | true |  | Boolean | true, false | Whether there is a whole house fan. |
| `whole_house_fan_flow_rate` | false | CFM | Double | auto | The flow rate of the whole house fan. |

The ResStock argument definitions set in the Mechanical Ventilation characteristic

</div>

#### Distribution Assumption(s)

None.

### Natural Ventilation

#### Description

Amount and schedule of natural ventilation through operable windows.

#### Distribution Data Source(s)

Building America House Simulation Protocols ((E. Wilson et al. 2014a)).

#### Direct Conditional Dependencies

None.

#### Options

All homes are currently set to the same natural ventilation option.

<div id="table:hc_opt_hvac_sec_ht" data-source="3b_ResStockInputs_HVAC.tex">

| Option name               | `window_fraction_operable` |
|:--------------------------|:---------------------------|
| Cooling Season, 7 days/wk | 0.67                       |

Natural Ventilation options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Natural Ventilation characteristic”. See the OpenStudio-HPXML [Natural Ventilation](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#natural-ventilation) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_nat_vent" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `window_fraction_operable` | false | Frac | Double | auto | Fraction of windows that are operable. |

The ResStock argument definitions set in the Natural Ventilation characteristic

</div>

#### Distribution Assumption(s)

None.

### Bathroom Spot Vent Hour

#### Description

Bathroom spot ventilation daily start hour. In ResStock, the bathroom fan(s) operates for 1 hour everyday. A schedule is generated on the fly based on these inputs.

#### Distribution Data Source(s)

Same as occupancy schedule from the Building America House Simulation Protocols ((E. Wilson et al. 2014a)).

#### Direct Conditional Dependencies

None.

#### Options

The start hours are spread out over all 24 hours of the day (Table “Bathroom Spot Vent Hour options and arguments that vary for each option”). The following ResStock arguments are constant across all options:

- `bathroom_fans_quantity`: auto

- `bathroom_fans_flow_rate`: auto

- `bathroom_fans_hours_in_operation`: auto

- `bathroom_fans_power`: auto.

<div id="table:hc_opt_bath_vent" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `bathroom_fans_start_hour` |
|:------------|:---------------------------|
| Hour0       | 0                          |
| Hour1       | 1                          |
| Hour2       | 2                          |
| Hour3       | 3                          |
| Hour4       | 4                          |
| Hour5       | 5                          |
| Hour6       | 6                          |
| Hour7       | 7                          |
| Hour8       | 8                          |
| Hour9       | 9                          |
| Hour10      | 10                         |
| Hour11      | 11                         |
| Hour12      | 12                         |
| Hour13      | 13                         |
| Hour14      | 14                         |
| Hour15      | 15                         |
| Hour16      | 16                         |
| Hour17      | 17                         |
| Hour18      | 18                         |
| Hour19      | 19                         |
| Hour20      | 20                         |
| Hour21      | 21                         |
| Hour22      | 22                         |
| Hour23      | 23                         |

Bathroom Spot Vent Hour options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Bathroom Spot Vent Hour characteristic”. See the OpenStudio-HPXML [Local Ventilation Fans](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-local-ventilation-fans) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_bath_vent" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `bathroom_fans_quantity` | false | \# | Integer | auto | The quantity of the bathroom fans. |
| `bathroom_fans_flow_rate` | false | CFM | Double | auto | The flow rate of the bathroom fans. |
| `bathroom_fans_hours_in_operation` | false | hrs/day | Double | auto | The hours in operation of the bathroom fans. |
| `bathroom_fans_power` | false | W | Double | auto | The fan power of the bathroom fans. |
| `bathroom_fans_start_hour` | false | hr | Integer | auto | The start hour of the bathroom fans. |

The ResStock argument definitions set in the Bathroom Spot Vent Hour characteristic

</div>

#### Distribution Assumption(s)

None.

### Range Spot Vent Hour

#### Description

Range spot ventilation daily start hour. In ResStock, the range hood operates for 1 hour every day. A schedule is generated on the fly for range spot ventilation based on these inputs.

#### Distribution Data Source(s)

Derived from national average cooking range schedule in Building America House Simulation Protocols ((E. Wilson et al. 2014a)).

#### Direct Conditional Dependencies

None.

#### Options

Start hours are spread across all hours of the day (Table “Range Spot Vent Hour options and arguments that vary for each option”). Across the options the following ResStock arguments are constant:

- `kitchen_fans_quantity`: auto

- `kitchen_fans_flow_rate`: auto

- `kitchen_fans_hours_in_operation`: auto

- `kitchen_fans_power`: auto.

<div id="table:hc_opt_range_vent" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `kitchen_fans_start_hour` |
|:------------|:--------------------------|
| Hour0       | 0                         |
| Hour1       | 1                         |
| Hour2       | 2                         |
| Hour3       | 3                         |
| Hour4       | 4                         |
| Hour5       | 5                         |
| Hour6       | 6                         |
| Hour7       | 7                         |
| Hour8       | 8                         |
| Hour9       | 9                         |
| Hour10      | 10                        |
| Hour11      | 11                        |
| Hour12      | 12                        |
| Hour13      | 13                        |
| Hour14      | 14                        |
| Hour15      | 15                        |
| Hour16      | 16                        |
| Hour17      | 17                        |
| Hour18      | 18                        |
| Hour19      | 19                        |
| Hour20      | 20                        |
| Hour21      | 21                        |
| Hour22      | 22                        |
| Hour23      | 23                        |

Range Spot Vent Hour options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Range Spot Vent Hour characteristic”. See the OpenStudio-HPXML [Local Ventilation](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-local-ventilation-fans) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_range_fan" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `kitchen_fans_quantity` | false | \# | Integer | auto | The quantity of the kitchen fans. |
| `kitchen_fans_flow_rate` | false | CFM | Double | auto | The flow rate of the kitchen fan. |
| `kitchen_fans_hours_in_operation` | false | hrs/day | Double | auto | Hours per day of operation. |
| `kitchen_fans_power` | false | W | Double | auto | The fan power of the kitchen fan. |
| `kitchen_fans_start_hour` | false | hr | Integer | auto | The start hour of the kitchen fan. |

The ResStock argument definitions set in the Range Spot Vent Hour characteristic

</div>

#### Distribution Assumption(s)

None.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-bahsp_2010" class="csl-entry">

Hendron, Robert, and Cheryn Engebrecht. 2010. *Building America House Simulation Protocols*. US DOE: Office of Energy Efficiency; Renewable Energy. <https://www1.eere.energy.gov/buildings/publications/pdfs/building_america/house_simulation.pdf>.

</div>

<div id="ref-Wilson2014" class="csl-entry">

Wilson, E., C. Engebrecht Metzger, S. Horowitz, and R. Hendron. 2014a. *2014 Building America House Simulation Protocols*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy14osti/60988.pdf>.

</div>

<div id="ref-bahsp_2014" class="csl-entry">

Wilson, E, C Engebrecht Metzger, S Horowitz, and R Hendron. 2014b. *2014 Building America House Simulation Protocols*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy14osti/60988.pdf>.

</div>

<div id="ref-Winkler2020" class="csl-entry">

Winkler, Jon, Saptarshi Das, Lieko Earle, et al. 2020. “Impact of Installation Faults in Air Conditioners and Heat Pumps in Single-Family Homes on u.s. Energy Usage.” *Applied Energy* 278: 115533. https://doi.org/<https://doi.org/10.1016/j.apenergy.2020.115533>.

</div>

</div>
