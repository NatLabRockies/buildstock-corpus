<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/how-to-guides/aws_athena_queries.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/how-to-guides/aws_athena_queries.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/how-to-guides/aws_athena_queries.html | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: github_site/docs/resources/how-to-guides/aws_athena_queries.md | section: Prompt 1: How many dwelling units exist in Colorado, by type and floor area? | lines: 8-26 -->
## Prompt 1: How many dwelling units exist in Colorado, by type and floor area?
<b>Query<b>
```
SELECT
  "in.geometry_building_type_recs" AS building_type,
  SUM("in.sqft..ft2") AS total_size_sqft,
  SUM("weight") AS total_building_count
FROM
  "resstock_amy2018_r1_2025_md_by_state_parquet"
WHERE
  "in.state" = 'CO' AND "upgrade" = 0
GROUP BY
  "in.geometry_building_type_recs"
ORDER BY
  "in.geometry_building_type_recs";
```
<b>Results<b>
![](../../../assets/images/Colorado_building_type_size.png)

