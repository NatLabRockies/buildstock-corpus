<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86199.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/86199.md | section: 6.4  Measure Impact by HVAC System Type | lines: 771-798 -->
## 6.4  Measure Impact by HVAC System Type

Figure 15 shows the percent site energy savings by different types of HVAC system. DOAS with water-source heat pump cooling tower with boiler and PVAV with gas heat with electric reheat exhibited the least savings. The primary reason for the limited savings observed in the DOAS with water-source heat pump cooling tower with boiler system is that heat pumps predominantly fulfill the heating load while the boiler solely provides heating for the DOAS units. In the case of the PVAV with gas heat with electric reheat system, the reduced savings are attributed to the presence of electric reheat coils in the VAVs which handle majority of the heating. On the other hand, the VAV systems with boiler reheat demonstrate higher savings. This is mainly due to the relatively higher floor areas they serve, makes them well suited for application of this measure.

Figure 15. Percent savings by HVAC system type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86199.yaml
     source: 86199_images/image_000015_e9579f9db49ec8e160be6d43b625f41b0b73132f412beef78cbd865913aa8e2b.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by HVAC system type](86199_images/image_000015_e9579f9db49ec8e160be6d43b625f41b0b73132f412beef78cbd865913aa8e2b.png)

Figure 15: horizontal violin-and-box plot of percent site energy savings by HVAC system type, x-axis -20% to 60%, titled Upgrade 05: HP Boiler E Backup (unweighted), eleven rows with model counts (PVAV with gas boiler reheat n=27,122; PVAV with gas heat with electric reheat n=21,685). The DOAS water-source heat pump and electric-reheat PVAV rows are lowest, per Section 6.4.

In each category, a few buildings exhibited negative savings due to their very small heating loads. In the baseline case, these loads were managed by modulating the boiler. However, in the updated case, the small nonzero flow in the hot water loop triggered the heat exchanger to request flow in the heat pump loop. However, the heat pump model used only supports constant flow, leading to frequent cycling of the heat pumps, as depicted in Figure 16. Consequently, this resulted in higher energy usage compared to the baseline. Only a very small fraction of the total buildings demonstrated this behavior, rendering its impact on the overall result to be minimal, and the absolute energy impact was small.

Figure 16. Flow in the hot water loop that triggers heat pump operation

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86199.yaml
     source: 86199_images/image_000016_425f4fce5b76eaabfe2704816d5e5a37c1a8e58d2e86546d749878fb3d171fc6.png
     method: vision-description
     described: 2026-08-21 -->

![Annotated time series of hot water loop flow across spring showing a period of very small flow](86199_images/image_000016_425f4fce5b76eaabfe2704816d5e5a37c1a8e58d2e86546d749878fb3d171fc6.png)

Figure 16: dense time-series line chart of flow in the hot water loop across April through June for one model, y-axis 0 to about 2,200. A red ellipse and the note "Very small flow in the hot water loop" mark a stretch at the right end where flow nearly vanishes - the condition Section 6.4 links to limited heat pump operation.

