<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Additional Capabilities | lines: 2364-2451 -->
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

