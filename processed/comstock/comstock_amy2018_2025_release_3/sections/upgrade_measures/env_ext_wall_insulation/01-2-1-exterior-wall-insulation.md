<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_ext_wall_insulation.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_ext_wall_insulation.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_ext_wall_insulation.html | corpus_version: b5faf42 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_ext_wall_insulation.md | section: 2.1  Exterior Wall Insulation | lines: 48-163 -->
## 2.1  Exterior Wall Insulation

Exterior insulation can be purchased in a range of materials and thicknesses. Therefore, it is possible to achieve a range of thermal performance. Because of the differences in climate across the United States, it is not desirable to have a single performance value; warmer climates generally derive less incremental benefit from insulation than colder climates because the temperature differential is lower in warmer climates. In practice, existing structure, cladding, and window penetrations will likely impact decisions.

As starting point for target assembly performance, the values from the ASHRAE *Achieving Zero Energy: Advanced Energy Design Guide for Small to Medium Office Buildings* \[3\] were reviewed, as shown in Table 2.

Table 2. AEDG Overall Assembly Performance Characteristics by Climate Zone

| **Climate Zone** | **CZ1** | **CZ2** | **CZ3** | **CZ4** | **CZ5** | **CZ6** | **CZ7** | **CZ8** |
|-|-|-|-|-|-|-|-|-|
| **R-Value (hr-ft2-F/Btu)** | 13 | 13 | 16 | 16 | 19 | 21 | 21 | 29 |

We compared the existing wall thermal performance assumptions in ComStock with the Advanced Energy Design Guide (AEDG) recommendations, and calculated a simplistic estimate of the thickness of XPS insulation needed to bring the total assembly to the AEDG recommended thermal performance, as shown in Table 3. In a detailed calculation, because the thermal bridging would be reduced by the application of exterior continuous insulation, the performance increase would be slightly higher than what is shown. Note that the table is sparse for some vintages, either because those vintages are so uncommon as to be nonexistent in the model in a given climate zone, or in the case of the CA vintages because CA does not include all ASHRAE climate zones.

Also, the ComStock team is aware that the baseline wall performance characteristics of the ComStock DOE Ref 1980-2004 vintages are inconsistent with the earlier (ComStock DOE Ref Pre-1980) and later (ComStock 90.1-2004) vintages. This is part of the baseline ComStock model and will need to be addressed independently of the exterior wall insulation measure.

Table 3. Comparison of ComStock Existing Opaque Wall Thermal Performance to ASHRAE Small and Medium Office Zero Energy AEDG Performance Targets by Climate Zone

<!-- table recovered from ./media/09c5c0be-0aa4-46b1-a2be-b4866aad1f4d.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_ext_wall_insulation.yaml
     method: vision-transcription -->

**Frame walls: ComStock Baseline R-value* by climate zone**

| Energy Code (R-value, ft2*F*hr/Btu) | CZ1 | CZ2 | CZ3 | CZ4 | CZ5 | CZ6 | CZ7 | CZ8 |
|---|---|---|---|---|---|---|---|---|
| AEDG Recommendation** | 13 | 13 | 16 | 16 | 19 | 21 | 21 | 29 |
| ComStock DOE Ref Pre-1980 | 4 | 4 | 4 | 6 | 6 | 7 | 7 | 8 |
| ComStock DOE Ref 1980-2004 | 13 | 5 | 6 | 10 | 11 | 15 | 17 | 22 |
| ComStock 90.1-2004 | 9 | 12 | 7 | 8 | 9 | 10 | 14 |  |
| ComStock 90.1-2007 | 10 | 7 | 9 | 10 | 12 | 13 | 13 | 9 |
| ComStock 90.1-2010 | 17 | 8 | 10 | 11 | 12 | 13 |  |  |
| ComStock 90.1-2013 |  | 9 | 9 | 11 | 14 | 14 |  |  |
| ComStock DEER Pre-1975 |  | 6 | 5 | 6 | 6 | 6 |  |  |
| ComStock DEER 1985 |  | 7 | 6 | 6 | 6 |  |  |  |
| ComStock DEER 1996 |  | 6 | 6 | 6 | 5 | 18 |  |  |
| ComStock DEER 2003 |  | 8 | 6 | 6 | 4 |  |  |  |
| ComStock DEER 2007 |  | 6 | 6 | 4 | 10 |  |  |  |
| ComStock DEER 2011 |  | 11 | 8 | 9 |  |  |  |  |
| ComStock DEER 2014 |  | 6 | 9 | 5 |  |  |  |  |
| ComStock DEER 2015 |  |  | 8 | 5 | 7 |  |  |  |
| ComStock DEER 2017 |  | 6 | 8 | 5 |  |  |  |  |

**Frame walls: inches of XPS to meet the AEDG Recommendation**

| Energy Code (inches of XPS) | CZ1 | CZ2 | CZ3 | CZ4 | CZ5 | CZ6 | CZ7 | CZ8 |
|---|---|---|---|---|---|---|---|---|
| AEDG Recommendation** |  |  |  |  |  |  |  |  |
| ComStock DOE Ref Pre-1980 | 1.7 | 1.7 | 2.2 | 2.2 | 2.6 | 2.9 | 2.8 | 4.1 |
| ComStock DOE Ref 1980-2004 | 0.0 | 1.6 | 1.9 | 1.2 | 1.6 | 1.3 | 0.9 | 1.3 |
| ComStock 90.1-2004 | 0.7 | 0.3 | 1.7 | 1.8 | 2.0 | 2.2 | 1.4 |  |
| ComStock 90.1-2007 | 0.5 | 1.2 | 1.4 | 1.2 | 1.5 | 1.6 | 1.7 | 3.9 |
| ComStock 90.1-2010 | -0.8 | 1.1 | 1.1 | 1.1 | 1.4 | 1.7 |  |  |
| ComStock 90.1-2013 |  | 0.9 | 1.3 | 1.0 | 1.1 | 1.4 |  |  |
| ComStock DEER Pre-1975 |  | 1.4 | 2.0 | 2.1 | 2.7 | 3.0 |  |  |
| ComStock DEER 1985 |  | 1.3 | 1.9 | 2.1 | 2.6 |  |  |  |
| ComStock DEER 1996 |  | 1.4 | 1.9 | 2.0 | 2.8 | 0.7 |  |  |
| ComStock DEER 2003 |  | 1.0 | 1.9 | 2.1 | 3.0 |  |  |  |
| ComStock DEER 2007 |  | 1.3 | 1.9 | 2.4 | 1.8 |  |  |  |
| ComStock DEER 2011 |  | 0.5 | 1.5 | 1.5 |  |  |  |  |
| ComStock DEER 2014 |  | 1.4 | 1.3 | 2.4 |  |  |  |  |
| ComStock DEER 2015 |  |  | 1.5 | 2.4 | 2.5 |  |  |  |
| ComStock DEER 2017 |  | 1.4 | 1.5 | 2.4 |  |  |  |  |

**Mass walls: ComStock Baseline R-value by climate zone**

| Energy Code (R-value, ft2*F*hr/Btu) | CZ1 | CZ2 | CZ3 | CZ4 | CZ5 | CZ6 | CZ7 | CZ8 |
|---|---|---|---|---|---|---|---|---|
| AEDG Recommendation** | 9 | 10 | 13 | 14 | 17 | 19 | 19 | 26 |
| ComStock DOE Ref Pre-1980 | 4 | 4 | 4 | 6 | 6 | 7 | 7 | 8 |
| ComStock DOE Ref 1980-2004 | 13 | 5 | 6 | 10 | 11 | 15 | 17 | 22 |
| ComStock 90.1-2004 | 9 | 12 | 7 | 8 | 9 | 10 |  | 16 |
| ComStock 90.1-2007 | 10 | 7 | 9 | 11 | 12 | 13 | 14 | 14 |
| ComStock 90.1-2010 | 14 | 8 | 10 | 11 | 12 | 13 |  |  |
| ComStock 90.1-2013 | 13 | 8 | 10 | 11 | 14 | 16 |  |  |
| ComStock DEER Pre-1975 |  | 5 | 5 | 6 | 6 |  |  |  |
| ComStock DEER 1985 |  | 6 | 6 | 7 | 8 |  |  |  |
| ComStock DEER 1996 |  | 4 | 7 | 8 | 4 |  |  |  |
| ComStock DEER 2003 |  |  | 6 | 6 | 4 | 4 |  |  |
| ComStock DEER 2007 |  | 4 | 6 | 13 | 13 |  |  |  |
| ComStock DEER 2011 |  | 6 | 8 | 7 | 6 |  |  |  |
| ComStock DEER 2014 |  |  | 9 |  |  |  |  |  |
| ComStock DEER 2015 |  |  | 10 | 18 | 6 |  |  |  |
| ComStock DEER 2017 |  |  | 9 | 5 |  |  |  |  |

**Mass walls: inches of XPS to meet the AEDG Recommendation**

| Energy Code (inches of XPS) | CZ1 | CZ2 | CZ3 | CZ4 | CZ5 | CZ6 | CZ7 | CZ8 |
|---|---|---|---|---|---|---|---|---|
| AEDG Recommendation** |  |  |  |  |  |  |  |  |
| ComStock DOE Ref Pre-1980 | 1.0 | 1.2 | 1.8 | 1.8 | 2.2 | 2.5 | 2.4 | 3.5 |
| ComStock DOE Ref 1980-2004 | -0.7 | 1.0 | 1.5 | 0.9 | 1.2 | 0.9 | 0.5 | 0.7 |
| ComStock 90.1-2004 | 0.0 | -0.4 | 1.3 | 1.4 | 1.6 | 1.9 |  | 2.0 |
| ComStock 90.1-2007 | -0.1 | 0.6 | 0.9 | 0.7 | 1.1 | 1.3 | 1.0 | 2.3 |
| ComStock 90.1-2010 | -0.9 | 0.5 | 0.7 | 0.7 | 1.1 | 1.3 |  |  |
| ComStock 90.1-2013 | -0.8 | 0.4 | 0.7 | 0.7 | 0.7 | 0.6 |  |  |
| ComStock DEER Pre-1975 |  | 1.1 | 1.6 | 1.7 | 2.2 |  |  |  |
| ComStock DEER 1985 |  | 0.9 | 1.4 | 1.4 | 1.9 |  |  |  |
| ComStock DEER 1996 |  | 1.2 | 1.4 | 1.3 | 2.6 |  |  |  |
| ComStock DEER 2003 |  |  | 1.4 | 1.7 | 2.6 | 3.0 |  |  |
| ComStock DEER 2007 |  | 1.2 | 1.4 | 0.3 | 0.8 |  |  |  |
| ComStock DEER 2011 |  | 0.8 | 1.1 | 1.4 | 2.2 |  |  |  |
| ComStock DEER 2014 |  |  | 0.8 |  |  |  |  |  |
| ComStock DEER 2015 |  |  | 0.7 | -0.6 | 2.2 |  |  |  |
| ComStock DEER 2017 |  |  | 0.8 | 2.0 |  |  |  |  |

*Frame walls are building-count-weighted average of steel-framed and wood-framed walls

**From ASHRAE Advanced Eenrgy Design Guide for Small to Medium Office Buildings - Achieving Zero Energy, Table 5-4

An argument can be made for higher levels of insulation when this measure is combined with infiltration reduction and other envelope and ventilation load reduction improvements. However, on their own, insulation levels above the AEDG recommended values seem unlikely to be cost-effective.

# 3.  ComStock Baseline Approach

Exterior wall properties are assigned to ComStock models by wall construction type and energy code. The following sections outline the approach and data sources for determining ComStock wall construction type, energy code, and thermal performance.

