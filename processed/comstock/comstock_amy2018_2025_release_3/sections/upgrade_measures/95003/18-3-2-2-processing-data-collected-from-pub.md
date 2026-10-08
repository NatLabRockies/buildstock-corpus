<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95003.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95003.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95003.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/95003.md | section: 3.2.2  Processing Data Collected From Public Resources | lines: 366-377 -->
## 3.2.2  Processing Data Collected From Public Resources

Based on the distinct differences in chiller performances shown in Table A-1 (with key highlights in Section 3.2.1), we have translated the real-world data into EnergyPlus ® /OpenStudio ® -compatible inputs using the following criteria:

- Exclude chillers in Table A-1 where performance metrics (i.e., full-load EER and IPLV EER) fall below the ASHRAE 90.1-2019 standard, which is the latest benchmark used in our models. This ensures that the remaining data points represent the most efficient and marketavailable options.
- Calculate the arithmetic average full-load EER separately for air-cooled and water-cooled chillers.
- Calculate the arithmetic average IPLV EER separately for air-cooled and water-cooled chillers.
- For creating performance curves, we found two options:

- Use Pacific Northwest National Laboratory's Copper tool [20], [21] to generate partload performance curves from IPLV EER values for air-cooled and water-cooled chillers independently. This option was chosen for creating new performance curves.
- Use manufacturers' published performance maps to generate a new set of curves. Based on the data collected during this exercise, not all manufacturers provide relevant performance maps (e.g., capacity and EER variations under different operating conditions). Therefore, while we are not endorsing any specific manufacturer, this approach will ultimately reflect the performance of only one manufacturer's chiller. Refer to the 'Include performance map?' column in Table A1 to see which chillers include performance maps. This option was not chosen in this study for creating new performance curves.

