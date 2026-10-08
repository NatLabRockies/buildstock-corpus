<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/87542.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/87542.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/87542.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/87542.md | section: 5.1  Single Building Example | lines: 471-524 -->
## 5.1  Single Building Example

In this section, we describe the operation behavior of a small office building in Golden, Colorado. The model uses packaged RTUs with direct expansion (DX) cooling and gas furnace heating. Outdoor ventilation air is provided directly through the RTUs. The baseline model starts with no energy recovery. When the upgrade is applied, an ERV is added to all RTUs.

Figure 5 shows the operation of the heat/energy recovery on a sample winter day. The area of interest falls within the hours where the RTU has outdoor airflow (light green line). During this period, the RTU is targeting a mixed air temperature of between 70°F and 75°F, while the outdoor air temperature is between 35°F and 40°F (blue line). The ERV recovers energy from the exhaust airstream, which raises the outdoor air temperature to around 60°F. This value still falls below the mixed air temperature set point, which means the remaining gap must be addressed by the heating coil, noting that return air may also cover some of this gap. The heat/energy recovery increases the outdoor air temperature to reduce load on the main heating coil. Similarly, Figure 5 demonstrates this behavior during a sample summer day, where the heat/energy recovery reduces the outdoor air temperature, therefore reducing load on the cooling coil.

Figure 7 demonstrates the frost prevention functionality of heat/energy recovery in the sample model. When the heat/energy recovery outlet air temperature (blue line) reaches the specified minimum exhaust temperature for frost prevention of 35°F, the sensible and latent effectiveness (pink and yellow lines, respectively) of the ERV are reduced. This occurs due to the heat/energy recovery initializing a bypass of the inlet air to keep the exhaust air temperature above 35°F, which prevents frost buildup.

Table 6 compares the energy consumption of the baseline sample model to the upgrade model with the heat/energy recovery measure applied. Adding energy recovery to the RTUs shows 14% whole building energy savings. The heating and cooling end uses show 45% and 14% annual site energy savings, respectively, due to the preconditioning of outdoor ventilation air that the energy recovery offers. The upgrade model shows additional E/HR energy that represents the additional fan power needed to overcome the static pressure added by the energy recovery heat exchanger.

Figure 5. Example heat/energy recovery operation for winter day.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/87542.yaml
     source: 87542_images/image_000006_47d8571a0078c0742d308d2ab32f5dc52a28e61215ee6ff606c68e0e8c7107d1.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 5. Time series plot of example heat/energy recovery operation on a sample winter day, showing outdoor air temperature, ERV outlet temperature, target mixed air node temperature setpoint, and RTU outdoor airflow over 24 hours](87542_images/image_000006_47d8571a0078c0742d308d2ab32f5dc52a28e61215ee6ff606c68e0e8c7107d1.png)

Annotated 24-hour time series for the single-building example, a small office in Golden, Colorado with packaged rooftop units, DX cooling, gas furnace heating, and an added ERV, plotted for a sample winter day (x-axis dated Jan 17, hours 00 through 21). The left y-axis is temperature in degrees F from below 0 to about 125; the right y-axis is the RTU outdoor air node mass flow rate. Four series are called out with labeled callout boxes: Outdoor air temperature, ERV outlet temperature, Target mixed air node temperature setpoint, and RTU Outdoor Airflow (the light green square-wave line that steps up at roughly hour 09 and back down near hour 19, bracketing the occupied period). Reading only inside that occupied window, which the text identifies as the area of interest: the RTU targets a mixed air temperature between 70F and 75F, the outdoor air temperature runs between 35F and 40F, and the ERV raises the entering outdoor air to roughly 60F. Because 60F is still below the mixed air setpoint, the remaining gap must be met by the heating coil and by return air mixing, so the recovery device reduces rather than eliminates the heating coil load. A brief temperature spike appears at system startup.

Figure 6. Example heat/energy recovery operation for summer day.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/87542.yaml
     source: 87542_images/image_000007_8498f6a339f52cc42b9cbca97b0b625ada7fda8cc6f818d86e33e235e71595f2.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 6. Time series plot of example heat/energy recovery operation on a sample summer day, showing outdoor air temperature above the ERV outlet temperature, the target mixed air node temperature setpoint, and RTU outdoor airflow over 24 hours](87542_images/image_000007_8498f6a339f52cc42b9cbca97b0b625ada7fda8cc6f818d86e33e235e71595f2.png)

Summer-day counterpart to Figure 5 for the same Golden, Colorado small office example, plotted over 24 hours (x-axis dated Jul 19). The left y-axis is temperature in degrees F, and the right y-axis is the RTU outdoor air node mass flow rate. The same four series are annotated with callout boxes: Outdoor air temperature, ERV outlet temperature, Target mixed air node temperature setpoint, and RTU Outdoor Airflow, the light green line that steps up near hour 08 and back down near hour 18 to mark the occupied period. The ordering of the temperature series is inverted relative to the winter case: outdoor air temperature is the highest curve, rising to roughly the high 80s F during the afternoon; the ERV outlet temperature sits below it in the roughly 68F to 75F range; and the target mixed air node temperature setpoint is the lowest, a flat line near the mid 50s F. The gap between the outdoor air and ERV outlet curves is the sensible precooling delivered by the energy recovery device, which lowers the entering air temperature and therefore reduces the load on the cooling coil, the summer analogue of the winter heating coil savings.

Figure 7. Heat/energy recovery sample defrost operation.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/87542.yaml
     source: 87542_images/image_000008_595e736284b669b3f5c3a8efe317fd4ce5f1503d65730c00d847dcf16eec5205.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 7. Time series plot of sample defrost and frost prevention operation, showing ERV sensible effectiveness and ERV latent effectiveness dropping as the ERV exhaust air temperature falls to the 35F minimum on a cold winter day](87542_images/image_000008_595e736284b669b3f5c3a8efe317fd4ce5f1503d65730c00d847dcf16eec5205.png)

Time series illustrating the frost prevention control for the sample model on a cold winter day (x-axis dated Dec 16, hours 00 through 21). Three annotated series are plotted: ERV Sensible Effectiveness (pink), ERV Latent Effectiveness (yellow), and ERV Exhaust Air Temperature (blue, on a separate axis). Effectiveness values are fractions: sensible sits near 0.65 to 0.68 and latent near 0.55 to 0.58 while the unit runs, both stepping up sharply from zero when the system starts near hour 08. The exhaust air temperature series falls steeply through the occupied period, dropping in visible steps to its lowest values in the afternoon. Coincident with that decline, both effectiveness curves are stepped downward in the second half of the day, sensible falling toward about 0.55 and latent toward about 0.50. The text explains the mechanism: defrost is modeled by holding the heat exchanger exhaust outlet temperature at or above the EnergyPlus default minimum of 35F, and when that limit is reached the system bypasses some inlet air around the recovery device, which reduces both sensible and latent effectiveness and keeps the exhaust stream warm enough to prevent ice formation.

Table 6. Annual Energy Consumption Comparison of Baseline and Upgrade for Sample Model

|               |   Baseline (GJ) |   Upgrade (GJ) | % Savings   |
|---------------|-----------------|----------------|-------------|
| Total         |            1818 |           1557 | 14%         |
| Heating       |             629 |            345 | 45%         |
| Cooling       |             175 |            162 | 7%          |
| Fans          |             280 |            280 | 0%          |
| Heat Recovery |               0 |             35 | -           |
| Other         |             734 |            734 | 0%          |

