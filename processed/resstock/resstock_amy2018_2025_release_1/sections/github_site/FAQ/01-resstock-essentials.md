<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/FAQ.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/FAQ.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/FAQ.html | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: github_site/docs/FAQ.md | section: ResStock Essentials | lines: 8-39 -->
## ResStock Essentials

### Is ResStock credible?

Yes. The models underwent extensive calibration as part of the End Use Load Profiles (EULP) project where we compared model load profiles to AMI data from around the country, and updated baseline model schedules, power densities, among other things using various data sources. Reference the [EULP final report](https://www.nlr.gov/docs/fy22osti/80889.pdf) for more details. The EULP project concluded in 2021.

For details about how to determine whether the models are appropriate for a specific analysis, reference [this explanation](docs/resources/explanations/Considerations_for_ResStock_Calibration_and_Validation.md).

### Which dataset release should I use? And can I compare upgrades from different dataset releases?

We recommend using the latest data release whenever possible. However, older datasets still provide valuable information and can be used if newer datasets are not appropriate for a specific use. We do not recommend a comparison of upgrade measures across different dataset releases due to the changes and improvements made in each dataset release. Each new dataset release includes its own set of upgrade measures, some of which are repeats, and improvements made to the baseline model and modeling methodology. See the [Data page](docs/data.md) for a list of available datasets and access links, as well as technical documentation for the ResStock tool.

### What are weights in ResStock and how are they used?

Weights in ResStock represent the number of real buildings in the U.S. building stock that a ResStock model represents. Each ResStock dataset release has a different weighting factor for the building models. As seen in [this paper](https://www.nlr.gov/docs/fy22osti/80889.pdf), our model or sample weights are constructed using U.S. EIA 2009 RECS microdata. Use the weights by multiplying the column of interest by the weight. Some results columns already have the weight applied. These have the word “weighted” in the name.

### What building types does ResStock model?

ResStock models most types of housing including single-family, multifamily, and manufactured or mobile homes. See [this explanation](docs/resources/explanations/Building_Types.md) for more detail on what is not modeled.

### How many profiles or models should be used, and how does the number used affect uncertainty of results?

We recommend estimating the standard error using the standard deviation divided by the square root of the number of samples (i.e. profiles or models) and using the results to inform the appropriate minimum sample size for a particular analysis. As a conservative reference, using at least 1,000 samples  will maintain 15% or lower sampling discrepancy for many common quantities of interest, as described in the [End-Use Load Profiles methodology report section 5.1.3](https://docs.nlr.gov/docs/fy22osti/80889.pdf).

See [this explanation](docs/resources/explanations/Number_of_samples.md) which has more details and also points to other ResStock references about how to increase the number of samples and calculate the uncertainty.

### Are these load profiles measured or simulated?

The profiles are simulated using the ResStock and ComStock modeling tools, which have been validated and informed by the best available data against an array of empirical datasets. ResStock and ComStock use the EnergyPlus simulation engine. The validation results and uncertainty for quantities of interest are presented in the [End-Use Load Profiles final report](https://docs.nlr.gov/docs/fy22osti/80889.pdf).

ResStock generally simulates 550,000 individual building energy models, and ComStock simulates 150,000 building energy models.

