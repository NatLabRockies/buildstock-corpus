<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/how-to-guides/aws_athena_queries.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/how-to-guides/aws_athena_queries.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/how-to-guides/aws_athena_queries.html | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: github_site/docs/resources/how-to-guides/aws_athena_queries.md | section: Prompt 3: What is the average headroom on an electric panel per area median income after a cold climate heat pump installation in New York? | lines: 38-59 -->
## Prompt 3: What is the average headroom on an electric panel per area median income after a cold climate heat pump installation in New York?
<b>Query<b>
```
SELECT
  "in.area_median_income" AS income_level,
  AVG(
    CASE
      WHEN "applicability" = true THEN "out.params.panel_breaker_space_headroom_count"
      ELSE NULL
    END
  ) AS headroom_count,
FROM
  "resstock_amy2018_r1_2025_md_by_state_parquet"
WHERE
  "in.state" = 'NY'AND "upgrade" = 04
GROUP BY
  "in.area_median_income"
ORDER BY
  "in.area_median_income";
```
<b>Results<b>
![](../../../assets/images/headroom_count_average.png)
