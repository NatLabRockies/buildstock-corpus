<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89340.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89340.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89340.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/89340.md | section: 5.2.1 Justification of Default Parameters | lines: 462-485 -->
## 5.2.1 Justification of Default Parameters

Figure 5 shows the distribution of median daily peak load reduction percentages in each month compared to the baseline model for different scenarios (Table 3) to investigate the impact of shorter peak window length, no rebound control, and larger thermostat setpoint adjustment. The results are derived from a ComStock test run with 10,000 building model samples (among which

90 large offices are applicable), due to the limitation of computational resources for full sample run (350,000 samples). From the figure we can conclude that:

- Different scenarios outperform others for any given month, depending on the compatibility of weather characteristics and the parameter set.
- The larger setpoint adjustment scenario generally leads to larger variance in peak reduction performance with more load shed potential but also higher risk of increased daily peak load.
- The shorter peak window scenario has similar performance to the default scenario, but it has a lower potential (upper limit) of peak reduction for most months.
- The no rebound control scenario shows accorded performance with the single building test result (Figure 4) where the rebound effect results in increased daily peak load for many months (April to October).

Figure 5. Distribution of reduction percentage of median daily peak load compared to the baseline model by month for measure with default and comparative scenarios

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89340.yaml
     source: 89340_images/image_000006_dca1b76a4e9daf0588275fd480bc137d1526bc80e1e2fb9f7fec746223f1a620.png
     method: vision-description
     described: 2026-08-20 -->

![Grid of box plots with one block per month and four rows per block for the default, more aggressive setback, shorter peak window, and no rebound control scenarios, showing median daily peak savings percentage from minus 30 to plus 20 percent](89340_images/image_000006_dca1b76a4e9daf0588275fd480bc137d1526bc80e1e2fb9f7fec746223f1a620.png)

Figure 5 of the ComStock thermostat-control-for-load-shedding measure documentation compares the four parameter scenarios of Table 3. For each month January through December, four box plots stack vertically, 'Default load shed', 'More aggressive setback', 'Shorter peak window', and 'No rebound control', on a shared x-axis of median daily peak savings from -30% to +20%. Boxes cluster just above zero for the first three scenarios in every month, with visibly wider spread in May through October. The 'More aggressive setback' rows have the widest whiskers, reaching the highest upper limits but also extending furthest negative. 'Shorter peak window' rows sit close to the default but with a lower upper limit in most months. The 'No rebound control' rows shift decisively negative from April through October, with the box centred below zero and whiskers reaching about -20% to -25% in June through August. Results come from a reduced ComStock test run of 10,000 building samples, of which only 90 large offices were applicable, rather than the full 350,000-sample run. No single scenario dominates every month; a larger setpoint adjustment buys shed potential at the cost of higher risk of increasing the daily peak.

Based on the comparison, the performance of default setting of the measure is determined to be the overall best in terms of peak reduction potential and performance.

