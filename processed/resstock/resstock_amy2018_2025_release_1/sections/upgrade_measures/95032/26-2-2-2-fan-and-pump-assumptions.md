<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95032.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: upgrade_measures/measure_pdfs/95032.md | section: 2.2.2  Fan and Pump Assumptions | lines: 343-360 -->
## 2.2.2  Fan and Pump Assumptions

Assumptions made about the fan and pump size have an impact on the nominal efficiency of the GHP, which in turn impacts the overall energy consumption results. The EnergyPlus models require a gross COP, without any impact from the fan and pump, as an input because the fan and pump are modeled separately. Specification sheets for GHPs list the performance across a wide range of conditions, but these represent the net performance (including the impact of the heat from the fan and pump), not the gross (without the fan and pump). More information on converting net to gross can be found in (Cutler 2013). Since we are calculating the size of the GHP as part of the HVAC equipment sizing and explicitly modeling the fan and pump, we need to be able to go from the net to the gross capacity so that we do not include the impact of heat gains from these devices twice. These net-to-gross calculations need to be updated to correctly reflect the impact of both the fan heat and the pump. EnergyPlus models the fan and pump separately, so the proper model input for the coil object is the gross COP without any impact from the fan and pump.

[7  https://github.com/NatLabRockies/resstock/blob/f2d372026f2860cc0f6e62f52ff1d20a3ace055c/resources/hpxml-measures/HPXMLtoOpenStudio/resources/defaults.rb#L2495-L2640](https://github.com/NREL/resstock/blob/f2d372026f2860cc0f6e62f52ff1d20a3ace055c/resources/hpxml-measures/HPXMLtoOpenStudio/resources/defaults.rb#L2495-L2640)

[8  https://github.com/NatLabRockies/resstock/blob/f2d372026f2860cc0f6e62f52ff1d20a3ace055c/resources/hpxml-measures/HPXMLtoOpenStudio/resources/defaults.rb#L1832-L2350](https://github.com/NREL/resstock/blob/f2d372026f2860cc0f6e62f52ff1d20a3ace055c/resources/hpxml-measures/HPXMLtoOpenStudio/resources/defaults.rb#L1832-L2350)

[9  https://github.com/NatLabRockies/resstock/blob/f2d372026f2860cc0f6e62f52ff1d20a3ace055c/resources/hpxml-measures/HPXMLtoOpenStudio/resources/defaults.rb#L4029-L4033](https://github.com/NREL/resstock/blob/f2d372026f2860cc0f6e62f52ff1d20a3ace055c/resources/hpxml-measures/HPXMLtoOpenStudio/resources/defaults.rb#L4029-L4033)

[10  https://github.com/NatLabRockies/resstock/blob/f2d372026f2860cc0f6e62f52ff1d20a3ace055c/resources/hpxml-measures/HPXMLtoOpenStudio/resources/defaults.rb#L5302](https://github.com/NREL/resstock/blob/f2d372026f2860cc0f6e62f52ff1d20a3ace055c/resources/hpxml-measures/HPXMLtoOpenStudio/resources/defaults.rb#L5302)

[11  https://github.com/NatLabRockies/resstock/blob/v3.4.0/resources/hpxml-measures/HPXMLtoOpenStudio/resources/defaults.rb](https://github.com/NREL/resstock/blob/v3.4.0/resources/hpxml-measures/HPXMLtoOpenStudio/resources/defaults.rb)

[12 https://github.com/NatLabRockies/resstock/tree/v3.4.0/resources/hpxml-measures/HPXMLtoOpenStudio/resources](https://github.com/NREL/resstock/tree/v3.4.0/resources/hpxml-measures/HPXMLtoOpenStudio/resources)

[13  https://github.com/NatLabRockies/resstock/blob/c832c19668561f31f2ff1bcc34828d60f518fec5/resources/hpxml-measures/HPXMLtoOpenStudio/resources/hvac.rb#L555-L928](https://github.com/NREL/resstock/blob/c832c19668561f31f2ff1bcc34828d60f518fec5/resources/hpxml-measures/HPXMLtoOpenStudio/resources/hvac.rb#L555-L928)

