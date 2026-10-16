<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_PV with Roof Insulation.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/2036a73dc9b7a5dccb8b62fe835cdcbc777175fa/assets/files/ComStock%20Measure%20Doc_PV%20with%20Roof%20Insulation.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_PV%20with%20Roof%20Insulation.pdf | corpus_version: comstock_amy2018_2025_release_3-v3 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_PV with Roof Insulation.md | section: 1 Introduction | lines: 161-188 -->
## 1 Introduction

Photovoltaics (PV) are an energy generation technology that has widespread adoption. The cost of panels has come down while efficiency has increased [2]. State-of-the-art modules are approaching nearly 25% efficiency, compared to less than 10% efficiency in the 1980s [3].

Despite increased overall PV adoption, commercial buildings still use PV at relatively low rates. According to the 2018 Commercial Buildings Energy Consumption Survey (CBECS), fewer than 2% of commercial buildings have on-site PV [4]. This statistic may have increased since the survey was conducted.

Commercial buildings generally have flat roofs, with fewer than 10% of the building stock having a pitched roof [4]. Ballasted PV panels can be placed on flat roofs at the locationdependent preferred tilt and azimuth angle to maximize energy and/or cost reduction. Pitched roofs generally require a system that mounts onto the roof; however, these systems are not modeled in ComStock. Some commercial buildings use a portion of the roof for heating, ventilating, and air conditioning (HVAC) equipment, so PV panels would have to work around these constraints. Rooftops can also be used for occupant space, such as patios, so these areas would need to be avoided as well. Additionally, with any configuration, proper access pathways and fire escapes need to be maintained. Thus, although there is notable commercial building rooftop area available, some of these areas would not be applicable for PV panels.

Roof insulation mitigates heat loss through a building's exterior roof surfaces. For the purposes of this document, a roof is defined as sky-facing exterior horizontal surfaces sloped within 60 degrees of sky-facing horizontal. The most common roof construction methods are covered in [5] and can be aligned to nominal thermal characteristics:

1. Roof with insulation entirely above deck (IEAD) refers to a roof with all insulation:
1. Installed above (outside of) the roof structure
2. Continuous (i.e., uninterrupted by framing members)
2. Metal building roof refers to a roof that:
1. Is constructed with a metal, structural, weathering surface
2. Has no ventilated cavity
3. Has the insulation entirely below deck (i.e., does not include composite concrete and metal deck construction nor a roof framing system that is separated from the superstructure by a wood substrate) and whose structure consists of one or more of the following configurations:
1. Metal roofing in direct contact with the steel framing members
2. Metal roofing separated from the steel framing members
3. Insulated metal roofing panels installed as described in subitems (a) or (b).
3. Attic and other roofs refers to all other roofs, including roofs with insulation entirely below (inside of) the roof structure (i.e., attics, cathedral ceilings, and single-rafter ceilings), roofs with insulation both above and below the roof structure, and roofs without insulation but excluding metal building roofs.

1. Single-rafter roof is a subcategory of attic roofs where the roof above and the ceiling below are both attached to the same wood rafter, and insulation is located in the space between these wood rafters.

Roof insulation is applied to many existing commercial buildings. Continuous insulation is included as a requirement for all climate zones with roofs that have insulation entirely above deck according to ASHRAE 90.1 2019 [5], noting that many existing roof systems were installed according to much older energy code requirements (or none at all) due to the long turnover rate of architectural elements. Problems with insulation performance tend to stem from improper water management design or installation; for this measure, and for the ComStock baseline models in general, those issues are assumed to be handled properly.

This study combines two existing ComStock measure scenarios as a package to understand the combined impact: PV with 40% rooftop coverage and improved rooftop insulation. This measure package was evaluated because roof insulation upgrades and PV upgrades can often be coordinated during planned roof replacement or renovation projects. For a more comprehensive review of the individual measure scenarios comprising this package, reference their individual documentation.

