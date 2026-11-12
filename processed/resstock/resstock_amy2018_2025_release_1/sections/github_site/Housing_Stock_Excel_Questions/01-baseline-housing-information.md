<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/how-to-guides/Housing_Stock_Excel_Questions.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/how-to-guides/Housing_Stock_Excel_Questions.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/how-to-guides/Housing_Stock_Excel_Questions.html | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: github_site/docs/resources/how-to-guides/Housing_Stock_Excel_Questions.md | section: Baseline Housing Information | lines: 89-128 -->
## Baseline Housing Information

The first two questions deal with the baseline housing, or the housing information without the upgrade applied. For the first question, home size, start by reviewing all of the column names in Column B and their description in Column E. After reading through the list, there are a few options that describe the home size. Lines 64, 65, and 156 all look like they could meet our needs. Let’s work with line 156, **in.sqft**, to look at floor area. Then, let’s determine which value we can use to evaluate energy consumption. Energy consumption for this ResStock dataset is measured in site energy usage. Energy consumption is actually an output on line 292 of the data_dictionary.tsv file, and the field is called **out.site_energy.total.energy_consumption.kwh**.

Heading back to the CO_baseline_metadata_and_annual_results.csv file, we can start the analysis.

To easily answer these questions, we can use Excel’s built-in <ins>PivotTable</ins>. You can also do this with coding or other means, but for this example we will use Excel. First, go to the <ins>Insert</ins> tab of Excel, and then choose the down arrow under PivotTable and choose From <ins>Table/Range</ins>. When a pop-up appears, choose <ins>New Worksheet</ins>, and then click OK.

![](../../../assets/images/pivottablesetup.png)

The blank <ins>PivotTable</ins> will look like this.

![](../../../assets/images/blankpivot.png)

The ResStock columns are on the right, and we will start to pull the fields into the four boxes on the bottom to begin the analysis.

We want to look at the questions by Single-Family Detached homes only, so let’s start with that first filter. In the fields table, click and drag **in.geometry_building_type_recs** into the Filters box. Then, where it says (All), we need to only select Single-Family Detached.

![](../../../assets/images/onlysfd.png)

Within Single-Family Detached, we want to look at the analysis by vintage so we will apply that to Rows. Drag in.vintage to the Rows box.

To answer our first question, the column or the field we need to add to the PivotTable is **in.sqft** . In the list of fields, choose **in.sqft** and drag it to the <ins>Values</ins> box. Choose the down arrow next to the box, and choose <ins>Value Field Settings</ins>. When the pop-up window appears, choose <ins>Average</ins> instead of Sum so we can understand the average size of home per vintage.

![](../../../assets/images/average.png)

The resulting table looks like the following.

![](../../../assets/images/vintagesize.png)

Over time, the average home size has grown over 1,000 sqft.

The next task is to determine the average energy consumption of homes through different vintages. In the fields list, choose **out.site_energy.total.energy_consumption.kwh** and drag it to the <ins>Values</ins>. Click the down arrow and choose <ins>Value Field Settings</ins> like we did in the previous step. Choose <ins>Average</ins> instead of Count and click OK. The table now shows the average size and energy consumption of the homes over time.

![](../../../assets/images/averageenergy.png)

In general, average energy consumption is lowest for homes built in the 1990s and 2000s, and highest for homes built before 1940 and in the 1940s.

These are just two examples of questions about housing that can be answered using the baseline housing information. Before performing a full residential building analysis, identifying questions like the two we just analyzed is a good idea. Now, let’s look at a few examples of using the upgrade information.

