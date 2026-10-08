<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86199.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/86199.md | section: 4.2.2.1  Sizing Based on Peak Load Percentage | lines: 506-528 -->
## 4.2.2.1  Sizing Based on Peak Load Percentage

In this approach, the target capacity is estimated as a percentage of the DHL. The corresponding outdoor air temperature (target OAT) that results in a heating demand equal to the target capacity is determined using the heating load line, as shown in Figure 5.

𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇 𝐶𝐶𝑇𝑇𝐶𝐶𝑇𝑇𝐶𝐶𝐶𝐶𝑇𝑇𝐶𝐶 = 𝑃𝑃𝑇𝑇𝑇𝑇𝑃𝑃 𝑃𝑃𝑇𝑇𝑇𝑇𝐶𝐶𝑇𝑇𝑃𝑃𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇 ∗ 𝐵𝐵𝐵𝐵𝐶𝐶𝐵𝐵𝑇𝑇𝑇𝑇 𝐶𝐶𝑇𝑇𝐶𝐶𝑇𝑇𝐶𝐶𝐶𝐶𝑇𝑇𝐶𝐶

where 16°C (60°F) is the assumed outdoor air temperature to enable heating, HDT is the heating design temperature, and DHL is the design heating load (which is assumed to be equal to the heating capacity of the existing boiler in the model).

As shown in Figure 5, the heat pump's capacity drops as the outdoor air temperature decreases. Thus, the heat pump should be sized to provide the target capacity when operated at the target OAT. When the outdoor air temperature is lower than the target OAT, the backup heater will supplement the heat pump. Once the outdoor temperature is lower than the heat pump cutoff temperature, the heat pump will stop operating and the backup heater will be the only source of heating. For this reason, the backup heating must be sized to accommodate the full DHL. The shaded region in Figure 5 indicates the portion of the heating provided by the backup heater.

If the target OAT is lower than the cutoff temperature, the target capacity should be computed based on the cutoff temperature instead of the target OAT.

Figure 5. Heat pump sizing approach

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86199.yaml
     source: 86199_images/image_000006_0f0e72c917b035de7fb98bc90881a14b3e35114dc52ea53a5c67dbccf41ab1ed.png
     method: vision-description
     described: 2026-08-21 -->

![Diagram of the heat pump sizing approach relating capacity and heating load to outdoor temperature](86199_images/image_000006_0f0e72c917b035de7fb98bc90881a14b3e35114dc52ea53a5c67dbccf41ab1ed.png)

Figure 5: schematic plotting heat pump capacity and a descending heating load line against outdoor air temperature (MBh on the y-axis) from the heating design temperature to 60F. Their intersection is labeled Target Capacity at a percentage of the design heating load, with the cutoff, target and design outdoor temperatures marked below. Section 4.2.2.1 explains this peak-load-percentage sizing.

