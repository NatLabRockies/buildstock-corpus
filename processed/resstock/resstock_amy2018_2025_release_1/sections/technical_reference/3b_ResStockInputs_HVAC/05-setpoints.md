<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3b_ResStockInputs_HVAC.md | section: Setpoints | lines: 1222-1696 -->
## Setpoints

### Setpoints Modeling Approach

There are a set of characteristics that assign heating and cooling setpoint schedules in ResStock. The characteristics assign the setpoint, whether there is a setpoint offset, the magnitude of the setpoint offset, and the offset period. The heating and cooling setpoints determine the temperature past which heating and cooling systems run to condition the home. They can vary over time as occupants change their thermostat settings, often choosing different settings overnight or when they are away from home. The setpoint offset specifies whether there is a change in the setpoint at any point during the day. An example would be a heating setback where the heating setpoint temperature is decreased during the day when no one is home. The offset magnitude is the number of degrees of the offset. The offset period determines what hours of the day the offset applies.

Every housing unit is assigned a heating setpoint and cooling setpoint, regardless of whether it has a heating system or a cooling system. If a sampled heating setpoint is greater than the cooling setpoint, the values are averaged and kept constant across heating and cooling seasons. Every housing unit is also assigned heating setpoint offsets, cooling setpoint offsets, or neither, and an offset magnitude and time period for any offsets it is assigned. The reason for the assignment of setpoint schedules for housing units without either heating or cooling systems is mainly for upgrades, as a diverse set of setpoint schedules can be applied to the unit without complicated upgrade apply logic. Another interpretation is that these setpoint schedules would be the preference of the housing units if they had a heating or cooling system.

The following describes the building stock characteristic distributions, their data sources, options, argument values, and assumptions.

### Heating Setpoint

#### Description

Base heating setpoint (prior to any offset applied).

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Building Type RECS

- HVAC Has Zonal Electric Heating

- HVAC Heating Type

- Tenure.

#### Options

The options for the housing unit heating setpoint range between 55° F and 80° F (Table “Heating Setpoint options and arguments that vary for each option”). All setpoints that are assigned 55° F are vacant units. The heating setpoint characteristic sets the `hvac_control_heating_season_period`, `hvac_control_heating_weekday_setpoint_temp`, `hvac_control_heating_weekend_setpoint_temp`, and `use_auto_heating_season` arguments. Argument definitions are in Table “The ResStock argument definitions set in the Heating Setpoint characteristic”. The `hvac_control_heating_season_period` is always set to “auto,” and the `use_auto_heating_season` argument is always set to “false,” meaning the heating system will run as needed year-round. The heating set points are the same for weekdays and weekends.

<div id="table:hc_opt_ht_stp" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `hvac_control_heating_weekday_setpoint_temp` | `hvac_control_heating_weekend_setpoint_temp` |
|:---|:---|:---|
| 55F | 55 | 55 |
| 60F | 60 | 60 |
| 62F | 62 | 62 |
| 65F | 65 | 65 |
| 67F | 67 | 67 |
| 68F | 68 | 68 |
| 70F | 70 | 70 |
| 72F | 72 | 72 |
| 75F | 75 | 75 |
| 76F | 76 | 76 |
| 78F | 78 | 78 |
| 80F | 80 | 80 |

Heating Setpoint options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_ht_stp" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hvac_control_heating_season_period` | false |  | String | auto | Enter a date like 'Nov 1 - Jun 30'. Can also provide 'BuildingAmerica' to use automatic seasons from the Building America House Simulation Protocols. |
| `hvac_control_heating_weekday_setpoint_temp` | true | deg-F | Double |  | Specify the weekday heating setpoint temperature. |
| `hvac_control_heating_weekend_setpoint_temp` | true | deg-F | Double |  | Specify the weekend heating setpoint temperature. |
| `use_auto_heating_season` | true |  | Boolean | true, false | Specifies whether to automatically define the heating season based on the weather file. |

The ResStock argument definitions set in the Heating Setpoint characteristic

</div>

#### Distribution Assumption(s)

- For dependency conditions with low samples, the dependency values are lumped together in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, (2) lump buildings into Single-Family and Multifamily only, and lump nearby climate zones within A/B regions and separately 7AK and 8AK, and (3) lump all building types together, and lump climate zones within A/B regions and separately 7AK and 8AK.

- Heating type dependency is always lumped into Heat pump/Non-heat pumps.

- For vacant units (for which Tenure = ‘Not Available’), the heating setpoint is set to 55° F.

### Heating Setpoint Has Offset

#### Description

Presence of a heating setpoint offset.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Building Type RECS

- HVAC Has Zonal Electric Heating.

#### Options

The options are either “Yes” or “No.” The options do not assign any ResStock arguments.

#### Distribution Assumption(s)

- For dependency conditions with low samples, the following dependency values are lumped together in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, and (2) lump all building types together.

### Heating Setpoint Offset Magnitude

#### Description

The magnitude of the heating setpoint offset.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Building Type RECS

- Heating Setpoint Has Offset

- HVAC Has Zonal Electric Heating.

#### Options

The options for Heating Setpoint Offset Magnitude are 0F, 3F, 6F, and 12F (Table “Heating Setpoint Offset Magnitude options and arguments that vary for each option”). The options are the ° F that the heating setpoint is decreased if a heating setpoint offset is selected. The heating offset magnitude is the same for weekdays and weekends. The Heating Setpoint Offset Magnitude characteristic sets the `hvac_control_heating_weekday_setpoint_offset_magnitude` and `hvac_control_heating_weekend_setpoint_offset_magnitude` arguments. Argument definitions are in Table “The ResStock argument definitions set in the Heating Setpoint Offset Magnitude characteristic”.

<div id="table:hc_opt_ht_stp_mag" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `hvac_control_heating_weekday_setpoint_offset_magnitude` | `hvac_control_heating_weekend_setpoint_offset_magnitude` |
|:---|:---|:---|
| 0F | 0 | 0 |
| 3F | 3 | 3 |
| 6F | 6 | 6 |
| 12F | 12 | 12 |

Heating Setpoint Offset Magnitude options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_ht_stp_mag" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hvac_control_heating_weekday_setpoint_offset_magnitude` | true | deg-F | Double |  | Specify the weekday heating offset magnitude. |
| `hvac_control_heating_weekend_setpoint_offset_magnitude` | true | deg-F | Double |  | Specify the weekend heating offset magnitude. |

The ResStock argument definitions set in the Heating Setpoint Offset Magnitude characteristic

</div>

#### Distribution Assumption(s)

- For dependency conditions with low samples, the following dependency values are lumped together in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, (2) lump buildings into Single-Family and Multifamily only, and lump nearby climate zones within A/B regions and separately 7AK and 8AK, and (3) lump all building types together and lump climate zones within A/B regions and separately 7AK and 8AK.

### Heating Setpoint Offset Period

#### Description

The time period(s) for the housing unit’s heating setpoint offset.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Building Type RECS

- Heating Setpoint Has Offset

- HVAC Has Zonal Electric Heating.

#### Options

The options are a combination of day and night offset periods (Table “Heating Setpoint Offset Period options and arguments that vary for each option.”). The default for the day is from 9 AM to 5 PM and for the night is 10 PM to 7 AM. The options then shift these periods randomly up to 5 hours in either direction. The shifting of the periods is mainly to avoid the synchronization of HVAC systems across the housing stock from all turning on and off at the same time. The characteristic sets the `hvac_control_heating_weekday_setpoint_schedule` and `hvac_control_heating_weekend_setpoint_schedule` ResStock arguments. The values for the arguments are 24-hour arrays for when the setback occurs (a value of -1) and when the setback does not occur (a value of 0). The argument definitions are in Table “The ResStock argument definitions set in the Heating Setpoint Offset Period characteristic”.

<div id="table:hc_opt_ht_stp_per" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `hvac_control_heating_weekday_setpoint_schedule` | `hvac_control_heating_weekend_setpoint_schedule` |
|:---|:---|:---|
| Day | 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day -1h | 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day -2h | 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day -3h | 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day -4h | 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day -5h | 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day +1h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day +2h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day +3h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day +4h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day +5h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day and Night | -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1 | -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1 |
| Day and Night -1h | -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1 | -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1 |
| Day and Night -2h | -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1 | -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1 |
| Day and Night -3h | -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 | -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 |
| Day and Night -4h | -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 | -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 |
| Day and Night -5h | -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 | -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 |
| Day and Night +1h | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1 | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1 |
| Day and Night +2h | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0 | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day and Night +3h | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0 | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day and Night +4h | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0 | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day and Night +5h | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0 | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night | -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1 | -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1 |
| Night -1h | -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1 | -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1 |
| Night -2h | -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1 | -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1 |
| Night -3h | -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 | -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 |
| Night -4h | -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 | -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 |
| Night -5h | -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 | -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 |
| Night +1h | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1 | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1 |
| Night +2h | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night +3h | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night +4h | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night +5h | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| None | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |

Heating Setpoint Offset Period options and arguments that vary for each option.

</div>

<div id="table:hc_arg_def_ht_stp_per" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hvac_control_heating_weekday_setpoint_schedule` | true |  | String |  | Specify the 24-hour comma-separated weekday heating schedule of 0s and 1s. |
| `hvac_control_heating_weekend_setpoint_schedule` | true |  | String |  | Specify the 24-hour comma-separated weekend heating schedule of 0s and 1s. |

The ResStock argument definitions set in the Heating Setpoint Offset Period characteristic

</div>

#### Distribution Assumption(s)

- For dependency conditions with low samples, the following dependency values are lumped in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, (2) lump buildings into Single-Family and Multifamily only, and lump nearby climate zones within A/B regions and separately 7AK and 8AK, and (3) lump all building types together and lump climate zones within A/B regions and separately 7AK and 8AK.

### Cooling Setpoint

#### Description

Baseline cooling setpoint (prior to any offset applied).

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Building Type RECS

- HVAC Cooling Type

- Tenure.

#### Options

The options for the Cooling Setpoint characteristic range between 60° F and 80° F (Table “Cooling Setpoint options and arguments that vary for each option”). The Cooling Setpoint characteristic sets the `hvac_control_cooling_season_period`, `hvac_control_cooling_weekday_setpoint_temp`, `hvac_control_cooling_weekend_setpoint_temp`, and `use_auto_cooling_season` ResStock arguments. The `hvac_control_cooling_season_period` argument is always set to “auto.” The `use_auto_cooling_season` argument is always set to “false.” These arguments allow the cooling system to run all year as needed. Argument definitions are in Table “The ResStock argument definitions set in the Cooling Setpoint characteristic”.

<div id="table:hc_opt_cl_stp" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `hvac_control_cooling_weekday_setpoint_temp` | `hvac_control_cooling_weekend_setpoint_temp` |
|:---|:---|:---|
| 60F | 60 | 60 |
| 62F | 62 | 62 |
| 65F | 65 | 65 |
| 67F | 67 | 67 |
| 68F | 68 | 68 |
| 70F | 70 | 70 |
| 72F | 72 | 72 |
| 75F | 75 | 75 |
| 76F | 76 | 76 |
| 78F | 78 | 78 |
| 80F | 80 | 80 |

Cooling Setpoint options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_cl_stp" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hvac_control_cooling_season_period` | false |  | String | auto | Enter a date like 'Jun 1 - Oct 31'. Can also provide 'BuildingAmerica' to use automatic seasons from the Building America House Simulation Protocols. |
| `hvac_control_cooling_weekday_setpoint_temp` | true | deg-F | Double |  | Specify the weekday cooling setpoint temperature. |
| `hvac_control_cooling_weekend_setpoint_temp` | true | deg-F | Double |  | Specify the weekend cooling setpoint temperature. |
| `use_auto_cooling_season` | true |  | Boolean | true, false | Specifies whether to automatically define the cooling season based on the weather file. |

The ResStock argument definitions set in the Cooling Setpoint characteristic

</div>

#### Distribution Assumption(s)

- For dependency conditions with low samples, the following dependency values are lumped together in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, (2) lump buildings into Single-Family and Multifamily only, and lump nearby climate zones within A/B regions and separately 7AK and 8AK, (3) lump all building types together and lump climate zones within A/B regions and separately 7AK and 8AK, and (4) Owner and Renter are lumped together, which at this point only modifies AK distributions. Vacant units (for which Tenure = ‘Not Available’) are assumed to follow the same distribution as occupied units.

### Cooling Setpoint Has Offset

#### Description

Presence of a cooling setpoint offset.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Building Type RECS.

#### Options

The options of the Cooling Setpoint Has Offset characteristic are “Yes” and “No.” An example of the offset for cooling is when the occupants leave the housing unit (e.g., commute to work), the cooling setpoint temperature is set up to a warmer temperature.

#### Distribution Assumption(s)

- For dependency conditions with low samples, the following dependency values are lumped in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, and (2) lump all building types together and lump climate zones within A/B regions and separately 7AK and 8AK.

### Cooling Setpoint Offset Magnitude

#### Description

The magnitude of cooling setpoint offset.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Cooling Setpoint Has Offset

- Geometry Building Type RECS.

#### Options

The options of the Cooling Setpoint Offset Magnitude characteristic are 0° F, 2° F, 5° F, and 9° F (Table “Cooling Setpoint Offset Magnitude options and arguments that vary for each option”). The characteristic set the `hvac_control_cooling_weekday_setpoint_offset_magnitude` and `hvac_control_cooling_weekend_setpoint_offset_magnitude` ResStock arguments. A zero degree offset corresponds to the setpoint not having an offset. Argument definitions are in Table “The ResStock argument definitions set in the Cooling Setpoint Offset Magnitude characteristic”.

<div id="table:hc_arg_def_cl_stp_mag" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hvac_control_cooling_weekday_setpoint_offset_magnitude` | true | deg-F | Double |  | Specify the weekday cooling offset magnitude. |
| `hvac_control_cooling_weekend_setpoint_offset_magnitude` | true | deg-F | Double |  | Specify the weekend cooling offset magnitude. |

The ResStock argument definitions set in the Cooling Setpoint Offset Magnitude characteristic

</div>

<div id="table:hc_opt_cl_stp_mag" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `hvac_control_cooling_weekday_setpoint_offset_magnitude` | `hvac_control_cooling_weekend_setpoint_offset_magnitude` |
|:---|:---|:---|
| 0F | 0 | 0 |
| 2F | 2 | 2 |
| 5F | 5 | 5 |
| 9F | 9 | 9 |

Cooling Setpoint Offset Magnitude options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

- For dependency conditions with low samples, the following dependency values are lumped in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, (2) lump buildings into Single-Family and Multifamily only, and lump nearby climate zones within A/B regions and separately 7AK and 8AK, and (3) lump all building types together and lumping climate zones within A/B and separately 7AK and 8AK regions.

### Cooling Setpoint Offset Period

#### Description

The time period(s) for the housing unit’s heating setpoint offset.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2020 RECS microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Cooling Setpoint Has Offset

- Geometry Building Type RECS.

#### Options

The options combine day and night offset periods (Table “Cooling Setpoint Offset Period options and arguments that vary for each option”). The default for the day is from 9 AM to 5 PM and for the night is 10 PM to 7 AM. The options then shift these periods randomly up to 5 hours in either direction. The shifting of the periods is mainly to avoid the synchronization of HVAC systems all turning on and off simultaneously. The characteristic set the `hvac_control_cooling_weekday_setpoint_schedule` and `hvac_control_cooling_weekdend_setpoint_schedule` ResStock arguments. The values for the arguments are hourly arrays for when the setup occurs (a value of 1), a setback (a value of -1), and when the setup or setback does not occur (a value of 0). The argument definitions are in Table “The ResStock argument definitions set in the Cooling Setpoint Offset Period characteristic”.

<div id="table:hc_opt_cl_stp_per" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `hvac_control_cooling_weekday_setpoint_schedule` | `hvac_control_cooling_weekend_setpoint_schedule` |
|:---|:---|:---|
| Day and Night Setup | 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1,1, 1, 0, 0, 0, 0, 0, 1, 1 | 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 |
| Day and Night Setup -1h | 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1 | 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1 |
| Day and Night Setup -2h | 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1 | 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 |
| Day and Night Setup -3h | 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 | 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 |
| Day and Night Setup -4h | 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1 | 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1 |
| Day and Night Setup -5h | 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1 | 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1 |
| Day and Night Setup +1h | 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1 | 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 |
| Day and Night Setup +2h | 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day and Night Setup +3h | 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0 | 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day and Night Setup +4h | 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0 | 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day and Night Setup +5h | 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0 | 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup | 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup -1h | 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup -2h | 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup -3h | 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup -4h | 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup -5h | 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup +1h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup +2h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup +3h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup +4h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup +5h | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup and Night Setback | -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, -1 | -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1 |
| Day Setup and Night Setback -1h | -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, -1, -1 | -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1 |
| Day Setup and Night Setback -2h | -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, -1, -1, -1 | -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1 |
| Day Setup and Night Setback -3h | -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 | -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 |
| Day Setup and Night Setback -4h | -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 | -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 |
| Day Setup and Night Setback -5h | -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 | -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 |
| Day Setup and Night Setback +1h | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, -1 | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1 |
| Day Setup and Night Setback +2h | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0 | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup and Night Setback +3h | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0 | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup and Night Setback +4h | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0 | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Day Setup and Night Setback +5h | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0 | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setback | -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1 | -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1 |
| Night Setback -1h | -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1 | -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1 |
| Night Setback -2h | -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1 | -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1 |
| Night Setback -3h | -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 | -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1 |
| Night Setback -4h | -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 | -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1 |
| Night Setback -5h | -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 | -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1 |
| Night Setback +1h | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1 | -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1 |
| Night Setback +2h | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setback +3h | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setback +4h | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setback +5h | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setup | 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 | 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 |
| Night Setup -1h | 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1 | 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1 |
| Night Setup -2h | 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 | 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 |
| Night Setup -3h | 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 | 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 |
| Night Setup -4h | 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1 | 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1 |
| Night Setup -5h | 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1 | 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1 |
| Night Setup +1h | 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 | 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 |
| Night Setup +2h | 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setup +3h | 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setup +4h | 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| Night Setup +5h | 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| None | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |

Cooling Setpoint Offset Period options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_cl_per" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hvac_control_cooling_weekday_setpoint_schedule` | true |  | String |  | Specify the 24-hour comma-separated weekday cooling schedule of 0s and 1s. |
| `hvac_control_cooling_weekend_setpoint_schedule` | true |  | String |  | Specify the 24-hour comma-separated weekend cooling schedule of 0s and 1s. |

The ResStock argument definitions set in the Cooling Setpoint Offset Period characteristic

</div>

#### Distribution Assumption(s)

- For dependency conditions with low samples, the following dependency values are lumped in progressive order until there are enough samples: (1) lump buildings into Single-Family and Multifamily only, (2) lump buildings into Single-Family and Multifamily only, and lump nearby climate zones within A/B regions and separately 7AK and 8AK, and (3) lump all building types together and lump climate zones within A/B and separately 7AK and 8AK regions.

