<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86897.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86897.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86897.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/86897.md | section: 5.5.1 Heating Penalties | lines: 538-578 -->
## 5.5.1 Heating Penalties

Some models in these end uses also saw penalties, particularly in the natural gas heating end use. We would not expect DCV to result in negative natural gas heating savings. Further investigation of these models shows that most are VAV systems located in warm climates and therefore have low heating loads (Figure 6). For example, one of these models had -100% natural gas heating savings. The baseline annual natural gas heating consumption was 2 kWh. After the DCV measure was applied, this increased to 5 kWh, which results in the -100% percent savings. 2 kWh to 5 kWh is not a significant increase and can skew the percent-savings distribution. Furthermore, the design outdoor air rates in these models remained the same between the baseline and upgrade model, but the average outdoor air fraction decreases, indicating the DCV is properly reducing operational outdoor air without impacting the design outdoor air rates. When considering the energy use intensity (EUI) savings distribution (Figure 7), natural gas heating shows practically all energy savings from the DCV measure being applied.

Figure 6. Natural gas heating savings distributions by ASHRAE 2006 climate zone

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86897.yaml
     source: 86897_images/image_000007_cdbf52cebc31c2e19f6b064ace4e61fed6b2be47fa473082edbc1728e52b4b86.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 6. Box plots of natural gas heating savings by ASHRAE 2006 climate zone across 17 zones from 1A to 8, plotted as a fraction from minus 1.8 to 1.0, with positive medians everywhere and the deepest penalties in the hot zones 1A, 2A and 3A](86897_images/image_000007_cdbf52cebc31c2e19f6b064ace4e61fed6b2be47fa473082edbc1728e52b4b86.png)

Box-and-whisker plots, one per ASHRAE 2006 climate zone, X-axis 1A, 2A, 2B, 3A, 3B, 3C, 4A, 4B, 4C, 5A, 5B, 6A, 6B, 7, 7A, 7B, 8. Y-axis: Percent Savings for Natural Gas Heating Energy Consumption, dimensionless, gridded from minus 1.8 to 1.0. Despite the axis title the scale is a fraction, so 1.0 is 100% savings and minus 1.0 is the minus 100% case discussed in Section 5.5.1. Medians sit just above zero in every zone, roughly 0.05 to 0.16, with 1A the widest box (about 0 to 0.81) and the boxes narrowing steadily toward the colder zones, where zone 8 spans only about 0.03 to 0.16. Upper whiskers reach 1.0 in most zones. Negative outliers, the natural gas heating penalties this figure is cited to explain, are concentrated in the hot and mixed zones: 2A extends to about minus 1.65 and minus 1.21, 1A and 5A each have a point near minus 1.0, and 3A reaches about minus 0.49. Zones 6A through 8 show almost no negative tail. Section 5.5.1 uses this to argue that the penalized models are mostly VAV systems in warm climates with very low heating loads, citing a model whose baseline gas heating of 2 kWh rose to 5 kWh and so registered minus 100% savings.

Figure 7. Site EUI savings distribution for ComStock models with the DCV measure applied by end use and fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86897.yaml
     source: 86897_images/image_000008_917262e039cb7869823e268aef3382d7dc1af0600cffb893eb1f3666567b2eab.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 7. Panel of 17 horizontal violin and box distributions of site EUI savings by end use and fuel type in kBtu per square foot, titled Upgrade 08: DCV (unweighted), where natural gas heating is almost entirely positive and reaches about 32 kBtu per square foot](86897_images/image_000008_917262e039cb7869823e268aef3382d7dc1af0600cffb893eb1f3666567b2eab.png)

Companion to Figure 5 with the same 17 rows and the same n values, but on an absolute intensity axis instead of a percentage one; each row label is suffixed Intensity(n=...). X-axis: Site EUI Savings by End Use in kBtu/ft2, from minus 5 to just past 30. Panel title Upgrade 08: DCV (unweighted). The mass of every distribution sits at or just above zero. Rows with visible positive spread and their approximate maxima: Natural Gas Heating about 32, District Heating Heating about 23, Other Fuel Heating about 18.5, Electricity Heating about 14, Electricity Cooling about 9.3, Other Fuel Water Systems about 8, District Cooling Cooling about 5. Negative excursions are small in absolute terms, reaching only about minus 5 for natural gas heating and district cooling and about minus 4 for electricity cooling and electricity heating. Section 5.5.1 draws the key inference from this contrast: on an EUI basis natural gas heating shows practically all savings, so the large negative percentages in Figure 5 come from models whose baseline heating consumption is so small that a trivial absolute increase produces a huge percentage penalty.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

Some models also saw electric heating penalties (Figure 5), which is unexpected with this measure. As with the models with natural gas heating penalties, most of these models are in warm climates (Figure 8) and therefore have low heating loads. One of these models, a retail building in climate zone 2B with a mixed fuel VAV system, had a 20% electric heating penalty. After the DCV upgrade, almost all gas heating was removed at the air-handling unit, and the model incurred a higher zone reheat electric penalty. The natural gas heating savings were far greater than the electric heating penalty, resulting in net heating savings, which is the case for several other models as well. These models also show no change in their design outdoor air rates between the baseline and upgrade model, and the average outdoor air fraction is reduced, indicating the DCV measure is being applied correctly.

Figure 8. Electricity heating savings distributions by ASHRAE 2006 climate zone

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86897.yaml
     source: 86897_images/image_000009_7a138b5c48b1fb792318c1e55ecea4c84bb7444a59b1cf2570e43445fdb2a515.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 8. Box plots of electricity heating savings by ASHRAE 2006 climate zone across 17 zones from 1A to 8, plotted as a fraction from minus 0.5 to 1.0, with the electric heating penalties concentrated in the hot zones](86897_images/image_000009_7a138b5c48b1fb792318c1e55ecea4c84bb7444a59b1cf2570e43445fdb2a515.png)

Box-and-whisker plots, one per ASHRAE 2006 climate zone, X-axis 1A, 2A, 2B, 3A, 3B, 3C, 4A, 4B, 4C, 5A, 5B, 6A, 6B, 7, 7A, 7B, 8. Y-axis: Percent Savings for Electricity Heating Energy Consumption, dimensionless, gridded from minus 0.5 to 1.0. As in Figure 6 the scale is a fraction rather than a percentage. Medians are slightly positive everywhere, roughly 0.02 to 0.09, and the boxes are narrow, typically 0 to 0.25 in the hot and mixed zones and tighter still, about 0 to 0.10, in zones 6B through 8. Dense columns of positive outliers run all the way to 1.0 in zones 1A through 5A. The negative tails that Section 5.5.1 discusses are largest in the hottest zones: 1A reaches about minus 0.50, 2A about minus 0.50 and minus 0.33, 2B and 3A about minus 0.22, and 5A about minus 0.50, while zones 6A through 8 show essentially no penalty. The example in the text is a retail model in climate zone 2B with a mixed-fuel VAV system that took a 20% electric heating penalty, that is minus 0.2 on this axis, because removing nearly all air-handling-unit gas heating pushed load onto electric zone reheat; its gas heating savings still exceeded the electric penalty.

