<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_5_envelope.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_5_envelope.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0a2f61f | corpus_path: technical_reference/documentation/reference_doc/4_5_envelope.md | section: Roof | lines: 265-300 -->
## Roof

### Roof Construction Type

First, we reviewed the general types of roof construction methods that could be represented. The three general roof types commonly used in commercial building energy codes were chosen because they cover the most common roof construction types and can be linked to nominal thermal characteristics. The definitions of these types from (ASHRAE 2010) are as follows:

- **Roof with insulation entirely above deck (IEAD)**: A roof that has all insulation installed above (outside of) the roof structure and that is continuous (i.e., uninterrupted by framing members).

- **Metal building roof**: A roof that is constructed with a metal, structural weathering surface; has no ventilated cavity; and has the insulation entirely below deck (i.e., does not include composite concrete and metal deck construction or a roof framing system that is separated from the superstructure by a wood substrate). In addition, the roof structure consists of one or more of the following configurations: (a) metal roofing in direct contact with the steel framing members, (b) metal roofing separated from the steel framing members by insulation, or (c) insulated metal roofing panels installed as described in a or b.

- **Attic and other roof**: All other roofs, including roofs with insulation entirely below (inside of) the roof structure (e.g., attics, cathedral ceilings, and single-rafter ceilings); roofs with insulation both above and below the roof structure; and roofs without insulation (excluding metal building roofs).

The analysis of roof properties in (U.S. Energy Information Administration 2012), shown in Figure “Weighted floor area by roof tilt and attic presence.”, indicates that about 90% of the commercial floor space covered by ComStock has flat or shallow pitch roofs, and that the large majority of the buildings with flat or shallow pitch roofs do not have attic space. Given these factors and the complexity associated with modeling the geometry of pitched roofs, we decided to model the entire stock as having flat roofs.

<figure id="fig:cbecs_floor_area_by_roof_tilt_and_attic_presence" data-latex-placement="h">
<img src="figures/cbecs_floor_area_by_roof_tilt_and_attic_presence.png" />
<figcaption>Weighted floor area by roof tilt and attic presence.</figcaption>
</figure>

No data sources for roof construction type were found. For buildings outside of California, a single roof construction type was chosen for each building type. As shown in Table “Roof Construction Types”, most buildings are assumed to use IEAD roofs, which is consistent with the assumption of flat roofs. For buildings in California, the construction types from the DEER prototype buildings were used (California Public Utilities Commission 2021).

### Roof System Turnover Rate

As described in Section “Building System Turnover and Effective Useful Life”, some building systems, including roofs, are assumed to be replaced over the lifespan of the building. Typically, for roofs, the structural elements are maintained, while the roof membrane and insulation are replaced. As noted in Section “Building System Turnover and Effective Useful Life”, the EUL for roofs was assumed to be 200 years, which means that most buildings are modeled with the roof insulation they were built with. Once the roof type probabilities and distribution of building types, sizes, and vintages are carried through the sampling process and simulations are created, the distribution of energy code levels can be reviewed. As shown in Figure “Weighted floor area by energy code followed during last roof replacement.”, because the majority of the building stock is older, and roof systems are replaced at a low rate, most of the building floor area is assumed to have roofs that follow the oldest energy codes.

<figure id="fig:weighted_floor_area_by_energy_code_roofs" data-latex-placement="h">
<img src="figures/weighted_floor_area_by_energy_code_roofs.png" />
<figcaption>Weighted floor area by energy code followed during last roof replacement.</figcaption>
</figure>

### Roof Thermal Performance

We did not find any data sources that contained the thermal performance (U-Value/R-Value) of roofs in the commercial building stock. This is likely because surveys would need to either find building plans, which can be difficult or impossible for older buildings, or disassemble part of the structure to look inside the roofs, which building owners are unlikely to allow. To account for the lack of data, we estimated roof thermal performance based on an estimate of the energy code followed when the roof was last replaced. Section “Energy Code” describes how the energy code was determined. The thermal performance of roofs for each energy code varies based on climate zone and construction type, as shown in Tables “Roof Assembly Thermal Performance (Outside California)” and “Roof Assembly Thermal Performance (Inside California)”. While these thermal performance values do include the thermal bridging inherent in the clear field roof, they do not include thermal bridging at parapets, skylight curbs, or roof penetrations for HVAC systems. These additional thermal bridges are expected to lower the overall thermal performance of the roof assembly.

As previously described, most of the building stock’s roofs are assumed to be older. Therefore, the thermal performance assumptions for older vintages have a much higher impact on the overall heating and cooling demand than the assumptions for newer vintages. The ComStock DOE Ref Pre-1980 assumptions, taken from (Deru et al. 2011), are originally from a study of only offices (Briggs et al. 1987). Unfortunately, this study no longer appears to be available. Following the methodology in (Deru et al. 2011), these values are used for all roof construction types and all building types.

