<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86103.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/86103.md | section: Indoor Unit Performance | lines: 557-560 -->
## Indoor Unit Performance

The VRF objects in EnergyPlus also requires specification of indoor/terminal units which is basically configuring a heat exchanger: rated capacity, rated sensible heat ratio, rated air flow rate, and capacity modifier performance curves. All specifications for indoor units follow the workflow defined in Openstudio Standards [30] where capacity of the indoor unit is based on zone sizing calculation and the other configurations (including performance curves) are following the EnergyPlus default parameters and, when applicable, overridden by energy code as describe in the ComStock documentation [17].

