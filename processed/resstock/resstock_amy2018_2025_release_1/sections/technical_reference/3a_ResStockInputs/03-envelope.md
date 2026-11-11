<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3a_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3a_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3a_ResStockInputs.md | section: Envelope | lines: 2072-3427 -->
## Envelope

The envelope components of ResStock inputs interface closely with the Geometry inputs, but focus more on the materials and thermal properties of the envelope. In this section, we discuss the various input files that control the modeled envelope in ResStock by envelope component.

### Walls

There are three major input files to ResStock that control the wall properties:

- Geometry Wall Type

- Geometry Wall Exterior Finish

- Insulation Wall.

Collectively, they specify the material choices and R-value of the housing unit walls.

#### Geometry Wall Type

##### Description

The wall material used for thermal mass calculations of exterior walls.

##### Distribution Data Source(s)

- HIFLD Parcel data.

##### Direct Conditional Dependencies

- Geometry Building Type RECS

- Geometry Story Bin

- State

- Vintage ACS.

##### Option(s)

ResStock models four different wall types: Brick, Concrete, Steel Frame, and Wood Frame. This is the interior structure of the wall, not the exterior cladding. This input file does not have any ResStock arguments, but other input files that influence the thermal properties of the model are dependent on Geometry Wall Type.

##### Distribution Assumption(s)

- Rows where sample size \< 10 are replaced with aggregated values down-scaled from dep='State' to dep='Census Division RECS'.

#### Geometry Wall Exterior Finish

##### Description

Wall siding material and color. This is the main input file that provides the thermal property arguments for the exterior cladding of a wall.

##### Distribution Data Source(s)

- HIFLD Parcel data.

##### Direct Conditional Dependencies

- Geometry Wall Type

- State

- Vintage ACS.

##### Option(s)

ResStock uses 11 options (see Table “Geometry Wall Exterior Finish options and arguments that vary for each option”) for the exterior finish of the walls—correlated with the Geometry Wall Type via the input dependencies. A portion of the wall R-value is attributable to this exterior finish.

<div id="table:hc_opt_geo_wall_ext_fin" data-source="3a_ResStockInputs.tex">

| Option name | `wall_siding_type` | `wall_color` | `exterior_finish_r` |  |
|:---|:---|:---|:---|:---|
| Aluminum, Light | aluminum siding | light | 0.6 |  |
| Brick, Light | brick veneer | light | 0.7 |  |
| Brick, Medium/Dark | brick veneer | medium dark | 0.7 |  |
| Fiber-Cement, Light | fiber cement siding | light | 0.2 |  |
| None | none | medium | 0 |  |
| Shingle, Asbestos, Medium | asbestos siding | medium | 0.6 |  |
| Shingle, Composition, Medium | composite shingle siding | medium | 0.6 |  |
| Stucco, Light | stucco | light | 0.2 |  |
| Stucco, Medium/Dark | stucco | medium dark | 0.2 |  |
| Vinyl, Light | vinyl siding | light | 0.6 |  |
| Wood, Medium/Dark | wood siding | medium dark | 1.4 |  |

Geometry Wall Exterior Finish options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions for the Geometry Exterior Finish characteristic”. See the OpenStudio-HPXML [Walls](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-walls) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ext_finish" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `wall_siding_type` | false |  | Choice | auto, aluminum siding, asbestos siding, brick veneer, composite shingle siding, fiber cement siding, masonite siding, none, stucco, synthetic stucco, vinyl siding, wood siding | The siding type of the walls. Also applies to rim joists. |
| `wall_color` | false |  | Choice | auto, dark, light, medium, medium dark, reflective | The color of the walls. Also applies to rim joists. |
| `exterior_finish_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | R-value of the exterior finish. |

The ResStock argument definitions for the Geometry Exterior Finish characteristic

</div>

##### Distribution Assumption(s)

- Rows where sample size \< 10 are replaced with aggregated values down-scaled from dep='State' to dep='Census Division RECS'

- Brick wall types are assumed to not have an additional brick exterior finish

- Steel and wood frame walls must have an exterior finish.

#### Insulation Wall

##### Description

Wall construction type and insulation level. Provides the main R-value for the walls of the home. This is in addition to the R-values provided by the exterior wall cladding.

##### Distribution Data Source(s)

- *Single-Family Heating and Cooling Requirements: Assumptions, Methods, and Summary Results* ((Ritschard et al. 1992)).

- *Data Collection-Data Characterization Summary* from the NorthernSTAR Building America Partnership ((Nettleton and Edwards 2012)), as described in Roberts et al., *Assessment of the U.S. Department of Energy’s Home Energy Score Tool* (2012), and Merket et al., *Building America Field Data Repository* webinar (2014).

##### Direct Conditional Dependencies

- Location Region

- Geometry Wall Type

- Vintage.

##### Option(s)

ResStock models 15 different Insulation Wall levels; see Table “Insulation Wall options and arguments that vary for each option”. These are based upon the Geometry Wall Type defined, but provide a distribution of insulation levels for each of those options.

<div id="table:hc_ins_wall" data-source="3a_ResStockInputs.tex">

| Option name | `wall_type` | `wall_assembly_r` |  |
|:---|:---|:---|:---|
| Wood Stud, Uninsulated | WoodStud | 3.4 |  |
| Wood Stud, R-7 | WoodStud | 8.7 |  |
| Wood Stud, R-11 | WoodStud | 10.3 |  |
| Wood Stud, R-15 | WoodStud | 12.1 |  |
| Wood Stud, R-19 | WoodStud | 15.4 |  |
| CMU, 6-in Hollow, Uninsulated | ConcreteMasonryUnit | 4 |  |
| CMU, 6-in Hollow, R-7 | ConcreteMasonryUnit | 9.4 |  |
| CMU, 6-in Hollow, R-11 | ConcreteMasonryUnit | 12.4 |  |
| CMU, 6-in Hollow, R-15 | ConcreteMasonryUnit | 15 |  |
| CMU, 6-in Hollow, R-19 | ConcreteMasonryUnit | 17.4 |  |
| Brick, 12-in, 3-wythe, Uninsulated | StructuralBrick | 4.9 |  |
| Brick, 12-in, 3-wythe, R-7 | StructuralBrick | 10.3 |  |
| Brick, 12-in, 3-wythe, R-11 | StructuralBrick | 13.3 |  |
| Brick, 12-in, 3-wythe, R-15 | StructuralBrick | 15.9 |  |
| Brick, 12-in, 3-wythe, R-19 | StructuralBrick | 18.3 |  |

Insulation Wall options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Insulation Wall characteristic”. See the OpenStudio-HPXML [Walls](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-walls) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ins_wall" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `wall_type` | true |  | Choice | WoodStud, ConcreteMasonryUnit, DoubleWoodStud, InsulatedConcreteForms, LogWall, StructuralInsulatedPanel, SolidConcrete, SteelFrame, Stone, StrawBale, StructuralBrick | The type of walls. |
| `wall_assembly_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Assembly R-value of the walls. |

The ResStock argument definitions set in the Insulation Wall characteristic

</div>

##### Distribution Assumption(s)

- Updated per new wall type from Lightbox, all wall type-specific distributions follow that of Wood Frame (WoodStud).

### Roof and Ceiling

There are three input files describing thermal properties of the roof and/or ceilings of housing units:

- Insulation Roof

- Insulation Ceiling

- Roof Material.

Additionally, there is an input for defining Radiant Barriers in homes with attics, but it is not currently used in ResStock.

A major assumption in ResStock is that multifamily buildings and mobile homes do not have attics (see Section “Space Geometry”), so their insulation is assigned in Insulation Ceiling, while for other building types it is assigned in the Insulation Roof housing characteristic.

#### Insulation Roof

##### Description

Finished roof insulation level. Insulation levels for unfinished attics covered separately.

##### Distribution Data Source(s)

- Derived from Home Innovation Research Labs 1982-2007 Data

- NEEA Residential Building Stock Assessment, 2012.

##### Direct Conditional Dependencies

- Geometry Attic Type.

##### Option(s)

Insulation roof options correspond to the amount of insulation at the roof deck and if the roof is finished; see Table “Insulation Roof options and arguments that vary for each option”. A finished roof is a cathedralized construction of the roof. An unfinished roof corresponds to the roof deck being open to the attic.

<div id="table:hc_ins_roof" data-source="3a_ResStockInputs.tex">

| Option name             | `roof_assembly_r` |
|:------------------------|:------------------|
| Unfinished, Uninsulated | 2.3               |
| Finished, Uninsulated   | 3.7               |
| Finished, R-7           | 10.2              |
| Finished, R-13          | 14.3              |
| Finished, R-19          | 21.2              |
| Finished, R-30          | 29.7              |
| Finished, R-38          | 36.5              |
| Finished, R-49          | 47.0              |

Insulation Roof options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Insulation Roof characteristic”. See the OpenStudio-HPXML [Roofs](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-roofs) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ins_roof" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `roof_assembly_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Assembly R-value of the roof |

The ResStock argument definitions set in the Insulation Roof characteristic

</div>

##### Distribution Assumption(s)

None

#### Radiant Barrier

##### Description

Presence of radiant barrier in the attic (not currently used in ResStock).

##### Distribution Data Source(s)

- Not applicable

- All homes are assumed to not have attic radiant barriers installed.

##### Direct Conditional Dependencies

- Geometry Building Type RECS.

##### Option(s)

Three options for radiant barriers are available in ResStock: “Yes,” “No,” and “None”; see Table “Radiant Barrier options and arguments that vary for each option”. “No” is assigned to homes with attics but without radiant barriers, while “None” is assigned to homes without attics. No homes in ResStock currently have the “Yes” option assigned.

<div id="table:hc_opt_rad_bar" data-source="3a_ResStockInputs.tex">

| Option name | `radiant_barrier_attic_location` | `radiant_barrier_grade` |     |
|:------------|:---------------------------------|:------------------------|:----|
| None        | none                             | 1                       |     |
| Yes         | attic roof only                  | 1                       |     |
| No          | none                             | 1                       |     |

Radiant Barrier options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Radiant Barrier characteristic”. See the OpenStudio-HPXML [Roofs](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-roofs) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_rad_bar" data-source="3a_ResStockInputs.tex">

| Name | Required | Type | Choices | Description |
|:---|:---|:---|:---|:---|
| `radiant_barrier_attic_location` | false | Choice | auto, none, attic roof only, attic roof and gable walls, attic floor | The location of the radiant barrier in the attic |
| `radiant_barrier_grade` | false | Choice | auto, 1, 2, 3 | The grade of the radiant barrier in the attic |

The ResStock argument definitions set in the Radiant Barrier characteristic

</div>

##### Distribution Assumption(s)

None

#### Roof Material

##### Description

Roof material and color.

##### Distribution Data Source(s)

- U.S. EIA 2020 RECS microdata.

##### Direct Conditional Dependencies

- Census Division RECS

- Geometry Building Type RECS

- Vintage ACS.

##### Option(s)

Seven roof material options are used in the ResStock baseline; see Table “Roof Material options and arguments that vary for each option”. These correspond to options available within OpenStudio-HPXML and have thermal properties associated with each within OpenStudio-HPXML, but this is not specified at the ResStock level.

<div id="table:hc_opt_roof_mat" data-source="3a_ResStockInputs.tex">

| Option name              | `roof_material_type`           | `roof_color` |
|:-------------------------|:-------------------------------|:-------------|
| Asphalt Shingles, Medium | asphalt or fiberglass shingles | medium       |
| Composition Shingles     | asphalt or fiberglass shingles | medium       |
| Metal, Dark              | metal surfacing                | dark         |
| Slate                    | slate or tile shingles         | medium       |
| Tile, Clay or Ceramic    | slate or tile shingles         | medium       |
| Tile, Concrete           | slate or tile shingles         | medium       |
| Wood Shingles            | wood shingles or shakes        | medium       |

Roof Material options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Roof Material characteristic”. See the OpenStudio-HPXML [Roof](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-roof) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_roof_mat" data-source="3a_ResStockInputs.tex">

| Name | Required | Type | Choices | Description |
|:---|:---|:---|:---|:---|
| `roof_material_type` | false | Choice | auto, asphalt or fiberglass shingles, concrete, cool roof, slate or tile shingles, expanded polystyrene sheathing, metal surfacing, plastic/rubber/synthetic sheeting, shingles, wood shingles or shakes | The material type of the roof |
| `roof_color` | false | Choice | auto, dark, light, medium, medium dark, reflective | The color of the roof |

The ResStock argument definitions set in the Roof Material characteristic

</div>

##### Distribution Assumption(s)

- Multifamily with 5+ Units is assigned ‘Asphalt Shingles, Medium’ only.

- Due to low samples, Vintage ACS is progressively grouped into: pre-1960, 1960-1999, and 2000+.

- Geometry Building Type RECS is progressively grouped into: Single-Family (including Mobile Home), and Multifamily.

- Census Division RECS is coarsened to Census Region.

#### Insulation Ceiling

##### Description

This characteristic in ResStock specifies the insulation level of the ceiling on the top floor of the home in housing units with vented or unvented attics.

##### Distribution Data Source(s)

- NEEA Residential Building Stock Assessment, 2012.

- *Data Collection-Data Characterization Summary* from the NorthernSTAR Building America Partnership ((Nettleton and Edwards 2012)), as described in Roberts et al., *Assessment of the U.S. Department of Energy’s Home Energy Score Tool* (2012) and Merket et al., *Building America Field Data Repository* webinar, 2014.

- Derived from Home Innovation Research Labs 1982-2007 Data.

##### Direct Conditional Dependencies

- Geometry Attic Type

- Location Region

- Vintage.

##### Option(s)

The options are levels of ceiling insulation by R-value; see Table “Insulation Ceiling options and arguments that vary for each option”. Uninsulated indicates that the housing unit could have ceiling insulation, but doesn’t, whereas “None” indicates the housing unit cannot have ceiling insulation because it does not have an unfinished attic.

<div id="table:hc_opt_ins_ceil" data-source="3a_ResStockInputs.tex">

| Option name | `ceiling_assembly_r` | `ceiling_insulation_r` |
|:------------|:---------------------|:-----------------------|
| None        | 0                    | 0                      |
| Uninsulated | 2.1                  | 0                      |
| R-7         | 8.7                  | 7                      |
| R-13        | 14.6                 | 13                     |
| R-19        | 20.6                 | 19                     |
| R-30        | 31.6                 | 30                     |
| R-38        | 39.6                 | 38                     |
| R-49        | 50.6                 | 49                     |

Insulation Ceiling options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Insulation Ceiling characteristic”. See the OpenStudio-HPXML [Attics](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-attics) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ins_ceil" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `ceiling_assembly_r` | true | h-ft<sup>2</sup>-R/Btu | Double | Assembly R-value for the ceiling (attic floor). |
| `ceiling_insulation_r` | true | h-ft<sup>2</sup>-R/Btu | Double | Nominal R-value for the ceiling (attic floor). |

The ResStock argument definitions set in the Insulation Ceiling characteristic

</div>

##### Distribution Assumption(s)

- Vented Attic has the same distribution as Unvented Attic

- CRHI is a copy of CR09

- CRAK is a copy of CR02.

### Foundation

Five input files specify insulation and heat transfer parameters with the ground:

- Insulation Floor

- Insulation Foundation Wall

- Insulation Rim Joist

- Insulation Slab

- Ground Thermal Conductivity.

The inputs starting with “Insulation” specify insulation levels that vary depending upon Geometry Foundation Type (Section “Geometry Foundation Type”).

#### Insulation Floor

##### Description

Sets the insulation levels of all foundation types except for slab-on-grade.

##### Distribution Data Source(s)

- Derived from Home Innovation Research Labs 1982-2007 Data

- Pre-1980 uses engineering judgment.

##### Direct Conditional Dependencies

- Location Region

- Vintage

- Geometry Building Type RECS

- Geometry Foundation Type.

##### Option(s)

ResStock has three different levels of floor insulation, plus a None option that is assigned to buildings with an illegible foundation type for the Insulation Floor characteristic; see Table “Insulation Floor options and arguments that vary for each option”. All options set the `floor_type` to `WoodFrame`.

<div id="table:hc_opt_ins_floor" data-source="3a_ResStockInputs.tex">

| Option name | `floor_over_foundation_assembly_r` | `floor_over_garage_assembly_r` |
|:---|:---|:---|
| None | 0 | 5.3 |
| Uninsulated | 5.3 | 5.3 |
| Ceiling R-13 | 17.8 | 17.8 |
| Ceiling R-19 | 22.6 | 22.6 |
| Ceiling R-30 | 30.3 | 30.3 |

Insulation Floor options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Insulation Floor characteristic”. See the OpenStudio-HPXML [Floors](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-floors) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ins_floor" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `floor_over_foundation_assembly_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Assembly R-value for the floor over the foundation. Ignored if the building has a slab-on-grade foundation. |
| `floor_over_garage_assembly_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Assembly R-value for the floor over the garage. Ignored unless the building has a garage under conditioned space. |
| `floor_type` | true |  | Choice | WoodFrame, StructuralInsulatedPanel, SolidConcrete, SteelFrame | The type of floors. |

The ResStock argument definitions set in the Insulation Floor characteristic

</div>

##### Distribution Assumption(s)

- CRHI is a copy of CR09

- CRAK is a copy of CR02.

#### Insulation Slab

##### Description

Defines the insulation level for all slab-on-grade foundation types.

##### Distribution Data Source(s)

- Derived from Home Innovation Research Labs 1982-2007 Data

- Pre-1980 uses engineering judgment.

##### Direct Conditional Dependencies

- Location Region

- Vintage

- Geometry Building Type RECS

- Geometry Foundation Type.

##### Option(s)

ResStock uses eight different options for Insulation Slab, plus a “None” flag for homes without a slab-on-grade foundation; see Table “Insulation Slab options and arguments that vary for each option”. The options specify both the R-value as well as the location of the slab insulation. The ResStock arguments `slab_thickness`,`slab_carpet_fraction`, and `slab_carpet_r` are constant across all the options and are all set to auto. The ResStock arguments `slab_under_insulation_width`, `slab_exterior_horizontal_insulation_width`, and `lab_exterior_horizontal_insulation_depth_below_grade` are constant and set to 0.

<div id="table:hc_opt_ins_slab" data-source="3a_ResStockInputs.tex">

| Option name | `slab_perimeter_insulation_r` | `slab_perimeter_depth` | `slab_under_insulation_r` | `slab_under_insulation_width` |
|:---|:---|:---|:---|:---|
| None | 0 | 0 | 0 | 0 |
| Uninsulated | 0 | 0 | 0 | 0 |
| 2ft R5 Under, Horizontal | 0 | 0 | 5 | 2 |
| 2ft R10 Under, Horizontal | 0 | 0 | 10 | 2 |
| 4ft R5 Under, Horizontal | 0 | 0 | 5 | 4 |
| 2ft R5 Perimeter, Vertical | 5 | 2 | 0 | 0 |
| 2ft R10 Perimeter, Vertical | 10 | 2 | 0 | 0 |
| R10 Whole Slab, Horizontal | 0 | 0 | 10 | 999 |

Insulation Slab options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Insulation Slab characteristic”. See the OpenStudio-HPXML [ Slabs](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-slabs) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ins_slab" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `slab_perimeter_insulation_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Nominal R-value of the vertical slab perimeter insulation. Applies to slab-on-grade foundations and basement/crawlspace floors. |
| `slab_perimeter_insulation_depth` | true | ft | Double |  | Depth from grade to bottom of vertical slab perimeter insulation. Applies to slab-on-grade foundations and basement/crawlspace floors. |
| `slab_exterior_horizontal_insulation_width` | false | h-ft<sup>2</sup>-R/Btu | Double |  | Nominal R-value of the slab exterior horizontal insulation. Applies to slab-on-grade foundations and basement/crawlspace floors. |
| `slab_exterior_horizontal_insulation_width` | false | ft | Double |  | Width of the slab exterior horizontal insulation measured from the exterior surface of the vertical slab perimeter insulation. Applies to slab-on-grade foundations and basement/crawlspace floors. |
| `slab_exterior_horizontal_insulation_depth_below_grade` | false | ft | Double |  | Depth of the slab exterior horizontal insulation measured from the top surface of the slab exterior horizontal insulation. Applies to slab-on-grade foundations and basement/crawlspace floors. |
| `slab_under_insulation_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Nominal R-value of the horizontal under slab insulation. Applies to slab-on-grade foundations and basement/crawlspace floors. |
| `slab_under_insulation_width` | true | ft | Double |  | Width from slab edge inward of horizontal under-slab insulation. Enter 999 to specify that the under slab insulation spans the entire slab. Applies to slab-on-grade foundations and basement/crawlspace floors. |
| `slab_thickness` | false | in | Double | auto | The thickness of the slab. Zero can be entered if there is a dirt floor instead of a slab. |
| `slab_carpet_fraction` | false | Frac | Double | auto | Fraction of the slab floor area that is carpeted. |
| `slab_carpet_r` | false | h-ft<sup>2</sup>-R/Btu | Double | auto | R-value of the slab carpet. |

The ResStock argument definitions set in the Insulation Slab characteristic

</div>

##### Distribution Assumption(s)

- CRHI is a copy of CR09

- CRAK is a copy of CR02.

#### Insulation Foundation Wall

##### Description

Specifies the insulation level of foundation types with foundation walls (i.e., crawlspaces and basements).

##### Distribution Data Source(s)

- Derived from Home Innovation Research Labs 1982-2007 Data

- Pre-1980 uses engineering judgment.

##### Direct Conditional Dependencies

- Location Region

- Vintage

- Geometry Building Type RECS

- Geometry Foundation Type.

##### Option(s)

ResStock provides four different options for Insulation Foundation Wall, plus a “None” flag for homes without foundation walls (Table “Insulation Foundation Wall options and arguments that vary for each option”). Several ResStock arguments are constant across all options: `foundation_wall_thickness` and `foundation_wall_assembly_r` are always set to *auto*, `foundation_wall_insulation_location` is always *exterior*, and `foundation_wall_insulation_distance_to_top` is 0.

<div id="table:hc_opt_ins_found_wall" data-source="3a_ResStockInputs.tex">

| Option name | `foundation_wall_type` | `foundation_wall_insulation_r` | `foundation_wall_insulation_distance_to_bottom` |
|:---|:---|:---|:---|
| None | solid concrete | 0 | 0 |
| Uninsulated | solid concrete | 0 | 0 |
| Wall R-5, Exterior | solid concrete | 5 | auto |
| Wall R-10, Exterior | solid concrete | 10 | auto |
| Wall R-15, Exterior | solid concrete | 15 | auto |

Insulation Foundation Wall options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Insulation Foundation Wall characteristic”. See the OpenStudio-HPXML [Foundation Walls](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-foundation-walls) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ins_found_wall" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `foundation_wall_type` | false |  | Choice | auto, solid concrete, concrete block, concrete block foam core, concrete block perlite core, concrete block vermiculite core, concrete block solid core, double brick, wood | The material type of the foundation wall. |
| `foundation_wall_thickness` | false | in | Double | auto | The thickness of the foundation wall. |
| `foundation_wall_insulation_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Nominal R-value for the foundation wall insulation. Only applies to basements/crawlspaces. |
| `foundation_wall_insulation_location` | false | ft | Choice | auto, interior, exterior | Whether the insulation is on the interior or exterior of the foundation wall. Only applies to basements/crawlspaces. |
| `foundation_wall_insulation_distance_to_top` | false | ft | Double | auto | The distance from the top of the foundation wall to the top of the foundation wall insulation. Only applies to basements/crawlspaces. |
| `foundation_wall_insulation_distance_to_bottom` | false | ft | Double | auto | The distance from the top of the foundation wall to the bottom of the foundation wall insulation. Only applies to basements/crawlspaces. |
| `foundation_wall_assembly_r` | false | h-ft<sup>2</sup>-R/Btu | Double |  | Assembly R-value for the foundation walls. Only applies to basements/crawlspaces. If provided, overrides the previous foundation wall insulation inputs. |

The ResStock argument definitions set in the Insulation Foundation Wall characteristic

</div>

##### Distribution Assumption(s)

- CRHI is a copy of CR09

- CRAK is a copy of CR02.

#### Insulation Rim Joist

##### Description

Insulation level for rim joists. Set the same as the insulation level for the foundation wall.

##### Distribution Data Source(s)

- Engineering judgment.

##### Direct Conditional Dependencies

- Insulation Foundation Wall.

##### Option(s)

ResStock uses four different levels of rim-joist insulation as well as a “None” flag for homes without rim joists. These options map directly to the foundation wall insulation levels. The ResStock argument for `rim_joist_assembly_r` is always set to *auto*, and `rim_joist_continuous_interior_r` and `rim_joist_assembly_interior_r` are both set to 0 for all options.

| Option name    | Stock saturation | `rim_joist_continuous_exterior_r` |
|:---------------|:-----------------|:----------------------------------|
| None           | 48%              | 0                                 |
| Uninsulated    | 47%              | 0                                 |
| R-5, Exterior  | 1.2%             | 5                                 |
| R-10, Exterior | 2.8%             | 10                                |
| R-15, Exterior | 0.52%            | 15                                |

Options and saturation for Insulation Rim Joist

For the argument definitions, see Table “The ResStock argument definitions set in the Rim Joist characteristic”. See the OpenStudio-HPXML [Rim Joists](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-rim-joists) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ins_rim_joists" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `rim_joist_assembly_r` | false | h-ft<sup>2</sup>-R/Btu | Double |  | Assembly R-value for the rim joists. Only applies to basements/crawlspaces. Required if a rim joist height is provided. |
| `rim_joist_continuous_exterior_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Nominal R-value for the rim joist continuous exterior insulation. Only applies to basements/crawlspaces. |
| `rim_joist_continuous_interior_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Nominal R-value for the rim joist continuous interior insulation that runs parallel to floor joists. Only applies to basements/crawlspaces. |
| `rim_joist_assembly_interior_r` | true | h-ft<sup>2</sup>-R/Btu | Double |  | Assembly R-value for the rim joist assembly interior insulation that runs perpendicular to floor joists. Only applies to basements/crawlspaces. |

The ResStock argument definitions set in the Rim Joist characteristic

</div>

##### Distribution Assumption(s)

- Rim joist insulation is the same value as the foundation wall insulation.

#### Ground Thermal Conductivity

##### Description

The thermal conductivity (in Btu/hr-ft-F) of the ground used in foundation and geothermal heat pump heat transfer calculations.

##### Distribution Data Source(s)

- Data from the Southern Methodist University Geothermal Laboratory. The data are from the Thermal Conductivity Observation in Content Model Format dataset. The data are available at <https://www.smu.edu/dedman/academics/departments/earth-sciences/research/geothermallab/datamaps/ngds-project>.

##### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004.

##### Option(s)

ResStock uses 8 options for Thermal Ground Conductivity, which is expressed in BTU/hr-ft-F (Table “Ground Thermal Conductivity options and arguments that vary for each option”). The ResStock arguments associated with each option vary only in the `site_ground_conductivity` parameter. The other two arguments, `site_soil_and_moisture_type` and `site_ground_diffusivity`, both receive `auto` assignment, regardless of the ResStock option.

<div id="table:hc_opt_ground_k" data-source="3a_ResStockInputs.tex">

| Option name | `site_ground_conductivity` |     |
|:------------|:---------------------------|:----|
| 0.5         | 0.5                        |     |
| 0.8         | 0.8                        |     |
| 1.1         | 1.1                        |     |
| 1.4         | 1.4                        |     |
| 1.7         | 1.7                        |     |
| 2.0         | 2.0                        |     |
| 2.3         | 2.3                        |     |
| 2.6         | 2.6                        |     |

Ground Thermal Conductivity options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Ground Thermal Conductivity characteristic”. See the OpenStudio-HPXML [Site](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-site) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_ground_k" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `site_soil_and_moisture_type` | false |  | Choice | auto, clay, dry, clay, mixed, clay, wet, gravel, dry, gravel, mixed, gravel, wet, loam, dry, loam, mixed, loam, wet, sand, dry, sand, mixed, sand, wet, silt, dry, silt, mixed, silt, wet, unknown, dry, unknown, mixed, unknown, wet | Type of soil and moisture. This is used to inform ground conductivity and diffusivity. |
| `site_ground_conductivity` | false | Btu/hr-ft-F | Double |  | Conductivity of the ground soil. If provided, overrides the previous soil and moisture type input. |
| `site_ground_diffusivity` | false | ft<sup>2</sup>/hr | Double |  | Diffusivity of the ground soil. If provided, overrides the previous soil and moisture type input. |

The ResStock argument definitions set in the Ground Thermal Conductivity characteristic

</div>

##### Distribution Assumption(s)

- The data obtained are from surveyed oil and gas well data.

- The latitudes and longitudes were assigned to counties and the data were joined to the ResStock spatial lookup tables. In this process, 1,482 of 59,332 samples did not have a FIPS match or did not have data and were dropped.

- Due to limited data in climate zone 1A, data were pulled from samples in 1A plus Florida 2A.

- Samples less than 0.5 Btu/hr-ft-F are assigned a value of 0.5 Btu/hr-ft-F. Samples greater than 2.6 Btu/hr-ft-F are assigned a value of 2.6 Btu/hr-ft-F.

### Doors and Windows

In ResStock, two input files control door specification in ResStock:

- Doors

- Door Area.

Two similar input files specify windows:

- Windows

- Window Areas.

Discussed also in this section are building features that might impact shading in windows. All three of these inputs are either not used or have constant values for the entire stock:

- Interior Shading

- Eaves

- Overhangs.

#### Door Area

##### Description

Area of exterior doors. All ResStock models currently receive the same option.

##### Distribution Data Source(s)

- Engineering judgment.

##### Direct Conditional Dependencies

- None.

##### Option(s)

All ResStock housing units currently receive an option of 20 ft<sup>2</sup> for the exterior area of doors; see Table “Door Area options and arguments that vary for each option”.

<div id="table:hc_opt_door_area" data-source="3a_ResStockInputs.tex">

| Option name       | `door_area` |
|:------------------|:------------|
| 20 ft<sup>2</sup> | 20          |

Door Area options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Door Area characteristic”. See the OpenStudio-HPXML [Doors](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-doors) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_door_area" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Description |  |
|:---|:---|:---|:---|:---|:---|
| `door_area` | true | ft<sup>2</sup> | Double | The area of the opaque door(s). |  |

The ResStock argument definitions set in the Door Area characteristic

</div>

##### Distribution Assumption(s)

None

#### Doors

##### Description

Exterior door material and properties.

##### Distribution Data Source(s)

- Engineering judgment.

##### Direct Conditional Dependencies

- None

##### Option(s)

All homes in ResStock receive Fiberglass doors with an R-value of 5 (Table “Door options and arguments that vary for each option”).

<div id="table:hc_opt_door" data-source="3a_ResStockInputs.tex">

| Option name | `door_rvalue` |
|:------------|:--------------|
| Fiberglass  | 5             |

Door options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Door characteristic”. See the OpenStudio-HPXML [Doors](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-doors) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_door" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `door_rvalue` | true | h-ft<sup>2</sup>-R/Btu | Double |  | R-value of the opaque door(s) |

The ResStock argument definitions set in the Door characteristic

</div>

##### Distribution Assumption(s)

None.

#### Windows

##### Description

Construction type and efficiency levels of windows.

##### Distribution Data Source(s)

- U.S. EIA 2020 RECS microdata.

##### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Federal Poverty Level

- Geometry Building Type RECS

- Tenure

- Vintage ACS.

##### Option(s)

ResStock uses 10 window options in the baseline, with variation across number of panes, low-emissivity coating, and frame material. Across all Window options, multiple ResStock arguments are constant (Table “Windows options and arguments that vary for each option”). `window_natvent_availability`, `window_exterior_shading_winter`, `window_exterior_shading_summer`, `window_shading_summer_season`, and `skylight_storm_type` are all set to *auto*. Furthermore, two skylight window parameters are constant: `skylight_ufactor` is always set to 0.37 and `skylight_shgc` is always 0.3.

<div id="table:hc_opt_window" data-source="3a_ResStockInputs.tex">

| Option name | `window_ufactor` | `window_shgc` |
|:---|:---|:---|
| Single, Clear, Metal | 1.16 | 0.76 |
| Single, Clear, Metal, Exterior Clear Storm | 0.67 | 0.56 |
| Single, Clear, Non-metal | 0.84 | 0.63 |
| Single, Clear, Non-metal, Exterior Clear Storm | 0.47 | 0.54 |
| Double, Clear, Metal, Air | 0.76 | 0.67 |
| Double, Clear, Metal, Air, Exterior Clear Storm | 0.55 | 0.51 |
| Double, Clear, Non-metal, Air | 0.49 | 0.56 |
| Double, Clear, Non-metal, Air, Exterior Clear Storm | 0.34 | 0.49 |
| Double, Low-E, Non-metal, Air, M-Gain | 0.38 | 0.44 |
| Triple, Low-E, Non-metal, Air, L-Gain | 0.29 | 0.26 |

Windows options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Windows characteristic”. See the OpenStudio-HPXML [Windows](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-windows) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_wind" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `window_natvent_availability` | false | Days/week | Integer | auto | For operable windows, the number of days/week that windows can be opened by occupants for natural ventilation. |
| `window_ufactor` | true | Btu/hr-ft<sup>2</sup>-R | Double |  | Full-assembly National Fenestration Rating Council (NFRC) U-factor. |
| `window_shgc` | true |  | Double |  | Full-assembly NFRC solar heat gain coefficient. |
| `window_exterior_shading_winter` | false | Frac | Double | auto | Exterior shading coefficient for the winter season. 1.0 indicates no reduction in solar gain, 0.85 indicates 15% reduction, etc. |
| `window_exterior_shading_summer` | false | Frac | Double | auto | Exterior shading coefficient for the summer season. 1.0 indicates no reduction in solar gain, 0.85 indicates 15% reduction, etc. |
| `window_shading_summer_season` | false |  | String | auto | Enter a date like 'May 1 - Sep 30'. Defines the summer season for purposes of shading coefficients; the rest of the year is assumed to be winter. |
| `skylight_ufactor` | true | Btu/hr-ft<sup>2</sup>-R | Double |  | Full-assembly NFRC U-factor. |
| `skylight_shgc` | true |  | Double |  | Full-assembly NFRC solar heat gain coefficient. |
| `skylight_storm_type` | false |  | Choice | auto, clear, low-e | The type of storm, if present. If not provided, assumes there is no storm. |

The ResStock argument definitions set in the Windows characteristic

</div>

##### Distribution Assumption(s)

- All Triple-Pane options assumed to be low-e.

- Only breaking out clear and low-e windows for the Double, Non-Metal frame type.

- Source of low-e distribution is based on engineering judgment, informed by high-level sales trends observed in Ducker Worldwide studies of the U.S. market for windows, doors and skylights.

- Due to low sample sizes, the following adjustments are made:

  - Vintage data are grouped into: (1) \<1960, (2) 1960-79, (3) 1980-99, (4) 2000s, (5) 2010s.

  - Building Type data are grouped into: (1) Single-Family Detached, Single-Family Attached, and Mobile homes, and (2) Multifamily 2-4 units and Multifamily 5+ units.

  - Climate zones are grouped into:

    - 1A, 2A, 2B

    - 3A, 3B, 3C, 4B

    - 4A, 4C

    - 5A, 5B

    - 6A, 6B and

    - 7A, 7B 7AK, 8AK.

  <!-- -->

  - Federal Poverty Levels are progressively grouped together until all bins are combined.

  - Tenure options are progressively grouped together until all bins are combined.

- Storm window saturations are based on D&R International, Ltd. [2013](https://www.energy.gov/sites/prod/files/2013/11/f5/residential_windows_coverings.pdf). *Residential Windows and Window Coverings: A Detailed View of the Installed Base and User Behavior*. Cut the % storm windows by factor of 55% because only 55% of storms are installed year-round.

- Due to lack of performance data, Triple-Pane windows with storms are modeled without the storm windows.

- Due to lack of performance data, Double-Pane, Low-E, Non-Metal, Air, M-gain, and Exterior Clear Storm windows are modeled as Double-Pane, Clear, Non-Metal, Air, Exterior Clear Storm windows.

#### Window Areas

##### Description

Window-to-wall ratios for the front, back, left, and right walls.

##### Distribution Data Source(s)

- 2016-17 Residential Building Stock Assessment (RBSA) II microdata.

##### Direct Conditional Dependencies

- Geometry Building Type Height.

##### Option(s)

ResStock arguments use window-to-wall ratios to specify the window area instead of defining absolute window areas. Therefore, the following wall area constants are all set to zero in ResStock:

- `window_area_front` = 0

- `window_area_back` = 0

- `window_area_left` = 0

- `window_area_right` = 0

- `skylight_area_front` = 0

- `skylight_area_back` = 0

- `skylight_area_left` = 0

- `skylight_area_right` = 0.

ResStock has six different levels of window-to-wall ratios between 0.06 and 0.3 (Table “Window Area options and arguments that vary for each option”). Window-to-wall ratios are assumed constant on all sides of the home.

Additionally, the `window_aspect_ratio` is set to 1.333 for all ResStock options.

<div id="table:hc_opt_window_area" data-source="3a_ResStockInputs.tex">

| Option name | `window_front_wwr` | `window_back_wwr` | `window_left_wwr` | `window_right_wwr` |
|:---|:---|:---|:---|:---|
| F6 B6 L6 R6 | 0.06 | 0.06 | 0.06 | 0.06 |
| F9 B9 L9 R9 | 0.09 | 0.09 | 0.09 | 0.09 |
| F12 B12 L12 R12 | 0.12 | 0.12 | 0.12 | 0.12 |
| F15 B15 L15 R15 | 0.15 | 0.15 | 0.15 | 0.15 |
| F18 B18 L18 R18 | 0.18 | 0.18 | 0.18 | 0.18 |
| F30 B30 L30 R30 | 0.30 | 0.30 | 0.30 | 0.30 |

Window Area options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Window Area characteristic”. See the OpenStudio-HPXML [Windows](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-windows) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_window_area" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `window_front_wwr` | true | Frac | Double | The ratio of window area to wall area for the unit’s front facade. Enter 0 if specifying Front Window Area instead. |
| `window_back_wwr` | true | Frac | Double | The ratio of window area to wall area for the unit’s back facade. Enter 0 if specifying Back Window Area instead. |
| `window_left_wwr` | true | Frac | Double | The ratio of window area to wall area for the unit’s left facade (when viewed from the front). Enter 0 if specifying Left Window Area instead. |
| `window_right_wwr` | true | Frac | Double | The ratio of window area to wall area for the unit’s right facade (when viewed from the front). Enter 0 if specifying Right Window Area instead. |
| `window_area_front` | true | ft<sup>2</sup> | Double | The amount of window area on the unit’s front facade. Enter 0 if specifying Front Window-to-Wall Ratio instead. |
| `window_area_back` | true | ft<sup>2</sup> | Double | The amount of window area on the unit’s back facade. Enter 0 if specifying Back Window-to-Wall Ratio instead. |
| `window_area_left` | true | ft<sup>2</sup> | Double | The amount of window area on the unit’s left facade (when viewed from the front). Enter 0 if specifying Left Window-to-Wall Ratio instead. |
| `window_area_right` | true | ft<sup>2</sup> | Double | The amount of window area on the unit’s right facade (when viewed from the front). Enter 0 if specifying Right Window-to-Wall Ratio instead. |
| `window_aspect_ratio` | true | Frac | Double | Ratio of window height to width. |
| `skylight_area_front` | true | ft<sup>2</sup> | Double | The amount of skylight area on the unit’s front conditioned roof facade. |
| `skylight_area_back` | true | ft<sup>2</sup> | Double | The amount of skylight area on the unit’s back conditioned roof facade. |
| `skylight_area_left` | true | ft<sup>2</sup> | Double | The amount of skylight area on the unit’s left conditioned roof facade (when viewed from the front). |
| `skylight_area_right` | true | ft<sup>2</sup> | Double | The amount of skylight area on the unit’s right conditioned roof facade (when viewed from the front). |

The ResStock argument definitions set in the Window Area characteristic

</div>

##### Distribution Assumption(s)

- The window-to-wall ratios (WWR) are exponential weibull distributed

- Multifamily with 2-4 Units distributions are independent of Geometry Stories

- Multifamily with 5+ Units distributions are grouped by 1-3 stories, 4-7 stories, and 8+ stories

- High-rise Multifamily buildings (8+ stories) have a 30% WWR

- SFD, SFA, and Mobile Homes are represented by the SFD window area distribution.

#### Overhangs

##### Description

Presence, depth, and location of window overhangs (not currently used in ResStock baseline).

##### Distribution Data Source(s)

- Not applicable.

##### Direct Conditional Dependencies

- None.

##### Option(s)

ResStock currently assumes all buildings have no overhang. Therefore, all models are assigned the option of “None” for this characteristic, and receive the following ResStock arguments:

- `overhangs_front_depth` = 0

- `overhangs_front_distance_to_top_of_window` = 0

- `overhangs_front_distance_to_bottom_of_window` = 4

- `overhangs_back_depth` = 0

- `overhangs_back_distance_to_top_of_window` = 0

- `overhangs_back_distance_to_bottom_of_window` = 4

- `overhangs_left_depth` = 0

- `overhangs_left_distance_to_top_of_window` = 0

- `overhangs_left_distance_to_bottom_of_window` = 4

- `overhangs_right_depth` = 0

- `overhangs_right_distance_to_top_of_window` = 0

- `overhangs_right_distance_to_bottom_of_window` = 4

For the argument definitions, see Table “The ResStock argument definitions set in the Overhangs characteristic”. See the OpenStudio-HPXML [Overhangs](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-overhangs) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_overhang" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Description |
|:---|:---|:---|:---|:---|
| `overhangs_front_depth` | true | ft | Double | The depth of overhangs for windows for the front facade. |
| `overhangs_front_distance_to_top_of_window` | true | ft | Double | The overhangs distance to the top of window for the front facade. |
| `overhangs_front_distance_to_bottom_of_window` | true | ft | Double | The overhangs distance to the bottom of window for the front facade. |
| `overhangs_back_depth` | true | ft | Double | The depth of overhangs for windows for the back facade. |
| `overhangs_back_distance_to_top_of_window` | true | ft | Double | The overhangs distance to the top of window for the back facade. |
| `overhangs_back_distance_to_bottom_of_window` | true | ft | Double | The overhangs distance to the bottom of window for the back facade. |
| `overhangs_left_depth` | true | ft | Double | The depth of overhangs for windows for the left facade. |
| `overhangs_left_distance_to_top_of_window` | true | ft | Double | The overhangs distance to the top of window for the left facade. |
| `overhangs_left_distance_to_bottom_of_window` | true | ft | Double | The overhangs distance to the bottom of window for the left facade. |
| `overhangs_right_depth` | true | ft | Double | The depth of overhangs for windows for the right facade. |
| `overhangs_right_distance_to_top_of_window` | true | ft | Double | The overhangs distance to the top of window for the right facade. |
| `overhangs_right_distance_to_bottom_of_window` | true | ft | Double | The overhangs distance to the bottom of window for the right facade. |

The ResStock argument definitions set in the Overhangs characteristic

</div>

##### Distribution Assumption(s)

- All homes are assumed to not have window overhangs (roof eaves are defined separately).

#### Eaves

##### Description

Depth of roof eaves.

##### Distribution Data Source(s)

- Building America House Simulation Protocols ((Wilson et al. 2014)).

##### Direct Conditional Dependencies

None.

##### Option(s)

All buildings receive the same value of 2 feet for `geometry_eaves_depth`.

For the argument definitions, see Table “The ResStock argument definitions set in the Eaves characteristic”. See the OpenStudio-HPXML [Enclosure](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-enclosure) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_eaves" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_eaves_depth` | true | ft | Double |  | The eaves depth of the roof. |

The ResStock argument definitions set in the Eaves characteristic

</div>

##### Distribution Assumption(s)

None.

#### Interior Shading

##### Description

Amount of window shading in the summer and winter.

##### Distribution Data Source(s)

- ANSI/RESNET/ICC 301 Standard.

##### Direct Conditional Dependencies

- None.

##### Option(s)

All models in ResStock receive the same shading option (Table “Interior Shading options and arguments that vary for each option”).

<div id="table:hc_opt_int_shade" data-source="3a_ResStockInputs.tex">

| Option name | `window_interior_shading_winter` | `window_interior_shading_summer` |
|:---|:---|:---|
| Summer = 0.7, Winter = 0.85 | 0.85 | 0.7 |

Interior Shading options and arguments that vary for each option

</div>

For the argument definitions, see Table “The ResStock argument definitions set in the Interior Shading characteristic”. See the OpenStudio-HPXML [Windows](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html#hpxml-windows) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_int_shad" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `window_interior_shading_winter` | false | Frac | Double | auto | Interior shading coefficient for the winter season. 1.0 indicates no reduction in solar gain, 0.85 indicates 15% reduction, etc. |
| `window_interior_shading_summer` | false | Frac | Double | auto | Interior shading coefficient for the summer season. 1.0 indicates no reduction in solar gain, 0.85 indicates 15% reduction, etc. |

The ResStock argument definitions set in the Interior Shading characteristic

</div>

##### Distribution Assumption(s)

None.

### Infiltration

Infiltration is air leakage between the envelope and the outdoor environment. In the U.S. residential sector, it is the leading driver of heating and cooling loads (compared to, for example, heat transfer through other parts of the envelope). In ResStock, infiltration is controlled by a single input file that provides a whole-home infiltration rate.

#### Infiltration

##### Description

Total infiltration to the dwelling unit.

##### Distribution Data Source(s)

- Distributions are based on the cumulative distribution functions from the [Residential Diagnostics Database (ResDB)](http://resdb.lbl.gov/).

- Alaska-specific distribution is based on Alaska Retrofit Information System (2008 to 2022), maintained by Alaska Housing Finance Corporation.

##### Direct Conditional Dependencies

- ASHRAE IECC Climate Zone 2004

- Geometry Floor Area

- Vintage.

##### Option(s)

All infiltration options in ResStock are provided in air changes per hour (ACH) at 50 Pascals, as calculated by a blower door test. The characteristic sets the `air_leakage_leakiness_description`, `air_leakage_units`, `air_leakage_house_pressure`, `air_leakage_value`, `air_leakage_type`, and `site_shielding_of_home` ResStock arguments. For the argument definitions, see Table “The ResStock argument definitions set in the Infiltration characteristic”. See the OpenStudio-HPXML [Site](https://openstudio-hpxml.readthedocs.io/en/v1.10.0/workflow_inputs.html##hpxml-site) documentation for the available HPXML schema elements, default values, and constraints.

<div id="table:hc_arg_def_infil" data-source="3a_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `site_shielding_of_home` | false |  | Choice | auto, exposed, normal, well-shielded | Presence of nearby buildings, trees, obstructions for infiltration model. |
| `air_leakage_leakiness_description` | false |  | Choice | auto, very tight, tight, average, leaky, very leaky | Qualitative description of infiltration. If provided, the Year Built of the home is required. Either provide this input or provide a numeric air leakage value below. |
| `air_leakage_units` | true |  | Choice | ACH, CFM (cubic feet per minute), ACHnatural, CFMnatural, EffectiveLeakageArea | The unit of measure for the air leakage if providing a numeric air leakage value. |
| `air_leakage_house_pressure` | false | Pa | Double |  | The house pressure relative to outside if providing a numeric air leakage value. Required when units are ACH or CFM. |
| `air_leakage_value` | false |  | string |  | Numeric air leakage value. For 'EffectiveLeakageArea', provide value in sq. in. If provided, overrides Leakiness Description input. |
| `air_leakage_type` | false |  | Choice | auto, unit total, unit exterior only | Type of air leakage. Type of air leakage if providing a numeric air leakage value. If 'unit total', represents the total infiltration to the unit as measured by a compartmentalization test, in which case the air leakage value will be adjusted by the ratio of exterior envelope surface area to total envelope surface area. Otherwise, if 'unit exterior only', represents the infiltration to the unit from outside only as measured by a guarded test. Required when unit type is single-family attached or apartment unit. |

The ResStock argument definitions set in the Infiltration characteristic

</div>

The options of the Infiltration characteristic range between 1 ACH 50 to 50 ACH 50 and set the `air_leakage_value` ResStock argument, Table “Infiltration options and arguments that vary for each option”.

Below is a list of arguments and their values that are constant across all the options.

- `air_leakage_leakiness_description` = auto

- `air_leakage_units` = ACH

- `air_leakage_house_pressure` = 50

- `air_leakage_type` = unit total

- `site_shielding_of_home` = normal

<div id="table:hc_opt_infil" data-source="3a_ResStockInputs.tex">

| Option name | `air_leakage_value` |
|:------------|:--------------------|
| 1 ACH50     | 1                   |
| 2 ACH50     | 2                   |
| 3 ACH50     | 3                   |
| 4 ACH50     | 4                   |
| 5 ACH50     | 5                   |
| 6 ACH50     | 6                   |
| 7 ACH50     | 7                   |
| 8 ACH50     | 8                   |
| 10 ACH50    | 10                  |
| 15 ACH50    | 15                  |
| 20 ACH50    | 20                  |
| 25 ACH50    | 25                  |
| 30 ACH50    | 30                  |
| 40 ACH50    | 40                  |
| 50 ACH50    | 50                  |

Infiltration options and arguments that vary for each option

</div>

##### Distribution Assumption(s)

- All ACH50 are based on Single-Family Detached blower door tests.

- Climate zones that are copied: 2A to 1A, 6A to 7A, and 6B to 7B.

- Vintage bins that are copied: 2000s to 2010s, 1950s to 1940s, 1950s to \<1940s.

- Homes are assumed to not be Weatherization Assistance Program qualified and not ENERGY STAR certified.

- Climate zones 7AK and 8AK are averages of 6A and 6B.

- ResStock models multi-family and SFA units with the unit total air leakage type. The unit total air leakage assume that some of the sampled ACH50 value goes to neighboring units. The model infiltration value to the exterior is a smaller infiltration value that what is sampled and is adjusted by the ratio of exterior envelope surface area to total envelope surface area. The modeled infiltration to the exterior is reported in the results.

- For Alaska, we are using a field in ARIS that lumps multifamily 2-4 units and multifamily 5+ units buildings together. Data from the American Community Survey are used to distribute proportionally between these two building types.

- For Alaska, Infiltration ACH50 values are calculated based on CFM50 from blower door test and estimated volume of the home.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-Bianchi2021" class="csl-entry">

Bianchi, Carlo, and Anthony Fontanini. 2021. *<span class="nocase">TMY3 Weather Data for ComStock and ResStock</span>*. <https://doi.org/10.7799/1756695>.

</div>

<div id="ref-BigLadderSoftware2015" class="csl-entry">

Big Ladder Software. 2015. *EnergyPlus Weather File (EPW) Data Dictionary*. <https://bigladdersoftware.com/epx/docs/8-3/auxiliary-programs/energyplus-weather-file-epw-data-dictionary.html>.

</div>

<div id="ref-Brown2019" class="csl-entry">

Brown, M., W. Cole, K. Eurek, et al. 2020. *Regional Energy Deployment System (ReEDS) Model Documentation: Version 2019*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy20osti/74111.pdf>.

</div>

<div id="ref-Gagnon2025" class="csl-entry">

Gagnon, Pieter, {Pedro Andres} {Sanchez Perez}, Julian Florez, James Morris, Marck {Llerena Velasquez}, and Jordan Eisenman. 2025. *Cambium 2024 Scenario Descriptions and Documentation*. Other. <https://doi.org/10.2172/2558937>.

</div>

<div id="ref-Nettleton2012" class="csl-entry">

Nettleton, G, and J Edwards. 2012. *Data Collection-Data Characterization Summary*. NorthernSTAR Building America Partnership, Building Technologies Program, U.S. Department of Energy.

</div>

<div id="ref-Ritschard1992" class="csl-entry">

Ritschard, R. L., J. W. Hanford, and A. O. Sezgen. 1992. *<span class="nocase">Single family heating and cooling requirements: Assumptions, methods, and summary results</span>*. Lawrence Berkeley Laboratory. <https://www.osti.gov/biblio/7243112>.

</div>

<div id="ref-nsrdb" class="csl-entry">

Sengupta, M., Y. Xie, A. Lopez, A. Habte, G. Maclaurin, and J. Shelby. 2018. “The National Solar Radiation Data Base (NSRDB).” *Renewable and Sustainable Energy Reviews*. <https://www.sciencedirect.com/science/article/pii/S136403211830087X>.

</div>

<div id="ref-Wilcox2008" class="csl-entry">

Wilcox, S., and W. Marion. 2008. *<span class="nocase">Users Manual for TMY3 Data Sets</span>*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy08osti/43156.pdf>.

</div>

<div id="ref-Wilson2014" class="csl-entry">

Wilson, E., C. Engebrecht Metzger, S. Horowitz, and R. Hendron. 2014. *2014 Building America House Simulation Protocols*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy14osti/60988.pdf>.

</div>

<div id="ref-Wilson2022" class="csl-entry">

Wilson, Eric, Andrew Parker, Anthony Fontanini, et al. 2022. *<span class="nocase">End-Use Load Profiles for the U.S. Building Stock: Methodology and Results of Model Calibration, Validation, and Uncertainty Quantification</span>*. National Renewable Energy Laboratory (NREL). <https://doi.org/10.2172/1854582>.

</div>

<div id="ref-Xing2014" class="csl-entry">

Xing, Lu. 2014. “<span class="nocase">Estimations of undisturbed ground temperatures using numerical and analytical modeling</span>.” PhD thesis, Oklahoma State University. <https://shareok.org/bitstream/handle/11244/15208/Xing_okstate_0664D_13659.pdf;jsessionid=B5F9178909D3631F0CCE74C1AA4F033D?sequence=1>.

</div>

</div>

[^1]: The Subarctic climate zone is not shown and is only found in Alaska.

[^2]: In review of the TMY3 data, we have identified some outliers in the initially published TMY3 data (e.g., erroneous temperature spikes). We have corrected those for ResStock use and published our corrected versions (Bianchi and Fontanini 2021).

[^3]: Occasionally nearby stations are used if data are missing from the target weather station.
