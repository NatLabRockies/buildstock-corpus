<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95005.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95005.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95005.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/95005.md | section: 5.8.1  Ground Heat Exchanger Sizing | lines: 981-1033 -->
## 5.8.1  Ground Heat Exchanger Sizing

Figure 12 shows the borehole count, borehole depth, and total length of the ground heat exchanger for the Comprehensive GHP package and Comprehensive GHP + High Efficiency Envelope package. Because commercial buildings have such a wide range of size and load, the borehole count is normalized by building floor area (number of boreholes per thousand feet of floor area). The total ground heat exchanger loop length is calculated by multiplying the number of boreholes by the borehole depth, resulting in a rough approximation for the total length of drilling that would be required for the system.

When comparing the Comprehensive GHP package and Comprehensive GHP + High Efficiency Envelope package, the median normalized borehole count is reduced by 0.3 boreholes per thousand feet of floor area (21% reduction) with the addition of the envelope measures. However, at the upper end of the box and whisker, we see the upper quartile is reduced by 1.1 boreholes per thousand feet (19% reduction), and the upper whisker is reduced by 2.6 boreholes per thousand feet (19% reduction).

The number of boreholes is not the only factor; the average borehole depth is also reduced because of the envelope improvements. The median is reduced by 2 feet, the lower quartile by 3.7 feet, and the lower whisker by 8.3 feet. The upper bound for borehole depth is fixed around 443 feet, which is due to practical constraints and limitations set in GHEDesigner.

By multiplying the borehole count (non-normalized) by the borehole depth, we can approximate the total ground heat exchanger loop length. We see that the median building can save nearly 11,000 feet (23.4% reduction) of drilling by implementing envelope measures combined with their GHP, saving drilling time, cost, and resources. Buildings at the upper whisker (likely large buildings with substantial loads) can reduce the size of the ground heat exchanger loop by 73,000 feet (17.5% reduction) by improving their envelope.

Based on these findings, we can expect about 15-25% reduction in the number of boreholes and total length of the ground heat exchanger loop when combining the GHP measures with the high efficiency envelope upgrades. Of course, each individual building's results will vary based on climate zone, building type, building loads, etc. This will be explored in subsequent plots.

Figure 12. Ground heat exchanger sizing comparison of Comprehensive GHP package and Comprehensive GHP +High Efficiency Envelope package

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95005.yaml
     source: 95005_images/image_000015_a9de057c2c1d24a65e94f11e54ed2d5efc14184b492612b78f85b93b2056c9dd.png
     method: vision-description
     described: 2026-08-21 -->

![Three-panel box plot of borehole count, borehole depth and total ground heat exchanger length](95005_images/image_000015_a9de057c2c1d24a65e94f11e54ed2d5efc14184b492612b78f85b93b2056c9dd.png)

Figure 12: three stacked box-plot panels comparing the Comprehensive GHP and GHP + High Efficiency Envelope packages on normalized borehole count (0 to 13 per thousand ft2), average borehole depth (360 to 440 ft) and total ground heat exchanger length (0 to 400K ft). Every distribution shifts down with the envelope. Section 5.8.1 gives median reductions of 0.3 boreholes, 2 ft, and nearly 11,000 ft of drilling.

The sizing of the ground heat exchanger by GHEDesigner is a complex calculation that is dependent on the annual building load, but it also considers the long-term ground temperature stability over many years of operation. Therefore, the normalized borehole count can vary greatly from building to building. Figure 13 shows the normalized borehole count by building type. As shown, the building type, and thus the energy intensity of the building, contributes heavily to the size of the ground heat exchanger. High energy intensity buildings like hospitals and restaurants are going to require far more boreholes per square foot of floor area compared to warehouses. For all building types, the addition of the envelope measures reduces the normalized borehole count.

Figure 13. Normalized borehole count by building type for the Comprehensive GHP package and Comprehensive GHP + High Efficiency Envelope package

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95005.yaml
     source: 95005_images/image_000016_e6405aaebe3df6935d91474f385c257cc8552282de40aba49af1c829d811ceeb.png
     method: vision-description
     described: 2026-08-21 -->

![Box plots of normalized borehole count by building type for the two GHP packages](95005_images/image_000016_e6405aaebe3df6935d91474f385c257cc8552282de40aba49af1c829d811ceeb.png)

Figure 13: box-and-whisker plot of normalized borehole count (boreholes per thousand ft2, x-axis 0 to 30) grouped by building type - Food Service, Healthcare, Lodging, Education, Office, Mercantile, and Warehouse and Storage - with one row per package. Food Service needs the most and Warehouse and Storage the fewest; the envelope package is lower in every group, per Section 5.8.1.

Similarly, climate zones also have a big impact on ground heat exchanger size. GHEDesigner sizes the ground heat exchanger such that the ground temperature remains stable within certain bounds over the assumed 20-year lifespan of the system. If a building is rejecting far more heat to the ground than it is extracting, or vice versa, the ground heat exchanger will need to be larger to prevent the ground temperature from shifting over time. We can see this illustrated in Figure 14, in which the moderate climates (with a more even balance of heating and cooling load throughout the year) result in the lowest borehole count. In climates 3 through 5 for the Comprehensive GHP scenario, the median building requires 0.7-1.3 boreholes per thousand square feet of floor area.

The hot climates, which reject heat to the ground for much of the year, show larger ground heat exchanger requirements (median of 6 boreholes per thousand square feet in climate zone 1 for the Comprehensive GHP scenario). The cold climates, especially Subarctic climate zone 8, show much larger ground heat exchanger requirements than the other climate zones (median of 44 boreholes per thousand square feet for Comprehensive GHP scenario). Buildings in this climate are using heating energy for much of the year and extracting a lot of heat from the ground, which is already 50°F-55°F (10°C-13°C) to begin with. For this reason, a building in climate zone 8 may require a much larger ground heat exchanger than an identical building in a moderate climate.

However, GHPs are still advantageous in cold climates due to their relatively stable source temperatures, resulting in consistent performance year-round. In all climate zones, we can see that the addition of the envelope measures reduces the required ground heat exchanger size. This effect is especially pronounced in the coldest climates, where the package with envelope measures has a substantial impact (in climate zone 8, the median building's ground heat exchanger is reduced by 15.8 boreholes per thousand square feet).

Figure 14. Normalized borehole count by climate zone for the Comprehensive GHP package and Comprehensive GHP + High Efficiency Envelope package

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95005.yaml
     source: 95005_images/image_000017_1377297918793e04cd201734706d45a16aefb6eaff291b11dc96714514417072.png
     method: vision-description
     described: 2026-08-21 -->

![Box plots of normalized borehole count by climate zone for the two GHP packages](95005_images/image_000017_1377297918793e04cd201734706d45a16aefb6eaff291b11dc96714514417072.png)

Figure 14: box-and-whisker plot of normalized borehole count (boreholes per thousand ft2, x-axis 0 to 300) grouped by climate zone 1 through 8, with one row per package. The moderate zones 3 through 5 need the fewest boreholes and subarctic zone 8 by far the most - Section 5.8.1 gives a zone 8 median of 44 against 0.7-1.3 in zones 3 through 5.

