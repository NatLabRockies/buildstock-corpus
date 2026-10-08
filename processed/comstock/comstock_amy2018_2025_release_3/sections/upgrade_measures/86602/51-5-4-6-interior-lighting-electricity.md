<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86602.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86602.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86602.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/86602.md | section: 5.4.6 Interior Lighting Electricity | lines: 917-950 -->
## 5.4.6 Interior Lighting Electricity

Finally, some models saw an 'Interior Lighting Electricity' penalty. This is attributed to the lower VLT from the window measure impacting models with daylight controls. These models may not be able to turn down the interior lights as much or as often with lower VLT windows, which can increase lighting equivalent full load hours (EFLH) and therefore increase lighting energy consumption. Figure 8 shows the relationship between interior lighting electricity percent savings and daylight control fraction. Models with higher daylight control fraction generally see a higher interior lighting penalty. Furthermore, the design interior lighting power density does not change between the baseline and upgrade package scenario, indicating the package is not impacting the interior lighting design. EFLH output variables also show a 1:1 relationship between EFLH percent increase and interior lighting penalty, supporting the conclusion that lower VLT windows are causing the interior lighting energy consumption increase.

Figure 8. Daylight control fraction vs. percent savings for interior lighting electricity

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86602.yaml
     source: 86602_images/image_000012_73cfd34b4e8cb526d96be48222466b78786e6274559064723cba0293da2f232c.png
     method: vision-description
     described: 2026-08-21 -->

![Scatter plot of daylight control fraction against interior lighting electricity savings](86602_images/image_000012_73cfd34b4e8cb526d96be48222466b78786e6274559064723cba0293da2f232c.png)

Figure 8: scatter plot of daylight control fraction (y-axis 0 to 1.0) against percent savings in interior lighting electricity consumption (x-axis -0.65 to 0.00, plotted as a fraction). Points crowd against zero and the penalty widens as the control fraction rises; no model shows a saving. Section 5.4.6 attributes the penalty to lower window visible light transmittance in daylight-controlled models.

Figure 9 shows the site energy savings distributions between the ComStock baseline and the High Efficiency Envelope, Interior Lighting and Heat Pump scenario by fuel type and total site energy. The total site energy savings distribution shows savings values generally between 15% and 40% for the 25 th and 75 th percentiles, respectively. Combined site energy savings alone is not a comprehensive assessment of electrification measures, so other considerations should be made as well.

The site electricity distribution shows some energy penalties. These are mostly buildings that changed from gas heat to electric heat, so the penalties are expected. Some of this electricity penalty is reduced or mitigated through savings for cooling, fans, and heat recovery, depending on the building and its climate zone. Many of the buildings, however, show electricity savings. Many of these models had their interior replaced with LEDs, or had their envelope updated. Others are buildings that had electric heating in the baseline; in these cases, the higher-efficiency HP-RTU system reduces electricity usage across multiple end uses.

The 'Natural Gas' and 'Other Fuel' end uses show many models with near 100% savings. These are buildings that are completely electrified from the HP-RTU or ASHP Boiler measures and where gas is not used for other end uses. Models with less than 100% gas or other fuel savings generally have some nonapplicable gas HVAC system type in the baseline, or other end uses, such as water heating, that are not electrified through the HP-RTU or ASHP Boiler measures. Some of these models only had the envelope measures applied, which resulted in lower heating savings compared to the HP measures. Several models show negative natural gas site savings. These are primarily models that either (1) only had the LED lighting measure applicable and therefore had higher heating requirements, (2) are losing beneficial solar gain through lower SHGCs from the window measure, or (3) have low heating loads that show misleadingly high percentage change in heating consumption, as previously discussed. This is the case for district heating negative savings, as well.

Figure 9. Percent site energy savings distribution for ComStock models with the High Efficiency Envelope, Interior Lighting and Heat Pump package applied by fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86602.yaml
     source: 86602_images/image_000013_2fdc99452add6eebd4497024c4cec9c3aa6741dd5215685dd106565ab0a2d31e.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by fuel type, including total site energy](86602_images/image_000013_2fdc99452add6eebd4497024c4cec9c3aa6741dd5215685dd106565ab0a2d31e.png)

Figure 9: horizontal violin-and-box plot of percent site energy savings by fuel, x-axis -140% to 100%, six rows - district cooling (n=58), district heating (n=93), other fuel (n=447), natural gas (n=6,204), electricity (n=9,543) and site (n=9,544). Natural gas and other fuel carry the highest medians, roughly 60% to 90%. Section 5.4 puts the site row's middle 50% at 15% to 40%.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

