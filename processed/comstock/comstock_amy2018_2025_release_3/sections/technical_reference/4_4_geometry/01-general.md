<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_4_geometry.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_4_geometry.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 267e3ea | corpus_path: technical_reference/documentation/reference_doc/4_4_geometry.md | section: General | lines: 4-14 -->
## General

A building’s geometry influences several aspects of its associated building energy model. It impacts the building envelope by dictating the orientation of windows, the surface-to-volume ratio, and the ratio of one surface type to another. Geometry also impacts how prevalent solar heat gain is for a given building through the building’s orientation and shape. ComStock uses seven characteristics to define a building energy model’s geometry: floor area, shape, aspect ratio, rotation, number of floors, floor height, and window-to-wall ratio (WWR). The majority of these characteristics are assigned to the models as part of the sampling process. Combined, they create a virtual building model geometry like the example shown in Figure <a href="#fig:geom_example" data-reference-type="ref" data-reference="fig:geom_example">1</a>. All building models are variations of rectangular prisms with flat roofs and windows wrapping around the exterior. This simple geometry allows ComStock to easily scale properties and generate the number of individual building models needed for a national stock model. The following subsections describe each of the seven characteristics that define a building energy model’s geometry in ComStock.

<figure id="fig:geom_example" data-latex-placement="h!">
<img src="figures/small_office_geometry.PNG" style="width:70.0%" />
<figcaption>Example building geometry for a small office.</figcaption>
</figure>

(Intentionally blank)

