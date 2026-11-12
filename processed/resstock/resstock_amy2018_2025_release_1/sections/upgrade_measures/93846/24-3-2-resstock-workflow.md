<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/93846.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: upgrade_measures/measure_pdfs/93846.md | section: 3.2  ResStock Workflow | lines: 436-456 -->
## 3.2  ResStock Workflow

Figure 2 illustrates the modeling approach used to integrate a load flexibility measure into ResStock. This measure modifies the existing building energy model thermostat set point schedules during the pre-peak and on-peak periods only. For times outside of the event, the existing thermostat schedules in the model are unchanged. If the baseline thermostat set point schedules indicate that the dwelling unit is already in a setback or a setup state, the demand flexibility thermostat change still applies.

The load flexibility scenario (which includes the pre-peak duration and the set point offset values) serves as input for the measure, allowing customized controls. The input values used for this measure are explained in section 3.3 Input Variables.

Figure 2. Modeling approach for running a load flexibility measure in ResStock

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/93846.yaml
     source: 93846_images/image_000003_06ad1ce32d34b0a4c47437dc4560d542e3896ac29aeb4ea0e7a85f2e95bb78c7.png
     method: vision-description
     described: 2026-11-11 -->

![Block diagram of the modeling approach: on-peak hour input, load flexibility measure, and results](93846_images/image_000003_06ad1ce32d34b0a4c47437dc4560d542e3896ac29aeb4ea0e7a85f2e95bb78c7.png)

Figure 2: block diagram in three columns headed On-peak Hour Input, Load Flexibility Measure and Results. The input is the on-peak hours in each state (summer, winter and intermediate peak start and end). The measure applies a relative set point offset during pre-peak and on-peak hours to the default set point schedule, with a random shift of -30 to 30 minutes, following a scenario design of pre-peak duration and offsets. Results are the baseline load profile and the profile after demand response.

Values for on-peak hours for summer months, winter months, and intermediate months are provided at the state level in an input file. The load flexibility measure first retrieves the heating and cooling set point schedules specific to each individual dwelling unit. It then modifies these schedules by adjusting the set points by an offset during the designated pre-peak and on-peak periods. This approach ensures that each unit's load flexibility aligns with its original comfort settings while providing targeted adjustments to reduce energy use during peak demand times. A minimum heating set point of 55°F and a maximum cooling set point of 82°F ensure that extreme discomfort is avoided. If the set point change would cause a heating set point higher than the original cooling set point or a cooling set point lower than the original heating set point, the set point adjustment is limited to avoid this condition. These thresholds and exceptions were chosen based on engineering judgment and only apply to a small percentage of dwelling units.

To prevent the creation of a new peak caused by the coincident return to normal set point temperatures, the load flexibility measure introduces a random shift to each dwelling unit's demand response start and stop time. The maximum allowable shift is defined in the scenario design, allowing each unit to randomly adjust its response start time within this range. For example, with a maximum random shift of 30 minutes and a 15-minute simulation time step, the potential random shift values are -30 minutes, -15 minutes, 0 minutes, 15 minutes, and 30 minutes.

