<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89040.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89040.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89040.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/89040.md | section: 3.2.3  Other Modeling Updates | lines: 334-340 -->
## 3.2.3  Other Modeling Updates

There are several fixes we made that did not happen in the previous work. These are listed below, which are from simple mistakes to EnergyPlus ®  source code limitations:

- The implementation of maximum operating temperature for heat pump heating was overlooked in the previous implementation. While manufacturer data showed that heat pump heating gets locked out when the outdoor air temperature is above 86°F (30°C), the actual value that was implemented in previous simulations was 61°F (16°C). The maximum operating temperature for heat pump heating is now corrected to 86°F (30°C).
- There are many output variables shown in Section 3 that are being reported after a ComStock run. While the design COP of a VRF heat pump at -22°F was initially implemented in the workflow to provide performance indicators of the cold climate heat pump, it was discovered that this output was never reported after the actual ComStock run. This output is fixed in this iteration.

