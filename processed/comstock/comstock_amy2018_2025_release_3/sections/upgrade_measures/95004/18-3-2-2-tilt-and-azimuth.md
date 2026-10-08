<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95004.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95004.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95004.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/95004.md | section: 3.2.2 Tilt and Azimuth | lines: 344-356 -->
## 3.2.2 Tilt and Azimuth

Tilt angle is measured as the angle of the panel relative to horizontal. A completely horizontal panel has a tilt angle of 0 degrees, while a vertical panel has a tilt angle of 90 degrees. Azimuth angle is measured as the angle clockwise to true north. A completely north-facing array has an azimuth angle of 0 degrees, while a south facing array has an azimuth angle of 180 degrees.

The PV arrays modeled in this work are assumed to be fixed, so tilt and azimuth are set at a fixed value for each model and remain constant throughout the simulation. They are calculated using the methodology from [6] to optimize the two parameters for maximizing solar collection based on latitude (summarized in Table 2). This represents one method for determining orientation, although others could be considered depending on what you are optimizing for (e.g. time of use pricing). Note that the tilt angle is always at least 10 degrees to allow rainwater to effectively clean the panels. The panels are not spaced, and are essentially modeled as one large, tilted panel with an area equaling 40% of the roof area.

Table 2. Title Formula by Orientation

| Orientation         |   Azimuth (°) | Tilt Formula                                                                                             |
|---------------------|---------------|----------------------------------------------------------------------------------------------------------|
| Northern Hemisphere |           180 | Tilt = 1.3793 + (Latitude ) × [1.2011 + (Lat) × (-0.014404 + (Lat itude) × 0.000080509)]                 |
| Southern Hemisphere |             0 | Tilt = &#124;-0.41657 + ( Latitude) × [1.4216 + (Latitude) × (0.024051 + (Latitude) × 0.00021828)]&#124; |

