<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/87542.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/87542.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/87542.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/87542.md | section: 3.2.2 Heat/Energy Recovery Effectiveness | lines: 410-423 -->
## 3.2.2 Heat/Energy Recovery Effectiveness

Both the energy recovery and heat recovery systems are modeled using the effectiveness performance of the Ventacity systems shown in Figure 2 [6]. EnergyPlus allows latent and sensible effectiveness to be set to 100% and 75% airflow, respectively, for both heating and cooling, which can be determined from Ventacity performance curves. Because the heat recovery system is only suitable for sensible energy recovery, the latent effectiveness is modeled as 0% for all cases. The modeled inputs for effectiveness are shown in Table 3. Note that the Ventacity system is an ERV or HRV with heat or energy recovery included. For a retrofit application, the type of heat/energy recovery appropriate for the use case may warrant a different type of system, which could impact the effectiveness assumptions.

Table 3. Modeled Effectiveness Inputs for Energy and Heat Recovery Based on Ventacity Systems Shown in Figure 2

|                       | ER      | ER      | HR      | HR      |
|-----------------------|---------|---------|---------|---------|
|                       | Heating | Cooling | Heating | Cooling |
| Sensible 100% Airflow | 75%     | 75%     | 84%     | 83%     |
| Sensible 75% Airflow  | 78%     | 78%     | 86%     | 84%     |
| Latent 100% Airflow   | 61%     | 55%     | 0%      | 0%      |
| Latent 75% Airflow    | 68%     | 60%     | 0%      | 0%      |

