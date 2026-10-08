<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_7_plug_and_process.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_7_plug_and_process.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 267e3ea | corpus_path: technical_reference/documentation/reference_doc/4_7_plug_and_process.md | section: Kitchen Equipment | lines: 109-300 -->
## Kitchen Equipment

Kitchens are one of the most energy-intensive space types. In ComStock, kitchen space types are modeled in six building types—FullServiceRestaurant, Hospital, LargeHotel, PrimarySchool, QuickServiceRestaurant, and SecondarySchool. In some building types, namely restaurants, the kitchen space type represents a significant proportion of the floor area. In these cases, kitchen loads have a major impact on the total building EUI. In hotels, hospitals, and schools, the kitchen space type only represents a small fraction of the total floor area. Table <a href="#tab:kitchen_floor_area" data-reference-type="ref" data-reference="tab:kitchen_floor_area">2</a> shows the percent of the total floor area represented by the kitchen space type for each building type. Note that some of the strip malls in ComStock contain some fraction of the "QuickServiceRestaurant" building type to account for food service that is often found in strip malls.

<div id="tab:kitchen_floor_area">

| **Building Type**      | **Space Type** | **Percentage of Total Floor Area** |
|:-----------------------|:---------------|:-----------------------------------|
| FullServiceRestaurant  | Kitchen        | 27.3%                              |
| Hospital               | Kitchen        | 4.1%                               |
| LargeHotel             | Kitchen        | 0.9%                               |
| PrimarySchool          | Kitchen        | 2.4%                               |
| QuickServiceRestaurant | Kitchen        | 50%                                |
| SecondarySchool        | Kitchen        | 1.1%                               |

Kitchen Space Type Percentage of Total Floor Area

</div>

Commercial building energy modeling often assumes an energy intensity per area for cooking equipment, like what is used in the DOE prototype buildings ((Zhang et al. 2010)). However, applying these power densities directly to the various building sizes in ComStock assumes cooking loads scale linearly with kitchen square footage, which does not necessarily represent reality ((U.S. Energy Information Administration 2012), (Zhang et al. 2010)). Further, it does not allow for straightforward analysis of specific cooking equipment since it is represented by a single aggregate load. However, little information exists regarding representative equipment-specific modeling of cooking appliances, as well as how cooking equipment scales with building area. The CBECS survey does provide some level of guidance for area-based intensity as they disaggregate cooking energy consumption separately and provide building area for their samples, but this end use energy consumption data is derived using statistical means from monthly billing data rather than directly measured making it less reliable ((U.S. Energy Information Administration 2012), (Zhang et al. 2010)).

ComStock uses published data to create representative probability distributions of commercial cooking equipment counts, by building type, for both gas and electric appliances. Additionally, the equipment distributions are scaled by area to represent the non-linear scaling suggested in the literature. Although other building types likely include some degree of cooking equipment as well, such as larger offices ((U.S. Energy Information Administration 2012)), the current implementation of ComStock only includes cooking equipment in the previously-mentioned six building types plus quick service restaurants found in strip malls.

Commercial kitchens can contain electric or gas cooking equipment, or a mix of both. The prevalence of gas and electric fuel types for each equipment type used in ComStock are derived from a DOE study ((Goetzler et al. 2016)). ComStock requires rated input power values and fractions of radiant, latent, and lost heat for gas and electric kitchen equipment. These values are primarily derived from the ASHRAE Fundamentals Handbook ((American Society of Heating and Air-Conditioning Engineers 2017)) after comparisons with other kitchen equipment studies and commercially available products. More details about how these values were determined can be found in the End Use Savings Shapes documentation ((Praprost 2024)).The assumptions used in ComStock for prevalence, rated input power, and fractions radiant, latent, and lost for gas and electric appliances are shown in Table <a href="#tab:kitchen_prev_and_power" data-reference-type="ref" data-reference="tab:kitchen_prev_and_power">3</a>.

<div id="tab:kitchen_prev_and_power">

<table>
<caption>Cooking Equipment Fuel Type Prevelance and Rater Power</caption>
<thead>
<tr>
<th style="text-align: center;"><strong>Appliance</strong></th>
<th colspan="2" style="text-align: center;"><strong>Fuel Prevalence Fraction</strong></th>
<th colspan="2" style="text-align: center;"><strong>Rated Power</strong></th>
<th colspan="2" style="text-align: center;"><strong>Fraction Radiant</strong></th>
<th colspan="2" style="text-align: center;"><strong>Fraction Latent</strong></th>
<th colspan="2" style="text-align: center;"><strong>Fraction Lost</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><span>2-11</span></td>
<td style="text-align: left;"><strong>Gas</strong></td>
<td style="text-align: left;"><strong>Electric</strong></td>
<td style="text-align: left;"><strong>Gas (Btu/h)</strong></td>
<td style="text-align: left;"><strong>Electric (kW)</strong></td>
<td style="text-align: left;"><strong>Gas</strong></td>
<td style="text-align: left;"><strong>Electric</strong></td>
<td style="text-align: left;"><strong>Gas</strong></td>
<td style="text-align: left;"><strong>Electric</strong></td>
<td style="text-align: left;"><strong>Gas</strong></td>
<td style="text-align: left;"><strong>Electric</strong></td>
</tr>
<tr>
<td style="text-align: left;">Broiler</td>
<td style="text-align: left;">0.91</td>
<td style="text-align: left;">0.09</td>
<td style="text-align: left;">96,000</td>
<td style="text-align: left;">10.8</td>
<td style="text-align: left;">0.12</td>
<td style="text-align: left;">0.35</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.68</td>
<td style="text-align: left;">0.45</td>
</tr>
<tr>
<td style="text-align: left;">Griddle</td>
<td style="text-align: left;">0.58</td>
<td style="text-align: left;">0.42</td>
<td style="text-align: left;">90,000</td>
<td style="text-align: left;">17.1</td>
<td style="text-align: left;">0.18</td>
<td style="text-align: left;">0.39</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.62</td>
<td style="text-align: left;">0.41</td>
</tr>
<tr>
<td style="text-align: left;">Fryer</td>
<td style="text-align: left;">0.5</td>
<td style="text-align: left;">0.5</td>
<td style="text-align: left;">80,000</td>
<td style="text-align: left;">14</td>
<td style="text-align: left;">0.23</td>
<td style="text-align: left;">0.36</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.57</td>
<td style="text-align: left;">0.44</td>
</tr>
<tr>
<td style="text-align: left;">Oven</td>
<td style="text-align: left;">0.55</td>
<td style="text-align: left;">0.45</td>
<td style="text-align: left;">44,000</td>
<td style="text-align: left;">12.1</td>
<td style="text-align: left;">0.08</td>
<td style="text-align: left;">0.22</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.72</td>
<td style="text-align: left;">0.58</td>
</tr>
<tr>
<td style="text-align: left;">Range</td>
<td style="text-align: left;">0.91</td>
<td style="text-align: left;">0.09</td>
<td style="text-align: left;">145,000</td>
<td style="text-align: left;">21</td>
<td style="text-align: left;">0.11</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.69</td>
<td style="text-align: left;">0.7</td>
</tr>
<tr>
<td style="text-align: left;">Steamer</td>
<td style="text-align: left;">0.33</td>
<td style="text-align: left;">0.67</td>
<td style="text-align: left;">200,000</td>
<td style="text-align: left;">27</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.1</td>
<td style="text-align: left;">0.7</td>
<td style="text-align: left;">0.7</td>
</tr>
</tbody>
</table>

</div>

Kitchens in ComStock models are assigned a quantity of each equipment type. These can be found in the ComStock metadata files for each model. Equipment quantities are assigned using probability distribtuions with dependencies on building type and food service floor area. The quantities used in the probability distributions are determined using an older dataset of equipment counts per restaurant type combined with the prevalence of the restaurant type ((Rahbar et al. 1996)). The restaurant types were mapped to ComStock building types. This is summarized in Table <a href="#tab:kitchen_cook_counts" data-reference-type="ref" data-reference="tab:kitchen_cook_counts">[tab:kitchen_cook_counts]</a>. Unfortunately, little data of this type was found in literature, so this older source was ultimately used for equipment counts. However, even with changes in culinary trends, it is not expected that counts of equipment types in a restaurant would have changed drastically over the past few decades. Additionally, a “None” restaurant type was created for schools, with a prevalence determined by the fraction of schools in CBECS that have kitchens ((U.S. Energy Information Administration 2012)).

This workflow also includes modifiers to the equipment counts shown in Table <a href="#tab:kitchen_cook_counts" data-reference-type="ref" data-reference="tab:kitchen_cook_counts">[tab:kitchen_cook_counts]</a> to scale equipment count for different kitchen sizes. As mentioned previously, it is not expected that equipment scales linearly with kitchen size, but there is little information in the literature to suggest appropriate scaling ((Zhang et al. 2010)). To account for equipment count scaling, we assume most typically-sized kitchens will have the same quantity of equipment. However, especially small and large kitchens will include scaling factors to account for very large changes in kitchen area that would likely correlate to higher/lower meals served. These factors were determined using engineering judgment and are summarized in Figure <a href="#fig:cooking_equipment_count_scaling_factors_by_building_type_and_area" data-reference-type="ref" data-reference="fig:cooking_equipment_count_scaling_factors_by_building_type_and_area">2</a>.

In summary, ComStock determines quantity and fuel type of cooking equipment based on sampling our probability distributions. A restaurant type is sampled for each model as per the prevenances shown by building type in Table <a href="#tab:kitchen_cook_counts" data-reference-type="ref" data-reference="tab:kitchen_cook_counts">[tab:kitchen_cook_counts]</a>. This yields the corresponding equipment counts for the restaurant type shown in Table <a href="#tab:kitchen_cook_counts" data-reference-type="ref" data-reference="tab:kitchen_cook_counts">[tab:kitchen_cook_counts]</a>, with square footage modifiers applied based on building size and type. Next, the equipment fuel type is sampled as per the prevalence shown in Table <a href="#tab:kitchen_prev_and_power" data-reference-type="ref" data-reference="tab:kitchen_prev_and_power">3</a> for each piece of equipment. Combined, this yields quantities of gas and electric cooking equipment for each ComStock sample. Note that kitchen spaces in ComStock additionally include some prevalence of electric load to account for non-major electrical appliances such as microwaves, heating lamps, toasters, coffee machines, electric kettles, etc. Additionally, the current implementation of cooking equipment in ComStock utilizes the same schedule for each equipment type. Future work could include implementing equipment-specific schedules for the various equipment types, which may better represent reality.

<figure id="fig:cooking_equipment_count_scaling_factors_by_building_type_and_area" data-latex-placement="ht!">
<img src="figures/kitchen_equipment_count_scaling.png" />
<figcaption>Cooking equipment count scaling factors by building type and area.</figcaption>
</figure>

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-ashrae2017" class="csl-entry">

American Society of Heating, Refrigerating, and Inc. Air-Conditioning Engineers. 2017. *ASHRAE Handbook - Fundamentals*. American Society of Heating, Refrigerating,; Air-Conditioning Engineers, Inc.

</div>

<div id="ref-osti_1129366" class="csl-entry">

Goel, Supriya, Rahul A. Athalye, Weimin Wang, et al. 2014. *Enhancements to ASHRAE Standard 90.1 Prototype Building Models*. Pacific Northwest National Laboratory. <https://doi.org/10.2172/1129366>.

</div>

<div id="ref-goetzler_commercial_appliances" class="csl-entry">

Goetzler, W., M. Guernsey, K. Foley, J. Young, and G. Chung. 2016. *Energy Savings Potential and RD&d Opportunities for Commercial Building Appliances (2015 Update)*. U.S. Department of Energy. <https://www.energy.gov/sites/prod/files/2016/06/f32/DOE-BTO%20Comml%20Appl%20Report%20-%20Full%20Report_0.pdf>.

</div>

<div id="ref-nrel89130" class="csl-entry">

Praprost, Marlena. 2024. *End-Use Savings Shapes Measure Documentation: Electric Cooking Equipment*. Technical Report No. 89130. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy24osti/89130.pdf>.

</div>

<div id="ref-com_food_service_equip" class="csl-entry">

Rahbar, Shahrzad, Senka Krsikapa, Don Fisher, Judy Nickel, Scot Ardley, and David Zabrowski. 1996. *Technology Review of Commercial Food Service Equipment*. Natural Resources Canada. <https://www.osti.gov/etdeweb/servlets/purl/404139>.

</div>

<div id="ref-eia2012cbecs" class="csl-entry">

U.S. Energy Information Administration. 2012. *2012 Commercial Building Energy Consumption Survey (CBECS)*. Http://www.eia.doe.gov/emeu/cbecs/.

</div>

<div id="ref-qsr_50pct_svs" class="csl-entry">

Zhang, J., DW. Schrock, DR. Fisher, et al. 2010. *Technical Support Document: 50% Energy Savings for Quick-Service Restaurants*. Pacific Northwest National Laboratory. <https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-19809.pdf>.

</div>

</div>
