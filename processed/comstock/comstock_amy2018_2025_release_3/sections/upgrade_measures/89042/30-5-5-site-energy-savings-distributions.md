<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89042.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/89042.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/89042.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89042.md | section: 5.5  Site Energy Savings Distributions | lines: 737-797 -->
## 5.5  Site Energy Savings Distributions

This section discusses site energy consumption savings between the standard performance and baseline scenario for quality assurance/quality control purposes. Site energy savings can be useful for these (and possibly other) purposes, but additional factors should be considered when drawing conclusions. This is because site energy savings do not necessarily translate proportionally to source energy savings, greenhouse gas emissions avoided, or energy cost, which vary widely across the United States.

Figure 14 through Figure 16 show distributions of the applicable baseline ComStock models versus the standard performance HP-RTU upgrade scenario for percent site energy or site end use intensity (EUI) savings with different end use, fuel type, or climate zone. Percent savings provide relative impact of the measure at the individual building level, while site EUI savings provide absolute (or aggregated) scale of impact. Also, the data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

Figure 14. Percent site energy savings (compared to baseline) distribution for ComStock models with the HP-RTU measure applied by end use and fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000016_78cb71c55bf0099c4924da0f6e11cda3c99f2697b5568a5c00f5297cc3ce5d7c.png
     method: vision-description
     described: 2026-08-22 -->

![Violin and box distributions of percent site energy savings by end use and fuel type](89042_images/image_000016_78cb71c55bf0099c4924da0f6e11cda3c99f2697b5568a5c00f5297cc3ce5d7c.png)

Figure 14: violin plots with embedded box plots of percent site energy savings by end use and fuel for models with the standard performance HP-RTU applied, x-axis -160 to 100 percent, sample counts printed per row. Natural gas and other fuel heating cluster near complete savings, while electricity heating, fans and heat recovery carry negative tails. Section 5.5 discusses these.

Figure 15. Site EUI savings (compared to baseline) distribution for ComStock models with the HPRTU measure applied by end use and fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000017_1a7425c5ecff06e06a69ef854f3fa049a164acd648a1a1022308bdfeea9e0539.png
     method: vision-description
     described: 2026-08-22 -->

![Violin and box distributions of site EUI savings by end use and fuel in kBtu per square foot](89042_images/image_000017_1a7425c5ecff06e06a69ef854f3fa049a164acd648a1a1022308bdfeea9e0539.png)

Figure 15: the same end-use rows plotted as absolute site EUI savings in kBtu per square foot rather than percentages, x-axis -60 to 100. Natural gas heating and other fuel heating carry the mass of the savings with long right tails past 40 kBtu per square foot, while the electricity end uses sit tightly around zero. Section 5.5 discusses these.

Figure 16. Site EUI savings (compared to baseline) distribution for ComStock models with the applied HP-RTU measure by climate zone

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000018_2bfa8d9aae52703a5b5db4fb1997ce37b83a9bf5101e6dbb5ff4c7a2b14410c6.png
     method: vision-description
     described: 2026-08-22 -->

![Violin and box distributions of site EUI savings by ASHRAE climate zone in kBtu per square foot](89042_images/image_000018_2bfa8d9aae52703a5b5db4fb1997ce37b83a9bf5101e6dbb5ff4c7a2b14410c6.png)

Figure 16: violin plots with embedded box plots of site EUI savings in kBtu per square foot for models with the HP-RTU measure applied, one row per ASHRAE climate zone from 1A to 8 with sample counts, x-axis -15 to 60. Medians rise with heating severity, and zones 5A through 7 carry the longest positive tails. Section 5.5 covers the pattern.

Highlights of conclusions drawn from Figure 14 through Figure 16 include:

- Fuel switching of combustion fuel-based heating:
- o Up to 100% savings on combustion fuel used for heating, as shown in Figure 14. Data points showing savings less than 100% indicate buildings with multiple heating fuels and where the upgrade is only applicable to some of those systems.
- o Absolute or aggregated impact of heating savings (using natural gas or other fuel) is more noticeable compared to the other end uses, as shown in Figure 15.
- o Absolute or aggregated savings penalty of electricity for heating due to fuel switching is well-depicted in Figure 15. This is especially noticeable in the colder climates.
- Conversion of electric resistance heating to HP-RTU heating:
- o Positive savings on electricity used for heating, as shown in Figure 14, leveraging more efficient heat pump compared to electric resistance heating.
- o Electric heating distribution only includes buildings in the baseline that had at least some electric heating load, and therefore does not show the electric heating increase of buildings without electric heating load with heat pumps.
- Higher cooling COP of HP-RTU compared to old buildings with older equipment:
- o Positive savings on electricity used for cooling and fans, as shown in Figure 14.
- o Absolute or aggregated savings scale is depicted in Figure 15.
- Increased site energy savings potential in colder climates:
- o By leveraging heat pumps that can operate down to 0 ° F (-17.9 ° C), savings potential is increased compared to hotter regions by leveraging higher efficiencies on both (heating and cooling) ends, as shown in Figure 16.
- o This is because heat pumps generally have higher heating 'site' energy COPs compared to gas or electric resistance RTUs, and colder climates have higher overall heating loads. However, as mentioned, site energy savings do not necessarily translate to energy cost savings.
- Others:
- o Data points for extreme (e.g., -150% savings for electricity used for cooling) positive/negative savings, shown in Figure 14, are 1) buildings either in very hot or very cold climates, 2) where absolute heating or cooling demand is small, and 3) a small change (due to upgrade) in heating or cooling demand (e.g., MWh) resulting in large relative (e.g., %) savings. The absolute impact of these data points should be understood with site EUI savings distributions.
- o More detailed findings related to the advanced HP-RTU can be found in the previous documentation, released in March 2023).
- o It should also be noted that figures showing higher site EUI savings toward colder climates in Figure 16 may not correspond to cheaper utility bills or decreased

greenhouse gas emissions. The only reason this trend happens is because we get more heating load in colder climates, so the COP improvements make a bigger relative impact.

