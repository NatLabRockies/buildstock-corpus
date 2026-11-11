<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96634.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96634.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96634.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96634.md | section: 3.1.2 ResStock Inputs for the Natural Gas Furnace | lines: 219-236 -->
## 3.1.2 ResStock Inputs for the Natural Gas Furnace

A central natural gas furnace combusts natural gas to heat indoor air, distributing it via the home's duct system. In HPXML, each furnace is represented under :

'/HPXML/Building/BuildingDetails/Systems/HVAC/HVACPlant/HeatingSystem , ' with type 'Furnace,' and a 95% AFUE, as shown in Table 2.

Table 2. ResStock Argument Values for Gas Furnace Upgrade

| ResStock Argument                   | Value                          | Units    |
|-------------------------------------|--------------------------------|----------|
| Heating System Type                 | Furnace                        | -        |
| Heating System Pilot Light Capacity | 0                              | Btu/hr   |
| Heating System Fuel                 | Natural Gas, Propane, Fuel Oil | -        |
| Annual Heating Efficiency           | 0.95                           | AFUE     |
| Fraction Heating Load Served        | 1                              | Fraction |

OpenStudio-HPXML maps these fields to an OpenStudio Furnace object, setting capacity, efficiency, distribution, and fan characteristics. Following is the input schema support, both required and optional fields.

