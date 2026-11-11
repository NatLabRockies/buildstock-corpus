<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96413.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96413.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96413.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96413.md | section: 1.2.8  Measure Upgrade Specification Process | lines: 234-261 -->
## 1.2.8  Measure Upgrade Specification Process

The intent of this ASHP measure upgrade is to reflect the specifications of a typical cold climate ASHP based on the median cold climate ASHP found on the NEEP database (Northeast Energy Efficiency Partnerships, Inc. 2023). The NEEP database specifies an ASHP as cold climate if its HSPF2 ≥ 7.7 and SEER2 ≥ 14.3, it is variable speed, and its COP at 5°F ≥ 1.75 at maximum capacity. In an analysis of all ducted ASHP systems on NEEP, the plurality of systems have an HSPF2 between 8.5 and 9.0. Figure 1 shows the histogram of this analysis (Winkler, et al. 2026).

Figure 1. Histogram of NEEP ASHP analysis

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/96413.yaml
     source: 96413_images/image_000002_1fa65a8bcf6b1a5498616801f3aae708bc78b9e08e11cadfa275d44d5e6d2d8e.png
     method: vision-description
     described: 2026-11-11 -->

![Histogram of NEEP ducted air-source heat pumps by HSPF2 (Region IV)](96413_images/image_000002_1fa65a8bcf6b1a5498616801f3aae708bc78b9e08e11cadfa275d44d5e6d2d8e.png)

Figure 1: histogram of the ducted air-source heat pumps in the NEEP database by HSPF2 (Region IV). X-axis is HSPF2 from 7.0 to 12.0 in bins of 0.5; y-axis is the fraction of systems, 0 to 0.25. The 8.5 to 9.0 bin is the tallest at about 0.24, followed by 8.0 to 8.5 at about 0.16; very few systems are rated above 10.0.

To define a 'Typical Cold Climate ASHP,' the NEEP database entries with the median HSPF value of 8.5 HSPF2 were identified and the median values of those entries for COP at max speed, COP at min speed, capacity at max speed, capacity at min speed were found (Winkler, et al. 2026). These results are shown in Figure 2. These details are used as inputs into the ResStock model using the HVAC Detailed Performance Archetype option. Refer to Section 3 for more information on how this measure upgrade is modeled.

Figure 2. Median values of heat pumps with an HSPF2 of 8.5 for COP at max speed, COP at min speed, capacity at max speed, capacity at min speed were found

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/96413.yaml
     source: 96413_images/image_000003_5a69086fab892d45ab18da2baadf6e222b2d13939b4bd6b30774a2dbd9a0959d.png
     method: vision-description
     described: 2026-11-11 -->

![Four panels of NEEP heat pump capacity ratio and COP against outdoor temperature, with medians](96413_images/image_000003_5a69086fab892d45ab18da2baadf6e222b2d13939b4bd6b30774a2dbd9a0959d.png)

Figure 2: four-panel line chart of NEEP database entries against outdoor temperature (°F, about -20 to 47), with the median in orange. Panels are maximum and minimum capacity as a ratio of rated capacity at 47°F (0 to 2.0) and COP at maximum and minimum speed (0 to 7). Median maximum capacity rises from about 0.5 at the coldest point to about 1.0 at 47°F. See Table 4.

