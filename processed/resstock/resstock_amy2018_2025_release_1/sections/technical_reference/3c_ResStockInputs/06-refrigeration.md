<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Refrigeration | lines: 553-979 -->
## Refrigeration

### Modeling Approach

Refrigeration energy is modeled for both refrigerators and standalone freezers. Each of these appliances is modeled by specifying the rated annual energy and a usage multiplier. There are primary refrigerators and, sometimes, a secondary refrigerator (misc extra refrigerator). Only up to two refrigerators and up to one standalone freezer are modeled. To account for additional refrigeration, correction factors derived using the count of refrigerators (which includes mini-fridges) and freezers from RECS 2020 are applied to each state. The timeseries schedules are handled by OpenStudio-HPXML. Currently, there are weekday and weekend schedules, and monthly multipliers.

### Refrigerator

#### Description

The presence and rated efficiency of the primary refrigerator.

#### Distribution Data Source(s)

Constructed using U.S. EIA 2020 RECS microdata. Age of refrigerator converted to efficiency levels using ENERGY STAR shipment-weighted efficiencies by year data from Home Energy Saver.[^2]

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- State

- Tenure

- Vintage.

#### Options

ResStock differentiates primary refrigerators based on their efficiency level. In the baseline stock, there are seven discrete efficiency levels ranging from EF 6.7 to EF 21.9, as well as a “None” option for housing units that do not have a refrigerator. The Refrigerator characteristic sets the `refrigerator_present`, `refrigerator_location`, and `refrigerator_rated_annual_kwh` arguments (Table “Refrigerator options and arguments that vary for each option”). The `refrigerator_location` argument is set to auto.

<div id="table:hc_opt_ref" data-source="3c_ResStockInputs.tex">

| Option name | `refrigerator_present` | `refrigerator_rated_annual_kwh` |
|:------------|:-----------------------|:--------------------------------|
| EF 6.7      | true                   | 1139                            |
| EF 10.2     | true                   | 748                             |
| EF 10.5     | true                   | 727                             |
| EF 15.9     | true                   | 480                             |
| EF 17.6     | true                   | 433                             |
| EF 19.9     | true                   | 383                             |
| EF 21.9     | true                   | 348                             |
| None        | false                  | 0                               |

Refrigerator options and arguments that vary for each option

</div>

For the argument definitions, see “The ResStock argument definitions set in the Refrigerator characteristic”. See the [OpenStudio-HPXML Refrigerators](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-refrigerators) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_refrigerator" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `refrigerator_present` | true |  | Boolean | true, false | Whether there is a refrigerator present. |
| `refrigerator_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, garage, other housing unit, other heated space, other multifamily buffer space, other non-freezing space | The space type for the refrigerator location. If not provided, the OS-HPXML default (see [HPXML Refrigerators](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-refrigerators)) is used. |
| `refrigerator_rated_annual_kwh` | false | kWh/yr | Double | auto | The EnergyGuide rated annual energy consumption for a refrigerator. |

The ResStock argument definitions set in the Refrigerator characteristic

</div>

#### Distribution Assumption(s)

The current year is assumed to be 2022. Currently, each year has its own distribution and then we average out the distributions to get the distribution for the age bins. The Energy Factor for all years are weighted equally when calculating the average distribution for the age bins. ENERGY STAR distributions from 2009 dependent on Geometry Building Type RECS, Federal Poverty Level, and Tenure are used to calculate efficiency distribution in RECS2020. ENERGY STAR Refrigerators are assumed to be 10% more efficient than standard. Due to the low sample count, the following coarsening rules are incorporated.

1.  State coarsened to Census Division RECS, with AK/HI separate.

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Vintage with Vintage ACS

5.  Vintage with combined 1960s

6.  Vintage with combined 1960s and post 2000s

7.  Federal Poverty Level coarsened every 100%

8.  Federal Poverty Level coarsened every 200%

9.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

10. Census Division RECS to Census Region

11. Census Region to National.

### Refrigerator Usage Level

#### Description

Refrigerator energy usage level multiplier.

#### Distribution Data Source(s)

- Not applicable—direct translation of the “Usage” Usage input file.

#### Direct Conditional Dependencies

- Usage Level.

#### Options

The refrigerator usage level is set based on the usage level characteristic. It is 95% Usage when the usage level is Low, 100% Usage when the usage level is Medium, and 105% Usage when the usage level is High. The characteristic sets the `refrigerator_usage_multiplier` argument (Table “Refrigerator options and arguments that vary for each option”).

<div id="table:hc_opt_ref_use" data-source="3c_ResStockInputs.tex">

| Option name | `refrigerator_usage_multiplier` |     |
|:------------|:--------------------------------|:----|
| 95% Usage   | 0.95                            |     |
| 100% Usage  | 1.0                             |     |
| 105% Usage  | 1.05                            |     |

Refrigerator options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Refrigerator Usage Level characteristic”.

<div id="table:hc_arg_def_refrigerator_usage_level" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `refrigerator_usage_multiplier` | false |  | Double | auto | Multiplier on the refrigerator energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Refrigerator Usage Level characteristic

</div>

#### Distribution Assumption(s)

None

### Misc Extra Refrigerator

#### Description

The presence and rated efficiency of the secondary refrigerator.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

- Age of refrigerator converted to efficiency levels using ENERGY STAR shipment-weighted efficiencies by year data from Home Energy Saver.[^3]

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- State

- Tenure

- Vintage.

#### Options

Extra refrigerators are specified using the same Energy Factor (EF) and annual rated kWh options as primary refrigerators. The characteristic set the `extra_refrigerator_present`, `extra_refrigerator_location`, `extra_refrigerator_rated_annual_kwh`, and `extra_refrigerator_usage_multiplier` ResStock arguments (Table “Misc Extra Refrigerator options and arguments that vary for each option”). If an extra refrigerator is present, the location is always set to auto. The usage multiplier varies by state and is set to account for the presence of teriary refrigerators and beyond, see “Misc Extra Refrigerator usage multiplier varies by state.”.

<div id="table:hc_opt_extra_ref" data-source="3c_ResStockInputs.tex">

| Option name | `extra_refrigerator_present` | `extra_refrigerator_rated_annual_kwh` |  |  |
|:---|:---|:---|:---|:---|
| EF 6.7 | true | 1139 |  |  |
| EF 10.2 | true | 748 |  |  |
| EF 10.5 | true | 727 |  |  |
| EF 15.9 | true | 480 |  |  |
| EF 17.6 | true | 433 |  |  |
| EF 19.9 | true | 383 |  |  |
| EF 21.9 | true | 348 |  |  |
| None | false | 0 |  |  |

Misc Extra Refrigerator options and arguments that vary for each option

</div>

<div id="table:hc_opt_extra_ref_usage_mult" data-source="3c_ResStockInputs.tex">

| State | `extra_refrigerator_usage_multiplier` |
|:------|:--------------------------------------|
| AK    | 1.80                                  |
| AL    | 1.76                                  |
| AR    | 1.90                                  |
| AZ    | 1.74                                  |
| CA    | 1.86                                  |
| CO    | 1.85                                  |
| CT    | 1.96                                  |
| DC    | 2.15                                  |
| DE    | 1.68                                  |
| FL    | 1.87                                  |
| GA    | 1.74                                  |
| HI    | 1.94                                  |
| IA    | 1.77                                  |
| ID    | 1.62                                  |
| IL    | 1.82                                  |
| IN    | 1.78                                  |
| KS    | 1.77                                  |
| KY    | 1.80                                  |
| LA    | 1.88                                  |
| MA    | 2.00                                  |
| MD    | 1.94                                  |
| ME    | 1.88                                  |
| MI    | 1.73                                  |
| MN    | 1.72                                  |
| MO    | 1.76                                  |
| MS    | 1.85                                  |
| MT    | 1.69                                  |
| NC    | 1.80                                  |
| ND    | 1.73                                  |
| NE    | 1.85                                  |
| NH    | 1.90                                  |
| NJ    | 1.81                                  |
| NM    | 1.90                                  |
| NV    | 1.87                                  |
| NY    | 1.91                                  |
| OH    | 1.81                                  |
| OK    | 1.86                                  |
| OR    | 1.84                                  |
| PA    | 1.73                                  |
| RI    | 1.91                                  |
| SC    | 1.83                                  |
| SD    | 1.83                                  |
| TN    | 1.86                                  |
| TX    | 1.84                                  |
| UT    | 1.78                                  |
| VA    | 1.80                                  |
| VT    | 1.82                                  |
| WA    | 1.76                                  |
| WI    | 1.74                                  |
| WV    | 1.68                                  |
| WY    | 1.80                                  |

Misc Extra Refrigerator usage multiplier varies by state.

</div>

For the argument definitions, see “The ResStock argument definitions set in the Refrigerator Usage Level characteristic”. See the [OpenStudio-HPXML Refrigerators](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-refrigerators) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_misc_extra_refrigerator" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `extra_refrigerator_present` | true |  | Boolean | true, false | Whether there is an extra refrigerator present. |
| `extra_refrigerator_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, garage, other housing unit, other heated space, other multifamily buffer space, other non-freezing space | The space type for the extra refrigerator location. |
| `extra_refrigerator_rated_annual_kwh` | false | kWh/yr | Double | auto | The EnergyGuide rated annual energy consumption for an extra refrigerator. |
| `extra_refrigerator_usage_multiplier` | false |  | Double | auto | Multiplier on the extra refrigerator energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Refrigerator Usage Level characteristic

</div>

#### Distribution Assumption(s)

The current year is assumed to be 2022. Currently, each year has its own distribution and then we average out the distributions to get the distribution for the age bins. EF for all years are weighted equally when calculating the average distribution for the age bins. ENERGY STAR distributions from 2009 dependent on Geometry Building Type RECS, Federal Poverty Level, and Tenure are used to calculate efficiency distribution in RECS 2020. ENERGY STAR refrigerators assumed to be 10% more efficient than standard. Due to the low sample count, the input file is constructed by downscaling a housing unit sub-input file with a household sub-input file. The sub-input files have the following dependencies: housing unit sub-input file: dependencies = Geometry Building Type RECS, State, and Vintage, with the following fallback coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Vintage with Vintage ACS

5.  Vintage with combined 1960s

6.  Vintage with combined 1960s and post 2000s

7.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

8.  Census Division RECS to Census Region.

Census Region to National Assumption: Household sub-input file : dependencies = Geometry Building Type RECS, State, Tenure, and Federal Poverty Level, with the following fallback coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

7.  Census Division RECS to Census Region

8.  Census Region to National.

In combining the housing unit sub-input file and household sub-input file, the conditional relationships are ignored across (Heating Fuel, \[Tenure, Federal Poverty Level\]).

### Misc Freezer

#### Description

The presence and rated efficiency of a standalone freezer.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- State

- Tenure.

#### Options

The Misc Freezer option in baseline has an EF of 12, intended to represent the national average. The characteristic sets the `freezer_present`, `freezer_location`, `freezer_rated_annual_kwh`, and `freezer_usage_multiplier` ResStock arguments (Table “Misc Freezer options and arguments that vary for each option”). The usage multiplier varies by state and is set to account for the presence of extra freezers, see “Misc Freezer usage multiplier varies by state.”.

<div id="table:hc_opt_freezer" data-source="3c_ResStockInputs.tex">

| Option name | `freezer_present` | `freezer_location` | `freezer_rated_annual_kwh` |
|:---|:---|:---|:---|
| EF 12, National Average | true | auto | 935 |
| None | false | auto | 0 |

Misc Freezer options and arguments that vary for each option

</div>

<div id="table:hc_opt_freezer_usage_mult" data-source="3c_ResStockInputs.tex">

| State | `freezer_usage_multiplier` |
|:------|:---------------------------|
| AK    | 1.27                       |
| AL    | 1.34                       |
| AR    | 1.25                       |
| AZ    | 1.09                       |
| CA    | 1.06                       |
| CO    | 1.06                       |
| CT    | 1.08                       |
| DC    | 1.21                       |
| DE    | 1.12                       |
| FL    | 1.04                       |
| GA    | 1.26                       |
| HI    | 1.21                       |
| IA    | 1.13                       |
| ID    | 1.38                       |
| IL    | 1.07                       |
| IN    | 1.25                       |
| KS    | 1.04                       |
| KY    | 1.19                       |
| LA    | 1.32                       |
| MA    | 1.06                       |
| MD    | 1.20                       |
| ME    | 1.09                       |
| MI    | 1.22                       |
| MN    | 1.27                       |
| MO    | 1.07                       |
| MS    | 1.34                       |
| MT    | 1.33                       |
| NC    | 1.10                       |
| ND    | 1.29                       |
| NE    | 1.19                       |
| NH    | 1.23                       |
| NJ    | 1.05                       |
| NM    | 1.17                       |
| NV    | 1.02                       |
| NY    | 1.06                       |
| OH    | 1.12                       |
| OK    | 1.26                       |
| OR    | 1.39                       |
| PA    | 1.18                       |
| RI    | 0.97                       |
| SC    | 1.13                       |
| SD    | 1.37                       |
| TN    | 1.25                       |
| TX    | 1.18                       |
| UT    | 1.20                       |
| VA    | 1.14                       |
| VT    | 1.25                       |
| WA    | 1.14                       |
| WI    | 1.20                       |
| WV    | 1.15                       |
| WY    | 1.32                       |

Misc Freezer usage multiplier varies by state.

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Refrigerator Usage Level characteristic”. See the [OpenStudio-HPXML Freezers](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-freezers) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_misc_freezer" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `freezer_present` | true |  | Boolean | true, false | Whether there is a freezer present. |
| `freezer_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, garage, other housing unit, other heated space, other multifamily buffer space, other non-freezing space | The space type for the freezer location. |
| `freezer_rated_annual_kwh` | false | kWh/yr | Double | auto | The EnergyGuide rated annual energy consumption for a freezer. |
| `freezer_usage_multiplier` | false |  | Double | auto | Multiplier on the freezer energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Refrigerator Usage Level characteristic

</div>

#### Distribution Assumption(s)

The national average EF is 12 based on the 2014 Building America house simulation protocols.

Due to the low sample count, the input file is constructed with the following coarsening order.

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

7.  Census Division RECS to Census Region

8.  Census Region to National.

