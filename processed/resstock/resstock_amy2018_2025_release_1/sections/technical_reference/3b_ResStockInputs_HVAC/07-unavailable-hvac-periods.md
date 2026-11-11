<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3b_ResStockInputs_HVAC.md | section: Unavailable HVAC Periods | lines: 1902-2029 -->
## Unavailable HVAC Periods

### Modeling Approach

Periods when the HVAC system is unavailable, either due to a system malfunction or because the household cannot afford to operate it, are modeled in ResStock. These periods are assigned using the availability schedules in OpenStudio-HPXML. Separate unavailability periods are defined for heating and cooling. The length of these periods can range from 0 days (indicating the HVAC system is always available) to a single day, or up to the entire year. If the "Year Round" option is sampled, the unavailability period is set to "Jan 1 - Dec 31." For a partial-year unavailability (e.g., 1, 7, 14 days, etc.), a randomly selected n-day period (where n is the duration of the unavailability) is chosen to start during the Building America heating or cooling months, as defined in the Building America House Simulation Protocols (E. Wilson et al. 2014b). In locations without Building America heating or cooling months (e.g., Hawaii has no heating months), the heating season is assumed to be December through February, and the cooling season is assumed to be June through August. If the number of unavailable days exceeds the length of the Building America season, the unavailability period extends beyond the defined season. To ensure deterministic simulations, the `building_id` is used as the seed for random date selection. There are two characteristics that sets the number of days the heating and cooling system is unavailable 1) Cooling Unavailable Days and 2) Heating Unavailable Days.

### Cooling Unavailable Days

#### Description

Number of days in a year the cooling system is unavailable.

#### Distribution Data Source(s)

- U.S. EIA 2020 Residential Energy Consumption Survey (RECS) microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- Tenure

#### Options

The options of Cooling Unavailable Days characteristic are a number of days the cooling system is unavailable. The characteristic sets the `schedules_space_cooling_unavailable_days` argument. The argument definition can be found in Table “The ResStock argument definitions set in the Cooling Unavailable Days characteristic”.

<div id="table:hc_arg_def_cooling_unavailable_days" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `schedules_space_cooling_unavailable_days` | false |  | Integer | Number of days space cooling equipment is unavailable. |

The ResStock argument definitions set in the Cooling Unavailable Days characteristic

</div>

The options range between 0 days (Never) to the whole year (year round). The Void option is for impossible combinations that are not sampled.

<div id="table:hc_opt_cooling_unavailable_days" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `schedules_space_cooling_unavailable_days` |
|:------------|:-------------------------------------------|
| Never       | 0                                          |
| 1 day       | 1                                          |
| 3 days      | 3                                          |
| 1 week      | 7                                          |
| 2 weeks     | 14                                         |
| 1 month     | 30                                         |
| 3 months    | 90                                         |
| Year round  | 365                                        |
| Void        |                                            |

Cooling Unavailable Days options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

None

### Heating Unavailable Days

#### Description

Number of days in a year the heating system is unavailable.

#### Distribution Data Source(s)

- U.S. EIA 2020 Residential Energy Consumption Survey (RECS) microdata.

#### Direct Conditional Dependencies

- Cooling Unavailable Days

- Federal Poverty Level

- Geometry Building Type RECS

#### Options

The options of Heating Unavailable Days characteristic are a number of days the cooling system is unavailable. The characteristic sets the `schedules_space_heating_unavailable_days` argument. The argument definition can be found in Table “The ResStock argument definitions set in the Heating Unavailable Days characteristic”.

<div id="table:hc_arg_def_heating_unavailable_days" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `schedules_space_heating_unavailable_days` | false |  | Integer | Number of days space heating equipment is unavailable. |

The ResStock argument definitions set in the Heating Unavailable Days characteristic

</div>

The options range between 0 days (Never) to the whole year (year round). The Void option is for impossible combinations that are not sampled.

<div id="table:hc_opt_heating_unavailable_days" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `schedules_space_heating_unavailable_days` |
|:------------|:-------------------------------------------|
| Never       | 0                                          |
| 1 day       | 1                                          |
| 3 days      | 3                                          |
| 1 week      | 7                                          |
| 2 weeks     | 14                                         |
| 1 month     | 30                                         |
| 3 months    | 90                                         |
| Year round  | 365                                        |
| Void        |                                            |

Heating Unavailable Days options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

- Where samples are less than 10, the data is aggregated in the following order until there are no rows with less than 10 samples:

  - The Federal Poverty Level dependency is aggregated every 100% bins

  - The Federal Poverty Level dependency is aggregated every 200% bins

  - The Geometry Building Type RECS dependency is aggregated into single-family, multi-family, and mobile home bins.

  - The Cooling Unavailable Days dependency is aggregated into days, weeks, month, and year round bins.

  - The Cooling Unavailable Days dependency is removed.

