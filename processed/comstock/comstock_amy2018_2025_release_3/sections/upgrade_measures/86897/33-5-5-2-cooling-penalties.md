<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86897.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86897.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86897.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/86897.md | section: 5.5.2 Cooling Penalties | lines: 579-623 -->
## 5.5.2 Cooling Penalties

Additionally, Figure 4 shows that several models with the DCV measure applied have electricity cooling penalties. Most of these models do not have economizers (Figure 9). The cooling penalties in these no-economizer models make sense because DCV will reduce outdoor air rates during periods of low occupancy regardless of whether an air loop is in cooling mode and bringing in design outdoor air would be beneficial to cool the air delivered to the zones. This results in higher cooling energy because the system is cooling the return air rather than benefiting from cooler outdoor air. Cooling penalties in some models with economizers can also be explained using this logic. Figure 10 shows that only 37% of models with economizers and cooling penalties have economizers on all their air loops. The remaining 63% have economizers on a fraction of the air loops, and the no-economizer loops are losing the benefit of cool outdoor air while in cooling mode.

Figure 9. Distribution of electricity cooling penalties by economizer type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86897.yaml
     source: 86897_images/image_000010_4b2093a9cfc86a35ed080ec2dd4334dfdec229c009304fd18b83f80e4b49504f.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 9. Horizontal strip and box plot of cooling electricity percent savings for models with cooling penalties, split into four economizer categories, where the No Economizer row carries by far the densest and longest negative tail](86897_images/image_000010_4b2093a9cfc86a35ed080ec2dd4334dfdec229c009304fd18b83f80e4b49504f.png)

Horizontal distribution plot restricted to models that show electricity cooling penalties, so every point lies at or below zero. X-axis: Cooling Electricity Energy Consumption Percent Savings, dimensionless, from minus 3.0 to 0.0, so minus 1.0 is a 100% increase in cooling electricity. Four rows, bottom to top: No Economizer, Fixed Dry Bulb, Differential Enthalpy, Differential Dry Bulb. Each row is a narrow grey box pinned against zero with a scatter of individual points trailing to the left. No Economizer is the densest row and has the longest tail, a continuous band of points from about minus 0.8 back through minus 1.6 and isolated points near minus 2.0 and minus 2.9. Fixed Dry Bulb trails to about minus 0.85, Differential Enthalpy only to about minus 0.45, and Differential Dry Bulb sits almost entirely within minus 0.1 apart from single points near minus 0.5 and minus 2.8. This supports the Section 5.5.2 argument that most penalized models have no economizer: DCV cuts outdoor air during low occupancy even when the air loop is cooling and would benefit from cool outdoor air, so the system cools return air instead.

Figure 10. Fraction of air loops in a model with economizers for models with electricity cooling penalties and fixed dry bulb, differential dry bulb, or differential enthalpy economizers

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86897.yaml
     source: 86897_images/image_000011_e23cf6ec67ad9c980f059f5989f0340e1fa265f1873544b2645ab0db37fabe82.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 10. Histogram of the fraction of a model's air loops that have an economizer, for the 11,096 models with cooling penalties and an economizer, showing a spike of 4,126 models (37%) at a fraction of 1.00 and most of the rest below 0.25](86897_images/image_000011_e23cf6ec67ad9c980f059f5989f0340e1fa265f1873544b2645ab0db37fabe82.png)

Bar histogram with a printed count above every bar. X-axis: Fraction Air Loops with Economizer (bin), labeled 0.05 through 1.00 in steps of 0.05. Y-axis: Count of Fraction Air Loops with Economizer, 0 to 4,500. Counts left to right: 655, 2,485, 1,662, 719, 376, 266, 104, 130, 299, 16, 18, 80, 53, 40, 40, 27 and then 4,126 in the 1.00 bin; three bins in the upper middle of the range are empty. The 17 printed counts sum to 11,096, and 4,126 of 11,096 is 37.2%, which is exactly the Section 5.5.2 statement that only 37% of models with economizers and cooling penalties have economizers on all their air loops and that the remaining 63% have economizers on only a fraction of loops. The distribution is strongly bimodal: a tall cluster from 0.05 to 0.25 (5,897 models, 53% of the total) plus the all-loops spike. Retrieval caveat: the sentence printed under this figure in the source, 82 of 289 (28%) models have economizers on all air loops, is inconsistent with both the plotted counts and the 37% in the surrounding prose.

82 of 289 (28%) models have economizers on all air loops.

For models with economizers on all air loops, we would expect the DCV measure to not affect the cooling energy consumption as the economizer will override the DCV when it is advantageous to bring in 100% outdoor air. Most of these models are in Very Cold, Cold, or Marine climate zones (Figure 11) and therefore have low cooling loads. One of these models is a

17,500-ft 2 small office in Fairbanks, Alaska, with a PVAV with parallel fan powered (PFP) boxes HVAC system and fixed dry bulb economizer on its two air loops. The annual electricity cooling consumption increases from 4,700 kWh to 5,800 kWh (22.6% increase) between the baseline and upgrade model. While the percent increase is notable, the actual increase (1,100 kWh) is minimal. These models also show no change in their design outdoor air rates between the baseline and upgrade model, and the average outdoor air fraction is reduced, indicating the DCV measure is being applied correctly.

The models located in a Hot-Dry climate zone had very minimal electricity cooling penalties, between 0.001 and 2%, and all have some form of VAV system (VAV chiller with gas boiler reheat, VAV chiller with PFP boxes, or PVAV with gas heat with electric reheat). Models are showing that the DCV measure is being applied correctly, so the cooling penalties in these models are assumed to be anomalies, but has minimal impact on the overall results of this measure.

Figure 11. Count of models with economizers on all air loops and electricity cooling penalties by Building America climate zone

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86897.yaml
     source: 86897_images/image_000012_2e16966ae8c7a9140faf09598c218307fb35c4ce2bd09a6d7ab5c7b23cba2241.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 11. Bar chart of model counts by Building America climate zone for the 4,129 models that have economizers on all air loops and an electricity cooling penalty, dominated by Marine at 2,360 and Cold at 1,130](86897_images/image_000012_2e16966ae8c7a9140faf09598c218307fb35c4ce2bd09a6d7ab5c7b23cba2241.png)

Vertical bar chart with a printed count above every bar. X-axis, eight Building America climate zones in alphabetical order. Y-axis: Model Count, dimensionless, 0 to 2,600. Values: Cold 1,130, Hot-Dry 359, Hot-Humid 16, Marine 2,360, Mixed-Dry 58, Mixed-Humid 40, Subarctic 13, Very Cold 153. The counts sum to 4,129 models. Marine, Cold and Very Cold together are 3,643, or 88% of the population, which corroborates the Section 5.5.2 claim that most of these models are in Very Cold, Cold or Marine zones and therefore have low cooling loads; the example given is a 17,500 square foot small office in Fairbanks, Alaska (the Subarctic bar) with a PVAV with parallel fan powered boxes system and a fixed dry bulb economizer on both air loops, whose annual cooling electricity rose from 4,700 to 5,800 kWh, a 22.6% increase but only 1,100 kWh. The Hot-Dry models are noted as having penalties between 0.001% and 2%, all on VAV systems. Retrieval caveat: this population should be the same as Figure 10's all-loops bin, but that bar is 4,126, three fewer.

