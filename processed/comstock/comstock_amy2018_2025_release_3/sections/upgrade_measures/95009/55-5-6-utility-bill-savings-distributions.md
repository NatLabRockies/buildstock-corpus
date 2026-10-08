<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95009.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95009.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95009.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/95009.md | section: 5.6 Utility Bill Savings Distributions | lines: 983-1014 -->
## 5.6 Utility Bill Savings Distributions

When evaluating utility bills savings distributions, there is a slight correlation between total utility bills savings and climate zone (Figure 8). A map of the ASHRAE climate zones is included in 0 [22]. In warmer climate zones, the median utility bill savings reach 30%-35%, whereas in the colder climate zones, the median is closer to 20%-25%. This is due to cold climates having higher heating loads. This package converts much of the natural gas heating load to electricity (which costs more than natural gas in most locations), therefore the utility bills in colder climates are impacted more significantly. However, the efficiency improvements from the envelope and lighting measures and GHPs offset the utility bill costs, therefore all climates see net positive savings in utility bills in the top 75% of buildings.

There are some buildings in the bottom 25% in each climate zone that see negative utility bill savings (i.e., an increase in bills). These are primarily buildings that didn't originally have cooling, or buildings in locations where electricity is much more expensive than natural gas. In addition, these once again tend to be buildings with low loads/bills, where the percent change is sensitive to any change in magnitude.

Figure 8. Percentage utility bills savings distribution for ComStock models with the Comprehensive GHP + High Efficiency Envelope + LED Lighting scenario applied by climate zone

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95009.yaml
     source: 95009_images/image_000009_595b78c3cfdd3b196f485a3d6d8e7c3dbfc59c8b40cb56a80c09771d7235c302.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 8. Violin and box plot distribution of percent utility bill savings by ASHRAE climate zone for models with the Comprehensive GHP + High Efficiency Envelope + LED Lighting scenario applied](95009_images/image_000009_595b78c3cfdd3b196f485a3d6d8e7c3dbfc59c8b40cb56a80c09771d7235c302.png)

Figure 8 is a horizontal violin plot with embedded box plots of percent utility bill savings by ASHRAE climate zone, annotated "Upgrade 57.0: Package_11 (unweighted)", with an x-axis from about -100% to +100% and a reference line at 0%. Rows from top to bottom with model counts: 1A (n=2445), 2A (n=5793), 2B (n=3189), 3A (n=11558), 3B (n=13869), 3C (n=4388), 4A (n=17214), 4B (n=4652), 4C (n=1569), 5A (n=16199), 5B (n=8312), 6A (n=9268), 6B (n=3822), 7 (n=5868), 8 (n=497). Medians sit positive in every zone, generally in the 20%-40% range, with the interquartile boxes widening in the colder zones. Zone 8 again shows the widest spread on the smallest sample. Left tails extend past -80% for a minority of models where the added electricity cost of the heat pump and ground-loop pumping outweighs the displaced fuel bill. Note that the model counts differ slightly from the site energy version of this chart (Figure 7) because utility bill results are unavailable for a handful of models in each zone.

When evaluating utility bill savings by fuel type (Figure 9), we see that natural gas, fuel oil, and propane bills show the highest reduction in bills, with the top 75% of buildings saving over 50%. Electricity bill savings are in the 10%-40% range for the middle 50% of buildings. Some buildings do show negative electricity bill savings, meaning the new electric heating load was not offset by the efficiency improvements of the GHP, envelope, or lighting measures.

The total utility bill when using the mean electricity rate for each building saw 20%-40% savings for the middle 50% of buildings. Some buildings saw total bill savings above 50%, while others saw an increase in their total utility bill as a result of converting to electric heating.

Figure 9. Percentage utility bills savings distribution for ComStock models with the Comprehensive GHP + High Efficiency Envelope + LED Lighting package applied by fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95009.yaml
     source: 95009_images/image_000010_d324828317df7accd9682ac2ce4b985e4d085bd276491e33d3d9da3e67d49157.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 9. Violin and box plot distribution of percent utility bill savings by fuel type for models with the Comprehensive GHP + High Efficiency Envelope + LED Lighting package applied](95009_images/image_000010_d324828317df7accd9682ac2ce4b985e4d085bd276491e33d3d9da3e67d49157.png)

Figure 9 is a horizontal violin plot with embedded box plots of percent utility bill savings by fuel type for the Comprehensive GHP + High Efficiency Envelope + LED Lighting package, annotated "Upgrade 57.0: Package_11 (unweighted)", with an x-axis from about -160% to +100% and a reference line at 0%. Rows from top to bottom with model counts: Propane Bill State Average (n=3356), Fuel Oil Bill State Average (n=1396), Natural Gas Bill State Average (n=56813), Electricity Bill w/ Mean Rate (n=108535), Bill Mean (n=108738). The three delivered- and piped-fuel rows cluster tightly against 100% savings, since the package removes fossil heating almost entirely and with it the whole fuel bill. The electricity row is centered around 25%-35% savings with a symmetric spread and a long left tail past -160% for models where electrification raises the electric bill sharply. The "Bill Mean" row, which is the total bill across all fuels, is centered around 30% savings with a tighter distribution than the electricity-only row.

