<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Input Characteristics | lines: 3207-3226 -->
## Input Characteristics

We derived the electrical panel service rating (A) and the breaker space headroom using a limited set of survey data. For single-family attached and detached dwellings, the data was used to train machine-learning models, which were then used to generate the distribution of the panel attributes. For multi-family, the characteristic distributions were derived directly from the data due to insufficient samples to support model training. As the dataset does not contain high-fidelity samples for mobile homes, we use the distributions for single-family detached to approximate mobile homes.

79% of the survey data comes from the Pacific regions via: TECH Clean California, Bay Area Renewable Energy Network, Home Energy Analytics, and Northwest Energy Efficiency Alliance Residential Building Stock Assessment, while 20% comes from the Minnesota Center for Energy and the Environment and 1% from LBL Citizen Science survey, which is administered nationally. Due to the data bias towards the Pacific states, where gas heating is dominant, separate model is used for electrically heated and fuel heated single-family dwellings. Table “Dependencies for the distributions of electrical panel service rating and breaker space.” outlines the dependencies for each of the distributions generated for assigning the panel characteristics. The field values for electrical panel service rating (A) are: \<100, 100, 101-124, 125, 126-199, 200, 201+. The availale breaker space options (count) range from 0 to 31.

<div id="tab:panel_deps" data-source="3c_ResStockInputs.tex">

| **Electrical Panel Input** | **Housing Segment** | **Dependencies** |
|:---|:---|:---|
| Service rating | Single-Family, electric heat | Building type, floor area, vintage, water heater fuel, cooling type, clothes dryer, cooking range |
| Service rating | Single-Family, fuel heat | Building type, floor area, vintage |
| Service rating | Multi-Family | Floor area, vintage, heating fuel |
| Breaker space headroom | Single-Family | Service rating, major electric load count, floor area |
| Breaker space headroom | Multi-Family | Service rating, major electric load count |

Dependencies for the distributions of electrical panel service rating and breaker space.

</div>

