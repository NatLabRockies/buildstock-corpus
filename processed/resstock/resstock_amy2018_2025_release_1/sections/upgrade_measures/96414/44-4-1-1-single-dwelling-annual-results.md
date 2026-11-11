<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96414.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96414.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96414.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96414.md | section: 4.1.1 Single Dwelling Annual Results | lines: 426-446 -->
## 4.1.1 Single Dwelling Annual Results

Table 7 presents the modeled annual energy consumption savings for key outputs for both individual dwelling test models. Both dwellings show expected savings, except for an increase in heating fans and pumps energy for Dwelling 2 and cooling fans and pump energy for Dwelling 1. The heat pump airflow rate is higher than typical furnace airflow rates, so the cooling and heating fans will not experience significant savings, if any. At the time of these simulations and dataset release, the heat pump fan airflow rate was used during backup heating mode due to a bug in the EnergyPlus software. This bug contributes to the low savings for heating fans. The EnergyPlus development team has been notified about the bug and no resolution has occurred at the time of this publication.

The N/A values for 'Electricity-Heating (incl. backup)' are due to from the absence of electric heating in the dwellings in the baseline. The nonzero electric heating in the upgrade results in an infinite increase in this category's energy consumption for both dwellings. For Dwelling 1, the increase in electric heating is reflected in the 'Utility Bills-Electricity' category. However, since Dwelling 2 requires far fewer heating hours than Dwelling 1, its savings for 'Utility Bills-Electricity' is only slightly negative.

Table 7. Savings in Annual Energy Consumption and Utility Bills for Two Individual Dwelling Test Models

The N/A value for the 'Electricity-Heating (incl. backup)' reflects the fact that each individual dwelling model had 0 electricity consumption for heating in the baseline.

| Dwelling ID                        | 1      | 2       |
|------------------------------------|--------|---------|
| Electricity-Cooling                | 25.6%  | 8.3%    |
| Electricity-Cooling Fans and Pumps | -69.0% | 25.7%   |
| Electricity-Heating (incl. backup) | N/A    | N/A     |
| Electricity-Heating Fans and Pumps | 5.8%   | -361.0% |
| Natural Gas-Heating                | 27.3%  | 79.2%   |
| Site Energy-Total                  | 13.9%  | 20.2%   |
| Utility Bills-Electricity          | -23.5% | -2.3%   |
| Utility Bills-Natural Gas          | 21.6%  | 31.2%   |

