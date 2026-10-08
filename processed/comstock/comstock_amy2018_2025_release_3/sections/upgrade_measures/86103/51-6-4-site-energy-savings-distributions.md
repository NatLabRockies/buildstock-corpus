<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86103.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/86103.md | section: 6.4  Site Energy Savings Distributions | lines: 891-951 -->
## 6.4  Site Energy Savings Distributions

This section discusses site energy consumption for quality assurance/quality control purposes. Note that site energy savings can be useful for these purposes, but other factors should be considered when drawing conclusions, as these do not necessarily translate proportionally to source energy savings, greenhouse gas emissions avoided, or energy cost. Figure 16 and Figure 17 show the percent and site end-use intensity (EUI) savings distributions, respectively, of the baseline ComStock models versus the upgrade scenario by end use and fuel type for applicable models. Percent savings provide relative impact of the measure against each end use and fuel type while site EUI savings provide absolute scale of impact.

Figure 16. Percent site energy savings distribution for ComStock models with the upgrade measure applied by end use and fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000023_653dce8b4a1742de9b9ea36be68abc27514ae130d4176a6bc50b9cede1008e3e.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 16: violin plots of percent site energy savings by end use and fuel](86103_images/image_000023_653dce8b4a1742de9b9ea36be68abc27514ae130d4176a6bc50b9cede1008e3e.png)

Figure 16: horizontal violin plots of percent site energy savings (axis -160% to 100%) for sixteen end-use and fuel combinations, each row labeled with its unweighted model count. Natural gas heating (n=172,830) concentrates near 100% savings while electricity heat recovery (n=233,966) spreads far negative from the added DOAS fan energy. Drivers are itemized in Section 6.4.

Figure 17. Site EUI savings distribution for ComStock models with the upgrade measure applied by end use and fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000024_b3f619ed3ed57d52f13434ada1fdc431913e6f9e8c1b7f4a2c9f0818125e847c.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 17: violin plots of site EUI savings by end use and fuel, kBtu/ft2](86103_images/image_000024_b3f619ed3ed57d52f13434ada1fdc431913e6f9e8c1b7f4a2c9f0818125e847c.png)

Figure 17: horizontal violin plots of site EUI savings (kBtu/ft2, axis -100 to 500) across the same sixteen end-use and fuel intensity rows as Figure 16, unweighted with model counts in each label. Most distributions cluster near zero; natural gas heating and electricity heating carry the long positive tails. The absolute view puts Figure 16's percentages in context. See Section 6.4.

Highlights of the savings reflected in Figure 16 and Figure 17 include the following:

- -Electrification of combustion fuel-based heating:
- o Up to 100% savings on combustion fuel used for heating.
- -Conversion of electric resistance heating to VRF heating:
- o Positive savings on electricity used for heating.
- -Higher cooling COP of VRF:
- o Positive savings on electricity used for cooling.
- -Converting hydronic system (e.g., chiller) to VRF:
- o Positive savings on electricity used for pumps.
- o Positive savings on electricity used for heat rejection (i.e., removal of cooling towers). Not always 100% savings because the applicability criteria with space type can result in buildings (after the upgrade) with existing HVAC system (e.g., VAV, chiller, and cooling tower) still serving a portion of the building.

- -Decoupling of ventilation with DOAS:
- o Positive savings on electricity used for fans due to VRF indoor fans only operating on sensible cooling needs.
- -DOAS with HRV/ERV:
- o Negative savings on electricity used for heat recovery with more fans in DOAS and higher static pressure, causing more fan energy.
- -Others:
- o The change in electricity used for refrigeration is due to a new HVAC system affecting the space condition (e.g., temperature/humidity) that affects the refrigeration system's performance. The absolute impact is small as shown in Figure 17.
- o Datapoints showing extreme (e.g., -120% natural gas heating savings) positive/negative savings are (1) buildings either in very hot or very cold climates, (2) where absolute heating or cooling demand is small, and (3) even small change (due to upgrade) in heating or cooling demand (e.g., MWh) resulting in large relative (e.g., %) savings. The absolute impact of these datapoints is small as shown in Figure 17.
- o Relative percent savings shown for electricity used for interior lighting is due to a small bug in ComStock, but the absolute impact of these datapoints is small, as shown in Figure 17, and overall impact is negligible, as shown in Figure 14.
- o More detailed findings related to DOAS with H/ERV can be found in the measure documentation of H/ERV upgrade.

Figure 18 shows the comparison of the ComStock baseline and the upgrade scenario in terms of the peak demand and timing changes. As shown in the figure, the winter peak demand (in kilowatts per building floor area) increases in the colder regions with this electrification measure, and the peak timings of the heating demand shift to earlier in the day due to morning heating demands (covered by the VRF electric heating) in winter season. On the other hand, as electricity is being more used for heating in hotter regions, converting electric resistance heating to more efficient VRF heat pump heating reduces winter peak demand. The peak demand for cooling is reduced across all regions due to higher cooling COP used in VRF and the peak timing remained similar.

Figure 18. Comparison of the ComStock baseline and the upgrade scenario in terms of peak demand change

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000025_cffcae1e13013a32061952420e02302a936fc7dd09d2a7dac7826c79ad1e9a1e.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 18: box plots of summer and winter peak timing and demand by climate zone](86103_images/image_000025_cffcae1e13013a32061952420e02302a936fc7dd09d2a7dac7826c79ad1e9a1e.png)

Figure 18: grid of box plots with rows for eight climate zones, each split into ComStock baseline and VRF with DOAS, and four metric columns: summer peak timing (hour of day), summer peak demand (kW/sq ft), winter peak timing, and winter peak demand. Winter peak demand shifts upward in the colder zones under this electrification measure. See Section 6.4.

