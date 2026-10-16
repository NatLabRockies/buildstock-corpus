<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.pdf | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/3b69decb4e5f7bb3d6cc24f6224b318c921fd45f/assets/files/ComStock%20Measure%20Doc_Low%20Priority%20Device%20Switching%20During%20Peak%20Hours.pdf | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/ComStock%20Measure%20Doc_Low%20Priority%20Device%20Switching%20During%20Peak%20Hours.pdf | corpus_version: comstock_amy2018_2025_release_3-v2 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.md | section: 3.2. Technology Specifics | lines: 187-208 -->
## 3.2. Technology Specifics

The measure aims to evaluate the fraction of end use load that potentially can be reduced during the system-level peak period within the commercial building sector. The default system-level peak periods are identified for each state using the 2050 net load profile from 2023 Cambium dataset, Mid-case scenario [9]. Cambium dataset is the projection of hourly select supply- and demand-side metrics including gross demand, VRE generation, and operational costs for multiple demand futures. The peak period for this load shedding measure is defined as the four hours including the peak hour with the highest average electricity load during each season. The whole year is categorized into three seasons as summer season (June to September), winter season (December to March) and intermediate season (all other months). The identified fourhour peak periods for each state are illustrated in Figure 2. The detailed start and end time can be found in the appendix. Note that Cambium dataset does not include system load profiles for Alaska and Hawaii, and the buildings of these two states are not within the scope of the BSS DF project. However, to facilitate the ComStock simulation, Alaska and Hawaii are assigned with peak periods from the state with the similar climate zones.

Figure 2. Default 4-hour peak (load shedding) period of each season and each state for the measures

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/assets/files/ComStock Measure Doc_Low Priority Device Switching During Peak Hours.yaml
     source: ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000002_382887ed6903a5baa80f0789b84475869a21429c0169aee857df426f858c2244.png
     method: vision-description
     described: 2026-10-15 -->

![Figure 2: grid of 48 state panels marking the default 4-hour peak period by season and hour of day](ComStock_Measure_Doc_Low_Priority_Device_Switching_During_Peak_Hours_images/image_000002_382887ed6903a5baa80f0789b84475869a21429c0169aee857df426f858c2244.png)

Figure 2: small-multiples grid, one panel per state (48 panels), x-axis hour of day 0 to 24.
Colored bars mark the default 4-hour load-shedding window for winter (blue), summer (red) and
intermediate season (green). Most windows fall in the late afternoon and evening, roughly hours
16 to 21, with the season-to-season shift differing by state.

This measure will loop through all the interior electric equipment objects and clone their schedules for each season if the equipment belongs to an applicable space type (listed in the previous section). The state of the building is identified from the additionalProperties object and the measure will adjust the equipment schedule on each day during the corresponding peak period of the state and the season. During the peak period, the electric equipment loads are reduced by 20% for applicable spaces. The 20% occupied reduction threshold represents the low end of the range found by previous studies in offices [6], [7]. For times outside of the peak period, the existing schedules in the model stays unchanged. The reduction is applied daily, and the expected outcome of the simulation is the distribution of daily percentage reduction of the end use load by the measure. The detailed demand response event dispatch strategy will be considered outside the ComStock simulation by DR-Path.

It is worth noting that the measure offers the flexibility for users to specify the start and end date and time of multiple peak periods when the electric equipment schedule is adjusted, as well as the percentage of the equipment load reduction. If no user inputs are provided, the aforementioned default values will be used.

