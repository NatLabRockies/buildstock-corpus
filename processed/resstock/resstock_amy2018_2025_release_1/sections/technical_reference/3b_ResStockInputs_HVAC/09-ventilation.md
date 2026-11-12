<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/3b_ResStockInputs_HVAC.md | section: Ventilation | lines: 2308-2661 -->
## Ventilation

### Modeling Approach

Mechanical ventilation, natural ventilation, and local ventilation fans (bath fan, range fan) can be modeled in ResStock. There is currently no mechanical ventilation in the baseline. The bath fan and range fan operate for one hour a day according to the daily hourly schedule specified in the Bathroom Spot Vent Hour and Range Spot Vent Hour characteristics. In aggregate, the distributions of the Bathroom Spot Vent Hour and Range Spot Vent Hour characteristics provide an average schedule for a group of housing units. For default, constraints, and notes about the modeling approach see [OpenStudio-HPXML Local Ventilation Fans](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-local-ventilation-fans) documentation. Natural ventilation (through opening the windows) is allowed during the Cooling Season under certain outside conditions set by the 2010 House Simulation Protocols ((Hendron and Engebrecht 2010)). When ventilating, 1/3 of the operable windows are open for natural ventilation ((Hendron and Engebrecht 2010)).

Four different input files influence ventilation in ResStock:

- Mechanical Ventilation

- Natural Ventilation

- Bathroom Spot Vent Hour

- Range Spot Vent Hour.

Mechanical ventilation is currently not used in the baseline, and natural ventilation has a single option assigned to all homes. Bathroom Spot Vent Hour and Range Spot Vent Hour provide diversity in the schedules of operation of localized bathroom and cooking ventilation, respectively.

### Mechanical Ventilation

#### Description

Mechanical ventilation type and efficiency.

#### Distribution Data Source(s)

Engineering judgment.

#### Direct Conditional Dependencies

None.

#### Options

In the baseline, no homes are assigned mechanical ventilation, so only the option “None” is used and all arguments are set to None or 0:

- `mech_vent_fan_type`: none

- `mech_vent_flow_rate`: 0

- `mech_vent_hours_in_operation`: 0

- `mech_vent_recovery_efficiency_type`: unadjusted

- `mech_vent_total_recovery_efficiency`: 0

- `mech_vent_sensible_recovery_efficiency`: 0

- `mech_vent_fan_power`: 0

- `mech_vent_num_units_served`: 0

- `mech_vent_shared_frac_recirculation`: auto

- `mech_vent_shared_preheating_fuel`: auto

- `mech_vent_shared_preheating_efficiency`: auto

- `mech_vent_shared_preheating_fraction_heat_load_served`: auto

- `mech_vent_shared_precooling_fuel`: auto

- `mech_vent_shared_precooling_efficiency`: auto

- `mech_vent_shared_precooling_fraction_cool_load_served`: auto

- `mech_vent_2_fan_type` : none

- `mech_vent_2_flow_rate`: 0

- `mech_vent_2_hours_in_operation`: 0

- `mech_vent_2_recovery_efficiency_type`: unadjusted

- `mech_vent_2_total_recovery_efficiency`: 0

- `mech_vent_2_sensible_recovery_efficiency`: 0

- `mech_vent_2_fan_power`: 0

- `whole_house_fan_present`: false

- `whole_house_fan_flow_rate`: 0

- `whole_house_fan_power`: 0.

For the argument definitions, see Table “The ResStock argument definitions set in the Mechanical Ventilation characteristic”. See the OpenStudio-HPXML [Mechanical Ventilation Fans](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-[https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-mechanical-ventilation-fans]) and [Local Ventilation Fans](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-local-ventilation-fans) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_mech_vent" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `mech_vent_fan_type` | true |  | Choice | none, exhaust only, supply only, energy recovery ventilator, heat recovery ventilator, balanced, central fan integrated supply | The type of the mechanical ventilation. Use 'none' if there is no mechanical ventilation system. |
| `mech_vent_flow_rate` | false | CFM | Double | auto | The flow rate of the mechanical ventilation. |
| `mech_vent_hours_in_operation` | false | hrs/day | Double | auto | The hours in operation of the mechanical ventilation. |
| `mech_vent_recovery_efficiency_type` | true |  | Choice | Unadjusted, Adjusted | The total recovery efficiency type of the mechanical ventilation. |
| `mech_vent_total_recovery_efficiency` | true | Frac | Double |  | The Unadjusted or Adjusted total recovery efficiency of the mechanical ventilation. Applies to energy recovery ventilator. |
| `mech_vent_sensible_recovery_efficiency` | true | Frac | Double |  | The Unadjusted or Adjusted sensible recovery efficiency of the mechanical ventilation. Applies to energy recovery ventilator and heat recovery ventilator. |
| `mech_vent_fan_power` | false | W | Double | auto | The fan power of the mechanical ventilation. |
| `mech_vent_num_units_served` | true | \# | Integer |  | Number of housing units served by the mechanical ventilation system. Must be 1 if single-family detached. Used to apportion flow rate and fan power to the unit. |
| `mech_vent_shared_frac_recirculation` | false | Frac | Double |  | Fraction of the total supply air that is recirculated, with the remainder assumed to be outdoor air. The value must be 0 for exhaust only systems. Required for a shared mechanical ventilation system. |
| `mech_vent_shared_preheating_fuel` | false |  | Choice | auto, electricity, natural gas, fuel oil, propane, wood, wood pellets, coal | Fuel type of the preconditioning heating equipment. Only used for a shared mechanical ventilation system. If not provided, assumes no preheating. |
| `mech_vent_shared_preheating_efficiency` | false | COP | Double |  | Efficiency of the preconditioning heating equipment. Only used for a shared mechanical ventilation system. If not provided, assumes no preheating. |
| `mech_vent_shared_preheating_fraction_heat_load_served` | false | Frac | Double |  | Fraction of heating load introduced by the shared ventilation system that is met by the preconditioning heating equipment. If not provided, assumes no preheating. |
| `mech_vent_shared_precooling_fuel` | false |  | Choice | auto, electricity | Fuel type of the preconditioning cooling equipment. Only used for a shared mechanical ventilation system. If not provided, assumes no precooling. |
| `mech_vent_shared_precooling_efficiency` | false | COP | Double |  | Efficiency of the preconditioning cooling equipment. Only used for a shared mechanical ventilation system. If not provided, assumes no precooling. |
| `mech_vent_shared_precooling_fraction_cool_load_served` | false | Frac | Double |  | Fraction of cooling load introduced by the shared ventilation system that is met by the preconditioning cooling equipment. If not provided, assumes no precooling. |
| `mech_vent_2_fan_type` | true |  | Choice | none, exhaust only, supply only, energy recovery ventilator, heat recovery ventilator, balanced | The type of the second mechanical ventilation. Use 'none' if there is no second mechanical ventilation system. |
| `mech_vent_2_flow_rate` | true | CFM | Double |  | The flow rate of the second mechanical ventilation. |
| `mech_vent_2_hours_in_operation` | true | hrs/day | Double |  | The hours in operation of the second mechanical ventilation. |
| `mech_vent_2_recovery_efficiency_type` | true |  | Choice | Unadjusted, Adjusted | The total recovery efficiency type of the second mechanical ventilation. |
| `mech_vent_2_total_recovery_efficiency` | true | Frac | Double |  | The Unadjusted or Adjusted total recovery efficiency of the second mechanical ventilation. Applies to energy recovery ventilator. |
| `mech_vent_2_sensible_recovery_efficiency` | true | Frac | Double |  | The Unadjusted or Adjusted sensible recovery efficiency of the second mechanical ventilation. Applies to energy recovery ventilator and heat recovery ventilator. |
| `mech_vent_2_fan_power` | true | W | Double |  | The fan power of the second mechanical ventilation. |
| `whole_house_fan_present` | true |  | Boolean | true, false | Whether there is a whole house fan. |
| `whole_house_fan_flow_rate` | false | CFM | Double | auto | The flow rate of the whole house fan. |

The ResStock argument definitions set in the Mechanical Ventilation characteristic

</div>

#### Distribution Assumption(s)

None.

### Natural Ventilation

#### Description

Amount and schedule of natural ventilation through operable windows.

#### Distribution Data Source(s)

Building America House Simulation Protocols ((E. Wilson et al. 2014a)).

#### Direct Conditional Dependencies

None.

#### Options

All homes are currently set to the same natural ventilation option.

<div id="table:hc_opt_hvac_sec_ht" data-source="3b_ResStockInputs_HVAC.tex">

| Option name               | `window_fraction_operable` |
|:--------------------------|:---------------------------|
| Cooling Season, 7 days/wk | 0.67                       |

Natural Ventilation options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Natural Ventilation characteristic”. See the OpenStudio-HPXML [Natural Ventilation](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#natural-ventilation) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_nat_vent" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `window_fraction_operable` | false | Frac | Double | auto | Fraction of windows that are operable. |

The ResStock argument definitions set in the Natural Ventilation characteristic

</div>

#### Distribution Assumption(s)

None.

### Bathroom Spot Vent Hour

#### Description

Bathroom spot ventilation daily start hour. In ResStock, the bathroom fan(s) operates for 1 hour everyday. A schedule is generated on the fly based on these inputs.

#### Distribution Data Source(s)

Same as occupancy schedule from the Building America House Simulation Protocols ((E. Wilson et al. 2014a)).

#### Direct Conditional Dependencies

None.

#### Options

The start hours are spread out over all 24 hours of the day (Table “Bathroom Spot Vent Hour options and arguments that vary for each option”). The following ResStock arguments are constant across all options:

- `bathroom_fans_quantity`: auto

- `bathroom_fans_flow_rate`: auto

- `bathroom_fans_hours_in_operation`: auto

- `bathroom_fans_power`: auto.

<div id="table:hc_opt_bath_vent" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `bathroom_fans_start_hour` |
|:------------|:---------------------------|
| Hour0       | 0                          |
| Hour1       | 1                          |
| Hour2       | 2                          |
| Hour3       | 3                          |
| Hour4       | 4                          |
| Hour5       | 5                          |
| Hour6       | 6                          |
| Hour7       | 7                          |
| Hour8       | 8                          |
| Hour9       | 9                          |
| Hour10      | 10                         |
| Hour11      | 11                         |
| Hour12      | 12                         |
| Hour13      | 13                         |
| Hour14      | 14                         |
| Hour15      | 15                         |
| Hour16      | 16                         |
| Hour17      | 17                         |
| Hour18      | 18                         |
| Hour19      | 19                         |
| Hour20      | 20                         |
| Hour21      | 21                         |
| Hour22      | 22                         |
| Hour23      | 23                         |

Bathroom Spot Vent Hour options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Bathroom Spot Vent Hour characteristic”. See the OpenStudio-HPXML [Local Ventilation Fans](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-local-ventilation-fans) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_bath_vent" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `bathroom_fans_quantity` | false | \# | Integer | auto | The quantity of the bathroom fans. |
| `bathroom_fans_flow_rate` | false | CFM | Double | auto | The flow rate of the bathroom fans. |
| `bathroom_fans_hours_in_operation` | false | hrs/day | Double | auto | The hours in operation of the bathroom fans. |
| `bathroom_fans_power` | false | W | Double | auto | The fan power of the bathroom fans. |
| `bathroom_fans_start_hour` | false | hr | Integer | auto | The start hour of the bathroom fans. |

The ResStock argument definitions set in the Bathroom Spot Vent Hour characteristic

</div>

#### Distribution Assumption(s)

None.

### Range Spot Vent Hour

#### Description

Range spot ventilation daily start hour. In ResStock, the range hood operates for 1 hour every day. A schedule is generated on the fly for range spot ventilation based on these inputs.

#### Distribution Data Source(s)

Derived from national average cooking range schedule in Building America House Simulation Protocols ((E. Wilson et al. 2014a)).

#### Direct Conditional Dependencies

None.

#### Options

Start hours are spread across all hours of the day (Table “Range Spot Vent Hour options and arguments that vary for each option”). Across the options the following ResStock arguments are constant:

- `kitchen_fans_quantity`: auto

- `kitchen_fans_flow_rate`: auto

- `kitchen_fans_hours_in_operation`: auto

- `kitchen_fans_power`: auto.

<div id="table:hc_opt_range_vent" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `kitchen_fans_start_hour` |
|:------------|:--------------------------|
| Hour0       | 0                         |
| Hour1       | 1                         |
| Hour2       | 2                         |
| Hour3       | 3                         |
| Hour4       | 4                         |
| Hour5       | 5                         |
| Hour6       | 6                         |
| Hour7       | 7                         |
| Hour8       | 8                         |
| Hour9       | 9                         |
| Hour10      | 10                        |
| Hour11      | 11                        |
| Hour12      | 12                        |
| Hour13      | 13                        |
| Hour14      | 14                        |
| Hour15      | 15                        |
| Hour16      | 16                        |
| Hour17      | 17                        |
| Hour18      | 18                        |
| Hour19      | 19                        |
| Hour20      | 20                        |
| Hour21      | 21                        |
| Hour22      | 22                        |
| Hour23      | 23                        |

Range Spot Vent Hour options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Range Spot Vent Hour characteristic”. See the OpenStudio-HPXML [Local Ventilation](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-local-ventilation-fans) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_range_fan" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `kitchen_fans_quantity` | false | \# | Integer | auto | The quantity of the kitchen fans. |
| `kitchen_fans_flow_rate` | false | CFM | Double | auto | The flow rate of the kitchen fan. |
| `kitchen_fans_hours_in_operation` | false | hrs/day | Double | auto | Hours per day of operation. |
| `kitchen_fans_power` | false | W | Double | auto | The fan power of the kitchen fan. |
| `kitchen_fans_start_hour` | false | hr | Integer | auto | The start hour of the kitchen fan. |

The ResStock argument definitions set in the Range Spot Vent Hour characteristic

</div>

#### Distribution Assumption(s)

None.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-bahsp_2010" class="csl-entry">

Hendron, Robert, and Cheryn Engebrecht. 2010. *Building America House Simulation Protocols*. US DOE: Office of Energy Efficiency; Renewable Energy. <https://www1.eere.energy.gov/buildings/publications/pdfs/building_america/house_simulation.pdf>.

</div>

<div id="ref-Wilson2014" class="csl-entry">

Wilson, E., C. Engebrecht Metzger, S. Horowitz, and R. Hendron. 2014a. *2014 Building America House Simulation Protocols*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy14osti/60988.pdf>.

</div>

<div id="ref-bahsp_2014" class="csl-entry">

Wilson, E, C Engebrecht Metzger, S Horowitz, and R Hendron. 2014b. *2014 Building America House Simulation Protocols*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy14osti/60988.pdf>.

</div>

<div id="ref-Winkler2020" class="csl-entry">

Winkler, Jon, Saptarshi Das, Lieko Earle, et al. 2020. “Impact of Installation Faults in Air Conditioners and Heat Pumps in Single-Family Homes on u.s. Energy Usage.” *Applied Energy* 278: 115533. https://doi.org/<https://doi.org/10.1016/j.apenergy.2020.115533>.

</div>

</div>
