<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89239.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89239.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89239.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89239.md | section: 5.1  Single Building Example | lines: 421-485 -->
## 5.1  Single Building Example

This Central Hydronic Geothermal Heat Pump measure was applied to a hospital building in the Portland, Oregon, area as an illustrative example. In the baseline, the building was conditioned by a fuel-oil-fired boiler and an air-cooled chiller, with heating hot water and chilled water coils in central air handling units. Figure 5 and Figure 6 show the configuration of the ground loop, condenser loop, and intermediate condenser loops that connect the ground heat exchanger to the heat pumps and the heat pumps to the load.

Figure 5. Schematic of ground loop (left), and condenser loop (right) in modeled building

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89239.yaml
     source: 89239_images/image_000011_bd25d78f31449fbe15dbcfbcbabb5781007c5f5f1f3b8a1778b4ac17700b8044.png
     method: vision-description
     described: 2026-08-21 -->

![Paired OpenStudio loop schematics for the ground loop and condenser loop of the example building](89239_images/image_000011_bd25d78f31449fbe15dbcfbcbabb5781007c5f5f1f3b8a1778b4ac17700b8044.png)

Figure 5: two OpenStudio plant-loop screenshots for the single-building example - ground loop at left, condenser loop at right. Each shows a supply-equipment branch above a demand-equipment branch with pumps, splitters and mixers, and the heat exchanger or ground loop component in place. Component names are too small to read at extraction resolution; Section 5.1 describes the configuration.

Figure 6. Schematic diagram of intermediate heating loop (left) and main heating loop (right) in modeled building, with additional heating coils not shown

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89239.yaml
     source: 89239_images/image_000012_17636e2a0085baddffc670e014fc82b5aae5078bd02813f43e3f92cfa6a2ab1c.png
     method: vision-description
     described: 2026-08-21 -->

![Paired OpenStudio schematics of the intermediate heating loop and the main heating loop](89239_images/image_000012_17636e2a0085baddffc670e014fc82b5aae5078bd02813f43e3f92cfa6a2ab1c.png)

Figure 6: two OpenStudio plant-loop screenshots for the example building - intermediate heating loop at left, main heating loop at right - each drawn as a supply-equipment branch over a demand-equipment branch with pumps and coils. Additional heating coils are omitted from the drawing and component labels are illegible at extraction resolution. Section 5.1 gives the loop description.

The distribution of heat pump COPs across operating conditions is key to interpreting the significant energy savings from implementing the Central Hydronic GHP measure in this building. Figure 7 (left) shows the distribution of COP during operation for a 'base load' heating heat pump in the building. The comparatively poor COP in heating (&lt;3) is largely due to the relatively high (for supply by water-to-water heat pumps) heating hot water supply temperature considered (135°F), intended for maximal compatibility with existing hydronic building systems. Figure 7 (right) shows the distribution of cooling COPs for a 'base load' cooling heat pump. This heat pump operates consistently at a COP of 5.17. This higher COP reflects the relatively lower 'lift' of the heat pump in operating in cooling mode than in heating mode at these temperatures, given the temperatures of the source-side loop (operating at an average temperature of around 55°F). Both COPs are consistent with the performance data used to characterize the heat pump.

Figure 7. Distribution of COP for a heating heat pump (left) and cooling heat pump (right)

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89239.yaml
     source: 89239_images/image_000013_77ea87b7042f27447b5c63604064c4f6d49e7770a96c84de498be0e2bd3eff0d.png
     method: vision-description
     described: 2026-08-21 -->

![Paired histograms of heating and cooling heat pump COP over 15-minute timesteps](89239_images/image_000013_77ea87b7042f27447b5c63604064c4f6d49e7770a96c84de498be0e2bd3eff0d.png)

Figure 7: two histograms of water-to-water heat pump COP in the single-building example, counted in 15-minute timesteps. The left (heating) panel spans about 2.1 to 2.6 with nearly all timesteps in the 2.5-2.6 bin; the right (cooling) panel is a single spike at a COP near 5 covering roughly 35,000 timesteps. Table 2 lists rated heat pump performance.

Figure 8 (left) shows the distribution of COP for the air-cooled chiller serving the building in the baseline case, excluding condenser fan energy (consistent with the presentation of the heat pump COP without distribution pump energy). Note that the baseline chiller COP is generally less than 2. The plot at right in Figure 8 shows the annual distribution of boiler efficiency in the baseline case. The boiler efficiency is consistently 79%.

Figure 8. Distribution of baseline chiller COPs (left) and boiler efficiency (right) for the baseline case

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89239.yaml
     source: 89239_images/image_000014_155acfd9e4119a241dee160a7e21a1776940642219e7c59c33ce4947a924e514.png
     method: vision-description
     described: 2026-08-21 -->

![Paired histograms of baseline air-cooled chiller COP and baseline boiler efficiency](89239_images/image_000014_155acfd9e4119a241dee160a7e21a1776940642219e7c59c33ce4947a924e514.png)

Figure 8: two baseline histograms for the example building. The left panel plots air-cooled chiller COP from about 1.8 to 3.2, with most timesteps in the lowest bin near 1.8 and a thin tail above 2.0; the right panel plots boiler efficiency on a 0-to-1 axis as a single spike near 0.8, reflecting the constant 79% efficiency noted in Section 5.1.

Figure 9 shows the disaggregation of site energy consumption by end use for this building for the base case and with the Central Hydronic GHP measure applied. In this building, application of the measure results in 62% cooling energy savings, 100% fuel oil savings for space heating, and a 13% increase in pump energy use. The pump energy use increase is expected due to the increased pump head and load associated with the ground loop. The cooling energy savings results from the increase in COP associated with the cooling equipment. Elimination of fuel oil use for heating is expected, due to the full electrification of heating. The increase in electricity consumption for heating and for circulation pumps, while somewhat offset by cooling energy savings, results in a net increase of 9% in electricity use at the building level. Implementation of the measure results in a 40% reduction in site energy use overall in this building.

Figure 9. Disaggregation of site energy consumption by end use for base case and with Central Hydronic GHP measure applied

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89239.yaml
     source: 89239_images/image_000015_d9d853b5ca934f0376840c969a67901fa72e87f3c6117ef1f5ddfc3eab82db18.png
     method: vision-description
     described: 2026-08-21 -->

![Stacked bar chart of site energy use by end use, base case versus Central Hydronic GHP measure](89239_images/image_000015_d9d853b5ca934f0376840c969a67901fa72e87f3c6117ef1f5ddfc3eab82db18.png)

Figure 9: two stacked bars of annual site energy use in GJ (y-axis to about 140,000) for the example building, Base versus Measure, segmented by end use and fuel per the legend - cooling, lighting, equipment, fans, pumps, water systems, refrigeration, electric heating, and heating fuel oil #2. The measure bar is roughly 40% shorter and drops the fuel-oil heating band entirely.

