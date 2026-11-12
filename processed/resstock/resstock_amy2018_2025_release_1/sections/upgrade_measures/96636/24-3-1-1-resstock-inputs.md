<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96636.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96636.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96636.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96636.md | section: 3.1.1  ResStock Inputs | lines: 279-410 -->
## 3.1.1  ResStock Inputs

The upgrade spans heating and cooling systems. This section details the ResStock inputs for each system type included in the upgrade: central furnaces, wall and floor furnace, electric furnaces, fuel boilers, central air conditioners, room air conditioners, and ASHPs. Any features not set in ResStock are defaulted to OpenStudio-HPXML defaults (HPXML 2025).

In OpenStudio-HPXML, each central furnace is represented under:

'/HPXML/Building/BuildingDetails/Systems/HVAC/HVACPlant/HeatingSystem , ' with type 'Furnace , ' and a federal minimum efficiency or like-for-like efficiency replacement. OpenStudio-HPXML maps these fields to an OpenStudio Furnace object, setting capacity, efficiency, distribution, and fan characteristics. Below are the OS-HPXML arguments assigned wit this measure, both required and optional fields.

Table 2. ResStock Argument Values for Central Furnace Upgrades in this Measure

| ResStock Argument                   | Value                                                 | Units    |
|-------------------------------------|-------------------------------------------------------|----------|
| Heating System Type                 | Furnace                                               | -        |
| Heating System Pilot Light Capacity | 0                                                     | Btu/hr   |
| Heating System Fuel                 | Natural Gas, Propane, Fuel Oil                        | -        |
| Annual Heating Efficiency           | 0.80* for Natural Gas and Propane, 0.83* for Fuel Oil | AFUE     |
| Fraction Heating Load Served        | 1                                                     | Fraction |

*Or like-for-like AFUE when existing furnace efficiency is greater than the minimum

In OpenStudio-HPXML, each fuel-fired floor or wall furnace is represented under: '/HPXML/Building/BuildingDetails/Systems/HVAC/HVACPlant/HeatingSystem.'

Table 3. ResStock Argument Values for Wall/Floor Furnace Upgrades in this Measure

| ResStock Argument            | Wall Furnace                   | Units    |
|------------------------------|--------------------------------|----------|
| Heating System Type          | Wall Furnace                   | -        |
| Heating System Fuel          | Natural Gas, Propane, Fuel Oil | -        |
| Annual Heating Efficiency    | Like-for-like*                 | AFUE     |
| Fraction Heating Load Served | 1                              | Fraction |

*The package keeps non-ducted wall/floor furnaces at their existing levels for like-for-like replacement.

In OpenStudio-HPXML, each electric furnace is represented under: '/HPXML/Building/BuildingDetails/Systems/HVAC/HVACPlant/HeatingSystem.'

Table 4. ResStock Argument Values for Electric Furnace Upgrades in this Measure

| ResStock Argument            | Electric Furnace    | Units    |
|------------------------------|---------------------|----------|
| Heating System Type          | Electric Resistance | -        |
| Heating System Fuel          | Electricity         | -        |
| Annual Heating Efficiency    | 1.0                 | AFUE     |
| Fraction Heating Load Served | 1                   | Fraction |

In OpenStudio-HPXML, each boiler is represented under:

'/HPXML/Building/BuildingDetails/Systems/HVAC/HVACPlant/HeatingSystem.'

Table 5. ResStock Argument Values for Boiler Upgrades in this Measure

<!-- table recovered from measure_pdfs/96636.pdf p.18
     overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/96636.yaml
     method: extracted grid (values, compared with the page)
     supersedes the extractor's own table here (values 7e8b3c968f70…):
     and its continuation grid(s) (values 97952f190995…):
       The table runs over pages 18 and 19 and was extracted as two grids (one row, then three, the header repeated). Every cell of both grids matches the pages. The rows are the extractor's own, joined under one header. The table's footnote is the extracted paragraph below it. -->

| ResStock Argument | Boiler | Units |
|---|---|---|
| Heating System Type | Boiler | - |
| Heating System Fuel | Natural Gas, Propane, Fuel Oil | - |
| Annual Heating Efficiency | Natural Gas or Propane: 0.80; Fuel Oil: 0.83 AFUE; or like-for-like* | AFUE |
| Fraction Heating Load Served | 1 | Fraction |

*If an existing boiler is greater than minimum, it is retained like-for-like efficiency

Boilers are slightly different than furnaces in that the actual efficiency of the boiler varies slightly based on the return water temperature, whereas for furnaces the efficiency is always constant and equal to the AFUE of the unit.

In OpenStudio-HPXML, each central air conditioner is represented under: '/HPXML/Building/BuildingDetails/Systems/HVAC/HVACPlant/ CoolingSystem .'

Table 6. ResStock Argument Values for Central Air Conditioner Upgrades in this Measure

| ResStock Argument            | Central Air Conditioner                                   | Units    |
|------------------------------|-----------------------------------------------------------|----------|
| Cooling System Type          | Central Air Conditioner                                   | -        |
| Cooling System Fuel          | Electricity                                               | -        |
| Annual Cooling Efficiency    | SEER2 14.3 (South); SEER2 13.4 (North); or like-for-like* | SEER2    |
| Fraction Cooling Load Served | 1                                                         | Fraction |
| Compressor Type              | Single stage                                              | -        |

*Like-for-like retention applies where the existing central AC is greater than minimum efficiency. See section 1.3.3 for a list of states in the South and North regions.

In OpenStudio-HPXML, each room air conditioner with reverse cycle is represented under: '/HPXML/Building/BuildingDetails/Systems/HVAC/HVACPlant/Heat Pump .'

Table 7. ResStock Argument Values for Room Air Conditioner Upgrades in this Measure

<!-- table recovered from measure_pdfs/96636.pdf p.19
     overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/96636.yaml
     method: extracted grid (values, compared with the page)
     supersedes the extractor's own table here (values ee4c93dbcda2…):
       The extractor flattened the superscript footnote markers into the values ('12.0 1', 'EER 3', 'Varies 2'), so the efficiency read as two numbers. The markers are restored as superscripts; every other cell is the extractor's own and matches page 19. The three footnotes they refer to are the extracted paragraphs below the table, numbered 1 to 3. The missing space in '1.01.ResStock' is the source's. -->

| ResStock Argument | Room Air Conditioner | Units |
|---|---|---|
| Heat Pump Type | Room Air Conditioner | - |
| Annual Cooling Efficiency | 12.0¹ | EER³ |
| Fraction Cooling Load Served | Varies² | Fraction |
| Compressor Type | Single Stage | - |

1 Like-for-like retention applies where the existing room AC is greater than minimum efficiency

2 Fraction of load served varies based on dwelling specification

3 EER is used rather than CEER as the default rated efficiency units for room AC in ResStock. One can convert between units using: CEER = EER / 1.01.ResStock may move to CEER for future releases.

In OpenStudio-HPXML, each ASHP is represented under: '/HPXML/Building/BuildingDetails/Systems/HVAC/HVACPlant/Heat Pump .'

Table 8. ResStock Argument Values for ASHP Upgrades in this Measure

| ResStock Argument                                         | ASHP         | Calculated by OpenStudio- HPXML?   |
|-----------------------------------------------------------|--------------|------------------------------------|
| Heat pump type                                            | Air-to-air   | No                                 |
| heat_pump_heating_efficiency_type                         | HSPF2        | No                                 |
| heat_pump_heating_efficiency                              | 7.5*         | No                                 |
| heat_pump_cooling_efficiency_type                         | SEER2        | No                                 |
| heat_pump_cooling_efficiency                              | 14.3*        | No                                 |
| heat_pump_sizing_methodology                              | ACCA         | No                                 |
| heat_pump_heating_capacity                                | Auto         | Yes                                |
| heat_pump_fraction_heat_load_served                       | 1            | No                                 |
| heat_pump_cooling_capacity                                | Auto         | Yes                                |
| heat_pump_fraction_cool_load_served                       | 1            | No                                 |
| heat_pump_backup_type                                     | Integrated   | No                                 |
| heat_pump_backup_fuel                                     | Electricity  | No                                 |
| heat_pump_backup_heating_efficiency                       | 1.0          | No                                 |
| heat_pump_backup_heating_capacity                         | Auto         | Yes                                |
| heat_pump_heating_capacity_retention_fraction             | 0.5          | No                                 |
| heat_pump_heating_capacity_retention_fraction_temperature | 5°F          | No                                 |
| heat_pump_is_ducted                                       | True         | No                                 |
| heat_pump_compressor_type                                 | Single stage | No                                 |

*Or like-for-like AFUE when existing heat pump efficiency is greater than minimum efficiency

