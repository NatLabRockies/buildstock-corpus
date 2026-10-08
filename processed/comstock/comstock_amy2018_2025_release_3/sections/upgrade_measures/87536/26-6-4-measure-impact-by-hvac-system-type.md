<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/87536.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/87536.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/87536.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/87536.md | section: 6.4  Measure Impact by HVAC System Type | lines: 615-642 -->
## 6.4  Measure Impact by HVAC System Type

Figure 11 shows the percent site energy savings by different types of HVAC system. DOAS with water-source heat pump cooling tower with boiler and PVAV with gas heating with electric reheat had the lowest savings. The primary reason for the limited savings for the DOAS with water-source heat pump cooling tower with boiler is that the heat pumps predominantly fulfill the heating load while the boiler solely provides heating for the DOAS units. Also, this measure only replaces the boilers in the hot water loop and doesn't replace supplemental boilers in the condenser loop for heat pump applications. In the case of the PVAV with gas heating and an electric reheat system, the reduced savings are attributed to the presence of electric reheat coils in the VAVs, which provide most of the heating. On the other hand, the VAV systems with boiler reheat show higher savings. This is mainly because the floor areas they serve are relatively large, which makes them well suited for the application of this measure.

Figure 11. Percent site energy savings by HVAC system type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/87536.yaml
     source: 87536_images/image_000016_f50d40e67712cdafc87a9e168be51a97b005ea4d51b1c1d5e4b603c15d54c115.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by HVAC system type](87536_images/image_000016_f50d40e67712cdafc87a9e168be51a97b005ea4d51b1c1d5e4b603c15d54c115.png)

Figure 11: horizontal violin-and-box plots titled Upgrade 06: HP Boiler G Backup (unweighted), percent site energy savings from about -20% to 60% on the x-axis, with eleven HVAC system rows labeled by model count. PVAV with gas heat and electric reheat (n=21,687) sits near zero while the VAV-with-boiler-reheat rows center near 20-30%. Section 6.4 explains the spread.

In each category, there were a few buildings that had negative savings due to their very low heating loads. In the baseline case, these loads were managed by modulating the boiler. However, in the updated case, the low flow in the hot water loop triggered the heat exchanger to request flow in the heat pump loop. However, the heat pump model used only supports a constant flow, which resulted in frequent cycling of the heat pumps, as shown in Figure 12. This resulted in higher energy consumption compared to the baseline. Only a very small fraction of the total buildings demonstrated this behavior, rendering its impact on the overall result to be minimal, and the absolute energy impact was small.

Figure 12. Flow in the hot water loop that triggers heat pump operation

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/87536.yaml
     source: 87536_images/image_000017_05ad0353f21670cb1fbd21a7a86c1fe1f13f1acf3c34f9bc75b0ba33e2fcb96a.png
     method: vision-description
     described: 2026-08-21 -->

![Annotated simulation time series showing very small flow in the hot water loop over spring](87536_images/image_000017_05ad0353f21670cb1fbd21a7a86c1fe1f13f1acf3c34f9bc75b0ba33e2fcb96a.png)

Figure 12: screenshot of a simulation time series spanning roughly April through June, showing tightly spaced spikes in loop flow and an annotation with a red ellipse reading "Very small flow in the hot water loop". It documents the low-load case where the heat exchanger requests flow and the constant-flow heat pump model cycles frequently. Section 6.4 explains the resulting negative savings.

