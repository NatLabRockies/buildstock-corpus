<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_ext_wall_insulation.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_ext_wall_insulation.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_ext_wall_insulation.html | corpus_version: fadc83e | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_ext_wall_insulation.md | section: 6.3  Energy Impacts | lines: 511-556 -->
## 6.3  Energy Impacts

Figure 4 shows the building floor area in each R-value bin by climate zone. The exterior wall insulation measure increased the R-value across the building stock, with the majority of the floor area in the R-14 bin.

![](./media/5843043d-6358-4949-99d4-51ad0c69a1f7.png)

Figure 4. Baseline and upgrade exterior wall insultation R-value by climate zone

This measure resulted in 2.52% total stock site energy savings, with the majority of savings occurring in the heating and cooling end uses (Figure 5).

![Bar chart Description automatically generated with low confidence](./media/a323ec32-696c-41da-ad91-3e0424fb61f3.jpeg)

Figure 5. Annual energy consumption by end use and fuel

As shown in Figure 5, the distribution of energy savings varies by end use. The primary expectation would be that this measure saves heating and cooling energy. This is confirmed in the figure, with the median savings around 20% for natural gas heating, 30% for electric heating, and 5% for electric cooling. Heating savings are expected to be larger than cooling savings because of the larger temperature difference between inside and outside during heating season. The secondary effects are expected to be decreased fan and pump electricity used to move the air and water for heating and cooling. Both electricity for fans and pumps shows around a 10% median savings. The slight changes in energy consumption for heat recovery, heat rejection, and refrigeration are minor third-order effects associated with the runtimes of the heating and cooling equipment.

One questionable area of the results is the small groups of outliers showing 80%--100% savings in natural gas and electricity for heating. Upon detailed investigation, these are due to a small number of buildings in very hot climates (e.g., Phoenix, AZ or Miami, FL) that start with very low annual heating energy consumption (typically less than 1 kBtu/ft<sup>2</sup>-yr). Adding insulation reduces this tiny amount even further, so the annual percent savings appear very large.

Another questionable area of the results is the even smaller groups of outliers showing negative 60%--80% savings (so, 60%--80% increases) in gas or electric heating, pump, and fan consumption. An investigation of these models shows that they are also models in hot climates with very low annual consumption (for example, 0.5 kBtu/ft<sup>2</sup>-yr). Small changes to the operation of the heating and cooling equipment result in small magnitude changes in the equipment operation, but because of the very low baseline consumption, the changes are large relative to the annual totals, thus the high negative savings percentages. Some of these changes appear to be due to changes in equipment sizes stemming from not hard-sizing the models before changing the loads. This will be corrected in an update.

![Chart Description automatically generated with medium confidence](./media/7b22853a-7409-4bed-a068-d28b4aa0f467.jpeg)

Figure 6. Distribution of savings by fuel and end use

As shown in Figure 6 and Figure 7, average gas and electricity heating energy use intensity (EUI) reductions increase in colder climates. This is expected, as colder climates have higher heating energy, therefore added insulation saves more energy. The very high average electric heating EUI reduction in climate zone 8 is due to a higher prevalence of electric resistance heating.

![Chart, bar chart Description automatically generated](./media/05e51f53-3b57-4336-b1b4-7ce3217ce24e.png)

Figure 7. Average natural gas heating EUI reduction by climate zone

![Chart, bar chart Description automatically generated](./media/edadacbd-5f62-42b0-b828-e0beafcb9b82.png)

Figure 8. Average electricity heating EUI reduction by climate zone

As shown in Figure 8, average electricity cooling EUI reductions are higher in warm climates than in colder climates. This is expected, as warmer climates have higher cooling energy consumption, therefore added insulation saves more energy.

![Chart, bar chart Description automatically generated](./media/fb9f2ca5-00e6-40e2-ba6d-aff4060585f9.png)

Figure 9. Average electricity cooling EUI reduction by climate zone

As shown in Figure 9, fan electricity EUI reduction is relatively constant across climate zones. This is because both heating and cooling energy are decreased by adding insulation, with the balance attributable to heating vs. cooling changing by climate.

![Chart, bar chart Description automatically generated](./media/a4b089c2-1c65-41c1-9eb5-8c00858334ac.png)

Figure 10. Average electricity fan EUI reduction by climate zone

