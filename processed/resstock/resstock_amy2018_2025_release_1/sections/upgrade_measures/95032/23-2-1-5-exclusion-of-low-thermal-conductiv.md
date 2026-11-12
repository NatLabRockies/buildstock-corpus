<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95032.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: upgrade_measures/measure_pdfs/95032.md | section: 2.1.5 Exclusion of Low Thermal Conductivity Soils | lines: 293-300 -->
## 2.1.5 Exclusion of Low Thermal Conductivity Soils

We have chosen not to include low thermal conductivity soils in our GHP upgrade logic. In real systems, these soil conditions can significantly reduce the performance of ground heat exchangers and may require larger, more expensive loop fields to maintain system efficiency.

When we try to model these scenarios, we often run into simulation failures or unstable results. These issues make it difficult to trust the upgrade impacts, especially when scaling across a large number of homes. Additionally, soil thermal properties can vary a lot and may not be well represented in the data we have, which adds more uncertainty.

The result is that we are not applying these GHPs to units with a ground thermal conductivity of 0.5 Btu/hr-ft-F to 0.8 Btu/hr-ft-F which make up 7.6% of the total building stock based on (X. W. Liu 2016). This helps ensure the model results are reliable and representative of scenarios where GHPs are more likely to perform well in practice.

