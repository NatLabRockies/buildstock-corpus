<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3b_ResStockInputs_HVAC.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3b_ResStockInputs_HVAC.md | section: Ducts | lines: 1697-1901 -->
## Ducts

### Modeling Approach

ResStock assigns three characteristics related to air distribution ductwork for each housing unit: whether there are ducts present, where the ducts are located, and a combined characteristic that includes the level of duct insulation and the amount of leakage from the ducts to unconditioned space. The location of the ductwork depends on the building type, the foundation type, the attic type, and presence of an attached garage, and if the housing unit has ducts. This is a direct map for each space combination. Air leakage and heat gains and losses are calculated for the fraction of the ductwork outside conditioned space. OpenStudio-HPXML assigns the fraction of the duct area in the conditioned space. Currently, in single-family homes, if the number of floors above grade is one, 100% of the duct surface area is outside the conditioned space. If the number of floors above grade is greater than one, then 75% of the duct surface area is outside the conditioned space. OpenStudio-HPXML also assigns fractions of supply/return ducts with a rectangular and circular cross-section, which affects the effective R-value for a given nominal duct insulation R-value.

ResStock has three inputs that control specify the primary ductwork arguments in the model:

- HVAC Has Ducts

- Duct Location

- Duct Leakage and Insulation.

### HVAC Has Ducts

#### Description

The presence of ducts in the housing unit.

#### Distribution Data Source(s)

- The sample counts and sample weights are constructed using RECS 2020 microdata.

#### Direct Conditional Dependencies

- HVAC Cooling Type

- HVAC Has Shared System

- HVAC Heating Type

- HVAC Secondary Heating Type.

#### Options

Two options are available for this input characteristic: yes or no. The presence of ductwork is dependent upon the heating and cooling systems. Both duct options set the `hvac_blower_fan_watts_per_cfm` argument to auto.

For the argument definitions, see Table “The ResStock argument definitions set in the HVAC Has Ducts characteristic”. See the OpenStudio-HPXML [Air Distribution](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#air-distribution) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_hvac_has_duct" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `hvac_blower_fan_watts_per_cfm` | false | W/CFM | Double | auto | The blower fan efficiency at maximum fan speed. Applies only to split (not packaged) systems (i.e., applies to ducted systems as well as ductless mini-split systems). |

The ResStock argument definitions set in the HVAC Has Ducts characteristic

</div>

#### Distribution Assumption(s)

- Ducted Heat Pump HVAC type assumed to have ducts.

- Non-Ducted Heat Pump HVAC type assumed to have no ducts.

- There could be homes with non-ducted heat pump having ducts (Central AC with non-ducted heat pump), but due to structure of ResStock we are not accounting for those homes.

- None of the shared system options currently modeled (in HVAC Shared Efficiencies) are ducted, therefore where there are discrepancies between HVAC Heating Type, HVAC Cooling Type, and HVAC Has Shared System, HVAC Has Shared System takes precedence (e.g., Central AC + Ducted Heating + Shared Heating and Cooling = No (Ducts)). (This is a temporary fix and will change when ducted shared system options are introduced.)

### Duct Leakage and Insulation

#### Description

Duct insulation and leakage to outside for the portion of ducts in unconditioned spaces.

#### Distribution Data Source(s)

- Duct insulation as a function of location: IECC 2009

- Leakage distribution: Lucas and Cole ([2009](https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-18545.pdf)). *Impacts of the 2009 IECC for Residential Buildings at State Level*.

#### Direct Conditional Dependencies

- Duct location

- Vintage.

#### Options

ResStock uses 13 combinations of insulation and air leakage from ducts (Table “Duct Leakage and Insulation options and arguments that vary for each option”). The following ResStock arguments are constant across all options:

- `ducts_leakage_units`: percent

- `ducts_supply_buried_insulation_level`: auto

- `ducts_supply_fraction_rectangular`: auto

- `ducts_return_buried_insulation_level`: auto

- `ducts_return_fraction_rectangular`: auto.

<div id="table:hc_opt_duct_leak" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `ducts_supply_leakage_to_outside_value` | `ducts_supply_insulation_r` | `ducts_return_leakage_to_outside_value` | `ducts_return_insulation_r` |
|:---|:---|:---|:---|:---|
| 0% Leakage to Outside, Uninsulated | 0 | 0 | 0 | 0 |
| 10% Leakage to Outside, R-4 | 0.067 | 4 | 0.033 | 4 |
| 10% Leakage to Outside, R-6 | 0.067 | 6 | 0.033 | 6 |
| 10% Leakage to Outside, R-8 | 0.067 | 8 | 0.033 | 8 |
| 10% Leakage to Outside, Uninsulated | 0.067 | 0 | 0.033 | 0 |
| 20% Leakage to Outside, R-4 | 0.133 | 4 | 0.067 | 4 |
| 20% Leakage to Outside, R-6 | 0.133 | 6 | 0.067 | 6 |
| 20% Leakage to Outside, R-8 | 0.133 | 8 | 0.067 | 8 |
| 20% Leakage to Outside, Uninsulated | 0.133 | 0 | 0.067 | 0 |
| 30% Leakage to Outside, R-4 | 0.200 | 4 | 0.100 | 4 |
| 30% Leakage to Outside, R-6 | 0.200 | 6 | 0.100 | 6 |
| 30% Leakage to Outside, R-8 | 0.200 | 8 | 0.100 | 8 |
| 30% Leakage to Outside, Uninsulated | 0.200 | 0 | 0.100 | 0 |
| None | 0 | 0 | 0 | 0 |

Duct Leakage and Insulation options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Duct Leakage and Insulation characteristic”. See the OpenStudio-HPXML [Air Distribution](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#air-distribution) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_duct_leak" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `ducts_leakage_units` | true |  | Choice | CFM25, CFM50, Percent | The leakage units of the ducts. |
| `ducts_supply_leakage_to_outside_value` | true |  | Double |  | The leakage value to outside for the supply ducts. |
| `ducts_supply_insulation_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | The nominal insulation r-value of the supply ducts excluding air films. Use 0 for uninsulated ducts. |
| `ducts_supply_buried_insulation_level` | false |  | Choice | auto, not buried, partially buried, fully buried, deeply buried | Whether the supply ducts are buried in, e.g., attic loose-fill insulation. Partially buried ducts have insulation that does not cover the top of the ducts. Fully buried ducts have insulation that just covers the top of the ducts. Deeply buried ducts have insulation that continues above the top of the ducts. |
| `ducts_supply_fraction_rectangular` | false | frac | Double | auto | The fraction of supply ducts that are rectangular (as opposed to round); this affects the duct effective R-value used for modeling. |
| `ducts_return_leakage_to_outside_value` | true |  | Double |  | The leakage value to outside for the return ducts. |
| `ducts_return_insulation_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | The nominal insulation r-value of the return ducts excluding air films. Use 0 for uninsulated ducts. |
| `ducts_return_buried_insulation_level` | false |  | Choice | auto, not buried, partially buried, fully buried, deeply buried | Whether the return ducts are buried in, e.g., attic loose-fill insulation. Partially buried ducts have insulation that does not cover the top of the ducts. Fully buried ducts have insulation that just covers the top of the ducts. Deeply buried ducts have insulation that continues above the top of the ducts. |
| `ducts_return_fraction_rectangular` | false | frac | Double | auto | The fraction of return ducts that are rectangular (as opposed to round); this affects the duct effective R-value used for modeling. |

The ResStock argument definitions set in the Duct Leakage and Insulation characteristic

</div>

#### Distribution Assumption(s)

Ducts entirely in conditioned spaces will not have any leakage to outside. Ducts with R-4/R-8 insulation were previously assigned to Geometry Foundation Type = Ambient or Slab. They now correspond to those with Duct Location = Garage, Unvented Attic, or Vented Attic.

### Duct Location

#### Description

Primary location of duct system. As described earlier, a fraction of the ducts will also be assumed to be in conditioned space for homes with multiple stories.

#### Distribution Data Source(s)

- OpenStudio-HPXML v1.6.0 and Building America House Simulation Protocols ((E. Wilson et al. 2014a)).

#### Direct Conditional Dependencies

- Geometry Space Combination

- HVAC Has Ducts.

#### Options

The duct location is a direct mapping of spaces from the hierarchical assignment in OpenStudio-HPXML. This is done to expose the duct location as an output in ResStock. The spaces available for the ducts are in Table “Duct Location options and arguments that vary for each option”. The “None” option is used for ducts that are located completely in the conditioned space. For all options of Duct Location, the following arguments are the same:

- `ducts_supply_surface_area`: auto

- `ducts_supply_surface_area_fraction`: auto

- `ducts_return_surface_area`: auto

- `ducts_return_surface_area_fraction`: auto.

<div id="table:hc_opt_duct_loc" data-source="3b_ResStockInputs_HVAC.tex">

| Option name | `ducts_supply_location` | `ducts_return_location` | `ducts_number_of_return_registers` |
|:---|:---|:---|:---|
| Attic | attic | attic | auto |
| Crawlspace | crawlspace | crawlspace | auto |
| Garage | garage | garage | auto |
| Heated Basement | basement—conditioned | basement—conditioned | auto |
| Living Space | conditioned space | conditioned space | auto |
| Unheated Basement | basement—unconditioned | basement—unconditioned | auto |
| None | conditioned space | conditioned space | 0 |

Duct Location options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Duct Location characteristic”. See the OpenStudio-HPXML [Air Distribution](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-air-distribtuion) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_duct_loc" data-source="3b_ResStockInputs_HVAC.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `ducts_supply_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, crawlspace, crawlspace—vented, crawlspace—unvented, crawlspace—conditioned, attic, attic—vented, attic—unvented, garage, exterior wall, under slab, roof deck, outside, other housing unit, other heated space, other multifamily buffer space, other non-freezing space, manufactured home belly | The location of the supply ducts. |
| `ducts_supply_surface_area` | false | ft<sup>2</sup> | Double | auto | The supply ducts surface area in the given location. |
| `ducts_supply_surface_area_fraction` | false | frac | Double | auto | The fraction of supply ducts surface area in the given location. Only used if Surface Area is not provided. If the fraction is less than 1, the remaining duct area is assumed to be in conditioned space. |
| `ducts_return_location` | false |  | Choice | auto, conditioned space, basement—conditioned, basement—unconditioned, crawlspace, crawlspace—vented, crawlspace—unvented, crawlspace—conditioned, attic, attic—vented, attic—unvented, garage, exterior wall, under slab, roof deck, outside, other housing unit, other heated space, other multifamily buffer space, other non-freezing space, manufactured home belly | The location of the return ducts. |
| `ducts_return_surface_area` | false | ft<sup>2</sup> | Double | auto | The return ducts surface area in the given location. |
| `ducts_return_surface_area_fraction` | false | frac | Double | auto | The fraction of return ducts surface area in the given location. Only used if Surface Area is not provided. If the fraction is less than 1, the remaining duct area is assumed to be in conditioned space. |
| `ducts_number_of_return_registers` | false | \# | Integer | auto | The number of return registers of the ducts. Only used to calculate default return duct surface area. |

The ResStock argument definitions set in the Duct Location characteristic

</div>

#### Distribution Assumption(s)

Based on default duct location assignment in OpenStudio-HPXML: the first present space type in the order of: basement—conditioned, basement—unconditioned, crawlspace—conditioned, crawlspace—vented, crawlspace—unvented, attic—vented, attic—unvented, garage, or living space.

