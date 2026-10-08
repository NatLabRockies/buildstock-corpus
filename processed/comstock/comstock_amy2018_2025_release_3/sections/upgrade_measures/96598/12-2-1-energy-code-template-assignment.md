<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/96598.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96598.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96598.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/96598.md | section: 2.1  Energy Code Template Assignment | lines: 255-286 -->
## 2.1  Energy Code Template Assignment

In the ComStock baseline, the energy code assigned to a building is based on the location of the building and the year of construction [11]. As shown in Table 1, much of the commercial building stock was constructed before energy codes became widespread. Forty-eight percent of the floor area modeled in ComStock was built before 1980, and another 30% was built from 1980 to 2000. For this period, the 'energy code' is described as either 'DOE Ref Pre-1980,' whose assumptions are drawn from Deru et al. [12], or 'DOE Ref 1980-2004,' whose assumptions are a combination of ASHRAE 90.1-1989 [13] and Deru et al. [12].

For later vintages, ComStock maps to ASHRAE 90.1 versions. If a state's code is not a derivative of the ASHRAE 90.1 series, the most similar version of ASHRAE 90.1 was used for that state. The only exception is California, where the Title 24 series of codes (as represented in DEER) [9] was used. This series of codes has key differences from ASHRAE 90.1 and therefore is used to more accurately model the buildings in California. The energy code template assigned to a building informs many performance assumptions in the model, including envelope; heating, ventilating, and air-conditioning (HVAC); and lighting.

Table 1. Breakdown of ComStock Floor by Building Vintage

| Building Vintage   | Percentage of ComStock Floor Area   | Notes [14]                         |
|--------------------|-------------------------------------|------------------------------------|
| Before 1946        | 12.6%                               |                                    |
| 1946 to 1959       | 9.5%                                |                                    |
| 1960 to 1969       | 12.0%                               |                                    |
| 1970 to 1979       | 13.8%                               | model energy residential buildings |
| 1980 to 1989       | 16.8%                               | National model codes               |
| 1990 to 1999       | 13.4%                               | but not on a                       |
| 2000 to 2012       | 17.4%                               | present: National                  |
| 2013 to 2018       | 4.6%                                | cycle                              |

The adoption of building codes over time varies for each state-some states are assumed to adopt the latest version of ASHRAE 90.1 within 1-2 years after it is released, whereas other states lag many cycles. Figure 2 shows the current ComStock baseline assumptions for the energy code in force as a function of the state and vintage of the building [11]. The assumptions around the code adoption history were largely derived from the Building Codes Assistance Project (BCAP) [15]. For more information about the assumptions that go into ComStock related to building energy codes, see the ComStock Reference Documentation [11].

Figure 2. Energy code in force during year of construction by state. Image from [11]

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/96598.yaml
     source: 96598_images/image_000003_eaa52d4bee3ab599de8b5a175a9f27320c823a87f5575b79225410659b7605a6.png
     method: vision-description
     described: 2026-08-21 -->

![Heatmap of energy code in force during year of construction, by state and construction period](96598_images/image_000003_eaa52d4bee3ab599de8b5a175a9f27320c823a87f5575b79225410659b7605a6.png)

Figure 2: heatmap grid with one row per state and columns for construction periods from 1900-1979 through 2019, each cell shaded by the energy code in force that year. The legend spans DOE Ref Pre-1980 through 90.1-2013 and DEER Pre-1975 through DEER 2017; California is the only state on the DEER track. Section 2.1 describes how these templates are assigned.

