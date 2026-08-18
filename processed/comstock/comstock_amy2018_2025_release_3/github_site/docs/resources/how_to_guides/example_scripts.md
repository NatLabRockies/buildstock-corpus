<!-- comstock 2025-3 | github_site | docs/resources/how_to_guides/example_scripts.md -->
# Access the ComStock Datasets Programmatically

# How-to: Access the ComStock datasets programmatically
These example queries and scripts demonstrate how users can access the ComStock datasets programmatically and provide a jumping off point for analysis.

More content will be posted as it becomes available.

## AWS Athena and SQL Queries
- [Example AWS Athena Queries](docs/resources/how_to_guides/aws_athena_queries.md). AWS Athena queries that pull data from a ComStock dataset release to address four example prompts.

## Python
### Jupyter Notebook
_These example notebooks were developed using the ComStock 2024 Release 2 dataset. Some dataset attributes, like column names, may have changed from earlier releases. Most notably, the [ComStock sampling method was updated](docs/resources/explanations/new_sampling_method.md) beginning with 2024 Release 2._
- [Download Annual Baseline and Upgrade Data][1]. Example Jupyter Notebook for pulling annual baseline and upgrade results from the Open Energy Data Initiative (OEDI) data lake, filtering to a specific geography, and plotting comparisons. Requires an Amazon Web Services (AWS) account.
- [Download Individual Building Load Profiles][2]. Example Jupyter Notebook for pulling individual baseline and upgrade load profiles from the OEDI data lake for a given geography and plotting comparisons. Requires an AWS account.

[1]:../../../assets/files/download_annual_baseline_and_upgrade_data.ipynb
[2]:../../../assets/files/download_individual_building_profiles.ipynb
