<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86601.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86601.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86601.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/86601.md | section: 3.5.1  Heat Pump Rooftop Unit | lines: 544-551 -->
## 3.5.1  Heat Pump Rooftop Unit

Limited comprehensive heat pump performance maps exist, which are required for detailed energy modeling. Consequently, understanding of heat pump performance and operation in this work is also limited. Heat pump modeling is sensitive to performance assumptions due to the strong relationship between efficiency and capacity with outdoor air temperature. This impacts both annual energy consumption and peak demand. This work attempts to use the most informative data available and makes documented assumptions about heat pump operation and performance. These will notably impact results. Please consider these assumptions.

Stock savings are sensitive to ComStock baseline assumptions. Compared to CBECS 2012, which is another prominent data source for commercial building stock energy usage, ComStock currently shows lower gas heating consumption and higher electric heating consumption [11]. This can affect the net impact of converting both gas furnace and electric resistance RTUs to HPRTUs.

Lastly, there is a known EnergyPlus bug regarding cycling operation for multispeed coil objects. This can cause the modeled HP-RTU systems to cycle at higher part load fractions than the baseline single-speed RTU systems. Many units are only minimally impacted by this since the HP-RTU systems are variable speed and can turn down to lower part load fractions.

