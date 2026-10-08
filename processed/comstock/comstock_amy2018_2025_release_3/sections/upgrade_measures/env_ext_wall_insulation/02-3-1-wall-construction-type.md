<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_ext_wall_insulation.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_ext_wall_insulation.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_ext_wall_insulation.html | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_ext_wall_insulation.md | section: 3.1  Wall Construction Type | lines: 164-246 -->
## 3.1  Wall Construction Type

First, we selected the general types of wall construction methods to be represented in ComStock. We chose the four general wall types commonly used in commercial building energy codes because they cover the most common wall construction types and can be linked to nominal thermal characteristics. The definitions of these types from ASHRAE are as follows, with the corresponding ComStock enumerations shown in parentheses:

-   **Mass wall (Mass)**: A wall with a heat capacity exceeding (1) 7 Btu/ft<sup>2</sup>-F or (2) 5 Btu/ft<sup>2</sup>-F, provided that the wall has a material unit weight not greater than 120 lb/ft<sup>2</sup>.

-   **Metal building wall (Metal Building)**: A wall whose structure consists of metal spanning members supported by steel structural members (i.e., does not include spandrel glass or metal panels in curtain wall systems).

-   **Steel-framed wall (SteelFramed)**: A wall with a cavity (insulated or otherwise) whose exterior surfaces are separated by steel framing members (i.e., typical steel stud walls and curtain wall systems).

-   **Wood-framed and other walls (WoodFramed)**: All other wall types, including wood stud walls.

To determine the prevalence of each wall construction type, we queried a database, LightBox, containing building type, number of stories, location, and wall construction. The database did not use the same wall construction types selected for ComStock, so we created a mapping between the database entries and the wall construction types listed above, as shown in Table 4. Some construction types in the database were excluded from the mapping, either because the meaning was ambiguous or because they represented an insignificant fraction of the entries in the database. The excluded constructions represent only 5% of the total samples, with 4.5% labeled "OTHER" (which there was no clear way to map).

Table 4. Mapping of Wall Construction Types from Database to ComStock

<!-- table recovered from ./media/037949da-0ec3-4567-9133-08fbcbaa44e6.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_ext_wall_insulation.yaml
     method: vision-transcription -->

**Database types covering 1% or more of entries**

| Database Type | Percent of Entries | ComStock Type | Note |
|---|---|---|---|
| FRAME | 24.96% | SteelFramed | We believe that this mostly represents steel stud construction based on a survey of samples of this type |
| WOOD | 23.93% | WoodFramed | Clearly meets wood-framed wall definition |
| MASONRY | 20.78% | Mass | Could be CMU or brick veneer; both meet the definition of mass wall |
| STEEL | 8.48% | SteelFramed | We believe that this mostly indicates curtain wall with steel framing for tall buildings, and steel stud for shorter buildings |
| BRICK | 6.01% | Mass | Could either be structural brick or brick veneer; both meet the definition of mass wall |
| OTHER | 4.49% | No Match | Meaning unclear |
| CONCRETE BLOCK | 4.48% | Mass | Clearly meets mass wall definition |
| CONCRETE | 3.34% | Mass | Clearly meets mass wall definition |
| TILT-UP (PRE-CAST CONCRETE) | 1.59% | Mass | Clearly meets mass wall definition |
| METAL | 1.26% | Metal Building | Clearly meets metal building definition |

**Database types covering less than 1% of entries**

| Database Type | Percent of Entries | ComStock Type | Note |
|---|---|---|---|
| STONE | 0.22% | No Match | Inconsistent, but often used to describe buildings with a small percentage of decorative stone veneer around the base of the wall. Insignificant fraction of stock |
| MIXED | 0.21% | No Match | Meaning unclear from survey, and insignificant fraction |
| LOG | 0.09% | No Match | Insignificant fraction |
| LIGHT | 0.07% | No Match | Insignificant fraction |
| ADOBE | 0.04% | No Match | Insignificant fraction |
| MANUFACTURED | 0.03% | No Match | Meaning unclear from survey, and insignificant fraction |
| HEAVY | 0.00% | No Match | Meaning unclear from survey, and insignificant fraction |
| DOME | 0.00% | No Match | Meaning unclear from survey, and insignificant fraction |

Upon reviewing the data, we identified two instances that were likely misclassifications. The first was buildings higher than five stories with the wall construction type "WoodFramed." Historically, it was not possible to use Wood-Framed construction for buildings over five stories, and even today, this practice is uncommon. We reassigned buildings with this combination to "Mass" walls, based on the assumption that people were observing large wood internal structural members in old buildings and classifying them as WoodFramed. The second was buildings higher than two stories with "MetalBuilding" walls. Based on experience, this construction technique is commonly reserved for 1- to 2-story buildings only. We reassigned buildings with this combination to "SteelFramed," based on the assumption that this would be the most likely alternative classification if a person observed steel structural elements.

After mapping each entry in the database to one of the ComStock construction types, we analyzed the data to determine other building characteristics in the database that were correlated with construction type. Older buildings were slightly more likely to use mass constructions, but the change over time was minor. Construction type varied significantly as a function of the number of stories. Shorter buildings were much more likely to be wood-framed, whereas taller buildings were more likely to be mass, and very tall buildings were likely to be steel-framed (steel studs or curtain wall). Based on spot-checking of the database, we found the building type classification to be less reliable than other building characteristics. Although there was some correlation between building type and wall construction, there was also a correlation between building type and number of stories. Because of the joint correlation, we selected number of stories instead of building type. There was a clear correlation between climate zone and construction type---most notably, there was a much lower incidence of mass walls in cold climate zones. There was some correlation between construction type and building floor area. However, there was also a correlation between the number of stories and the building area. Because the construction type is physically limited by a building's height, it was more logical to use the number of stories as a driving characteristic for construction type. Following this analysis, we concluded that the number of stories and climate zone should be used as drivers of wall construction type. The probabilities for each combination of number of stories and climate zone were calculated and then used as the input distribution for wall construction type in ComStock. This distribution is summarized in Table 5.

Table 5. Input Distribution of Wall Construction Types by Climate Zone and Number of Stories

<!-- table recovered from ./media/dafea5c3-6536-4788-a383-99d60682e6c0.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_ext_wall_insulation.yaml
     method: vision-transcription -->

| Climate | Mass | Metal Building | Steel Framed | Wood Framed |
|---|---|---|---|---|
| Cold (Zones 5-8) | 51% | 0% | 40% | 9% |
| 1-2 stories | 23% | 1% | 46% | 30% |
| 3-5 stories | 38% | 0% | 35% | 27% |
| 6-10 stories | 71% | 0% | 29% | 0% |
| 11-14 stories | 57% | 0% | 43% | 0% |
| 15-25 stories | 41% | 0% | 59% | 0% |
| over 25 stories | 33% | 0% | 67% | 0% |
| Hot (Zones 1-3) | 52% | 0% | 43% | 5% |
| 1-2 stories | 46% | 1% | 33% | 19% |
| 3-5 stories | 49% | 0% | 39% | 12% |
| 6-10 stories | 64% | 0% | 36% | 0% |
| 11-14 stories | 53% | 0% | 47% | 0% |
| 15-25 stories | 34% | 0% | 66% | 0% |
| over 25 stories | 23% | 0% | 77% | 0% |
| Mixed (Zone 4) | 65% | 0% | 31% | 4% |
| 1-2 stories | 43% | 1% | 40% | 16% |
| 3-5 stories | 60% | 0% | 28% | 12% |
| 6-10 stories | 78% | 0% | 22% | 0% |
| 11-14 stories | 69% | 0% | 31% | 0% |
| 15-25 stories | 56% | 0% | 44% | 0% |
| over 25 stories | 47% | 0% | 53% | 0% |
| Grand Total | 54% | 0% | 40% | 7% |

