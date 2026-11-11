<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95036.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95036.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95036.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95036.md | section: 2.3  Limitations and Concerns | lines: 442-451 -->
## 2.3  Limitations and Concerns

In addition to the limitations and concerns discussed in the prior single-stage and two-stage GHP documents, the following concerns are unique to variable-speed GHPs:

- EMS program flow rate calculation: The EMS program used for variable-speed GHPs calculates the pump mass flow rate based on the steady-state heat pump capacities. Although this approach is sufficient for most conditions, it could introduce minor differences in the mass flow estimates, which could slightly affect flow-rate-dependent capacity and efficiency curves.
- Limited compressor speed data: Only two speeds are explicitly modeled due to limitations in the manufacturer data for the variable-speed unit used here. Interpolation between these speeds, along with water flow and airflow-rate-dependent curves, is applied to represent performance across the full operating range.
- Part-load representation: Unlike single- or two-stage systems, no part-load ratio to partload fraction curve is applied for the variable-speed model. In EnergyPlus, the system is assumed to continuously modulate between 0 and 100% capacity, even at very low-load fractions. In reality, at extremely low-load conditions (for example, 5% of the maximum load), even variable-speed equipment might cycle on and off to meet the load seen during

the time step in EnergyPlus. Because of the small amount of time and energy spent at fractions such as 5% or below, this better captures the overall energy performance of this equipment.

