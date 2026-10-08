<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86199.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86199.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/86199.md | section: 4.2.6  Heat Pump Set Point | lines: 567-615 -->
## 4.2.6  Heat Pump Set Point

Heat pumps have a lower hot water temperature output than boilers. There are some CO2 refrigerant heat pump water heaters that supply hot water up to 180°F [11], but most of the commercially available heat pumps have a hot water supply temperature capped at around 140°F. The hot water supply temperature they generate also depends on the outdoor air temperature. Figure 6 and Figure 7 show operation maps of heat pumps by Trane and Mitsubishi. For the Trane unit, the hot water leaving temperature drops from 140°F at an outdoor air temperature of 70°F to 100°F at an outdoor air temperature of 0°F. The Mitsubishi unit maintains a hot water set point even at colder temperatures; it supplies 158°F hot water at an outdoor air temperature as low as -4°F and drops to 150°F at -13°F.

Taking the performance of the Mitsubishi unit into consideration, the measure assumed the heat pump can provide the requested hot water supply temperature all the way to the cutoff temperature.

Figure 6. Operating map for ACX heat pump by Trane Figure from [2]

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86199.yaml
     source: 86199_images/image_000007_9d976226315d7817a3a3d181fd7cdfb3529a60bc84acbc07601303f1121e743e.png
     method: vision-description
     described: 2026-08-21 -->

![Operating envelope of the Trane ACX heat pump, hot water leaving temperature vs ambient temperature](86199_images/image_000007_9d976226315d7817a3a3d181fd7cdfb3529a60bc84acbc07601303f1121e743e.png)

Figure 6: operating map for the Trane ACX heat pump, hot water leaving temperature 60 to 160F against ambient temperature -10 to 100F. A red envelope marks ACX full load on R410A, topping out near 140F leaving water between about 50F and 90F ambient; a green band below 80F leaving water marks where 25% glycol is required. Reproduced from reference 2.

Figure 7. Operation map for Mitsubishi Ecodan ASHP Figure from [10]

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86199.yaml
     source: 86199_images/image_000008_879d10bd373f0577436b98ee6660d4ae4875f0f2ad518df6c6628257c1116d29.png
     method: vision-description
     described: 2026-08-21 -->

![Operating envelope of the Mitsubishi Ecodan ASHP, outlet water temperature vs outdoor temperature](86199_images/image_000008_879d10bd373f0577436b98ee6660d4ae4875f0f2ad518df6c6628257c1116d29.png)

Figure 7: operation map for the Mitsubishi Ecodan ASHP, outlet water temperature 0 to 80C against outdoor temperature -30 to 45C. The envelope allows roughly 25C to 70C leaving water above -20C outdoor, narrows into a hatched band below -20C, and steps its minimum down to about 25C between 0C and 45C. Reproduced from reference 10.

From an energy use perspective, if the existing coil sizes are big enough, using a lower hot water set point is recommended. Figure 8 shows ASHRAE's recommended minimum COPs for different hot water set points [12].

Figure 8. American National Standards Institute (ANSI)/ASHRAE/Illuminating Engineering Society (IES) 90.1-2021 minimum heating COPs

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86199.yaml
     source: 86199_images/image_000009_1d5a487534488a78f815176dec3e52d707188b69c75948dbfcad9ba86e33898a.png
     method: vision-description
     described: 2026-08-21 -->

![Line chart of ASHRAE 90.1-2021 minimum heating COP requirements at 47F and 17F outdoor air](86199_images/image_000009_1d5a487534488a78f815176dec3e52d707188b69c75948dbfcad9ba86e33898a.png)

Figure 8: line chart titled Minimum COP Requirement, COP on the y-axis 0 to 3.5 against leaving water temperature 105 to 140F, with one line per rating condition. At 47F outdoor air the minimum falls from 3.28 to 2.31; at 17F it falls from 2.05 to 1.50. Section 4.2.6 applies these ANSI/ASHRAE/IES 90.1-2021 minima.

We have provided two options in the measure for assigning a hot water set point: original set point or new set point.

- Original set point: The existing hot water loop set point will be used as a set point for the heat pump and the hot water loop.

- New set point: The user-assigned new set point value will be used for the heat pump and hot water loop.

When the set point is changed, it will have an impact on the downstream coils connected to the heat pump. More flow needs to be supplied by the pump to handle the same heating load with a lower set point. To accommodate this change, the measure provides an option to auto-size the heating coil. If users choose to auto-size, the measure will auto-size the overall heat transfer coefficient and maximum water flow rate of the values of the coil.

