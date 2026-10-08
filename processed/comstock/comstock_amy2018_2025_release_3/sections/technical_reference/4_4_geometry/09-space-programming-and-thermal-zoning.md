<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_4_geometry.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_4_geometry.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 267e3ea | corpus_path: technical_reference/documentation/reference_doc/4_4_geometry.md | section: Space Programming and Thermal Zoning | lines: 120-163 -->
## Space Programming and Thermal Zoning

As described above, all ComStock building models are a rectangular prism with a prescribed aspect ratio, floor area, etc. Within each building, there are one or more space types, as described in Section <a href="#sec:space_type_ratios" data-reference-type="ref" data-reference="sec:space_type_ratios">[sec:space_type_ratios]</a>. Space types are represented within the rectangular geometry as “slices” through the building that correspond to the floor area fractions of each space type. This is shown in Figure <a href="#fig:geometry_by_space_type_and_zone" data-reference-type="ref" data-reference="fig:geometry_by_space_type_and_zone">10</a>(a). In the cases of very small buildings, this can sometimes result in spaces which are unrealistically long and narrow for space types that make up only a small fraction of the building.

For larger buildings where the length and width are both greater than 37.5 feet, each space type is divided into core-and-perimeter thermal zones with a 15-foot depth (Figure <a href="#fig:geometry_by_space_type_and_zone" data-reference-type="ref" data-reference="fig:geometry_by_space_type_and_zone">10</a>(b)). Notice that the space types adjacent to the shorter ends of the building are each broken into six thermal zones, whereas the space types in the center of the building are each broken into three thermal zones. In multistory buildings, space types are often found on more than one floor, and in some cases, a floor will be a single space type. The downside to this thermal zoning approach is that thermal zones—and, as a follow-on, the HVAC systems that serve them—may be unrealistically small or large for certain geometry and building type combinations. These may later be modified to set a minimum and maximum size threshold for thermal zones.

<figure id="fig:geometry_by_space_type_and_zone" data-latex-placement="hb!">
<img src="figures/geometry_by_space_type_and_zone.png" style="width:100.0%" />
<figcaption>Example building geometry colored by (a) space type and (b) zone.</figcaption>
</figure>

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-guidehouse_nfrc_window_report" class="csl-entry">

Ciraulo, Rebecca, Valerie Nubbe, Sasha Wedekind, Chelsea Jean-Michel, and Jared Stanley. 2021. *Commercial Fenestration Market Study*. Guidehouse Inc.

</div>

<div id="ref-costar" class="csl-entry">

CoStar. 2018. *CoStar Property - Commercial Property Research and Information*. <a href="http://www.costar.com/products/costar-property-professional" class="uri">Http://www.costar.com/products/costar-property-professional</a>.

</div>

<div id="ref-deru_2011" class="csl-entry">

Deru, M, K Field, D Studer, et al. 2011. *U.s. Department of Energy Commercial Reference Building Models of the National Building Stock*. NREL/TP-5500-46861. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy11osti/46861.pdf>.

</div>

<div id="ref-hsip" class="csl-entry">

U.S. Department of Homeland Security. 2012. *Homeland Security Infrastructure Program*. <a href="https://hifld-geoplatform.hub.arcgis.com/" class="uri">Https://hifld-geoplatform.hub.arcgis.com/</a>.

</div>

<div id="ref-eia2012cbecs" class="csl-entry">

U.S. Energy Information Administration. 2012. *2012 Commercial Building Energy Consumption Survey (CBECS)*. Http://www.eia.doe.gov/emeu/cbecs/.

</div>

</div>
