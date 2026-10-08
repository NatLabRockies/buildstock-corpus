<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89042.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/89042.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/89042.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/89042.md | section: 5.1  Single Building Measure Tests | lines: 591-656 -->
## 5.1  Single Building Measure Tests

In this section, the standard performance implementation described in this document is compared against the original 'advanced performance' HP-RTU measure ('Heat Pump RTUs,' released in March 2023) using a sample model represented with typical meteorological year 3 weather for New York City (ASHRAE climate zone 4A).

To be clear, the original 'advanced performance' measure investigated a high-performance variable-speed HP-RTU, whereas this study investigates a standard performance HP-RTU with two cooling speeds and one heating speed. Figure 7 shows the operating difference between the original HP-RTU (advanced performance) and the standard performance HP-RTU. Annual simulations are performed for both scenarios, and normalized airflow rates and operating stages are marked against the heating (negative value) and cooling (positive) loads in each simulation time step. As shown in Figure 7, the original advanced performance HP-RTU operates between four different stages for both heating and cooling. This is how we represent full variable speed operation in the simulation program (EnergyPlus). On the other hand, the standard performance HP-RTU operates between two stages for cooling and with single heat pump stage for heating (i.e., always using both compressors simultaneously). Because of this difference in compressor operation, the standard performance HP-RTU cycles more, which may show lower efficiencies under part-load operation compared to the advanced performance HP-RTU.

Figure 7 . Single building results: operating stage comparison

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000009_cf54f95937c7abd6e5485cc56f48a4ea38d73d29e48b5a5d1dbcf77124596334.png
     method: vision-description
     described: 2026-08-22 -->

![Two scatter panels of normalized airflow versus load, colored by operating stage, advanced vs standard](89042_images/image_000009_cf54f95937c7abd6e5485cc56f48a4ea38d73d29e48b5a5d1dbcf77124596334.png)

Figure 7: two scatter panels comparing single-building operating stages, advanced performance against standard performance. Normalized air flow rate from 0 to 1 is plotted against load in Btu/hr, negative for heating and positive for cooling, with points colored by operating stage 0 to 4. The advanced unit modulates continuously where the standard unit collapses onto discrete stages. See Table 7.

Figure 8 shows the operating COPs (accounting for compressor and outdoor fan power for cooling and also including defrosting power, crankcase power, and supplemental heating for heating) against the outdoor air temperature across the annual simulation for the two scenarios. As expected, operating COPs are generally lower in standard performance HP-RTU compared to the advanced performance HP-RTU. This difference is less prevalent for heating at colder temperatures when both systems are operating under full-load conditions, and more prevalent when operating at more mild outdoor temperatures. The difference in COPs under part-load conditions (i.e., heating and cooling in mild weather conditions) is because the standard performance HP-RTU only operates between two stages during cooling operation and a single stage (both compressors running simultaneously) during heating operation. Note that both systems incur efficiency losses due to short cycling (low part-load ratios), but this is less prevalent in the advanced performance RTU that uses variable speed compressors.

Figure 8. Single building results: operating COP comparison

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000010_bfd80c0545046236f28f9fb1c073ef5dbf4fbd1cc0290c8775e780faf8ba6622.png
     method: vision-description
     described: 2026-08-22 -->

![Two scatter panels of operating COP versus outdoor air temperature, cooling and heating](89042_images/image_000010_bfd80c0545046236f28f9fb1c073ef5dbf4fbd1cc0290c8775e780faf8ba6622.png)

Figure 8: two scatter panels of single-building operating COP, including compressor and outdoor fan power, against outdoor dry-bulb air temperature in degrees F, with separate cooling and heating series, advanced performance beside standard performance. Cooling COP reaches about 6.7 for the advanced unit against roughly 5 for the standard unit. Table 7 lists the resulting annual end-use consumption.

Figure 9 is another example that highlights the part-load performance differences between the advanced and standard performance scenarios on the heating operation side. The figure is a heat map (x-axis is day in a year and y-axis is hour in a day) showing heating operating COP (only including compressor and outdoor fan power), where the color shows how much improvement to COP the advanced performance unit has compared to the standard performance unit. The smallest improvements (i.e., red areas) come from full-load conditions where the heat pump runs on full capacity at the beginning of a cold day (e.g., 6 a.m.). Other than those hours, the better part-load performance of the advanced unit takes over and the operating heating COP can improve by 2.5.

Figure 9. Single building results: heating operating difference between two performance scenarios

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000011_7d1f8d46088e4f5e97202461c24d4124c9bd9e3b727015e106f9327bef4f8d89.png
     method: vision-description
     described: 2026-08-22 -->

![Hour-by-day heatmap of heating operating COP difference between the two performance scenarios](89042_images/image_000011_7d1f8d46088e4f5e97202461c24d4124c9bd9e3b727015e106f9327bef4f8d89.png)

Figure 9: heatmap of the single-building heating operating COP difference between the two performance scenarios, hour of the day on the vertical axis and day of the year on the horizontal, on a diverging 0.5 to 2.5 scale where positive values mean the advanced unit performs better. Winter morning hours carry both the largest gains and the largest deficits. See Table 7.

Table 7 summarizes the annual simulation results of the two scenarios showing the differences in performance metrics. Because of consistent inefficiency of the standard performance HP-RTU compared to the advanced performance HP-RTU, the advanced performance unit outperforms the standard performance unit in all categories: rated COP, operating COP, and portion of backup heating load against the entire heating load. Multiple HP-RTUs are installed in this example building model, and additional calculations are performed to extract representative performance metrics (e.g., COP). For instance, the rated heating (or cooling) COP shown in Table 7 is the weighted average of the rated COPs of the nine HP-RTUs, with weights based on their annual heating (or cooling) loads. To calculate the operating heating COP in Table 7, the annual heat pump heating load and annual electricity consumption (only including compressor and outdoor unit fan power) of each HP-RTU are used to determine the annual average operating COP for each unit. These individual COPs are then used to calculate the weighted (also by annual heating load) average operating heating COP across all HP-RTUs. The heating backup fraction is determined by dividing the annual backup heating load by the total annual heating load for all HP-RTUs. While the operating COP accounts only for the heat pump heating load, compressor power, and outdoor unit fan power, the "total" operating heating COP also includes backup heating load/electricity, crankcase heater electricity, and defrosting electricity. The same metrics released in our data are calculated using these methods.

As mentioned, the 'rated' COPs (for both heating and cooling) shown in Table 7 and other parts of this report are based on rated conditions and only account for compressor power and outdoor fan power. Rated COP values are extracted from the manufacturers' performance sheets and correspond to standard rated conditions, which are typically available in performance tables (e.g., variations of capacity and power with indoor and outdoor temperatures). However, rated COPs reported in this study can be different from the rated COP reported with AHRI performance rating (i.e., more common rated COP definition in general), as the AHRI COP calculation will include not only outdoor fan power but also supply air blower power.

Table 7. Single Building Results: Annual End-Use Consumptions

<!-- table recovered from measure_pdfs/89042.pdf p.34
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     method: vision-transcription -->

| Scenario | Advanced unit | Standard unit |
|---|---|---|
| Heating Rated COP | 3.892 | 3.660 |
| Heating Operating COP | 4.172 | 2.786 |
| Heating backup fraction | 0.062 | 0.080 |
| Heating Total Operating COP | 3.490 | 2.437 |
| Cooling Rated COP | 3.780 | 3.674 |
| Cooling Operating COP | 5.313 | 4.097 |

Legend, which a pipe table cannot carry: the source fills the whole "Advanced unit" column blue for "Better" and the whole "Standard unit" column orange for "Worse".

Other factors should also be considered (such as utility cost impacts on peak demand charges, greenhouse gas emissions and its time dependence, and return on investment) in order to comprehensively assess the impact of a standard efficiency HP-RTU versus a high-efficiency HP-RTU.

