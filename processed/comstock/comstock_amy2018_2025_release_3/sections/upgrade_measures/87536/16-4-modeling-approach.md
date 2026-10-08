<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/87536.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/87536.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/87536.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/87536.md | section: 4  Modeling Approach | lines: 372-396 -->
## 4  Modeling Approach

According to the Commercial Buildings Energy Consumption Survey (CBECS), natural gas used by boilers and furnaces accounts for 73% of space-heating energy consumption in U.S. commercial buildings [4]. This measure replaces natural gas boilers used for HVAC applications with heat pump boilers. The results of the simulations could be used to estimate the carbon reduction and energy impacts from electrifying these boilers.

The measure provides several options for replacing natural gas boilers. Table 1 summarizes the measure inputs and their default values used in the simulation run.

Table 3. Measure Input Summary

| Description                                                                                                                      | Default Value           | Units      |
|----------------------------------------------------------------------------------------------------------------------------------|-------------------------|------------|
| Option to keep the original hot water set point.                                                                                 | False                   | True/False |
| New hot water set point if user chooses to change the original value.                                                            | 140                     | ° F        |
| Option to auto-size heating coils when a user provides a new hot water set point.                                                | True                    | True/False |
| Option for sizing the heat pump. The two options are sizing based on 'percentage of peak load' and on 'outdoor air temperature.' | Outdoor air temperature | -          |
| Outdoor air temperature on which to base ASHP sizing if user chooses the sizing method as 'outdoor                               | 17                      | ° F        |
| Percentage of the peak heating load on which to base the sizing if user chooses the sizing method as                             | 70                      | %          |
| Maximum design heat pump heating capacity per unit. If the model requires a higher capacity, multiple                            | 40                      | kW         |

| Measure Inputs    | Description                                                                                         | Default Value      | Units   |
|-------------------|-----------------------------------------------------------------------------------------------------|--------------------|---------|
| bu_type           | Two options for backup heater: keeping the existing boiler or adding an electric resistance boiler. | Natural gas boiler | -       |
| hpwh_cutoff_Te mp | Cutoff temperature for the heat pump boiler.                                                        | - 5                | ° F     |
| hpwh_Design_O AT  | Design outdoor air temperature for the heat pump boiler.                                            | 47                 | ° F     |
| COP               | Design coefficient of performance (COP) at the design outdoor air temperature.                      | 2.85               | -       |

