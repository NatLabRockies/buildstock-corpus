<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96405.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96405.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96405.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: upgrade_measures/measure_pdfs/96405.md | section: 3.2.2  Default Inputs From OpenStudio-HPXML | lines: 433-445 -->
## 3.2.2  Default Inputs From OpenStudio-HPXML

There are no default values set by OpenStudio-HPMXL for this measure. However, one important modeling approach that OpenStudio-HPXML uses is worth mentioning. The windows in the model use EnergyPlus' 'WindowMaterial:SimpleGlazingSystem' object. For this object, OpenStudio-HPXML only fills in the U-factor and SHGC fields, and leaves the optional visible transmittance field blank. According to the EnergyPlus documentation, when this field is left blank 'the visible transmittance properties are taken from the solar properties.' Table 10 shows the visible transmittance values assumed by EnergyPlus based on the input U-factor and SHGC.

Table 10. Visible Transmittance Values Calculated by EnergyPlus Given U-Factor and SHGC

| Climate Zone   |   U-Factor (Btu/h ft 2 ∙˚F) |   SHGC |   Visible Transmittance |
|----------------|-----------------------------|--------|-------------------------|
| Northern       |                        0.22 |   0.17 |                   0.081 |
| North-Central  |                        0.25 |   0.40 |                   0.315 |
| South-Central  |                        0.28 |   0.23 |                   0.142 |
| Southern       |                        0.32 |   0.23 |                   0.142 |

