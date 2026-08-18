<!-- comstock 2025-3 | github_site | docs/resources/explanations/sample_size_considerations.md -->
# Sample Size Considerations

A frequently asked question is, “How granular are ComStock™ data sets?” The answer depends in part on which portion of the dataset you are using and the question(s) you are trying to answer. The appropriate geography (e.g., state, county, PUMA, or tract) to use for your analysis depends on several factors, including but not limited to:
- Sample count
- Quality of building characteristic distribution input data
- A given building characteristic’s probability distribution dependencies

There are other important considerations when conducting analysis using ComStock datasets not covered in this explanation, including modeling methods and assumptions, and calibration. See the [ComStock reference documentation](docs/resources/resources.md#references) for information.

## Updated Sampling Methodology
Note that the ComStock sampling methodology was updated as of 2024 Release 2 (see [new sampling method overview](docs/resources/explanations/new_sampling_method.md) for more detail, including updates to the OEDI file structure). In the new sampling method, a single energy model may be used to represent multiple similar buildings across distinct but comparable geographies through a reallocation process. As a result, there are two types of metadata and annual results files available on OEDI: (1) aggregate files that combine duplicate building IDs for a given geography, and (2) “raw” files that show all instances of each building ID after the reallocation process.

This explanation provides guidance for assessing the sample count for the both the aggregate, and raw, unaggregated metadata and annual results files.

## Sampling Overview
In ComStock, U.S. commercial building characteristics are sampled so that each building energy model (BEM) does not represent a specific real-world building but rather a small, representative portion of the overall building stock. This is achieved through a two-step process. First, ComStock generates "sampled models" that capture the diversity of U.S. commercial buildings based on key characteristics such as building type, size, vintage, and energy sources. Second, the sampled models are allocated to specific geographic regions using "stock truth data" estimates.

To create the sampled models, ComStock selects a subset of input characteristic combinations, prioritizing five key segmentation factors: building type, heating fuel type, HVAC system type, building size, and sampling region. This process results in approximately 12,000 unique combinations, each of which is allotted 12 samples. The remaining input characteristics are assigned through sampling their probability distributions. In the ComStock results, there are 12 modeled samples per combination. In some cases, simulation failures may result in one or two missing models within a given combination.

Once generated, these models are allocated to geographic regions using stock truth data, which estimates the distribution of buildings by type, size, and vintage. The allocation process is quasirandom, ensuring that each sampled model is placed in locations where it is most representative of the building stock.

For more detail, please see the [ComStock reference documentation](docs/resources/resources.md#references).

## Sample Count
Any estimate of the energy consumption of the U.S. commercial building stock relies heavily on an estimate of how much building floor area exists in each part of the country. ComStock uses multiple data sources to create probabilistic distributions used in its stock estimation process. For more details about the ComStock stock estimation and sampling process, please see the [Sampling and Weighting in ComStock](docs/resources/explanations/sampling_and_weighting.md) explanation.

The minimum sample count required for a given geography in ComStock is a function of the number of commercial buildings present in that area, as well as the quality of available input data for the ComStock model. The allocation of ComStock samples aims to achieve representative coverage across different geographic regions while reflecting the variability in local building stock data. When using ComStock, it is important to double-check the total square footage in your analysis against your best judgment or other trusted sources—does it make sense for your region or use case? Because ComStock draws from multiple underlying datasets of varying quality, including assessor data aggregated at the national level, some areas may have gaps or inaccuracies in representation. Users should be aware that the representativeness and accuracy of ComStock results can vary depending on the quality of local data sources.

## Building Characteristic Probability Distribution Assignment Conditions
The probability distributions for the building characteristic fields are described in Table 2 of the [ComStock reference documentation](docs/resources/resources.md#references). Many of the fields in the Commercial Building Energy Consumption Survey (CBECS) data source are only resolved to the census division level, while data sources such as CoStar and Lightbox are resolved to the census tract level and below. To determine how good a probability distribution is, one must understand the data source and then make a judgement call. For example, the data source for HVAC system type fields is CBECS. So, ComStock may not accurately capture the HVAC system type distribution at anything finer than census division resolution, while several data sources including CoStar and accessors data are the source for the fields building type, size (square feet), vintage, and number of stories.

## Determining Sample Count in ComStock Datasets
You can determine the number of samples in the ComStock dataset by counting the unique values in the bldg_id column within the metadata_and_annual_results files available on OEDI. Each bldg_id corresponds to a single building energy model, or sample, in ComStock.

Starting with ComStock 2024 Release 2, a [new sampling method](docs/resources/explanations/new_sampling_method.md) was introduced to reduce the number of samples while maintaining representativeness of the U.S. commercial building stock via a reallocation process. As a result, you may now see multiple records with the same bldg_id within a given geography—these duplicates are intentional and reflect reallocated rather than distinct models. Models with the same bldg_id are identical in characteristics and performance. When assessing sample size for analysis, use the count of **unique** bldg_id values.

Note that "metadata_and_annual_results_aggregate" files are also available on OEDI, which consolidate data by combining duplicate models in the geography. Each bldg_id appears only once, with an associated weight representing the sum of the weights of all instances of the bldg_id in the geography.

## Recommendations
Additional models may be required to maintain statistical robustness in more detailed analyses. The need for more models depends on the level of specificity in your analysis. For example, if analyzing energy performance trends across small office buildings, you should have at least six small office samples to capture variability. However, if you refine the analysis further—such as looking specifically at small offices with hours of operations exceeding 18 hours—you now need at least six small office buildings with hours of operations exceeding 18 hours.

This principle applies to other segmentation factors as well, such as building sub-type, vintage, and building size. For instance, if you’re evaluating retail strip malls with 20% restaurant square footage, you should ensure at least six samples are of that specific building sub-type. If you want to understand the energy use across different vintages, you’d need at least six buildings per vintage group for a meaningful comparison.

When considering whether there are sufficient samples for an analysis, compare ComStock metadata results against external sources, such as Google Maps, tax assessor databases, and other local datasets. For example, use external sources to estimate how many primary schools are present in the geography, and compare against the ComStock metadata. If the number of primary schools in ComStock is significantly lower than in the external sources, consider adjusting the ComStock data to better reflect the building stock in that specific geography. Use methods such as those detailed in the how-to guide titled [Understand the annual energy use by building type for a city](docs/resources/how_to_guides/puma_level_analysis.md) to make these adjustments.
