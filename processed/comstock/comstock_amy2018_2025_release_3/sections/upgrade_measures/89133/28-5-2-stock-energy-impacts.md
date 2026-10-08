<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89133.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89133.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89133.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/89133.md | section: 5.2 Stock Energy Impacts | lines: 327-356 -->
## 5.2 Stock Energy Impacts

This package demonstrates 18.0% total site energy savings (783 trillion British thermal units [TBtu]) for the U.S. commercial building stock modeled in ComStock (Figure 3). The savings are attributed to the electrification of natural gas heating systems, as well as efficiency improvements to cooling due to the installation of a GHP:

- 83.2% stock heating gas savings (711.7 TBtu)
- -96.7% stock heating electricity savings (-169.4 TBtu)
- 29.4% stock cooling electricity savings (196.3 TBtu)
- -92.5% stock pump electricity savings (-39.4 TBtu).

Figure 3. Comparison of annual site energy consumption between the ComStock baseline and the Comprehensive GHP scenario.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89133.yaml
     source: 89133_images/image_000010_8f7f65c756920bb051020c683d977a1740d306b8470700958f31443eaea12867.png
     method: vision-description
     described: 2026-08-20 -->

![Stacked column chart of annual stock site energy consumption by end use and fuel, Baseline vs Comprehensive GHP](89133_images/image_000010_8f7f65c756920bb051020c683d977a1740d306b8470700958f31443eaea12867.png)

Figure 3. Stacked column chart of Annual Energy Consumption (TBtu), y-axis 0 to 4500, comparing ComStock Baseline (total 4338) and Comprehensive GHP (total 3555), a reduction of about 783 TBtu (18%). Columns are segmented by end use and fuel per the legend. Legible segments: Interior Equipment Electricity 739.7 (unchanged); Fans Electricity 519.1 to 510.3; Cooling Electricity 667.3 to 471.0 (a large cooling-efficiency gain from the GHP); Heating Natural Gas 451.9 in the baseline largely replaced by Heating Electricity 344.6 in the GHP scenario as gas heating is electrified; a District Heating segment 175.2 in the baseline; Water Systems 191.0. Shows savings come from electrifying gas heating and from more efficient ground-source cooling.

Energy consumption is categorized both by fuel type and end use.

This package reduces stock-level natural gas heating by 83%, which is expected because the implementation of the GHP measures results in nearly full electrification of space heating in buildings for which it is applicable. There are a few exceptions to this, including some warehouse and retail spaces, which in the baseline RTU systems do not get the Packaged GHP upgrade, as described in the individual documentation for that measure. In addition, 20% of the ComStock floor area is made up of HVAC systems that do not receive any of the three GHP

measures, including district systems, direct evaporative coolers, and a few other less common system types. Therefore, this package does not electrify 100% of the natural gas heating load in ComStock.

There is a 97% increase in electric heating, which is also expected when transitioning from gas heating to electric heating. Note that the magnitude of the site's gas space heating savings is much larger than the magnitude of the site's electric space heating increase. This is due to the same space heating load being met more efficiently with heat pumps (heating coefficient of performance typically between 3 and 5) relative to the existing gas or electric coils in ComStock (efficiency 0.8 for gas and 1 for electric). As a result, the total heating load across all heating fuels decreased by 54%, which contributes substantially to the total site energy savings of 18%. However, note that site energy savings is not a comprehensive assessment of other notable considerations such as source energy savings, energy costs, greenhouse gas emissions, or peak demand.

The simulations also show a cooling savings of 29% because of the higher efficiency of the various heat pump configurations compared with existing cooling systems. The fans end use also showed a 2% savings, which is a result of numerous changes to operation across the three GHP configurations including changes in supply temperatures, cooling load requirements, and airflow rates. The pump end uses, while they make up a small portion of the total stock energy, experienced a 93% increase due to the pumping demands of the ground and condenser loops of the new GHP systems.

