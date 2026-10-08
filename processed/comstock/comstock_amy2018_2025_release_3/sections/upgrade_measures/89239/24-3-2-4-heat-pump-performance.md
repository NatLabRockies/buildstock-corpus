<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89239.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89239.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89239.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/89239.md | section: 3.2.4  Heat pump performance | lines: 351-360 -->
## 3.2.4  Heat pump performance

The performance of each of the HeatPump:PlantLoop:EIR objects is characterized by three curves: a capacity modifier as a function of condenser water temperature and supply water temperature, an EIR modifier as a function of supply water temperature and condenser water temperature, and an EIR modifier as a function of part-load ratio. The part-load ratio is defined as the ratio of cooling load to steady-state capacity. These curves account for the effect of the condenser water supply temperature, supply water temperature set point, and part-load ratio on the heat pump's capacity and energy consumption. These performance curves are set based on the capacity of the heat pump selected.

The sizing approach for the ground heat exchanger is discussed in the Ground Loop and GHEDesigner Workflow documentation.

Performance curve values were evaluated based on tabular performance data available from Carrier's 61WG/30WG series for a water-to-water heat pump model sold in Europe [16]. The selected performance data reflect the use of glycol in the source side of the heat pump loop, consistent with our modeled scenario.

The required performance data were not available for water-to-water heat pumps in this size range (30-90 tons) currently sold in the United States. The Carrier model was selected because it falls in the desired capacity range, and performance data for our desired range of source- and load-side temperatures were available. While the 61WG/30WG models are representative of a commercially available water-to-water heat pump, refining the performance data is a potential area for future work.

