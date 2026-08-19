<!-- comstock comstock_amy2018_2025_release_3 | github_site | docs/resources/tutorials/local_segmentation_study.md -->
# Using Local Data in a ComStock Analysis

# Tutorial: Perform an analysis by blending ComStock and local data

**_This tutorial uses the ComStock 2023 Release 1 dataset. Some dataset attributes, like column names, may have changed in later releases._**

## Introduction

When performing a commercial stock energy analysis, the incorporation of the ComStock data sets and local data sources can greatly enhance the accuracy and relevance of results. However, despite its extensive coverage, ComStock's dataset operates at a statistical level that might not fully capture the fine-grained details that local data can offer. Energy use in commercial buildings is highly dependent on numerous factors that can significantly vary from one location to another. While ComStock accounts for many factors, such as building codes and regional variations in weather, the accuracy of building square footage estimates in ComStock decreases with geographic resolution. This has largely been addressed by the [new ComStock sampling method](docs/resources/explanations/new_sampling_method.md) implemented in 2024 Release 2.

Local data sources come into play here, bringing a higher level of resolution to our understanding of energy usage. They provide more detailed, location-specific information that can supplement and true-up ComStock's commercial building energy consumption at a more granular level. This depth of understanding can lead to the development of highly targeted, effective energy conservation measures and strategies, specifically tailored to local conditions and needs. This results in a more robust, precise, and locally attuned picture of commercial building energy usage.

In this tutorial we discuss how to take a local data source and blend it with ComStock. This integrated approach leverages the strengths of both types of data, providing a more comprehensive, detailed, and locally relevant understanding of commercial energy usage and the associated opportunity impact space.

## Instructions

There are three steps required to use a local dataset to perform a segmentation analysis. First we clean and categorize the local data source so it can be used with ComStock. Second, we identify which models from ComStock we want to include in the local analysis. Third, we calculate updated weights for the ComStock models selected in the second step based on the local data source data produced in the first step.

Note: Text in **bold** refers to a column in your excel sheet. In the case of the local data source the names of the individual columns will depend on the data source, and so we use descriptive column names. Text in *italics* describes a sheet in the excel workbook. Text in "quotes" specifies values expected in a cell or cells. <u>Underlined</u> text specifies an excel function.

### Step 1: Clean and normalize the local data source:

1.  Open the local data source.

2.  Identify the following columns, all of which are required for this process.

    a.  **Building Class**: A column that categorizes buildings / parcels as residential, commercial, etc. This may have to be accomplished through use of the zoning column.

    b.  **Building Type**: A column that categorizes buildings with moderate specificity e.g. "Warehouse", "Bank", "Strip Mall", "Medical Office", etc.

    c.  **Building Square Footage**: A column the defines the total square footage of the building.

3.  Filter the data to only reflect commercial using the **Building Class** column. If an "exempt" (often denoted as "EX") category is listed it should likely be included. Assessor data often uses this label for denoting the property is exempt from taxes, e.g. buildings like schools are often exempt from taxes but are still commercial buildings.

4.  Create a new sheet named *building type mapping* and use the excel function <u>UNIQUE</u> on your data's **Building Class** column to determine the list of all unique **Building Type** values in the dataset.

5.  For each building type determine the associated ComStock building type categories.

    a.  For initial analyses use the categories of "Education", "Food Service", "Healthcare", "Mercantile", Office", and "Warehouse and Storage". These categories are the allowed values for ComStock Building Type Groups.

    b.  In many cases there will not be a mapping between a building type in the local data source and ComStock. Common examples include manufacturing, dormitories, religious institutions, agricultural buildings, and buildings providing public utilities. Note these building types as they will be removed from the local data source in the next step.

    c.  In the case of building types which are not clearly labeled (e.g. "General" or "Hist" or "C&D") review some of the buildings on google maps using the building address and the "Street View" mode in google. If there are a significant number of addresses to review filter to the addresses that need review, copy them into a new excel file, and use the process described in Steps 1 and 2 [here](https://support.google.com/mymaps/answer/3024836) to create a custom google map. This significantly speeds up the process for checking over 15 addresses.

    d.  This analysis can also be performed with a mapping to all 16 ComStock building types, however they are more difficult to use as it can be difficult to differentiate primary and secondary schools, types of retail stores and offices, etc.

    e.  Example mappings between two different data sources and ComStock's building types can be found in Table 1 on page 16 of the [ComStock documentation](docs/resources/resources.md#references).

6.  Filter the data to remove all building types from the local data source that do not have a match in ComStock.

7.  Review the remaining data to identify and remove any duplicates. This step will typically result in removing up to 50% of the **Building Square Footage** from the analysis. Not performing it may lead to significant errors.

    a.  Typically duplicate entries in local data sources have the same square footage and are at the same location.

    b.  While this can be programmatically determined to a fairly high degree of accuracy using geospatial data processing tools, for local data sources a manual review will typically be sufficient and significantly quicker.

8.  Create a second sheet named *cleaned data* and copy the down selected data to it.

9.  Update the <u>UNIQUE</u> statement in the *building type mapping* sheet to use the **Building Type** column in the *cleaned data* sheet and update the mapping between the remaining **Building Type** values and the ComStock Building Type Group values if necessary. At this point every **Building Type** value in the *cleaned data* sheet should have a ComStock Building Type Group value associated with it in the *building type mapping* sheet.

10. Create a new column in the *cleaned data* sheet named **ComStock Building Type Group** and use the <u>VLOOKUP</u> excel operator to insert the ComStock building type category for each row based on the **Building Type** column and the mapping in the *building type mapping* sheet.

11. Create a new column in the *cleaned data* sheet named **ComStock Floor Area Bin** and use nested <u>IF</u> excel operators to have each row take on a value of "under 25k", "25k-50k", "50k-200k", or "over 200k" based on the of the **Building Square Footage** column. A custom floor area bin column is available in the file: Template Building Stock Characteristic Analysis.xlsx in column 605.

12. Create a pivot table of the down-selected data in *cleaned data*.

    a.  Drag the field **ComStock Building Type Group** and the field **ComStock Floor Area Bin** into the 'Rows' and **Building Square Footage** into 'Values' sections in the PivotTable Fields sidebar on the right. Change the aggregation from 'Count' to 'Sum'. This will show how square footage of each building type / size bin combination exists in your local data source.

    b.  Review the aggregated data and check it against your knowledge of the local area covered by the data sources? Are the raw values or relative amount of any combinations surprising to you? Consider both if there is too much or too little of something. This can be an important opportunity to identify issues in the filtering steps, the building type mapping, or the duplicate removal.

    c.  Note which combinations exist in the pivot table, i.e. "Education, 50k-200k". This information will be needed in the second step of this process.

### Step 2: Identify ComStock models to include in the local segmentation analysis.

Note that the process described here uses counties as the base geographic unit. If this work is being performed in a highly dense region (for example Los Angeles county has a population of 10 million) then counties are likely not appropriate for the analysis, and Public Use Microdata Areas (PUMAs) are recommended. To learn more about PUMAs please read [this page](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/pumas.html) from the US Census Bureau. ComStock uses PUMAs from the 2010 census. Maps from the census identifying PUMAs of the correct vintage on a state and county basis can be found [here](https://www.census.gov/geographies/reference-maps/2010/geo/2010-pumas.html). If using PUMAs all advice and instructions below hold, however instead of **in.nhgis_county_gisjoin** or **in.county_name** please use **in.nhgis_puma_gisjoin**.

For help regarding interpreting **in.nhgis_county_gisjoin** and **in.nhgis_puma_gisjoin** please refer to our guide on interpreting geographic extent specifications.

1.  Download the ComStock annual results file from OEDI S3 bucket-- the link for the Baseline End Use Savings Shape 2023 Release 1 is here. The national file is 1.5gb. It's recommend to use the state .csv files if your selected geography is only in one state. New datasets are released every 6 months. Please check for our latest datasets on the [ComStock Documentation Website](docs/data.md).

2.  Filter using the **in.nhgis_county_gisjoin** or **in.county_name** columns to the county (or counties) containing the region defined in the local data source.

3.  Create a new column named **ComStock Floor Area Bin** and use nested <u>IF</u> excel operators to have each row take on a value of "under 25k", "25k-50k", "50k-200k", or "over 200k" based on the of the **in.sqft** column.

4.  Create a second sheet named *included models* and copy the down-selected data to the new sheet.

5.  Create a pivot table of the data in *included models*.

    a.  Drag the field **in.comstock_building_type_group** and **ComStock Floor Area Bin** into the 'Rows' and **in.sqft** into the 'Values' sections in the PivotTable Fields sidebar on the right. Ensure the aggregation function is set to 'Count'. This will show how many samples for each building type group and floor area bin combination are in the ComStock sample for the selected geography.

    b.  First, note which combinations have fewer than 7 samples. These combinations will need to be supplemented with additional ComStock modeling results.

    c.  Second, note any combinations that existed in the local data source analysis which are not present in the pivot table. These combinations will need to be added through inclusion of additional ComStock modeling results.

6.  For each combination noted in steps 5b or 5c:

    a.  In the baseline sheet filter by the specific values of **in.comstock_building_type_group** and **ComStock Floor Area Bin** for the combination.

    b.  Next, attempt to filter by counties which are similar to region covered by the local data source. Familiarity with the region is a significant benefit for this process. There are several key factors to keep in mind when selecting additional counties to pull data from:<br>
        &emsp;*  Density: the supplemental counties should have similar building densities -- i.e. if modeling a suburban area a neighboring high density city is not a good candidate.<br>
        &emsp;* Climate similarity: the supplemental counties should have weather that is highly similar.<br>
        &emsp;* Historic development: ideally the supplemental counties should, to the extent possible, have a similar history of development to the region under consideration -- i.e. if modeling what was originally a colonial settlement a neighboring region built out in the last 20 years is not a good candidate.<br>
        &emsp;* Economic drivers: when possible the supplemental counties should have similar economic drivers -- i.e. if the local region's development has been driven by manufacturing jobs, a proposed complemental county that is a regional healthcare hub is not a good candidate.

    c.  If sufficient results are returned to satisfy the 7 buildings per combination of building type group and floor area bin then add these results to the *included model*s sheet. If the number of models is still insufficient then further expand the counties being considered.

    d.  If the above steps have not produced sufficient results consider including using previous ComStock county clustering work to identify counties in the same cluster. This methodology is significantly less preferable the local knowledge and consideration of the factors listed in 6b.

7.  Update the pivot table (be sure that any new rows of data added to *included models* are included in the pivot table) and confirm that each combination specified by the local data source has at least seven ComStock models associated with it.

8.  Alter the aggregation function of the pivot table to 'Sum' instead of 'Count'.

### Step 3: Calculate updated weights for the ComStock model results.

1.  Create a new sheet in the ComStock results workbook called *updated weights*. In this sheet copy the results of the local data source pivot table.

2.  Create a new column named **ComStock Floor Area Totals** in the *updated weights* sheet and for each combination of **ComStock Building Type Group** and **ComStock Floor Area Bin** enter the associated floor area total from the pivot table referencing *included models*.

3.  Create a new column named **Mapping Lookup** in the *updated weights* sheet and use the <u>CONCAT</u> function in excel to make each row the concatenation of the **ComStock Building Type Group** and **ComStock Floor Area Bin** columns.

4.  Create a new column named **Updated Weight** in the *updated weights* sheet and define each row value as the division of the **Sum of Building Square Footage** column by the **ComStock Floor Area Totals** column.

5.  In the *included models* sheet create a new column named **Mapping Lookup**. Use the <u>CONCAT</u> function in excel to make each row the concatenation of the **in.comstock_building_type_group** and **ComStock Floor Area Bin** columns.

6.  Create a new column in the *included models* sheet named **Updated Weight** and use the <u>VLOOKUP</u> excel function to insert the **Updated Weight** value for each row based on the **Mapping Lookup** column and the mapping in the *updated weights* sheet.

7.  For each of the columns listed below create a new column titled '**localized.weighted.**' followed by the column name below in the *included models* sheet. These columns contain an energy, emissions, or building square footage value multiplied by the weighting factor calculated using the localized data source. Make each row value the value from the column listed below multiplied by the **Updated Weight** value for that row:

    a.  **calc.emissions.total_with_egrid..metric_ton**

    b.  **in.sqft**

    c.  **calc.enduse_group.district_cooling.hvac.energy_consumption..kwh**

    d.  **calc.enduse_group.district_heating.hvac.energy_consumption..kwh**

    e.  **calc.enduse_group.district_heating.water_systems.energy_consumption..kwh**

    f.  **calc.enduse_group.electricity.hvac.energy_consumption..kwh**

    g.  **calc.enduse_group.electricity.interior_equipment.energy_consumption..kwh**

    h.  **calc.enduse_group.electricity.lighting.energy_consumption..kwh**

    i.  **calc.enduse_group.electricity.refrigeration.energy_consumption..kwh**

    j.  **calc.enduse_group.electricity.water_systems.energy_consumption..kwh**

    k.  **calc.enduse_group.natural_gas.hvac.energy_consumption..kwh**

    l.  **calc.enduse_group.natural_gas.interior_equipment.energy_consumption..kwh**

    m.  **calc.enduse_group.natural_gas.water_systems.energy_consumption..kwh**

    n.  **calc.enduse_group.other_fuel.hvac.energy_consumption..kwh**

    o.  **calc.enduse_group.other_fuel.interior_equipment.energy_consumption..kwh**

    p.  **calc.enduse_group.other_fuel.water_systems.energy_consumption..kwh**

    q.  **calc.enduse_group.site_energy.hvac.energy_consumption..kwh**

    r.  **calc.enduse_group.site_energy.interior_equipment.energy_consumption..kwh**

    s.  **calc.enduse_group.site_energy.lighting.energy_consumption..kwh**

    t.  **calc.enduse_group.site_energy.refrigeration.energy_consumption..kwh**

    u.  **calc.enduse_group.site_energy.water_systems.energy_consumption..kwh**

8.  Finally, for each fuel type, specifically "district_cooling", "district_heating", "electricity", "natural_gas", and "other_fuel", create a new column titled '**localized.weighted.**' concatenated with the fuel type listed above concatenated with **'.total.energy_consumption'**. These values are the summation of the localized fuel type end use energy values calculated in step 7 on a fuel type basis. For the value of each row's cell sum the row values associated localized fuel variables calculated in step 7.

At this point use the columns that start with '**localized.weighted.**' in addition to the **in.comstock_building_type_group** and **ComStock Floor Area Bin** columns in the *included models* sheet to calculate segmentations as desired. Keep in mind that the '**in.**' and '**param.**' variables defined in the *included models* sheet can additionally be used to perform rudimentary segmentations. It is highly recommended that no more than two segmentation filters be applied to the results, given the relatively small ComStock model count that will typically result from this process. For additional details on the columns and what they mean please refer to the data dictionary available on OEDI. The data dictionary for the ComStock End Use Savings Shape 2023 Release 1 can be found [here](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2023/comstock_amy2018_release_1/data_dictionary.tsv).
