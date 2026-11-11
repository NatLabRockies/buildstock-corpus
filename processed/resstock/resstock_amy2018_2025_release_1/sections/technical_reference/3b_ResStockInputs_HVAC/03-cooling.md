<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3b_ResStockInputs_HVAC.md | section: Cooling | lines: 630-890 -->
## Cooling

### Modeling Approach

ResStock models various cooling equipment such as central air conditioners, room air conditioners, and heat pumps. Evaporative (swamp) coolers are an option as a cooling type but are not currently modeled. In ResStock, the cooling system is assigned after the heating system, so that if the heating system is a heat pump, the cooling system is also set to a heat pump. Central air conditioners are ducted systems; room air conditioners are equipment that often are in a window or mounted on the wall. Both room air conditioners and central air conditioners sometimes cool only a fraction of the floor area (more common with room air conditioners). This is represented by assigning a fraction of the cooling load to the cooling system. Heat pumps are assumed to serve the 100% of the cooling load. ResStock also varies the efficiency of the cooling system to represent newer, more efficient systems along with older, less efficient systems.

Three input files inform cooling system selection in ResStock:

- HVAC Cooling Type

- HVAC Cooling Efficiency

- HVAC Cooling Partial Space Conditioning.

Additionally, HVAC Cooling Autosizing Factor is related to cooling, but is not currently used in the ResStock baseline.

### HVAC Cooling Type

#### Description

The presence and type of primary cooling system in the housing unit.

#### Distribution Data Source(s)

- U.S. EIA 2020 RECS microdata.

- Alaska-specific distribution is based on Alaska Retrofit Information System (2008 to 2022), maintained by Alaska Housing Finance Corporation.

#### Direct Conditional Dependencies

- Geometry Building Type RECS

- HVAC Heating Type

- State

- Vintage ACS.

#### Options

The options of HVAC Cooling Type are Central AC, Ducted Heat Pump, Evaporative or Swamp Cooler, Non-Ducted Heat Pump, None, and Room AC. The options do not assign any ResStock arguments but are used as dependencies in other characteristics.

#### Distribution Assumption(s)

- Due to low sample sizes, fallback rules were applied, with coarsening of (1) HVAC Heating type: Non-ducted heating and None, (2) Geometry building SF: Mobile, Single-family attached, Single-family detached, (3) Geometry building MF: Multifamily with 2-4 Units, Multifamily with 5+ Units, (4) Vintage Lump: 20-yr bins.

- Homes having ducted heat pump for heating and electricity fuel are assumed to have ducted heat pump for cooling (separating from central AC category).

- Homes having non-ducted heat pump for heating are assumed to have non-ducted heat pump for cooling.

- For Hawaii, central air conditioning saturation is from RECS 2020 by heating type, ignoring all other dependencies

- For Hawaii, Non-Ducted Heat Pump saturation is underestimated because ResStock does not currently allow cooling-only Non-Ducted Heat Pumps. These samples are modeled as Room ACs

- For Alaska, we are using a field in ARIS that lumps multifamily 2-4 units and multifamily 5+ units buildings together. Data from the American Community Survey are used to distribute between these two building types.

- For Alaska, we are not modeling any central and room AC.

- For Alaska, cooling systems are never shared.

- Hawaii does not follow the same fallback rules. All distributions are custom adjusted so that state-level central air-conditioning saturation matches the state-level saturation in RECS2020.

### HVAC Cooling Efficiency

#### Description

The presence and efficiency of primary cooling system in the housing unit. In the assumptions heat pumps (both ducted and non ducted) are assumed to serve for both heating and cooling. In the RECS2020 survey that cooling and heating technologies are based on, it was recently discoved that some samples reported None for heating, but heat pump for cooling (especialy non-ducted heat pumps). This is especially prevalent in hot climates with low cooling saturation. In ResStock, those samples with None heating and non ducted heat pump cooling in the survey are currently not being counted as having heat pumps. This is a known issue that will be addressed in a future release. In Hawaii, where this issue is most prevalent, the Room AC saturation has been increased to account for the undercounting of non-ducted heat pumps.

#### Distribution Data Source(s)

- The sample counts and sample weights are constructed using U.S. EIA 2020 RECS microdata

- Efficiency data based on ENERGY STAR shipment and Home Energy Saver data combined with age of equipment data from RECS 2020.

#### Direct Conditional Dependencies

- HVAC Cooling Type

- HVAC Has Shared System

- Vintage.

#### Options

ResStock includes four options for central air conditioners and four options for room air conditioners (Table “HVAC Cooling Efficiency options and arguments that vary for each option”). If a building has a heat pump, it is assumed that the heat pump is serving both the heating and cooling load. Buildings with heat pumps assigned in the HVAC Heating input files are flagged, but no ResStock arguments are passed to those building based on this file. Similarly, homes with a shared cooling system for the building are flagged, but the ResStock arguments for that system are assigned in the HVAC Shared Systems Efficiencies characteristic.

Across options with ResStock arguments, many are the same and set to *auto*:

- `cooling_system_cooling_compressor_type`

- `cooling_system_cooling_sensible_heat_fraction`

- `cooling_system_cooling_capacity`

- `cooling_system_cooling_autosizing_limit`

- `cooling_system_crankcase_heater_watts`

- `cooling_system_integrated_heating_system_fuel`

- `cooling_system_integrated_heating_system_efficiency_percent`

- `cooling_system_integrated_heating_system_capacity`

- `cooling_system_integrated_heating_system_fraction_heat_load_served`.

Additionally, `cooling_system_is_ducted` is set to false since ducts are defined in separate input files, and mini-split heat pumps will not be assigned ducts.

<div id="table:hc_opt_hvac_cool_eff" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `cooling_system_type` | `cooling_system_cooling_efficiency_type` | `cooling_system_cooling_efficiency` |
|:---|:---|:---|:---|
| AC, SEER 8 | central air conditioner | SEER | 8 |
| AC, SEER 10 | central air conditioner | SEER | 10 |
| AC, SEER 13 | central air conditioner | SEER | 13 |
| AC, SEER 15 | central air conditioner | SEER | 15 |
| Ducted Heat Pump | none | SEER | 0 |
| Non-Ducted Heat Pump | none | SEER | 0 |
| None | none | SEER | 0 |
| Room AC, EER 8.5 | room air conditioner | EER | 8.5 |
| Room AC, EER 9.8 | room air conditioner | EER | 9.8 |
| Room AC, EER 10.7 | room air conditioner | EER | 10.7 |
| Room AC, EER 12.0 | room air conditioner | EER | 12 |
| Shared Cooling |  |  |  |

HVAC Cooling Efficiency options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC Cooling Efficiency characteristic”. See the OpenStudio-HPXML [Cooling Systems](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-cooling-systems) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_cool_eff" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `cooling_system_type` | true |  | Choice | none, central air conditioner, room air conditioner, evaporative cooler, mini-split, packaged terminal air conditioner | The type of cooling system. Use 'none' if there is no cooling system or if there is a heat pump serving a cooling load. |
| `cooling_system_cooling_efficiency_type` | true |  | Choice | SEER, SEER2, EER, CEER | The efficiency type of the cooling system. System types central air conditioner and mini-split use SEER or SEER2. System types room air conditioner and packaged terminal air conditioner use EER or CEER. Ignored for system type evaporative cooler. |
| `cooling_system_cooling_efficiency` | true |  | Double |  | The rated efficiency value of the cooling system. Ignored for evaporative cooler. |
| `cooling_system_cooling_compressor_type` | false |  | Choice | auto, single stage, two stage, variable speed | The compressor type of the cooling system. Only applies to central air conditioner and mini-split. |
| `cooling_system_cooling_sensible_heat_fraction` | false | Frac | Double | auto | The sensible heat fraction of the cooling system. Ignored for evaporative cooler. |
| `cooling_system_cooling_autosizing_limit` | false | Btu/hr | Double |  | The maximum capacity limit applied to the auto-sizing methodology. If not provided, no limit is used. |
| `cooling_system_is_ducted` | false |  | Boolean | auto, true, false | Whether the cooling system is ducted or not. Only used for mini-split and evaporative cooler. It’s assumed that central air conditioner is ducted, and room air conditioner and packaged terminal air conditioner are not ducted. |
| `cooling_system_crankcase_heater_watts` | false | W | Double | auto | Cooling system crankcase heater power consumption in watts. Applies only to central air conditioner, room air conditioner, packaged terminal air conditioner and mini-split. |
| `cooling_system_integrated_heating_system_fuel` | false |  | Choice | auto, electricity, natural gas, fuel oil, propane, wood, wood pellets, coal | The fuel type of the heating system integrated into cooling system. Only used for packaged terminal air conditioner and room air conditioner. |
| `cooling_system_integrated_heating_system_efficiency_percent` | false | Frac | Double |  | The rated heating efficiency value of the heating system integrated into cooling system. Only used for packaged terminal air conditioner and room air conditioner. |
| `cooling_system_integrated_heating_system_capacity` | false | Btu/hr | Double |  | The output heating capacity of the heating system integrated into cooling system. |
| `cooling_system_integrated_heating_system_fraction_heat_load_served` | false | Frac | Double |  | The heating load served by the heating system integrated into cooling system. Only used for packaged terminal air conditioner and room air conditioner. |

The ResStock argument definitions set in the HVAC Cooling Efficiency characteristic

</div>

#### Distribution Assumption(s)

None

### HVAC Cooling Partial Space Conditioning

#### Description

The fraction of cooling load served by the cooling system. This is approximately equal to the fraction of finished floor area served by the cooling system. Cooling load must be met at every time step for the portion of floor area covered, and does not represent intermittent cooling overtime.

#### Distribution Data Source(s)

- Constructed using U.S. EIA 2009 RECS microdata.

- Hawaii constructed using U.S. EIA 2020 Residential Energy Consumption Survey (RECS) microdata.

#### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004—Sub-CZ Split

- Geometry Building Type RECS

- Geometry Floor Area Bin

- HVAC Cooling Type.

#### Options

Six different levels of percent of floor area cooled are provided, plus an option for homes that have no cooling (Table “HVAC Cooling Partial Space Conditioning options and arguments that vary for each option”).

<div id="table:hc_opt_hvac_cool_par" data-source="3b_ResStockInputs_HVAC.tex">

| Option name       | `cooling_system_fraction_cool_load_served` |
|:------------------|:-------------------------------------------|
| \<10% Conditioned | 0.1                                        |
| 20% Conditioned   | 0.2                                        |
| 40% Conditioned   | 0.4                                        |
| 60% Conditioned   | 0.6                                        |
| 80% Conditioned   | 0.8                                        |
| 100% Conditioned  | 1                                          |
| None              | 0                                          |

HVAC Cooling Partial Space Conditioning options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC Cooling Partial Conditioning characteristic”. See the OpenStudio-HPXML [Cooling-Systems](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-cooling-systems) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_cool_par" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Description |  |
|:---|:---|:---|:---|:---|:---|
| `cooling_system_fraction_cool_load_served` | true | Frac | Double | The cooling load served by the cooling system. |  |

The ResStock argument definitions set in the HVAC Cooling Partial Conditioning characteristic

</div>

#### Distribution Assumption(s)

- Central AC systems need to serve at least 60% of the floor area.

- Heat pumps serve 100% of the floor area because the system serves 100% of the heated floor area, except in Hawaii.

- Due to low sample count, this input is constructed by downscaling a core sub-input file with 3 sub-input files of different dependencies. The sub-input files have the following dependencies:

  - input1 : ‘HVAC Cooling Type’, ‘ASHRAE IECC Climate Zone 2004—Sub-CZ Split’

  - input2 : ‘HVAC Cooling Type’, ‘Geometry Floor Area Bin’

  - input3 : ‘HVAC Cooling Type’, ‘Geometry Building Type RECS’

### HVAC Cooling Autosizing Factor

#### Description

The cooling capacity and airflow scaling factor applied to the auto-sizing methodology. Not currently used in baseline.

#### Distribution Data Source(s)

- N/A.

#### Direct Conditional Dependencies

- HVAC Cooling Efficiency

- HVAC System is Scaled.

#### Options

Since this input file is not currently used, all homes are set to an option of “None.”

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC Cooling Autosizing Factor characteristic”. See the OpenStudio-HPXML [Cooling Systems](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-cooling-systems) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_cool_auto" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Type | Description |
|:---|:---|:---|:---|
| `cooling_system_cooling_autosizing_factor` | false | Double | The capacity scaling factor applied to the auto-sizing methodology. If not provided, 1.0 is used. |
| `heat_pump_cooling_autosizing_factor` | false | Double | The capacity scaling factor applied to the auto-sizing methodology. If not provided, 1.0 is used. |

The ResStock argument definitions set in the HVAC Cooling Autosizing Factor characteristic

</div>

#### Distribution Assumption(s)

HVAC sizing follows ACCA Manual J and Manual S. There is no additional oversizing or undersizing the capacity and airflow of the HVAC system.

