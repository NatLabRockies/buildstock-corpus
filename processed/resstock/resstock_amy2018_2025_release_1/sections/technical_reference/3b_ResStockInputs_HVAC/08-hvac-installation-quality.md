<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3b_ResStockInputs_HVAC.md | section: HVAC Installation Quality | lines: 2030-2307 -->
## HVAC Installation Quality

### Modeling Approach

ResStock includes features that allow users to account for the quality of HVAC installation. Two key factors that impact installation quality are the refrigeration charge and the airflow rate.

ResStock specifies the installed refrigerant charge as a percentage of the system’s design charge for each option. It also sets the actual airflow rate per ton of cooling capacity, which may differ from the design airflow rate.

These variables, refrigerant charge fractions and airflow rates, can be adjusted for single-speed air conditioners and air-source heat pumps. However, despite these capabilities, ResStock currently does not make use of these options in the baseline model.

### HVAC System Single-Speed ASHP Airflow

#### Description

Single-speed ASHP actual airflow rates for faulted systems. This input file is currently not used since ResStock is still lacking data on faults.

#### Distribution Data Source(s)

- *Impact of installation faults in air conditioners and heat pumps in single-family homes on U.S. energy usage* ((Winkler et al. 2020)).

#### Direct Conditional Dependencies

- HVAC Heating Efficiency

- HVAC System is Faulted.

#### Options

Thirteen options are available in ResStock, but currently none are used, and all homes as set to “None” (Table “HVAC System Single-Speed ASHP Airflow options and arguments that vary for each option”). The `cooling_system_rated_cfm_per_ton` for all 13 options is 400.0.

<div id="table:hc_opt_hvac_single_speed" data-source="3b_ResStockInputs_HVAC.tex">

| Option name   | `cooling_system_actual_cfm_per_ton` |
|:--------------|:------------------------------------|
| 154.8 cfm/ton | 154.8                               |
| 204.4 cfm/ton | 204.4                               |
| 254.0 cfm/ton | 254.0                               |
| 303.5 cfm/ton | 303.5                               |
| 353.1 cfm/ton | 353.1                               |
| 402.7 cfm/ton | 402.7                               |
| 452.3 cfm/ton | 452.3                               |
| 501.9 cfm/ton | 501.9                               |
| 551.5 cfm/ton | 551.5                               |
| 601.0 cfm/ton | 601.0                               |
| 650.6 cfm/ton | 650.6                               |
| 700.2 cfm/ton | 700.2                               |
| None          |                                     |

HVAC System Single-Speed ASHP Airflow options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC System Single-Speed ASHP characteristic”. See the OpenStudio-HPXML [Air-to-Air Heat Pump](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#air-to-air-heat-pump) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_single_speed" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `cooling_system_rated_cfm_per_ton` | false | cfm/ton | Double | The rated cfm per ton of the cooling system. |
| `cooling_system_actual_cfm_per_ton` | false | cfm/ton | Double | The actual cfm per ton of the cooling system. |

The ResStock argument definitions set in the HVAC System Single-Speed ASHP characteristic

</div>

#### Distribution Assumption(s)

None

### HVAC System Single-Speed ASHP Charge

#### Description

ASHP deviation between design/installed charge. Not currently used because of lack of data on faulted HVAC.

#### Distribution Data Source(s)

- *Impact of installation faults in air conditioners and heat pumps in single-family homes on U.S. energy usage* ((Winkler et al. 2020)).

#### Direct Conditional Dependencies

- HVAC Heating Efficiency

- HVAC System is Faulted.

#### Options

Seven different options are available for faulted ASHP charges, but none are currently in use (Table “HVAC System Single-Speed ASHP options and arguments that vary for each option”).

<div id="table:hc_opt_ss_hp_charge" data-source="3b_ResStockInputs_HVAC.tex">

| Option name       | `heat_pump_frac_manufacturer_charge` |
|:------------------|:-------------------------------------|
| 0.570 Charge Frac | 0.570                                |
| 0.709 Charge Frac | 0.709                                |
| 0.848 Charge Frac | 0.848                                |
| 0.988 Charge Frac | 0.988                                |
| 1.127 Charge Frac | 1.127                                |
| 1.266 Charge Frac | 1.266                                |
| 1.405 Charge Frac | 1.405                                |
| None              |                                      |

HVAC System Single-Speed ASHP options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC Secondary Heating characteristic”. See the OpenStudio-HPXML [Air-to-Air Heat Pumps](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#air-to-air-heat-pump) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ss_hp_charge" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `heat_pump_frac_manufacturer_charge` | false | Frac | Double | The fraction of manufacturer recommended charge of the heat pump. |

The ResStock argument definitions set in the HVAC Secondary Heating characteristic

</div>

### HVAC System Single-Speed AC Airflow

#### Description

Single-speed central and room air conditioner actual air flow rates for faulted systems. Not currently used since ResStock lacks data on faulted systems.

#### Distribution Data Source(s)

- *Impact of installation faults in air conditioners and heat pumps in single-family homes on U.S. energy usage* ((Winkler et al. 2020)).

#### Direct Conditional Dependencies

- HVAC Cooling Efficiency

- HVAC System is Faulted.

#### Options

Twelve options are given for real airflow, but none are currently in use (Table “HVAC System Single-Speed AC Airflow options and arguments that vary for each option”). The `heat_pump_rated_cfm_per_ton` argument is set to 400 for all options.

<div id="table:hc_opt_hvac_ss_ac_airflow" data-source="3b_ResStockInputs_HVAC.tex">

| Option name   | `heat_pump_actual_cfm_per_ton` |
|:--------------|:-------------------------------|
| 154.8 cfm/ton | 154.8                          |
| 204.4 cfm/ton | 204.4                          |
| 254.0 cfm/ton | 254.0                          |
| 303.5 cfm/ton | 303.5                          |
| 353.1 cfm/ton | 353.1                          |
| 402.7 cfm/ton | 402.7                          |
| 452.3 cfm/ton | 452.3                          |
| 501.9 cfm/ton | 501.9                          |
| 551.5 cfm/ton | 551.5                          |
| 601.0 cfm/ton | 601.0                          |
| 650.6 cfm/ton | 650.6                          |
| 700.2 cfm/ton | 700.2                          |
| None          | 100%                           |

HVAC System Single-Speed AC Airflow options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC System Single-Speed AC Airflow characteristic”. See the OpenStudio-HPXML [Central Air Conditioner](-https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#central-air-conditioner) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_ss_ac_airflow" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type s | Description |
|:---|:---|:---|:---|:---|
| `heat_pump_rated_cfm_per_ton` | false | cfm/ton | Double | The rated cfm per ton of the heat pump. |
| `heat_pump_actual_cfm_per_ton` | false | cfm/ton | Double | The actual cfm per ton of the heat pump. |

The ResStock argument definitions set in the HVAC System Single-Speed AC Airflow characteristic

</div>

#### Distribution Assumption(s)

None

### HVAC System Single-Speed AC Charge

#### Description

Central and room air conditioner deviation between design/installed charge.

#### Distribution Data Source(s)

- *Impact of installation faults in air conditioners and heat pumps in single-family homes on U.S. energy usage* ((Winkler et al. 2020)).

#### Direct Conditional Dependencies

- HVAC Cooling Efficiency

- HVAC System is Faulted.

#### Options

Seven different options are available for faulted AC charges, but none are currently in use (Table “HVAC System Single-Speed AC Charge options and arguments that vary for each option”).

<div id="table:hc_opt_ss_ac_charge" data-source="3b_ResStockInputs_HVAC.tex">

| Option name       | `cooling_system_frac_manufacturer_charge` |
|:------------------|:------------------------------------------|
| 0.570 Charge Frac | 0.570                                     |
| 0.709 Charge Frac | 0.709                                     |
| 0.848 Charge Frac | 0.848                                     |
| 0.988 Charge Frac | 0.988                                     |
| 1.127 Charge Frac | 1.127                                     |
| 1.266 Charge Frac | 1.266                                     |
| 1.405 Charge Frac | 1.405                                     |
| None              |                                           |

HVAC System Single-Speed AC Charge options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC System Single-Speed AC Charge”. See the OpenStudio-HPXML [Air Distribution](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-air-distribution) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_ss_ac_charge" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `cooling_system_frac_manufacturer_charge` | false | Frac | Double | The fraction of manufacturer recommended charge of the cooling system. |

The ResStock argument definitions set in the HVAC System Single-Speed AC Charge

</div>

#### Distribution Assumption(s)

None.

#### Distribution Assumption(s)

None.

### HVAC System is Scaled

#### Description

Whether the HVAC system has been undersized or oversized (not used in baseline) compared to what was autosized using ACCA Manual J and Manual S.

#### Distribution Data Source(s)

This is currently a capability that is not used. ResStock assumes no oversizing or undersizing, until we have the data necessary to characterize all types of systems.

#### Direct Conditional Dependencies

None.

#### Options

All buildings assigned an option of “No” with no associated ResStock arguments.

#### Distribution Assumption(s)

None.

### HVAC System is Faulted

#### Description

The presence of an HVAC system giving a fault or error. Note: this is a capability but is not used in baseline ResStock.

#### Distribution Data Source(s)

N/A.

#### Direct Conditional Dependencies

None.

#### Options

All homes currently set to “No” with no associated ResStock arguments.

#### Distribution Assumption(s)

None.

