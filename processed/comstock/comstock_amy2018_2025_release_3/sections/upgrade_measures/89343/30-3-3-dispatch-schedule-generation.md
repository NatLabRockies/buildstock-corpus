<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89343.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89343.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89343.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89343.md | section: 3.3  Dispatch Schedule Generation | lines: 380-392 -->
## 3.3  Dispatch Schedule Generation

Different combinations of objective and load prediction methods generate different dispatch schedules. The fixed schedule method results in a predetermined dispatch schedule that could be directly used by other measures. The other load prediction methods that result in a load profile require additional parameter specification to determine dispatch windows.

Major parameters are dispatch window length and the methods to determine the start and end times of the daily dispatch window. The dispatch window length is 4 hours by default, according to the GEB guide [15]. We provide four methods to determine the start and end times of the dispatch window.

1. Center with peak: The start and end times of the window are determined so the predicted peak load/emission takes place in the middle of the window.
2. Start with peak: The start time of the window is the peak time.
3. End with peak: The end time of the window is the peak time.
4. Max savings potential: The start and end times of window are determined so the peak takes place in the window, and the summation of load/emission throughout the window is the maximum of all candidates.

Other parameters associated with specific demand flexibility measures are pre-conditioning (precooling and/or pre-heating) period length for load shifting strategy and rebound control period length for thermostat control for load shedding measure. The default settings for those parameters are specified in the corresponding measure documentations when applicable.

