<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89343.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89343.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89343.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/89343.md | section: 4.2  Computational Efficiency of the Bin-Sampling Method | lines: 437-450 -->
## 4.2  Computational Efficiency of the Bin-Sampling Method

The bin-sampling method was proposed as a compromise between computational effort and prediction accuracy within the constraints of the ComStock workflow, based on the intuitive assumption that simulations on a small number of days (samples) would be computationally lighter compared to a full annual simulation and thus should take less computational time for load prediction than the perfect load prediction method. However, the bin-sampling method underperformed in test implementation regarding computational time (much longer time consumed) when applied with the demand flexibility measure of load shedding in a ComStock run with 90 applicable building models (large offices with electric HVAC systems). The test run results are summarized in Table 5.

Table 5. Consumed Run Time With the Load Shedding Measure With Different Dispatch Schedule Generation Options

| Scenarios                                          | Run Time (HH:MM:SS)   |
|----------------------------------------------------|-----------------------|
| 15:40:04                                           | Baseline              |
| Load shedding measure with perfect load prediction | 23:42:50              |
| Load shedding measure with bin-sampling method     | 43:38:12              |

The reason for the unexpected extra time used by the bin-sampling method is the repeated presimulation steps for EnergyPlus ® /OpenStudio ®  simulation (warm-up and sizing) for each sample daily simulation. This issue has not been resolved at the time of release, and future work is needed to make the bin-sampling method more feasible in terms of computational time.

