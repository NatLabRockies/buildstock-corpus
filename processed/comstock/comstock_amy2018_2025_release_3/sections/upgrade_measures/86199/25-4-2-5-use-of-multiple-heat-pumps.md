<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86199.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/86199.md | section: 4.2.5  Use of Multiple Heat Pumps | lines: 559-566 -->
## 4.2.5  Use of Multiple Heat Pumps

In practice, it is more common to have multiple heat pumps of medium size than to have one big heat pump in a building. It creates redundancy and increases the energy efficiency of the system by providing the flexibility to run a few heat pumps at a higher part load ratio and with less cycling than running a big chiller. This measure allows users to provide the rated capacity of the heat pump they would like to use. The default heating capacity per unit used in the measure is 40 kW (136.5 MBH) and is based on Mitsubishi's Ecodan ASHP [10]. The measure adds multiple heat pumps in parallel when the estimated rated capacity is greater than the assumed rated capacity per unit. The number of ASHPs is estimated as:

where 'Roundup' is used to convert a fraction to the closest higher integer value.

If the estimated rated capacity is lower than the assumed rated capacity per unit, only one heat pump with the estimated rated capacity will be used in the model.

