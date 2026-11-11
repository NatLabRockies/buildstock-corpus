<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96635.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96635.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96635.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96635.md | section: 3.1.1  ResStock Inputs | lines: 191-210 -->
## 3.1.1  ResStock Inputs

Propane and fuel oil furnaces are modeled as forced-air heating systems serving homes with central ducts. Each upgrade replaces the existing heating system with a furnace that uses either propane or fuel oil, with efficiency defined by a target AFUE level: 88% AFUE for fuel oil heated dwellings and 95% AFUE for propane heated dwellings. These furnaces are modeled assuming that the efficiency is constant at the AFUE and that heating is always available if there is a demand for it. This measure assumes the furnaces are always installed correctly, although models exist in OpenStudio-HPXML to account for issues with installation that may degrade performance. The furnaces supply air at a constant temperature to the ducts. Duct losses are then calculated based on the supply temperature, airflow rate, and duct characteristics using a custom routine in EnergyPlus.

For propane furnaces, the AFUE used here requires a condensing furnace, modeled with a side vent. Lower efficiency equipment often uses a vertical atmospheric vent, as it vents at a higher temperature and can rely on buoyancy. In OpenStudio-HPXML, the type of vent affects the infiltration in the home, as atmospheric vents can increase infiltration. This means this upgrade can also decrease infiltration in these homes if they don't have another atmospheric vent for the water heater; see references for more details on when atmospheric flues are modeled (HPXML 2025).

In OpenStudio-HPXML, each central furnace is represented under:

'/HPXML/Building/BuildingDetails/Systems/HVAC/HVACPlant/HeatingSystem,' with type 'Furnace,' and a federal minimum efficiency or like -for-like efficiency replacement. OpenStudio-HPXML maps these fields to an OpenStudio Furnace object, setting capacity, efficiency, distribution, and fan characteristics. Below is the input schema support, both required and optional fields.

Table 2. ResStock Argument Values for Central Furnaces

| ResStock Argument                   | Value                               | Units    |
|-------------------------------------|-------------------------------------|----------|
| Heating System Type                 | Furnace                             | -        |
| Heating System Pilot Light Capacity | 0                                   | Btu/hr   |
| Heating System Fuel                 | Propane, Fuel Oil                   | -        |
| Annual Heating Efficiency           | 0.95 for Propane, 0.88 for Fuel Oil | AFUE     |
| Fraction Heating Load Served        | 1                                   | Fraction |

