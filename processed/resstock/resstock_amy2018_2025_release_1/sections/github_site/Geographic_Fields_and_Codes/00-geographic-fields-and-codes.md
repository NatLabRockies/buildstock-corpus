<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/explanations/Geographic_Fields_and_Codes.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/explanations/Geographic_Fields_and_Codes.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/explanations/Geographic_Fields_and_Codes.html | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: github_site/docs/resources/explanations/Geographic_Fields_and_Codes.md | section: Geographic Fields and Codes | lines: 2-11 -->
# Geographic Fields and Codes

ResStock provides many geographic fields to allow for a variety of analysis. Many of the geographic codes are self-explanatory, such as the name of the county, but there are some codes that are not as user friendly. Sometimes these codes can represent counties, census tracts, and PUMAs. **ResStock uses the National Historical GIS (NHGIS) GISJOIN standard codes for 2010 counties, 2010 PUMAs, and 2010 Census Tracts. 2020 geographic codes are not available at this time.** That means that all 2020 geographic codes must be converted to 2010 codes before using ResStock.

These are based on Federal Information Processing Standard (FIPS) codes. Example names of columns that include these geographic codes include **in.county** or **in.county_and_puma**. They can even be seen in the [Data Viewer](https://resstock.nlr.gov) when trying to filter by PUMA. It starts with a G followed by several numbers. Below is an example.

![](../../../assets/images/gis-join.png)

Want to learn how to convert your geography into the right ResStock format? Examples are provided below on how to find the 2010 PUMA. After converting your geography into the right format, use the [Check That You Have Enough Samples or Dwelling Units with the Data Viewer](docs/resources/tutorials/Enough_Samples_Data_Viewer.md) tutorial with the Data Viewer example to make sure your region is broad enough to draw conclusions from; otherwise your sample size is too low and you could have a large margin of error in your results.

