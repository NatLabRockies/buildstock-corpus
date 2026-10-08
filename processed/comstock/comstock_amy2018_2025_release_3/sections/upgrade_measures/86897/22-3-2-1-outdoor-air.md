<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86897.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86897.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86897.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/86897.md | section: 3.2.1 Outdoor Air | lines: 404-409 -->
## 3.2.1 Outdoor Air

For the EnergyPlus DCV function to work properly, a space needs both a per-person and perarea outdoor air rate specified. In OpenStudio ®  Standards, some space types have either 100% per-person or 100% per-area outdoor air rates specified. For these spaces on applicable air loops, outdoor air rates are converted to a per-person rate of 10 CFM/person, and the remainder of the outdoor air requirement is assigned as per-area.

Air loops that serve both applicable and inapplicable space types will have DCV applied but will only function in spaces that are applicable. To do this, inapplicable space types will have their outdoor air rates converted to 100% per-area to avoid triggering the EnergyPlus function.

