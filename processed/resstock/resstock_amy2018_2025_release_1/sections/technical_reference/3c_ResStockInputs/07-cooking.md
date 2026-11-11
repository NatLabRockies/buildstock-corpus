<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Cooking | lines: 980-1141 -->
## Cooking

### Modeling Approach

ResStock models all cooking units as ranges with an integrated (non-convection) oven located in the conditioned space. Housing units can have no cooking units. The fuel options include electric induction, electric resistance, gas, and propane, although more fuel options are available in OpenStudio-HPXML, see [Cooling Range/Oven](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-cooking-range-oven). The annual energy used for cooking is calculated per the Energy Rating Rated Home in ANSI/RESNET/ICC 301-2019 ((International Code Council 2019)) and is further adjusted by a Cooking Range Usage Level multiplier; see Section “Cooking Range Usage Level”. The annual energy is multiplied with a stochastically generated detailed cooking schedule based on ATUS to produce the cooking end-use load profile. See Section “Schedule Creation” for details on schedule generation.

ResStock also models the use of a range hood for cooking. However, the range hood operation does not use the cooking schedule. Instead, the range operates for one hour every day with a starting hour sampled by the Range Spot Vent Hour characteristic distribution; see Section “Range Spot Vent Hour”.

The next sections describe the building stock distributions for cooking, their assumptions, data sources, and argument assignment.

### Cooking Range

#### Description

Presence and fuel type of the cooking range.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- Heating Fuel

- State

- Tenure

- Vintage.

#### Options

ResStock baseline has four cooking range options, which include electric induction, electric resistance, natural gas, and propane, as well as a “none” option. The characteristic assigns the `cooking_range_oven_present`, `cooking_range_oven_location`, `cooking_range_oven_fuel_type`, `cooking_range_oven_is_induction`, `cooking_range_oven_is_convection` ResStock arguments (Table “Cooking Range options and arguments that vary for each option”). The `cooking_range_oven_is_convection` and `cooking_range_oven_location` is always set to auto.

<div id="table:hc_opt_cooking" data-source="3c_ResStockInputs.tex">

| Option name | `cooking_range_oven_present` | `cooking_range_oven_fuel_type` | `cooking_range_oven_is_induction` |
|:---|:---|:---|:---|
| Electric Induction | true | electricity | true |
| Electric Resistance | true | electricity | false |
| Gas | true | natural gas | false |
| None | false | natural gas | false |
| Propane | true | propane | false |

Cooking Range options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Cooking Range characteristic”. See the OpenStudio-HPXML [Cooking Range/Oven](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-cooking-range-oven) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_cooking_range" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `cooking_range_oven_present` | true |  | Boolean | true, false | Whether there is a cooking range/oven present. |
| `cooking_range_oven_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, garage, other housing unit, other heated space, other multifamily buffer space, other non-freezing space | The space type for the cooking range/oven location. |
| `cooking_range_oven_fuel_type` | true |  | Choice | electricity, natural gas, fuel oil, propane, wood, coal | Type of fuel used by the cooking range/oven. |
| `cooking_range_oven_is_induction` | false |  | Boolean | auto, true, false | Whether the cooking range is induction. |
| `cooking_range_oven_is_convection` | false |  | Boolean | auto, true, false | Whether the oven is convection. |

The ResStock argument definitions set in the Cooking Range characteristic

</div>

#### Distribution Assumption(s)

For Dual Fuel Range, the distribution is split equally between Electric and Natural Gas.

Due to low sample count, the input file is constructed by downscaling a housing unit sub-input file with a household sub-input file. The sub-input files have the following dependencies: housing unit sub-input file: deps = ‘Geometry Building Type RECS’, ‘State’, ‘Heating Fuel’, and ‘Vintage,’ with the following fallback coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Heating Fuel coarsened to Other Fuel, Wood and Propane combined

3.  Heating Fuel coarsened to Fuel Oil, Other Fuel, Wood and Propane combined

4.  Geometry Building Type RECS coarsened to SF/MF/MH

5.  Geometry Building Type RECS coarsened to SF and MH/MF

6.  Vintage coarsened to every 20 years before 2000 and every 10 years subsequently

7.  Vintage homes built before 1960 coarsened to pre-1960

8.  Vintage homes built after 2000 coarsened to 2000-20

9.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

10. Census Division RECS to Census Region

11. Census Region to National.

Household sub-input file : deps = ‘Geometry Building Type RECS’, ‘State’ ‘Tenure’, ‘Federal Poverty Level,’ with the following fallback coarsening order

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

7.  Census Division RECS to Census Region

8.  Census Region to National.

In combining the housing unit sub-input file and household sub-input file, the conditional relationships are ignored across ‘Heating Fuel’ and ‘Vintage’, as well as for ‘Tenure’ and ‘Federal Poverty Level’.

### Cooking Range Usage Level

#### Description

Cooking range energy usage level multiplier.

#### Distribution Data Source(s)

- Not applicable—direct translation of the Usage Level input file; see Section “Usage”.

#### Direct Conditional Dependencies

- Usage Level.

#### Options

The cooking range usage level is set based on the usage level characteristic (Section “Usage”). It is 80% Usage when the usage level is Low, 100% Usage when the usage level is Medium, and 120% Usage when the usage level is High. The characteristic sets the `cooking_range_oven_usage_multiplier` ResStock argument.

<div id="table:hc_opt_cooking" data-source="3c_ResStockInputs.tex">

| Option name | `cooking_range_oven_usage_multiplier` |
|:------------|:--------------------------------------|
| 80% Usage   | 0.8                                   |
| 100% Usage  | 1.0                                   |
| 120% Usage  | 1.2                                   |

Cooking Range Usage Level options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Cooking Range characteristic”. See the [OpenStudio-HPXML Refrigerators](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-refrigerators) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_cooking_range_usage_level" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `cooking_range_oven_usage_multiplier` | false |  | Double | auto | Multiplier on the cooking range/oven energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Cooking Range characteristic

</div>

#### Distribution Assumption(s)

None.

