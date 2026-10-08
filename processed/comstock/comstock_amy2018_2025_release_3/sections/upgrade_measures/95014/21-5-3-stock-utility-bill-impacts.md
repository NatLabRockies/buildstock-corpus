<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95014.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95014.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95014.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/95014.md | section: 5.3  Stock Utility Bill Impacts | lines: 691-724 -->
## 5.3  Stock Utility Bill Impacts

This section includes a comparison of national-level annual utility bills of the stock across different fuel sources (i.e., electricity, natural gas, propane, and fuel oil). ComStock uses utility region mapping to determine all associated electricity rates that can be used by a building in that region. Therefore, the results can include many annual utility rates per building. The comparison in this section highlights three statistics (maximum, mean, and minimum) across all possible electric utility rates in a given location. For more information about the utility bill methodology in ComStock, see the ComStock Reference Documentation [5].

When combining all fuels, the Condensing Boiler measure scenario resulted in $1 billion (1%) total utility bill savings (Figure 11) across the building stock. The bill reduction is attributable to natural gas savings, with minimal impact on electricity bills. The natural gas rates used are fixed by state and therefore remain constant across all three scenarios shown.

Figure 11. Comparison of national annual utility bills between the ComStock baseline and the Condensing Boiler measure scenario

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95014.yaml
     source: 95014_images/image_000013_259c22a34b5579c8c87f3f4e33afdc03e15a7f3cd011c2181f8d99692369333a.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 11. Three panels of stacked bars comparing national annual utility bills for the baseline and Condensing Boilers scenario under maximum, mean and minimum electricity rates, each showing a 1% total reduction driven entirely by natural gas](95014_images/image_000013_259c22a34b5579c8c87f3f4e33afdc03e15a7f3cd011c2181f8d99692369333a.png)

Three side-by-side panels of stacked bars titled With Max Electricity Rate, With Mean Electricity Rate and With Min Electricity Rate, each holding a Baseline bar and a Condensing Boilers bar. Shared y-axis: Annual Utility Bill (Billion USD, 2022), 0 to 160. Legend: Electricity, Natural Gas, Propane, Fuel Oil. Printed values, baseline then measure: max rate total 144 to 143 (-1%), electricity 125 to 125, natural gas 17 to 16; mean rate total 127 to 126 (-1%), electricity 108 to 108, natural gas 17 to 16; min rate total 112 to 111 (-1%), electricity 93 to 93, natural gas 17 to 16. Propane and fuel oil are too small to label. The natural gas band is identical across all three panels because, as Section 5.3 notes, natural gas rates are fixed by state and do not vary with the electricity rate scenario; only the electricity band changes between panels. The mean-rate panel corroborates Table ES-3 exactly, which gives a baseline total of 126.8, electricity 107.7 and natural gas 17.4 billion 2022 dollars. The stated result is $1 billion, about 1%, of total utility bill savings across the building stock, attributable to natural gas with minimal impact on electricity bills.

Figure 12 shows the percentage utility bill savings distributions of the baseline ComStock models versus the Condensing Boiler measure by fuel type for applicable models. In other words, each data point in the distribution represents the percentage utility bill savings between a baseline ComStock model and the corresponding model with measures applied.

When evaluating utility bill savings by fuel type for buildings applicable to the measure scenario, we see that natural gas bills show 10%-15% savings in most buildings, with the upper whisker reaching 25%. There were only minor changes in electricity bills, which could be a result of small changes in cooling, fan, or pump operation. Fuel oil bills show 10%-20% savings for the middle 50% of buildings, with the upper whisker reaching 30% savings. The total utility bill shows up to 5% savings for the middle 50% of buildings, with the upper whisker reaching 10% total bill savings. A few outliers show negative savings (an increase) in natural gas bills or total bills. Upon investigation, these outliers were a small number of buildings in hot climates that either (a) have a negligible heating load, or (b) appear to have had some anomaly with outdoor air behavior that caused an increase in heating and/or cooling loads.

Figure 12. Percentage utility bill savings distribution by fuel type for ComStock models with the Condensing Boiler measure applied

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95014.yaml
     source: 95014_images/image_000014_8f566c8c218a46bef5584fa69446c1373985c7a6441911b5170e1255fa3538dd.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 12. Horizontal violin-and-box distributions of percent utility bill savings by fuel type for applicable ComStock models, with natural gas bills centered on 10 to 15% savings and total bill savings up to about 5% for the middle 50%](95014_images/image_000014_8f566c8c218a46bef5584fa69446c1373985c7a6441911b5170e1255fa3538dd.png)

Horizontal violin plots with embedded box plots, annotated Upgrade 16.0: Condensing Boilers (unweighted). X-axis: Percent Utility Bill Savings by Fuel (%), -120 to 100, with a reference line at 0. Rows top to bottom with their applicable-model counts: Propane Bill State Average (n=1), Fuel Oil Bill State Average (n=544), Natural Gas Bill State Average (n=30313), Electricity Bill w/ Mean Rate (n=30691), Bill Mean (n=30859). The propane row contains a single model and shows no distribution. Per Section 5.3, natural gas bills show 10%-15% savings in most buildings with the upper whisker reaching 25%; fuel oil bills show 10%-20% savings for the middle 50% with the upper whisker at 30%; electricity bill changes are minor, a narrow distribution straddling zero attributed to small changes in cooling, fan or pump operation; and the total Bill Mean row shows up to 5% savings for the middle 50% with the upper whisker at 10%. Scattered points far left of zero are outliers beyond 1.5 times the interquartile range, traced to a small number of buildings in hot climates with negligible heating load or an outdoor-air anomaly that increased heating and cooling loads.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

