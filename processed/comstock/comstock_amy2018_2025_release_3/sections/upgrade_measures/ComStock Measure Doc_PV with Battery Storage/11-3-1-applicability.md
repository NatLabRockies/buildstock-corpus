<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_PV with Battery Storage.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/assets/files/ComStock%20Measure%20Doc_PV%20with%20Battery%20Storage.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_PV%20with%20Battery%20Storage.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_PV with Battery Storage.md | section: 3.1  Applicability | lines: 201-217 -->
## 3.1  Applicability

The rooftop PV measure scenario is applicable to all models in the ComStock baseline. No building models are excluded. In practice, some commercial buildings may be less suitable for rooftop PV (e.g., the roof does not have 40% of the area available for PV), which these applicability criteria do not consider. In addition, as mentioned, the ComStock baseline does not currently include the estimated &lt;2% of commercial buildings that already have PV. Therefore, this study likely slightly overestimates the potential for mass commercial rooftop PV adoption in the stock.

| Parameter              | Value                                         |
|------------------------|-----------------------------------------------|
| Inverter Efficiency    | 96%                                           |
| DC/AC Ratio            | 1.10                                          |
| System Losses          | 14%                                           |
| Panel Rated Efficiency | 21%                                           |
| Panel Area             | 40% of roof area                              |
| Title and Azimuth      | Varies by latitude                            |
| Battery Capacity       | Varies by rated PV capacity and building type |
| Battery Power          | Varies by rated PV capacity and building type |

3.2  Measure Scenario Modeling Methodology This study uses PVWatts® EnergyPlus objects and follows the same methodology as a comparable ComStock study (rooftop PV measure) [1], with the key difference being the inclusion of battery storage in the current analysis. PVWatts is a National Renewable Energy Laboratory (NREL) developed tool that estimates the energy production of PV systems [8]. The workflow takes the baseline ComStock energy models, representing the building stock of 2018, and applies PVWatts objects with total power levels corresponding to 40% of each model's roof area. The panels are fixed with no tracking. Battery storage is then added according to Equations 1 and 2. This workflow is repeated for all ComStock models. The individual performance assumptions for the PV modules are summarized in Error! Reference source not found. and described in the following sections. Table 2. Summary of Assumptions for PV Modeling Parameter Inverter Efficiency DC/AC Ratio System Losses Panel Rated Efficiency Panel Area Title and Azimuth Battery Capacity Battery Power PRE-PUBLICATION

