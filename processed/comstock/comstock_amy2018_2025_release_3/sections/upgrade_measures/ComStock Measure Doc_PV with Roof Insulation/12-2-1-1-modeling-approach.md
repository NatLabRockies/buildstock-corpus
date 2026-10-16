<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_PV with Roof Insulation.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/2036a73dc9b7a5dccb8b62fe835cdcbc777175fa/assets/files/ComStock%20Measure%20Doc_PV%20with%20Roof%20Insulation.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_PV%20with%20Roof%20Insulation.pdf | corpus_version: comstock_amy2018_2025_release_3-v3 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_PV with Roof Insulation.md | section: 2.1.1  Modeling Approach | lines: 201-215 -->
## 2.1.1  Modeling Approach

This study leverages the PVWatts ®  EnergyPlus ®  objects. PVWatts is a National Laboratory of the Rockies (NLR) tool that estimates the energy production of PV systems [7]. The workflow takes the baseline ComStock energy models and applies PVWatts objects with total power levels corresponding to 40% of each model's roof area , multiplied by a 21% panel efficiency. The panels are fixed with no tracking. This workflow is repeated for all ComStock models. The individual performance assumptions for the PV modules are summarized in Table 4 and described further in the individual upgrade documentation.

Table 4. Assumptions for PV Modeling

| Parameter                | Value            |
|--------------------------|------------------|
| Inverter Efficiency      | 96%              |
| DC/AC Ratio              | 1.10             |
| System Losses            | 14%              |
| Panel Related Efficiency | 21%              |
| Panel Area               | 40% of roof area |
| Title and Azimuth        | Varies           |

