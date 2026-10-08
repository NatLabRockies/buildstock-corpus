<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89481.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89481.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89481.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/89481.md | section: 5.1  Single Building Measure Tests | lines: 458-497 -->
## 5.1  Single Building Measure Tests

In this section, we describe the operation behavior of a small office building in Yellowstone Lake, WY, to demonstrate the measure scenario application on a single building. The baseline model uses packaged RTUs with direct expansion cooling and gas furnace heating. Outdoor ventilation air is provided directly through the RTUs. The HP-RTU measure is applied, which replaces the gas-fired RTUs with HP-RTUs as described in this report. The HP-RTUs are applied both with and without energy recovery for comparison.

Figure 5 illustrates RTU air temperatures for the HP-RTU with energy recovery scenario during a cold week in February. Outdoor air (blue) ranges from -25 ° F to 5 ° F. This is the temperature of outdoor ventilation air that enters the heat recovery section of the RTU. The air temperature after the energy recovery section (orange) increases roughly 25 ° F, varying based on temperature and flow conditions. The increased air temperature of the ventilation air during cold heating conditions reduces the heating load on the heat pump and electric resistance supplemental heating coils. Ultimately, the combined impact of the heating coils must ensure the supply air temperature (green) following the impact of mixing with return air and fan heat. Heat recovery reduces the electricity required to meet this target. Alternatively, the HP-RTU scenario without the energy recovery applied requires the heat pump and supplemental heat to cover a larger lift.

The outcome for this sample period is illustrated in Figure 6, where the HP-RTU scenario with no heat recovery (blue) shows higher site electricity consumption compared to the HP-RTU scenario with heat recovery applied (orange). These savings (in orange) are from the energy recovery reducing loads on the heating and cooling coils. Because this plot shows total building electricity, other end uses that are not impacted by the HVAC scenarios are included (e.g., lighting, plug loads), thereby showing a smaller impact than if only HVAC electricity were shown.

Figure 5 . Air temperatures for a HP -RTU with heat recovery applied

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89481.yaml
     source: 89481_images/image_000007_3372d7fe227fac55b0d8a1dc42a0b417da5948ee2284450d948eab883aea806b.png
     method: vision-description
     described: 2026-08-20 -->

![Time-series line chart of outdoor air, post-energy-recovery, and supply air temperatures for a heat pump RTU with heat recovery over a cold week in February](89481_images/image_000007_3372d7fe227fac55b0d8a1dc42a0b417da5948ee2284450d948eab883aea806b.png)

Figure 5 plots three air temperatures in degrees F against date and time for February 19-23, 2018, for the single-building example: a small office in Yellowstone Lake, Wyoming (ASHRAE climate zone 7) with the HP-RTU plus energy recovery scenario applied. Outdoor air temperature (blue) is the coldest trace, ranging from about -25 F to 5 F on a daily cycle; this is the outdoor ventilation air entering the heat recovery section of the RTU. Air temperature after the energy recovery section (orange) tracks above it, roughly 25 F warmer, varying with temperature and flow conditions, because building exhaust air has preheated it before it reaches the heating coils. Supply air temperature (green) is the highest and most sharply cycling trace, rising in tall square-topped pulses to roughly 100 F to 120 F during occupied heating periods and falling back to about 60 F to 70 F otherwise, reflecting mixing with return air, fan heat, and the heat pump plus electric resistance supplemental heating coils. The vertical gap between the outdoor and post-recovery traces is the heating load avoided by energy recovery; without it the heat pump and supplemental coils would have to cover a larger temperature lift.

Figure 6 . Total building electricity usage for HP -RTU scenario (blue) and HP -RTU with energy recovery scenario (orange)

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89481.yaml
     source: 89481_images/image_000008_0640683085927bf947f18204b7e14ff3877e73b916acf1590ab15166b01502d9.png
     method: vision-description
     described: 2026-08-20 -->

![Time-series comparison of total building site electricity consumption for the heat pump RTU with and without energy recovery over a cold February week](89481_images/image_000008_0640683085927bf947f18204b7e14ff3877e73b916acf1590ab15166b01502d9.png)

Figure 6 plots building site electricity consumption in Wh, on a 0 to 60,000 Wh axis, against date and time for February 19-23, 2018, for the same single small office example in Yellowstone Lake, Wyoming. Two traces are shown: site electricity with no recovery (blue) and site electricity with recovery (orange). Both follow the same daily pattern, with sharp morning startup spikes reaching roughly 45,000 to 50,000 Wh, an occupied plateau near 20,000 to 30,000 Wh, and overnight troughs near 10,000 Wh. The orange with-recovery trace sits at or below the blue no-recovery trace throughout, with the widest gaps at the morning peaks and during cold occupied periods; that difference is the electricity saved by energy recovery reducing loads on the heating and cooling coils. Because the plot shows total building electricity rather than HVAC electricity alone, end uses unaffected by the HVAC scenarios such as lighting and plug loads are included, which makes the proportional impact look smaller than an HVAC-only comparison would. For this model, Table 6 reports a 7% electricity reduction from adding energy recovery.

The HP-RTU with no energy recovery scenario ('HP-RTU, No ER') shows 42% site energy savings versus the baseline scenario that uses natural gas RTUs (Table 6). These savings are attributable to the combination of 100% natural gas savings, since this scenario electrifies natural gas heating, and 42% increase in electricity usage from transitioning to electric heating. When adding energy recovery ('HP-RTU, with ER'), we see a 7% reduction in electricity usage compared to the HP-RTU scenario without energy recovery. These savings are primarily due to reduced heating loads when using energy recovery. This model example is from a very cold climate (ASHRAE climate zone 7), so the impact may be higher than many other cases.

Table 6 . Annual Site Energy Comparison for Single Model Example Between the Baseline, HP -RTU With No ER (Energy Recovery), and HP -RTU With ER Scenarios Note that these results include the prevalence of electric resistance supplemental heating when the HP system is unable to meet the full heating load.

|                 |   Natural Gas (KBtu) |   Electricity (KBtu) |   Total Site Energy (KBtu) |
|-----------------|----------------------|----------------------|----------------------------|
| Baseline        |              855,869 |              526,304 |                  1,382,173 |
| HP-RTU, No ER   |                    0 |              807,095 |                    807,095 |
| HP-RTU, with ER |                    0 |              733,023 |                    733,023 |

