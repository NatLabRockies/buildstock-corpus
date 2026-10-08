<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89341.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89341.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89341.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/89341.md | section: 5.2.1 Justification of Default Parameters | lines: 394-414 -->
## 5.2.1 Justification of Default Parameters

Figure 3 shows the distribution of median daily peak load reduction percentages in each month compared to the baseline model for different scenarios (Table 3), to investigate the impact of shorter pre-peak window length and larger thermostat setpoint adjustment. The results are derived from a ComStock test run with 10,000 building model samples (among which 90 large offices are applicable), due to the limitation of computational resources required for full sample run (350,000 samples). From the figure we can conclude that:

- Different parameter sets outperform others or perform similarly for any given month, depending on the compatibility of weather characteristics and the parameter set.
- The aggressive pre-cooling parameter set generally leads to larger variance in peak reduction performance with more load shift potential but also higher risk of new increased daily peak load.
- Shorter pre-peak increases the risk of new increased daily peak load.

Figure 3. Distribution of reduction percentage of median daily peak load compared to the baseline model by month for measure with default and comparative scenarios

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89341.yaml
     source: 89341_images/image_000005_9989c39b69208b7225ce03196ad31d66ef475c406a57b017c051ea6868bc468b.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 3. Grid of box plots of median daily peak load savings percentage by month, comparing the default load shift scenario against the more aggressive pre-cooling, shorter peak, and shorter pre-peak scenarios](89341_images/image_000005_9989c39b69208b7225ce03196ad31d66ef475c406a57b017c051ea6868bc468b.png)

Small-multiple box plot grid comparing measure parameter sets month by month. Rows are grouped by month, January through December, and within each month there are four scenario rows: Default load shift, More aggressive, Shorter peak, and Shorter pre-peak. The shared x-axis is Median Peak savings [%], running from about -15% through 0% to +5%, with positive values indicating peak reduction and negative values indicating a new, higher peak. Results come from a reduced ComStock test run of 10,000 model samples, of which 90 large offices were applicable. In the winter and shoulder months (January through April, October through December) all four scenarios are tightly clustered within roughly a percent of zero. In the cooling season (May through September) the distributions widen sharply and shift negative, most severely for the More aggressive scenario, whose boxes sit around -5% to -8% with whiskers past -15%. The Default scenario stays closest to zero with the least spread. The stated conclusions are that no single parameter set dominates in every month, that aggressive pre-cooling buys more shift potential at the cost of much larger variance and higher risk of creating a new peak, and that a shorter pre-peak window also raises that risk. On this basis the default settings were judged the most robust.

Based on the comparison, the performance of default setting of the measure is determined to be the overall best in terms of peak reduction potential and performance robustness.

