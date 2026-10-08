<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89040.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89040.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89040.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/89040.md | section: 1  Technology Summary | lines: 203-264 -->
## 1  Technology Summary

The upgrade described in this document concerns replacing an existing heating, ventilating, and air-conditioning (HVAC) system. The upgraded system decouples ventilation from space conditioning, with ventilation handled by a DOAS and the remaining space conditioning handled by a VRF air-source heat pump system. An additional consideration in this study compared to the previous work on VRF (HR) DOAS upgrade is the allowance of up to 25% upsizing (or 125% of the original size) from equipment sized to the design cooling load for heating-dominant buildings.

Figure 1 shows the key features of the VRF system considered in this modeling work. VRF heat pump systems use direct expansion to transfer heat between indoor and outdoor air for use in both heating and cooling operation. Thermodynamically, VRF systems have many of the same components as (conventional) heat pumps such as compressors, expansion devices, and heat exchangers. VRF systems transfer heat between one or, more commonly, multiple indoor units, often called 'heads' or 'terminal units,' with a shared common outdoor unit. Some features that differentiate VRF systems from other types of heat pump systems are the scalability (multiple indoor units can be served by one outdoor unit), prevalence of variable speed compressors, distributed control of the refrigerant network, and in some cases the ability to utilize simultaneous heating and cooling between heads of the same system. According to the 2020 ASHRAE Handbook: HVAC Systems and Equipment [1], a VRF system requires the ability to vary the system capacity by three or more steps with one or more indoor units individually controlled through an interconnected piping and communications network.

Figure 1. Highlights of a VRF heat pump system with heat recovery [2]

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89040.yaml
     source: 89040_images/image_000008_823b9276160ea2abe226a95a1c1662553b60c593fa2570fe888045aee25cdba0.png
     method: vision-description
     described: 2026-08-21 -->

![Cutaway illustration of a VRF heat pump system serving an office floor with heat recovery](89040_images/image_000008_823b9276160ea2abe226a95a1c1662553b60c593fa2570fe888045aee25cdba0.png)

Figure 1: cutaway illustration of a VRF heat pump system with heat recovery, labeling the outdoor unit, the two- or three-pipe refrigerant piping, a refrigerant management component and the ceiling-mounted indoor units serving private offices and open areas. Zones in heating are tinted differently from zones in cooling. Reproduced from reference 2; Section 1 summarizes the technology.

There are two distinctive types of VRF systems: (1) multi-split VRF without simultaneous heating and cooling, and (2) VRF with heat recovery (HR) capable of simultaneous heating and cooling. As shown in Figure 1, the VRF (HR) system that allows a single outdoor unit connected to multiple indoor units can provide heating and cooling simultaneously between different zones as needed. This ability to heat and cool simultaneously is made possible by (1) controlling and regulating the refrigerant flow differently between different indoor units and the outdoor unit, and (2) recovering heat from the cooling zones and repurposing the energy for the heating zones. This is advantageous in buildings with varying space conditions that have different heating and cooling requirements. For example, a conference room in the core of a building may require cooling year-round, while perimeter offices may require heating in the winter and cooling in the summer.

Within the category of VRF (HR), the system can be designed as either a two-pipe or three-pipe system, and manufacturers tend to select one option for their model lineup. The selection depends more on the layout of the floor plan and budget than on system heating and cooling demands. The main difference between the two systems is the number of pipes used to connect the outdoor unit to the branch controller (two pipes versus three). Depending on whether the system is a two- or three-pipe system, the piping layout can vary significantly, resulting in a different overall piping length. This in turn affects the performance of the VRF system (Figure 2). Additionally, while the three-pipe system requires a special Y-branch copper pipe fitting (also known as REFNET fitting), it is not required for the two-pipe system. The three-pipe system is known to provide better heating capacity at lower temperatures (compared to two-pipe systems) through less refrigerant line heat losses when designed properly [3].

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89040.yaml
     source: 89040_images/image_000009_dcff12afeb7b613d3674cbcc3629a6e6c73a0ed153d7c7ac6b31220c46ea54fc.png
     method: vision-description
     described: 2026-08-21 -->

![Two floor-plan schematics comparing three-pipe and two-pipe VRF layouts with pipe-length totals](89040_images/image_000009_dcff12afeb7b613d3674cbcc3629a6e6c73a0ed153d7c7ac6b31220c46ea54fc.png)

Figure 2: paired floor-plan schematics of three-pipe and two-pipe VRF layouts on the same building design, each annotated with per-system pipe-run arithmetic. The three-pipe layout totals 2,260 feet of pipe against 5,320 feet for the two-pipe layout, and the three-pipe case additionally requires four mode change units. Reproduced from reference 3; Section 1 discusses heat recovery.

- (a) Three-pipe system example

(b) Two-pipe system example

Figure 2. Different piping layouts between two- and three-pipe systems on the same building design [3]

VRF systems are highly versatile and scalable. Typical capacities range from 1.5 to 63 tons for outdoor units and 0.4 to 10 tons for indoor units [1]. Multiple outdoor units can be connected together to serve larger demands. Some (not all manufacturers' outdoor units) VRF systems allow more than 60 indoor units to be connected to a single outdoor unit, which allows them to be applied to many building designs. Table 1 includes specifications of some VRF (HR) products in the market.

Table 1. Specifications of Available VRF (HR) Systems on the Market

<!-- table recovered from measure_pdfs/89040.pdf p.13
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89040.yaml
     method: vision-transcription -->

| Manufacturer | Daikin | Mitsubishi Electric | Carrier | LG Electronics |
|---|---|---|---|---|
| Model | VRV | PURY-P | 38VMR | Multi V |
| Outdoor unit capacity range | 6-40 tons | 6-28 tons | 6-28 tons | 1.7-17 tons |
| Heat recovery mode available? | yes | yes | yes | yes |
| Operating temperature (cooling) | -4 to 122°F (-20 to 50°C) | 23 to 126°F (-5 to 52°C) | 14 to 122°F (-10 to 50°C) | 5 to 118°F (-15 to 48°C) |
| Operating temperature (heating) | -22 to 60°F (-30 to 16°C) | -22 to 60°F (-30 to 16°C) | -13 to 60°F (-25 to 16°C) | -13 to 64°F (-25 to 18°C) |
| Max height difference between outdoor vs indoor unit | 361 ft (110 m) | 360 ft (110 m) | - | 360 ft (110 m) |
| Max length between indoor units | 295 ft (90 m) | 98 ft (30 m) | - | 131 ft (40 m) |
| Max total piping length | 3,281 ft (1,000 m) | 2,624-3,280 ft (800-1000 m) | 3,280 ft (1,000 m) | 3,281 ft (1,000 m) |
| Refrigerant | R-410A | R-410A | R-410A | R-410A |

VRF systems, like many heat pumps, have several sizing options. One of the options is to size the system to meet the design cooling load. If the associated heating capacity for that equipment cannot meet the full design heating load, supplemental heating is then used to address any unmet load from the VRF system. Supplemental heat can be sourced from various options, including an existing system, electric resistance baseboards, or electric resistance elements integrated within ducted systems [4]. This option may be attractive in very cold climates to avoid oversized equipment for the cooling load and to limit additional upfront costs from upsizing to larger VRF systems.

They can also be sized such that the available heat pump capacity at the design heating temperature matches the design heating load, accounting for the decreased heat pump capacity at temperatures lower than the rating point. This avoids the need for any supplemental heating system and can maximize efficiency, but may require 'upsizing' to a larger VRF system, which adds cost [4, 5]. However, Trane recommends limiting VRF oversizing to a maximum of 125% of the design cooling load, so the system does not end up being too oversized for the cooling load [6]. Daikin has similar recommendations for limiting oversizing, citing that oversized equipment can lead to control issues. This suggests that it may not be advisable to size for the full heating load at the heating design temperature in some climates. Furthermore, the compressor lockout temperature, which specifies the minimum operating temperature for the heat pump, needs to be considered. If the design heating conditions are below that temperature, a supplemental heating source will need to meet the full design heating load.

For this study, we allow up to 25% upsizing (or 125% of the original size) from the design cooling load only for heating-dominant buildings. To provide high-level context on the 25% upsizing algorithm, if a thermal zone is cooling dominant, the indoor unit capacity of the VRF heat pump is sized based on the design cooling load. However, if the thermal zone is heating dominant, it is allowed for the 25% upsizing allowance. Once the 25% upsizing is allowed, if the 25% upsized capacity (or 125% from the original size) represented with the design condition exceeds the design heating load, the design heating load is used to calculate the rated capacity of the indoor unit. If the 25% upsized capacity represented with the design condition does not exceed the design heating load, the 25% upsized capacity represented with the rated condition is used for the capacity of the indoor unit, while the remaining heating load is handled with the supplemental/backup electric resistance coil. The outdoor unit capacity is calculated by summing all indoor unit capacities. More detailed description of the upsizing algorithm is presented in Section 3.2.2 and details on the DOAS and additional background on the technology can be found in the Variable Refrigerant Flow with Heat Recovery and Dedicated Outdoor Air System measure from Commercial End-Use Savings Shapes 2023 Release 2.

