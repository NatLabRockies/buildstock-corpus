<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/3b_ResStockInputs_HVAC.md | section: Secondary Heating | lines: 403-629 -->
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

