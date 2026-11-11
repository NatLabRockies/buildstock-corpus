<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Clothes Washer | lines: 1282-1514 -->
## Clothes Washer

### Modeling Approach

ResStock models all clothes washers as a standalone appliance located in the conditioned space with hot water supplied by the water heater. Clothes Washer Presence defines whether the appliance is present in the housing unit and is created to influence the Clothes Dryer (Section “Clothes Dryer”) presence as a dependency. Clothes washer performance is defined by integrated modified Energy Factor along with other EnergyGuide label information, including rated annual kWh, capacity (volume), label usage (cycles per week), electric and gas rate, and annual gas cost.

The number of cycles is used to calculate the annual energy and hot water use for clothes washer per the Energy Rating Rated Home in ANSI/RESNET/ICC 301-2019 Addendum A ((International Code Council 2019)). The total energy and hot water use are further adjusted by a Clothes Washer Usage Level multiplier for added diversity.

The energy estimate is multiplied with a stochastically generated laundry schedule to produce the clothes washer end-use load profile. Similarly, the total hot water use is paired with a stochastic schedule to produce an appliance hot water draw schedule for the water heater. The appliance schedule and the hot water draw schedule line up in terms of the event onset, which comes from ATUS, but not the duration or magnitude, which are sampled from data from the RBSA survey ((Northwest Energy Efficiency Alliance 2024)). See Section “Schedule Creation” for details on schedule generation. The hot water energy for clothes washer is attributed to the hot water end use rather than the appliance.

The following subsections describe the characteristics, the distributions, assumptions, data sources, options, and argument assignments for clothes washers.

### Clothes Washer

#### Description

Presence and rated efficiency of the clothes washer.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Clothes Washer Presence

- Federal Poverty Level

- Geometry Building Type RECS

- Tenure

- Vintage.

#### Options

ResStock has two clothes washer options in baseline, along with a “None” option. Both clothes washer options have a `clothes_washer_location` of *auto*, a `clothes_washer_efficiency_type` of *IntegratedModifiedEnergyFactor*, a `clothes_washer_label_electric_rate` of 0.1065, a `clothes_washer_gas_rate` of 1.218, and a `clothes_washer_label_usage` of 7.538462. The arguments that differ between the two options are shown in Table “Clothes Washer options and arguments that vary for each option”.

<div id="table:opt_def_clothes washer" data-source="3c_ResStockInputs.tex">

| Option name | `clothes_washer_efficiency` | `clothes_washer_rated_annual_kwh` | `clothes_washer_label_annual_gas_cost` | `clothes_washer_capacity` |
|:---|:---|:---|:---|:---|
| ENERGY STAR | 2.07 | 123 | 9 | 3.68 |
| None | 0 | 0 | 0 | 0 |
| Standard | 0.95 | 387 | 24 | 3.5 |

Clothes Washer options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Clothes Washer characteristic”. See the OpenStudio-HPXML [Clothes Washer](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-clothes-washer) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_clothes washer" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `clothes_washer_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, garage, other housing unit, other heated space, other multifamily buffer space, other non-freezing space | The space type for the clothes washer location. |
| `clothes_washer_efficiency_type` | true |  | Choice | ModifiedEnergyFactor, IntegratedModifiedEnergyFactor | The efficiency type of the clothes washer. |
| `clothes_washer_efficiency` | false | ft<sup>3</sup>/kWh-cyc | Double | auto | The efficiency of the clothes washer. |
| `clothes_washer_rated_annual_kwh` | false | kWh/yr | Double | auto | The annual energy consumed by the clothes washer, as rated, obtained from the EnergyGuide label. This includes both the appliance electricity consumption and the energy required for water heating. If not provided, the OS-HPXML default (see [HPXML Clothes Washer](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-clothes-washer)) is used. |
| `clothes_washer_label_electric_rate` | false | \$/kWh | Double | auto | The annual energy consumed by the clothes washer, as rated, obtained from the EnergyGuide label. This includes both the appliance electricity consumption and the energy required for water heating. |
| `clothes_washer_label_gas_rate` | false | \$/therm | Double | auto | The annual energy consumed by the clothes washer, as rated, obtained from the EnergyGuide label. This includes both the appliance electricity consumption and the energy required for water heating. If not provided, the OS-HPXML default (see [HPXML Clothes Washer](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-clothes-washer)) is used. |
| `clothes_washer_label_annual_gas_cost` | false | \$ | Double | auto | The annual cost of using the system under test conditions. Input is obtained from the EnergyGuide label. |
| `clothes_washer_label_usage` | false | cyc/wk | Double | auto | The clothes washer loads per week. |
| `clothes_washer_capacity` | false | ft^3 | Double | auto | Volume of the washer drum. Obtained from the ENERGY STAR website or the manufacturer’s literature. |

The ResStock argument definitions set in the Clothes Washer characteristic

</div>

#### Distribution Assumption(s)

The 2020 RECS survey does not contain ENERGY STAR rating of clothes washers. ENERGY STAR efficiency distributions with Geometry Building Type, Federal Poverty Level, and Tenure as dependencies are imported from RECS 2009. Due to low sample count, the input file is constructed by downscaling a housing unit sub-input file with a household sub-input file. The sub-input files have the following dependencies: housing unit sub-input file: dependencies = Geometry Building Type RECS, State, Clothes Washer Presence, and Vintage, with the following coarsening order:

1.  Geometry Building Type RECS coarsened to SF/MF/MH

2.  Geometry Building Type RECS coarsened to SF and MH/MF

3.  Vintage coarsened to every 20 years before 2000 and every 10 years subsequently

4.  Vintage homes built before 1960 coarsened to pre-1960

5.  Vintage homes built after 2000 coarsened to 2000-20.

Household sub-input file: dependencies = Geometry Building Type RECS, State, Tenure, and Federal Poverty Level, with the following coarsening order:

1.  Geometry Building Type RECS coarsened to SF/MF/MH

2.  Geometry Building Type RECS coarsened to SF and MH/MF

3.  Federal Poverty Level coarsened every 100%

4.  Federal Poverty Level coarsened every 200%.

In combining the housing unit sub-input file and household sub-input file, the conditional relationships are ignored across Clothes Washer Presence and Vintage, as well as for Tenure and Federal Poverty Level.

### Clothes Washer Presence

#### Description

The presence of a clothes washer in the housing unit.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- State

- Tenure

- Vintage.

#### Options

This characteristic determines whether there is a clothes washer present in the housing unit. The characteristic sets the `clothes_washer_present` ResStock argument (Table “Clothes Washer Presence options and arguments that vary for each option”).

<div id="table:opt_def_clothes_washer" data-source="3c_ResStockInputs.tex">

| Option name | `clothes_washer_present` |
|:------------|:-------------------------|
| None        | false                    |
| Yes         | true                     |

Clothes Washer Presence options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Clothes Washer Presence characteristic”.

<div id="table:hc_arg_def_clothes_washer_presence" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `clothes_washer_present` | true |  | Boolean | true, false | Whether there is a clothes washer present. |

The ResStock argument definitions set in the Clothes Washer Presence characteristic

</div>

#### Distribution Assumption(s)

Due to the low sample count, the input file is constructed by downscaling a housing unit sub-input file with a household sub-input file. The sub-input files have the following dependencies. Housing unit sub-input file: dependencies = Geometry Building Type RECS, State, Heating Fuel, and Vintage, with the following coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Vintage coarsened to every 20 years before 2000 and every 10 years subsequently

5.  Vintage homes built before 1960 coarsened to pre-1960

6.  Vintage homes built after 2000 coarsened to 2000-20

7.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

8.  Census Division RECS to Census Region

9.  Census Region to National.

Household sub-input file: dependencies = Geometry Building Type RECS, State, Tenure, and Federal Poverty Level, with the following coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

7.  Census Division RECS to Census Region

8.  Census Region to National.

In combining the housing unit sub-input file and household sub-input file, the conditional relationships are ignored across Geometry Building Type RECS and Vintage, as well as for Tenure and Federal Poverty Level.

### Clothes Washer Usage Level

#### Description

Clothes washer energy usage level multiplier.

#### Distribution Data Source(s)

Not applicable.

#### Direct Conditional Dependencies

- Usage Level.

#### Options

The clothes washer usage level is set based on the usage level (Section “Usage”) characteristic. It is 80% Usage when the usage level is Low, 100% Usage when the usage level is Medium, and 120% Usage when the usage level is High. The characteristic sets the `clothes_washer_usage_multiplier` ResStock argument (Table “Clothes Washer Usage Level options and arguments that vary for each option”).

<div id="table:opt_def_clothes_washer_use" data-source="3c_ResStockInputs.tex">

| Option name | `clothes_washer_usage_multiplier` |
|:------------|:----------------------------------|
| 80% Usage   | 0.8                               |
| 100% Usage  | 1.0                               |
| 120% Usage  | 1.2                               |

Clothes Washer Usage Level options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Clothes Washer Usage Level characteristic”.

<div id="table:hc_arg_def_clothes_washer_usage_level" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `clothes_washer_usage_multiplier` | false |  | Double | auto | Multiplier on the clothes washer energy and hot water usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Clothes Washer Usage Level characteristic

</div>

#### Distribution Assumption(s)

- Engineering judgment.

