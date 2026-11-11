<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95036.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95036.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95036.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95036.md | section: 2.2.1  Variable-Speed GHP Heating and Cooling Efficiency | lines: 255-266 -->
## 2.2.1  Variable-Speed GHP Heating and Cooling Efficiency

This measure includes a water-to-air GHP with a variable-speed compressor rated with a heating COP of 4.4 and a rated cooling EER of 30.9. The ground heat exchanger shape and properties are the same as used for the single- and two-stage GHPs: a rectangular and vertically drilled single U-tube design with thermally enhanced grout and piping. This section describes the inputs and modeling methodology for the heat pump. Some inputs, the sizing methodology, and the modeling methodology for the heat pump and the ground heat exchanger are the same as for the single- and two-stage GHPs. Refer to the section with the corresponding name in those documents for additional details.

Many ResStock arguments are assigned in the HVAC heating efficiency characteristic. The arguments being specified (different than the OpenStudio-HPXML defaults) that help distinguish these technologies from the single- and two-stage GHP are:

- Heat pump compressor type
- Heat pump heating efficiency
- Heat pump cooling efficiency.

For this measure, the compressor type is variable speed, as stated by the measure definition.

