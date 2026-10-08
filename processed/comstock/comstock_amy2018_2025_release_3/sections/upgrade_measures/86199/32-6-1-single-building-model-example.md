<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86199.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/86199.md | section: 6.1  Single Building Model Example | lines: 695-732 -->
## 6.1  Single Building Model Example

Table 8 shows an end-use energy consumption comparison for a 75,000-square-foot hospital building model in Gallatin Field, MT before and after application of the default measure inputs. The two categories that are significantly affected by this measure are the heating and pump energy end uses. The electricity consumption for heating is 2.3 times lower than the natural gas consumption in the baseline. This is equivalent to an overall COP of 2.3 by the heat pump assuming a 100% efficiency boiler in the baseline model. The rated COP of the heat pump used is 2.85, and the observed reduction in the overall COP is due to a lower operating outdoor air temperature than the rated outdoor air temperature of 47°F and the use of electric resistance heater during outdoor air temperatures below the heat pump boiler cutoff temperature. The increment in the pump energy consumption is due to the addition of a constant speed circulation pump in the heat pump loop.

Table 8. End-Use Energy Consumption Comparison

|                    | Baseline         | Baseline         | Updated          | Updated          |
|--------------------|------------------|------------------|------------------|------------------|
| End Use            | Electricity [GJ] | Natural Gas [GJ] | Electricity [GJ] | Natural Gas [GJ] |
| Heating            | 0                | 6864.46          | 2976.96          | 0                |
| Cooling            | 681.2            | 0                | 681.25           | 0                |
| Interior Lighting  | 872.41           | 0                | 872.41           | 0                |
| Exterior Lighting  | 256.9            | 0                | 256.9            | 0                |
| Interior Equipment | 1860.28          | 214.09           | 1860.28          | 214.09           |
| Exterior Equipment | 0                | 0                | 0                | 0                |
| Fans               | 1188.21          | 0                | 1188.54          | 0                |
| Pumps              | 155.45           | 0                | 173.07           | 0                |
| Heat Rejection     | 0                | 0                | 0                | 0                |
| Humidification     | 0                | 0                | 0                | 0                |
| Heat Recovery      | 0                | 0                | 0                | 0                |
| Water Systems      | 285.01           | 405.9            | 285.02           | 405.9            |
| Refrigeration      | 126.52           | 0                | 126.5            | 0                |
| Generators         | 0                | 0                | 0                | 0                |
| Total End Uses     | 5425.99          | 7484.45          | 8420.95          | 619.99           |

We checked the sequencing between the heat pump and the boiler during low-temperature operation using an example cutoff temperature of 25°F ( -4°C). Figure 12 shows the operation pattern. As expected, the heat pump handled most of the load at a higher temperature. The boiler starts supplementing the ASHP as the temperatures drops and takes over all the heating when the temperature is below the cutoff temperature.

Figure 12. Sequencing between ASHP and boiler

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86199.yaml
     source: 86199_images/image_000012_01d1e052ed4f877b886e59640fb35c5cf5825f9472c4fc355cdadba5d992c70f.png
     method: vision-description
     described: 2026-08-21 -->

![Scatter plot of boiler and heat pump heating rate against outdoor air temperature](86199_images/image_000012_01d1e052ed4f877b886e59640fb35c5cf5825f9472c4fc355cdadba5d992c70f.png)

Figure 12: scatter plot of hourly heating rate in watts (y-axis to about 450,000) against outdoor air temperature (-25 to 15C) for the single example model, with separate series for boiler and heat pump heating rate. The boiler carries the load below roughly -5C, reaching 300,000 to 400,000 W, while the heat pump runs above that near 200,000 W. Section 6.1 discusses the sequencing.

