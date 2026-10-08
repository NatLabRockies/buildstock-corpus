<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/98223.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/98223.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/98223.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/98223.md | section: 5.5  Site Energy Savings Distributions | lines: 558-627 -->
## 5.5  Site Energy Savings Distributions

This section discusses site energy consumption for quality assurance/quality control purposes. Site energy savings can be useful for these (and possibly other) purposes, but additional factors should be considered when drawing conclusions, as site energy savings do not necessarily translate proportionally to source energy savings or energy costs, which vary widely across the United States. Savings shown in this section are based on comparisons between the baseline and pump-replacement-only scenarios on the HVAC system (including chilled water, condenser water, and hot water loops).

Figure 13 to Figure 16 show distributions of the applicable baseline ComStock models versus the upgrade scenario for percentage site energy or site energy use intensity savings with different HVAC types, fuel types, or end uses. Percentage savings provide relative impact of the measure at the individual building level while site energy use intensity savings provide absolute (or aggregated) scale of impact. The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category. It should also be noted that these pairwise comparisons represented with distributions only calculate percentage savings for buildings where the baseline included some prevalence of end use/fuel type. Thus, the electric heating savings only show buildings that originally used some amount of electric heating and do not represent buildings where natural gas was the only heating fuel.

Figure 13. Percentage site energy savings distribution for ComStock models with applied measure scenario by end use and fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98223.yaml
     source: 98223_images/image_000014_a84a1e8cbdd3518081773de611217aaa757f13dfc8fcc10ebd76b0c078bdd0e8.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 13: violin and box plots of percent site energy savings by end use and fuel type for the applicable ComStock models, with 18 rows each annotated with its model count](98223_images/image_000014_a84a1e8cbdd3518081773de611217aaa757f13dfc8fcc10ebd76b0c078bdd0e8.png)

Figure 13 of the ComStock Variable-Speed Pumps measure documentation, titled 'Upgrade 26.0: Pmp (unweighted)'. Eighteen horizontal violin-and-box distributions are plotted against 'Percent Site Energy Savings by End Use (%)' spanning -50 to 100, one per end use and fuel combination, each labeled with its applicable model count: District Heating Water Systems 270 and Heating 3,286; District Cooling Cooling 2,321; Fuel Oil Water Systems 101 and Heating 2,062; Propane Water Systems 53 and Heating 1,035; Natural Gas Water Systems 2,338 and Heating 18,861; and for Electricity, Water Systems 1,741, Refrigeration 173, Pumps 28,084, Interior Equipment 5, Heating 3,018, Heat Rejection 8,164, Heat Recovery 597, Fans 9,167 and Cooling 15,326. Electricity Pumps is by far the widest distribution, with an interquartile range of roughly 33 to 94 percent and a bimodal violin with lobes near 30 and near 100 percent; Section 5.5 attributes the upper lobe to constant-speed pumps being replaced by variable-speed models and the 100 percent cases to buildings with negligible thermal load. Electricity Heat Rejection's interquartile range is roughly 10 to 15 percent. All heating rows centre near zero with negative tails, and every Water Systems row collapses to a point at zero because the measure does not touch service water heating.

Figure 14. Site energy use intensity savings distribution for ComStock models with applied measure scenario by end use and fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98223.yaml
     source: 98223_images/image_000015_cb066f7ee64ff05df1511f80275c64caa90f665615dba6f76dd5356afd814e36.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 14: violin and box plots of absolute site energy use intensity savings by end use and fuel type for the applicable ComStock models, in kBtu per square foot](98223_images/image_000015_cb066f7ee64ff05df1511f80275c64caa90f665615dba6f76dd5356afd814e36.png)

Figure 14 of the ComStock Variable-Speed Pumps measure documentation, titled 'Upgrade 26.0: Pmp (unweighted)'. The rows and model counts are identical to Figure 13, but the x axis is 'Site EUI Savings by End Use (kBtu/ft2)' spanning about -3 to +4, so the distributions show absolute rather than percentage impact and are dominated by the end uses that consume the most energy per square foot. Electricity Pumps is again the largest positive distribution, with an interquartile range of roughly 0.05 to 0.27 kBtu/ft2 and outliers extending to about 4.4 kBtu/ft2. Electricity Cooling has the longest negative tail, reaching about -3.2 kBtu/ft2, and Natural Gas Heating spans about -1.5 to +0.45. District Cooling Cooling reaches about +1.0 and Electricity Heat Rejection about +0.36; Propane Heating, Fuel Oil Heating and District Heating Heating extend to about -1.0, -0.8 and -0.8 respectively, the heating penalty Section 5.5 describes as more efficient pumps adding less heat to the water loop. The Water Systems rows again sit at zero. Because the plotted range is only about 7 kBtu/ft2 across roughly 220 pixels, the narrow interquartile ranges other than Electricity Pumps are at the resolution limit and are described only qualitatively.

Figure 15. Percentage site energy savings distribution for ComStock models with the applied measure scenario by HVAC type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98223.yaml
     source: 98223_images/image_000016_0d69d1089a5bb39f21da89dc521323b42d3875cf07833970e492ae1c18c74c79.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 15: violin and box plots of site energy savings for the applicable ComStock models grouped by the 20 baseline HVAC system types, each row annotated with its model count](98223_images/image_000016_0d69d1089a5bb39f21da89dc521323b42d3875cf07833970e492ae1c18c74c79.png)

Figure 15 of the ComStock Variable-Speed Pumps measure documentation, titled 'Upgrade 26.0: Pmp (unweighted)'. Twenty horizontal violin-and-box distributions are plotted, one per baseline HVAC system type, with x axis tick labels running -4 to 16 in steps of 2. Rows and model counts, top to bottom: DOAS with fan coil air-cooled chiller with boiler 1,321; DOAS with fan coil chiller with baseboard electric 164, with boiler 944, with district hot water 239; DOAS with fan coil district chilled water with baseboard electric 45, with district hot water 137; DOAS with WSHP cooling tower with boiler 1,256; DOAS with WSHP with ground source heat pump 1,021; PSZ-AC with district hot water 152, with gas boiler 1,851; PTAC with gas boiler 2,590; PVAV with district hot water reheat 84, with gas boiler reheat 7,643; VAV air-cooled chiller with PFP boxes 109, with district hot water reheat 7, with gas boiler reheat 2,660; VAV chiller with PFP boxes 1,489, with district hot water reheat 535, with gas boiler reheat 3,537; and VAV district chilled water with district hot water reheat 2,139. The chiller and cooling-tower systems show the largest savings while the boiler-only systems such as PTAC and PSZ-AC with gas boiler sit at or just below zero, the pattern Section 5.5 describes.

Figure 16. Percentage site energy savings distribution for ComStock models with the applied measure scenario by climate zone

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98223.yaml
     source: 98223_images/image_000017_0df5c51617ba972c2b870f37f1299149cf79ce3c7f632a1e857b0ee688f5d91b.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 16: violin and box plots of site energy use intensity savings for the applicable ComStock models grouped by the 15 ASHRAE climate zones, in kBtu per square foot](98223_images/image_000017_0df5c51617ba972c2b870f37f1299149cf79ce3c7f632a1e857b0ee688f5d91b.png)

Figure 16 of the ComStock Variable-Speed Pumps measure documentation, titled 'Upgrade 26.0: Pmp (unweighted)'. Fifteen horizontal violin-and-box distributions are plotted against 'Site EUI Savings by Climate Zone (kBtu/ft2)' spanning -1.5 to +4, one per ASHRAE climate zone, with model counts 1A 373, 2A 1,263, 2B 541, 3A 3,178, 3B 2,957, 3C 977, 4A 5,993, 4B 765, 4C 566, 5A 5,201, 5B 2,002, 6A 2,685, 6B 532, 7 848 and 8 42. Measured interquartile ranges run from about 0.01 to 0.56 kBtu/ft2 in zone 1A and narrow steadily through the cooler zones - about 0.01 to 0.43 in 2A, 0.01 to 0.37 in 3A, 0.02 to 0.27 in 4A, 0.01 to 0.18 in 5A, 0.01 to 0.13 in 6A and 0.01 to 0.14 in zone 7. That ordering is the basis for Section 5.5's conclusion that hotter climates, which require more chiller energy, see greater savings. Zone 8 is the exception, showing the widest interquartile range of any zone at about 0.01 to 0.62 kBtu/ft2, but it has only 42 applicable models. Zone 1A also has the widest violin, with mass extending from about -1.2 to beyond +2 kBtu/ft2.

Highlights of conclusions drawn from Figure 13 through Figure 16 include:

- Positive electricity pump savings (Figure 13):
- o The primary savings result from replacing old pumps with newer, more efficient models.
- o The observed 100% electricity savings for pumps are attributed to buildings with minimal annual heating and cooling demands. Due to their inherently low thermal loads, pump operation in these buildings is infrequent. When these pumps are replaced with high-efficiency models featuring improved part-load performance, the resulting energy consumption is extremely low, often below measurable thresholds (e.g., &lt;0.1 kWh). In simulation outputs, this low consumption is rounded to zero, especially when compared to significantly higher energy use from other end uses.
- o Regarding the interquartile range of pump electricity savings, the higher end (e.g., &gt;80% savings) corresponds to cases where constant-speed pumps are replaced with variable-speed pumps, resulting in bigger efficiency gains. Conversely, the lower end of the range (e.g., &lt;40% savings) typically reflects scenarios where older variable-speed pumps are upgraded to newer models, offering more modest improvements due to the better part-load capabilities.

- o Figure 15 illustrates energy use intensity savings, which enables more meaningful comparisons across buildings of different sizes by normalizing energy savings relative to floor area.
- Positive electricity heat rejection savings (Figure 13):
- o These savings stem from reduced electricity usage by cooling towers in watercooled chiller systems.
- o Constant-speed condenser water pumps are upgraded to variable-speed pumps, enabling enhanced modulation and reduced flow during part-load conditions. This decreases the heat rejection load on the cooling tower, allowing the tower fan to operate at lower speeds or for shorter durations, ultimately reducing fan energy consumption.
- Negative heating savings (Figure 13):
- o With more efficient pumps adding less heat to the water loop, the demand for heating increases, resulting in higher usage of heating with electricity, natural gas, fuel oil, propane, or district heating.
- o However, the increase in heating energy use is outweighed by the overall site energy savings achieved through pump efficiency improvements.
- Various HVAC system types leveraging water systems with pumps (Figure 15):
- o Water-cooled chiller systems, which include cooling tower fans, tend to show relatively higher savings compared to air-cooled systems that lack cooling towers.
- o HVAC systems equipped with boilers but no chillers (e.g., packaged terminal air conditioners with gas boilers) tend to show marginally negative savings. This occurs because the reduced heat added to the water stream-due to improved pump efficiency-increases the heating load, which can outweigh the pump energy savings, particularly in buildings with already low heating demand.
- Impacts on climate zones (Figure 16):
- o Hotter climates, which require more energy for chiller systems, tend to experience greater savings from these upgrades compared to the same systems operating in colder climates.

