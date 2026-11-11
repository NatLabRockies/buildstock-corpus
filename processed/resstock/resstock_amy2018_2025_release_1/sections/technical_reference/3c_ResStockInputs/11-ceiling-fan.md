<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Ceiling Fan | lines: 1673-1730 -->
## Ceiling Fan

### Modeling Approach

ResStock models all ceiling fan options as a single fan operating at medium speed periodically throughout the year. The efficiency of the fans is specified at this speed and used to calculate the annual ceiling fan energy per the Energy Rating Rated Home in ANSI/RESNET/ICC 301-2019 ((International Code Council 2019)). The annual energy is multiplied with a stochastically generated detailed schedule to produce the ceiling fan end-use load profile. The ceiling fan schedule is created as a submetered reference schedule from RBSAM prorated by a separate occupancy schedule based on ATUS. See Section “Schedule Creation” for details on schedule generation. In the characteristic distribution, while ResStock distinguishes between the options “None” (no ceiling fan) and “Standard Efficiency, No Usage,” both options lead to zero energy consumption.

Ceiling fans are characterized in a single housing characteristic. The distribution, data sources, assumptions, and argument assignment are discussed in the next subsection.

### Ceiling Fan

#### Description

Presence and efficiency of ceiling fans.

#### Distribution Data Source(s)

Building America House Simulation Protocols ((Wilson et al. 2014)); national average used as saturation.

#### Direct Conditional Dependencies

- Vacancy Status.

#### Options

ResStock has three options for the ceiling fan characteristic: a standard efficiency ceiling fan, a standard efficiency ceiling fan that is not used, and “None.” For the standard efficiency ceiling fan that is not used, as well as the “None” option, the `ceiling_fan_present` argument is set to false and the `ceiling_fan_quantity` is set to 0. The `ceiling_fan_cooling_setpoint_offset` argument is 0 for all options. The remaining arguments set by ResStock are shown in Table “Ceiling Fan options and arguments that vary for each option”.

<div id="table:opt_def_ceiling_fans" data-source="3c_ResStockInputs.tex">

| Option name | `ceiling_fan_label_energy_use` | `ceiling_fan_efficiency` |
|:---|:---|:---|
| None | 0 | 0 |
| Standard Efficiency | auto | 70.4 |
| Standard Efficiency, No usage | auto | 0 |

Ceiling Fan options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Ceiling Fan characteristic”. See the OpenStudio-HPXML [Ceiling Fans](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-ceiling-fans) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ceiling_fans" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `ceiling_fan_present` | true |  | Boolean | true, false | Whether there are any ceiling fans. |
| `ceiling_fan_label_energy_use` | false | W | Double | auto | The label average energy use of the ceiling fan(s). If neither Efficiency nor Label Energy Use provided, the OS-HPXML default (see [HPXML Ceiling Fans](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-ceiling-fans)) is used. |
| `ceiling_fan_efficiency` | false | CFM/W | Double | auto | The efficiency rating of the ceiling fan(s) at medium speed. Only used if Label Energy Use not provided. If neither Efficiency nor Label Energy Use provided, the OS-HPXML default (see [HPXML Ceiling Fans](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-ceiling-fans)) is used. |
| `ceiling_fan_quantity` | false | \# | Integer | auto | Total number of ceiling fans. |
| `ceiling_fan_cooling_setpoint_temp_offset` | false | deg-F | Double | auto | The cooling setpoint temperature offset during months when the ceiling fans are operating. Only applies if ceiling fan quantity is greater than zero. |

The ResStock argument definitions set in the Ceiling Fan characteristic

</div>

#### Distribution Assumption(s)

If the unit is vacant, there is no ceiling fan energy.

