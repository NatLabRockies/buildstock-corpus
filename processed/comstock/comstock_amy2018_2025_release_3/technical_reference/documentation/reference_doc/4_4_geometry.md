<!-- comstock 2025-3 | technical_reference | documentation/reference_doc/4_4_geometry.tex -->
# Geometry

## General

A building’s geometry influences several aspects of its associated building energy model. It impacts the building envelope by dictating the orientation of windows, the surface-to-volume ratio, and the ratio of one surface type to another. Geometry also impacts how prevalent solar heat gain is for a given building through the building’s orientation and shape. ComStock uses seven characteristics to define a building energy model’s geometry: floor area, shape, aspect ratio, rotation, number of floors, floor height, and window-to-wall ratio (WWR). The majority of these characteristics are assigned to the models as part of the sampling process. Combined, they create a virtual building model geometry like the example shown in Figure <a href="#fig:geom_example" data-reference-type="ref" data-reference="fig:geom_example">1</a>. All building models are variations of rectangular prisms with flat roofs and windows wrapping around the exterior. This simple geometry allows ComStock to easily scale properties and generate the number of individual building models needed for a national stock model. The following subsections describe each of the seven characteristics that define a building energy model’s geometry in ComStock.

<figure id="fig:geom_example" data-latex-placement="h!">
<img src="figures/small_office_geometry.PNG" style="width:70.0%" />
<figcaption>Example building geometry for a small office.</figcaption>
</figure>

(Intentionally blank)

## Area

Building floor area is assigned to each model through the sampling process. Probability distributions were generated using CoStar (CoStar 2018) for most building types. HSIP (U.S. Department of Homeland Security 2012) was used for schools and hospitals, as neither are well represented in CoStar.

Figure <a href="#fig:area_dist" data-reference-type="ref" data-reference="fig:area_dist">2</a> shows the breakdown of each building type in the national building stock by building size category (referred to as “rentable area”). Notice that the categories are presented as ranges. At this time, ComStock uses the area in the middle of the range, with the exception of "\_1000" and "over_1mil," which use 1000 square feet and 1 million square feet, respectively. This method could be improved by adding variability to the building areas by selecting a variety of areas within the range.

<figure id="fig:area_dist" data-latex-placement="H">
<img src="figures/area_dist.png" style="width:100.0%" />
<figcaption>Distribution of rentable area by building type. The x-axis represents rentable area (square feet), and the y-axis represents the fraction of the building stock.</figcaption>
</figure>

## Building Shape

Building shape is an intermediate characteristic assigned to the model during the sampling process. It is not a direct input to the model, as ComStock assumes a rectangular footprint for all buildings. Its function is as a dependency for aspect ratio (see next section <a href="#subsec_aspect_ratio" data-reference-type="ref" data-reference="subsec_aspect_ratio">1.4</a>). Probability distributions for building shape were generated from 2012 CBECS data, based on building type (U.S. Energy Information Administration 2012). CBECS uses numbers to represent many of the answers to survey questions, and ComStock adopted these numbers to represent building shapes.

Figure <a href="#fig:shape_dist" data-reference-type="ref" data-reference="fig:shape_dist">3</a> shows the breakdown of the national building stock by building shape and type.

<figure id="fig:shape_dist" data-latex-placement="H">
<img src="figures/shape.png" style="width:100.0%" />
<figcaption>Distribution of building shape by building type. The x-axis represents the building shape, and the y-axis represents the fraction of the building stock.</figcaption>
</figure>

## Aspect Ratio

Aspect ratio is defined as the overall length in the east–west direction divided by the overall length in the north–south direction. It is assigned to the building models during the sampling process. Probability distributions based on building shape were generated from 2012 CBECS data (U.S. Energy Information Administration 2012).

Figure <a href="#fig:aspect_ratio_dist" data-reference-type="ref" data-reference="fig:aspect_ratio_dist">4</a> shows the breakdown of the national building stock by aspect ratio. The aspect ratios are integers from one to six, which represent a building’s north-south:east-west ratio.

<figure id="fig:aspect_ratio_dist" data-latex-placement="H">
<img src="figures/aspect_ratio.png" style="width:100.0%" />
<figcaption>Distribution of aspect ratio by building type. The x-axis represents the aspect ratio (an integer from 1-6), and the y-axis represents the fraction of the building stock.</figcaption>
</figure>

## Rotation

Rotation defines the orientation of the building relative to the cardinal directions. In ComStock, there are eight rotation options, ranging from 0 to 315 degrees at 45-degree intervals. Ninety and 270 degrees correspond to a north-south length and east-west width (Figure <a href="#fig:rotation" data-reference-type="ref" data-reference="fig:rotation">5</a>). Rotations are evenly distributed throughout the building stock due to a lack of available data for more detailed distributions. This will be improved if new data becomes available.

<figure id="fig:rotation" data-latex-placement="H">
<img src="figures/rotation_example.png" style="width:70.0%" />
<figcaption>Illustration of building rotation. (a) Buildings with either 90 or 270 degree rotation have a north-south length. (b) Buildings with either 0 or 180 degree rotation have an east-west length.</figcaption>
</figure>

## Floor Height

Floor height is represented in the models as floor-to-floor height. ComStock uses the floor-to-floor heights found in the DOE prototype buildings, which were established using expert opinion (Deru et al. 2011). These floor-to-floor heights are summarized in Table <a href="#tab:floor_height" data-reference-type="ref" data-reference="tab:floor_height">1</a>.

<div id="tab:floor_height">

|    **Building Type**     | **Floor-to-Floor Height (feet)** |
|:------------------------:|:--------------------------------:|
| Full Service Restaurant  |                10                |
|         Hospital         |                14                |
|       Large Hotel        |      Ground: 13; Upper: 10       |
|       Large Office       |                13                |
|      Medium Office       |                13                |
|        Outpatient        |                10                |
|      Primary School      |                13                |
| Quick Service Restaurant |                10                |
|          Retail          |                20                |
|     Secondary School     |                13                |
|       Small Hotel        |       Ground: 11; Upper: 9       |
|       Small Office       |                10                |
|        Strip Mall        |                17                |
|        Warehouse         |                28                |

Floor-to-Floor Heights by Building Type

</div>

## Number of Floors

ComStock assigns a number of floors to each model during the sampling process to create a distribution of building heights in the stock. This value represents the number of aboveground floors for a given model. No buildings in ComStock have belowground stories.

For most of the building types, we generated probability distributions based on county and building type using CoStar (CoStar 2018). We used HSIP (U.S. Department of Homeland Security 2012) for schools and hospitals, as neither are well-represented in CoStar.

Figure <a href="#fig:nfloors_dist" data-reference-type="ref" data-reference="fig:nfloors_dist">6</a> shows the breakdown of the national building stock by number of floors and building type.

<figure id="fig:nfloors_dist" data-latex-placement="H">
<img src="figures/nfloors.png" style="width:100.0%" />
<figcaption>Distribution of number of aboveground floors by building type. The x-axis represents the number of floors, and the y-axis represents the fraction of the building stock.</figcaption>
</figure>

## Window-to-Wall Ratio (WWR)

The ComStock window-to-wall ratio (WWR) assumptions were created as part of the EULP project. WWR is defined as the fraction of abovegrade wall area that is covered by fenestration. Previously, ComStock used the WWR from the DOE prototype building models. Although each building type had a different WWR, there was no variability within each building type, which is not representative of the building stock. To address this issue, we referenced the NFRC Commercial Fenestration Market Study conducted by Guidehouse (Ciraulo et al. 2021). The study characterized the national commercial window stock through data collection and analysis. Six primary data sources representing all regions of the United States were used in the study—a 2020 Guidehouse survey, NEEA CBSA, DOE Code Study, CAEUS, CBECS, and RECS (multifamily). A variety of window properties were collected, including WWR, number of panes, frame material, glazing type, low-emissivity coating, gas fill, and many others. In total, the database contained approximately 16,000 samples, each with an appropriate weighting factor based on the coverage, completeness, and fidelity of each data source. We incorporated the WWR results from this study into the ComStock model, and we may incorporate other fields in the future to further refine our window modeling methodology.

From the Guidehouse data, we developed a WWR distribution for each combination of building type, floor area, and vintage. We first analyzed the WWRs separately by building type, floor area, geographic location, and vintage to determine which filters were appropriate to use for the final distributions. Geographic location did not have a significant impact on WWR, so it was left out of the final distributions. As can be seen in Figures <a href="#fig:wwr_by_rentable_area" data-reference-type="ref" data-reference="fig:wwr_by_rentable_area">7</a> and <a href="#fig:wwr_by_building_vintage" data-reference-type="ref" data-reference="fig:wwr_by_building_vintage">8</a>, there is a noticeable change in the WWR of buildings built after 2014, indicating that new buildings are trending toward larger windows. Similarly, there is a distinct trend in the WWR as a function of floor area; larger buildings tend to have more windows. Whereas the previous methodology only varied WWR by building type, these new distributions introduce more WWR variability by considering vintage and floor area.

The WWR distributions for all buildings before and after incorporating the NFRC data are shown in Figure <a href="#fig:wwr_before_after_all_buildings" data-reference-type="ref" data-reference="fig:wwr_before_after_all_buildings">9</a>. The distinct bins in the graph are a result of the way WWR is binned in the CBECS Show Card: 0%–1% WWR is binned to 0.0, 2%–10% to 0.06, 11%–25% to 0.18, 26%–50% to 0.38, 51%–75% to 0.63, and 76%–100% to 0.88. The final distributions do not change the stock total energy consumption significantly, but they do add realistic variability within building types. For example, previously, all large offices had the same WWR of 0.15, whereas using the new distributions, large office WWRs vary from 0.01 to 0.88.

<figure id="fig:wwr_by_rentable_area" data-latex-placement="h">
<img src="figures/wwr_by_rentable_area.png" />
<figcaption>Window-to-wall ratio by rentable floor area.</figcaption>
</figure>

<figure id="fig:wwr_by_building_vintage" data-latex-placement="h">
<img src="figures/wwr_by_building_vintage.png" />
<figcaption>Window-to-wall ratio by building vintage.</figcaption>
</figure>

<figure id="fig:wwr_before_after_all_buildings" data-latex-placement="h!">
<img src="figures/wwr_before_after_all_buildings.png" />
<figcaption>Window-to-wall ratio distribution in all building types before and after incorporating NFRC data.</figcaption>
</figure>

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
