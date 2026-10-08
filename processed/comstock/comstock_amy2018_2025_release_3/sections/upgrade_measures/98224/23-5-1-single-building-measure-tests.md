<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/98224.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/98224.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/98224.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/98224.md | section: 5.1  Single-Building Measure Tests | lines: 573-614 -->
## 5.1  Single-Building Measure Tests

In this section, we analyze the performance of a small office building model in St. Louis, Missouri (climate zone 4A) to demonstrate the application of the measure scenario to a single building. Figure 12 illustrates the impact of the upgrade by comparing the baseline and upgrade models, using hourly data for operating/cooling COP and runtime fraction throughout the year in relation to outdoor air temperature. The baseline RTU is equipped with a single-speed DX system with a rated cooling COP of 3.0 and a constant air volume fan. In contrast, the upgraded model features a variable-speed DX system with a higher rated cooling COP of 4.4 and a singlezone variable air volume fan.

Figure 12. Single-building model example with upgrade measure

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98224.yaml
     source: 98224_images/image_000017_b07093c045ac7dd919f50ddbbfdadbe7412da58a5416787486c8389cd5454d72.png
     method: vision-description
     described: 2026-08-22 -->

![Three scatter panels of single-building COP, cooling runtime fraction and fan power versus temperature](98224_images/image_000017_b07093c045ac7dd919f50ddbbfdadbe7412da58a5416787486c8389cd5454d72.png)

Figure 12: three scatter panels for one example single building, each plotted against outdoor air temperature in degrees F and comparing the upgrade against the baseline - operating cooling COP, cooling runtime fraction from 0 to 1, and supply fan power in watts. The upgrade holds a higher COP at every temperature and drops below the baseline's fixed fan power. Table 5 gives annual totals.

As shown in Figure 12, the baseline single-speed DX unit shows limited improvement in operating COP as outdoor temperatures decrease, indicating it benefits less from colder air than the upgraded system. In contrast, the upgraded unit maintains higher COPs across the full range of outdoor temperatures, including the rated condition of 95°F. The performance gap between the two systems widens at lower outdoor air temperatures.

This improvement is driven by several factors: (1) higher rated COP, (2) better efficiency at lower speeds, (3) better performance across operating temperatures, and (4) improved part-load performance. Collectively, these advantages enable the upgraded RTU to operate more efficiently than the baseline model. As indicated in Figure 9 and Figure 10, the performance maps employed in this study are limited to outdoor air dry-bulb temperatures of 75°F (23.9°C). This limitation accounts for the plateau observed in the operating cooling COP below that temperature in Figure 12. The second graph in Figure 12 also shows that cooling runtime fractions are much smaller below 75°F, minimizing the influence of this plateau.

Figure 12 also compares the runtime fractions between the baseline and upgrade scenarios. The runtime fraction (also known as the duty factor) represents the proportion of time the cooling coil (or the compressor and condenser fan) is actively operating relative to the total time it is available to run for a given time period. It is based on the part-load ratio, defined as the ratio of the cooling load (part-load capacity) to the coil's full or steady-state capacity. As expected for a single-speed DX unit compared to a variable-speed system, the baseline unit shows lower runtime fractions across the temperature range, indicating more frequent short cycling and less continuous operation. In contrast, the variable-capacity systems operate more continuously at lower compressor speeds, reducing cycling losses associated with short run times.

The RTU upgrade also delivers fan energy savings by incorporating a variable-speed supply fan. As shown in Figure 12, the constant-speed fan used in the baseline system operates at a fixed speed whenever it is on, providing steady airflow regardless of the actual heating or cooling demand. In contrast, the upgraded system includes multiple fan power levels, allowing it to reduce speed-and therefore power consumption-during periods of lower load. While the constant-speed fan is simpler to control and generally less expensive up front, it is less efficient under part-load conditions because it consumes the same amount of energy even when full airflow is unnecessary. The variable-speed fan, on the other hand, adjusts airflow to match the required load, improving energy efficiency, enhancing occupant comfort through more consistent temperature and humidity control, and reducing system wear caused by frequent cycling.

Table 5 summarizes the modeled annual electricity use and operating performance for the baseline and upgraded RTU systems (heating is served with an electric resistance coil in this example). Overall, the upgrade scenario achieves an 11.4% reduction in total electricity consumption, primarily driven by savings in cooling (43.8%) and fan energy (24.9%). These improvements reflect the combined benefits of a higher-efficiency variable-speed DX system and a variable-speed supply fan, which reduces energy use by modulating airflow to match realtime cooling demand. Despite these overall savings, heating energy usage increased slightly by 1.9%. This is attributed to the improved fan efficiency in the upgraded system: Unlike the baseline's constant-speed fan, which adds more waste heat to the airstream during operation, the variable-speed fan introduces less incidental heat. As a result, the system must compensate with additional mechanical heating to meet space heating loads. The upgrade also yields a notable improvement in annual cooling system performance, with the average operating COP (including compressor and condenser fan power only) increasing from 3.5 to 4.8 (a 37.1% improvement), along with gains in minimum and maximum COP across the cooling season. The higher standard deviation of COP observed in the upgraded system reflects its broader range of efficient partload operation, enabled by variable-speed modulation.

Table 5. Annual Summary of Baseline vs. Upgrade Measure Scenarios

|                    |   Baseline | Upgrade    | Improvement   |
|--------------------|------------|------------|---------------|
| Heating            |      43.15 | 43.95      | -1.9%         |
| Cooling            |      19.43 | 10.92      | 43.8%         |
| Interior Lighting  |       3.58 | 3.58       | 0.0%          |
| Exterior Lighting  |      10.62 | 10.62      | 0.0%          |
| Interior Equipment |      24.87 | 24.87      | 0.0%          |
| Fans               |      31.82 | 23.9       | 24.9%         |
| Water Systems      |       3.54 | 3.54       | 0.0%          |
| Total              |     137.01 | 121.38     | 11.4%         |
| Average            |        3.5 | 4.8        | 37.1%         |
| Minimum            |        2.6 | 3.1        | 19.2%         |
| Maximum            |        4.7 | 6.4 36.2%  | 37.1%         |
| Standard deviation |       0.37 | 0.63 70.3% | 37.1%         |

