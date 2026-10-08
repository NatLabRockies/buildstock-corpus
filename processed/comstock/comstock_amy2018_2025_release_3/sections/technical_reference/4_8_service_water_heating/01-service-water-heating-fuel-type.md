<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_8_service_water_heating.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_8_service_water_heating.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0396270 | corpus_path: technical_reference/documentation/reference_doc/4_8_service_water_heating.md | section: Service Water Heating Fuel Type | lines: 6-21 -->
## Service Water Heating Fuel Type

It would be logical to assume that the SWH system in a building would use the same fuel as the space heating system. An examination of the CBECS 2012 data (U.S. Energy Information Administration 2012) shows that this is the most common case, but it is not always true. In particular, it appears that building types that have large SWH loads, such as hotels and hospitals, are much more likely to use natural gas for SWH, regardless of what their space heating fuel is, presumably because of fuel cost differences. In contrast, building types with low SWH loads are more likely to use electricity for SWH, presumably because of the ease and cost of running wiring compared to installing natural gas piping.

To represent this variability, we used the CBECS 2012 data to create a distribution of SWH fuels for each combination of space heating fuel and building type. The resulting distribution of floor area served by various SWH fuels is shown in Figure “Area-weighted distribution of service water heating fuel by space heating fuel and building type.”. As described in Section “Heating, Ventilating, Air Conditioning, and Refrigeration”, the prevalence of different space heating fuel varies considerably by county. Because the service water heating fuel depends on the space heating fuel, the probabilities at a stock level are heavily skewed toward the more common space heating fuels, as shown in Figure “Floor area served by each service water heating fuel by space heating fuel and building type.”.

<figure id="fig:swh_fuel_dist" data-latex-placement="ht!">
<img src="figures/swh_fuel_dist.png" />
<figcaption>Area-weighted distribution of service water heating fuel by space heating fuel and building type.</figcaption>
</figure>

<figure id="fig:swh_fuel_area" data-latex-placement="ht!">
<img src="figures/swh_fuel_area.png" />
<figcaption>Floor area served by each service water heating fuel by space heating fuel and building type.</figcaption>
</figure>

