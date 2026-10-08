<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95002.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95002.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95002.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/95002.md | section: 5.5  Site Energy Savings Distributions | lines: 701-752 -->
## 5.5  Site Energy Savings Distributions

This section discusses site energy consumption for quality assurance/quality control purposes for the Reduced Thermostat Setbacks for Heat Pumps measure. Note that while site energy savings can be informative for these purposes, they don't always correspond directly to outcomes of greater practical significance, such as source energy savings, reduced energy bills, or avoided CO₂e emissions. It's important for a decisionmaker to consider which metrics best align with their specific goals or context. See the documentation for the Standard Performance HP-RTU measure for analysis of the savings impact of that measure alone [11].

Figure 20 shows percent site energy savings distributions by end use for the HP-RTU with reduced setbacks measure compared to the corresponding baseline model. For comparison purposes, Figure 21 shows the same distributions for the HP-RTU measure with standard setbacks. The percent site energy savings by end use are very similar for the two measures. The very small changes in refrigeration energy use observed for some buildings under both measures results from slight variations in indoor air temperature. Both measures show a reduction in interior equipment electricity use for a small number of models (30-40). This is the result of a known issue in the ComStock workflow that results in different schedules between the baseline and upgrade workflows. The effect of this bug on the overall energy results is negligible.

Figure 22 and Figure 23 show percent site energy savings distributions by climate zones for the HP-RTU measures with and without setbacks, respectively. Distributions of energy savings by climate zone are also very similar between the two measures, with a few exceptions. Climate Zones 3A, 4A, 5A, 6B, and 8 have a longer portion of the distribution with negative energy savings under the reduced setbacks, relative to standard setbacks, though this accounts for a small number of datapoints. (Climate Zone 8 has only around 240 samples in total applicable to this measure.) In general, the HP-RTU with reduced setbacks measure has a slight energy penalty relative to the HP-RTU measure with standard setbacks, as expected, due to the greater number of hours with heating operation at higher setpoints.

Figure 20. Percent site energy savings distribution for ComStock models with applied measure scenario (HP-RTU with reduced setbacks) by end use and fuel type. The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95002.yaml
     source: 95002_images/image_000022_cd736b36cd705534a39cdae1f8927cb100c9ca1c4f110a35ed035955e1511844.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by end use and fuel, reduced-setback scenario](95002_images/image_000022_cd736b36cd705534a39cdae1f8927cb100c9ca1c4f110a35ed035955e1511844.png)

Figure 20: horizontal violin-and-box plots titled Upgrade 9.0: HPRTU_Reduced_Setback (unweighted), x-axis Percent Site Energy Savings by End Use (-160% to 100%). Rows are end-use/fuel pairs with sample sizes, from Other Fuel Water Systems (n=151) to Electricity Cooling (n=34279). Fossil heating rows cluster near 100% savings, while Electricity Heating (n=14060) and Electricity Fans (n=34336) straddle zero with long negative tails.

Figure 21. Percent site energy savings distribution for ComStock models with applied measure scenario (HP-RTU with standard setbacks) by end use and fuel type. The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95002.yaml
     source: 95002_images/image_000023_598db99918849e382f6406385bab8769f7f5c4d4cfdd777adec5342c7e26a750.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by end use and fuel, standard-setback scenario](95002_images/image_000023_598db99918849e382f6406385bab8769f7f5c4d4cfdd777adec5342c7e26a750.png)

Figure 21: the Figure 20 companion for Upgrade 4.0: HPRTU_Std_Perf (unweighted), on the same axes - x-axis Percent Site Energy Savings by End Use (-160% to 100%) - with the same end-use/fuel rows and sample sizes. Distributions are very close to the reduced-setback case; Electricity Heating (n=14091) and Electricity Fans (n=34349) again center near or below zero.

Figure 22. Site energy use intensity savings (compared to baseline) distribution for ComStock models with the applied HP-RTU setback measure by climate zone

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95002.yaml
     source: 95002_images/image_000024_85bd62e887e73e7d4f99a1bd96549498bc58a8b329cb6be9a5c698de758ffb58.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by ASHRAE climate zone, reduced-setback scenario](95002_images/image_000024_85bd62e887e73e7d4f99a1bd96549498bc58a8b329cb6be9a5c698de758ffb58.png)

Figure 22: horizontal violin-and-box plots titled Upgrade 9.0: HPRTU_Reduced_Setback (unweighted), x-axis Percent Site Energy Savings by Climate Zone (-20% to 60%). One row per ASHRAE climate zone with sample sizes, 1A (n=794) through 8 (n=242). Medians sit roughly between 10% and 25% in every zone, and the colder zones carry the longer negative tails.

Figure 23. Site energy use intensity savings (compared to baseline) distribution for ComStock models with the applied HP-RTU measure by climate zone

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95002.yaml
     source: 95002_images/image_000025_004b03e035a626060552ef38d949811ede3224f6a5b484346992f699d61771ea.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by ASHRAE climate zone, standard-setback scenario](95002_images/image_000025_004b03e035a626060552ef38d949811ede3224f6a5b484346992f699d61771ea.png)

Figure 23: the Figure 22 companion for Upgrade 4.0: HPRTU_Std_Perf (unweighted), x-axis Percent Site Energy Savings by Climate Zone (-10% to 60%), with the same climate-zone rows and sample sizes. Medians again land near 10%-25% per zone, but the negative tails are shorter than under reduced setbacks - the setback reduction costs a small amount of energy savings.

