<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/FAQ.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/FAQ.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/FAQ.html | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: github_site/docs/FAQ.md | section: Analysis | lines: 197-226 -->
## Analysis

### Can I run ComStock and ResStock myself?

The code required to run ComStock and ResStock is available on our public GitHub repositories: [https://github.com/NatLabRockies/ComStock](https://github.com/NatLabRockies/ComStock) ; [https://github.com/NatLabRockies/ResStock](https://github.com/NatLabRockies/ResStock). Other related code repositories are provided on the For Developers page for [ComStock](https://natlabrockies.github.io/ComStock.github.io/docs/for_developers/for_developers.html) and [ResStock](docs/developers.md).

While these resources are available, ComStock and ResStock are complex modeling tools and there is no documentation for running the model other than what exists in the codebase, and we are not able to support running the models at this time. We generally do not recommend running the model unless you have a deep understanding of the methodology and objectives. Please email us at [ComStock@nlr.gov](mailto:ComStock@nlr.gov) or [ResStock@nlr.gov](mailto:ResStock@nlr.gov)  if you have suggestions for improvements or specific needs.

### I am interested in an upgrade measure combination that is not currently available as an upgrade package in the public datasets. Can I combine results from the individual measures?

Our general guidance is to NOT combine measure results. There are interactions between most upgrade measures that affect the amount of savings and make results of multiple measures together misleading.

See an explanation and examples on this topic, for [ComStock](https://natlabrockies.github.io/ComStock.github.io/docs/resources/explanations/combining_measure_results.html) and [ResStock](docs/resources/explanations/Individual_Measures_Not_Combined.md).

Please email us at [ComStock@nlr.gov](mailto:ComStock@nlr.gov) or [ResStock@nlr.gov](mailto:ResStock@nlr.gov) if you have questions about combining specific measures.

### I want to analyze only part of a package, not the whole package. Can I compare samples that did not get this part of the upgrade, with samples that got the full upgrade to analyze the impact?

Yes you can, but there are a few caveats to be aware of. For example, if looking at one envelope package that includes air sealing, insulation, and duct sealing, downselecting to models without the wall insulation measure applied is creating a biased sample, since the package applies wall insulation only to uninsulated wood stud walls. Using this method, you are removing some of the poorest performing buildings. Take a look at the samples to see how many samples you would be removing with this approach, and then consider if it is reasonable.

### How do I calculate COP?

The as-simulated heating COP can be determined by calculating the heating delivered divided by the energy consumed for heating. Because ResStock outputs these values with different units, a unit conversion is also required.

For example, the COP of an all-electric heating system can be calculated as (out.load.heating.energy_delivered.kbtu * (293.07 / 1000)) / (out.electricity.heating.energy_consumption.kwh + out.electricity.heating_fans_pumps.energy_consumption.kwh + out.electricity.heating_hp_bkup.energy_consumption.kwh + out.electricity.heating_hp_bkup_fa.energy_consumption.kwh)

This can be calculated using the timeseries results to get the COP at an individual timestep, or using totals for the year from the metadata_and_annual files to get an annual average value.

Heating systems that use additional fuels in addition to electricity will require additional fields to be included in the denominator. E.g. out.natural_gas.heating.energy_consumption.kwh

