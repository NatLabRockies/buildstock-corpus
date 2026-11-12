<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Well Pump | lines: 2033-2098 -->
## Well Pump

### Modeling Approach

Well pumps are used to extract potable water from a well. The 2017-2019 American Housing Surveys ((U.S. Census 2022)) estimated that 11% of US homes have a well pump, and that data is used to construct the characteristic distribution, which has a dependency to Census Division, PUMA Metro Status, and Geometry Building Type Height. Well pumps are also more common outside the metro areas than in metro areas, particularly within a principal city. A well pump in ResStock is modeled as a type of plug load that does not provide any latent or sensible heat to the housing units. The annual energy for well pumping is estimated based on conditioned floor area and number of bedrooms converted from occupants using an equation from 2014 Building America House Simulation Protocols (BAHSP) ((Wilson et al. 2014)) and can be adjusted by a usage multiplier. The annual energy is then multiplied by a default simple schedule to produce the end-use load profile.

### Misc Well Pump

#### Description

Presence of well pump according to the use of well for domestic water source.

#### Distribution Data Source(s)

- 2017 and 2019 American Housing Survey (AHS) microdata.

- Core Based Statistical Area (CBSA) data based on the Feb 2013 CBSA delineation file.

#### Direct Conditional Dependencies

- Census Division

- PUMA Metro Status

- Geometry Building Type Height

#### Options

The options for the Misc Well Pump characteristic are Typical Efficiency if there is a well pump and None if there is no well pump. The characteristic sets the `misc_plug_loads_well_pump_present`, `misc_plug_loads_well_pump_usage_multiplier`, `misc_plug_loads_well_pump_2_usage_multiplier`, and `misc_plug_loads_well_pump_annual_kwh` ResStock arguments (Table “Misc Well Pump options and arguments that vary for each option”).

The `misc_plug_loads_well_pump_usage_multiplier` argument is 1.0 for “Typical Efficiency” and 0 for “None.” The `misc_plug_loads_well_pump_2_usage_multiplier` argument is 1.0 for “Typical Efficiency” and 0 for “None.”

<div id="table:hc_opt_def_well_pump" data-source="3c_ResStockInputs.tex">

| Option name | `misc_plug_loads_well_pump_present` | `misc_plug_loads_well_pump_annual_kwh` |
|:---|:---|:---|
| Typical Efficiency | true | auto |
| None | false | 0 |

Misc Well Pump options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Misc Well Pump characteristic”. See the OpenStudio-HPXML [Misc Loads](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-misc-loads) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_well_pump" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `misc_plug_loads_well_pump_present` | true |  | Boolean | true, false | Whether there is a well pump. |
| `misc_plug_loads_well_pump_annual_kwh` | false | kWh/yr | Double | auto | The annual energy consumption of the well pump plug loads. |
| `misc_plug_loads_well_pump_usage_multiplier` | false |  | Double | auto | Multiplier on the well pump energy usage that can reflect, e.g., high/low usage occupants. |
| `misc_plug_loads_well_pump_2_usage_multiplier` | true |  | Double |  | Additional multiplier on the well pump energy usage that can reflect, e.g., high/low usage occupants. |

The ResStock argument definitions set in the Misc Well Pump characteristic

</div>

#### Distribution Assumption(s)

- All well pumps are assumed to have typical efficiency.

- Where the number of samples \< 10, the Census Division is aggregated up to Census Region.

- AHS has data for buildings up to 7 stories tall. Buildings with 8 or more stories are assumed not to have a well pump.

