<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Plug Loads | lines: 2692-2783 -->
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

