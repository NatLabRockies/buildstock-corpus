<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95003.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95003.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95003.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/95003.md | section: 5.2  Sensitivity Results With Reduced Stock Models | lines: 604-646 -->
## 5.2  Sensitivity Results With Reduced Stock Models

We conducted a sensitivity analysis by (1) varying the chilled water system upgrades and (2) applying these different upgrades to ComStock with reduced stock models (i.e., ~14,000 instead of ~150,000 models that reasonably represent variations of the commercial building stock). This section includes the results of this sensitivity analysis to provide partial snapshots of how these different upsizing allowances propagate to the stock of building models. Note that because the sensitivity analysis in this section uses far fewer models to represent the building stock than a full ComStock run, results should be used for understanding generalized and conceptual trends only. Results with the full ComStock run shown in Section 6.3 and after might show slightly different trends because of including the remaining ~140,000 models. More detailed analyses should always utilize the available scenarios in the full published ComStock datasets.

Figure 14 shows the aggregated site energy consumption across different chilled water system upgrade scenarios: baseline, chiller replacement only (shown as Chlr), chiller and pump replacement (shown as Chlr Pmp), chiller/pump replacement and chilled water temperature reset (shown as Chlr Pmp CHW), and chiller/pump replacement and chilled/condenser water temperature reset (shown as Chlr Pmp CHW CW). As expected, the chiller replacement had the greatest impact on site energy savings, while the other upgrade options-such as pump improvements and chilled water/condenser water setpoint controls-contributed to a lesser extent. Also, as mentioned earlier in Section 5.1, chilled water supply temperature reset strategy resulted in reheat energy savings (i.e., heating energy savings shown in Figure 14).

Figure 14. Sensitivity analysis: aggregated site energy consumption with applicable models only

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95003.yaml
     source: 95003_images/image_000016_8ae0c5b67f3e4b316caa4dc4c184699f9640db6ce4139a8db0d09c7078bdea5b.png
     method: vision-description
     described: 2026-08-21 -->

![Stacked bar chart of aggregated site energy across five chilled water upgrade scenarios](95003_images/image_000016_8ae0c5b67f3e4b316caa4dc4c184699f9640db6ce4139a8db0d09c7078bdea5b.png)

Figure 14: five stacked bars of annual site energy consumption in TBtu for applicable models only, from Baseline (993) through cumulative upgrade scenarios - chiller (951), chiller plus pumps (951), plus chilled water reset (933), and plus condenser water control (932). Bars are segmented by end use and fuel with values printed on the bands; cooling electricity carries the reduction.

To break this down further, Figure 15 isolates electricity consumption for cooling, pumps, and heat rejection (i.e., cooling tower fans). An increase in pump power is noticeable when the chilled water supply temperature reset is implemented, as discussed in Section 5.1. Changes in cooling tower fan energy use are minimal and nearly negligible.

Figure 15. Sensitivity analysis: aggregated electricity consumption related to chilled water systems

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95003.yaml
     source: 95003_images/image_000017_ae60b56202e1fe20737595c06c172a209d6b3d2f72a8f370d77ec7a46f76881a.png
     method: vision-description
     described: 2026-08-21 -->

![Horizontal stacked bars of chilled water system electricity by scenario, air- versus water-cooled](95003_images/image_000017_ae60b56202e1fe20737595c06c172a209d6b3d2f72a8f370d77ec7a46f76881a.png)

Figure 15: horizontal stacked bars of stock electricity consumption in TBtu attributable to chilled water systems, grouped into air-cooled and water-cooled panels with four cumulative upgrade scenarios each, segmented into cooling, pumps, and cooling tower electricity. Air-cooled cooling falls from 52.6 to 51.3 TBtu; water-cooled cooling falls from 69.4 to 65.4 while its pump electricity rises from 24.3 to 27.2.

To better understand the chiller operation characteristics across upgrade scenarios, Figure 16 presents chiller performance metrics and capacities using box plots. Compared to the baseline scenario, the rated COPs of chillers in all upgrade cases are higher, with the rated COP for upgraded water-cooled chillers nearly doubling. To provide a more industry-recognized performance metric, the IPLV expressed in EER is also included in Figure 16. A similar trend is observed in the annual average operating COPs across the different scenarios.

Figure 16. Sensitivity analysis: chiller capacities and performance metrics

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95003.yaml
     source: 95003_images/image_000018_f352346ab5d2bf2a4687f82ab9e8a2a227c650e353ceae4b150b5d082183a457.png
     method: vision-description
     described: 2026-08-21 -->

![Box plot grid of chiller capacities and performance metrics by scenario and condenser type](95003_images/image_000018_f352346ab5d2bf2a4687f82ab9e8a2a227c650e353ceae4b150b5d082183a457.png)

Figure 16: grid of box plots for air-cooled and water-cooled groups, with rows for baseline plus four cumulative upgrade scenarios and columns for rated COP, standard-rating IPLV EER in Btu/W-hr, chiller annual average operating COP, and chiller capacity in tons. The upgrade scenarios shift rated COP and IPLV EER distinctly above baseline while capacity distributions stay nearly unchanged.

