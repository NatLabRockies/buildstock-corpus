<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/93846.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/93846.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/93846.md | section: 4.2.1 Quantifying Demand Flexibility Impacts | lines: 502-551 -->
## 4.2.1 Quantifying Demand Flexibility Impacts

Traditional energy efficiency measures are often evaluated based on how much energy or utility bills they save on an annual basis. Because the goal of demand flexibility is to modify the load profile for a small number of days per year, metrics that evaluate the ability to modify the load are more useful than annualized energy consumption impacts.

There are many ways that the peak load impact of demand flexibility can be quantified. For this analysis, we adopted the demand decrease percentage (D3) metric, as defined by (Jingjing Liu, 2022). This metric is defined as:

The D3 metric can be computed for a single building or a group of buildings in aggregate. It can also be computed for the whole building load or for individual end uses.

This metric was adopted because it quantifies the impact for a single demand response event (in our case, each day where demand response is dispatched), but it can easily and meaningfully be summarized over multiple events. For example, the mean or quartile values can be used to describe how the impact changes during a year, a season, or a month. This is particularly useful when the demand flexibility impacts are later used as the input to other models seeking to represent demand flexibility but that do not endogenously represent building physics. Examples of such models include Lawrence Berkeley National Laboratory's DR-Path (Brian Gerke, 2019) and the Brattle Group's Load Flex model (Ryan Hledik A. F., 2019).

Because the goal of this analysis is to feed results into downstream modeling efforts, we calculated the D3 metric for the aggregate load of groups of buildings of a common type located in a common geography.

Figure 8 shows how the D3 metric varies with different pre-peak durations for cooling load flexibility on the hottest day of the year for each state. We used an approximate 20% reduction for the 2°F offset and an approximate 40% reduction for the 4°F offset. Although only the peak offset without any precooling can provide a significant percentage reduction, pairing that with precooling can push the reduction even further -more so in some states than others. Also, the longer the duration of precooling, the higher the percentage reduction, with the highest reduction coming from 4-hour precooling.

Figure 9 shows the same metrics calculated year-round. That is, we calculated the average cooling energy consumption during the peak period for the whole year for both the baseline and the upgrade, and we calculated the difference as a percentage reduction. Some states have more percentage savings year-round than their hottest day, whereas others have less. Regardless, most show a positive correlation with the duration of the pre-peak period (at all offset levels) except for a handful of states that show a surprising negative correlation. We examined the results with the largest negative correlation -an identification with a 6°F pre-peak offset to investigate how a larger precooling duration (or having precooling at all) could result in a higher load during the peak.

The answer is in how the precooling and preheating was initially implemented. In the sensitivity analysis, we always chose to either precool or preheat, depending on the daily average temperature. If the daily average temperature was less than 66°F, we classified that as a heating day, otherwise we classified the day as a cooling day; however, this might not always work neatly. For some days in shoulder season with mostly low temperatures during the morning but a hot afternoon, we classified the day as a heating day even though the building needed more cooling than heating; therefore, we mistakenly preheated a building that needed precooling (or at least not preheating).

![Image](93846_images/image_000009_2495bdaaa88f1d942605d350662dd9d2731318e0bdc82ec792f3a82008fdbf3d.png)

Figure 8. D3 percentage reduction of cooling energy consumption during the peak period on an extreme day and at various pre-peak durations (including no pre-peak). The top figure shows a 2°F offset for both the pre-peak and peak periods, the middle shows a 4°F offset for both, and the bottom shows a 6°F offset for the pre-peak period and a 4°F offset for the peak period. Note that the ordering of states varies.

![Image](93846_images/image_000010_31a3b6f9472ee7882b0c081baafed934581c4572b394e472da91cc5a4f77dbc6.png)

![Image](93846_images/image_000011_65450befe3cba9bb93cad8f3ddf5b0e2f95da7953fad5c8ca7565170ba960923.png)

Figure 9. D3 percentage reduction of cooling energy consumption during the peak period for the whole year and at various pre-peak durations (including no pre-peak). The top figure shows a 2°F offset for both the pre-peak and peak periods, the middle shows a 4°F offset for both, and the bottom shows a 4°F offset for the peak period and a 6°F offset for the pre-peak period. Note that the ordering of the states varies.

![Image](93846_images/image_000012_129951035cfe5ecb59cd46b0a110748ac65b4708fa12fddfb92ed44233e3173b.png)

Figure 10 shows an example of a heating day misclassified as a cooling day for a single model. The day was misclassified as a heating day, and preheating was performed from 14:00 to 18:00, resulting in a large reduction in cooling load later in the day because the preheating increased both the heating and the cooling set points 2 ; however, once the peak period begins at 18:00, the increased cooling set point is reset to normal, resulting in increased cooling energy consumption. Essentially, we tried to preheat when precooling would have been appropriate, resulting in increased load during the peak. The solution was to avoid preheating or precooling when the average daily outdoor temperature is near the threshold (66°F) because it is hard to predict whether precooling or preheating would be the more appropriate action. In the final run, we implemented this correction.

Figure 10. Anomalous demand response in a shoulder season day in Idaho

![Image](93846_images/image_000013_23d53b26aa5e4186935f6d6eac63b188087cda48003e428010de7152ad96512d.png)

To help decide the appropriate switchover temperatures, we looked at the distribution of the average heating and cooling loads during the peak period across various daily average temperatures, as shown in Figure 11 and Figure 12.

2 Preheating does not require raising the cooling set point by default -it only requires raising the heating set point; however, to prevent an inverted set point (where the cooling set point is lower than the heating set point), the algorithm raises the cooling set point as well when the heating set point exceeds the cooling set point.

Figure 11. State average hourly cooling load per building during the peak period

![Image](93846_images/image_000014_be750ad86d30b61c6abb090759d400be4aeb849dbc0794f50ea6eaa0fa2d29c9.png)

Figure 12. State average hourly heating load per building during the peak period

![Image](93846_images/image_000015_ef0017f010af5299bca91b9cb7119768ae4d1ffbb283ad5bb3fc89d27212a2fd.png)

The average load at a given average daily temperature for a given state varies among different days (different dots in the figure), depending on the specific temperature profile for the day and the internal heat generated in the building via various occupancy-driven end uses. Figure 11 shows minimal cooling below an average daily temperature of 10°C (50°F), and Figure 12 shows minimal heating above an average daily temperature of 25°C (68°F). Based on these results, in the final implementation, we precooled only if the daily average temperature is above 68°F, and we preheated only if the daily average temperature is below 50°F. We did not need to follow these thresholds for load shedding -decreasing the heating set point and increasing the cooling set point during the peak period will reduce the demand regardless of the building having a cooling or a heating load.

