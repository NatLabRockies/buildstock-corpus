<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/96598.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96598.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96598.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/96598.md | section: 1  Introduction | lines: 215-250 -->
## 1  Introduction

Building energy codes play a crucial role in improving energy performance and reducing utility costs in buildings. The most widely adopted model energy codes are the International Energy Conservation Code (IECC) [1] and the ANSI/ASHRAE/IES Standard 90.1 [2] (for simplicity, referred to as 'ASHRAE 90.1' throughout this document). 1 The IECC includes residential and some commercial building types, while ASHRAE 90.1 covers commercial and high-rise residential buildings. These codes and standards establish minimum requirements for energy efficiency for insulation, windows, heating and cooling systems, lighting, and more.

Building energy codes are intended for new construction buildings and major renovations. Existing buildings are not required to comply with the most current building energy code adopted by the state; however, this can leave a large portion of the commercial building stock lagging many code cycles in terms of performance. This is especially apparent with the building envelope (wall insulation, roof insulation, and windows) because these components of a building are not frequently replaced or upgraded.

In the United States, each state decides how to adopt and enforce building energy codes. Cities and local jurisdictions can also choose to adopt their own set of codes; however, at a minimum, they must adhere to the state-adopted code [3]. New IECC and ASHRAE 90.1 standards are released every 3 years. Many states choose to quickly adopt the most recent code version, whereas other states lag several code cycles behind. Nine states do not have any statewide commercial building energy codes: Alaska, Arizona, Colorado, Kansas, Mississippi, Missouri, North Dakota, South Dakota, and Wyoming [4]. States can be classified into four categories based on their historical rate of code adoption:

- Aggressive: The state adopts the new code within one code cycle. Future adoption lag = 1 year.
- Moderate: The state adopts the new code within two code cycles. Future adoption lag = 4 years.
- Slow: The state adopts the new code after two code cycles. Future adoption lag = 7 years.
- Not applicable: States with no statewide code [5].

Although most states and local jurisdictions officially adopt IECC codes as law, the IECC recognizes ASHRAE 90.1 as a pathway for compliance with the requirements of the IECC [6]. Furthermore, ASHRAE 90.1 has multiple compliance pathways, typically either prescriptive or performance based. This study considers only the prescriptive pathway, in which our buildings are modeled to comply with the established criteria for the energy-related characteristics of building components (in this case, wall insulation R-value, roof insulation R-value, and window U-value and solar heat gain coefficient [SHGC]) [7]. This measure will use ASHRAE 90.1 when referring to code adoption, as ComStock™ modeling assumptions are largely based around the ASHRAE 90.1 standard. The main exception is California, which follows Title 24, the California Building Energy Code. Title 24 relies on the Database for Energy Efficient Resources (DEER) to set the minimum energy efficiency standards for new buildings [8], [9]; therefore, for California, this measure uses DEER assumptions for California buildings.

1 ANSI: American National Standards Institute; IES: Illuminating Engineering Society

The U.S. Department of Energy (DOE) Building Energy Codes Program (BECP) tracks code adoption by state and provides other resources and analysis related to building energy code adoption in the United States [4]. Figure 1 shows the commercial code adoption by state as of December 2024 [4]. The ASHRAE 90.1 standard is used as the basis for assigning a current code efficiency category for each state. California, which uses the DEER standard, is categorized as 'greater than or equal to 90.1-2019' for this figure.

In addition, Arizona, despite not having a statewide code, is categorized along with Oklahoma as adhering to a code lower than 90.1-2007. The BECP found that more than 80% of Arizona's population is covered by codes at this level. A similar review of all other states without statewide energy codes will be conducted in subsequent sections to assign the most appropriate/widely followed ASHRAE 90.1 code to these states.

Figure 1. Commercial building energy code adoption by state as of December 2024. Image from [4]

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/96598.yaml
     source: 96598_images/image_000002_7c0cd53f094e7b4639bc5803954c89ea9c0e8855c086fc174ed02cc1ce6b0d55.png
     method: vision-description
     described: 2026-08-21 -->

![Choropleth map of US commercial building energy code efficiency category by state, December 2024](96598_images/image_000002_7c0cd53f094e7b4639bc5803954c89ea9c0e8855c086fc174ed02cc1ce6b0d55.png)

Figure 1: choropleth map of the United States shading each state by commercial building energy code efficiency category as of December 2024, legend running from 90.1-2019 or newer down to below 90.1-2007 plus No statewide code. Pacific, Mountain and New England states hold the newest codes; Arizona and Oklahoma sit lowest; Wyoming, Colorado, Kansas, Missouri and the Dakotas have no statewide code. Table 8 lists the categories by state.

As mentioned, states adopt and enforce energy codes; however, cities and jurisdictions can adopt stricter codes if they wish. These intricacies will not be captured in this measure, which simply upgrades the buildings in a state to the statewide code. As a result, savings estimates when upgrading a building's envelope to the state code could be underestimated if a building is located in a jurisdiction with codes that exceed the state code, but this was the most conservative approach.

The city and local adoption of energy codes also occurs in states with no statewide code. For example, Colorado has no statewide code, but Denver has adopted strict building energy codes that align with 90.1-2019 or better [10]; therefore, there will be some limitations in this measure, as it would be extremely difficult to determine and implement local code (e.g., at the city level) adoption in ComStock.

