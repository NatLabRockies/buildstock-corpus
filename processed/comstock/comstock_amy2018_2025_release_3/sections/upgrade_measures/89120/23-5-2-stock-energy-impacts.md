<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89120.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89120.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89120.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/89120.md | section: 5.2  Stock Energy Impacts | lines: 285-323 -->
## 5.2  Stock Energy Impacts

The Improved Fan Scheduling and Outdoor Air Control measure demonstrates 3.5% total site energy savings (150 TBtu) for the U.S. commercial building stock modeled in ComStock (Figure 4). The savings are primarily attributed to:

- 11% stock fan savings (58.3 TBtu).
- 7.2% stock heating electricity savings (12.7 TBtu)
- 5.6% stock heating gas savings (50.5 TBtu)
- 2.7% stock cooling savings (18.3 TBtu).

Figure 4. Comparison of annual site energy consumption between the ComStock baseline and the Improved Fan Scheduling and Outdoor Air Control measure scenario across the building stock Energy consumption is categorized both by fuel type and end use.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89120.yaml
     source: 89120_images/image_000011_dfd2c001200fe30cd0e8057dc9c03dee94e368f8b83e7e097049b7f01f5ce3b4.png
     method: vision-description
     described: 2026-08-20 -->

![Two stacked bars comparing whole-stock annual site energy consumption in TBtu by end use and fuel between the ComStock baseline and the measure scenario](89120_images/image_000011_dfd2c001200fe30cd0e8057dc9c03dee94e368f8b83e7e097049b7f01f5ce3b4.png)

Figure 4. Two stacked vertical bars for the whole modeled U.S. commercial building stock. The y axis is 'Annual Energy Consumption (TBtu)', ticked 0 to 4500. The left bar 'Baseline' totals 4,338 TBtu and the right bar 'Unoccupied AHU Control' totals 4,188 TBtu, a 150 TBtu (3.5%) reduction. Labeled segments, baseline then measure: Interior Equipment Electricity 739.7 unchanged; Interior Equipment Natural Gas 212.1 unchanged; Fans Electricity 519.1 to 460.8 (-58.3); Cooling Electricity 667.3 to 649.0 (-18.3); Interior Lighting Electricity 451.9 unchanged; Heating Electricity 175.2 to 162.5 (-12.7); Heating Natural Gas 854.9 to 804.4 (-50.5). Those four deltas reproduce section 5.2's numbers exactly. The legend lists 19 end-use and fuel combinations, from Heat Rejection Electricity down to Interior Equipment Electricity; the smaller ones (heat rejection, heat recovery, pumps, refrigeration, exterior lighting, water systems, district energy) are unlabeled, and the hatched Cooling District Cooling band is about 86 TBtu. Natural gas segments are drawn with a diagonal hatch.

Figure 5. Comparison of annual site energy consumption between the ComStock baseline and the Improved Fan Scheduling and Outdoor Air Control measure scenario in applicable buildings only

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89120.yaml
     source: 89120_images/image_000012_98d457e4422ac2470c0a80cc3d2f48137b8b5a7fce8fd13ca3befbe30e3591be.png
     method: vision-description
     described: 2026-08-20 -->

![Two stacked bars comparing annual site energy consumption in TBtu by end use and fuel for applicable buildings only, baseline against measure](89120_images/image_000012_98d457e4422ac2470c0a80cc3d2f48137b8b5a7fce8fd13ca3befbe30e3591be.png)

Figure 5. The applicable-buildings-only counterpart to Figure 4, same axes and legend. The y axis is 'Annual Energy Consumption (TBtu)'. The Baseline bar totals 1,991 TBtu and the Unoccupied AHU Control bar 1,840 TBtu, a 151 TBtu reduction. Labeled segments, baseline then measure: Interior Equipment Electricity 402.9 unchanged; Interior Equipment Natural Gas 112.9 unchanged; Fans Electricity 262.5 to 204.2 (-58.3); Cooling Electricity 277.1 to 258.9 (-18.2); Interior Lighting Electricity 217.6 unchanged; Heating Electricity 82.7 to 70.0 (-12.7); Heating Natural Gas 348.5 to 298.0 (-50.5); Water Systems Natural Gas 69.9 unchanged. Because the absolute savings are the same as in Figure 4 but the baseline is smaller, the proportional saving is larger. Note that 151/1991 works out to 7.6%, whereas section 5.2 states 9.5% aggregate site energy savings for applicable buildings; and fan savings are 38.6% of the total saving shown here, not the 26% quoted in the text.

Energy consumption is categorized both by fuel type and end use.

Figure 5 shows the comparison of site energy consumption disaggregated by end use with and without the measure applied for buildings that were applicable to the upgrade. The aggregate site energy savings observed (9.5%) in buildings in which the measure was applicable (those with some degree of ventilation during unoccupied periods), is similar to the percentage site energy savings of 7.3% observed by Fernandez et al. (2017) in small office buildings. The implementation of the measure by Fernandez et al. (2013) also involved ensuring that minimum ventilation levels were met, which resulted in a slight site energy penalty (0.3%) across the entire building stock, because some buildings were under-ventilated in baseline conditions. Note that ComStock in general assumes that minimum ventilation levels are met in baseline conditions, and this analysis did not extend the measure to building types in which adequate data were not available to characterize the prevalence of existing ventilation control faults (hospitals and outpatient health facilities). Note that this measure was also not applied to schools, as past ComStock analysis has indicated that available data on fault prevalence may not be widely representative.

Note that implementation of this measure also involved control of AHU fans to operate during unoccupied periods only when a call for heating or cooling occurred, as well as the elimination of ventilation during unoccupied periods. Thus, application of this measure resulted in notable fan energy savings, as well as heating energy savings, with a smaller fraction of energy savings from cooling, because the majority of unoccupied hours for most buildings occur at nighttime, when outdoor air is more likely to impose a heating load than cooling load in many climates. Additionally, in buildings with gas or electric resistance heating, a reduction in each heating load generally results in greater site energy savings than the same reduction in cooling load, due to the higher coefficient of performance of direct expansion cooling systems (often 3-4), than the efficiencies of natural gas (often 80%) or electric resistance (exactly 100%) heating. The fraction of fan energy savings (26%) in buildings to which the measure was applicable is notable but expected. In the buildings in which the 'upper bound' of relative energy savings will occur (those with 'fan on-vent' schedules in unoccupied periods), the measure could result in reduction of fan operating hours by as much as 60% (based on the average operating hours among applicable buildings in this sample for the small office building). The small office building is one of the most common building types with this measure applicable.

Some buildings with ventilation scheduled off at night in their primary HVAC systems have dedicated systems serving other spaces (such as data centers) that have constant schedules applied to their minimum outdoor air levels. These secondary system schedules were changed to reflect building occupancy as part of this measure, but because the minimum outdoor air levels for these spaces were generally set to zero, this schedule change did not affect actual operations and produced only a minor (&lt;0.01%) change in site energy use.

