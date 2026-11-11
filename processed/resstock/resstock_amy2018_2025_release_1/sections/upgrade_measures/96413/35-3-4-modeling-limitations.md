<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96413.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96413.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96413.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96413.md | section: 3.4  Modeling Limitations | lines: 379-386 -->
## 3.4  Modeling Limitations

Ducted heat pump units run their indoor fan during defrost. This would create a 'cold blow' that would be objectionable to some homeowners. To avoid this, the backup heat is brought on to temper the air and avoid discomfort. This results in backup heating usage even at mild temperatures. This backup heating is not presently modeled in EnergyPlus. The cooling delivered during defrost is offset by additional heat pump heating if the building load does not exceed the heat pump capacity after defrost degradation penalties. This limitation causes lower estimates for backup heating (COP = 1.0) in simulations because the heat pump compressor (COP &gt; 1.0) is being modeled to offset the defrost cooling.

Additionally, some dwellings that receive this heat pump will not have a duct system that is sized large enough for the heat pump's capacity. ResStock resizes ducts in the dwelling to accommodate the new heat pump upgrade.

The functions of flow fraction are 1 because the blower is assumed to have constant flow

