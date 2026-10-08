<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_4_geometry.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_4_geometry.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0a2f61f | corpus_path: technical_reference/documentation/reference_doc/4_4_geometry.md | section: Area | lines: 15-25 -->
## Area

Building floor area is assigned to each model through the sampling process. Probability distributions were generated using CoStar (CoStar 2018) for most building types. HSIP (U.S. Department of Homeland Security 2012) was used for schools and hospitals, as neither are well represented in CoStar.

Figure “Distribution of rentable area by building type. The x-axis represents rentable area (square feet), and the y-axis represents the fraction of the building stock.” shows the breakdown of each building type in the national building stock by building size category (referred to as “rentable area”). Notice that the categories are presented as ranges. At this time, ComStock uses the area in the middle of the range, with the exception of "\_1000" and "over_1mil," which use 1000 square feet and 1 million square feet, respectively. This method could be improved by adding variability to the building areas by selecting a variety of areas within the range.

<figure id="fig:area_dist" data-latex-placement="H">
<img src="figures/area_dist.png" style="width:100.0%" />
<figcaption>Distribution of rentable area by building type. The x-axis represents rentable area (square feet), and the y-axis represents the fraction of the building stock.</figcaption>
</figure>

