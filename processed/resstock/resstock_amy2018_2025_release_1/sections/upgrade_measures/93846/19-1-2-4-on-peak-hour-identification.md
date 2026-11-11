<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/93846.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/93846.md | section: 1.2.4 On-Peak Hour Identification | lines: 286-359 -->
## 1.2.4 On-Peak Hour Identification

When analyzing the impact of load flexibility, it is necessary to define the target time periods when demand flexibility will be dispatched to reduce load. These time periods are commonly referred to as on-peak hours. On-peak hours can be identified in different ways, depending on the goal. For instance:

- Reducing system net load: Grid-wide net load data can be analyzed to identify hours with the highest demand, and demand flexibility can be dispatched to help lower overall system peak power generation requirements.
- Responding to time-of-use pricing: Utility rates for individual customers can be analyzed to identify times with the highest electricity prices. This is only applicable for customers with time-of-use rates. Demand flexibility can be dispatched to reduce individual customer utility bills.
- Minimizing grid operation costs: Grid-wide operational cost data can be analyzed to identify hours with the highest operational costs, which could be dependent on system

peak demand, renewable generation, and local or distribution-level peak power. Demand flexibility can be dispatched to help reduce overall system operation costs.

The primary use for the results from this analysis is to feed into a national-scale energy system analysis that extends to 2050. The hypothesis is that demand flexibility will play a more important role further in the future; therefore, for this measure, the goal is to quantify load flexibility's technical potential to reduce net system load in 2050. Cambium is a dataset of load profiles based on assumed changes to the power sector over time (Gagnon, et al., 2024). It provides future load projections and related metrics. The MidCase scenario within Cambium adopts central estimates for key inputs, including technology costs, fuel prices, and demand growth. One important note is that the Cambium data do not consider future changes in load profiles due to wide-scale electrification, such as the addition of electric vehicles or heat pumps. Future work intends to update these load profiles and reassess the peak period definitions.

This project uses 2050 net load data from Cambium's MidCase scenario (Gagnon, et al., 2024) to identify the peak hours for each state, categorized by summer months (June to September), winter months (January to March and December) and intermediate months (April to May and October to November). The definition of seasons as a uniform set of months across all states is imprecise, but given that the modeling is also based on forecasts of the power system in 2050, it was judged to be an acceptable simplification. The identified peak hour is applied consistently as the dispatch time for each day within the corresponding months for each state. On-peak period timing by state is shown in Table 3. The on-peak period is defined as the 4-hour window containing the peak load, not the exact hour of the peak load.

Table 3.On-Peak Timing by State and Season

| State   | Summer Peak Start   |          | Winter Peak Start   |          | Intermediate   | Intermediate   |
|---------|---------------------|----------|---------------------|----------|----------------|----------------|
| State   | Summer Peak Start   | Peak End | Winter Peak Start   | Peak End | Peak Start     | Peak End       |
| AK      | 17:00               | 21:00    | 17:00               | 21:00    | 16:00          | 20:00          |
| AL      | 18:00               | 22:00    | 18:00               | 22:00    | 18:00          | 22:00          |
| AR      | 17:00               | 21:00    | 17:00               | 21:00    | 18:00          | 22:00          |
| AZ      | 18:00               | 22:00    | 18:00               | 22:00    | 17:00          | 21:00          |
| CA      | 18:00               | 22:00    | 17:00               | 21:00    | 17:00          | 21:00          |
| CO      | 18:00               | 22:00    | 18:00               | 22:00    | 16:00          | 20:00          |
| CT      | 17:00               | 21:00    | 17:00               | 21:00    | 17:00          | 21:00          |
| DE      | 17:00               | 21:00    | 17:00               | 21:00    | 17:00          | 21:00          |
| FL      | 18:00               | 22:00    | 18:00               | 22:00    | 18:00          | 22:00          |
| GA      | 18:00               | 22:00    | 18:00               | 22:00    | 18:00          | 22:00          |
| HI      | 18:00               | 22:00    | 18:00               | 22:00    | 18:00          | 22:00          |
| IA      | 17:00               | 21:00    | 17:00               | 21:00    | 17:00          | 21:00          |
| ID      | 19:00               | 23:00    | 17:00               | 21:00    | 18:00          | 22:00          |
| IL      | 18:00               | 22:00    | 16:00               | 20:00    | 16:00          | 20:00          |
| IN      | 18:00               | 22:00    | 17:00               | 21:00    | 17:00          | 21:00          |
| KS      | 18:00               | 22:00    | 17:00               | 21:00    | 17:00          | 21:00          |
| KY      | 19:00               | 23:00    | 17:00               | 21:00    | 17:00          | 21:00          |
| LA      | 18:00               | 22:00    | 17:00               | 21:00    | 18:00          | 22:00          |
| MA      | 17:00               | 21:00    | 17:00               | 21:00    | 17:00          | 21:00          |
| MD      | 17:00               | 21:00    | 16:00               | 20:00    | 17:00          | 21:00          |
| ME      | 17:00               | 21:00    | 17:00               | 21:00    | 16:00          | 20:00          |
| MI      | 17:00               | 21:00    | 18:00               | 22:00    | 17:00          | 21:00          |
| MN      | 17:00               | 21:00    | 17:00               | 21:00    | 16:00          | 20:00          |
| MO      | 18:00               | 22:00    | 8:00                | 12:00    | 16:00          | 20:00          |
| MS      | 18:00               | 22:00    | 17:00               | 21:00    | 18:00          | 22:00          |
| MT      | 17:00               | 21:00    | 18:00               | 22:00    | 19:00          | 23:00          |
| NC      | 18:00               | 22:00    | 17:00               | 21:00    | 17:00          | 21:00          |
| ND      | 19:00               | 23:00    | 19:00               | 23:00    | 18:00          | 22:00          |
| NE      | 15:00               | 19:00    | 17:00               | 21:00    | 16:00          | 20:00          |
| NH      | 17:00               | 21:00    | 17:00               | 21:00    | 17:00          | 21:00          |
| NJ      | 17:00               | 21:00    | 17:00               | 21:00    | 17:00          | 21:00          |
| NM      | 18:00               | 22:00    | 17:00               | 21:00    | 17:00          | 21:00          |
| NV      | 18:00               | 22:00    | 17:00               | 21:00    | 18:00          | 22:00          |

| State   | Summer     | Summer   | Winter     | Winter   | Intermediate   | Intermediate   |
|---------|------------|----------|------------|----------|----------------|----------------|
| State   | Peak Start | Peak End | Peak Start | Peak End | Peak Start     | Peak End       |
| NY      | 18:00      | 22:00    | 17:00      | 21:00    | 17:00          | 21:00          |
| OH      | 17:00      | 21:00    | 17:00      | 21:00    | 17:00          | 21:00          |
| OK      | 15:00      | 19:00    | 4:00       | 8:00     | 3:00           | 7:00           |
| OR      | 17:00      | 21:00    | 17:00      | 21:00    | 16:00          | 20:00          |
| PA      | 17:00      | 21:00    | 17:00      | 21:00    | 17:00          | 21:00          |
| RI      | 18:00      | 22:00    | 17:00      | 21:00    | 18:00          | 22:00          |
| SC      | 19:00      | 23:00    | 18:00      | 22:00    | 17:00          | 21:00          |
| SD      | 15:00      | 19:00    | 16:00      | 20:00    | 18:00          | 22:00          |
| TN      | 17:00      | 21:00    | 17:00      | 21:00    | 17:00          | 21:00          |
| TX      | 18:00      | 22:00    | 17:00      | 21:00    | 17:00          | 21:00          |
| UT      | 18:00      | 22:00    | 17:00      | 21:00    | 17:00          | 21:00          |
| VA      | 18:00      | 22:00    | 16:00      | 20:00    | 16:00          | 20:00          |
| VT      | 18:00      | 22:00    | 18:00      | 22:00    | 17:00          | 21:00          |
| WA      | 17:00      | 21:00    | 17:00      | 21:00    | 17:00          | 21:00          |
| WI      | 18:00      | 22:00    | 17:00      | 21:00    | 17:00          | 21:00          |
| WV      | 16:00      | 20:00    | 17:00      | 21:00    | 16:00          | 20:00          |
| WY      | 18:00      | 22:00    | 8:00       | 12:00    | 8:00           | 12:00          |

