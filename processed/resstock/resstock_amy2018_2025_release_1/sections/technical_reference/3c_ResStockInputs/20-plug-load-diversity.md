<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Plug Load Diversity | lines: 2784-2832 -->
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

