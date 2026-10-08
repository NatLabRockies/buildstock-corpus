<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_roof_insulation.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_roof_insulation.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_roof_insulation.html | corpus_version: b5faf42 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_roof_insulation.md | section: 1.2.  Measure Summary | lines: 30-284 -->
## 1.2.  Measure Summary

| **Measure Title**  | Roof Insulation                                                                                                                         |
| **Measure Definition** | This measure adds additional roof insulation to the meet the R-values specified in the *Advanced Energy Design Guide* (AEDG) by climate zone. |
| **Applicability**      | Models with roof insulation R-values that are below those specified in the AEDG for the respective climate zone.                              |
| **Not Applicable**     | Models with roof insulation R-values that already meet or exceed the R-values specified in the AEDG will not be impacted.                     |
| **Release**            | EUSS 2023 Release 1                                                                                                                           |

# 2.  Technology Summary

Roof insulation mitigates heat loss through a building’s exterior roof surfaces. For the purposes of this document, a roof is defined as sky-facing exterior horizontal surfaces sloped within 60 degrees of sky-facing horizontal. [1] covers the most common roof construction methods and can be lined to nominal thermal characteristics:

1.  **Roof with insulation entirely above deck (IEAD)** refers to a roof with all insulation:
    1.  Installed above (outside of) the roof structure; and
    2.  Continuous (i.e., uninterrupted by framing members).
2.  **Metal building roof** refers to a roof that:
    1.  Is constructed with a metal, structural, weathering surface;
    2.  Has no ventilated cavity; and
    3.  Has the insulation entirely below deck (i.e., does not include composite concrete and metal deck construction nor a roof framing system that is separated from the superstructure by a wood substrate) and whose structure consists of one or more of the following configurations:
        1.  Metal roofing in direct contact with the steel framing members;
        2.  Metal roofing separated from the steel framing members;
        3.  Insulated metal roofing panels installed as described in subitems (a) or (b).
3.  **Attic and other roofs** refers to all other roofs, including roofs with insulation entirely below (inside of) the roof structure (i.e., attics, cathedral ceilings, and single-rafter ceilings), roofs with insulation both above and below the roof structure, and roofs without insulation but excluding metal building roofs.
    1.  **Single-rafter roof** is a subcategory of attic roofs where the roof above and the ceiling below are both attached to the same wood rafter and where insulation is located in the space between these wood rafters.

Roof insulation is applied to many existing commercial buildings. Continuous insulation is included as a requirement for all climate zones with roofs that have insulation entirely above deck according to ASHRAE 90.1 2019 [1], noting that many existing roof systems were installed according to much older energy code requirements (or none at all) due to the long turnover rate of architectural elements. Problems with insulation performance tend to stem from improper water management design or installation; for this measure, and for the ComStock baseline models in general, those issues are assumed to be handled properly.

# 3.  ComStock Baseline Approach

An analysis of roof properties from the U.S. Energy Information Administration’s 2018 Commercial Buildings Energy Consumption Survey (CBECS), shown in Figure 1, indicates that about 85% of ComStock’s commercial buildings by floor area have flat or shallow pitch roofs, and we know that the large majority of the buildings with flat or shallow pitch roofs do not have attic space. Given these factors and the complexity associated with modeling the geometry of pitched roofs, an assumption was made that 85% of roof surfaces in ComStock are flat, and we therefore model the entire stock as having flat roofs.

![Chart, bar chart Description automatically generated](media/49b7c87775b756b227d60e9c9ee4d402.png)

Figure 1. 2018 CBECS Report: Roof tilt by total floor space

No data sources for roof construction type were found in the CBECS report. For buildings outside of California, a single roof construction type was chosen for each building type. As shown in Table 1, most buildings are assumed to use IEAD roofs, which is consistent with the assumption of flat roofs. For buildings in California, we used the construction types from the California Public Utilities Commission’s Database of Energy Efficiency Resources (DEER) prototype buildings.

Table 1. Roof Construction Types

<!-- table recovered from media/1d093dd8864b636f6dd02a3d70bcc1c1.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_roof_insulation.yaml
     method: vision-transcription -->

| Building Type | DOE Ref and 90.1: Construction Type | DOE Ref and 90.1: Building Category for Exterior Roofs | DEER (CA ONLY): Construction Type | DEER (CA ONLY): Building Category for Exterior Roofs |
|---|---|---|---|---|
| Full-Service Restaurant | IEAD | Nonresidential | Wood Framed | Nonresidential |
| Hospital | IEAD | Nonresidential | Mass | Nonresidential |
| Large Hotel | IEAD | Residential | IEAD | Residential |
| Large Office | IEAD | Nonresidential | Mass | Nonresidential |
| Medium Office | IEAD | Nonresidential | Mass | Nonresidential |
| Outpatient | IEAD | Nonresidential | Mass | Nonresidential |
| Primary School | IEAD | Nonresidential | Wood Framed | Nonresidential |
| Quick-Service Restaurant | IEAD | Nonresidential | Wood Framed | Nonresidential |
| Retail | IEAD | Nonresidential | IEAD | Nonresidential |
| Secondary School | IEAD | Nonresidential | Wood Framed | Nonresidential |
| Small Hotel | IEAD | Residential | Wood Framed | Residential |
| Small Office | IEAD | Nonresidential | Wood Framed | Nonresidential |
| Strip Mall | IEAD | Nonresidential | Wood Framed | Nonresidential |
| Warehouse | Metal* | Semiheated* | Wood Framed | Nonresidential |

\*Except pre-1980, which assumes IEAD and nonresidential for all years

**Roof System Turnover Rate**

Some building systems, including roofs, are assumed to be replaced over the lifespan of the building. Typically, for roofs, the structural elements of the roof would be maintained, while the roof membrane and insulation would be replaced. In ComStock, the expected useful life for roofs is assumed to be 200 years, which means that most buildings are modeled with the roof insulation they were built with. Once the roof type probabilities and distribution of building types, sizes, and vintages are carried through the sampling process and simulations are created, the distribution of energy code levels can be reviewed. As shown in Figure 2, because most of the building stock is older, and because of the low rate of replacement of roof systems, most of the building floor area is assumed to have roofs that follow the oldest energy codes.

![Chart Description automatically generated with medium confidence](media/a823cf89012a03ca74b6c5437393a988.png)

Figure 2. Floor area by energy code followed during last roof replacement

**Roof Thermal Performance**

No data sources were found that contained thermal performance (U-value/R-value) of roofs in the commercial building stock, likely because surveys would need to either find building plans, which can be difficult or impossible for older buildings, or disassemble part of the structure to look inside the roofs, which building owners are unlikely to allow. To account for the lack of data, we estimated roof thermal performance based on an estimate of the energy code followed when the roof was last replaced. For now, to determine the proper energy code we assume that all building systems meet the requirements of the energy code that was in force in their location, both when originally constructed and as buildings systems were replaced over time [2]. The thermal performance of roofs for each energy code varies based on climate zone and construction type, as shown in Table 2, Table 3, and Table 4. Note that while these thermal performance values do include the thermal bridging inherent in the clear field roof, they do not include thermal bridging at parapets, skylight curbs, or roof penetrations for HVAC systems. These additional thermal bridges would be expected to lower the overall thermal performance of the roof assembly.

Table 2. ASHRAE 90.1 IEAD Nonresidential Roof R-Value (c.i.)

<!-- table recovered from media/18037d38ef99b57c02dadc77d31718da.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_roof_insulation.yaml
     method: vision-transcription -->

| ComStock Energy Code | 1A | 1B | 2A | 2B | 3A | 3B | 3C | 4A | 4B | 4C | 5A | 5B | 5C | 6A | 6B | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DOE Ref Pre-1980 | 10 | - | 10 | 10 | 10 | 10 | 10 | 12 | 11 | 12 | 14 | 13 | 13 | 17 | 17 | 17 | 17 |
| DOE Ref 1980-2004 | 14 | - | 15 | 22 | 14 | 21 | 11 | 17 | 17 | 16 | 19 | 20 | 20 | 22 | 20 | 24 | 31 |
| 90.1-2004 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 21 |
| 90.1-2007 | 16 | 16 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 |
| 90.1-2010 | 16 | 16 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 |
| 90.1-2013 | 21 | 21 | 26 | 26 | 26 | 26 | 26 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 36 | 36 |
| 90.1-2016 | 21 | 21 | 26 | 26 | 26 | 26 | 26 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 36 | 36 |
| 90.1-2019 | 21 | 21 | 26 | 26 | 26 | 26 | 26 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 36 | 36 |

Table 3. ASHRAE 90.1 IEAD Residential Roof R-Value (c.i.)

<!-- table recovered from media/966c33bf3e0e85644df23434a31aaf2e.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_roof_insulation.yaml
     method: vision-transcription -->

| ComStock Energy Code | 1A | 1B |
|---|---|---|
| 90.1-2010 | 21 | 21 |
| 90.1-2013 | 26 | 26 |
| 90.1-2016 | 26 | 26 |
| 90.1-2019 | 26 | 26 |

In general, it appears that the only difference between ASHRAE 90.1 Nonresidential and Residential IEAD U-values are within climate zone 1 (A, B).

Table 4. DEER Roof R-Values (c.i.)

<!-- table recovered from media/5b3aa079ea5a972fa681e72f08e872af.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_roof_insulation.yaml
     method: vision-transcription -->

**DEER Wood-Framed Nonresidential**

| ComStock Energy Code | T24-CEC 1 | T24-CEC 2 | T24-CEC 3 | T24-CEC 4 | T24-CEC 5 | T24-CEC 6 | T24-CEC 7 | T24-CEC 8 | T24-CEC 9 | T24-CEC 10 | T24-CEC 11 | T24-CEC 12 | T24-CEC 13 | T24-CEC 15 | T24-CEC 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DEER Pre-1975 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| DEER 1985 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| DEER 1996 | 18 | 18 | 18 | 18 | 18 | 13 | 13 | 13 | 13 | 13 | 18 | 18 | 18 | 18 | 18 |
| DEER 2003 | - | 18 | 18 | 18 | 18 | 13 | 13 | 13 | 13 | 18 | 18 | 18 | 18 | 18 | - |
| DEER 2007 | - | 20 | 20 | 20 | 20 | 14 | 14 | 14 | 14 | 20 | 20 | 20 | 20 | 20 | - |
| DEER 2011 | - | 26 | 26 | 26 | 21 | 14 | 16 | 16 | 26 | 26 | 26 | 26 | 26 | - | - |
| DEER 2014 | - | 26 | 26 | 26 | 21 |  | 16 | 16 | 26 | 26 | 26 | 26 | 26 | - | - |
| DEER 2015 | - | 26 | 26 | 26 | 21 | 14 | 16 | 16 | 26 | 26 | 26 | 26 | 26 | - | - |
| DEER 2017 | - | 26 | 26 | 26 | 21 | 14 | 16 | 16 | 26 | 26 | 26 | 26 | 26 | - | - |

**DEER Wood-Framed Residential**

| ComStock Energy Code | T24-CEC 1 | T24-CEC 2 | T24-CEC 3 | T24-CEC 4 | T24-CEC 5 | T24-CEC 6 | T24-CEC 7 | T24-CEC 8 | T24-CEC 9 | T24-CEC 10 | T24-CEC 11 | T24-CEC 12 | T24-CEC 13 | T24-CEC 15 | T24-CEC 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DEER Pre-1975 | 13 | 13 | - | 13 | 13 | 13 | 13 | 13 | 13 | 13 | 13 | 13 | 13 | 13 | 13 |
| DEER 1985 | - | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | - | - |
| DEER 1996 | - | 20 | 20 | 20 | 20 | 20 | 20 | 20 | 20 | 20 | - | 28 | 28 | - | - |
| DEER 2003 | - | - | 20 | 20 | - | - | - | - | 20 | 28 | - | 28 | 28 | - | - |
| DEER 2007 | - | 29 | 20 | 20 | - | - | - | - | - | 29 | - | 29 | - | - | - |
| DEER 2011 | 30 | 36 | 26 | - | - | 26 | - | - | - | 36 | - | 36 | - | - | - |
| DEER 2014 | - | - | - | - | - | - | - | - |  | - | - | 36 | - | - | - |
| DEER 2015 | - | - | - | - | - | - | - | - | 36 | 36 | - | 36 | - | - | - |
| DEER 2017 | - | - | - | 36 | - | 26 | - | - | 36 | - | - | 36 | - | - | - |

**DEER Mass Nonresidential**

| ComStock Energy Code | T24-CEC 1 | T24-CEC 2 | T24-CEC 3 | T24-CEC 4 | T24-CEC 5 | T24-CEC 6 | T24-CEC 7 | T24-CEC 8 | T24-CEC 9 | T24-CEC 10 | T24-CEC 11 | T24-CEC 12 | T24-CEC 13 | T24-CEC 15 | T24-CEC 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DEER Pre-1975 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 |
| DEER 1985 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 |
| DEER 1996 | 18 | 18 | 18 | 18 | 18 | 13 | 13 | 13 | 13 | 13 | 18 | 18 | 18 | - | - |
| DEER 2003 | - | 18 | 18 | 18 | 18 | 13 | 13 | 13 | 13 | 18 | 18 | 18 | 18 | - | - |
| DEER 2007 | 20 | 20 | 20 | 20 | 20 | 14 | 14 | 14 | 14 | 20 | 20 | 20 | 20 | 20 | - |
| DEER 2011 | 21 | 26 | 26 | 26 | - | 14 | 16 | 16 | 26 | 26 | 26 | 26 | - | - | - |
| DEER 2014 | - | 26 | 26 | 26 | - | 14 | 16 | - | 26 | 26 | - | 26 | 26 | - | - |
| DEER 2015 | - | - | 26 | 26 | 21 | 14 | 16 | - | 26 | - | - | 26 | 26 | - | - |
| DEER 2017 | - | - | - | 26 | 21 | - | 16 | - | 26 | 26 | 26 | 26 | 26 | - | - |

**DEER IEAD Nonresidential**

| ComStock Energy Code | T24-CEC 1 | T24-CEC 2 | T24-CEC 3 | T24-CEC 4 | T24-CEC 5 | T24-CEC 6 | T24-CEC 7 | T24-CEC 8 | T24-CEC 9 | T24-CEC 10 | T24-CEC 11 | T24-CEC 12 | T24-CEC 13 | T24-CEC 15 | T24-CEC 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DEER Pre-1975 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 |
| DEER 1985 | - | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | - |
| DEER 1996 | - | 18 | 18 | 18 | 18 | 13 | 13 | 13 | 13 | 13 | 18 | 18 | 18 | - | 18 |
| DEER 2003 | - | 18 | 18 | 18 | 18 | 13 | 13 | 13 | 13 | 18 | 18 | 18 | 18 | 18 | - |
| DEER 2007 | - | 20 | 20 | 20 | 20 | 14 | 14 | 14 | 14 | 20 | 20 | 20 | 20 | 20 | 20 |
| DEER 2011 | - | 26 | 26 | 26 | 21 | 14 | 16 | 16 | 26 | 26 | 26 | 26 | 26 | 26 | 26 |
| DEER 2014 | - | 26 | 26 | 26 | 21 | 14 | 16 | 16 | 26 | 26 | 26 | 26 | 26 | - | - |
| DEER 2015 | 21 | 26 | 26 | 26 | 21 | - | 16 | - | 26 | 26 | 26 | 26 | 26 | 26 | - |
| DEER 2017 | 21 | - | 26 | 26 | 21 | 14 | 16 | - | 26 | 26 | 26 | 26 | 26 | 26 | - |

**DEER IEAD Residential**

| ComStock Energy Code | T24-CEC 1 | T24-CEC 2 | T24-CEC 3 | T24-CEC 4 | T24-CEC 5 | T24-CEC 6 | T24-CEC 7 | T24-CEC 8 | T24-CEC 9 | T24-CEC 10 | T24-CEC 11 | T24-CEC 12 | T24-CEC 13 | T24-CEC 15 | T24-CEC 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DEER Pre-1975 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | - | 16 |
| DEER 1985 | - | - | 18 | 18 | - | - | 18 | - | 18 | - | 18 | 18 | - | - | - |
| DEER 1996 | - | 18 | - | - | - | - | - | 13 | 13 | 13 | - | - | - | - | - |
| DEER 2003 | - | - | - | - | - | - | - | 13 | 13 | - | - | 18 | 18 | - | - |
| DEER 2007 | - | 20 | 20 | - | - | 14 | 14 | - | - | - | - | - | 20 | - | - |
| DEER 2011 | - | - | - | 26 | - | - | - | - | - | - | - | - | 26 | - | - |
| DEER 2014 | - | - | - | - | - | - | - | - | 26 | - | - | - | - | - | - |
| DEER 2015 | - | - | - | - | - | 14 | - | - | - | - | - | - | - | - | - |
| DEER 2017 | - | - | - | - | - | 14 | - | - | - | - | - | - | - | - | - |

As mentioned above, most of the building stock’s roofs are assumed to be older, and therefore the thermal performance assumptions for older vintages have a much higher impact on the overall heating and cooling demand than the assumptions for the newer vintages. The ComStock DOE Ref Pre-1980 assumptions are originally from the study of only offices (Briggs, Belzer, and Crawley[^1]) that unfortunately no longer appears to be available. Following the methodology in Deru et al.[^2], these values are used for all roof construction types and all building types.

[^1]: Briggs, R. S., D. B. Belzer, and D. B. Crawley. “Analysis and categorization of the office building stock. Topical report, February-September 1987” (Oct. 1987). <https://www.osti.gov/biblio/6795134>.

[^2]: Deru, M, et al. “U.S. Department of Energy Commercial Reference Building Models of the National Building Stock” (Feb. 2011). <https://doi.org/10.2172/1009264>. <https://www.osti.gov/biblio/1009264>.

Average roof assembly R-values by ComStock code year are shown in Figure 3. Note that a more recent code year alone does not always indicate a higher aversage roof R-value for ComStock. This is because certain ComStock code years can be more prevalent in certain locations, causing each code year followed to vary in terms of the proportion of each climate zone it serves. This is illustrated in Figure 4. Since climate zone is a key driver of insulation requirements, code years serving a higher prevalence of warmer climates may appear to have a lower average R-value compared to older cold years serving a higher prevalence of colder climate zones.

![A picture containing graphical user interface Description automatically generated](media/f93fbe1444b89b6541f7d5ca40fe73d0.png)

Figure 3. Average roof assembly R-value of ComStock models for each energy code followed during the last roof replacement

![A picture containing table Description automatically generated](media/6879600cec63b0bfbc890ff44f7e450c.png)

Figure 4. Climate zone floor area percentage per energy code followed during last roof replacement

# 4.  Modeling Approach

As a starting point for target assembly performance of roof insulation based on R-value, the values from the *AEDG for Small to Medium Office Buildings* [3] were reviewed, as shown in Table 5.

Table 5. Overall Target Assembly Performance Characteristics by Climate Zone per AEDG [3]

<!-- table recovered from media/0379b78f3c35327610fbdfa65e3fac94.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_roof_insulation.yaml
     method: vision-transcription -->

| Climate Zone | CZ 1 | CZ 2 | CZ 3 | CZ 4 | CZ 5 | CZ 6 | CZ 7 | CZ 8 |
|---|---|---|---|---|---|---|---|---|
| R-Value | 21 | 26 | 26 | 33 | 33 | 33 | 37 | 37 |

We compared the existing roof thermal performance assumptions in ComStock with the AEDG recommendations, and calculated a simplistic estimate of the thickness of insulation (XPS) of
R-5/inch needed to bring the total assembly to the AEDG recommended thermal performance, as shown in Table 6. In a detailed calculation, because the thermal bridging would be reduced by the application of exterior continuous insulation, the performance increase would be slightly higher than what is shown. Note that the table is sparse for some vintages, either because those vintages are so uncommon as to be nonexistent in the model in a given climate zone or absent in the case of the California vintages because California does not follow ASHRAE climate zones.

Table 6. Comparison of ComStock Existing Roof Thermal Performance to AEDG Performance Targets by Climate Zone

<!-- table recovered from media/00fe2fa136ffe4432caf0f0f462a8d81.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_roof_insulation.yaml
     method: vision-transcription -->

**ComStock Baseline R-value**

| Roof R-value / Climate Zone | 1A | 1B | 2A | 2B | 3A | 3B | 3C | 4A | 4B | 4C | 5A | 5B | 5C | 6A | 6B | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AEDG Recommendation* | 21 | 21 | 26 | 26 | 26 | 26 | 26 | 33 | 33 | 33 | 33 | 33 | 33 | 33 | 33 | 37 | 37 |
| ComStock DOE Ref Pre-1980 | 10 |  | 10 | 10 | 10 | 10 | 10 | 12 | 11 | 12 | 14 | 13 | 13 | 17 | 17 | 17 | 17 |
| ComStock DOE Ref 1980-2004 | 14 |  | 15 | 22 | 14 | 21 | 11 | 17 | 17 | 16 | 19 | 20 | 20 | 22 | 20 | 24 | 31 |
| ComStock 90.1-2004 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 21 |
| ComStock 90.1-2007 | 16 | 16 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 |
| ComStock 90.1-2010 | 16 | 16 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 |
| ComStock 90.1-2013 | 21 | 21 | 26 | 26 | 26 | 26 | 26 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 36 | 36 |
| ComStock 90.1-2016 | 21 | 21 | 26 | 26 | 26 | 26 | 26 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 36 | 36 |
| ComStock 90.1-2019 | 21 | 21 | 26 | 26 | 26 | 26 | 26 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 36 | 36 |

**Inches of XPS to Meet AEDG Recommendation (R-5/inch)**

| Roof R-value / Climate Zone | 1A | 1B | 2A | 2B | 3A | 3B | 3C | 4A | 4B | 4C | 5A | 5B | 5C | 6A | 6B | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AEDG Recommendation* |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ComStock DOE Ref Pre-1980 | 2 |  | 3 | 3 | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 |
| ComStock DOE Ref 1980-2004 | 1 |  | 2 | 1 | 2 | 1 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 1 |
| ComStock 90.1-2004 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 |
| ComStock 90.1-2007 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| ComStock 90.1-2010 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 3 |
| ComStock 90.1-2013 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ComStock 90.1-2016 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ComStock 90.1-2019 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

\*From ASHRAE Advanced Eenrgy Design Guide for Small to Medium Office Buildings - Achieving Zero Energy, Table 5-4

*Note that from 2013 forward the inches of XPS needed to meet the AEDG recommendation are zero for all climate zones. This is because the ComStock 90.1 2013, 2016, and 2019 R-values already meet the AEDG recommended value.*

Functionally, this measure increases the insulation value of roof surfaces such that the final applied insulation value meets the values shown in Table 5, skipping roof surfaces that already meet or exceed these values. To better align with how insulation is often sold, the applied thickness of additional insulation is rounded up to the nearest inch, which may cause some buildings to slightly exceed the AEDG values. The measure assumes XPS insulation with a thermal resistance of R-5/inch.

