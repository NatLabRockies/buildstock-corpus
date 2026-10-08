<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89131.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89131.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89131.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89131.md | section: 3.2.1 Sizing | lines: 288-295 -->
## 3.2.1 Sizing

While the EnergyPlus model of the system uses two separate coils to represent heating and cooling operation, in reality, a water-to-air heat pump has a single refrigerant-to-air coil that performs either heating or cooling, depending on the mode. Because water-to-air heat pump coils often require relatively high minimum entering air temperatures of 50°F-55°F [4], [5], an electric preheat coil to temper outdoor air is modeled in the packaged unit.

The preheat coil is sized to temper the expected mixed air flow rate, with outdoor air at design heating conditions (to 55°F) to provide a suitable entering air temperature for the heat pump coil. The heat pump coils are then sized for the design cooling load, with a supplemental electric coil providing additional heating if the design heating load exceeds the design cooling load. This is consistent with common heat pump sizing practices in industry.

The capacity of the ground loop is sized based on a common benchmark assumption of flow rate per unit load (3 gallons per minute per ton) [8].

