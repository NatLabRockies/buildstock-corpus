<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_4_geometry.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_4_geometry.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: fadc83e | corpus_path: technical_reference/documentation/reference_doc/4_4_geometry.md | section: Building Shape | lines: 26-36 -->
## Building Shape

Building shape is an intermediate characteristic assigned to the model during the sampling process. It is not a direct input to the model, as ComStock assumes a rectangular footprint for all buildings. Its function is as a dependency for aspect ratio (see next section <a href="#subsec_aspect_ratio" data-reference-type="ref" data-reference="subsec_aspect_ratio">1.4</a>). Probability distributions for building shape were generated from 2012 CBECS data, based on building type (U.S. Energy Information Administration 2012). CBECS uses numbers to represent many of the answers to survey questions, and ComStock adopted these numbers to represent building shapes.

Figure <a href="#fig:shape_dist" data-reference-type="ref" data-reference="fig:shape_dist">3</a> shows the breakdown of the national building stock by building shape and type.

<figure id="fig:shape_dist" data-latex-placement="H">
<img src="figures/shape.png" style="width:100.0%" />
<figcaption>Distribution of building shape by building type. The x-axis represents the building shape, and the y-axis represents the fraction of the building stock.</figcaption>
</figure>

