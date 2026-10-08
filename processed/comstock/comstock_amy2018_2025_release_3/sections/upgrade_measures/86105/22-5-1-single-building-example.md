<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86105.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86105.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86105.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/86105.md | section: 5.1  Single Building Example | lines: 339-355 -->
## 5.1  Single Building Example

Figure 9 shows a simulation example of an economizer installed in a building that previously did not have an economizer. In this example, outdoor air temperature varies between 32°F/0°C and 95°F/35°C throughout the year. Annual mechanical cooling energy savings were 2.6% for this example model (Figure 9 (a)) by leveraging free cooling during the times when outdoor air temperatures were below 50°F/10°C, as shown in Figure 9 (b) and (c). To note, savings potential of the economizer implementation heavily depends on the local climate, cooling needs, building's outdoor air requirement, heat gain level in the return air stream, and configuration of the economizer. From Figure 9 (c), it is easy to notice the relatively small-time window within three days where savings occur. These small-time windows disappear even more when weather is not favorable, the building does not need cooling, or the building already requires a high ventilation rate.

Figure 9. Simulation example of economizer implementation

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86105.yaml
     source: 86105_images/image_000014_76e31c393566984ca818da00d3ddd7ec0817ec16bf679fc0e1f0ceaaab443a9c.png
     method: vision-description
     described: 2026-08-21 -->

![Three-panel single-building example: a bar pair annotated 2.644% load difference, a scatter of mechanical cooling load against outdoor air temperature showing the upgrade cloud starting only above about 12 degrees C, and three days of transient traces for outdoor air temperature, outdoor air fraction and cooling load.](86105_images/image_000014_76e31c393566984ca818da00d3ddd7ec0817ec16bf679fc0e1f0ceaaab443a9c.png)

Figure 9 (Section 5.1, Single Building Example) demonstrates the measure on one model that previously had no economizer. Panel (a), "mechanical cooling load", is a bar pair on a 0-45 MWh/year axis: baseline about 40.6 and upgrade about 38.5, annotated "2.644% load difference", which corroborates the body's "2.6%". Panel (b), "changepoint temperature", scatters mechanical cooling load in W against outdoor air temperature from 0 to 35C for both scenarios. The baseline points fill the low temperature region, while the upgrade points appear only above roughly 11-12C: below that changepoint the economizer meets the load with free cooling and mechanical cooling drops out entirely. The x-extent corroborates the body's "between 32F/0C and 95F/35C", and the changepoint corresponds to its "below 50F/10C". Panel (c), "transient behavior", stacks three traces over 6-8 June 2023 with baseline and upgrade overlaid: outdoor air temperature (about 10-27C), outdoor air fraction (0 to 1), and cooling load (0 to about 20 kW). The upgrade holds the outdoor air fraction at 1 in sustained daytime blocks where the baseline cycles, and the cooling load traces are almost indistinguishable apart from brief upgrade drops to zero - the narrow savings windows the text points out.

It must be noted that other factors such as return on investment should also be considered to comprehensively assess the impact of this upgrade.

