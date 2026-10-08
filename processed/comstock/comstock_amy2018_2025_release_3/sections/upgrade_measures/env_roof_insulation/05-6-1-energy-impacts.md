<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_roof_insulation.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_roof_insulation.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_roof_insulation.html | corpus_version: b5faf42 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_roof_insulation.md | section: 6.1.  Energy Impacts | lines: 312-364 -->
## 6.1.  Energy Impacts

The roof insulation measure demonstrates 3% (112 TBtu) aggregate site energy savings, combined for all fuel types, across the modeled U.S. commercial building stock. The savings are primarily attributed to:

-   11% (50 TBtu) natural gas heating site energy savings
-   12% (28 TBtu) electricity heating site energy savings
-   3% (21 TBtu) electricity cooling site energy savings
-   1% (5 TBtu) electricity fan site energy savings.

The heating savings are due to higher roof R-values decreasing the heating load on the building. Gas and electricity heating show similar percent site energy savings, but the natural gas heating savings are approximately double the electricity savings due to the relatively higher prevalence of natural gas heating energy in the U.S. commercial building stock. Note, however, that site energy savings between electricity and natural gas may not correspond proportionally to energy cost savings, or source energy savings. Electricity savings are also realized due to decreased envelope cooling loads. However, the savings are relatively less for cooling than for heating. This is due in part to much of a building’s cooling load occurring from heat generated within the building, which increased roof insulation would not necessarily help. Furthermore, the temperature difference between the indoor thermostat setpoint and the most extreme outdoor temperatures will often be much higher for heating than for cooling, which may also increase the effectiveness of insulation measure for heating versus cooling. Fans also show some electricity savings, which is primarily attributed to overall decreased heating and cooling loads, which can reduce the amount of time HVAC fans need to cycle on to maintain zone thermostat setpoints (for HVAC systems that include cycling fan operation).

![](media/295d1c520e99cde1143fc6ce7c188410.jpeg)

Figure 5. Comparison of annual site energy consumption between the ComStock baseline and the roof insulation (AEDG Roof) measure. Energy consumption is categorized both by fuel type and end use.

Figure 6 compares the percentage of total ComStock floor area served, the total site energy savings, and the percent savings of the average building for each code year of last roof replacement. Results show a strong correlation between percentage of ComStock floor area served and annual stock site energy savings, as expected. The average percent site energy savings represents the average savings of all ComStock models for the particular code year of last roof replacement. Generally, older code years show higher average percent energy savings compared to newer code years, since older code years have lower R-value requirements. However, there is some variation in this trend in part due to variation in climate zone prevalence for each code year described previously (Figure 4), but also variation in building type prevalence for a given code year. Figure 7 shows the average percent savings of ComStock models for each ComStock building type, with some building types showing up to three times the percent site energy savings compared to others. Multiple factors in ComStock play into these building type differences, including typical equipment intensities, ventilation loads, thermostat setpoints, hours of operation, etc. The ComStock methods for these features are describe in detail in the ComStock documentation report [2].

![Chart, bar chart Description automatically generated](media/6b2f9bfd93c7658eb59081665e4ed554.png)

Figure 6. Comparison of percentage of stock floor area, total site energy savings, and average percent site energy savings by code year followed during last roof replacement

Table 9 shows a summary of the roof insulation measure applied to the ComStock baseline. The first two columns of the table show that the applied roof R-value for the roof insulation measure matches the target AEDG values. The applied values are slightly higher than the AEDG values due to other roof construction layers increasing the R-value by a small amount. The table also summarizes, by climate zone, the average baseline R-value the roof insulation measure is applied to, the corresponding average R-value added, and the average percent site energy savings of ComStock models. The site energy savings is lowest for the warmest climate zone, which aligns with previous discussions regarding the heating end use showing the largest savings. Climate zones 4 through 7 show the highest percent site energy savings of around 4%–5%. Climate zone 8 shows lower percent savings than the middle climate zones. This may seem unexpected, but Table 9 shows climate zone 8 as having higher baseline roof insulation values on average, so the additional insulation added is less than the other climate zones even when considering the higher AEDG target values.

![Chart, bar chart Description automatically generated](media/6b89117267c804a18b16de1a39bebb3b.png)

Figure 7. Average site percent energy savings by ComStock building type

Table 9. Summary of Roof Insulation Measure for Comstock Baseline

<!-- table recovered from media/8d9229694413bdc8f5321a544038f684.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_roof_insulation.yaml
     method: vision-transcription -->

| Climate Zone | Applied Roof R-value | Target Roof R-value | Average Baseline Roof R-value | Average R-value Added | Average % Site Energy Savings |
|---|---|---|---|---|---|
| 1A | 21.8 | 21.0 | 10.9 | 10.9 | 1% |
| 2A | 26.8 | 26.0 | 12.0 | 14.8 | 2% |
| 2B | 26.8 | 26.0 | 14.6 | 12.2 | 2% |
| 3A | 26.8 | 26.0 | 11.6 | 15.2 | 4% |
| 3B | 26.8 | 26.0 | 15.7 | 11.1 | 2% |
| 3C | 26.8 | 26.0 | 16.0 | 10.8 | 2% |
| 4A | 33.8 | 33.0 | 13.0 | 20.8 | 4% |
| 4B | 33.8 | 33.0 | 13.7 | 20.1 | 4% |
| 4C | 33.8 | 33.0 | 12.8 | 21.0 | 4% |
| 5A | 33.8 | 33.0 | 15.0 | 18.8 | 5% |
| 5B | 33.8 | 33.0 | 15.0 | 18.8 | 5% |
| 6A | 33.8 | 33.0 | 18.3 | 15.5 | 4% |
| 6B | 33.8 | 33.0 | 18.1 | 15.7 | 4% |
| 7 | 37.8 | 37.0 | 20.8 | 17.0 | 4% |
| 7A | 37.8 | 37.0 | 19.9 | 17.9 | 4% |
| 7B | 37.8 | 37.0 | 19.6 | 18.2 | 3% |
| 8 | 37.8 | 37.0 | 24.0 | 13.8 | 3% |

