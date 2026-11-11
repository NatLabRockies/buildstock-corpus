<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/93846.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/93846.md | section: 4.2.1 Quantifying Demand Flexibility Impacts | lines: 572-670 -->
## 4.2.1 Quantifying Demand Flexibility Impacts

Traditional energy efficiency measures are often evaluated based on how much energy or utility bills they save on an annual basis. Because the goal of demand flexibility is to modify the load profile for a small number of days per year, metrics that evaluate the ability to modify the load are more useful than annualized energy consumption impacts.

There are many ways that the peak load impact of demand flexibility can be quantified. For this analysis, we adopted the demand decrease percentage (D3) metric, as defined by (Jingjing Liu, 2022). This metric is defined as:

The D3 metric can be computed for a single building or a group of buildings in aggregate. It can also be computed for the whole building load or for individual end uses.

This metric was adopted because it quantifies the impact for a single demand response event (in our case, each day where demand response is dispatched), but it can easily and meaningfully be summarized over multiple events. For example, the mean or quartile values can be used to describe how the impact changes during a year, a season, or a month. This is particularly useful when the demand flexibility impacts are later used as the input to other models seeking to represent demand flexibility but that do not endogenously represent building physics. Examples of such models include Lawrence Berkeley National Laboratory's DR-Path (Brian Gerke, 2019) and the Brattle Group's Load Flex model (Ryan Hledik A. F., 2019).

Because the goal of this analysis is to feed results into downstream modeling efforts, we calculated the D3 metric for the aggregate load of groups of buildings of a common type located in a common geography.

Figure 8 shows how the D3 metric varies with different pre-peak durations for cooling load flexibility on the hottest day of the year for each state. We used an approximate 20% reduction for the 2°F offset and an approximate 40% reduction for the 4°F offset. Although only the peak offset without any precooling can provide a significant percentage reduction, pairing that with precooling can push the reduction even further -more so in some states than others. Also, the longer the duration of precooling, the higher the percentage reduction, with the highest reduction coming from 4-hour precooling.

Figure 9 shows the same metrics calculated year-round. That is, we calculated the average cooling energy consumption during the peak period for the whole year for both the baseline and the upgrade, and we calculated the difference as a percentage reduction. Some states have more percentage savings year-round than their hottest day, whereas others have less. Regardless, most show a positive correlation with the duration of the pre-peak period (at all offset levels) except for a handful of states that show a surprising negative correlation. We examined the results with the largest negative correlation -an identification with a 6°F pre-peak offset to investigate how a larger precooling duration (or having precooling at all) could result in a higher load during the peak.

The answer is in how the precooling and preheating was initially implemented. In the sensitivity analysis, we always chose to either precool or preheat, depending on the daily average temperature. If the daily average temperature was less than 66°F, we classified that as a heating day, otherwise we classified the day as a cooling day; however, this might not always work neatly. For some days in shoulder season with mostly low temperatures during the morning but a hot afternoon, we classified the day as a heating day even though the building needed more cooling than heating; therefore, we mistakenly preheated a building that needed precooling (or at least not preheating).

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/93846.yaml
     source: 93846_images/image_000009_2495bdaaa88f1d942605d350662dd9d2731318e0bdc82ec792f3a82008fdbf3d.png
     method: vision-description
     described: 2026-11-11 -->

![Two line charts of percent cooling reduction by state on an extreme day, 2°F and 4°F offsets, six pre-peak durations](93846_images/image_000009_2495bdaaa88f1d942605d350662dd9d2731318e0bdc82ec792f3a82008fdbf3d.png)

Figure 8, first bitmap: two line charts, 'Offset: 2F' above 'Offset: 4F'. X-axis is state, ordered from largest to smallest reduction; y-axis is percent reduction. Six series are no pre-peak and pre-peak durations of 15 minutes, 30 minutes, 1 hour, 2 hours and 4 hours. Longer pre-peak periods give larger reductions: about 35% to 45% in the leading state at 2°F and about 62% to 75% at 4°F, falling to about 10% and 30% in the last states.

Figure 8. D3 percentage reduction of cooling energy consumption during the peak period on an extreme day and at various pre-peak durations (including no pre-peak). The top figure shows a 2°F offset for both the pre-peak and peak periods, the middle shows a 4°F offset for both, and the bottom shows a 6°F offset for the pre-peak period and a 4°F offset for the peak period. Note that the ordering of states varies.

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/93846.yaml
     source: 93846_images/image_000010_31a3b6f9472ee7882b0c081baafed934581c4572b394e472da91cc5a4f77dbc6.png
     method: vision-description
     described: 2026-11-11 -->

![Line chart of percent cooling reduction by state on an extreme day, 4°F peak offset with 6°F pre-peak offset](93846_images/image_000010_31a3b6f9472ee7882b0c081baafed934581c4572b394e472da91cc5a4f77dbc6.png)

Figure 8, second bitmap: line chart titled 'Offset: Peak 4F, Pre-peak 6F', laid out like the two above it. X-axis is state; y-axis is percent reduction, 0 to above 80. Six series are no pre-peak and pre-peak durations from 15 minutes to 4 hours. Reductions are about 63% to 82% in the leading states and about 25% to 45% in the last ones, the 4-hour pre-peak line highest throughout.

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/93846.yaml
     source: 93846_images/image_000011_65450befe3cba9bb93cad8f3ddf5b0e2f95da7953fad5c8ca7565170ba960923.png
     method: vision-description
     described: 2026-11-11 -->

![Two line charts of percent cooling reduction by state over the whole year, 2°F and 4°F offsets](93846_images/image_000011_65450befe3cba9bb93cad8f3ddf5b0e2f95da7953fad5c8ca7565170ba960923.png)

Figure 9, first bitmap: two line charts, 'Offset: 2F' above 'Offset: 4F', for the whole year. X-axis is state, ordered from largest to smallest reduction; y-axis is percent reduction. Six series are no pre-peak and pre-peak durations from 15 minutes to 4 hours. Reductions run from about 37% to 51% in the leading state down to about 13% to 15% at 2°F, and from about 65% to 83% down to about 25% at 4°F.

Figure 9. D3 percentage reduction of cooling energy consumption during the peak period for the whole year and at various pre-peak durations (including no pre-peak). The top figure shows a 2°F offset for both the pre-peak and peak periods, the middle shows a 4°F offset for both, and the bottom shows a 4°F offset for the peak period and a 6°F offset for the pre-peak period. Note that the ordering of the states varies.

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/93846.yaml
     source: 93846_images/image_000012_129951035cfe5ecb59cd46b0a110748ac65b4708fa12fddfb92ed44233e3173b.png
     method: vision-description
     described: 2026-11-11 -->

![Line chart of percent cooling reduction by state over the whole year, 4°F peak offset with 6°F pre-peak offset](93846_images/image_000012_129951035cfe5ecb59cd46b0a110748ac65b4708fa12fddfb92ed44233e3173b.png)

Figure 9, second bitmap: line chart titled 'Offset: Peak 4F, Pre-peak 6F', for the whole year. X-axis is state; y-axis is percent reduction, about 20 to 90. Six series are no pre-peak and pre-peak durations from 15 minutes to 4 hours. Reductions are about 65% to 88% in the leading state and about 23% to 27% in the last, with the lines crossing in a few low-reduction states.

Figure 10 shows an example of a heating day misclassified as a cooling day for a single model. The day was misclassified as a heating day, and preheating was performed from 14:00 to 18:00, resulting in a large reduction in cooling load later in the day because the preheating increased both the heating and the cooling set points 2 ; however, once the peak period begins at 18:00, the increased cooling set point is reset to normal, resulting in increased cooling energy consumption. Essentially, we tried to preheat when precooling would have been appropriate, resulting in increased load during the peak. The solution was to avoid preheating or precooling when the average daily outdoor temperature is near the threshold (66°F) because it is hard to predict whether precooling or preheating would be the more appropriate action. In the final run, we implemented this correction.

Figure 10. Anomalous demand response in a shoulder season day in Idaho

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/93846.yaml
     source: 93846_images/image_000013_23d53b26aa5e4186935f6d6eac63b188087cda48003e428010de7152ad96512d.png
     method: vision-description
     described: 2026-11-11 -->

![Line chart of average cooling energy and outdoor temperature on a shoulder-season day in Idaho, with peak bands](93846_images/image_000013_23d53b26aa5e4186935f6d6eac63b188087cda48003e428010de7152ad96512d.png)

Figure 10: line chart from 09:00 on May 25 to 00:00 on May 26, 2020. Left axis is average cooling in kWh, 0 to about 0.45; right axis is temperature in °C for the outdoor temperature line. Shaded bands mark the pre-peak and peak periods, and the legend lists the baseline and the offset scenarios. Cooling is near zero until mid-afternoon, then spikes to roughly 0.25 to 0.3 kWh at the starts of the shaded periods.

To help decide the appropriate switchover temperatures, we looked at the distribution of the average heating and cooling loads during the peak period across various daily average temperatures, as shown in Figure 11 and Figure 12.

2 Preheating does not require raising the cooling set point by default -it only requires raising the heating set point; however, to prevent an inverted set point (where the cooling set point is lower than the heating set point), the algorithm raises the cooling set point as well when the heating set point exceeds the cooling set point.

Figure 11. State average hourly cooling load per building during the peak period

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/93846.yaml
     source: 93846_images/image_000014_be750ad86d30b61c6abb090759d400be4aeb849dbc0794f50ea6eaa0fa2d29c9.png
     method: vision-description
     described: 2026-11-11 -->

![Scatter plot of state average hourly cooling load during the peak period against daily average temperature](93846_images/image_000014_be750ad86d30b61c6abb090759d400be4aeb849dbc0794f50ea6eaa0fa2d29c9.png)

Figure 11: scatter plot, points coloured by state. X-axis is daily average temperature in °C, 0 to about 37; y-axis is cooling in kWh, 0 to 1.2. Cooling load is near zero below about 10°C and rises with temperature, reaching about 0.6 to 1.2 kWh at 30°C and above, with a wide spread between states at any one temperature.

Figure 12. State average hourly heating load per building during the peak period

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/93846.yaml
     source: 93846_images/image_000015_ef0017f010af5299bca91b9cb7119768ae4d1ffbb283ad5bb3fc89d27212a2fd.png
     method: vision-description
     described: 2026-11-11 -->

![Scatter plot of state average hourly heating load during the peak period against daily average temperature](93846_images/image_000015_ef0017f010af5299bca91b9cb7119768ae4d1ffbb283ad5bb3fc89d27212a2fd.png)

Figure 12: scatter plot, points coloured by state. X-axis is daily average temperature in °C, -30 to 40; y-axis is average heating in kWh, 0 to 25. Heating load falls as temperature rises: the highest points, about 20 to 24 kWh, are at about -20°C, most points at 0°C are below about 12 kWh, and the load is near zero above about 20°C.

The average load at a given average daily temperature for a given state varies among different days (different dots in the figure), depending on the specific temperature profile for the day and the internal heat generated in the building via various occupancy-driven end uses. Figure 11 shows minimal cooling below an average daily temperature of 10°C (50°F), and Figure 12 shows minimal heating above an average daily temperature of 25°C (68°F). Based on these results, in the final implementation, we precooled only if the daily average temperature is above 68°F, and we preheated only if the daily average temperature is below 50°F. We did not need to follow these thresholds for load shedding -decreasing the heating set point and increasing the cooling set point during the peak period will reduce the demand regardless of the building having a cooling or a heating load.

