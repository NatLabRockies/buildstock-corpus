<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86199.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/86199.md | section: 4  Modeling Approach | lines: 388-408 -->
## 4  Modeling Approach

According to the Commercial Buildings Energy Use Survey (CBECS), natural gas used by boilers and furnaces accounts for 73% of space heating energy consumption in U.S. commercial buildings [4]. Electrifying these heat sources would have a considerable impact in achieving climate coals. This measure replaces natural gas boilers for HVAC applications by heat pump boilers. Outputs from the simulation runs could be used to quantify the carbon reduction and energy impact of the electrification.

The measure provides multiple options for the natural gas boiler replacement. Table 3 summarizes the measure inputs and their default values used in the simulation run.

Table 3. Measure Input Summary

| Measure Inputs   | Description                                                                                                                                  | Default Value              | Units True/False   |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|--------------------|
| Keep_setpoint    | Provides an option to keep the original hot water set point.                                                                                 | False                      |                    |
| autosize_hc      | value. Provides an opportunity to auto-size heating coils when a user provides a new hot water set point.                                    | True                       | True/False         |
| Sizing_method    | Provides an option for sizing the heat pump. The two options are sizing based on 'percentage of peak load' and on 'outdoor air temperature.' | Outdoor air temperature    |                    |
| hp_sizing_temp   | Provides the outdoor air temperature on which to base ASHP sizing if user chooses the sizing method as 'outdoor air temperature.'            | 17                         | ° F                |
| hp_sizing_per    | Provides the percentage of the peak heating load on which to base the if user chooses the sizing method as                                   | 70                         | %                  |
| hp_des_cap       | sizing 'percentage of peak load.' Maximum design heat pump heating                                                                           | 40                         | kW                 |
| bu_type          | Provides two options for backup heater: keeping the existing boiler or adding an electric resistance heater.                                 | Electric resistance heater |                    |
| hpwh_cutoff_Temp | Provides the cutoff temperature for the heat pump boiler.                                                                                    | - 5                        | ° F                |
| hpwh_Design_OAT  | Provides design outdoor air temperature for the heat pump boiler.                                                                            | 47                         | ° F                |
| COP              | Provides the design coefficient of performance (COP) at the design outdoor air temperature.                                                  | 2.85                       |                    |

