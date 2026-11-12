<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Dishwasher | lines: 1142-1281 -->
## Dishwasher

### Modeling Approach

ResStock models all dishwashers as a standalone appliance located in the conditioned space with hot water supplied by the water heater. Housing units can have no dishwasher. Dishwasher performance is defined by rated annual kWh along with other EnergyGuide label information, including place setting capacity assumed to be 12, label usage (cycles per week), electric and gas rate, and annual gas cost. The number of cycles is used to calculate the annual energy and hot water use for dishwasher per the Energy Rating Rated Home in ANSI/RESNET/ICC 301-2019 Addendum A ((International Code Council 2019)). The total energy and hot water use are further adjusted by a Dishwasher Usage Level multiplier (Section “Dishwasher Usage Level”) for added diversity.

The energy estimate is multiplied with a stochastically generated appliance schedule to produce the dishwasher end-use load profile. Similarly, the total hot water use is paired with a stochastic schedule to produce an appliance hot water draw schedule for the water heater. The appliance schedule and the hot water draw schedule line up in terms of the event onset, which comes from ATUS, but not the duration or magnitude, which are sampled from data from the RBSA survey ((Northwest Energy Efficiency Alliance 2024)). See Section “Schedule Creation” for details on schedule generation. The hot water energy for dishwasher is attributed to the hot water end use rather than the appliance.

The following subsections describe the characteristics, distributions, data sources, and arguments assigned for the dishwasher.

### Dishwasher

#### Description

The presence and rated efficiency of the dishwasher.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- State

- Tenure

- Vintage.

#### Options

The ResStock baseline has two dishwasher options, one at 290 rated kWh and one at 318 rated kWh, along with a “None” option.[^4] Both dishwasher options have arguments of true for `dishwasher_present`, auto for `dishwasher_location`, RatedAnnualkWh for `dishwasher_efficiency_type`, 0.12 for `dishwasher_label_electric_rate`, 1.09 for `dishwasher_label_gas_rate`, 4 for `dishwasher_label_usage`, and 12 for `dishasher_place_setting_capacity`; see Table “Dishwasher options and arguments that vary for each option”.

<div id="table:hc_opt_dish" data-source="3c_ResStockInputs.tex">

| Option name   | `dishwasher_efficiency` | `dishwasher_label_annual_gas_cost` |
|:--------------|:------------------------|:-----------------------------------|
| 290 Rated kWh | 290                     | 23                                 |
| 318 Rated kWh | 318                     | 25                                 |
| None          | 0                       | 0                                  |

Dishwasher options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Dishwasher characteristic”. See the OpenStudio-HPXML [Dishwasher](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-dishwasher) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_dishwasher" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `dishwasher_present` | true |  | Boolean | true, false | Whether there is a dishwasher present. |
| `dishwasher_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, garage, other housing unit, other heated space, other multifamily buffer space, other non-freezing space | The space type for the dishwasher location. |
| `dishwasher_efficiency_type` | true |  | Choice | RatedAnnualkWh, EnergyFactor | The efficiency type of dishwasher. |
| `dishwasher_efficiency` | false | RatedAnnualkWh or EnergyFactor | Double | auto | The efficiency of the dishwasher. |
| `dishwasher_label_electric_rate` | false | \$/kWh | Double | auto | The label electric rate of the dishwasher. |
| `dishwasher_label_gas_rate` | false | \$/therm | Double | auto | The label gas rate of the dishwasher. |
| `dishwasher_label_annual_gas_cost` | false | \$ | Double | auto | The label annual gas cost of the dishwasher. |
| `dishwasher_label_usage` | false | cyc/wk | Double | auto | The dishwasher loads per week. |
| `dishwasher_place_setting_capacity` | false | \# | Integer | auto | The number of place settings for the unit. Data obtained from manufacturer’s literature. |

The ResStock argument definitions set in the Dishwasher characteristic

</div>

#### Distribution Assumption(s)

The 2020 RECS survey does not contain ENERGY STAR rating of dishwashers. ENERGY STAR efficiency distributions with Geometry Building Type, Census Division RECS, Federal Poverty Level, and Tenure as dependencies are imported from RECS 2009.

Due to the low sample count, the input file is constructed with the following coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  Vintage coarsened to every 20 years before 2000 and every 10 years subsequently

7.  Vintage homes built before 1960 coarsened to pre-1960

8.  Vintage homes built after 2000 coarsened to 2000-20

9.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

10. Census Division RECS to Census Region.

### Dishwasher Usage Level

#### Description

Dishwasher energy usage level multiplier.

#### Distribution Data Source(s)

- Not applicable—direct translation of Usage Level; see Section “Usage”.

#### Direct Conditional Dependencies

- Usage Level.

#### Options

The dishwasher usage level is set based on the usage level characteristic; see Section “Usage”. It is 80% Usage when the usage level is Low, 100% Usage when the usage level is Medium, and 120% Usage when the usage level is High. The characteristic sets the `dishwasher_usage_multiplier` ResStock argument (Table “Dishwasher Usage Level options and arguments that vary for each option”).

<div id="table:hc_opt_dish_use" data-source="3c_ResStockInputs.tex">

| Option name | `dishwasher_usage_multiplier` |
|:------------|:------------------------------|
| 80% Usage   | 0.8                           |
| 100% Usage  | 1.0                           |
| 120% Usage  | 1.2                           |

Dishwasher Usage Level options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Dishwasher Usage Level characteristic”.

<div id="table:hc_arg_def_dishwasher_usage_level" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `dishwasher_usage_multiplier` | false |  | Double | auto | Multiplier on the dishwasher energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Dishwasher Usage Level characteristic

</div>

#### Distribution Assumption(s)

None.

