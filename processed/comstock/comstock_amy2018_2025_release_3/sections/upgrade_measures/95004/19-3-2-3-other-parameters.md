<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95004.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95004.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95004.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/95004.md | section: 3.2.3  Other Parameters | lines: 355-362 -->
## 3.2.3  Other Parameters

The DC-to-AC size ratio compares an inverter's AC rating to the array's DC rating. This study uses the PVWatts default of value of 1.10 for all systems. This means that a PV array with a nameplate capacity of 10 kW DC would have an inverter nameplate of 9.1 kW AC. This is modeled in PVWatts by limiting the power output based on the rated AC size [7]. Note that this parameter can be optimized to life cycle cost when designing PV systems, although this type of detailed analysis is not included in this work. This value can vary substantially, with estimates ranging from 1.1-1.3 [8]. The PVWatts assumption of 1.1 is on the conservative end, with higher values potentially providing more favorable economics in some cases.

In this work, the inverter efficiency is modeled at 96% for all models, which is the default in PVWatts [4]. This value reflects the nominal rated AC-to-DC conversion efficiency and is the ratio between the inverter's rated AC power to DC power. For example, this represents a system with 9.6 kW AC and 10 kW DC.

In this work, the system losses are modeled at 14% for all models, which is the default in PVWatts [4]. This is used to account for losses in real systems that are not explicitly modeled in PVWatts calculations, such as panel or inverter failure.

