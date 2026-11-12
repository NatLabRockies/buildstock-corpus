<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96826.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96826.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96826.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: upgrade_measures/measure_pdfs/96826.md | section: 4.1.1 Individual Dwelling Annual Results | lines: 568-615 -->
## 4.1.1 Individual Dwelling Annual Results

Table 8 presents selected metrics before and after the HPWH upgrade and percent change. As expected, total delivered hot water is largest in colder climate because the ground water is colder, more energy is needed to deliver the same amount of hot water. The amount of delivered hot water remains nearly the same before and after the HPWH upgrade, indicating that the upgrade does not lead to an increase in unmet water heating demand.

The upgrade led to a significant reduction in water heating energy use across all locations. Water heater site energy consumption was reduced by 80%, 77%, and 43% for the dwelling in HI, CA, and AK, respectively. These reductions are as expected for HI and CA, given the improvement in efficiency from an EF of 0.92 (~0.92 UEF) for the electric storage water heater to a UEF of 3.98 for the HPWH. In unconditioned space installations, such as in garages, the efficiency of the heat pump and amount of backup usage varies substantially depending on the ambient air temperature available to the HPWH. The average garage temperature is lower in CA (71 ° F) than in HI (82 ° F), leading a lower overall HPWH coefficient of performance (COP, 3.93 for CA and 4.62 for HI) and less energy savings. For AK, where the garage temperature can reach below freezing 2 , the use of electric resistance backup for the HPWH is much more common (27% of the total heating time) and reduced both the COP and the energy savings from the upgrade. Electric resistance backup use is zero or nearly zero for the other locations.

It is worth noting that ResStock may be slightly underestimating the use of HPWH backup and therefore overestimating the energy savings potential from HPWH. This is because the current simulation timestep at 15 minutes is longer than many hot water usage events. As a result, the flow rate of individual hot water draw events may be averaged over the timestep, which reduces the rate at which energy is removed from the tank and may show that the heat pump is able to recover from events that might have triggered the backup elements, which reheat more rapidly than the heat pump, for part of the recovery period. Additionally, the EnergyPlus Energy Management System controller is allowing the HPWH to run slightly hotter than the electric storage water heater. This allows the HPWH to store more hot water, reducing the use of the backup.

Table 8. Selected Metrics Before and After the HPWH Upgrade

<!-- table recovered from measure_pdfs/96826.pdf p.22
     overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/96826.yaml
     method: vision-transcription
     supersedes the extractor's own table here (values e688359718de…):
       The extractor dropped the first column: the four metric labels (Delivered Hot Water (MBtu), Hot Water Energy (MBtu), Annual Average COP, Total Site Energy (MBtu)) are absent, leaving four unlabelled groups of Baseline/Upgrade/Change rows, so no value says what it measures. Every value is right. Labels are restored from the page and repeated on each row; the values are the extractor's own, compared with page 22. -->

The three value columns are Dwelling ID/State/Climate Zone.

| Metric | Case | 1/HI/1A | 2/CA/3B | 3/AK/7 |
|---|---|---|---|---|
| Delivered Hot Water (MBtu) | Baseline | 7.11 | 11.12 | 17.13 |
| Delivered Hot Water (MBtu) | Upgrade | 7.13 | 11.18 | 17.16 |
| Delivered Hot Water (MBtu) | Change | 0.3% | 0.5% | 0.2% |
| Hot Water Energy (MBtu) | Baseline | 7.91 | 12.10 | 18.55 |
| Hot Water Energy (MBtu) | Upgrade | 1.54 | 2.84 | 10.52 |
| Hot Water Energy (MBtu) | Change | -80% | -77% | -43% |
| Annual Average COP | Baseline | 0.90 | 0.92 | 0.92 |
| Annual Average COP | Upgrade | 4.62 | 3.93 | 1.63 |
| Annual Average COP | Change | 414% | 328% | 77% |
| Total Site Energy (MBtu) | Baseline | 35.02 | 90.12 | 111.74 |
| Total Site Energy (MBtu) | Upgrade | 28.58 | 81.04 | 105.01 |
| Total Site Energy (MBtu) | Change | -18% | -10% | -6% |

2 Water heater location data came from EIA's RECS 2020 and shows some garage installations of water heaters for AK. While not modeled, mitigation, such as heat trace and insulation, can help prevent pipe freezes for installations outside of the living space in cold climates where mitigation is required.

Figure 4 presents the breakdown of modeled annual site energy consumption of the sample dwellings before and after the HPWH upgrade. The HPWH upgrade has minor impacts on other end uses because the water heater is in the garage where its impact on HVAC is limited. Because HPWHs operate by extracting heat from the surrounding air and transferring it to the water in the tank, they cool the air around them. As a result, the temperature in the garage decreases compared to the baseline for all three example dwelling units. Since the garage is attached to the thermal envelope, it slightly increases space heating and reduces space cooling demand needed to maintain setpoints. In AK, the average garage temperature is reduced by over 5°F from 52°F, leading to an increase in space heating energy by 2%. In CA, the garage temperature decrease is 3°F, causing a 2% increase in space heating and a 1% decrease in space cooling. For HPWHs installed in the conditioned space, the interaction between HVAC and water heating is more direct and causes slightly larger changes in space heating and cooling demands.

Figure 4. Modeled annual site energy consumption before and after the HPWH upgrade

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/96826.yaml
     source: 96826_images/image_000005_919376e3baaea1050e90ac3b6a415fd36fb0ba51affe87bf3405f151ec8234ab.png
     method: vision-description
     described: 2026-11-11 -->

![Stacked bars of annual energy use for three example dwellings (HI, CA, AK), baseline vs HPWH](96826_images/image_000005_919376e3baaea1050e90ac3b6a415fd36fb0ba51affe87bf3405f151ec8234ab.png)

Figure 4: three-panel horizontal stacked bar chart for the example dwellings in HI, CA and AK. X-axis is annual energy consumption in MBtu; each panel has a baseline bar (50-gal electric resistance) and an upgrade bar (80-gal HPWH), stacked by end use. The water heater segment falls from 7.9 to 1.5 MBtu in HI, 12.1 to 2.8 in CA and 18.5 to 10.5 in AK. See Table 8.

