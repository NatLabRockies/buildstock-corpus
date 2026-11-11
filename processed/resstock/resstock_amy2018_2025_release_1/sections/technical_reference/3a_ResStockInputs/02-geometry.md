<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3a_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3a_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3a_ResStockInputs.md | section: Geometry | lines: 840-2071 -->
## Geometry

In this section, we discuss the inputs that control the actual geometry of the building energy model used for simulation of each sample. We discuss the geometry parameters in five categories: housing unit location, building type, construction year, housing unit geometry, and space geometry.

### Housing Unit Location

There are two reference frames for locating the housing units modeled in ResStock: (1) the building frame of reference and (2) the polar reference frame. The building frame defines the front, back, top, bottom, left, and right sides of the unit. The polar reference frame defines the orientation of the unit’s front door with respect to the cardinal directions north, south, east, and west.

In ResStock, housing units are modeled as single zones, regardless if they are in larger buildings. To do this, adiabatic walls are assigned/modeled for walls, ceilings, or floors shared between the modeled housing unit, an adjacent unit, and a corridor.

The units are shaded by how near other buildings are to the modeled unit. OpenStudio-HPXML can model shading with exterior corridors for multifamily units, but ResStock does not use these capabilities for multifamily or single-family attached units.

The height above grade for the unit is based on the the number of floors the average ceiling height and the unit level (top floor, middle floors, or bottom floor). The height above grade largely impacts the importance of wind driven infiltration. For bottom units the above grade height is 0 ft. For middle units, the average height of all middle units is used. For top units, the height of the top floor.

There are 12 input files controlling building siting in ResStock:

- Orientation

- Geometry Stories

- Geometry Stories Bin

- Geometry Building Type Height

- Geometry Stories Low Rise

- Geometry Building Number Units MF

- Geometry Building Number Units SFA

- Geometry Building Level MF

- Geometry Building Horizontal Location MF

- Geometry Building Horizontal Location SFA

- Neighbors

- Corridor.

#### Orientation

##### Description

Orientation of the front of the housing unit as it faces the street. The front door is assumed to face the street.

##### Distribution Data Source(s)

- OpenStreetMap data queried by Radiant Labs.

##### Direct Conditional Dependencies

No direct conditional dependencies.

##### Options

The options for the Orientation characteristic are east, west, northeast, southwest, north, south, northwest, and southeast. The options set the `geometry_unit_orientation` ResStock argument; see Table “Orientation options and arguments that vary for each option”. The argument definition can be found in Table “The ResStock argument definitions set in the Orientation characteristic”.

<div id="table:hc_opt_orient" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_unit_orientation` |
|:------------|:-----------------|:----------------------------|
| East        | 17%              | 90                          |
| West        | 17%              | 270                         |
| Northeast   | 7.2%             | 45                          |
| Southwest   | 7.2%             | 225                         |
| North       | 18%              | 0                           |
| South       | 18%              | 180                         |
| Northwest   | 7.7%             | 315                         |
| Southeast   | 7.7%             | 135                         |

Orientation options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Geometry Stories characteristics”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_oient" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `geometry_unit_orientation` | true | degrees | Double | The unit’s orientation is measured clockwise from north (e.g., North=0, East=90, South=180, West=270). |

The ResStock argument definitions set in the Orientation characteristic

</div>

##### Distribution Assumption(s)

No assumptions were made. The distribution was taken directly from the Radiant Labs query.

#### Geometry Stories

##### Description

The number of stories in the building in which the housing unit is located.

##### Distribution Data Source(s)

- U.S. EIA 2009 RECS microdata.

##### Direct Conditional Dependencies

- Geometry Building Type ACS

- Geometry Floor Area Bin.

##### Options

The options for Geometry stories are a set of integers between 1 and 35; see Table “Geometry Stories options and arguments that vary for each option”. The stories of a building refer to the number of floors above grade. The number of stories does not include basements but would include finished attics. The `geometry_num_floors_above_grade` argument definition is in Table “Argument definitions for the Geometry Stories characteristics”.

<div id="table:hc_opt_geom_stories" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_num_floors_above_grade` |
|:------------|:-----------------|:----------------------------------|
| 1           | 49%              | 1                                 |
| 2           | 37%              | 2                                 |
| 3           | 8%               | 3                                 |
| 4           | 2%               | 4                                 |
| 5           | 0.79%            | 5                                 |
| 6           | 0.7%             | 6                                 |
| 7           | 0.16%            | 7                                 |
| 8           | 0.16%            | 8                                 |
| 9           | 0.13%            | 9                                 |
| 10          | 0.17%            | 10                                |
| 11          | 0.09%            | 11                                |
| 12          | 0.19%            | 12                                |
| 13          | 0.12%            | 13                                |
| 14          | 0.11%            | 14                                |
| 15          | 0.12%            | 15                                |
| 20          | 0.21%            | 20                                |
| 21          | 0.66%            | 21                                |
| 35          | 0.11%            | 35                                |

Geometry Stories options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Geometry Stories characteristics”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_geom_stories" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `geometry_num_floors_above_grade` | true | \# | Integer | The number of floors above grade (in the unit if single-family detached or single-family attached, and in the building if apartment unit). Conditioned attics are included. |

Argument definitions for the Geometry Stories characteristics

</div>

##### Distribution Assumption(s)

- All mobile homes are 1 story.

- Single-Family Detached and Single-Family Attached use the STORIES field in RECS, whereas Multifamily with 5+ units uses the NUMFLRS field.

- Building types 2 Unit and 3 or 4 Unit use the stories distribution of Multifamily 5 to 9 Unit (capped at 4 stories) because RECS does not report stories or floors for multifamily with 2-4 units.

- The dependency on floor area bins is removed for multifamily with 5+ units.

- Vintage ACS rows for the 2010s are copied from the 2000-09 rows.

#### Geometry Story Bin

##### Description

Tags the building in which the housing unit is located as having more than 8 stories or less than 8 stories.

##### Distribution Data Source(s)

- U.S. EIA 2009 RECS microdata.

##### Direct Conditional Dependencies

- Geometry Stories.

##### Options

The options are either \<8 stories or 8+ stories. This characteristic is an aggregation of the Geometry stories characteristic to identify units in high-rise buildings. No arguments are assigned based on this housing characteristic, but it is used as a dependency for other input files.

| Option name | Stock saturation |
|:------------|:-----------------|
| \<8         | 98%              |
| 8+          | 2.1%             |

Options and saturation for the Geometry Story Bin

##### Distribution Assumption(s)

- The probability values are a direct mapping of the Geometry Stories characteristic.

#### Geometry Building Type Height

##### Description

The 2009 U.S. EIA RECS building type with multifamily buildings split out by low-rise, mid-rise, and high-rise.

##### Distribution Data Source(s)

- The assignment of building type and height are assigned based on the building type and the number of stories.

##### Direct Conditional Dependencies

- Geometry Building Type RECS

- Geometry Stories.

##### Options

The options break up the Geometry Building Type RECS multi-family 5+ unit buildings into low-rise (1-3 stories), mid-rise (4-7 stories), and high-rise (8+ stories). No arguments are directly assigned based on the options in this input file.

| Option name                             | Stock saturation |
|:----------------------------------------|:-----------------|
| Mobile Home                             | 6.2%             |
| Multi-Family with 2-4 Units             | 8%               |
| Multi-Family with 5+ Units, 1-3 Stories | 13%              |
| Multi-Family with 5+ Units, 4-7 Stories | 3.4%             |
| Multi-Family with 5+ Units, 8+ Stories  | 2.1%             |
| Single-Family Attached                  | 5.9%             |
| Single-Family Detached                  | 61%              |

Options and saturation for Geometry Building Type Height

##### Distribution Assumption(s)

No assumptions are made.

#### Geometry Stories Low Rise

##### Description

Number of building stories for low-rise buildings.

##### Distribution Data Source(s)

- The assignment of building type and height are assigned based on the number of stories.

##### Direct Conditional Dependencies

- Geometry Stories.

##### Options

The options are a categorization of the Geometry Stories characteristic for low-rise buildings (1 story, 2 stories, 3 stories, 4+ stories).

##### Distribution Assumption(s)

None.

#### Geometry Building Number Units MF

##### Description

The number of housing units in the multifamily building.

##### Distribution Data Source(s)

- U.S. EIA 2009 RECS microdata.

##### Direct Conditional Dependencies

- Geometry Building Type ACS

- Geometry Stories.

##### Options

The options for the Geometry Building Level MF characteristic are a set of integers between 2 and 326; see Table “Geometry Building Level Number of Units MF options and arguments that vary for each option”. The “None” option is used for all building types other than multifamily. The options set the `geometry_building_num_units` ResStock argument; see Table “Argument definitions for the Geometry Building Number of Units MF characteristic”.

<div id="table:hc_opt_geom_build_units_mf" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_building_num_units` |
|:------------|:-----------------|:------------------------------|
| 2           | 3.6%             | 2                             |
| 3           | 1.4%             | 3                             |
| 4           | 3%               | 4                             |
| 5           | 0.54%            | 5                             |
| 6           | 1.5%             | 6                             |
| 7           | 0.26%            | 7                             |
| 8           | 2.3%             | 8                             |
| 9           | 0.15%            | 9                             |
| 10          | 0.95%            | 10                            |
| 11          | 0.098%           | 11                            |
| 12          | 1.9%             | 12                            |
| 13          | 0.15%            | 13                            |
| 14          | 0.18%            | 14                            |
| 15          | 0.27%            | 15                            |
| 16          | 0.61%            | 16                            |
| 17          | 0.023%           | 17                            |
| 18          | 0.22%            | 18                            |
| 19          | 0.016%           | 19                            |
| 20          | 0.75%            | 20                            |
| 24          | 0.96%            | 24                            |
| 30          | 0.81%            | 30                            |
| 36          | 0.48%            | 36                            |
| 43          | 0.67%            | 43                            |
| 67          | 2.7%             | 67                            |
| 116         | 1.2%             | 116                           |
| 183         | 0.62%            | 183                           |
| 326         | 1%               | 326                           |
| None        | 74%              |                               |

Geometry Building Level Number of Units MF options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Geometry Building Number of Units MF characteristic”. See the OpenStudio-HPXML [Whole-SFA-MF-Buildings](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#whole-sfa-mf-buildings) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_geom_build_units_mf" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `geometry_building_num_units` | false | \# | Integer | The number of units in the building. Required for single-family attached and apartment units. |

Argument definitions for the Geometry Building Number of Units MF characteristic

</div>

##### Distribution Assumption(s)

- Uses NUMAPTS (number of apartments) field in EIA RECS 2009

- EIA RECS 2009 does not report NUMAPTS for Multifamily 2-4 units, so assumptions are made based on the number of stories

- Data were sampled from the following bins of Geometry Stories: 1, 2, 3, 4-7, 8+.

#### Geometry Building Number Units Single-Family Attached

##### Description

The number of housing units in the single-family attached (SFA) building.

##### Distribution Data Source(s)

- U.S. EIA 2009 RECS microdata.

##### Direct Conditional Dependencies

- Geometry Building Type ACS.

##### Options

The options for the Geometry Building Level SFA characteristic are a set of integers between 2 and 144; see Table “Geometry Building Level Number of Units SFA options and arguments that vary for each option”. The “None” option is used for all building types other than SFA.

<div id="table:hc_opt_geom_build_units_sfa" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_building_num_units` |
|:------------|:-----------------|:------------------------------|
| None        | 94%              |                               |
| 2           | 0%               | 2                             |
| 3           | 0%               | 3                             |
| 4           | 0%               | 4                             |
| 5           | 0.72%            | 5                             |
| 6           | 0.78%            | 6                             |
| 7           | 0.36%            | 7                             |
| 8           | 1.1%             | 8                             |
| 9           | 0%               | 9                             |
| 10          | 0.38%            | 10                            |
| 12          | 0.57%            | 12                            |
| 15          | 0.14%            | 15                            |
| 16          | 0.33%            | 16                            |
| 20          | 0.27%            | 20                            |
| 24          | 0.27%            | 24                            |
| 30          | 0.27%            | 30                            |
| 36          | 0.27%            | 36                            |
| 50          | 0.13%            | 50                            |
| 60          | 0.1%             | 60                            |
| 90          | 0.086%           | 90                            |
| 144         | 0.11%            | 144                           |

Geometry Building Level Number of Units SFA options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Geometry Building Number of Units MF characteristic”. See the OpenStudio-HPXML [Whole-SFA-MF-Buildings](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#whole-sfa-mf-buildings) documentation for the available HPXML schema elements, default values, and constraints.

##### Distribution Assumption(s)

No assumptions were made.

#### Geometry Building Level Multifamily

##### Description

Location of the multifamily (MF) unit vertically within the building (bottom, middle, top).

##### Distribution Data Source(s)

- Calculated directly from the Geometry Building Type RECS and Geometry Stories characteristics.

##### Direct Conditional Dependencies

- Geometry Building Type RECS

- Geometry Stories.

##### Options

The options for the Geometry Building Level MF characteristic are Bottom, Middle, None, and Top; see Table “Geometry Building Level MF options and arguments that vary for each option”. The None option is used for all building types other than MF. The characteristic sets the `geometry_unit_level` ResStock argument; see Table “Argument definitions for the Geometry Building Level MF characteristic”.

<div id="table:hc_opt_geom_build_lev_mf" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_unit_level` |
|:------------|:-----------------|:----------------------|
| Bottom      | 11%              | Bottom                |
| Middle      | 6.1%             | Middle                |
| Top         | 8.9%             | Top                   |
| None        | 74%              |                       |

Geometry Building Level MF options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Geometry Building Level MF characteristic”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_build_lev_mf" data-source="3a_ResStockInputs.tex">

| Name | Required | Type | Choices | Description |
|:---|:---|:---|:---|:---|
| `geometry_unit_level` | false | Choice | Bottom, Middle, Top | The level of the unit. This is required for apartment units. |

Argument definitions for the Geometry Building Level MF characteristic

</div>

##### Distribution Assumption(s)

- Calculated using the number of stories, where buildings greater than or equal to 2 stories have Top and Bottom probabilities = 1/Geometry Stories, and Middle probabilities = 1-2/Geometry stories.

#### Geometry Building Horizontal Location Multifamily

##### Description

Location of the multifamily unit horizontally within the building (left, middle, right).

##### Distribution Data Source(s)

- Calculated directly from the Geometry Number of Units MF and Geometry Stories characteristics.

##### Direct Conditional Dependencies

- Geometry Number of Units MF

- Geometry Stories.

##### Options

The options of the Geometry Building Horizontal Location MF characteristic are None, Left, Middle, Right, and Not Applicable. The characteristic sets the `geometry_unit_horizontal_location` ResStock argument; see Table “Geometry Building Horizontal Location Multifamily options and arguments that vary for each option”. The “Not Applicable” option is used for a pair of number of units and stories that cannot be sampled. For example, a 9-story, 2-unit multifamily building is unlikely to exist in reality and cannot be modeled in ResStock. ResStock does not model units in buildings with more stories than units. All building types other than multifamily receive the “None” option. For the argument definitions, see Table “Argument definitions for the Geometry Building Horizontal Location MF and Geometry Building Horizontal Location SFA characteristics”.

<div id="table:hc_opt_geom_build_hor_loc_mf" data-source="3a_ResStockInputs.tex">

| Option name    | Stock saturation | `geometry_unit_horizontal_location` |
|:---------------|:-----------------|:------------------------------------|
| Left           | 7.1%             | Left                                |
| Middle         | 8%               | Middle                              |
| Right          | 7.1%             | Right                               |
| Not Applicable | 4.2%             | None                                |
| None           | 74%              |                                     |

Geometry Building Horizontal Location Multifamily options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Geometry Building Horizontal Location MF and Geometry Building Horizontal Location SFA characteristics”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_geom_build_hor_loc_mf" data-source="3a_ResStockInputs.tex">

| Name | Required | Type | Choices | Description |
|:---|:---|:---|:---|:---|
| `geometry_unit_horizontal_location` | false | Choice | None, Left, Middle, Right | The horizontal location of the unit when viewing the front of the building. This is required for single-family attached and apartment units. |

Argument definitions for the Geometry Building Horizontal Location MF and Geometry Building Horizontal Location SFA characteristics

</div>

##### Distribution Assumption(s)

- All probabilities are calculated assuming the building has double-loaded corridors (with some exceptions like 3 units in a single-story building).

#### Geometry Building Horizontal Location Single-Family Attached

##### Description

Location of the SFA unit horizontally within the building (left, middle, right).

##### Distribution Data Source(s)

- Calculated directly from the Geometry Number of Units SFA and Geometry Stories characteristics.

##### Direct Conditional Dependencies

- Geometry Number of Units SFA

- Geometry Stories.

##### Options

The options of the Geometry Building Horizontal Location SFA characteristic are None, Left, Middle, and Right. The characteristic sets the `geometry_unit_horizontal_location` ResStock argument; see Table “Geometry Building Horizontal Location SFA options and arguments that vary for each option”. All non-single-family-attached building types receive the “None” option. For the argument definitions, see Table “Argument definitions for the Geometry Building Horizontal Location MF and Geometry Building Horizontal Location SFA characteristics”.

<div id="table:hc_opt_geom_build_hor_loc_sfa" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_unit_horizontal_location` |
|:------------|:-----------------|:------------------------------------|
| Left        | 0.63%            | Left                                |
| Middle      | 4.6%             | Middle                              |
| Right       | 0.63%            | Right                               |
| None        | 94%              |                                     |

Geometry Building Horizontal Location SFA options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Geometry Building Horizontal Location MF and Geometry Building Horizontal Location SFA characteristics”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) documentation for the available HPXML schema elements, default values, and constraints.

##### Distribution Assumption(s)

- All probabilities are calculated from the direct conditional dependencies.

#### Neighbors

##### Description

Presence and distance between the housing unit and the nearest neighbors to the left and right.

##### Distribution Data Source(s)

- OpenStreetMap data queried by Radiant Labs for Multifamily and Single-Family Attached

- Engineering judgment for others.

##### Direct Conditional Dependencies

- Geometry Building Type RECS.

##### Options

The options for Neighbors are Left/Right at 15 ft, 2, 4, 7, 12, 27, and None. The option values correspond to distances in feet to the nearest neighbor on the left and right sides of the building. The options set ResStock arguments corresponding to the distance and height a shading object. The `neighbor_front_height`, `neighbor_back_height`, `neighbor_left_height` and `neighbor_right_height` arguments are all set to “auto,” which sets the shading object height to the total height of the housing unit. The other arguments assign the distance from the housing unit. The `neighbor_front_distance` and `neighbor_back_distance` arguments are set to 0 (meaning there are no neighbors to the front and back of the unit). The left and right distances are set by Table “Neighbors options and arguments that vary for each option”. The None option sets distances to 0 (meaning there are no neighbors). The argument definitions can be seen in Table “The ResStock argument definitions set in the Neighbors characteristic”.

<div id="table:hc_opt_neighbor" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `neighbor_left_distance` | `neighbor_right_distance` |
|:---|:---|:---|:---|
| Left/Right at 15ft | 68% | 15 | 15 |
| 2 | 0.19% | 2 | 2 |
| 4 | 3.4% | 4 | 4 |
| 7 | 5% | 7 | 7 |
| 12 | 9.2% | 12 | 12 |
| 27 | 13% | 27 | 27 |
| None | 1.3% | 0 | 0 |

Neighbors options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Neighbors characteristic”. See the OpenStudio-HPXML documentation section [Neighbor Buildings](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-neighbor-buildings) for the available elements, default values, and constraints.

<div id="table:hc_arg_def_neighbors" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `neighbor_front_distance` | true | ft | Double |  | The distance between the unit and the neighboring building to the front (not including eaves). A value of zero indicates no neighbors. Used for shading. |
| `neighbor_back_distance` | true | ft | Double |  | The distance between the unit and the neighboring building to the back (not including eaves). A value of zero indicates no neighbors. Used for shading. |
| `neighbor_left_distance` | true | ft | Double |  | The distance between the unit and the neighboring building to the left (not including eaves). A value of zero indicates no neighbors. Used for shading. |
| `neighbor_right_distance` | true | ft | Double |  | The distance between the unit and the neighboring building to the right (not including eaves). A value of zero indicates no neighbors. Used for shading. |
| `neighbor_front_height` | false | ft | Double | auto | The height of the neighboring building to the front. |
| `neighbor_back_height` | false | ft | Double | auto | The height of the neighboring building to the back. |
| `neighbor_left_height` | false | ft | Double | auto | The height of the neighboring building to the left. |
| `neighbor_right_height` | false | ft | Double | auto | The height of the neighboring building to the right. |

The ResStock argument definitions set in the Neighbors characteristic

</div>

##### Distribution Assumption(s)

None

#### Corridor

##### Description

Type of corridor attached to multifamily units.

##### Modeling Approach

Single-family attached and multifamily buildings can have corridors, which are passageways between units. Interior corridors are enclosed and assumed to be conditioned, which are modeled by adiabatic walls being created for the wall of the unit that is adjacent to the corridor. Exterior corridors provide shading, but are not enclosed. The way this is modeled is to add a shading object to the front and/or the back of the unit. ResStock only allows multifamily units to have a double-loaded interior corridor. ResStock does not model energy use (e.g., lighting, plug load, or HVAC) associated with corridors; it only models their impact on the multifamily housing units.

##### Distribution Data Source(s)

- Engineering judgment.

##### Direct Conditional Dependencies

- Geometry Building Type RECS.

##### Options

For Mobile Homes, Single-Family Detached, and Single-Family Attached building types the option assigned is “Not Applicable.” Multifamily units all have a “Double-Loaded Interior” corridor with a width of 10 feet. The Corridor characteristic assigns the `geometry_corridor_position` and the `geometry_corridor_width` arguments. For the options and arguments set for each option, see Table “Corridor options and arguments that vary for each option”. For the argument definitions, see Table “Argument definitions for the Corridor characteristic”.

<div id="table:hc_opt_corridor" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_corridor_position` | `geometry_corridor_width` |
|:---|:---|:---|:---|
| Not Applicable | 74% | None | 0 |
| Double-Loaded Interior | 26% | Double-Loaded Interior | 10 |
| None | 0% | None | 0 |
| Single Exterior Front | 0% | Single Exterior (Front) | 10 |
| Double Exterior | 0% | Double Exterior | 10 |

Corridor options and arguments that vary for each option

</div>

For the argument definitions, see Table “Argument definitions for the Corridor characteristic”. See the OpenStudio-HPXML [Dwelling Units](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#dwelling-units) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_corridor" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_corridor_position` | true |  | Choice | Double-Loaded Interior, Double Exterior, Single Exterior (Front), None | The position of the corridor. Only applies to single-family attached and apartment units. Exterior corridors are shaded, but not enclosed. Interior corridors are enclosed and conditioned. |
| `geometry_corridor_width` | true | ft | Double |  | The width of the corridor. Only applies to apartment units. |

Argument definitions for the Corridor characteristic

</div>

##### Distribution Assumption(s)

- Single-Family Attached units do not have corridors.

- All Multifamily units have a double-loaded interior corridor with a width of 10 ft.

### Building Type

This section discusses the ResStock input files that control tagging and model differentiation of building type. These building types control a lot of assumptions and treatment of variables in the OpenStudio-HPXML workflow. An example is that the plug load energy is based on a regression equation, and the equation coefficients are different between the building types.

There are two input files controlling building type assignment in ResStock:

- Geometry Building Type ACS

- Geometry Building Type RECS.

#### Geometry Building Type ACS

##### Description

The building type classification according to the U.S. Census American Community Survey.

##### Distribution Data Source(s)

- 2019 5-year PUMS from the University of Minnesota.

##### Direct Conditional Dependencies

- PUMA.

##### Options

ACS considers nine building types, which are tagged in ResStock based on PUMA. No arguments are directly assigned based on this input characteristic.

<div id="table:test" data-source="3a_ResStockInputs.tex">

| Option name            | Stock saturation |
|:-----------------------|:-----------------|
|                        |                  |
| 2 Unit                 | 3.6%             |
| 3 or 4 Unit            | 4.4%             |
| 5 to 9 Unit            | 4.7%             |
| 10 to 19 Unit          | 4.5%             |
| 20 to 49 Unit          | 3.7%             |
| 50 or More Unit        | 5.6%             |
| Mobile Home            | 6.2%             |
| Single-Family Attached | 5.9%             |
| Single-Family Detached | 61%              |

Options and saturation for Geometry Building Type ACS

</div>

##### Distribution Assumption(s)

None.

#### Geometry Building Type RECS

##### Description

The building type classification according to the U.S. EIA RECS.

##### Distribution Data Source(s)

- 2019 5-year PUMS from the University of Minnesota.

##### Direct Conditional Dependencies

- Geometry Building Type ACS.

##### Options

The EIA RECS building types are direct aggregations of the ACS building types. Multifamily units are grouped into 2-4 unit buildings and 5+ unit buildings. The options set the `geometry_unit_type`, `geometry_unit_aspect_ratio`, and `geometry_average_ceiling_height` ResStock arguments; see Table “Geometry Building Type RECS options and arguments that vary for each option”. The `geometry_average_ceiling_height` is always set to 8 ft. The argument definitions are in Table “The ResStock argument definitions set in the Geometry Building Type RECS characteristic”.

<div id="table:hc_opt_gbt_recs" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `geometry_unit_type` | `geometry_unit_aspect_ratio` |
|:---|:---|:---|:---|
| Mobile Home | 6.2% | manufactured home | 1.8 |
| Multifamily with 2-4 Units | 8% | apartment unit | 0.5556 |
| Multifamily with 5+ Units | 18% | apartment unit | 0.5556 |
| Single-Family Attached | 5.9% | single-family attached | 0.5556 |
| Single-Family Detached | 61% | single-family detached | 1.8 |

Geometry Building Type RECS options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Geometry Building Type RECS characteristic”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_gbt_recs" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_unit_type` | true |  | Choice | single-family detached, single-family attached, apartment unit, manufactured home | The type of housing unit. Use single-family attached for a housing unit with 1 or more stories, attached units to one or both sides, and no units above/below. Use apartment unit for a housing unit with 1 story, attached units to one, two, or three sides, and units above and/or below. |
| `geometry_unit_aspect_ratio` | true | Frac | Double |  | The ratio of front/back wall length to left/right wall length for the unit, excluding any protruding garage wall area. |
| `geometry_average_ceiling_height` | true | ft | Double |  | Average distance from the floor to the ceiling. |

The ResStock argument definitions set in the Geometry Building Type RECS characteristic

</div>

##### Distribution Assumption(s)

None.

### Construction Year

ResStock captures the change in energy codes over time by relying on survey data (mainly from ACS and EIA RECS) to inform how housing units have adopted energy code vintages and retrofits over time. The approach used in ResStock is to assign a decadal bin when the building was constructed. The decadal bins range from pre-1940s to the 2010s. The Vintage and Vintage ACS characteristics are then used as dependencies to assign probabilities for each Vintage bin. For example, wall insulation being dependent on vintage allows the wall insulation R-value mean to increase over time.

There are two input files controlling building type assignment in ResStock:

- Vintage

- Vintage ACS.

#### Vintage

##### Description

Time period in which the building was originally constructed.

##### Distribution Data Source(s)

- 2019 5-year PUMS from the University of Minnesota.

##### Direct Conditional Dependencies

- Geometry Building Type ACS

- PUMA.

##### Options

The options are decade bins for when the building was constructed: \<1940, 1940s, 1950s, 1960s, 1970s, 1980s, 1990s, 2000s, 2010s. The options set the `year_built` and `vintage` ResStock arguments. The `year_built` argument is always set to “auto.” The `vintage` argument is set to the same value as the option name; see Table “Vintage options and arguments that vary for each option”.

<div id="table:hc_opt_vintage" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation | `vintage` |
|:------------|:-----------------|:----------|
| \<1940      | 13%              | \<1940    |
| 1940s       | 4.9%             | 1940s     |
| 1950s       | 10%              | 1950s     |
| 1960s       | 11%              | 1960s     |
| 1970s       | 15%              | 1970s     |
| 1980s       | 13%              | 1980s     |
| 1990s       | 14%              | 1990s     |
| 2000s       | 14%              | 2000s     |
| 2010s       | 5.1%             | 2010s     |

Vintage options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Vintage characteristic”.

<div id="table:hc_arg_def_vintage" data-source="3a_ResStockInputs.tex">

| Name | Required | Type | Description |
|:---|:---|:---|:---|
| `year_built` | false | Integer | The year the building was built. |
| `vintage` | false | String | The building vintage, used for informational purposes only. |

The ResStock argument definitions set in the Vintage characteristic

</div>

##### Distribution Assumption(s)

- Where sample counts are less than 10 (812 / 21024 rows), the State average distribution has been inserted.

- “Mobile Home” does not exist in the PUMS DC sample and is replaced by “Single-Family Detached.”

#### Vintage ACS

##### Description

Time period in which the housing unit was constructed as defined by the U.S. Census American Community Survey.

##### Distribution Data Source(s)

- 2019 5-year PUMS from the University of Minnesota.

##### Direct Conditional Dependencies

- Vintage.

##### Options

The options for Vintage ACS are the same vintage bins as ACS, “Option and saturation for Vintage ACS”. They are roughly 20-year bins. No arguments are set based on this input file.

<div id="table:hc_vintage_acs" data-source="3a_ResStockInputs.tex">

| Option name | Stock saturation |     |
|:------------|:-----------------|:----|
| \<1940      | 13%              |     |
| 1940-59     | 15%              |     |
| 1960-79     | 26%              |     |
| 1980-99     | 27%              |     |
| 2000-09     | 14%              |     |
| 2010s       | 5.1%             |     |

Option and saturation for Vintage ACS

</div>

##### Distribution Assumption(s)

- The Vintage ACS options are directly mapped from the Vintage characteristic options.

### Housing Unit Geometry

There are seven input files controlling housing unit geometry in ResStock:

- Geometry Building Floor Area

- Geometry Building Floor Area Bin

- Bedrooms

- Geometry Attic Type

- Geometry Foundation Type

- Geometry Garage

- Geometry Space Combination.

#### Geometry Floor Area

##### Description

The conditioned floor area of the housing unit using bins from 2017-2019 American Housing Survey.

##### Distribution Data Source(s)

- 2017 and 2019 American Housing Survey microdata.

##### Direct Conditional Dependencies

- Census Division

- Geometry Building Type RECS

- Income RECS2020

- PUMA Metro Status

- Tenure.

##### Options

The options of Geometry Floor Area characteristic are the American Housing Survey floor area bins. The options set the `geometry_unit_cfa`, `geometry_unit_cfa_bin`, and the `geometry_garage_protrusion` ResStock arguments; see Table “Geometry Floor Area options and arguments that vary for each option”. The `geometry_unit_cfa` argument is always set to “auto.” Because in the ResStockArguments measure “auto” is used for the `geometry_unit_cfa` argument, a representative conditioned floor area is assigned using the `geometry_unit_cfa_bin` argument. The values of the conditioned floor area bin are taken from the 2017 and 2019 American Housing Surveys and split out by housing type. The housing types are single-family detached, single-family attached, apartment, and manufactured homes. Currently, the same conditioned floor area values are used for single-family detached and manufactured homes. For the ResStock argument definition see Table “The ResStock argument definitions set in the Geometry Floor Area characteristic”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) section of the documentation. The floor area is used many places in the OpenStudio-HPXML model workflow.

<div id="table:hc_opt_geom_floor_area" data-source="3a_ResStockInputs.tex">

| Option name | `geometry_garage_protrusion` | `geometry_unit_cfa_bin` |
|:------------|:-----------------------------|:------------------------|
| 0-499       | 0.72                         | 0-499                   |
| 500-749     | 0.75                         | 500-749                 |
| 750-999     | 0.5                          | 750-999                 |
| 1000-1499   | 0.5                          | 1000-1499               |
| 1500-1999   | 0.5                          | 1500-1999               |
| 2000-2499   | 0.5                          | 2000-2499               |
| 2500-2999   | 0.5                          | 2500-2999               |
| 3000-3999   | 0.5                          | 3000-3999               |
| 4000+       | 0.5                          | 4000+                   |

Geometry Floor Area options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_geom_floor_area" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_unit_cfa_bin` | true |  | String |  | E.g., '2000-2499'. |
| `geometry_unit_cfa` | true | ft<sup>2</sup> | Double |  | E.g., '2000' or 'auto'. |
| `geometry_garage_protrusion` | true | Frac | Double |  | The fraction of the garage that is protruding from the conditioned space. Only applies to single-family detached units. |

The ResStock argument definitions set in the Geometry Floor Area characteristic

</div>

##### Distribution Assumption(s)

- Due to low sample count, the characteristic distributions are constructed by downscaling a core input file with 4 sub-input files of different dependencies.

- Sub-input file 1 has dependencies: 'Census Division', 'PUMA Metro Status', 'Geometry Building Type RECS', 'Income RECS2020'

- Sub-input file 2 has dependencies: 'Census Division', 'PUMA Metro Status', 'Geometry Building Type RECS', 'Tenure'

- Sub-input file 3 has dependencies: 'Census Division', 'PUMA Metro Status', 'Geometry Building Type RECS', 'Vintage ACS'

- Sub-input file 4 has dependencies: 'Census Division', 'PUMA Metro Status', 'Income RECS2020', 'Tenure'.

- For each sub-input file, rows with \<10 samples are replaced with coarsening dependency Census Region, followed by the national distribution.

#### Geometry Floor Area Bin

##### Description

The finished floor area of the housing unit using bins.

##### Distribution Data Source(s)

- Directly assigned from the Geometry Floor Area characteristic.

##### Direct Conditional Dependencies

- Geometry Floor Area.

##### Options

The options of the Geometry Floor Area Bin characteristic are 0-1499, 1500-2499, 2500-3999, and 4000+. These floor area bins options are a coarser representation than the Geometry Floor Area characteristic. The Geometry Floor Area Bin Characteristic is often used as a dependency for other characteristics.

##### Distribution Assumption(s)

- The options are directly assigned from the Geometry Floor area characteristic.

### Space Geometry

#### Bedrooms

##### Description

The number of bedrooms in the housing unit.

##### Distribution Data Source(s)

- 2017 and 2019 American Housing Survey microdata.

- Building type categorization based on U.S. EIA 2009 RECS.

##### Direct Conditional Dependencies

- Geometry Building Type RECS

- Geometry Floor Area.

##### Options

The Bedrooms characteristic set the `geometry_unit_num_bedrooms` and the `geometry_unit_num_bathrooms` ResStock arguments. The options for bedrooms are integers from 1 to 5; see Table “Bedroom options and arguments that vary for each option”. The `geometry_unit_num_bathrooms` argument is always set to “auto.” For the argument definitions, see Table “The ResStock argument definitions set in the Bedrooms characteristic”. See the OpenStudio-HPXML [Building Construction](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-building-construction) section of the documentation. The number of bedrooms is used many places in the OpenStudio-HPXML model workflow.

<div id="table:hc_opt_bed" data-source="3a_ResStockInputs.tex">

| Option name | `geometry_unit_num_bedrooms` |
|:------------|:-----------------------------|
| 1           | 1                            |
| 2           | 2                            |
| 3           | 3                            |
| 4           | 4                            |
| 5           | 5                            |

Bedroom options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_bed" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_unit_num_bedrooms` | true | \# | Integer |  | The number of bedrooms in the unit. |
| `geometry_unit_num_bathrooms` | false | \# | Integer | auto | The number of bathrooms in the unit. |

The ResStock argument definitions set in the Bedrooms characteristic

</div>

##### Distribution Assumption(s)

- More than 5 bedrooms are labeled as 5 bedrooms and 0 bedrooms are labeled as 1 bedroom.

- Limit 0-499 ft<sup>2</sup> housing units to only 1 or 2 bedrooms. The geometry measure has a limit of (ffa-120)/70 \>= bedrooms.

#### Geometry Attic Type

##### Description

The housing unit attic type.

##### Distribution Data Source(s)

- U.S. EIA 2020 RECS microdata.

##### Direct Conditional Dependencies

- Census Division RECS

- Geometry Building Type RECS

- Geometry Stories Low Rise

- Vintage ACS.

##### Options

The options for Geometry Attic Type are Finished Attic or Cathedral Ceilings, Unvented Attic, Vented Attic. The None option is used for multifamily and mobile homes. The options in the Geometry Attic Type characteristic set the `geometry_attic_type`, `geometry_roof_type`, and `geometry_roof_pitch` ResStock arguments; see Table “Geometry Attic Type options and arguments that vary for each option”. The `geometry_roof_type` is always set to “gable.” The `geometry_roof_pitch` is always set to 6:12. For ResStock argument definitions, see Table “The ResStock argument definitions set in the Geometry Attic characteristic”. See OpenStudio-HPXML [Attics](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-attics) section of the documentation for elements, constraints, and default values.

<div id="table:hc_opt_attic" data-source="3a_ResStockInputs.tex">

| Option name                          | `geometry_attic_type` |
|:-------------------------------------|:----------------------|
| Finished Attic or Cathedral Ceilings | ConditionedAttic      |
| None                                 | FlatRoof              |
| Unvented Attic                       | UnventedAttic         |
| Vented Attic                         | VentedAttic           |

Geometry Attic Type options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_attic" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_attic_type` | true |  | Choice | FlatRoof, VentedAttic, UnventedAttic, ConditionedAttic, BelowApartment | The attic type of the building. Attic type ConditionedAttic is not allowed for apartment units. |
| `geometry_roof_type` | true |  | Choice | gable, hip | The roof type of the building. Ignored if the building has a flat roof. |
| `geometry_roof_pitch` | true |  | Choice | 1:12, 2:12, 3:12, 4:12, 5:12, 6:12, 7:12, 8:12, 9:12, 10:12, 11:12, 12:12 | The roof pitch of the attic. Ignored if the building has a flat roof. |

The ResStock argument definitions set in the Geometry Attic characteristic

</div>

##### Distribution Assumption(s)

- Multifamily building types and Mobile Homes have Flat Roof (None) only.

- 1-story Single-Family building types cannot have Finished Attic/Cathedral Ceiling because that attic type is modeled as a new story, and 1-story does not have a second story.

- 4+story Single-family and mobile homes are an impossible combination. The None option is assigned but not sampled.

#### Geometry Foundation Type

##### Description

The type of foundation.

##### Distribution Data Source(s)

- The sample counts and sample weights are constructed using U.S. EIA 2009 RECS microdata.

##### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Building Type RECS

- Vintage ACS.

##### Options

The options of the Geometry Foundation type characteristic are Ambient, Heated Basement, Slab, Unheated Basement, Unvented Crawlspace, and Vented Crawlspace. The options set the `geometry_foundation_type`, `geometry_foundation_height`, `geometry_foundation_height_above_grade`, and `geometry_rim_joist_height` ResStock arguments; see Table “Geometry Foundation Type options and arguments that vary for each option”. For ResStock argument definitions, see Table “The ResStock argument definitions set in the Geometry Foundation Type characteristic”. Another name for Ambient foundations is pier and beam.

<div id="table:hc_opt_geom_found_type" data-source="3a_ResStockInputs.tex">

| Option name | `geometry_foundation_type` | `geometry_foundation_height` | `geometry_foundation_height_above_grade` | `geometry_rim_joist_height` |
|:---|:---|:---|:---|:---|
| Ambient | Ambient | 4 | 4 | 0 |
| Heated Basement | ConditionedBasement | 8 | 1 | 9.25 |
| Slab | SlabOnGrade | 0 | 0 | 0 |
| Unheated Basement | UnconditionedBasement | 8 | 1 | 9.25 |
| Unvented Crawlspace | UnventedCrawlspace | 4 | 1 | 9.25 |
| Vented Crawlspace | VentedCrawlspace | 4 | 1 | 9.25 |

Geometry Foundation Type options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_geom_found_type" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_foundation_type` | true |  | Choice | SlabOnGrade, VentedCrawlspace, UnventedCrawlspace, ConditionedCrawlspace, UnconditionedBasement, ConditionedBasement, Ambient, AboveApartment, BellyAndWingWithSkirt, BellyAndWingNoSkirt | The foundation type of the building. Foundation types ConditionedBasement and ConditionedCrawlspace are not allowed for apartment units. |
| `geometry_foundation_height` | true | ft | Double |  | The height of the foundation (e.g., 3 ft for crawlspace, 8 ft for basement). Only applies to basements/crawlspaces and Ambient. |
| `geometry_foundation_height_above_grade` | true | ft | Double |  | The depth above grade of the foundation wall. Only applies to basements/crawlspaces and Ambient. |
| `geometry_rim_joist_height` | false | in | Double |  | The height of the rim joists. Only applies to basements/crawlspaces. |

The ResStock argument definitions set in the Geometry Foundation Type characteristic

</div>

##### Distribution Assumption(s)

- All mobile homes have Ambient foundations.

- Multifamily buildings cannot have Ambient or Heated Basements foundations.

- Single-family attached buildings cannot have Ambient foundations.

- All foundation types are used across all housing types except for mobile homes, which have constrained options.

- Because we need to assume a foundation type for ground-floor MF units, we use the lumped SFD+SFA distributions for MF2-4 and MF5+ building foundations. (RECS data for households in MF2-4 unit buildings are not useful since we do not know which floor the unit is on. RECS does not include foundation responses for households in MF5+ unit buildings.)

- For SFD and SFA, if no foundation type is specified, then the sample has Ambient foundation.

#### Geometry Garage

##### Description

The presence and size of an attached garage.

##### Distribution Data Source(s)

- U.S. EIA 2020 RECS microdata.

##### Direct Conditional Dependencies

- Census Division RECS

- Geometry Building Type RECS

- Geometry Floor Area Bin

- Geometry Foundation Type

- Geometry Stories Low Rise.

##### Options

The options for the Geometry Garage characteristic are 1 Car, 2 Car, 3 Car, and None. The options set the `geometry_garage_width`, `geometry_garage_depth`, and `geometry_garage_position` ResStock arguments; see Table “Bedroom options and arguments that vary for each option”. The `geometry_garage_depth` argument is always set to 24 ft. The `geometry_garage_position` argument is always set to “Right.” ResStock argument definitions can be seen in Table “The ResStock argument definitions set in the Geometry Garage characteristic”.

<div id="table:hc_opt_garage" data-source="3a_ResStockInputs.tex">

| Option name | `geometry_garage_width` |     |     |
|:------------|:------------------------|:----|:----|
| 1 Car       | 12                      |     |     |
| 2 Car       | 24                      |     |     |
| 3 Car       | 36                      |     |     |
| None        | 0                       |     |     |

Bedroom options and arguments that vary for each option

</div>

<div id="table:hc_arg_def_garage" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_garage_width` | true | ft | Double |  | The width of the garage. Enter zero for no garage. Only applies to single-family detached units. |
| `geometry_garage_depth` | true | ft | Double |  | The depth of the garage. Only applies to single-family detached units. |
| `geometry_garage_position` | true |  | Choice | Right, Left | The position of the garage. Only applies to single-family detached units. |

The ResStock argument definitions set in the Geometry Garage characteristic

</div>

##### Distribution Assumption(s)

Most of the assumptions below are not from the survey data, but are constraints of the geometry modeling in OpenStudio and are set to avoid errors.

- Only Single-Family Detached homes are assigned a probability for attached garage.

- No garage for ambient (i.e., pier & beam) foundation type.

- Due to modeling constraints restricting that garage cannot be larger or deeper than livable space: Single-family detached units that are 0-1499 square feet can only have a maximum of a 1-car garage.

- Single-family detached units that are 0-1499 square feet and 3+ stories cannot have a garage.

- The geometry stories distributions are all the same except for 0-1499 square feet and 3 stories.

- Single-family detached units that are 1500-2499 square feet cannot have a 3-car garage.

- Single-family detached units that are 2500-3999 square feet and a heated basement cannot have a 3-car garage.

- Due to low sample sizes, the following sets of dependencies are progressively lumped together.

  - Crawl, basements, and slab are lumped.

  - Story levels are lumped together.

  - Census Division RECS is grouped into Census Region.

  - Vintage ACS is grouped into: pre-1960, 1960-1999, and 2000+.

#### Geometry Space Combination

##### Description

Valid combinations of building type, building level mf, attic, foundation, and garage.

##### Distribution Data Source(s)

- U.S. EIA 2020 RECS microdata.

##### Direct Conditional Dependencies

- Geometry Attic Type

- Geometry Building Level MF

- Geometry Building Type RECS

- Geometry Foundation Type

- Geometry Garage.

##### Options

The options are a direct mapping of Geometry Building Type, Geometry Building Level MF, Geometry Foundation Type, Geometry Attic Type, and Geometry Garage.

##### Distribution Assumption(s)

No assumptions are made. The options of the dependencies are directly mapped into options of this characteristic.

