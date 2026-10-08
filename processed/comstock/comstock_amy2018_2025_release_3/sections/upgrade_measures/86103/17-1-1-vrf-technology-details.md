<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86103.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/86103.md | section: 1.1  VRF Technology Details | lines: 213-271 -->
## 1.1  VRF Technology Details

The upgrade described in this document is about replacing the existing heating, ventilation, and air-conditioning (HVAC) system. The upgraded system decouples ventilation from space conditioning, with ventilation being handled by the dedicated outdoor air system (DOAS), and the remaining space conditioning handled by a variable refrigerant flow (VRF) air-source heat pump system.

Figure 1 shows the key features of the VRF system considered in this modeling work. VRF heat pump systems use direct expansion (DX) to transfer heat between indoor and outdoor air for use in both heating and cooling operation. Thermodynamically, VRFs have many of the same components as (conventional) heat pumps such as compressors, expansion devices, and heat exchangers. VRF systems transfer heat between one or, more commonly, multiple indoor units, often called 'heads' or 'terminal units,' with a shared common outdoor unit. Some features that differentiate VRF systems from other types of heat pump systems are the scalability (multiple indoor units can be served by one outdoor unit), prevalence of variable speed compressors, distributed control of the refrigerant network, and in some cases the ability to utilize simultaneous heating and cooling between heads of the same system. According to the 2020 ASHRAE Handbook of HVAC Systems and Equipment [1], a VRF system requires the ability to vary the system capacity by three or more steps with one or more indoor units individually controlled through an interconnected piping and communications network.

Figure 1. Highlights of VRF heat pump system with heat recovery [2]

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000007_74a37b2d69fd5e8fc21669ba27453e964f2487518f49a639c6ff0cc74f67b128.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 1: cutaway diagram of a VRF heat-recovery system serving a commercial floor](86103_images/image_000007_74a37b2d69fd5e8fc21669ba27453e964f2487518f49a639c6ff0cc74f67b128.png)

Figure 1: cutaway isometric schematic of an open-plan commercial floor served by a VRF heat pump with heat recovery. Callouts label the outdoor unit, the two- or three-pipe refrigerant lines, the refrigerant management component (branch controller), and ceiling-mounted indoor units in each zone. Illustrates how simultaneously heating and cooling zones exchange heat through one refrigerant loop. See Section 1.1.

There are two distinctive types of VRFs: (1) a multisplit VRF without simultaneous heating and cooling, and (2) a VRF with heat recovery (HR) capable of simultaneous heating and cooling. As shown in Figure 1, the VRF HR system that allows a single outdoor unit connected to multiple indoor units can provide heating and cooling simultaneously between different zones as needed. This ability to heat and cool simultaneous is made possible by (1) controlling and regulating the refrigerant flow differently between different indoor units and the outdoor unit, and (2) recovering heat from the cooling zones and repurposing the energy for the heating zones. This is advantageous in buildings with varying space conditions that have different heating and cooling requirements. For example, a conference room in the core of a building may require cooling year-round while perimeter offices may require heating in the winter and cooling in the summer.

Within the category of a VRF HR, the system can be designed as either a two-pipe or three-pipe system, and manufacturers tend to select one option for their model lineup. The selection depends more on the layout of the floor plan and budget than on system heating and cooling demands. The main difference between the two systems is the number of pipes used to connect the outdoor unit to the branch controller (two pipes versus three). Depending on whether the system is a two- or three-pipe system, the piping layout can vary significantly, resulting in a different overall piping length, which in turn affects the performance of the VRF system as shown in Figure 2. Additionally, while the three-pipe system requires a special Y branch copper pipe fitting (also known as REFNET fitting), that is not required for the two-pipe system. The three-pipe system is known to provide better heating capacity at lower temperatures (compared to two-pipe system) through less refrigerant line losses when designed properly [3].

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000008_9bd099f5218cc3fbbac0faab30e116439b40f9924630689368b12786ae873ed1.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 2: three-pipe and two-pipe VRF piping layouts for the same building design](86103_images/image_000008_9bd099f5218cc3fbbac0faab30e116439b40f9924630689368b12786ae873ed1.png)

Figure 2: paired piping-layout diagrams for the same building design, three-pipe (a) and two-pipe (b), each overlaying refrigerant runs on a floor plan with the required components and pipe-length arithmetic listed beneath. The three-pipe layout needs four mode change units and 2,260 total feet of pipe; the two-pipe layout needs 5,320 feet. See Section 1.1.

- (a) Three-pipe system example
- (b) Two-pipe system example

Figure 2. Different piping layouts between two- and three-pipe systems on the same building design [3]

VRF systems are highly versatile and scalable. Typical capacities range from 1.5 to 63 tons for outdoor units and 0.4 to 10 tons for indoor units [1]. And multiple outdoor units can even be connected together to serve larger demands. Some (not all manufacturers' outdoor units) VRF systems allow more than 60 indoor units to be connected to a single outdoor unit, which allows them to be applied to many building designs. Table 1 includes specifications of some VRF (with heat recovery) products in the market.

Table 1. Specifications of Available VRF (HR) Systems on the Market

<!-- table recovered from measure_pdfs/86103.pdf p.14
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     method: vision-transcription -->

| manufacturer | Daikin | Mitsubishi Electric | Carrier | LG electronics |
|---|---|---|---|---|
| model | VRV | PURY-P | 38VMR | Multi V |
| outdoor unit capacity range | 6-40 tons | 6-28 tons | 6-28 tons | 1.7-17 tons |
| heat recovery mode available? | yes | yes | yes | yes |
| operating T (cooling) | -4 to 122°F | 23 to 126°F | 14 to 122°F | 5 to 118°F |
| operating T (heating) | -22 to 60°F | -22 to 60°F | -13 to 60°F | -13 to 64°F |
| max height diff outdoor vs indoor unit | 110 m (361 ft) | 110 m (360 ft) | - | 110 m (360 ft) |
| max length between indoor units | 90 m (295 ft) | 30 m (98 ft) | - | 40 m (131 ft) |
| max total piping length | 1,000 m (3,281 ft) | 800-1000 m (2,624-3,280 ft) | 1,000 m (3,280 ft) | 1,000 m (3,281 ft) |
| refrigerant | R-410a | R-410a | R-410a | R-410a |

VRF systems, like many heat pumps, have several sizing options. They can be sized such that the available heat pump capacity at the design heating temperature matches the design heating load, accounting for the decreased heat pump capacity at lower temperatures. This avoids the need for any supplemental heating system and can maximize efficiency, but may require 'upsizing' to a larger VRF system, which adds cost [4]. This approach has some limitations. Trane recommends limiting VRF oversizing to a maximum of 125% of the design cooling load so that the system does not end up being too oversized for the cooling load [5]. Daikin has similar recommendations for limiting oversizing citing that oversized equipment can lead to control issues. This suggests that it may not be possible to size for the full heating load at the heating design temperature in some climates. Furthermore, the compressor lockout temperature, which specifies the minimum operating temperature for the heat pump, needs to be considered. If the design heating conditions are below this temperature, then a supplemental heating source will be needed to meet the full design heating load.

Another sizing option is to size the system to meet the design cooling load. If the associated heating capacity for that equipment cannot meet the full design heating load, supplemental heating is then used to address any unmet load from the VRF system. Supplemental heat can be sourced from various options, including an existing system, electric resistance baseboards, or electric resistance elements integrated within ducted systems [4]. This option may be attractive in very cold climates to avoid oversized equipment for the cooling load and to limit additional upfront costs from upsizing to larger VRF systems.

