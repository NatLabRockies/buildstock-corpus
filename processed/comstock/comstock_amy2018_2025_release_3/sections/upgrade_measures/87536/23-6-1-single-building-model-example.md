<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/87536.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/87536.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/87536.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/87536.md | section: 6.1  Single Building Model Example | lines: 537-574 -->
## 6.1  Single Building Model Example

Table 6 shows a comparison of an end-use energy consumption for a 37,491 square-foot large office building model in Denver, CO, before and after application of the default measure inputs. The two energy end-use categories that are significantly affected by this measure are heating and cooling energy. For the same heating load, the total heating energy consumption drops by ~24% from 532 GJ to 403 GJ. Note that the natural gas consumption for the updated case is the one used by the backup natural gas boiler. Overall, the electric consumption increases by ~5% while natural gas consumption drops by ~48%.

Table 6. End-Use Energy Consumption Comparison

|                    | Baseline         | Baseline         | Updated          | Updated          |
|--------------------|------------------|------------------|------------------|------------------|
| End Use            | Electricity [GJ] | Natural Gas [GJ] | Electricity [GJ] | Natural Gas [GJ] |
| Heating            | 99               | 433              | 176              | 227              |
| Cooling            | 291              | 0                | 296              | 0                |
| Interior Lighting  | 551              | 0                | 551              | 0                |
| Exterior Lighting  | 75               | 0                | 75               | 0                |
| Interior Equipment | 380              | 0                | 380              | 0                |
| Exterior Equipment | 0                | 0                | 0                | 0                |
| Fans               | 204              | 0                | 204              | 0                |
| Pumps              | 59               | 0                | 59               | 0                |
| Heat Rejection     | 15               | 0                | 15               | 0                |
| Humidification     | 0                | 0                | 0                | 0                |
| Heat Recovery      | 0                | 0                | 0                | 0                |
| Water Systems      | 15               | 0                | 15               | 0                |
| Refrigeration      | 0                | 0                | 0                | 0                |
| Generators         | 0                | 0                | 0                | 0                |
| Total End Uses     | 1689.09          | 433.03           | 1770.93          | 226.92           |

Figure 8. Sequencing between ASHP and boiler

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/87536.yaml
     source: 87536_images/image_000013_01d1e052ed4f877b886e59640fb35c5cf5825f9472c4fc355cdadba5d992c70f.png
     method: vision-description
     described: 2026-08-21 -->

![Scatter plot of boiler and heat pump heating rate against outdoor air temperature](87536_images/image_000013_01d1e052ed4f877b886e59640fb35c5cf5825f9472c4fc355cdadba5d992c70f.png)

Figure 8: scatter plot of sequencing between the ASHP and the boiler, with outdoor air temperature from about -25 to 15 degrees C on the x-axis and heating rate up to roughly 450,000 W on the y-axis, one series per device. The heat pump carries the load at milder temperatures and the gas boiler takes over below the cutoff. Section 6.1 walks through the changeover logic.

We checked the sequencing between the heat pump and the boiler during low-temperature operation using an example cutoff temperature of 25°F (-4°C). Figure 8 shows the operation pattern. As expected, the heat pump handled most of the load at a higher temperature. The boiler starts supplementing the ASHP as the temperatures drops and takes over all heating when the temperature is below the cutoff temperature.

