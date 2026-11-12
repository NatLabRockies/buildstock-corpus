<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/how-to-guides/Housing_Stock_Excel_Questions.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/how-to-guides/Housing_Stock_Excel_Questions.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/how-to-guides/Housing_Stock_Excel_Questions.html | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: github_site/docs/resources/how-to-guides/Housing_Stock_Excel_Questions.md | section: Analyze Your Housing Stock and Different What if Scenarios Using Excel | lines: 2-88 -->
# Analyze Your Housing Stock and Different What if Scenarios Using Excel

# Analyze Your Housing Stock and Different "What-If" Scenarios Using Excel

Building stock analysis involves collecting and assessing the characteristics of a set of buildings within a defined area. It includes analyzing data about the buildings, such as their physical attributes, energy performance, and occupancy patterns. Analyzing these things can help support policy planning and decision-making related to energy efficiency, energy affordability, and grid impacts.

A typical analysis starts with defining the goal and scope (e.g., retrofits to cut building consumption by X%) and a geographic boundary (e.g., a state, city, or low-income housing only within a county). Then data is collected/generated and amalgamated, often from multiple sources such as tax assessor records, surveys, and energy audits. ResStock can support or even sidestep this typically time- and labor-intensive data collection step by providing housing data aggregated from multiple national datasets. Additionally, ResStock data offers simulated data for estimating the energy performance baseline and energy savings from a broad range of energy efficiency retrofit measures.

The following steps are a starting point for using ResStock data in a residential building stock analysis. If you use ResStock for your residential building stock analysis, spend more time planning out specific questions and goals that you have for your analysis.

We will do a simple analysis to understand some of the characteristics of single-family detached homes in Colorado and identify the energy and utility bill impacts of deploying high-efficiency cold-climate heat pumps with electric back up to all eligible single-family detached homes in the state.

ResStock publishes national level datasets containing the energy baseline and a set of energy efficiency measures on the [Open Energy Data Initiative (OEDI) website](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock). The documentation for each release is on our website, and near each release you will see a Technical Documentation button. We recommend browsing the documentations so that you can choose the dataset that can best answer your questions. The datasets can vary in the type of housing upgrades, weather years, model assumptions, reporting metrics, and more. Below is a screenshot showing an example of where our documentation is located for our 2024.2 dataset.

![](../../../assets/images/documentation.png)

For this example, we will look at the single-family detached homes in Colorado and try to answer the following questions:
1.	What is the median home size by vintage?
2.	How does the average energy consumption differ by vintage?
3.	How does site energy consumption before and after the upgrade has been applied vary by housing vintage?
4.	Do natural gas energy bills change before and after the upgrade has been applied by housing vintage?

We will use the AMY2018 dataset from the [2024.2 data release](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2024/resstock_amy2018_release_2/resstock_documentation_2024_release_2.pdf), which contains 16 upgrade packages. According to the [dataset documentation](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2024/resstock_amy2018_release_2/resstock_documentation_2024_release_2.pdf), Measure Package 2 is a high-efficiency cold-climate air-to-air heat pump paired with electric backup, which we wll examine in the analysis.

This ResStock 2024.2 dataset contains roughly 550,000 dwelling samples that cover the contiguous United States, including Washington D.C., with the lowest geographic resolution available at the intersection of 2010 county and 2010 PUMA regions. In this 2024.2 dataset, each model sample represents about ~252 dwelling units. Refer to Section [Quota-Based Sampling and the Implications](docs/resources/explanations/Quota_Based_Sampling.md) for more details on sampling methods.

![](../../../assets/images/datadictionary.png)

To get to the 2024.2 dataset, visit the ResStock website, and go to the Datasets tab. Under the name of each release is a table of information about the release. In the Supplemental Data and Dictionaries column, there is a link for the Data Repository of each dataset. This is how to reach the data on OEDI. Clicking on the Data Repository link for this dataset shows the following:

![](../../../assets/images/oedihomepage.png)

If you go into the metadata_and_annual_results folder, the data is available at two scales and in two file formats. Metadata refers to the housing characteristics of the dwelling samples, while annual results are annually aggregated metrics from the simulations. The baseline file contains housing metadata as well as the energy baseline, while the upgrade files contain the energy consumption and resulting metrics post-upgrade, upgrade savings, and housing metadata from the baseline.  Below is a screenshot of the file structure showing an example of this for Colorado.

![](../../../assets/images/coloradofilestructure.png)

Both the baseline and upgrade files have all data organized by bldg_id or the number of the dwelling unit that was modeled. To compare the baseline and the upgrade file, you can join the two files together by the building_id column, but we will not be demonstrating this in the example today.

The first step of the analysis is to down select to the geography and/or housing segment of interest and examine how many samples are available. This can be done by downloading the appropriate state sample file and further filtering to the geography and/or housing segment of choice. We are focusing on Colorado, single-family detached homes, and Package 2: High efficiency cold-climate air-to-air heat pump with electric backup, so we will download the relevant files. We will need the baseline file too. The files are highlighted below. Click on the file title for it to download.

![](../../../assets/images/coloradofiles.png)

Open the downloaded CO_baseline_metadata_and_annual_results.csv file, and the first 10 lines look like this.

![](../../../assets/images/firstten.png)

We are only interested in single-family detached homes, so we have to find a way to filter based on building type. The question is, what column should we use? Let’s review the data_dictionary.tsv, or the file that gives a summary of most of the column titles and what they mean. The data_dictionary.tsv file is found a few folders back, right on the screen we started with.

![](../../../assets/images/oedihomepage2.png)

There are different ways to open a .tsv file, and for this example we will use Excel. Click on the data_dictionary.tsv file, and then open a new instance of Excel. Go to open a new file, and try to open the data_dictionary.tsv file. In your file explorer, make sure All Files is chosen, not All Excel Files: otherwise the data_dictionary.tsv file will not show up. Go through the steps to open up the file, and the first 10 rows will look like this when you are done.

![](../../../assets/images/firsttendatadictionary.png)

For more information on the data dictionary and how things are labeled in ResStock, see Data and the section Field Naming Convention to get a better idea.

Reading through the data_dictionary.tsv Column B, **field_name**, row 63 has in.geometry_building_type_recs with a field description of "PUMS 2019 building type", and allowable_baseline_enumerations of "Mobile Home", "Multi-Family with 2–4 Units"," Multifamily with 5+ Units", "Single-Family Attached", and "Single-Family Detached". This is the column we need to filter the baseline and upgrade files to only see results for Single-Family Detached homes.

Going back to the CO_baseline_metadata_and_annual_results.csv file, and click <ins>Format as Table</ins> so we can perform our filter.

![](../../../assets/images/formatastable.png)

Then, search for the column name we need to filter: **in.geometry_building_type_recs**. Turns out it is column BK. Click the down arrow in the column, and make sure Single-Family Detached is the only housing option selected. Click <ins>OK</ins> to apply the filter.

![](../../../assets/images/sfd.png)

Repeat this process to filter to Single-Family Detached homes in the CO_upgrade02_metadata_and_annual_results file too. With the CO_upgrade02_metadata_and_annual_results file, we need to filter to only the samples that have had this upgrade applied, because not every home has this upgrade applied. Some homes may not have the right home configuration or may have an out-of-scope heating fuel: therefore, only some of the homes are actually modeled with this upgrade. To determine the column that describes whether the home received the upgrade or not, go back to the data_dictionary_tsv.

The second row shows a field_name called applicability with a field_description of: The measure was or was not applied to bldg_id. This is what we are looking for. Going back to the CO_upgrade02_metadata_and_annual_results file, search for the **applicability** column, and make sure only TRUE is chosen as an option. That means only the samples that were actually upgraded with our package of interest, high-efficiency cold-climate air-to-air heat pump with electric backup, will be shown. If the value is FALSE, that means the building sample was not upgraded with this package.

Next, check to make sure there are the right number of samples or at least 1,000 samples. For more information on the number of samples that should be used in an analysis, see the *How Many Samples are Required for this Analysis* explanation on the Resources page.

To do this, highlight the first column of each of the two files, and look at the <ins>Count</ins> value at the bottom right of the screen. For the baseline file, it shows Count: "5901".

![](../../../assets/images/count.png)

Doing the same on the upgrade file, the <ins>Count</ins> value is showing Count: "5701". We expect the count of the upgrade file to be less because not all samples or bldg_id had the upgrade applied.

Luckily for us, each file has over 1,000 samples so we are good to begin the analysis. For more information on the number of samples that should be used in an analysis, see the *How Many Samples are Required for this Analysis* explanation on the Resources page.

We can analyze the data and extract key baseline and upgrade information now that we have confirmed we have enough samples. Let’s revisit the questions for our analysis:
1.	What is the median home size by vintage?
2.	How does the average energy consumption differ by vintage?
3.	How does site energy change before and after the upgrade has been applied by housing vintage?
4.	Do natural gas energy bills change before and after the upgrade has been applied by housing vintage?
To analyze this key information, we first need to know where to look. Back to the data_dictionary.tsv to find out which columns we should analyze!

