<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89042.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/89042.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/89042.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89042.md | section: 5.6  Other Findings | lines: 798-879 -->
## 5.6  Other Findings

This section includes additional and more detailed findings specific to the standard performance HP-RTU measure that are not covered in the previous sections. Figure 17 shows the rated and (annual average) operating COPs from all models (represented with a box plot excluding outliers) between advanced and standard performance scenarios. Based on operating performance differences (especially part-load performances) depicted in Figure 8, the stock level operating COPs are consistently lower in standard performance HP-RTUs compared to advanced HP-RTUs (leveraging variable speed compressors), as shown in Figure 17.

Operating heating COPs, including the impact of defrost and backup electric resistance heating energy, decrease more in colder climates. However, from the minimum bound perspective, the majority of the standard performance HP-RTUs' overall heating COPs (including backup heating, crankcase heater electricity, and defrosting electricity) remain higher than 1 (i.e., better than electric resistance heating). Again, this reflects the average performance derivation described in Section 3.2.1.2 and the minimum operating (or lockout) temperature of 0 ° F (17.9 ° C) we implemented in our models.

Figure 17. Distributions between advanced and standard performance HP-RTU scenarios: COP

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000019_fa7a47daa361113c17f615d26ccfb1eaa04a3b6320058171628d63cd120160e4.png
     method: vision-description
     described: 2026-08-22 -->

![Box plots of rated and operating COP by state for the advanced and standard performance scenarios](89042_images/image_000019_fa7a47daa361113c17f615d26ccfb1eaa04a3b6320058171628d63cd120160e4.png)

Figure 17: grid of box plots comparing the advanced and standard performance scenarios, both with a 0 degrees F lockout, for Arizona, Texas, New York and Minnesota. Five columns give rated cooling COP, annual average operating cooling COP, rated heating COP, and annual average operating heating COP with and without backup heating. Standard performance sits lower in every column. See Section 5.6.

Again, the "rated" COPs (for both heating and cooling) shown in the figures above account only for compressor power and outdoor fan power. The rated COPs reported in this study may differ from those reported under the AHRI performance rating (i.e., the more commonly used definition of rated COP). This is because the AHRI COP calculation includes not only outdoor fan power but also supply air blower power.

Figure 18 shows the annual average cycling ratio in cooling operation for two different performance scenarios and under four different weather conditions. Cycling ratio represents cycling losses where higher average ratio means lower cycling losses. One other metric reflecting how hot the weather is throughout the year is also included in this figure: total hours above 65 ° F in a year. As shown in the figure, a standard performance unit with two stage cooling undergoes more frequent short cycling (i.e., efficiency loss) compared to the advanced unit with variable speed. As the weather conditions get hotter (i.e., toward Arizona), the annual average cycling ratio in both performance scenarios increases because the unit experiences hotter outdoor conditions more frequently.

Figure 18. Distributions between advanced and standard performance HP-RTU scenarios: COP

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000020_5bde6f633af10b8267bf3c4d92baf8388b9acdcec981890437aa45838396089d.png
     method: vision-description
     described: 2026-08-22 -->

![Box plots of cooling cycling ratio and annual hours above 65 F by state and performance scenario](89042_images/image_000020_5bde6f633af10b8267bf3c4d92baf8388b9acdcec981890437aa45838396089d.png)

Figure 18: grid of box plots over the same four states and two performance scenarios, but the two columns are annual average cooling cycling ratio (0 to 1) and total hours per year above 65 degrees F - not COP, despite the caption repeating Figure 17's. The standard performance unit shows a lower cycling ratio in every state. Section 5.6 discusses the operating behavior.

Figure 19 and Figure 20 are highlighting the median annual operating COPs for cooling and heating, respectively, across contiguous U.S. states. The heating operating COP in Figure 20 includes backup heating, defrosting electricity, and crankcase heater electricity. Compressor and outdoor fan powers are included in both heating and cooling operating COPs, but the blower fan power is not. These COP values represent median COPs of either advanced or standard performance HP-RTUs for stock of buildings in each state and reflect the performance difference depending on weather characteristics. The biggest differences in heating operating COP occur in warmer climates where variable speed is more beneficial. The same differences are only slightly notable in the coldest climates.

Figure 19. Annual operating median cooling COP between contiguous U.S. states

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000021_35c76844ceb3d8ebd0dfd84632f24bbc81cbea698cb0d9f230c3964abe1c4a2d.png
     method: vision-description
     described: 2026-08-22 -->

![Two US state choropleth maps of median annual operating cooling COP, advanced versus standard](89042_images/image_000021_35c76844ceb3d8ebd0dfd84632f24bbc81cbea698cb0d9f230c3964abe1c4a2d.png)

Figure 19: paired choropleth maps of the contiguous United States shading each state by median annual operating cooling COP, advanced performance on the left and standard performance on the right, on a shared 3.1 to 5.1 scale. Advanced performance reaches 4.2 to 4.8 across the north while standard performance holds near 3.3 to 3.8 nationwide. Section 5.6 discusses.

Figure 20. Annual operating median heating COP between contiguous U.S. states

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000022_d2e7fc03c3779ff8fe6687d8975ed465be8f7087eb1592807085ac4ff877b389.png
     method: vision-description
     described: 2026-08-22 -->

![Two US state choropleth maps of median annual total operating heating COP including backup heat](89042_images/image_000022_d2e7fc03c3779ff8fe6687d8975ed465be8f7087eb1592807085ac4ff877b389.png)

Figure 20: paired choropleth maps of median annual total operating heating COP including backup heating, advanced performance on the left and standard performance on the right, on a shared 1.5 to 4.3 scale. Values fall with heating severity, from roughly 3.6 in the south to 2.0 in the northern tier, and standard performance is lower in every state. See Section 5.6.

Figure 21 shows the state-level peak power implications (using normalized peak metric of W/ft ² ) between three different scenarios: baseline, advanced performance HP-RTU, and standard performance HP-RTU. As can be expected, an increased winter peak due to fuel switching of gas heating systems is illustrated in Figure 21. A consistent decrease in summer peak leveraging relatively higher COP (compared to older units in reality) is also shown in Figure 21.

Figure 21. Distributions among all scenarios: peak power intensity

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000023_8ac4138d520c4333b156755460fc29ad7e7c7d1f397910dee268da09729479b5.png
     method: vision-description
     described: 2026-08-22 -->

![Box plots of peak power intensity by season, state and scenario in watts per square foot](89042_images/image_000023_8ac4138d520c4333b156755460fc29ad7e7c7d1f397910dee268da09729479b5.png)

Figure 21: grid of box plots of peak power intensity in watts per square foot, three columns for the shoulder, summer and winter peaks and rows for Minnesota, New York, Texas and Arizona, each row holding baseline, advanced performance and standard performance under a 0 degrees F lockout. Winter peaks shift up most under both HP-RTU scenarios. Section 5.6 discusses peak impacts.

Figure 22 shows the peak power timing implications between three different scenarios: baseline, advanced performance HP-RTU, and standard performance HP-RTU. Fuel switching of gas heating system shifts the peak to an earlier time in colder regions, which is often when outdoor air temperatures are coldest and when commercial buildings are warming up in the morning from an unoccupied evening time with setback temperature set points. Peak timing differences in the shoulder and summer seasons are less noticeable compared to the winter peak timing shift. Future research regarding the results shown in Figure 22 should examine better controls of thermostats (e.g., relaxed or delayed thermostat set point change) when using heat pumps to mitigate the morning peak happening in colder climates.

Figure 22. Distributions among all scenarios: peak power timing

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000024_48207e8cef2ae98aed5ccac4d34e0e8e99e23e5ca8e377252f4be38c67d3c6ab.png
     method: vision-description
     described: 2026-08-22 -->

![Box plots of peak timing by season, state and scenario, in hour of the day](89042_images/image_000024_48207e8cef2ae98aed5ccac4d34e0e8e99e23e5ca8e377252f4be38c67d3c6ab.png)

Figure 22: grid of box plots of peak timing expressed as hour of the day from 0 to 24, three columns for the shoulder, summer and winter peaks and rows for Minnesota, New York, Texas and Arizona, comparing baseline against the advanced and standard performance scenarios. Summer peaks stay near mid-afternoon while winter peaks sit earlier in the day. Section 5.6 discusses.

