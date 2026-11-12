<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Lighting Characteristics | lines: 2470-2691 -->
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

