<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86103.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/86103.md | section: Reviewing Existing Performance Maps (Directly Compatible with EnergyPlus ® ) for Outdoor Units | lines: 416-466 -->
## Reviewing Existing Performance Maps (Directly Compatible with EnergyPlus ® ) for Outdoor Units

There are two approaches of modeling VRF in EnergyPlus; using the 'older' (system curve based) EnergyPlus object [18], or using the 'newer' (physics based) EnergyPlus object [19]. These two approaches differ significantly in terms of input requirements for modeling, and one of the major inputs to both approaches is the performance maps (designed differently between the two approaches) that determine the operating behavior (e.g., available heating/cooling capacity, COP) of VRF under various operating conditions (e.g., outdoor air temperature, operating mode, combination ratio). We have investigated both options during this exercise with many performance maps to understand performance variations especially under colder outdoor air conditions.

The latest, as of this publication, VRF technology in any applications (including one in cold climates) includes several key features such as vapor injection technology, heat recovery capability, and a three-pipe system. There are many publicly available performance maps  that are directly compatible with EnergyPlus, and we selected four different maps (three maps applicable to older object [20]-[22] and one map applicable to newer object) for initial investigation. Table 2 shows the differences between two different approaches with four different performance maps, highlighting what they represent against 2023 technology available in the market.

Table 2. Performance Indicators Between Four Different VRF Modeling Options

<!-- table recovered from measure_pdfs/86103.pdf p.26
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     method: vision-transcription -->

| EnergyPlus object | older VRF | older VRF | older VRF | newer VRF |
|---|---|---|---|---|
| manufacturer | Daikin | Mitsubishi Electric | LG Electronics | Daikin |
| reference model | REYQ72T | PUHY-HP72 | ARUB072BTE4 | generalized |
| source | Building Component Library | OpenStudio Standards | Building Component Library | EnergyPlus |
| outdoor unit capacity | 6 ton | 6 ton | 6 ton | generalized |
| heat recovery mode available? | yes | no | yes | yes |
| 2 pipe or 3 pipe system? | 3 | 2 | 3 | 3 |
| vapor injection technology? | no | yes | yes | generalized |
| operating temperature (cooling) | 23 to 122°F (DB) | 23 to 109°F (DB) | 14 to 122°F (DB) | generalized |
| operating temperature (heating) | -13 to 60°F (WB) | -13 to 60°F (WB) | -13 to 61°F (WB) | generalized |
| published reference available? | no | no | no | yes |
| validation against field data? | no | no | no | yes |

Legend: orange = "not representing the latest/best technology"; blue = "generalized and not representing specific product".

Shading in the source, which a pipe table cannot carry. Orange: "heat recovery mode available?" and "2 pipe or 3 pipe system?" in the Mitsubishi Electric column; "vapor injection technology?" in the Daikin older-VRF column; "operating temperature (heating)" in all three older-VRF columns (Daikin, Mitsubishi Electric, LG Electronics). Blue: "outdoor unit capacity", "vapor injection technology?", "operating temperature (cooling)" and "operating temperature (heating)" in the newer-VRF (Daikin) column.

As shown in Table 2, there are performance maps published by three manufacturers for the older VRF EnergyPlus object. One of the main concerns with these maps for the older object is that they do not have published references for validating the performance map against real measurements. While the manufacturers may have gone through rigorous steps for developing these maps, not knowing the specifics (e.g., how well the map fits to real measurements) dissuades us from using these for our implementation. Another concern with these maps for the older object is that they might not represent the behavior of 2023 technology. For instance, two of them (Daikin and LG) were published long enough ago that they likely do not capture 2023 technology advancements (e.g., better heating capacity under lower outdoor air temperature).

The heat pump in heating mode needs to work harder to extract heat (through the outdoor unit's heat exchanger) from the ambient air when outdoor air temperature decreases, often causing decreased capacity and efficiency (COP) under colder conditions. One of the concerns when looking into performance maps in detail was an inverse trend where the heating COP increased with lower outdoor air temperature when using the 'dual curve' approach. The 'dual curve' approach defines two different sets of performance curves for low and high temperature ranges and where the distinction between low and high temperature is defined by another curve (called a boundary curve) [23].

Figure 8 shows heating performance of VRF from building energy simulation (applied with one of the maps in Table 2) highlighting the comparison between single curve approach (shown as AllTemp in Figure 8) and dual curve approach (shown as LowTemp and HighTemp in Figure 8). Both COPcomp&amp;fan,operating (common context for the industry) and energy input ratio (EIR, inverse of COP and actual input to EnergyPlus) modifiers are presented. For consistency, AllTemp, LowTemp, and HighTemp curves reflected in this simulation results are all from one of the manufacturers shown in Table 2. The dual curve approach is meant to capture a performance change when the heat pump can operate under a wide range of outdoor air temperature but has relatively impactful performance shift within that range. However, all the low temperature performance curves for the older object shown in Table 2 showed the reverse trend like the LowTemp datapoint trend (orange square markers) in Figure 8. Because there are no reference publications providing context for the reverse trend, and because it conflicts with expected heat pump behavior, we did not implement the dual curve approach for either heating or cooling performances.

Figure 8. Single curve approach versus dual curve approach (COP based on compressor and outdoor unit fan power only)

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000014_1ce165e552f018b54cec004e8e157d20f59b79260e43563fe9bd15a46eb1f585.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 8: single- versus dual-curve heating EIR and COP modifiers versus outdoor air temperature](86103_images/image_000014_1ce165e552f018b54cec004e8e157d20f59b79260e43563fe9bd15a46eb1f585.png)

Figure 8: two simulation scatter panels against outdoor air temperature (-30 to 20 deg C) - (a) heating EIR modifier, (b) heating COPcomp&fan,operating modifier - each plotting LowTemp, HighTemp and AllTemp series. The single AllTemp curve tracks one straight line while the paired low- and high-temperature curves diverge below roughly -10 deg C. EIR modifier spans about 1.1 to 2.2. Curve sources in Table 3.

Lawrence Berkeley National Laboratory (LBNL) has developed newer VRF objects in EnergyPlus that reflect a more physics-based modeling approach compared to the older approach [24], [25]. The development work is well documented in terms of validating the modeling approach as well as performance maps (generated by the manufacturer) by comparing EnergyPlus simulation results against field or test chamber measurements. Because the performance maps used in this work reflect generalized performances of Daikin's model lineup at the time of the project period, they are not tied to any specific product in the market. However, there is an ongoing project (led by LBNL) for further improving the accuracy of VRF modeling in EnergyPlus by leveraging 2023 products in the market, which will be reflected in future EnergyPlus updates.

One goal for this analysis is to explore and capture VRF performance in colder climates. For that reason, we would like to capture 2023 cold climate technology (i.e., top of the line products) available in the market. Based on the goal and concerns described previously, it is difficult to implement 2023 technology with publicly available EnergyPlus VRF performance maps. Thus, we have made the determination to use the older VRF EnergyPlus object, create new performance maps for capacity/EIR modifiers (for both heating and cooling), and reuse existing performance data for the other remaining performance curves.

