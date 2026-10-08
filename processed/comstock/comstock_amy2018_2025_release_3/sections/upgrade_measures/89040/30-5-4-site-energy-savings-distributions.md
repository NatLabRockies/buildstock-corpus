<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89040.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89040.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89040.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/89040.md | section: 5.4  Site Energy Savings Distributions | lines: 571-633 -->
## 5.4  Site Energy Savings Distributions

This section discusses site energy consumption for quality assurance/quality control purposes. Note that site energy savings can be useful for these purposes, but other factors should be considered when drawing conclusions, as these do not necessarily translate proportionally to source energy savings, greenhouse gas emissions avoided, or energy cost.

Figure 10 and Figure 11 show the percent and site end-use intensity savings distributions, respectively, of the baseline ComStock models versus the upgrade scenario by end use and fuel type for applicable models. Percent savings provide relative impact of the measure at the individual building level, while site end-use intensity savings provide absolute (or aggregated) scale of impact. Also, the data points that appear above some of the distributions indicate outliers in the distribution, meaning they fall outside 1.5 times the interquartile range. The value for n indicates the number of ComStock models that were applicable for energy savings for the fuel type category.

Figure 10. Percent site energy savings distribution for ComStock models with the VRF DOAS upgrade applied by end use and fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89040.yaml
     source: 89040_images/image_000017_4a302b3496be3783db70d37616b16be8c665d1bbbeb4449d4d75f40b9c8ab7a9.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of percent site energy savings by end use and fuel type](89040_images/image_000017_4a302b3496be3783db70d37616b16be8c665d1bbbeb4449d4d75f40b9c8ab7a9.png)

Figure 10: horizontal violin-and-box plots titled Upgrade 06: VRF with 25pct Upsizing Allowance (unweighted), percent site energy savings from -160% to 100% with fifteen end-use and fuel rows labeled by model count. Natural gas heating (n=162,422) clusters near 100% savings while electricity heating (n=220,233) and heat recovery (n=221,115) carry long negative tails. Section 5.4 explains the penalties.

Figure 11. Site end-use intensity (EUI) savings distribution for ComStock models with the VRF DOAS upgrade applied by end use and fuel type

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89040.yaml
     source: 89040_images/image_000018_42356f9251017babe4734299fbc9ddb1a6380619076a0b01e0240ab08675ccf6.png
     method: vision-description
     described: 2026-08-21 -->

![Violin and box plots of site EUI savings by end use and fuel type in kBtu per square foot](89040_images/image_000018_42356f9251017babe4734299fbc9ddb1a6380619076a0b01e0240ab08675ccf6.png)

Figure 11: the same fifteen end-use and fuel rows as Figure 10 plotted as site EUI savings in kBtu/ft2 on an x-axis from -150 to 300. Every distribution collapses toward zero except electricity heating (n=220,233), which spreads across the full range - the large percentage swings are small in absolute intensity. Section 5.4 reads the two figures together.

Similar conclusions from the previous VRF DOAS analysis can be drawn from Figure 10 and Figure 11. Highlights of the savings reflected in the two figures include:

- Electrification of combustion fuel-based heating:
- o Up to 100% savings on combustion fuel used for heating. Data points showing savings less than 100% are buildings with multiple HVAC systems and where the upgrade is only applicable to some of those systems.
- Conversion of electric resistance heating to VRF heating:
- o Positive savings on electricity used for heating.
- Higher cooling COP of VRF (compared to baseline direct expansion systems):
- o Positive savings on electricity used for cooling.
- Converting hydronic system (e.g., chiller) to VRF:
- o Positive savings on electricity used for pumps.
- o Positive savings on electricity used for heat rejection (i.e., removal of cooling towers). Not always 100% savings because the applicability criteria with space type can result in buildings (after the upgrade) with existing HVAC system (e.g., VAV, chiller, and cooling tower) still serving a portion of the building.

- Decoupling of ventilation with DOAS:
- o Positive savings on electricity used for fans due to VRF indoor fans only operating on sensible cooling needs.
- o Negative electricity cooling savings in moderate climate zones (e.g., California). This is due to the cooling coil in the DOAS operating based on outdoor air temperature reset control; thus, when the cooling load is less for a building, it can still provide conditioned air while the baseline system will only operate based on the load (i.e., controlled by space thermostat set point). However, these data points are mostly outliers and the overall impact is small, as shown in Figure 11.
- DOAS with heat or energy recovery ventilator (H/ERV) :
- o Negative savings on electricity used for heat recovery. These are buildings that originally included heat recovery and where the DOAS upgrade added a bigger heat recovery system; thus, bigger fans and higher static pressure.
- Others:
- o The change in electricity used for refrigeration is due to a new HVAC system affecting the space condition (e.g., temperature/humidity) that affects the refrigeration system's performance. The absolute impact is small, as shown in Figure 11.
- o Data points showing extreme (e.g., -150% electricity cooling savings) positive/negative savings are (1) buildings either in very hot or very cold climates, (2) where absolute heating or cooling demand is small, and (3) even small changes (due to upgrade) in heating or cooling demand (e.g., megawatt-hours) resulting in large relative (e.g., percent) savings. The absolute impact of these data points is small, as shown in Figure 11.
- o More detailed findings related to H/ERV can be found in the measure documentation of H/ERV upgrade.

Figure 12 shows the comparison of the ComStock baseline and the two upgrade scenarios (regular sizing and 25% upsizing allowance) in terms of the peak demand and timing changes. The differences between the two upgrade scenarios are not noticeable in terms of peak demands. The winter peak demand (in kilowatts per building floor area) increases in the colder regions in both sizing scenarios, and the peak timings of the heating demand shift to earlier in the day due to morning heating demands (covered by the VRF electric heating) in the winter season. The peak demand for cooling is reduced (from baseline) across all regions due to higher cooling COP used in VRF and energy recovery and the peak timing remaining similar.

Figure 12. Comparison of the ComStock baseline and the upgrade scenario in terms of peak demand change

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89040.yaml
     source: 89040_images/image_000019_8e63e1791d7801484753b297fe2677b0a96118a53ec96f8eec7f5a6a8a5ed448.png
     method: vision-description
     described: 2026-08-21 -->

![Grid of box plots of summer and winter peak timing and demand by climate zone for three cases](89040_images/image_000019_8e63e1791d7801484753b297fe2677b0a96118a53ec96f8eec7f5a6a8a5ed448.png)

Figure 12: a grid of box plots by ASHRAE climate zone in four columns - summer peak timing (hour of day), summer peak demand (W/sqft), winter peak timing and winter peak demand - with three rows per zone for the baseline, VRF with regular sizing and VRF with 25pct upsizing allowance. Peak timing barely moves while demand medians shift down slightly. Section 5.4 discusses peak impacts.

