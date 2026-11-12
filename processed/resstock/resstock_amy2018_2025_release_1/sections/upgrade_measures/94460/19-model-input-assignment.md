<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/94460.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/94460.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/94460.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: upgrade_measures/measure_pdfs/94460.md | section: Model Input Assignment | lines: 228-247 -->
## Model Input Assignment

We synthesize data from the external sources to characterize EV ownership, driving behavior, and charging behavior in ResStock, which ultimately influences the at-home charging energy as described in Sections 3 and 4 of Speake et al. (2025). Table 2 summarizes the ResStock input files used to characterize EV energy use and driving behavior. The ResStock input files are distributions of parameters assigned in the baseline simulation but also represent parameters that can be adjusted in a measure. ResStock leverages the OpenStudio-HPXML workflow to model individual dwelling units as OpenStudio ® models, with each ResStock option assigned one or more arguments in OpenStudio-HPXML to directly inform the energy model inputs.

Table 2. Mapping of ResStock Input Files to ResStock and OpenStudio-HPXML Arguments 4

<!-- table recovered from measure_pdfs/94460.pdf p.15
     overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/94460.yaml
     method: extracted grid, with the cells named in `why` corrected from the PDF text layer
     supersedes the extractor's own table here (values 1f3c231e839f…):
       Every cell is right, but the home-charging bin '40-59%' carries a space where the PDF breaks the line ('40- 59%'), so a search for the bin misses it; 'kilowatt-hours' was broken the same way. The cell text is the extractor's own with those two joined. Several arguments share one cell in the PDF and are run together, as extracted. -->

| ResStock Input File | ResStock Arguments | OpenStudio-HPXML Arguments | Description |
|---|---|---|---|
| Electric Vehicle Ownership | Yes, No | ev_present [bool] | Turns on/off the battery EV model. |
| Electric Vehicle Charger | L1, L2, None | ev_charger_present [bool] ev_charger_power (watts, or W) [float] | Describes presence and charging power of the EV charger. |
| Electric Vehicle Battery | Compact, Midsize, Pickup, and SUV with 200- and 300-mile ranges | ev_battery_usable_capacity (kilowatt-hours, or kWh) [float] ev_energy_efficiency (kWh/mile) [float] ev_average_mph (miles per hour, or mph) [float] | Physical description of the battery that ultimately informs charging demand; average speed used to calculate hours driven. |
| Annual Miles Driven | 14 values ranging from 1,000 to 22,500 miles | ev_miles_per_year [integer] ev_hours_per_week [float] (calculated internally from ev_miles_per_year using an assumed default average speed) | Total miles driven per year; an assumed default average speed is used to calculate ev_hours_per_week , which informs the hourly driving schedules. |
| Home Charging Fraction | 6 bins, 0-19%, 20-39%, 40-59%, 60-79%, 80-99%, 100% | ev_fraction_charged_home [float] | Describes what fraction of energy is provided by an at-home charger; informs the effective annual miles traveled for the generation of schedules. |

