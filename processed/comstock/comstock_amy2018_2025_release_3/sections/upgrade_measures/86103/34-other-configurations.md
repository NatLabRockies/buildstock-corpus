<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86103.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | corpus_version: 267e3ea | corpus_path: upgrade_measures/measure_pdfs/86103.md | section: Other Configurations | lines: 569-587 -->
## Other Configurations

Rated COPs for heating and cooling are specified based on linear regressions of actual products' specifications [31] as shown in Figure 12. When capacity determined by the sizing algorithm passes beyond the capacity range shown in the figure, minimum or maximum COP datapoints shown in the figure are used. Pipe configurations such as piping length are also necessary as inputs to the VRF object.

Figure 12. Rated COP derivation based on sized capacities

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000018_c7cd27b2907baefc61d90b394bc017f684b0ed9e8fd39208e27180008262d654.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 12: rated heating and cooling COP regressions against sized capacity](86103_images/image_000018_c7cd27b2907baefc61d90b394bc017f684b0ed9e8fd39208e27180008262d654.png)

Figure 12: two scatter panels with fitted trend lines deriving rated non-ducted COP from sized capacity - (a) heating COP versus heating capacity (about 20,000-80,000 W), (b) cooling COP versus cooling capacity. Both decline with size; the printed fits are y = -0.000011x + 4.500686 for heating and y = -0.00002x + 4.934802 for cooling. See Section 4.2.1 under 'Other Configurations'.

In order to provide adequate variations between VRF systems installed in different building configurations, an approximation algorithm based on building geometry is used [32]. This algorithm first selects the outdoor unit location based on the availability of an attic: place the outdoor unit on the center of the roof if the building does not have an attic, and place it outdoors next to the lowest floor if there is an attic. Then the algorithm finds thermal zones with VRF indoor units to get Cartesian coordinates of each zone's centroid (i.e., representing physical location of an indoor unit). These coordinates of all thermal zones as well as the centroid of the outdoor unit location are used to calculate the farthest piping length and highest/lowest vertical piping length between indoor and outdoor units. To provide early context regarding the location of the outdoor unit, all the VRF systems' outdoor units are located on the roof in our analysis (but with varying piping lengths and heights).

The waste heat recovery is enabled in EnergyPlus to simulate VRF with simultaneous heating and cooling capability. In EnergyPlus, modifiers are applied to the operating capacity and EIR when the VRF system is in heat recovery mode to reflect degraded performance as well as some level of time delay. And depending on the operating mode of the outdoor unit (e.g., heating mode when heating is more dominant across all indoor units), the electric power of the compressor is added to either heating or cooling electricity consumption in the final result. More details on simultaneous heating and cooling operation can be found in EnergyPlus documentation [18]. Additionally, The defrost strategy is configured with reverse cycling.

