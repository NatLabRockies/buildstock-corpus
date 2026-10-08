<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_4_geometry.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_4_geometry.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0396270 | corpus_path: technical_reference/documentation/reference_doc/4_4_geometry.md | section: Number of Floors | lines: 84-96 -->
## Number of Floors

ComStock assigns a number of floors to each model during the sampling process to create a distribution of building heights in the stock. This value represents the number of aboveground floors for a given model. No buildings in ComStock have belowground stories.

For most of the building types, we generated probability distributions based on county and building type using CoStar (CoStar 2018). We used HSIP (U.S. Department of Homeland Security 2012) for schools and hospitals, as neither are well-represented in CoStar.

Figure “Distribution of number of aboveground floors by building type. The x-axis represents the number of floors, and the y-axis represents the fraction of the building stock.” shows the breakdown of the national building stock by number of floors and building type.

<figure id="fig:nfloors_dist" data-latex-placement="H">
<img src="figures/nfloors.png" style="width:100.0%" />
<figcaption>Distribution of number of aboveground floors by building type. The x-axis represents the number of floors, and the y-axis represents the fraction of the building stock.</figcaption>
</figure>

