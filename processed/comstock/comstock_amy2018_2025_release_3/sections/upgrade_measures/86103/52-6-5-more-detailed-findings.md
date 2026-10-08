<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86103.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/86103.md | section: 6.5  More Detailed Findings | lines: 954-1046 -->
## 6.5  More Detailed Findings

Figure 9 and Figure 10 in Section 4.2.1 highlight design condition COPcomp&amp;fan,design (definitions of different COPs included in Section 4.2.1) for certain VRF products. Because we use a normalized EIR modifier that gets applied to the rated COP of each outdoor unit, the actual design condition COPcomp&amp;fan,design also varies slightly with varying rated COPs depending on the size of the outdoor unit (shown in Figure 12). Figure 19 shows COPcomp&amp;fan,design in different outdoor air conditions (i.e., everything else is held at design conditions other than the outdoor air temperature) as well as in rated conditions applied to the models applicable for the upgrade. This figure is to provide a quick reference on what design condition VRF COPcomp&amp;fan,design range we are modeling compared to manufacturers' performance maps on both heating and cooling.

Figure 19. Distribution of VRF rated and design COPcomp&amp;fan,design

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000026_e60a0a0ad5e05d6b9476c9d79ce91c4d67f8ace082cfd75d47a65788689bba5b.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 19: box plots of VRF rated and design COP across heating and cooling conditions](86103_images/image_000026_e60a0a0ad5e05d6b9476c9d79ce91c4d67f8ace082cfd75d47a65788689bba5b.png)

Figure 19: horizontal box-and-whisker distributions of design COPcomp&fan,design (axis 1 to 12) across nine conditions - design heating COP at 0, 20 and 40 deg F plus rated heating COP, and design cooling COP at 35, 60, 85 and 110 deg F plus rated cooling COP. Cooling at 35 deg F centers near 8 while heating at 0 deg F falls below 2. See Section 6.5.

Figure 20 shows the distribution of annual operating and average COPcomp&amp;fan,operating only for buildings that received the VRF DOAS upgrade. Unlike from 'design' condition COPs shown in Figure 19, COPs shown in this figure reflect various operating conditions (e.g., change in indoor/outdoor temperatures) as well as piping losses through refrigerant lines. And again, COPcomp&amp;fan,operating only accounts for power used by the compressor and outdoor unit fan. While median cooling COPcomp&amp;fan.operating varies between 4 and 6 between hot and cold regions, median heating operating COPcomp&amp;fan,operating varies between 2.5 and 4.5. Heating COPcomp&amp;fan,operating datapoints shown in the figure also reflect the impact of waste heat recovery of the VRF system where the heat extracted from zones in cooling mode is transferred to zones in heating mode (i.e., principle of simulataneous heating and cooling), thus, heating COPs shown in the figure can go beyond the claimed heating COPcomp&amp;fan,design shown in Figure 9.

Figure 20. Distribution of VRF annual average COPcomp&amp;fan,operating

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000027_864688995575e5b22e0749efa760b249166473b131123f5c95c57bc812633767.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 20: box plots of annual average cooling and heating operating COP by climate zone](86103_images/image_000027_864688995575e5b22e0749efa760b249166473b131123f5c95c57bc812633767.png)

Figure 20: two panels of box plots by climate zone (Subarctic through Hot-Humid) for annual average cooling COPcomp&fan,operating with a SEER scale on the top axis, and annual average heating COPcomp&fan,operating with an HSPF scale. Cooling medians run roughly 4 to 6.5 and fall in hotter zones; heating medians are highest in Marine and lowest in the coldest zones. See Section 6.5.

Figure 21 shows the distribution of supplemental heating fraction against VRF heating only for buildings that received the VRF DOAS upgrade. As shown in the figure, the median fraction of supplemental heating is between 0.03 (3%) and 0.06 (6%) in colder regions (climate zone of subarctic, very cold, and cold), while the maximum fraction goes up to 0.25 (25%). Because (1) the sizing of the VRF system (and DOAS) can be geared differently between hotter and colder regions and (2) the sizing applied in this modeling work applied the same sizing method for all climatic regions, the results shown in this figure might overestimate the prevelance of supplemental heating in extremely cold climates. To provide additional support with further data, a field study reported the VRF system applied in climate region of 5 and 6 maintained proper indoor conditions without a supplemental backup heating system [13].

Figure 21. Distribution of fraction of VRF supplemental heating with electric resistance heating

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000028_21f79ebe5d0b82c9484e24469fa757683ea354d313e1f492d03f2835b9973a2c.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 21: box plots of supplemental electric resistance heating fraction by climate zone](86103_images/image_000028_21f79ebe5d0b82c9484e24469fa757683ea354d313e1f492d03f2835b9973a2c.png)

Figure 21: box plots by climate zone of the fraction of supplemental electric resistance heating relative to VRF heat pump heating (axis 0 to 0.24), for buildings that received the upgrade. Medians run about 0.03-0.06 in the colder zones and sit near zero in mild ones, with scattered outliers out to 0.24. See Section 6.5.

Figure 22 shows distributions of COPsystem,operating as well as the difference between two COP metrics (COPcomp&amp;fan,operating and COPsystem,operating) for buildings that received the VRF DOAS upgrade. The difference between the two COP metrics mostly comes from accounting COPsystem,operating and not accounting COPcomp&amp;fan,operating supplemental heating. As can be expected with an increased fraction of supplemental heating shown in Figure 22 in colder climates, the relative difference between two metrics is also higher in colder climates.

Figure 22. Distribution of annual average heating COPsystem,operating

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000029_010016b80e20abefc7f74be5b07ba981c43633279e10d7e7b740a9b332834f5d.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 22: box plots of heating system COP and its difference from compressor-and-fan COP](86103_images/image_000029_010016b80e20abefc7f74be5b07ba981c43633279e10d7e7b740a9b332834f5d.png)

Figure 22: two panels of box plots by climate zone - annual average heating COPsystem,operating (axis 1 to 5) and the relative difference from COPcomp&fan,operating to COPsystem,operating (%, axis -10 to 60). System COP medians run about 2 to 3, and the two metrics differ by roughly 20% to 30%, reflecting indoor fan and supplemental heating energy. See Section 6.5.

It is also necessary to provide context around the indoor conditions (i.e., if room conditions were maintained properly) to properly justify the energy savings. Figure 23 shows the distribution of total hours in a year where space temperature did not meet the setpoint. The increased unmet hours for heating with VRF DOAS upgrade is due to the limitations described in Section 4.4.

Figure 23. Distribution of unmet hours to heating and cooling setpoints

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000030_161a4477986be2f3470cdc9dace128d1d998e92f4e1bc90307d1ff73685ad387.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 23: box plots of annual unmet heating and cooling setpoint hours](86103_images/image_000030_161a4477986be2f3470cdc9dace128d1d998e92f4e1bc90307d1ff73685ad387.png)

Figure 23: box plots of total unmet setpoint hours per year (axis 0 to 250), grouped into cooling and heating setpoint unmet hours and split by scenario (Baseline, VRF with DOAS) and the raw applicability.hvac_vrf_hr_doas flag (True/False). Applicable models under the upgrade show the widest spread in heating unmet hours. See Section 6.5.

Figure 24 shows the distribution and variations of piping configurations (averaged per building) for buildings that received the VRF DOAS upgrade. Maximum vertical piping height is the farthest vertical distance between the outdoor unit and corresponding indoor unit, and negative value represents when the outdoor unit is located in a higher position (i.e., roof) compared to the indoor unit. To note, all the VRF systems' outdoor units are located on the roof in our analysis as shown in Figure 24. Maximum equivalent piping length is the farthest piping distance between the outdoor unit and the indoor unit. The maximum piping length and height can be limitations on VRF system implementation, where maximum equivalent piping length can have a limit of 500 feet (152 meters) and maximum vertial piping height can have a limit of 130 feet (40 meters) to 160 feet (49 meters) [13]. While our modeling has applicability criteria regarding building size and total number of indoor units (described in Section 4.1) for determining if the upgrade is eligible and feasible, the piping length and height limits are not applied in the applicability criteria resulting in buildings with piping lengths and heights above those limits as shown in Figure 24. However, most of the building stock within the interquartile range shown in Figure 24 falls within the limits.

Figure 24. Distribution of VRF piping configurations

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000031_0a1811bd3a911f33d380982c73720ce3b8712bf58b5b471e02b4d4db44032684.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 24: box plots of maximum vertical piping height and equivalent length by story count](86103_images/image_000031_0a1811bd3a911f33d380982c73720ce3b8712bf58b5b471e02b4d4db44032684.png)

Figure 24: two panels of box plots by building story count (1 through 14, 15_25, over_25) - maximum vertical piping height (m, plotted negative to -60) and maximum equivalent piping length (m, 0 to 400), averaged per building. Vertical height grows with story count while equivalent length is widest for low-rise buildings. See Section 6.5.

Figure 25 shows the count of indoor and outdoor units (per building) only for buildings that received the VRF DOAS upgrade. The counts of indoor and outdoor units as well as capacities of these units could be used to estimate a rough investment cost. Indoor unit counts shown in the figure represent the total counts in the buildings, meaning indoor unit counts per outdoor unit can be gleaned from both indoor and outdoor unit counts.

Figure 25. Distribution of VRF indoor and outdoor unit counts

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000032_31e556f29efa848d176e47b129bd4e865ee3025dcdf0c6af770af103065f50a1.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 25: box plots of indoor and outdoor unit counts per building by story count](86103_images/image_000032_31e556f29efa848d176e47b129bd4e865ee3025dcdf0c6af770af103065f50a1.png)

Figure 25: two panels of box plots by building story count of total indoor units per building (axis 0 to 250) and total outdoor units per building (axis 0 to 30), for buildings that received the upgrade. Both counts rise with story count - low-rise models cluster below about 25 indoor units while models of seven or more stories spread past 100. See Section 6.5.

