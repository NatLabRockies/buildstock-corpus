<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Miscellaneous Gas Uses | lines: 2099-2204 -->
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

