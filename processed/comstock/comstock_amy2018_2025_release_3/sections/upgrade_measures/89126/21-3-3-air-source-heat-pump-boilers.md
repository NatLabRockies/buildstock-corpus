<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89126.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/89126.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/89126.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89126.md | section: 3.3 Air-Source Heat Pump Boilers | lines: 372-391 -->
## 3.3 Air-Source Heat Pump Boilers

The ASHP Boiler upgrade replaces natural gas boilers for space heating with ASHP boilers. The upgrade provides multiple options for the natural gas boiler replacement. Table 4 summarizes the upgrade inputs and their default values used in the simulation run.

Table 4. Upgrade Input Summary

| Upgrade Inputs   | Unit/Value   | Description                                                                                                                                  | Default Value              |
|------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| keep_setpoint    | True/False   | Provides an option to keep the original hot water set point.                                                                                 | False                      |
| hw_setpoint      | °F           | Provides a new hot water set point if user chooses to change the original value.                                                             | 140                        |
| autosize_hc      | True/False   | Provides an opportunity to auto- size heating coils when a user provides a new hot water set point.                                          | True                       |
| Sizing_method    | -            | Provides an option for sizing the heat pump. The two options are sizing based on 'percentage of peak load' and on 'outdoor air temperature.' | Outdoor air temperature    |
| hp_sizing_temp   | °F           | Provides the outdoor air temperature on which to base ASHP sizing if user chooses the sizing method as 'outdoor air                          | 17                         |
| hp_sizing_per    | %            | Provides the percentage of the peak heating load on which to base the sizing if user chooses the sizing method as 'percentage of peak load.' | 70                         |
| hp_des_cap       | kW           | Maximum design heat pump heating capacity per unit. If the model requires a higher capacity, multiple units will be added in the loop.       | 40                         |
| bu_type          | -            | Provides two options for backup heater: keeping the existing boiler or adding an electric resistance heater.                                 | Electric resistance heater |
| hpwh_cutoff_Temp | °F           | Provides the cutoff temperature for the heat pump boiler.                                                                                    | -5                         |
| hpwh_Design_OAT  | °F           | Provides design outdoor air temperature for the heat pump boiler.                                                                            | 47                         |
| COP              | -            | Provides the design COP at the designated outdoor air temperature.                                                                           | 2.85                       |

