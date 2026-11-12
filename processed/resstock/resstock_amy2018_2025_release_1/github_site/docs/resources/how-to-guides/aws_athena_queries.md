<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/how-to-guides/aws_athena_queries.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/how-to-guides/aws_athena_queries.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/how-to-guides/aws_athena_queries.html | corpus_version: resstock_amy2018_2025_release_1-v1 -->
# AWS Athena Queries

# Amazon Web Services (AWS) Athena Queries

The following queries were run on a table created from this Amazon S3 bucket: [https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2025%2Fresstock_amy2018_release_1%2Fmetadata_and_annual_results%2F&limit=50](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2025%2Fresstock_amy2018_release_1%2Fmetadata_and_annual_results%2F&limit=50).

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
