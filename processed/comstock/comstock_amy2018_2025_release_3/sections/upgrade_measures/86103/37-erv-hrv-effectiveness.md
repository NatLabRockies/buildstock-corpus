<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86103.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/86103.md | section: ERV/HRV Effectiveness | lines: 596-609 -->
## ERV/HRV Effectiveness

Both the ERV and HRV systems are modeled using the effectiveness performance of the Ventacity systems (that comply NEEA's very high efficiency DOAS) shown in Figure 3 [9]. EnergyPlus allows the specification of latent and sensible effectiveness at 100% and 75% airflow for both heating and cooling, which can be determined from Ventacity performance curves. Because the HRV system is only suitable for sensible energy recovery, the latent effectiveness is modeled as 0% for all cases. The modeled inputs for effectiveness are shown in Table 4.

Table 4. Modeled Effectiveness Inputs for ERV and HRV Based on Ventacity Systems Shown in Figure 3

|                       | ERV     | ERV     | HRV     | HRV     |
|-----------------------|---------|---------|---------|---------|
|                       | Heating | Cooling | Heating | Cooling |
| Sensible 100% Airflow | 75%     | 75%     | 84%     | 83%     |
| Sensible 75% Airflow  | 78%     | 78%     | 86%     | 84%     |
| Latent 100% Airflow   | 61%     | 55%     | 0%      | 0%      |
| Latent 75% Airflow    | 68%     | 60%     | 0%      | 0%      |

