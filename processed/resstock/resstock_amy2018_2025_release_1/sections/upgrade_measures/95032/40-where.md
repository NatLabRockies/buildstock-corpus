<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/95032.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/95032.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/95032.md | section: Where: | lines: 683-764 -->
## Where:

𝑓𝑓 𝑠𝑠 ( 𝑧𝑧 , 𝑡𝑡 ) : Undisturbed soil temperature at the depth of 𝑧𝑧 and time 𝑡𝑡 of the year in °C

𝛽𝛽

: Correction factor, unitless

𝑧𝑧

: Soil depth, in m or ft

𝑡𝑡

: Time of year, starting from January 1, in h

𝑡𝑡 𝑝𝑝

: Period of soil temperature cycle (365), in days

𝛼𝛼 𝑠𝑠 : Soil diffusivity, in 𝑚𝑚 2 / 𝑑𝑑𝑎𝑎𝑑𝑑 or 𝑓𝑓𝑡𝑡 2 / 𝑑𝑑𝑎𝑎𝑑𝑑

𝑓𝑓 𝑠𝑠 , 𝑓𝑓𝑎𝑎𝑒𝑒 : Annual average surface soil temperature of different depth and time, in °C or °F

𝑓𝑓 𝑠𝑠 , 𝑓𝑓𝑝𝑝𝑝𝑝𝑎𝑎𝑎𝑎𝑟𝑟𝐵𝐵𝑟𝑟𝑟𝑟 , 𝑓𝑓 ∶ 𝜋𝜋 𝑟𝑟ℎ order surface amplitude, which can be assumed to be half of the difference between the maximum and minimum monthly average temperatures in a year

𝑃𝑃𝑃𝑃 𝑓𝑓 : Phase angle of the annual soil temperature cycle, in radians

The input parameters for the model ( 𝑓𝑓 𝑠𝑠 , 𝑓𝑓𝑎𝑎𝑒𝑒 , 𝑓𝑓 𝑠𝑠 , 𝑓𝑓𝑝𝑝𝑝𝑝𝑎𝑎𝑎𝑎𝑟𝑟𝐵𝐵𝑟𝑟𝑟𝑟 , 1 , 𝑓𝑓 𝑠𝑠 , 𝑓𝑓𝑝𝑝𝑝𝑝𝑎𝑎𝑎𝑎𝑟𝑟𝐵𝐵𝑟𝑟𝑟𝑟 , 2 , 𝑃𝑃𝑃𝑃1 ,  and 𝑃𝑃𝑃𝑃2 ) were published for short and tall grass cover in Appendix A of the dissertation (Xing 2014). Parameters from the short grass table are used and would represent the boreholes being covered by short grass in a residential backyard. 18 Xing's Table A-3 provides model parameters for over 1,000 locations within the United States. Xing's Appendix Table A-3 is specific as a lookup file in OpenStudio-HPXML. Based on the latitude and longitude of the weather file, the nearest location in the table is chosen. During sizing, there are places where the ground temperature is estimated using the annual average outdoor air temperature (see the 'Ground Heat Exchanger Sizing Methodology' section, below) for calculating the required total length during sizing.

18 The short grass reference is to the appendix tables in Xing's thesis. The choices were short grass or long grass.

Figure 10. Xing's Appendix A-3 locations integrated into a lookup table for OpenStudio-HPXML

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/95032.yaml
     source: 95032_images/image_000008_b1a456a8c1eca543c81f5150d2eff7bcc6c401302d7a735081af76e30bcd6038.png
     method: vision-description
     described: 2026-11-11 -->

![Map of North America with a dot at each ground temperature site in Xing's Appendix A-3](95032_images/image_000008_b1a456a8c1eca543c81f5150d2eff7bcc6c401302d7a735081af76e30bcd6038.png)

Figure 10: dot map of North America on a street-map base. Each black dot is one site from Xing's Appendix A-3 lookup table of ground temperature model parameters. Dots cover the contiguous United States densely, most heavily in the Northeast, the Midwest and along the West Coast, with sparser coverage of Alaska, Canada, Hawaii, Mexico and the Caribbean. There are no axes, legend or values.

To show the values expected during simulations, the latitude and longitude locations for these data points were joined with the corresponding IECC 2012 climate zones. Figure 11 shows the distribution of annual average undisturbed ground temperatures from the Simplified Design Model and the data from Xing's Table A-3. Warmer climates have a higher undisturbed ground temperature than colder climates due to higher ambient air conditions throughout the year. Dryer climates (moisture zone B) also have higher ground temperatures than the corresponding moist (moisture zone A) and marine (moisture zone C) climates due to less moisture being in the soil. The median values from these distributions are presented in Table 3.

Figure 11. Annual average undisturbed ground temperatures from the Simplified Design Model (Xing 2014) by 2012 IECC climate and moisture zones 19

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/95032.yaml
     source: 95032_images/image_000009_68544727652b6af7cc6d1e1a93d0616e1fbf31d2ffa47da83fe33af2848ce710.png
     method: vision-description
     described: 2026-11-11 -->

![Box plots of annual mean undisturbed ground temperature by IECC 2012 climate and moisture zone](95032_images/image_000009_68544727652b6af7cc6d1e1a93d0616e1fbf31d2ffa47da83fe33af2848ce710.png)

Figure 11: box plots of annual mean undisturbed ground temperature. Y-axis is ground temperature in °C, about -2 to 27; x-axis is 17 IECC 2012 zones grouped by moisture regime: (A, 1A) to (A, 7A), (AK, 7AK), (AK, 8AK), (B, 2B) to (B, 7B), (C, 3C), (C, 4C). Medians fall from about 25°C in 1A to about 2°C in 8AK; 4B has the widest box. Table 3 lists the medians.

19  In IECC 2012, Alaska climate zones denoted 7AK and 8AK do not include a moisture zone.

Table 3. Short Grass Median Undisturbed Ground Temperatures by IECC 2012 Climate Zones, According to the Simplified Design Model and Site Locations in (Xing 2014)

[Climate zone map available: https://basc.pnnl.gov/images/iecc-climate-zone-map](https://basc.pnnl.gov/images/iecc-climate-zone-map)

| 2012 IECC Climate Zone   |   Annual Average Undisturbed Ground Temperature (°C) |
|--------------------------|------------------------------------------------------|
| 1A                       |                                                 25.9 |
| 2A                       |                                                 20.9 |
| 2B                       |                                                 25.0 |
| 3A                       |                                                 17.9 |
| 3B                       |                                                 19.7 |
| 3C                       |                                                 17.0 |
| 4A                       |                                                 14.7 |
| 4B                       |                                                 16.3 |
| 4C                       |                                                 13.3 |
| 5A                       |                                                 11.5 |
| 5B                       |                                                 12.9 |
| 6A                       |                                                  9.0 |
| 6B                       |                                                  9.3 |
| 7A                       |                                                  7.0 |
| 7AK                      |                                                  5.4 |
| 7B                       |                                                  6.5 |
| 8AK                      |                                                  2.3 |

