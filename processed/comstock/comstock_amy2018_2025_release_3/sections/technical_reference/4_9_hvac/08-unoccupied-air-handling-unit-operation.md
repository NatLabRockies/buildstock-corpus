<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0396270 | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: Unoccupied Air Handling Unit Operation | lines: 489-529 -->
## Unoccupied Air Handling Unit Operation

Commercial buildings require constant design outdoor air ventilation rates when the building is occupied per ASHRAE-90.1. For air handling units (AHUs), the outdoor air is generally mixed with the supply air. This requires constant supply fan operation to maintain the outdoor air requirements established by ASHRAE-62.1 (ASHRAE 2004). However, AHUs do not need to provide outdoor ventilation air when the building is unoccupied. Therefore, ASHRAE-90.1 requires outdoor air dampers to close when the building is unoccupied, and to only cycle on supply fans as needed to maintain thermostat set points. This control scheme can have a large impact on energy usage, and data suggests that not all buildings implement these controls in their AHU systems. This section discusses ComStock’s methodology for including the prevalence of different unoccupied AHU control schemes observed in real buildings, which follows the methodology used in (CaraDonna and Dombrovski 2022).

An industry-provided BAS data set of over 5,700 AHUs was used to inform the prevalence of three unoccupied AHU operation modes. The data set includes time series (hourly) BAS variables for “Occupied Status” (describes whether the AHU was in an occupied mode for that hour), “Fan Status” (describes whether the fan was used for that hour), and “Ventilation Status” (describes whether outdoor ventilation air was used for that hour). Counts of AHUs and buildings by building type in the data set are shown in Table “Site and AHU Counts of Time Series BAS Data per Building Type”, and the three unoccupied AHU shutdown control schemes are summarized in Table “AHU Operating Mode Schemes Used During Scheduled Unoccupied Times”.

The data set suggests that 27% of AHUs use scheme 1 (least efficient), 50% of AHUs use scheme 2 (more efficient), and 23% of AHUs use scheme 3 (most efficient; ASHRAE-90.1 required). The prevalence of the AHU unoccupied control schemes by building type is shown in Table “AHU Unoccupied Operation Mode Percentages by Building Type Informed by BAS Data Source”. These probability distributions are used in ComStock sampling to set the fraction of buildings utilizing the discussed control schemes, by building type, for models that use AHU-based HVAC systems. Non-AHU HVAC system types are not applicable to this methodology, nor are building types not listed in Table “AHU Unoccupied Operation Mode Percentages by Building Type Informed by BAS Data Source”. Note that building types with less than 25 buildings in the BAS data set (Table “Site and AHU Counts of Time Series BAS Data per Building Type”) use the “All Types” distribution of the data set at large, as fewer than 25 samples cannot reliably be used to represent a population.

The following building types are not included in the unnocupied air handling unit operation workflow, and utilize default scheduling only: small hotels, large hotels, outpatient, hospitals, primary schools, and secondary schools. The building types may be integrated into this workflow in the future as more data becomes available.

<div id="tab:unnoc_ahu_data_counts" data-source="tables/unnoc_ahu_data_counts.tex">

| **Building Type** | **Site Count** | **AHU Count** |
|:------------------|:---------------|:--------------|
| **All Types**     | 843            | 5,706         |
| **Retail**        | 541            | 3,300         |
| **Unknown**       | 164            | 1,391         |
| **Office**        | 43             | 466           |
| **Restaurant**    | 39             | 155           |
| **Grocery**       | 35             | 212           |
| **Hotel**         | 6              | 46            |
| **Education**     | 6              | 29            |
| **Warehouse**     | 5              | 94            |
| **Healthcare**    | 4              | 13            |

Site and AHU Counts of Time Series BAS Data per Building Type

</div>

<div id="tab:unnoc_ahu_schemes" data-source="tables/unnoc_ahu_schemes.tex">

| **Scheme Name** | **Unoccupied Control Scheme Description** | **Expected Efficiency** | **Occupied Status** | **Fan Status** | **Ventilation Status** |
|:---|:---|:---|:---|:---|:---|
| **Scheme 1** | Scheduled on, running | Least Efficient | Active | Active | Active |
| **Scheme 2** | Scheduled off, fan cycles with ventilation to maintain thermostat setpoints | More Efficient | Inactive | Active | Active |
| **Scheme 3** | Scheduled off, fan cycles without ventilation to maintain thermostat setpoints | Most Efficient | Inactive | Active | Inactive |

AHU Operating Mode Schemes Used During Scheduled Unoccupied Times

</div>

