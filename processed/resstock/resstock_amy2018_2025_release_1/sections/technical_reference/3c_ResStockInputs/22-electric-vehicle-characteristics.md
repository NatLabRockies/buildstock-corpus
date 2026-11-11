<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Electric Vehicle Characteristics | lines: 2837-3179 -->
## Electric Vehicle Characteristics

### Electric Vehicle Ownership

#### Description

The dwelling unit owns an electric vehicle.

#### Distribution Data Source(s)

- EV Registration Data from Experian 2023.

- 2019-5yrs Public Use Microdata Samples (PUMS). IPUMS USA, University of Minnesota, www.ipums.org.

- U.S. EIA 2020 Residential Energy Consumption Survey (RECS) microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- PUMA

- Tenure

#### Options

The options for Electric Vehicle Ownership characteristic determine if other arguments for the EV are used. The characteristic sets the `vehicle_type` ResStock argument. The argument definition is found in Table “The ResStock argument definitions set in the Electric Vehicle Ownership characteristic”.

<div id="table:hc_arg_def_ev_ownership" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `vehicle_type` | false |  | String |  | The type of vehicle present at the home. |

The ResStock argument definitions set in the Electric Vehicle Ownership characteristic

</div>

The options and their ResStock arguments values can be found in Table “Electric Vehicle Ownership options and arguments that vary for each option”. The Void option is used for impossible dependency conditions and is not sampled.

<div id="table:hc_opt_ev_ownership" data-source="3c_ResStockInputs.tex">

| Option name | `vehicle_type`         |
|:------------|:-----------------------|
| No          |                        |
| Void        |                        |
| Yes         | BatteryElectricVehicle |

Electric Vehicle Ownership options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

- Due to low sample sizes, coarsening rules applied in the following order.

  1.  Federal Poverty Level lumped every 100%

  2.  Federal Poverty Level lumped every 200%

  3.  Building type is consolidated into three bins 1) single-family, 2) multi-family, and 3) mobile home

  4.  Building type is consolidated into two bins 1) single-family and 2) multi-family and mobile home

- PUMA level battery EV saturation is calculated using a weighted average of the County level Experian data and ResStock unit counts for each County and PUMA.

- The RECS 2020 satuations for each segment in a given PUMA are scaled to match the Experian PUMA weighted averaged battery EV saturation using the segment unit counts from PUMS 2019-5yrs survey.

### Electric Vehicle Battery

#### Description

The type of electric vehicle and battery range in miles.

#### Distribution Data Source(s)

- The 2023 Vehicle Stock Projection Data from NREL’s TEMPO model

- EV Registration Data from Experian 2023

#### Direct Conditional Dependencies

No direct conditional dependencies.

#### Options

The options for Electric Vehicle Battery characteristic is a set of electric vehicle types and battery range in miles. These options do not specifiy if the unit has a vehicle, but rather the preference of the vehicle type and battery range if the household owned an electric vehicle. Every unit is assigned one of these options so that the vehicle type and battery range does not need to be sampled during an electric vehicle upgrade. The housing units at which an electric vehicle is modeled are specified by the Electric Vehicle Ownership characteristic. The characteristic sets the `vehicle_battery_usable_capacity`, `vehicle_fuel_economy_units`, `vehicle_fuel_economy_combined`, `ev_average_mph`, and `ev_efficiency_percent_increase` ResStock arguments. The argument definitions are found in Table “The ResStock argument definitions set in the Electric Vehicle Battery characteristic”.

<div id="table:hc_arg_def_ev_battery" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `vehicle_battery_usable_capacity` | false | kWh | Double | auto | The usable capacity of the vehicle battery, only applies to electric vehicles. If not provided, the OS-HPXML default (see [HPXML Vehicles](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-vehicles)) is used. |
| `vehicle_fuel_economy_units` | false |  | Choice | auto, kWh/mile, mile/kWh, mpge, mpg | The combined fuel economy units of the vehicle. Only ’kWh/mile’, ’mile/kWh’, or ’mpge’ are allow for electric vehicles. If not provided, the OS-HPXML default (see [HPXML Vehicles](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-vehicles>)) is used. |
| `vehicle_fuel_economy_combined` | false |  | Double | auto | The combined fuel economy of the vehicle. If not provided, the OS-HPXML default (see [HPXML Vehicles](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-vehicles>)) is used. |
| `ev_average_mph` | false | miles/hour | Double |  | The average miles/hour driven by the vehicle. |
| `ev_efficiency_percent_increase` | false | Frac | Double |  | The increase (fraction) in efficiency of the electric vehicle. |

The ResStock argument definitions set in the Electric Vehicle Battery characteristic

</div>

The options and their ResStock argument values can be found in Table “Electric Vehicle Battery options and arguments that vary for each option”. The Experian dataset is used to characterize the distribution of electric vehicles and associated battery sizes in the vehicle stock. We used the latest available data for the year 2023, which ensures that our analysis is based on the most current information regarding the electric vehicle battery stock. Although the vehicle data included information on internal combustion engine vehicles in addition to the battery electric vehicles, we filtered the dataset to focus exclusively on personal light-duty battery electric vehicles. In the dataset, there are four different categories of light-duty vehicles, including (a) Compact, (b) Midsize, (c) Sport Utility Vehicle (SUV), and (d) Pickup truck. Additionally, the dataset includes information on two total mileage ranges for the battery: (a) 200-mile range and (b) 300-mile range.

Then, for each electric vehicle type, we draw from Argonne National Laboratory’s Autonomie20[^6] vehicle powertrain simulation model for the electric vehicle energy consumption (`vehicle_fuel_economy_combined`) and battery capacity (`vehicle_battery_usable_capacity`). The units for the combined fuel economy (`vehicle_fuel_economy_units`) are always kWh/mile. The average driving speed is sourced from the 2017 NHTS which summarizes U.S. travel behavior ((Federal Highway Administration 2017)). We assume that the average speed of electric vehicles is the same as the average speed of all vehicles. A scaling factor is applied to increase the efficiency of electric vehicles (`ev_efficiency_percent_increase`). This value is 0.0 for the ResStock baseline meaning that the efficiency is equal to `vehicle_fuel_economy_combined`, but it is exposed so that scenarios of EV efficiency improvements can be modeled.

<div id="table:hc_opt_ev_battery" data-source="3c_ResStockInputs.tex">

| Option name | `vehicle_battery_usable_capacity` | `vehicle_fuel_economy_combined` | `ev_average_mph` | `vehicle_fuel_economy_units` | `ev_efficiency_percent_increase` |
|:---|:---|:---|:---|:---|:---|
| Compact, Battery Electric Vehicle, 200 mile range | 40.168 | 0.209901 | 22 | kWh/mile | 0.0 |
| Compact, Battery Electric Vehicle, 300 mile range | 63.433 | 0.220020 | 22 | kWh/mile | 0.0 |
| Midsize, Battery Electric Vehicle, 200 mile range | 41.978 | 0.219174 | 22 | kWh/mile | 0.0 |
| Midsize, Battery Electric Vehicle, 300 mile range | 65.441 | 0.229449 | 22 | kWh/mile | 0.0 |
| Pickup, Battery Electric Vehicle, 200 mile range | 67.738 | 0.357648 | 22 | kWh/mile | 0.0 |
| Pickup, Battery Electric Vehicle, 300 mile range | 105.946 | 0.373794 | 22 | kWh/mile | 0.0 |
| SUV, Battery Electric Vehicle, 200 mile range | 53.503 | 0.267513 | 22 | kWh/mile | 0.0 |
| SUV, Battery Electric Vehicle, 300 mile range | 83.680 | 0.278934 | 22 | kWh/mile | 0.0 |

Electric Vehicle Battery options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

- Vehicle stock data starts with the Experian registration data and then is projected by TEMPO to 2023.

- If the household does not have an electric vehicle, the options represent the household preference.

### Electric Vehicle Charge At Home

#### Description

The percentage a household would or does charge their electric vehicle at home.

#### Distribution Data Source(s)

U.S. EIA 2020 Residential Energy Consumption Survey (RECS) microdata.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

#### Options

The options for the Electric Vehicle Charge At Home characteristic is a set of percentages that determine how much of the electric vehicle’s energy shows up on the residential meter vs charging at work or at public chargers. Every unit in the baseline is assigned one of these options so that the home charging fraction does not need to be sampled during an electric vehicle upgrade. The units with an electric vehicle are specified by the Electric Vehicle Ownership characteristic. The characteristic sets the `vehicle_fraction_charged_home` ResStock argument. The argument definition is found in Table “The ResStock argument definitions set in the Electric Vehicle Charge At Home characteristic”.

<div id="table:hc_arg_def_ev_charge_at_home" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `vehicle_fraction_charged_home` | false |  | Double | auto | The fraction of charging energy provided by the at-home charger to the vehicle, only applies to electric vehicles. If not provided, the OS-HPXML default (see [HPXML Vehicles](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-vehicles)) is used. |

The ResStock argument definitions set in the Electric Vehicle Charge At Home characteristic

</div>

The options and their ResStock arguments values can be found in Table “Electric Vehicle Charge At Home options and arguments that vary for each option”.

<div id="table:hc_opt_ev_charge_at_home" data-source="3c_ResStockInputs.tex">

| Option name | `vehicle_fraction_charged_home` |
|:------------|:--------------------------------|
| 0-19%       | 0.1                             |
| 20-39%      | 0.3                             |
| 40-59%      | 0.5                             |
| 60-79%      | 0.7                             |
| 80-99%      | 0.9                             |
| 100%        | 1.0                             |

Electric Vehicle Charge At Home options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

- Due to a low sample count, the distributions are constructed by downscaling a dwelling unit sub-tsv with a household sub-tsv. The two sub-tsvs have the following dependencies: tsv1 dependency=\[’Geometry Building Type RECS’\], tsv2 dependency=\[’Federal Poverty Level’\], In combining tsv1 and tsv2, the conditional relationships are ignored across (’Geometry Building Type RECS’ and ’Federal Poverty Level’).

### Electric Vehicle Charger

#### Description

Presence and type of electric vehicle charger used at the dwelling unit.

#### Distribution Data Source(s)

U.S. EIA 2020 Residential Energy Consumption Survey (RECS) microdata.

#### Direct Conditional Dependencies

- Electrical Vehicle Ownership

- Federal Poverty Level

- Geometry Building Type RECS

- Tenure

#### Options

The options for the Electric Vehicle Charger characteristic describe the type of charger used by an electric vehicle owner at home. The characteristic sets the `ev_charger_present`, `ev_charger_power`, and `ev_charger_location` ResStock arguments. The argument definition is found in Table “The ResStock argument definitions set in the Electric Vehicle Charger characteristic”. If `ev_charger_present` is set to "true", then the other arguments are required otherwise the power and location arguments will not be used. In the baseline stock the `ev_charger_location` argument is set to "auto", meaning it takes the default OpenStudio-HPXML value (see OpenStudio-HPXML [Electric Vehicle Charger](https://openstudio-hpxml.readthedocs.io/en/latest/workflow_inputs.html#hpxml-electric-vehicle-chargers)).

<div id="table:hc_arg_def_ev_charger" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `ev_charger_present` | false |  | Boolean | auto, true, false | Whether there is an electric vehicle charger present. |
| `ev_charger_power` | false | W | Double | auto | The rated power output of the EV charger. If not provided, the OS-HPXML default (see HPXML [Electric Vehicle Chargers](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-electric-vehicle-chargers>)) is used. |
| `ev_charger_location` | false |  | Choice | auto, garage, outside | The space type for the EV charger. If not provided, the OS-HPXML default (see HPXML [Electric Vehicle Chargers](<https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-electric-vehicle-chargers>)) is used. |

The ResStock argument definitions set in the Electric Vehicle Charger characteristic

</div>

The options and their ResStock arguments values can be found in Table “Electric Vehicle Charger options and arguments that vary for each option”. The Void option will not be sampled but indicates when an impossible combination of dependencies are listed.

<div id="table:hc_opt_ev_charger" data-source="3c_ResStockInputs.tex">

| Option name | `ev_charger_present` | `ev_charger_power` | `ev_charger_location` |
|:---|:---|:---|:---|
| Level 1 charger | true | 1600 | auto |
| Level 2 charger | true | 5690 | auto |
| None | false |  |  |
| Void | false |  |  |

Electric Vehicle Charger options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

Dwelling units with an electric vehicle need to have at least a Level 1 charger. Due to low sample sizes, coarsening of the dependencies are applied in the following order.

1.  Federal Poverty Level lumped every 100%

2.  Federal Poverty Level lumped every 200%

3.  Building type is consolidated into three bins 1) single-family detached and 2) multi-family with 5+ units, and 3) mobile homes, multi-family 2-4 units, and single-family attached

4.  Building type is consolidated into two bins 1) single-family detached and 2) all other building types

5.  Federal Poverty Level is combined into 400%+ and \<400% bins

### Electric Vehicle Miles Traveled

#### Description

The number of miles an electric vehicle is driven in a year if the unit owns an electric vehicle.

#### Distribution Data Source(s)

The 2022 U.S. Federal Highway Administration National Household Travel Survey (NHTS) microdata.

#### Direct Conditional Dependencies

No direct conditional dependencies.

#### Options

The options for Electric Vehicle Miles Traveled characteristic are a set of miles traveled by the electric vehicle. These options do not specifiy if the unit has a vehicle, but rather the amount of miles the EV travels if the dwelling unit has an electric vehicle. Every unit is assigned one of these options so that the vehicle miles traveled does not need to be sampled during an electric vehicle upgrade. The units with an electric vehicle is specified by the Electric Vehicle Ownership characteristic. The characteristic sets the `vehicle_miles_driven_per_year` ResStock argument. The argument definition is found in Table “The ResStock argument definitions set in the Electric Vehicle Miles Traveled characteristic”.

<div id="table:hc_arg_def_ev_vmt" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `vehicle_miles_driven_per_year` | false | miles | Double | auto | The annual miles the vehicle is driven. If not provided, the OS-HPXML default (see HPXML [Vehicles](<https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-vehicles>)) is used. |

The ResStock argument definitions set in the Electric Vehicle Miles Traveled characteristic

</div>

The options and their ResStock arguments values can be found in Table “Electric Vehicle Vehicle Miles Traveled options and arguments that vary for each option”. The options range between 1,000 miles and 22,500 miles.

<div id="table:hc_opt_ev_vmt" data-source="3c_ResStockInputs.tex">

| Option name | `vehicle_miles_driven_per_year` |
|:------------|:--------------------------------|
| 1000        | 1000                            |
| 3000        | 3000                            |
| 5000        | 5000                            |
| 7000        | 7000                            |
| 9000        | 9000                            |
| 11000       | 11000                           |
| 13000       | 13000                           |
| 15000       | 15000                           |
| 17000       | 17000                           |
| 19000       | 19000                           |
| 22500       | 22500                           |

Electric Vehicle Vehicle Miles Traveled options and arguments that vary for each option

</div>

#### Distribution Assumption(s)

No assumptions are made.

### Electric Vehicle Outlet Access

#### Description

The unit has an outlet within 20 feet of vehicle parking.

#### Distribution Data Source(s)

U.S. EIA 2020 Residential Energy Consumption Survey (RECS) microdata.

#### Direct Conditional Dependencies

- Electric Vehicle Charger

- Federal Poverty Level

- Geometry Building Type RECS

- Tenure

- Vinteage ACS

#### Options

The options for Electric Vehicle Outlet Access characteristic indicate whether the unit has charging within 20 ft of the vehicle parking. This characteristic does not assign any ResStock arguments. The options are Yes, No, and Void. The Void option is assigned to impossible dependency combinations.

#### Distribution Assumption(s)

- RECS 2020 has Multi-Family 5+ units marked as Not Applicable. These units are replaced by data from the No Place Like Home Study (https://www.nrel.gov/docs/fy22osti/81065.pdf) Table 1 Scenario 2. Multi-Family 5+ units owners is assumed for 12% units having electrical access. This fraction is based on the average of mid-capacity apartment and high-capacity apartment. Multi-Family 5+ units owners is assumed for 28% units having electrical access.

- Units reported to have a Level 1 or Level 2 charger in the field EVCHRGTYPE are assumed to have outlet access.

- Level 1 chargers without outlet access are units with EVs, but report no outlet access within 20 ft of vehicle parking.

- Due to low sample count, the tsv is constructed by downscaling a dwelling unit sub-tsv with a household sub-tsv. The sub-tsvs have the following dependencies:

  - Dwelling unit sub-tsv : deps=\[’Geometry Building Type RECS’, ’Vintage ACS’, ’Electric Vehicle Charger’\] with the following fallback coarsening order: 1) Vintage ACS to the National distribution and 2) combining Geometry Building Type RECS together into two bins a) single-family detached, mobile homes, and single family attached and b) multi-family with 2 - 4 units and multi-family with 5+ units

  - Household sub-tsv : deps=\[’Geometry Building Type RECS’, ’State’ ’Tenure’, ’Federal Poverty Level’\]

  - In combining the dwelling unit sub-tsv and household sub-tsv, the conditional relationships are ignored across (\[’Vintage ACS’, ’Electric Vehicle Charger’\], \[’Tenure’, ’Federal Poverty Level’\]).

