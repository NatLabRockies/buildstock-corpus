<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96413.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96413.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96413.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96413.md | section: 3.2.1 ResStock Inputs for the Typical Cold Climate Heat Pump Upgrade | lines: 328-390 -->
## 3.2.1 ResStock Inputs for the Typical Cold Climate Heat Pump Upgrade

Inputs from ResStock that describe the typical cold climate heat pump are listed in the table below. These inputs include both the ResStock 'HVAC Heating Efficiency' and 'HVAC Detailed Performance Data' parameters, with the latter noted with an asterisk. Descriptions of each of these arguments can be found in Table 81 of the ResStock Technical Reference Documentation (Reyna, et al. 2025).

Table 4. ResStock Argument Values for the Typical Cold Climate Heat Pump

<!-- table recovered from measure_pdfs/96413.pdf p.19
     overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/96413.yaml
     method: pdf-text-layer
     supersedes the extractor's own table here (values 737d036358fd…):
     and its continuation grid(s) (values 3dc9d1adb303…):
       The table runs over pages 19 and 20 and was extracted as two grids. In the first, the last value of hvac_perf_data_heating_max_speed_cops* (1.490) fell out of its cell and sits below the grid as a paragraph, leaving four of five values in the row; and the minus sign of -15.0 in the heating outdoor temperatures was split from its number. Every other cell matched pages 19 and 20 and is the extractor's own. Split into three sub-tables so no group is cut mid-row. The 'Calculated by OpenStudio-HPXML?' cell of heat_pump_compressor_lockout_temp is blank on the page. -->

**Heat pump arguments**

| ResStock Argument | Typical Cold Climate Heat Pump | Calculated by OpenStudio-HPXML? |
|---|---|---|
| heat_pump_type | air-to-air | No |
| heat_pump_heating_efficiency_type | HSPF2 | No |
| heat_pump_heating_efficiency | 8.5 | No |
| heat_pump_cooling_efficiency_type | SEER2 | No |
| heat_pump_cooling_efficiency | 17.5 | No |
| heat_pump_sizing_methodology | max load | No |
| heat_pump_sizing_is_duct_limited | FALSE | Yes |
| heat_pump_fraction_heat_load_served | 1 | No |
| heat_pump_fraction_cool_load_served | 1 | No |
| heat_pump_backup_type | integrated | No |
| heat_pump_backup_fuel | electricity | No |
| heat_pump_backup_heating_efficiency | 1 | No |
| heat_pump_backup_heating_capacity | auto | Yes |
| heat_pump_is_ducted | TRUE | No |
| heat_pump_compressor_lockout_temp | -15.0°F |  |
| heat_pump_cooling_compressor_type | variable speed | No |

**HVAC detailed performance data: capacity type and heating**

| ResStock Argument | Typical Cold Climate Heat Pump | Calculated by OpenStudio-HPXML? |
|---|---|---|
| hvac_perf_data_capacity_type* | normalized capacity fractions | No |
| hvac_perf_data_heating_outdoor_temperatures* | 67.0, 47.0, 17.0, 5.0, −15.0 (all °F) | No |
| hvac_perf_data_heating_min_speed_capacities* | 0.423, 0.308, 0.353, 0.371, 0.331 | No |
| hvac_perf_data_heating_max_speed_capacities* | 1.387, 1.028, 0.766, 0.688, 0.507 | No |
| hvac_perf_data_heating_min_speed_cops* | 5.150, 4.390, 2.550, 2.050, 1.660 | No |
| hvac_perf_data_heating_max_speed_cops* | 3.684, 3.370, 2.330, 1.980, 1.490 | No |

**HVAC detailed performance data: cooling**

| ResStock Argument | Typical Cold Climate Heat Pump | Calculated by OpenStudio-HPXML? |
|---|---|---|
| hvac_perf_data_cooling_outdoor_temperatures* | 125.0, 95.0, 82.0, 70.0 (all °F) | No |
| hvac_perf_data_cooling_min_speed_capacities* | 0.267, 0.333, 0.368, 0.391 | No |
| hvac_perf_data_cooling_max_speed_capacities* | 0.847, 1.017, 1.090, 1.148 | No |
| hvac_perf_data_cooling_min_speed_cops* | 1.918, 3.870, 5.860, 7.126 | No |
| hvac_perf_data_cooling_max_speed_cops* | 2.017, 3.220, 4.140, 4.900 | No |

Arguments denoted with an asterisk (*) signify arguments used for the HVAC Detailed Performance Data ResStock parameter.

<!-- text repaired by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/96413.yaml
     The last value of hvac_perf_data_heating_max_speed_cops* in Table 4, which fell out of its cell and was left as a paragraph below the table. The hand-authored Table 4 carries it in its row, so the fragment is only a stray number.
     removed line: 1.490 -->

Values from the detailed performance data parameter are used to access a lookup table in OSHPXML to determine the performance of the heat pump. The lookup tables in OS-HPXML approximate the equation below according to the performance data inputs from ResStock (Cutler, et al. 2013). No flow fraction curves are used because the temperature data at the minimum and maximum speeds are assumed to account for airflow variation.

