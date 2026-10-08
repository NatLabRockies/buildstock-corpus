<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/92618.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/92618.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/92618.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/92618.md | section: 5.4  Stock Utility Bill Impacts | lines: 451-484 -->
## 5.4  Stock Utility Bill Impacts

The measure scenario package shows between 3% and 4% savings in utility bills for the U.S. commercial building stock annually compared to the ComStock baseline depending on the electricity rate structure used (Figure 4). The HP-RTU scenario with roof insulation (Std Perf w Roof) shows slightly higher savings than the HP-RTU scenario alone (HP RTU Std Perf). The drivers of savings are similar to those discussed for site energy and GHG emissions. However, the cost difference of gas and electricity, the various rate structures across the country, and climate also influence utility bills and should be investigated in the ComStock public dataset as needed.

Figure 6. Electricity bill comparison of the ComStock baseline, the measure package scenario (Std Perf w Roof), and the standard performance heat pump RTU scenario (HP RTU Std Perf) in isolation

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/92618.yaml
     source: 92618_images/image_000008_7023cc0180e3eb6ecffdc92c56a61de9ae3582b138210fb47c9c7a4c9cf6d69c.png
     method: vision-description
     described: 2026-08-20 -->

![Three-panel stacked bar chart of annual utility bills under maximum, mean, and minimum electricity rates, Baseline vs HP RTU Std Perf vs Std Perf w Roof](92618_images/image_000008_7023cc0180e3eb6ecffdc92c56a61de9ae3582b138210fb47c9c7a4c9cf6d69c.png)

Figure 6. Three-panel stacked bar chart of Annual Utility Bill (Billion USD, 2022), y-axis 0 to about 150, under three electricity-rate assumptions. Each panel has three bars (Baseline, HP RTU Std Perf, Std Perf w Roof) stacked by fuel (Electricity, Natural Gas, Fuel Oil, Propane). With Max Electricity Rate: Baseline 142 (Electricity 123, Natural Gas 17), HP RTU Std Perf 139 (-2%), Std Perf w Roof 138 (-3%). With Mean Rate: Baseline 123 (Electricity 104, NG 17), HP RTU Std Perf 120 (-3%), Std Perf w Roof 119 (-3%). With Min Rate: Baseline 110 (Electricity 90, NG 17), HP RTU Std Perf 106 (-3%), Std Perf w Roof 105 (-4%). Bill savings are a low single-digit percent, slightly larger with the roof-insulation variant.

Because multiple electricity rates are simulated in ComStock, the maximum, mean, and minimum rates are presented for comparison.

Figure 6 illustrates the distribution of utility bill savings (%) by climate zone across models that received the measure scenario package compared to their corresponding baseline ComStock models representing existing buildings. Each data point represents the percentage bill savings for a single building model upgraded with the measure package relative to its existing state. Except for climate zone 8 (coldest), all climate zones show the median building reducing utility bills by around 5% -15%.

It is apparent that warmer and more temperate climates show higher bill savings on average compared to colder climates. A key factor in this is that the heat pumps modeled in this study experience reduced heating capacity and efficiency at colder temperatures, which colder climates will experience more of. Coupled with the assumed heat pump sizing scheme (size to cooling) and minimum lockout temperature of 0 º F, colder climates are also more likely to rely on relatively less-efficient supplemental electric resistance heating. Warmer climates, on the other hand, have more mild heating conditions on average where the heat pump is both more efficient and less likely to require supplemental heating. Additionally, all climates benefit from the cooling and fan savings when replacing older, less-efficient RTUs with newer RTUs, regardless of the heating source.

Figure 7 . Percent utility bills savings distribution for ComStock models with applied measure scenario package by end use and fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/92618.yaml
     source: 92618_images/image_000009_4a794eff8bae602346903fab706200cfc2dff69632324eab30532d6268ec55af.png
     method: vision-description
     described: 2026-08-20 -->

![Violin and box plots of percent utility bill savings by climate zone across the modeled stock for the measure package](92618_images/image_000009_4a794eff8bae602346903fab706200cfc2dff69632324eab30532d6268ec55af.png)

Figure 7. Horizontal violin-plus-box plots of Percent Utility Bill Savings by Climate (%), x-axis about -100% to 80%, titled 'Upgrade 5.0: Std Perf w Roof (unweighted)'. (The source caption labels this 'by end use and fuel type', but the plotted bitmap is by climate zone -- flag the caption mismatch for QA.) Rows are climate zones with model counts: 1A (n=795), 2A (n=1796), 2B (n=1010), 3A (n=3383), 3B (n=3925), 3C (n=1270), 4A (n=5278), 4B (n=1494), 4C (n=526), 5A (n=5313), 5B (n=2854), 6A (n=3038), 6B (n=1288), 7 (n=2131), and 8 (n=249). Most zones show a small positive median bill savings (roughly 5-15%); the coldest zone 8 is the exception, with a negative median (bill increase) as electrified heating raises costs in very cold climates.

Mean electric rate structure is used for each sample. The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

