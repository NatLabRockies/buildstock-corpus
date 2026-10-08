<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89128.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89128.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89128.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/89128.md | section: 5.2 Stock Energy Impacts | lines: 805-836 -->
## 5.2 Stock Energy Impacts

The HP-RTU + ASHP Boiler + DCV + HR + Economizers package demonstrates 19.8% total site energy savings (857 trillion British thermal units [TBtu]) for the U.S. commercial building stock modeled in ComStock (Figure 9). The savings are a result of electrification of gas-furnace and boiler systems, which are then combined with efficiency upgrades like DCV, Heat/Energy Recovery, and Economizers:

- 86.7% stock heating gas savings (740.8 TBtu)
- -84.9% stock heating electricity savings (-148.7 TBtu)
- 21.8% stock cooling electricity savings (145.5 TBtu)
- 18.6% stock fan electricity savings (96.5 TBtu).

Figure 9. Comparison of annual site energy consumption between the ComStock baseline and the HP-RTU + ASHP Boiler + DCV + HR + Economizers (Package 5) scenario Energy consumption is categorized both by fuel type and end use.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89128.yaml
     source: 89128_images/image_000016_89852b2fc36f921f9b377f4903ebd5d012e22748fb9a88a3530f4a1869316083.png
     method: vision-description
     described: 2026-08-21 -->

![Stacked bar chart of annual site energy consumption by end use and fuel, baseline vs Package 5](89128_images/image_000016_89852b2fc36f921f9b377f4903ebd5d012e22748fb9a88a3530f4a1869316083.png)

Figure 9: stacked bar chart of annual site energy consumption in TBtu for the baseline and Package 5, each bar segmented by end use and fuel with the larger segments labeled. Totals fall from 4,338 to 3,481 TBtu. Natural gas heating drops from 838.9 while electricity heating rises 175.2 to 323.9 and cooling falls 667.3 to 521.8. Section 5.2 lists the end-use savings.

The HP-RTU + ASHP Boiler + DCV + HR + Economizers package is made up of five different HVAC measures, which results in measure interaction and compounding energy savings. While it is difficult to extract the savings attributed to each individual measure from the stock level results, we have an idea of what impacts each of the five measures should have on the results. This helps us validate that the savings we see from the full package are reasonable and as expected.

- HP-RTU : This measure electrifies natural gas heating in RTU systems, so we expect large natural gas heating savings (up to 50%) and heating electricity penalties. The measure also replaces electric resistance RTUs with higher efficiency heat pumps, so in

- those cases we see electric heating savings. These somewhat offset the electric heating penalties from buildings that started with natural gas heating, so the stock heating electricity penalty is expected to be no larger than 5%. We can also expect cooling and fan savings around 15%-25% due to replacing the existing cooling system with a higher efficiency heat pump.
- ASHP-Boiler: This measure electrifies gas boiler systems, so we expect large natural gas heating savings (up to 50%) and heating electricity penalties (up to 35%). The buildings this measure applies to tend to be larger buildings that make up a small portion of the stock by number of buildings but a more substantial portion of the stock by energy consumption. This building does not affect cooling or fan end uses, but we can expect some increases in pump energy due to the installation of the heat pump, although pump energy makes up a very small portion of the annual site energy.
- DCV: This measure reduces outdoor air intake during periods of reduced occupancy, resulting in heating and cooling savings during those times. We can expect up to 10% heating savings and up to 5% cooling savings because of the implementation of DCV. When combined with economizing, we may expect higher cooling savings because the technologies will work together to ensure the DCV is not reducing outdoor air if it is beneficial for cooling.
- Exhaust Air Heat/Energy Recovery: This measure installs heat/energy recovery systems which precondition outdoor ventilation air using exhaust air. This measure reduces the loads on heating and cooling coils, so we can expect up to 25% heating savings and up to 10% cooling savings at the stock level. We can also expect an increase in energy recovery end use; however, this makes up a very small portion of the annual stock site energy.
- Economizers: This measure implements economizing in buildings that do not already have it, enabling the spaces to leverage colder outdoor air when it is beneficial for cooling. We expect this measure to primarily impact cooling end uses with up to 5% savings. There could be small heating penalties (&lt;1%) because of this measure. Because economizing is already required by energy codes in some climates, the expected energy savings for this measure are lower than others in the package. However, when combined with the other HVAC measures in the package, there could be larger impacts.

When combining all five of these HVAC measures together, we see impressive stock-level savings of 19.8%. The two heat pump measures electrify 87% of the natural gas heating end use but add substantial electric heating loads. This large reduction in natural gas heating is possible because the HVAC systems that receive either the HP-RTU measure or ASHP-Boiler measure make up 62% of the ComStock floor area but 91% of the stock natural gas heating end use. The heat pumps also result in cooling savings due to the addition of a more efficient cooling system. When DCV, Heat/Energy Recovery, and Economizers are added after the heat pump measures, they result in additional cooling and fan savings as well as a reduced electric heating penalty at the stock level. In addition, there were changes in the heat recovery and pump end uses as discussed above, although these make up a small portion of the stock energy.

