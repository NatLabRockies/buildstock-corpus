<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Clothes Dryer | lines: 1515-1672 -->
## Clothes Dryer

### Modeling Approach

A clothes dryer is an in-unit residential appliance for drying clothes. Clothes dryers impact energy through the direct use of running the appliance. Clothes dryers in shared spaces and common areas of multifamily buildings are not currently captured in ResStock. Vented clothes dryers will result in increased infiltration to the conditioned space during dryer operation.

ResStock models clothes dryers with different heating fuels (Natural Gas, Electric, and Propane). Uses the *CombinedEnergyFactor* in OpenStudio-HPXML to specify the performance of each fuel.

The schedule of the clothes dryer usage is based on the American Time Use Survey data. The clothes dryer is scheduled to start immediately after the clothes washer ends its cycle. The duration of the clothes dryer is based on distributions from RBSA ((Northwest Energy Efficiency Alliance 2024)). See Section “Schedule Creation” for details on schedule generation.

ResStock provides distributions for what housing units have a clothes dryer, the fuel of the dryer, and clothes dryer energy multiplier in the “Clothes Dryer” and “Clothes Dryer Usage Level” characteristics.

### Clothes Dryer

#### Description

The presence, rated efficiency, and fuel type of the clothes dryer in a housing unit.

#### Distribution Data Source(s)

Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- Clothes Washer Presence

- Federal Poverty Level

- Geometry Building Type RECS

- Heating Fuel

- State

- Tenure.

#### Options

The ResStock baseline includes three dryer options: an electric dryer, a natural gas dryer, and a propane dryer. There is also a “None” option. Certain arguments are common across all three dryer options: auto for `clothes_dryer_location`, CombinedEnergyFactor for `clothes_dryer_efficiency_type`, and auto for `clothes_dryer_vented_flow_rate`. The arguments that differ across options are shown in Table “Clothes Dryer options and arguments that vary for each option”.

<div id="table:opt_def_clothes dryer" data-source="3c_ResStockInputs.tex">

| Option name | `clothes_dryer_present` | `clothes_dryer_fuel_type` | `clothes_dryer_efficiency` |
|:---|:---|:---|:---|
| Electric | true | electricity | 2.70 |
| Gas | true | natural gas | 2.39 |
| None | false | natural gas | 2.70 |
| Propane | true | propane | 2.39 |

Clothes Dryer options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Clothes Dryer characteristic”. See the OpenStudio-HPXML [Clothes Dryer](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-clothes-dryer) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_clothes_dryer" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `clothes_dryer_present` | true |  | Boolean | true, false | Whether there is a clothes dryer present. |
| `clothes_dryer_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, garage, other housing unit, other heated space, other multifamily buffer space, other non-freezing space | The space type for the clothes dryer location. |
| `clothes_dryer_fuel_type` | true |  | Choice | electricity, natural gas, fuel oil, propane, wood, coal | Type of fuel used by the clothes dryer. |
| `clothes_dryer_efficiency_type` | true |  | Choice | EnergyFactor, CombinedEnergyFactor | The efficiency type of the clothes dryer. |
| `clothes_dryer_efficiency` | false | lb/kWh | Double | auto | The efficiency of the clothes dryer. |
| `clothes_dryer_vented_flow_rate` | false | CFM | Double | auto | The exhaust flow rate of the vented clothes dryer. |

The ResStock argument definitions set in the Clothes Dryer characteristic

</div>

#### Distribution Assumption(s)

Clothes dryer option is “None” if the clothes washer is not present.

Due to the low sample count, the input file is constructed by downscaling a housing unit sub-input file with a household sub-input file. The sub-input files have the following dependencies: housing unit sub-input file: dependencies = Geometry Building Type RECS, State, Heating Fuel, and Clothes Washer Presence, with the following fallback coarsening order:

1.  State coarsened to Census Division RECS without AK, HI

2.  Heating Fuel coarsened to Other Fuel, Wood and Propane combined

3.  Heating Fuel coarsened to Fuel Oil, Other Fuel, Wood and Propane combined

4.  Geometry Building Type RECS coarsened to SF/MF/MH

5.  Geometry Building Type RECS coarsened to SF and MH/MF

6.  State coarsened to Census Division RECS

7.  State coarsened to Census Region

8.  State coarsened to National.

Household sub-input file: dependencies = Geometry Building Type RECS, Tenure, and Federal Poverty Level, with the following fallback coarsening order:

1.  State coarsened to Census Division RECS without AK, HI

2.  Geometry Building Type RECS coarsened to SF/MF/MH

3.  Geometry Building Type RECS coarsened to SF and MH/MF

4.  Federal Poverty Level coarsened every 100%

5.  Federal Poverty Level coarsened every 200%

6.  State coarsened to Census Division RECS

7.  State coarsened to Census Region

8.  State coarsened to National.

In combining the housing unit sub-input file and household sub-input file, the conditional relationships are ignored across Heating Fuel and Clothes Washer Presence, as well as across Tenure and Federal Poverty Level.

### Clothes Dryer Usage Level

#### Description

Clothes dryer energy usage level multiplier.

#### Distribution Data Source(s)

Not applicable—direct mapping of usage level (Section “Usage”).

#### Direct Conditional Dependencies

- Usage Level.

#### Options

The clothes dryer usage level is set based on the usage level (Section “Usage”) characteristic. It is 80% Usage when the usage level is Low, 100% Usage when the usage level is Medium, and 120% Usage when the usage level is High. The characteristic assigns the `clothes_dryer_usage_multiplier` ResStock argument (Table “Clothes Dryer Usage Level options and arguments that vary for each option”).

<div id="table:hc_opt_clothes_dryer" data-source="3c_ResStockInputs.tex">

| Option name | `clothes_dryer_usage_multiplier` |
|:------------|:---------------------------------|
| 80% Usage   | 0.8                              |
| 100% Usage  | 1.0                              |
| 120% Usage  | 1.2                              |

Clothes Dryer Usage Level options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Clothes Dryer Usage Level characteristic”. See the [OpenStudio-HPXML Refrigerators](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-refrigerators) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_clothes_dryer_usage_level" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `clothes_dryer_usage_multiplier` | false |  | Double | auto | Multiplier on the clothes dryer energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Clothes Dryer Usage Level characteristic

</div>

#### Distribution Assumption(s)

None.

