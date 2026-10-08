<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89120.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89120.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89120.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89120.md | section: 3.2  Technology Specifics Such as Sizing, Performance, and Configuration | lines: 207-214 -->
## 3.2  Technology Specifics Such as Sizing, Performance, and Configuration

This measure will iterate through air loops in a building and set the minimum outdoor air schedule for each Controller:OutdoorAir to be identical to the availability manager schedule for the air loop, so that no requirement for a minimum outdoor air level for ventilation is applied when the area served by the air loop is unoccupied. Because this is simply setting the minimum level of outdoor airflow to zero, it continues to allow for airside economizing.

ASHRAE 90.1. permits use of outdoor air during unoccupied periods for airside economizing. Specifically, ASHRAE 90.1 2022 (Section 6.4.3.4.2) provides an exception to the requirement for ventilation control during unoccupied periods for 'when the supply of outdoor air reduces energy costs,' or when outdoor air must be supplied to meet code requirements (ASHRAE 2022).

This measure will also set the availability schedule of air loops to align with occupancy of their corresponding zones and create an availability manager for each air loop to configure it to cycle on if any connected zone the current temperature differs from the setpoint by more than one-half of a pre-set tolerance value.

