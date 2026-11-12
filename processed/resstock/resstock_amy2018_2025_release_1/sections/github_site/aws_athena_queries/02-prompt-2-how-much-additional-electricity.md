<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/how-to-guides/aws_athena_queries.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/how-to-guides/aws_athena_queries.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/how-to-guides/aws_athena_queries.html | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: github_site/docs/resources/how-to-guides/aws_athena_queries.md | section: Prompt 2: How much additional electricity would be consumed by electric vehicles charging if each applicable dwelling unit in Alaska got one electric vehicle and one Level 1 charger? | lines: 27-37 -->
## Prompt 2: How much additional electricity would be consumed by electric vehicles charging if each applicable dwelling unit in Alaska got one electric vehicle and one Level 1 charger?
<b>Query<b>
```
SELECT SUM("calc.weighted.electricity.ev_charging.energy_consumption..tbtu") AS total_electricity_consumption
FROM "resstock_amy2018_r1_2025_md_by_state_parquet"
WHERE
"in.state" = 'AK' AND "upgrade" = 19 AND "applicability" = true;
```
<b>Results<b>
![](../../../assets/images/Alaska_ev_charging_consumption.png)

