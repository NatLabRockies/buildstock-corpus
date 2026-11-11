<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Hot Water Distribution | lines: 412-468 -->
## Hot Water Distribution

ResStock follows the OpenStudio-HPXML default assumptions when modeling hot water distribution, see the OpenStudio-HPXML [Hot Water Distribution](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-hot-water-distribution) documentation. Pipes are not explicitly modeled for any distribution systems, and correlations are instead used for determining the amount of hot water waste and heat gains in the living space depending on the hot water distribution system type and insulation. For a recirculation distribution system, the pipe length is calculated differently and additional inputs (e.g., power rating, control type) are used to specify the recirculation pump and pipe loop length. While recirculation options are available, all housing units in the baseline are assumed to have uninsulated trunk and branch hot water distribution system with copper pipes and without recirculation or drain water heat recovery. The inputs are captured in a single housing characteristic Hot Water Distribution.

### Hot Water Distribution

#### Description

Hot water piping material and insulation level.

#### Distribution Data Sources

- Engineering judgment.

#### Direct Conditional Dependencies

No dependencies.

#### Options

For the ResStock baseline baseline, all Hot Water Distribution is assumed to be “Uninsulated, trunk and branch, copper pipes.” This option specifies the following ResStock arguments.

- `hot_water_distribution_system_type` = standard

- `hot_water_distribution_recirc_control_type` = no control

- `dwhr_facilities_connected` = none

- `dwhr_equal_flow` = true

- `dwhr_efficiency` = 0.0.

For retrofit upgrades, other options are available and can be defined using the following arguments. For the argument definitions, see Table “The ResStock argument definitions set in the Hot Water Distribution characteristic”. See the OpenStudio-HPXML [Hot Water Distribution](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-hot-water-distribution) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hot_water_dist" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hot_water_distribution_system_type` | true |  | Choice | Standard, Recirculation | The type of the hot water distribution system. |
| `hot_water_distribution_standard_piping_length` | false | ft | Double | auto | If the distribution system is Standard, the length of the piping. |
| `hot_water_distribution_recirc_control_type` | false |  | Choice | auto, no control, timer, temperature, presence sensor demand control, manual demand control | If the distribution system is Recirculation, the type of hot water recirculation control, if any. |
| `hot_water_distribution_recirc_piping_length` | false | ft | Double | auto | If the distribution system is Recirculation, the length of the recirculation piping. |
| `hot_water_distribution_recirc_branch_piping_length` | false | ft | Double | auto | If the distribution system is Recirculation, the length of the recirculation branch piping. If not provided, the OS-HPXML default (see [Recirculation (In-Unit)](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#recirculation-in-unit)) is used. |
| `hot_water_distribution_recirc_pump_power` | false | W | Double | auto | If the distribution system is Recirculation, the recirculation pump power. |
| `hot_water_distribution_pipe_r` | false | h-ft<sup>2</sup>-R/Btu | Double | auto | Nominal R-value of the pipe insulation. |
| `dwhr_facilities_connected` | true |  | Choice | none, one, all | Which facilities are connected for the drain water heat recovery. Use 'none' if there is no drain water heat recovery system. |
| `dwhr_equal_flow` | false |  | Boolean | auto, true, false | Whether the drain water heat recovery has equal flow. |
| `dwhr_efficiency` | false | Frac | Double |  | The efficiency of the drain water heat recovery. |

The ResStock argument definitions set in the Hot Water Distribution characteristic

</div>

#### Distribution Assumptions

No assumptions are made.

