<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89481.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89481.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89481.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89481.md | section: 3.2.3  Energy Recovery Effectiveness | lines: 384-401 -->
## 3.2.3  Energy Recovery Effectiveness

Both the energy recovery and heat recovery systems are modeled using the effectiveness performance of the Ventacity systems shown in Table 3 [9]. These values dictate how much energy is transferred between the supply and exhaust airstreams and will vary based on specific products and configurations. Note that the Ventacity system is an energy recovery ventilator, which would not be installed inside a packaged RTU. These performance values are used since Ventacity publishes detailed performance data that can be leveraged for energy modeling. In practice, it is likely more common to choose an RTU with heat/energy recovery already integrated into the system, like the options available for the Daikin Rebel, rather than a separate system.

EnergyPlus allows latent and sensible effectiveness assignments at 100% and 75% airflow, respectively, for both heating and cooling, which can be determined from Ventacity performance curves. Because the heat recovery system is only suitable for sensible energy recovery, the latent effectiveness is modeled as 0% for all cases. The modeled inputs for effectiveness are shown in Table 3. Note that performance values can change based on product selection, configuration, and operation.

Table 3. Modeled Effectiveness Inputs for Energy and Heat Recovery Based on Ventacity Systems Shown in Figure 1

|                       | Energy Recovery   | Energy Recovery   | Heat Recovery   | Heat Recovery   |
|-----------------------|-------------------|-------------------|-----------------|-----------------|
|                       | Heating           | Cooling           | Heating         | Cooling         |
| Sensible 100% Airflow | 75%               | 75%               | 84%             | 83%             |
| Sensible 75% Airflow  | 78%               | 78%               | 86%             | 84%             |
| Latent 100% Airflow   | 61%               | 55%               | 0%              | 0%              |
| Latent 75% Airflow    | 68%               | 60%               | 0%              | 0%              |

As mentioned, ComStock does account for zone exhaust fans in some building types, but not in offices, retail buildings, or warehouses, which are prominent in the stock. Furthermore, ComStock does not currently account for duct leakage. A PNNL study using the DOE prototype models assumes that 90% of exhaust air is available for energy recovery to account for both zone exhaust and duct losses [6]. To account for this, the energy/heat recovery measure assumes that 90% of return air is available for recovery through a derating of the recovery effectiveness.

