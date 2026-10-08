<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89340.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89340.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89340.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89340.md | section: 5.1.2  Rebound Effect | lines: 443-457 -->
## 5.1.2  Rebound Effect

Figure 4 shows the daily load profile comparison of the same building in the baseline scenario, applying the 'default' parameter set, and applying the 'no rebound control' parameter set. As can be seen from the different post-peak load profiles, load shed strategy without addressing rebound effect would almost always generate new peak load higher than original baseline peak for the illustrated summer days, and this trend is maintained throughout the year among different building models. This reveals the natural drawback of rebound effect in load shed control for responsive systems that have ordinary differential equation component(s) such as HVAC systems. Therefore, rebound control is necessary in load shed strategy for thermostat control, and is included in the default scenario.

Figure 4. Daily load profile comparison for rebound control

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89340.yaml
     source: 89340_images/image_000005_0d341283ef45889cd4efef35c4c22492901956e2ea3276ede778c29c3f466d8c.png
     method: vision-description
     described: 2026-08-20 -->

![Line chart of hourly load over five days in mid-July comparing baseline, default load shed, and load shed without rebound control for one building, showing the no-rebound-control case spiking above the baseline peak each day](89340_images/image_000005_0d341283ef45889cd4efef35c4c22492901956e2ea3276ede778c29c3f466d8c.png)

Figure 4 of the ComStock thermostat-control-for-load-shedding measure documentation isolates the rebound effect for a single large office model. Hourly load (kWh, axis 50 to 250) is plotted for five consecutive days, 7/16 through 7/20, with three traces: a dashed 'Baseline', a solid red 'Load shed, Default', and a solid yellow 'Load shed, No rebound control'. Baseline afternoon peaks reach roughly 190 to 200 kWh. The default scenario clips those peaks to roughly 170 to 180 kWh and returns to the baseline curve gradually. The no-rebound-control scenario sheds the same load during the window but then snaps the setpoint back, producing a narrow spike each day that reaches roughly 210 to 220 kWh, above the original baseline peak on every one of the five days. The text notes this pattern holds throughout the year across different building models and reflects an inherent drawback of load shedding for responsive systems governed by differential-equation dynamics such as HVAC. Rebound control is therefore necessary and is included in the default scenario, which ramps linearly back to the nominal setpoint over two hours.

