<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/94463.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/94463.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/94463.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: upgrade_measures/measure_pdfs/94463.md | section: Peak Period Definition | lines: 388-470 -->
## Peak Period Definition

When analyzing the impact of load flexibility, it is necessary to define the target time periods when DF will be dispatched to reduce the load. These time periods are commonly referred to as on-peak hours. On-peak hours can be identified in different ways depending on the goal, for example:

- Reducing System Peak Power: Grid-wide net load data can be analyzed to identify hours with the highest demand, and DF can be dispatched to help lower the overall system peak power requirements.
- Responding to time-of-use (TOU) Pricing: Utility rates for individual customers can be analyzed to identify times with the highest electricity prices. This approach is applicable only for customers with TOU rates. DF can be dispatched to reduce individual customer utility bills.
- Minimizing Grid Operation Costs: Grid-wide operational cost data can be analyzed to identify hours with the highest operational costs, and DF can be dispatched to help lower the overall system operation costs.

For this measure, the goal is to quantify the load flexibility's technical potential to reduce system peak power in 2050. This project uses 2050 net load data from Cambium 2024's Mid-case scenario (Gagnon et al. 2025) to identify the peak hours for each state, categorized by summer months (June to September), winter months (December to March), and shoulder seasons (April to May and October to November). The Cambium data are taken from a publicly available dataset that provides future load predictions and other related metrics. The mid-case scenario within Cambium 2024 adopts moderate estimates for key inputs, including technology costs, fuel prices, and demand growth. The identified peak hours are then applied consistently as the dispatch time for each day within the corresponding months for each state. The on-peak period timing by state is shown in Table 4.

Table 4. On-Peak Timing by State and Season

<!-- table recovered from measure_pdfs/94463.pdf p.24
     overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/94463.yaml
     method: extracted grids joined under one header (compared with the page text layer)
     supersedes the extractor's own table here (values 4ddcb227089d…):
     and its continuation grid(s) (values e44030df6e20…):
       The table runs over two pages and was extracted as two grids, each opening with the two header rows (season over Peak Start and Peak End), the second of them as a data row. Every value in both grids matches the pages. The 49 state rows are the extractor's own, joined under one header whose two rows are written together ('Summer: Peak Start'). -->

**Table 4, part 1 of 3**

| State | Summer: Peak Start | Summer: Peak End | Winter: Peak Start | Winter: Peak End | Intermediate: Peak Start | Intermediate: Peak End |
|---|---|---|---|---|---|---|
| AK | 17:00 | 21:00 | 17:00 | 21:00 | 16:00 | 20:00 |
| AL | 18:00 | 22:00 | 18:00 | 22:00 | 18:00 | 22:00 |
| AR | 17:00 | 21:00 | 17:00 | 21:00 | 18:00 | 22:00 |
| AZ | 18:00 | 22:00 | 18:00 | 22:00 | 17:00 | 21:00 |
| CA | 18:00 | 22:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| CO | 18:00 | 22:00 | 18:00 | 22:00 | 16:00 | 20:00 |
| CT | 17:00 | 21:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| DE | 17:00 | 21:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| FL | 18:00 | 22:00 | 18:00 | 22:00 | 18:00 | 22:00 |
| GA | 18:00 | 22:00 | 18:00 | 22:00 | 18:00 | 22:00 |
| IA | 17:00 | 21:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| ID | 19:00 | 23:00 | 17:00 | 21:00 | 18:00 | 22:00 |
| IL | 18:00 | 22:00 | 16:00 | 20:00 | 16:00 | 20:00 |
| IN | 18:00 | 22:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| KS | 18:00 | 22:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| KY | 19:00 | 23:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| LA | 18:00 | 22:00 | 17:00 | 21:00 | 18:00 | 22:00 |
| MA | 17:00 | 21:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| MD | 17:00 | 21:00 | 16:00 | 20:00 | 17:00 | 21:00 |
| ME | 17:00 | 21:00 | 17:00 | 21:00 | 16:00 | 20:00 |
| MI | 17:00 | 21:00 | 18:00 | 22:00 | 17:00 | 21:00 |

**Table 4, part 2 of 3**

| State | Summer: Peak Start | Summer: Peak End | Winter: Peak Start | Winter: Peak End | Intermediate: Peak Start | Intermediate: Peak End |
|---|---|---|---|---|---|---|
| MN | 17:00 | 21:00 | 17:00 | 21:00 | 16:00 | 20:00 |
| MO | 18:00 | 22:00 | 8:00 | 12:00 | 16:00 | 20:00 |
| MS | 18:00 | 22:00 | 17:00 | 21:00 | 18:00 | 22:00 |
| MT | 17:00 | 21:00 | 18:00 | 22:00 | 19:00 | 23:00 |
| NC | 18:00 | 22:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| ND | 19:00 | 23:00 | 19:00 | 23:00 | 18:00 | 22:00 |
| NE | 15:00 | 19:00 | 17:00 | 21:00 | 16:00 | 20:00 |
| NH | 17:00 | 21:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| NJ | 17:00 | 21:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| NM | 18:00 | 22:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| NV | 18:00 | 22:00 | 17:00 | 21:00 | 18:00 | 22:00 |
| NY | 18:00 | 22:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| OH | 17:00 | 21:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| OK | 15:00 | 19:00 | 4:00 | 8:00 | 3:00 | 7:00 |
| OR | 17:00 | 21:00 | 17:00 | 21:00 | 16:00 | 20:00 |
| PA | 17:00 | 21:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| RI | 18:00 | 22:00 | 17:00 | 21:00 | 18:00 | 22:00 |
| SC | 19:00 | 23:00 | 18:00 | 22:00 | 17:00 | 21:00 |
| SD | 15:00 | 19:00 | 16:00 | 20:00 | 18:00 | 22:00 |
| TN | 17:00 | 21:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| TX | 18:00 | 22:00 | 17:00 | 21:00 | 17:00 | 21:00 |

**Table 4, part 3 of 3**

| State | Summer: Peak Start | Summer: Peak End | Winter: Peak Start | Winter: Peak End | Intermediate: Peak Start | Intermediate: Peak End |
|---|---|---|---|---|---|---|
| UT | 18:00 | 22:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| VA | 18:00 | 22:00 | 16:00 | 20:00 | 16:00 | 20:00 |
| VT | 18:00 | 22:00 | 18:00 | 22:00 | 17:00 | 21:00 |
| WA | 17:00 | 21:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| WI | 18:00 | 22:00 | 17:00 | 21:00 | 17:00 | 21:00 |
| WV | 16:00 | 20:00 | 17:00 | 21:00 | 16:00 | 20:00 |
| WY | 18:00 | 22:00 | 8:00 | 12:00 | 8:00 | 12:00 |

