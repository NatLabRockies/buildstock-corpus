<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95005.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95005.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95005.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/95005.md | section: 5.5 Site Energy Savings Distributions | lines: 861-908 -->
## 5.5 Site Energy Savings Distributions

This section discusses site energy consumption for quality assurance/quality control purposes. Site energy savings can be useful for these purposes, but other factors should be considered when drawing conclusions, as they do not necessarily translate proportionally to source energy savings, energy cost savings, or avoided emissions.

Figure 6 shows the percent savings distributions of the baseline ComStock models versus the Comprehensive GHP + High Efficiency Envelope package by end use and fuel type for applicable models. In other words, each data point in the distribution represents the percent energy savings between a baseline ComStock model and the corresponding upgrade model with measures applied.

Natural gas heating and other fuel heating show nearly 100% savings in most buildings as a result of converting the space heating load to electricity. As mentioned previously, some buildings such as warehouses and retail, maintain some gas-heated spaces after the GHPs are installed, which is why not all buildings show 100% savings for these end uses.

Electric heating savings are in the range of 50%-90% for most buildings. It is important to note that Figure 6 only shows buildings that started out with some amount of electric heating. Buildings that started with 100% natural gas heating would have an infinite increase in electric heating and are not shown in Figure 6. Therefore, the electric heating savings represent swapping out electric resistance heating with heat pumps that have a heating coefficient of performance of 3-5, combined with the envelope measures that further reduce HVAC loads. Some buildings show large negative electric heating savings. This represents buildings that started out with mostly gas heating but a small portion of electric resistance heating; they therefore show a large increase in electric heating when converting much of the heating load to electricity.

Cooling energy in applicable buildings decreased by 50%-70% in most buildings because of the replacement of existing air-cooled direct-expansion cooling systems with a more efficient groundcoupled system, combined with several envelope improvements. A small number of buildings experienced cooling penalties, which are mainly warehouses with very low cooling loads, making the percentage savings very sensitive to small changes in magnitude.

Pump energy increased by 10%-90% due to the added pumping demands of vertical GHP systems. Pumps represent a relatively small percentage of the overall stock energy (&lt;2%), so the high percent savings can be misleading. Fan electricity saw savings in 75% of buildings, while 25% saw an increase in fan energy. Many of the buildings with very large changes in fan energy were found to be warehouses, which start out with low HVAC loads and therefore percentage calculations are sensitive to small energy use changes. In addition, the system replacement results in a variety of changes that can affect fan energy, including lower supply temperatures, increase pumping energy, replacement and/or addition of fans. The median percent change in fan energy across the stock is around 25% savings.

The heat recovery end use showed nontrivial percentage changes in some buildings. However, this is solely based on the changes causing existing heat recovery systems to run for different amounts of time. The magnitude of this end use is minimal compared to total site energy.

Minimal or no differences are observed for service water heating systems, refrigeration, interior lighting, and interior equipment, as these systems are not directly impacted by the upgrade package. However, some buildings show minor changes due only to subtle differences in ambient air temperature that affect the operation of these systems.

Figure 6. Percent site energy savings distribution for ComStock models with the Comprehensive GHP + High Efficiency Envelope package applied by end use and fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95005.yaml
     source: 95005_images/image_000009_5f8f863cfeefd6f56ae1f86c6676017ecb3ac54d5c08f6f73ab816843d2cf2c3.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by end use and fuel type for the package](95005_images/image_000009_5f8f863cfeefd6f56ae1f86c6676017ecb3ac54d5c08f6f73ab816843d2cf2c3.png)

Figure 6: horizontal violin-and-box plot of percent site energy savings by end use and fuel type, x-axis -160% to 100%, titled Upgrade 56.0: Package_10 (unweighted), with model counts per row (electricity cooling n=108,799; natural gas heating n=56,499). The gas and other-fuel heating rows sit near 100% savings while electricity pumps and heat recovery carry long negative tails. Section 5.5 explains the distributions.

The data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

Figure 7 shows the percentage of total site energy savings by climate zone. A map of the ASHRAE climate zones is included in 0 [22]. There is a subtle trend of increased savings as we move from the hottest climate zone (1A - Hot Humid) to the coldest climate zone (8 - Subarctic). In warmest climate zones (1 through 3), the median building shows site energy savings around 25%-30%, with the 75 th percentile reaching around 40% site energy savings. In colder climate zones (5 through 7) we see median site energy savings up to 35%-40% with the 75 th percentile reaching 50% or more. This trend indicates that heating energy savings for this package is outpacing cooling energy savings, which is why the colder climates with heating dominated load see higher savings.

Some outliers across all climate zones show an increase in site energy with the package applied. Further investigation of these buildings revealed that large increases in fan and pump energy were the driving end uses behind the increased site energy consumption. With GHP systems, unless the building is rejecting and extracting the exact same amount of heat to and from the ground over the course of the year, the system could end up with an imbalanced load. This imbalanced load can result in increased pumping energy to maintain temperatures within the desired range for the heat pump condenser loop. Compressor heat can also exacerbate imbalanced loads. In climates with a more balanced heating and cooling load, the ground temperatures remain more stable through the year, and over the course of many years of operation.

Despite cold climates experiencing more significant air temperature swings throughout the year, the ground temperature stays relatively stable, resulting in consistent and efficient performance of GHPs year-round. Since cooling loads are present during most parts of the year in commercial buildings, cold climates tend to exhibit more balanced load profiles. GHPs can be more advantageous in climates with more balanced heating and cooling loads because of the long-term ground temperature implications on the ground heat exchange size.

Figure 7. Percent site energy savings by climate zone between the baseline and Comprehensive GHP + High Efficiency Envelope scenario

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95005.yaml
     source: 95005_images/image_000010_61b27d1c93000b00a392c23e24625ba535c4a8a8d2287f26189e6ee4db8cdecf.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by ASHRAE climate zone](95005_images/image_000010_61b27d1c93000b00a392c23e24625ba535c4a8a8d2287f26189e6ee4db8cdecf.png)

Figure 7: horizontal violin-and-box plot of percent site energy savings by ASHRAE climate zone, x-axis -100% to 80%, 15 rows from 1A (n=2,429) through 8 (n=509), same Upgrade 56.0: Package_10 (unweighted) title. Medians climb from the hottest zones to the coldest. Section 5.5 reports 25%-30% medians in zones 1 through 3 and 35%-40% in zones 5 through 7.

