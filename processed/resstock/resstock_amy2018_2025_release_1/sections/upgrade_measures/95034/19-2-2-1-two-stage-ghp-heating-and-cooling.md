<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95034.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95034.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95034.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95034.md | section: 2.2.1  Two-Stage GHP Heating and Cooling Efficiency | lines: 252-263 -->
## 2.2.1  Two-Stage GHP Heating and Cooling Efficiency

This measure includes a water-to-air GHP with a two-stage compressor rated at a heating coefficient of performance (COP) of 4.0 and a rated cooling energy efficiency ratio (EER) of 20.5. The ground heat exchanger shape and properties are the same as used for the single-stage GHP: rectangular and vertically drilled single U-tube design with thermally enhanced grout and piping. This section will describe the inputs and modeling methodology for the heat pump. Refer to the single-stage GHP model documentation (Maguire et al. 2025) for inputs and methodology not discussed in this document.

The ResStock arguments assigned in the 'HVAC Heating Efficiency' characteristic (different than the default OpenStudio-HPXML defaults) that help distinguish the two-stage GHP from the single-stage GHP are:

- Heat pump compressor type
- Heat pump heating efficiency
- Heat pump cooling efficiency.

For this measure, the compressor type is two-stage, as stated by the measure definition.

