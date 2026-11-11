<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/93846.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/93846.md | section: 3.3  Input Variables | lines: 457-470 -->
## 3.3  Input Variables

There are two types of input variables: input variables for load flexibility scenario design and onpeak hour inputs. On-peak hour inputs are provided as a json file to indicate the peak hour start and end time at the state level. Table 5 presents a list of input variables and settings used for this analysis. These were based on the utility programs outlined in the technology overview in consultation with the demand flexibility modelers using the outputs of this analysis.

Table 5. Input Variables for HVAC Load Flexibility

| Variable Name                    | Description                                                                                                                                       | Value                                   |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| loadflex_peak_offset             | Set point offset value during the peak period in degrees Fahrenheit. The set point is increased for cooling, and it is decreased for heating.     | 2 - 4°F                                 |
| loadflex_pre_peak_duration_hours | Duration of the pre-peak period in hours                                                                                                          | 1 - 4 hours                             |
| loadflex_pre_peak_offset         | Set point offset value during the pre-peak period in degrees Fahrenheit. The set point is decreased for cooling, and it is increased for heating. | 2 - 4°F                                 |
| loadflex_random_shift_minutes    | Maximum minutes to randomly shift the peak period. If the minutes are less than the time step, they will be assumed to be 0.                      | 30 minutes                              |
| peak_start_time                  | The time (local time) the peak period starts                                                                                                      | Varies by state and season; see Table 3 |

