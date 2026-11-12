<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Pool and Hot Tub | lines: 1731-2032 -->
## Pool and Hot Tub

### Modeling Approach

ResStock models pools and hot tubs/spas that are connected to the home’s electric panel (i.e., not community/building pools). The saturation of pool, pool pump, pool heater, and hot tub/spa come from RECS 2020. The hot tub/spa pump is not modeled in ResStock. As pools in multifamily buildings are often for common use, the presence of pools are excluded from multifamily building types. All pools are assumed to have a pool pump. Hot tubs can be standalone or integrated as a bathroom fixture and therefore exist in all building types for units with hot tubs. The modeling of pool heaters, pool pumps, and hot tub/spa heaters in ResStock mostly relies on default OpenStudio-HPXML assumptions. Their annual energy is estimated using a reference calculation based on conditioned floor area and number of bedrooms, adjusted for occupants, using an equation from Hendron and Engebrecht (2010), and can be adjusted by a usage multiplier. The annual energy is then multiplied by a default simple schedule to produce the end-use load profile.

In OpenStudio-HPXML, pool and hot tub/spa heater options are electric resistance, gas-fired, and heat pump. Therefore, heaters for pools or spas using “Other Fuel” do not have any modeled energy consumption. Heat pump heaters are assumed to be five times more efficient than electric resistance. The use of pool cover or heating setpoint is approximated using a usage multiplier.

The building stock characterization distributions, data sources, assumptions, and argument assignment of pools and hot tubs are discussed in the next subsections.

### Misc Pool

#### Description

The presence of a pool.

#### Distribution Data Source(s)

Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- State

- Tenure

- Vintage.

#### Options

The options for the Misc Pool characteristic are “Has Pool” and “None.” The characteristic assigns the `pool_present` ResStock argument (Table “Misc Pool options and arguments that vary for each option”).

<div id="table:opt_def_pool" data-source="3c_ResStockInputs.tex">

| Option name | `pool_present` |     |
|:------------|:---------------|:----|
| Has Pool    | true           |     |
| None        | false          |     |

Misc Pool options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Misc Pool characteristic”. See the OpenStudio-HPXML [Pools](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-pools) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_pool" data-source="3c_ResStockInputs.tex">

| Name           | Required | Units | Type    | Choices     | Description              |
|:---------------|:---------|:------|:--------|:------------|:-------------------------|
| `pool_present` | true     |       | Boolean | true, false | Whether there is a pool. |

The ResStock argument definitions set in the Misc Pool characteristic

</div>

#### Distribution Assumption(s)

The only valid option for multifamily homes is None, because the pool is most likely to be part of the common load and not associated with a specific unit.

Due to the low sample count, the input file is constructed with the following fallback coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  Vintage coarsened to every 20 years before 2000 and every 10 years subsequently

7.  Vintage homes built before 1960 coarsened to pre-1960

8.  Vintage homes built after 2000 coarsened to 2000-20

9.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

10. Census Division RECS to Census Region

11. Census Region to National.

### Misc Pool Heater

#### Description

The heating fuel of the pool heater if there is a pool.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

- Constructed using the California Energy Commission 2019 Residential Appliance Saturation Study (RASS) microdata

#### Direct Conditional Dependencies

- Heating Fuel

- Misc Pool.

#### Options

There are five options for pool heaters: Electricity, Electric Heat Pump, Natural Gas, None, and Other Fuel. The Electricity option defines a traditional electric resistance pool heater, whereas the Electric Heat Pump option uses heat pump technology for heating the pool. The “Other Fuel” pool heater option currently is currently not modeled in ResStock. The ResStock arguments assigned for each of these options is given in Table “Pool Heater options and arguments that vary for each option”.

<div id="table:opt_def_pool_heat" data-source="3c_ResStockInputs.tex">

| Option name | `pool_heater_type` | `pool_heater_annual_kwh` | `pool_heater_annual_therm` | `pool_heater_usage_multiplier` |
|:---|:---|:---|:---|:---|
| Electric Heat Pump | heat pump | auto | 0 | 1.0 |
| Electricity | electric resistance | auto | 0 | 1.0 |
| Electric Heat Pump | heat pump | auto | 0 | 1.0 |
| Natural Gas | gas fired | 0 | auto | 1.0 |
| None | none | 0 | 0 | 0 |
| Other Fuel | none | 0 | 0 | 0 |

Pool Heater options and arguments that vary for each option

</div>

The “Other Fuel” option is assigned the same arguments as “None,” and will result in no energy consumption.

For the argument definitions, see Table “The ResStock argument definitions set in the Pool Heater characteristic”. See the OpenStudio-HPXML [Pool Heater](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#pool-heater) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_pool_heat" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `pool_heater_type` | true |  | Choice | none, electric resistance, gas fired, heat pump | The type of pool heater. Use 'none' if there is no pool heater. |
| `pool_heater_annual_kwh` | false | kWh/yr | Double | auto | The annual energy consumption of the electric resistance pool heater. |
| `pool_heater_annual_therm` | false | therm/yr | Double | auto | The annual energy consumption of the gas fired pool heater. |
| `pool_heater_usage_multiplier` | false |  | Double | auto | Multiplier on the pool heater energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Pool Heater characteristic

</div>

#### Distribution Assumption(s)

- Within electric pool heaters, proportion of heat pump electric pool heating vs. non-heat pump electric pool heating was derived from RASS 2019.

### Misc Pool Pump

#### Description

Presence and size of pool pump.

#### Distribution Data Source(s)

Building America House Simulation Protocols ((Wilson et al. 2014)); national average fraction used for saturation.

#### Direct Conditional Dependencies

- Misc Pool.

#### Options

The options for Misc Pool Pump are None and 1.0 horsepower (HP) Pump. If there is a pool, then the 1.0 HP Pump option is assigned. The characteristic assigns the `pool_pump_annual_kwh` and `pool_pump_usage_multiplier` ResStock arguments, Table “Misc Pool Pump options and arguments that vary for each option”.

<div id="table:opt_def_pool_pump" data-source="3c_ResStockInputs.tex">

| Option name | `pool_pump_annual_kwh` | `pool_pump_usage_multiplier` |     |
|:------------|:-----------------------|:-----------------------------|:----|
| None        | 0                      | 0                            |     |
| 1.0 HP Pump | auto                   | 1.0                          |     |

Misc Pool Pump options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Misc Pool Pump characteristic”. See the OpenStudio-HPXML [ Pool Pump](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#pool-pump) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_pool_pump" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `pool_pump_annual_kwh` | false | kWh/yr | Double | auto | The annual energy consumption of the pool pump. |
| `pool_pump_usage_multiplier` | false |  | Double | auto | Multiplier on the pool pump energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Misc Pool Pump characteristic

</div>

#### Distribution Assumption(s)

None

### Misc Hot Tub Spa

#### Description

The presence and heating fuel of a hot tub/spa at the housing unit.

#### Distribution Data Source(s)

Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- Heating Fuel

- State

- Tenure.

#### Options

The options for the Misc Hot tub Spa characteristic are the heating fuel of the hot tub heater: Electricity, Natural gas, and Other Fuel. The None option is used when the housing unit does not have a hot tub. The characteristic assigns the `permanent_spa_present` `permanent_spa_heater_type`, `permanent_spa_pump_usage_multiplier`, `permanent_spa_heater_usage_multiplier`, `permanent_spa_pump_annual_kwh`, `permanent_spa_heater_annual_kwh`, and `permanent_spa_heater_annual_therm` ResStock arguments. The following arguments are set for the options:

- `permanent_spa_pump_usage_multiplier` is 1.0 for "Electricity" and "Natural Gas" and 0 for everything else.

- `permanent_spa_heater_usage_multiplier` is 1.0 for "Electricity" and "Natural Gas" and 0 for everything else.

- `permanent_spa_pump_annual_kwh` is auto for "Electricity" and "Natural Gas" and 0 for everything else.

- `permanent_spa_heater_annual_kwh` is auto for "Electricity" and 0 for everything else.

- `permanent_spa_heater_annual_therm` is auto for "Natural Gas" and 0 for everything else.

As shown, the “Other Fuel” option is assigned the same arguments as “None,” and will result in no energy consumption. The other arguments that vary across the arguments are in Table “Misc Hot Tub Spa options and arguments that vary for each option”.

<div id="table:opt_def_hot_tub" data-source="3c_ResStockInputs.tex">

| Option name | `permanent_spa_present` | `permanent_spa_heater_type` |
|:------------|:------------------------|:----------------------------|
| Electricity | true                    | electric resistance         |
| Natural Gas | true                    | gas fired                   |
| None        | false                   | none                        |
| Other Fuel  | false                   | none                        |

Misc Hot Tub Spa options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Misc Hot Tub Spa characteristic”. See the OpenStudio-HPXML [Permanent Spas](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-permanent-spas) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hot_tub" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `permanent_spa_present` | true |  | Boolean | true, false | Whether there is a permanent spa. |
| `permanent_spa_pump_annual_kwh` | false | kWh/yr | Double | auto | The annual energy consumption of the permanent spa pump. If not provided, the OS-HPXML default (see [Permanent Spa Pump](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#permanent-spa-pump)) is used. |
| `permanent_spa_pump_usage_multiplier` | false |  | Double | auto | Multiplier on the permanent spa pump energy usage that can reflect, e.g., high/low usage occupants. |
| `permanent_spa_heater_type` | true |  | Choice | none, electric resistance, gas fired, heat pump | The type of permanent spa heater. Use 'none' if there is no permanent spa heater. |
| `permanent_spa_heater_annual_kwh` | false | kWh/yr | Double | auto | The annual energy consumption of the electric resistance permanent spa heater. |
| `permanent_spa_heater_annual_therm` | false | therm/yr | Double | auto | The annual energy consumption of the gas fired permanent spa heater. |
| `permanent_spa_heater_usage_multiplier` | false |  | Double | auto | Multiplier on the permanent spa heater energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Misc Hot Tub Spa characteristic

</div>

#### Distribution Assumption(s)

Due to the low sample count, the input file is constructed by downscaling a housing unit sub-input file with a household sub-input file. The sub-input files have the following dependencies:

housing unit sub-input file dependencies = Geometry Building Type RECS, State, and Heating Fuel, with the following fallback coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Heating Fuel coarsened to Other Fuel, Wood and Propane combined

3.  Heating Fuel coarsened to Fuel Oil, Other Fuel, Wood and Propane combined

4.  Geometry Building Type RECS coarsened to SF/MF/MH

5.  Geometry Building Type RECS coarsened to SF and MH/MF

6.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

7.  Census Division RECS to Census Region

8.  Census Region to National.

Household sub-input file: dependencies = Geometry Building Type RECS, State, Tenure, and Federal Poverty Level, with the following fallback coarsening order:

1.  State coarsened to Census Division RECS with AK/HI separate

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  Census Division RECS with AK/HI separate coarsened to Census Division RECS

7.  Census Division RECS to Census Region

8.  Census Region to National.

In combining the housing unit sub-input file and household sub-input file, the conditional relationships are ignored across Heating Fuel, as well as across Tenure and Federal Poverty Level.

