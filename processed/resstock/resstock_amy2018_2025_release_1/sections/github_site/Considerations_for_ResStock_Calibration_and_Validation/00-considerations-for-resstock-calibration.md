<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/explanations/Considerations_for_ResStock_Calibration_and_Validation.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/explanations/Considerations_for_ResStock_Calibration_and_Validation.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/explanations/Considerations_for_ResStock_Calibration_and_Validation.html | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: github_site/docs/resources/explanations/Considerations_for_ResStock_Calibration_and_Validation.md | section: Considerations for ResStock Calibration and Validation | lines: 2-18 -->
# Considerations for ResStock Calibration and Validation

A common question is whether ResStock has been appropriately calibrated for a specific use case. The answer is dependent on many factors, including the robustness of the relevant model inputs, the type of data needed, the housing segment of interest, and the user's tolerance for uncertainty.

ResStock has been calibrated and validated as part of the three-year [End Use Load Profiles (EULP)](https://www.nlr.gov/buildings/end-use-load-profiles.html) project. EULP calibrated and validated ResStock against 33 measured datasets including utility load research data, advanced metering infrastructure (AMI) data from utilities, the U.S. Energy Information Administration Residential Energy Consumption Survey (RECS) monthly data, and sub-metered datasets. ResStock is continually improved through new input and calibration/validation data as they becomes available.

There are two main ways to understand the calibration process and model inputs:
1. The [EULP Final Report](https://www.nlr.gov/docs/fy22osti/80889.pdf) provides a detailed description of the initial ResStock calibration and validation process and results.

    - Section 2.3.6 Empirical Data Used for Residential Calibration and Validation

    - Section 4.1 Final Calibration and Validation Results - Residential

2. [ResStock Documentation](https://www.nlr.gov/docs/fy18osti/68670.pdf) provides the methods, assumptions, and data sources used in ResStock.
    Note: This documentation is for an older version of ResStock. New documentation is being written with an expected release date in fall 2024.

Determining if ResStock is appropriate for a given use case is ultimately a judgement call for the user with the combined help of these resources. **The ResStock team and the U.S. Department of Energy are not responsible for any actions or consequences that arise because of the assumptions, conclusions, or performed work that is based on ResStock.** The EULP Final Report should be referenced to understand how well ResStock aligns to other available data sources, both annually and subhourly. ResStock documentation describes the data sources and assumptions used to build the models. Keep in mind that the data sources used in ResStock potentially have their own errors and biases, which can be reflected in ResStock. ResStock is a model of residential housing, not an actual representation of residential housing. Therefore, users should compare their own data with ResStock whenever possible. Users should rely on their own judgement, with the resources available, to decide if ResStock is suitable for their use case.
