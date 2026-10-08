<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_2_meta.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_2_meta.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 43ae2d4 | corpus_path: technical_reference/documentation/reference_doc/4_2_meta.md | section: Location | lines: 4-27 -->
## Location

ComStock has four levels of location granularity for its building models: ASHRAE Standard 169 - 2006 climate zone, census division, state, and county. During sampling, each model is first assigned a climate zone, then a county, then a state and census division. The climate zone and county probability distributions come from the CoStar and HIFLD data provided by the Homeland Security Infrastructure Program (HSIP) on a building count basis. The state and census division are assigned using a lookup table that is based on the model’s sampled county. The location metadata impacts numerous characteristics in the model, such as weather file, building type, building geometry characteristics (e.g., number of stories and rentable area), and energy code applicability. Table <a href="#tab:census_division_models_table" data-reference-type="ref" data-reference="tab:census_division_models_table">1</a> shows the number of models used in each census division.

Additional location metadata is joined to the *buildstock.csv* for use in parsing ComStock results. This includes data such as [Public Use Microdata Area](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/pumas.html) (PUMA), [Building America climate zone](https://www.energy.gov/eere/buildings/building-america-climate-specific-guidance), [independent system operator (ISO) region](https://isorto.org/), and [ReEDS balancing area](https://www.nrel.gov/analysis/reeds). This location metadata is joined on the [census tract](https://www2.census.gov/geo/pdfs/education/CensusTracts.pdf) level. Census tracts are assigned to the *buildstock.csv* using the CoStar and HSIP data. These location fields also include building cluster ID and name. Developed by DOE and NREL, these 88 geographic clusters allow for localized building stock analyses and are the basis for the U.S. Building Stock Segmentation Series. For more details about these clusters and their development, reference the [Building Stock Segmentation Cluster Development](https://www.nrel.gov/docs/fy23osti/84648.pdf) technical report.

<div id="tab:census_division_models_table" data-source="tables/census_division_models_table.tex">

| **Census Division** | **Count** | **Percentage** |
|:-------------------:|:---------:|:--------------:|
| East North Central  |   54122   |     15.46%     |
| East South Central  |   19882   |     5.68%      |
|    Mid-Atlantic     |   44976   |     12.85%     |
|      Mountain       |   24258   |     6.93%      |
|     New England     |   16791   |     4.80%      |
|       Pacific       |   54799   |     15.66%     |
|   South Atlantic    |   72616   |     20.75%     |
| West North Central  |   20910   |     5.97%      |
| West South Central  |   41646   |     11.90%     |

Distribution of ComStock Models in Each Census Division

</div>

