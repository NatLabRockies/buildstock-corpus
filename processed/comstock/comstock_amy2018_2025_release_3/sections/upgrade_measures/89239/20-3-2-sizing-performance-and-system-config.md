<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89239.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89239.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89239.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/89239.md | section: 3.2  Sizing, Performance, and System Configuration | lines: 297-336 -->
## 3.2  Sizing, Performance, and System Configuration

Entering loop temperature on the source side is often the most important variable in influencing the performance of water-to-water heat pumps [6]. Entering temperatures on the load side and source- and load-side mass flow rates also affect performance of water-to-water heat pumps [6]. As an example, Table 2 shows rated energy efficiency ratio and COP for a 20-ton Trane Axiom EXW water-to-water heat pump at Air-Conditioning, Heating, and Refrigeration Institute (AHRI) rating conditions for geothermal heat pumps, and the range of rated Energy Efficiency Ratio (EER) and COP values for another set of entering loop temperatures [9]. The range of rated performance values at the non-AHRI conditions represents variations in performance due to load- and source-side mass flow rate and variation in load-side entering water temperatures.

Table 2. Rated Performance of a Selected Water-to-Water Heat Pump Model Available in the United States

| Entering Water Temperature Conditions (Cooling/Heating)   | Energy Efficiency Ratio   | Coefficient of Performance                  | Notes     |
|-----------------------------------------------------------|---------------------------|---------------------------------------------|-----------|
| 77°F/50°F 15.7                                            | 2.8                       | AHRI rating conditions for ground loop heat |           |
| 11.2-22.5                                                 | 2.4-5.6                   |                                             | 86°F/45°F |

Based on discussions with design practitioners who have experience in retrofits with ground heat exchangers, in buildings with hydronic HVAC systems, existing air-side ductwork is generally sufficient for a reduction in hydronic supply temperatures in heating, while hydronic pipes and coils are more likely to be the limiting factor.

This measure will implement a lower set point based on the typical operating range of watersource heat pumps (135°F) [8]. Components such as coils will be resized for the lower supply temperatures. If the change is significant, this would correspond in a real building to the need for a coil replacement or the use of a novel solution such as coil twinning. Resizing the coils reduces the likelihood of an excessive number of time steps in which the zone-level set points are not met. The measure will report coil sizes before and after the supply temperature change. These values can be used to assess the cost associated with any required coil retrofit. Additionally, users will have the option to limit the increase in design system mass flow rates to a specified proportion, and instead resize heating coils for a larger temperature differential, which could emulate replacing coils while maintaining the same hydronic distribution infrastructure (pipes). Per discussions with design professionals, hydronic distribution infrastructure is often sufficiently oversized to allow for an increase in flow rate of around 20% [10].

The centralized heating and cooling heat pumps will be controlled to an outlet temperature set point. This measure will also implement a reset of the chilled water temperature based on outdoor air temperature, as presented in Table 3. The chilled water supply temperature reset scheme is based on a reset described in Appendix G of ASHRAE 90.1 2022, which is intended to represent industry standard practice[13].

The modeled hydronic loop configuration is shown in Figure 2. Tying the heating and cooling heat pumps to the same ground loop allows for potential heat recovery if the two are operating simultaneously. The separation of the ground heat exchanger from the source-side heat pump loop allows for the ground heat exchanger to be bypassed when the heating and heat-rejection loads from the heat pumps are close to balanced, which can reduce circulation pump energy use on the ground loop. This configuration is a modified version of one proposed by Mescher [14].

Table 3. Chilled Water Supply Temperature Reset Implemented in This Measure (Consistent with ASHRAE 90.1 2022)

| Outdoor Air Temperature   | Chilled Water Supply Temperature       |
|---------------------------|----------------------------------------|
| 80°F and above            | 44°F                                   |
| Between 60°F and 80°F     | Linearly varying between 44°F and 54°F |
| 60°F and below            | 54°F                                   |

In conjunction with the ground heat exchanger sizing measure, this measure gives users the ability to specify on what load (heating or cooling) and on what fraction of load (ranging from 20% to 100%), they wish to size the ground heat exchanger. If the ground heat exchanger is sized to less than 100% of the dominant load (heating or cooling), supplemental equipment will be used (a cooling tower, boiler, or both, depending on the need). A boiler will be electric and will be connected in parallel to the water-source heat pump supplying heating, and a cooling tower will be connected to the ground loop. This configuration is generally based on the recommendations of Kavanaugh and Rafferty [6]. The boiler is configured in parallel with the heat pumps, rather than in series, for consistency with a lower hydronic supply temperature, facilitating operation of the heat pumps alone in lower-load conditions. The placement of the boiler on the building loop, rather than on the ground loop, in the context of 'sharing' heating load, permits the ground loop to operate at lower temperatures, reducing the penalty on the cooling heat pump during simultaneous heating and cooling.

Figure 2. Modeled hydronic loop configuration, with optional equipment shown in dashed-line boxes

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89239.yaml
     source: 89239_images/image_000008_668c1f9b7b0a6740382a7a08dbd04cd5d0a1d8561bc78ed89856055859622525.png
     method: vision-description
     described: 2026-08-21 -->

![Block diagram of the modeled hydronic loop configuration; optional equipment in dashed boxes](89239_images/image_000008_668c1f9b7b0a6740382a7a08dbd04cd5d0a1d8561bc78ed89856055859622525.png)

Figure 2: schematic block diagram of the four modeled hydronic loops stacked top to bottom - a ground loop with ground heat exchanger, a condenser loop coupled through a water-to-water heat exchanger, and separate heating and cooling loops each served by a water-source heat pump feeding AHU heating or cooling coils. Optional cooling tower and backup boiler are drawn in dashed boxes; supply and demand sides and pumps are marked.

