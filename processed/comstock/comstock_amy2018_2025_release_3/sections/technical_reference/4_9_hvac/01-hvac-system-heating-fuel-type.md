<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 43ae2d4 | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: HVAC System Heating Fuel Type | lines: 4-47 -->
## HVAC System Heating Fuel Type

Commercial HVAC equipment can use various heating fuel types, with the most common being natural gas, electricity, propane, fuel oil, and district heating. To reflect the variability of heating fuels in the real building stock, the ComStock workflow creates probability distributions of heating fuel types per building type at the county level. These distributions are used to assign a heating fuel type to each ComStock building model during the sampling process.

The probability distributions are informed by two data sources. First, there are the CBECS 2012 microdata, which include data on heating fuel(s), building type, and census division for the surveyed buildings. This data can be used to produce probability distributions for heating fuel by building type at the census division level. However, several data sources suggest notable variation within census divisions, which indicates that increased granularity may be needed (beyond what CBECS can provide). The heating fuel type probability distributions used in ResStock—which provides data for residential buildings at the county level—were used to add granularity. However, initial comparisons showed discrepancies between the ResStock data and the CBECS data, which is likely due to inherent differences between residential and commercial buildings. This indicated that the ResStock data should not be used directly. To rectify this, the county-level ResStock data were scaled to align with the CBECS data. This preserved the county-level variation in fuel type prevalence provided by the ResStock data, while also preserving the census division totals provided by the CBECS commercial data. District heating values were not available in the ResStock data, so the per-building-type CBECS values were used for all counties in a given census division.

In some cases, filtering down to a specific region and building type in the CBECS data yields very few samples. This can lead to unreliable conclusions for a region. To mitigate this, we took a blended approach, where some fraction of the CBECS region fuel type percentage comes from the regional samples only, and some fraction comes from the national sample for the building type. If more than 15 samples exist for a given building type and region, then 100% of the fuel type prevalence comes from that specific region. (The threshold of 15 samples was selected baced on engineering judgment to balance process reliability and regional variability.) If there are fewer than 15 samples, the number of samples divided by 15 will be the fraction used for the region, and the remainder will use the national numbers. For example, if a region has only 12 office samples, 80% (12/15) of the effective CBECS regional value will come from the CBECS region, and the other 20% will come from the national CBECS value for the building type. This will cause region/building type combinations with lower sample sizes to have a stronger inheritance of the national characteristics than the regional characteristics when we lack sufficient evidence to support this level of detail.

Some commercial building HVAC systems use multiple fuel types. For example, a VAV system with a gas furnace in the air handling unit and electric resistance coils in the reheat boxes, or a gas furnace DOAS with variable refrigerant flow (VRF) heat pumps serving the zones. This can complicate the categorization of these systems into a single primary fuel type. To address this, we determine the primary heating fuel type for the mixed fuel systems. The primary heating fuel is the heating fuel expected to carry the majority of the heating load. For example, the previously mentioned example of a VAV system with gas heat at the air handler and electric reheat would be classified as an electric-heated system, since the majority of heating for multizone VAV systems usually comes from the reheat. A full list of ComStock HVAC systems and their fuel type categories are shown in Table <a href="#tab:hvac_system_heating_fuel_categories" data-reference-type="ref" data-reference="tab:hvac_system_heating_fuel_categories">1</a>. Further detail on model HVAC system assignment methodology can be found in Section <a href="#sec:HVAC_System_Type" data-reference-type="ref" data-reference="sec:HVAC_System_Type">1.2</a>.

Figure <a href="#fig:fuel_cbecs_v_cstock" data-reference-type="ref" data-reference="fig:fuel_cbecs_v_cstock">1</a> compares the prevalence of heating fuel type by stock floor area for CBECS 2012 and ComStock, by building type. In most cases, ComStock closely aligns to the CBECS 2012 values. However, there are some differences between the two sources due to randomness in the sampling process and from the use of other data sources to achieve county-level granularity in fuel type prevalence. The largest difference is in small hotels where ComStock shows 87% of the floor area using electric heating while CBECS suggest 74%, an absolute difference of 12%.

<figure id="fig:fuel_cbecs_v_cstock">
<img src="figures/cbecs_comstock_fuel_type_comparison.png" style="width:110.0%" />
<figcaption>Comparison of heating fuel type prevalence by floor area between CBECS 2012 and ComStock.</figcaption>
</figure>

The county-level prevalences of different heating fuel types are shown in Figure <a href="#fig:map_naturalgas" data-reference-type="ref" data-reference="fig:map_naturalgas">2</a> (natural gas), Figure <a href="#fig:map_electricity" data-reference-type="ref" data-reference="fig:map_electricity">3</a> (electricity), Figure <a href="#fig:map_fueloil" data-reference-type="ref" data-reference="fig:map_fueloil">4</a> (fuel oil), Figure <a href="#fig:map_propane" data-reference-type="ref" data-reference="fig:map_propane">5</a> (propane), and Figure <a href="#fig:map_district" data-reference-type="ref" data-reference="fig:map_district">6</a> (district heating).

<figure id="fig:map_naturalgas">
<img src="figures/map_naturalgas.png" style="width:80.0%" />
<figcaption>Fraction of ComStock models using natural gas heating per county.</figcaption>
</figure>

<figure id="fig:map_electricity">
<img src="figures/map_electricity.png" style="width:80.0%" />
<figcaption>Fraction of ComStock models using electric heating per county.</figcaption>
</figure>

<figure id="fig:map_fueloil">
<img src="figures/map_fueloil.png" style="width:80.0%" />
<figcaption>Fraction of ComStock models using fuel oil heating per county.</figcaption>
</figure>

<figure id="fig:map_propane">
<img src="figures/map_propane.png" style="width:80.0%" />
<figcaption>Fraction of ComStock models using propane heating per county.</figcaption>
</figure>

<figure id="fig:map_district">
<img src="figures/map_districtheating.png" style="width:80.0%" />
<figcaption>Fraction of ComStock models using district heating per county.</figcaption>
</figure>

