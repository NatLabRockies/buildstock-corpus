<!-- comstock comstock_amy2018_2025_release_3 | github_site | docs/resources/explanations/comstock_calibration.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/resources/explanations/comstock_calibration.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/resources/explanations/comstock_calibration.html | corpus_version: 0396270 | corpus_path: github_site/docs/resources/explanations/comstock_calibration.md | section: ComStock Calibration, Validation, and Uncertainty | lines: 2-23 -->
# ComStock Calibration, Validation, and Uncertainty

# Considerations for ComStock Calibration, Validation, and Uncertainty

A common question is whether ComStock™ is appropriately calibrated for a specific use case. The answer is highly interpretive based on many factors, including the robustness of relevant model inputs, the type of data needed (15-minute time series, annual averages, etc.), the stock segment of interest (e.g., building type, location), and the user’s tolerance for uncertainty. This document discusses the resources available to approach this question for a specific use case with examples.

ComStock has been calibrated and validated as part of the three-year End-Use Load Profiles (EULP) project. This includes using 15-minute advanced metering infrastructure (AMI) time series data from 10 regions at the building type level to improve/validate load profiles. Moreover, annual comparisons were made to the AMI data as well as the Commercial Building Energy Consumption Survey (CBECS). Beyond EULP, the ComStock tool is continuously improved as data and resources become available. Note, however, the EULP project focused on electricity calibration and therefore did not attempt to calibrate natural gas. ComStock is known to underestimate natural gas consumption, and there are ongoing efforts to resolve this issue.

There are two primary resources to help understand the calibration state and relevant model inputs of ComStock for a given use case:
1. The [EULP Final Report](https://www.nlr.gov/docs/fy22osti/80889.pdf) provides a detailed description of the ComStock calibration/validation process and results.
- Describes the 10 regional AMI data sources used (p. 36–37)
- Load profile comparisons to AMI data sources, normalized and raw, per region and building type (p. 210–292)
- Comparisons of annual energy use intensity (EUI) distributions to CBECS and AMI by region and building type (p. 210–292).

2. [ComStock Documentation](docs/resources/resources.md#references) provides the methods, assumptions, and data sources used in ComStock.
- Describes assumptions and data sources for each model feature (e.g., How are HVAC system types assigned to models? How are lighting types determined? How are data centers accounted for in offices?)
- Describes model outputs
- General reference guide for users.

Determining if ComStock is appropriate for a given use case is ultimately a judgement call for the user with the combined help of these resources. The EULP Final Report should be referenced to understand how well ComStock aligns to other available data sources, both annually and subhourly. ComStock Documentation should be engaged to understand the data sources and assumptions used to build the models.
It is important to note that there is limited data available similar to that produced by ComStock, and therefore it is difficult to confidently validate the tool. Furthermore, the data sources that are available often have errors and discrepancies of their own. This poses further challenges when validating the model. For all intents and purposes, there is no “truth” data to determine how well ComStock matches reality. Rather, there are data sources that we can compare to increase or reduce our confidence in an aspect of the model. When one or multiple data sources align with each other and ComStock, confidence in that aspect of the model is increased. When multiple data sources do not align well with each other and/or ComStock, it becomes difficult to determine the calibration status of the tool. Users should compare their own data with ComStock, such as city benchmark data, whenever possible. They should ultimately rely on their own judgment, with the resources available, to decide if ComStock is suitable for their use case.

