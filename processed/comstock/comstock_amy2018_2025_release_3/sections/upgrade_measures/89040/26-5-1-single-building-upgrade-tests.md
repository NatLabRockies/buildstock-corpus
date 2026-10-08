<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89040.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89040.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89040.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/89040.md | section: 5.1  Single Building Upgrade Tests | lines: 423-489 -->
## 5.1  Single Building Upgrade Tests

Table 4 shows the sizing comparison of a sample model with and without upsizing allowance. A weather file that represents Helena, Montana (ASHRAE climate zone 6B), is applied to this sample model to highlight upsizing implementation under a relatively colder region. As shown in the table, this sample building model includes nine indoor units where each indoor unit contains three types of coil models: backup electric resistance coil, cooling coil, and heating coil. Based on the upsizing algorithm shown in Figure 5, the upsizing is applied to eight indoor units where seven out of those eight units received the full 25% upsizing while one of them received 17% upsizing. The reason for the 17% upsizing instead of the full 25% is because 17% upsizing matches 100% with the design heating load (6,595 W), so additional capacity is not necessary. The only indoor unit (i.e., indoor unit 4 in Table 4) that did not receive the upsizing is because the indoor unit's design cooling load (14,787 W) is larger than the design heating load (10,261 W), meaning it is not a heating-dominant zone and upsizing for heating is not necessary. The original sizing based on the design cooling load violated the maximum allowable 450 cfm/ton; thus, the design capacities before the upsizing do not match with the reference design load. While the upsizing allowance was set to 25% initially, the actual upsizing resulted in an average 21.3% increase across all indoor units, as well as for the corresponding outdoor unit. As shown in the table, the size of the backup electric resistance coil matches the design heating load.

Table 4. Single Building Model Results: Sizing Results Before and After Upsizing Allowance

<!-- table recovered from measure_pdfs/89040.pdf p.25
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89040.yaml
     method: vision-transcription -->

**Indoor units 1-3**

| Coil Type | Reference Design Load [W] | Before upsizing: Final Rated Capacity [W] | Before upsizing: Design Capacity [W] | Before upsizing: Design Heating Load Coverage [%] | Before upsizing: CFM/ton bound violated? | After upsizing: Final Rated Capacity [W] | After upsizing: Capacity Change from Original Sizing [%] | After upsizing: Design Capacity [W] | After upsizing: Design Heating Load Coverage [%] | After upsizing: CFM/ton bound violated? |
|---|---|---|---|---|---|---|---|---|---|---|
| Indoor unit 1 VRF cooling coil | 4,599 | 6,349 | 5,251 | 80% | Max | 7,918 | 25% | 6,595 | 100% | No |
| Indoor unit 1 VRF heating coil | 6,595 | 6,349 |  |  |  | 7,918 |  |  |  |  |
| Indoor unit 1 backup electric resistance coil | 6,595 | 6,595 |  |  |  | 6,595 |  |  |  |  |
| Indoor unit 2 VRF cooling coil | 1,464 | 2,291 | 1,900 | 68% | Max | 2,863 | 25% | 2,393 | 85% | No |
| Indoor unit 2 VRF heating coil | 2,808 | 2,291 |  |  |  | 2,863 |  |  |  |  |
| Indoor unit 2 backup electric resistance coil | 2,808 | 2,808 |  |  |  | 2,808 |  |  |  |  |
| Indoor unit 3 VRF cooling coil | 1,301 | 2,285 | 1,892 | 68% | Max | 2,856 | 25% | 2,383 | 85% | No |
| Indoor unit 3 VRF heating coil | 2,801 | 2,285 |  |  |  | 2,856 |  |  |  |  |
| Indoor unit 3 backup electric resistance coil | 2,801 | 2,801 |  |  |  | 2,801 |  |  |  |  |

**Indoor units 4-6**

| Coil Type | Reference Design Load [W] | Before upsizing: Final Rated Capacity [W] | Before upsizing: Design Capacity [W] | Before upsizing: Design Heating Load Coverage [%] | Before upsizing: CFM/ton bound violated? | After upsizing: Final Rated Capacity [W] | After upsizing: Capacity Change from Original Sizing [%] | After upsizing: Design Capacity [W] | After upsizing: Design Heating Load Coverage [%] | After upsizing: CFM/ton bound violated? |
|---|---|---|---|---|---|---|---|---|---|---|
| Indoor unit 4 VRF cooling coil | 14,787 | 20,418 | 16,886 | 165% | Max | 20,418 | 0% | 16,886 | 165% | Max |
| Indoor unit 4 VRF heating coil | 10,261 | 20,418 |  |  |  | 20,418 |  |  |  |  |
| Indoor unit 4 backup electric resistance coil | 10,261 | 10,261 |  |  |  | 10,261 |  |  |  |  |
| Indoor unit 5 VRF cooling coil | 4,912 | 6,782 | 5,626 | 85% | Max | 7,910 | 17% | 6,595 | 100% | No |
| Indoor unit 5 VRF heating coil | 6,595 | 6,782 |  |  |  | 7,910 |  |  |  |  |
| Indoor unit 5 backup electric resistance coil | 6,595 | 6,595 |  |  |  | 6,595 |  |  |  |  |
| Indoor unit 6 VRF cooling coil | 4,320 | 5,964 | 4,932 | 75% | Max | 7,455 | 25% | 6,211 | 95% | No |
| Indoor unit 6 VRF heating coil | 6,567 | 5,964 |  |  |  | 7,455 |  |  |  |  |
| Indoor unit 6 backup electric resistance coil | 6,567 | 6,567 |  |  |  | 6,567 |  |  |  |  |

**Indoor units 7-9**

| Coil Type | Reference Design Load [W] | Before upsizing: Final Rated Capacity [W] | Before upsizing: Design Capacity [W] | Before upsizing: Design Heating Load Coverage [%] | Before upsizing: CFM/ton bound violated? | After upsizing: Final Rated Capacity [W] | After upsizing: Capacity Change from Original Sizing [%] | After upsizing: Design Capacity [W] | After upsizing: Design Heating Load Coverage [%] | After upsizing: CFM/ton bound violated? |
|---|---|---|---|---|---|---|---|---|---|---|
| Indoor unit 7 VRF cooling coil | 4,552 | 6,285 | 5,221 | 80% | Max | 7,848 | 25% | 6,567 | 100% | No |
| Indoor unit 7 VRF heating coil | 6,567 | 6,285 |  |  |  | 7,848 |  |  |  |  |
| Indoor unit 7 backup electric resistance coil | 6,567 | 6,567 |  |  |  | 6,567 |  |  |  |  |
| Indoor unit 8 VRF cooling coil | 1,459 | 2,285 | 1,908 | 68% | Max | 2,856 | 25% | 2,402 | 86% | No |
| Indoor unit 8 VRF heating coil | 2,801 | 2,285 |  |  |  | 2,856 |  |  |  |  |
| Indoor unit 8 backup electric resistance coil | 2,801 | 2,801 |  |  |  | 2,801 |  |  |  |  |
| Indoor unit 9 VRF cooling coil | 1,293 | 2,278 | 1,902 | 68% | Max | 2,848 | 25% | 2,395 | 86% | No |
| Indoor unit 9 VRF heating coil | 2,793 | 2,278 |  |  |  | 2,848 |  |  |  |  |
| Indoor unit 9 backup electric resistance coil | 2,793 | 2,793 |  |  |  | 2,793 |  |  |  |  |

Figure 6 shows time-series results (covering 1 week) highlighting the difference with and without upsizing allowance for a sample model. The weather applied to this model represents the subarctic region, and the figure shows the outdoor air temperature reaching down to -20°F for this simulated week. Because the minimum operating temperature for VRF heating is set as -22°F, heat pump heating is kept operated during this simulation period. Because of the upsized coils, a heat pump provides a higher heating rate to the building, as shown in the second graph in Figure 6. Because of this additional heating power with an upsized unit, the backup heating rate (with an electric resistance coil) decreases, as shown in the third graph in Figure 6.

Figure 6. Single building model results: time-series sample results before and after upsizing allowance

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89040.yaml
     source: 89040_images/image_000013_0ac4d2bb05fa92696a1fe167977f77e0d89a2b131114b46379372ea23a72bcda.png
     method: vision-description
     described: 2026-08-21 -->

![Three stacked time-series panels of zone temperature and VRF heat pump and backup heating rates](89040_images/image_000013_0ac4d2bb05fa92696a1fe167977f77e0d89a2b131114b46379372ea23a72bcda.png)

Figure 6: three stacked time-series panels over one week (hour 0 to 168) for a single building model - average zone temperature in degrees F plotted with outdoor air temperature, VRF heat pump heating rate to 120,000 Btu/hr, and VRF backup heating rate to 100,000 Btu/hr - each comparing before and after upsizing. After upsizing the heat pump peaks higher and the backup spikes shrink sharply. Section 5.1 discusses the test.

Table 5 shows the annual summary results of the same sample simulations shown in Figure 6. While the upsized VRF unit provides benefits by leveraging a more efficient heating mechanism (i.e., heat pump heating) compared to electric resistance heating, there are downsides as well. Based on the product research conducted in the previous analysis, the rated COP of a VRF heat pump unit typically decreases with larger capacity. Thus, in our modeling, the upsized unit is assigned with slightly lower-rated COPs (compared to the unit without upsizing) for both heating and cooling, which will also result in lower operating COPs, as shown in Table 5. We also described about this limitation and what can be done in real designing in Section 3.4. The overall impact of the upsizing allowance implementation can be a combined result of benefits and drawback as summarized below:

