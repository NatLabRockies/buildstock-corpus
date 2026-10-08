<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89341.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89341.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89341.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/89341.md | section: 5.1  Single Building Measure Tests | lines: 364-391 -->
## 5.1  Single Building Measure Tests

Several single building measure tests are performed to demonstrate the implementation of the developed measure, as shown in the following sections. Specifically, a large office building model with electric cooling HVAC systems is applied as the baseline sample model, with multiple weather files that represent different climate characteristics to evaluate performances.

The default and alternative sets of input parameters are summarized in Table 3. Parametric analysis is performed using these input parameter sets (scenarios) to investigate the impact of thermostat setpoint adjustment magnitude and pre-peak window length on peak load reduction performance.

Table 3. Default and Compared Options for Measure Parameters

| Parameter                                  | Default                                       | More Aggressive Pre-Cooling   | Shorter Pre-Peak   |
|--------------------------------------------|-----------------------------------------------|-------------------------------|--------------------|
| Length of peak window                      | 4 hours                                       | Same as default               | Same as default    |
| Length of pre-peak period                  | 2 hours                                       | Same as default               | 1 hour             |
| Thermostat setpoint adjustment (pre- peak) | 1°C                                           | 2°C                           | Same as default    |
| Load prediction method                     | Perfect prediction (full baseline simulation) | Same as default               | Same as default    |

Figure 2 shows the load profiles for three consecutive days (8/7-8/9) from several simulations corresponding to different scenarios for comparison. Comparison between the baseline profile and the load shift events (appearing as peaks followed by valleys) in the default load shift profile illustrate the timing of the pre-peak period and the peak window each day. Figure 2 shows that even with the default parameter set, there is still a chance of generating a new higher peak load in the pre-cooling period (shown on 8/8), and this chance increases with the more aggressive precooling scenario. The shorter pre-peak scenario could yield a higher chance of creating a new peak because the pre-cooling starts closer to the original peak, when the initial cooling load is higher, compared to the default scenario.

Figure 2. Daily load profile comparison for baseline and different scenarios

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89341.yaml
     source: 89341_images/image_000004_2e8bde333eff30d31d7899e57c5ece81e72e0a987e0a380e0b063ba08d9a9df8.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 2. Two stacked line charts of hourly building load in kWh over three consecutive days (August 7 to 9), comparing the baseline against the default load shift scenario and, respectively, the more aggressive pre-cooling and shorter pre-peak scenarios](89341_images/image_000004_2e8bde333eff30d31d7899e57c5ece81e72e0a987e0a380e0b063ba08d9a9df8.png)

Two stacked time-series line charts of hourly building load in kWh across three consecutive summer days labeled 8/7, 8/8 and 8/9, for a single large office test model. Both panels share a y-axis of Hourly load (kWh) from 50.00 to 250.00 and both plot the same dashed blue Baseline and solid red Load Shift, Default series; the top panel adds Load Shift, More Aggressive Pre-cooling and the bottom panel adds Load Shift, Shorter Pre-peak, both in yellow. Each day shows an overnight floor near 110 kWh climbing to a broad daytime peak near 200 kWh. The load shift traces depart from the baseline as a spike followed by a dip, which visually marks the pre-cooling period and the subsequent peak window where the pre-conditioned thermal mass suppresses load. On 8/8 the shifted traces overshoot the baseline peak, reaching roughly 215 kWh, demonstrating that even the default parameter set can create a new higher peak during pre-cooling. The more aggressive pre-cooling and shorter pre-peak variants both overshoot more, because a larger setpoint offset or a pre-cool window that starts closer to the original peak acts when the cooling load is already high.

