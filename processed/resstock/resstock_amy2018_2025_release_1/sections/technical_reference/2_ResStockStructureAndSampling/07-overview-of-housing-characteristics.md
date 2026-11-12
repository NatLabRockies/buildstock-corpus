<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/2_ResStockStructureAndSampling.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/2_ResStockStructureAndSampling.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/2_ResStockStructureAndSampling.md | section: Overview of Housing Characteristics | lines: 121-223 -->
## Overview of Housing Characteristics

ResStock uses a set of conditional distributions to describe the characteristics of U.S. housing units and the households living in them. There are over [150 characteristics described in ResStock](https://github.com/NREL/resstock/tree/v3.3.0/project_national/housing_characteristics), the majority of which describe the physical attributes of the buildings. Some demographic household characteristics are also included as inputs, both to describe the demographics of the households (e.g., income and renter/owner status) as well as to differentiate key appliance ownership and building characteristic differences that exist between households of different demographics. Each sample in ResStock represents one housing unit (as opposed to a building with many housing units) and will have a value selected for every input housing characteristic defined in ResStock.

Table “Subset of Water Heating Fuel distribution” is an illustrative example of a conditional distribution table for the housing characteristic Water Heating Fuel. There are three parts to this table—options, dependencies, and sampling probability. The options are the values a characteristic parameter can take on (e.g., water heater fuel has the options: electricity, fuel oil, natural gas, other fuel, and propane). If one characteristic is described based on another, this is known as a dependency. The dependencies explain how the characteristic is distributed (e.g., Water Heater Fuel saturation varies based on Geometry Building Type RECS, Heating Fuel, and State). Since all buildings must receive a value assigned for a Water Heating Fuel option during sampling, the probabilities in the option columns are equal to one when summed row-wise. Each row gives the parameter distribution within a housing segment defined by the dependencies. For example, the Water Heating Fuel for Mobile Homes with a Heating Fuel of Electricity located in CA has a 72.37% probability of being Electricity, and a 17.59% probability of being Natural Gas. The *sampling_probability* column provides the likelihood of sampling a home with the dependency characteristics, i.e., the relative size of the housing segment in the United States. The column can be extended with the option probability (i.e., each value under the option column) to give the joint probability of sampling the characteristics of both the dependencies and the option. For example, Mobile Homes with a Heating Fuel of Electricity located in CA represent 0.09022% of the national residential housing units. Multiplying this by the 72.37% probability of these housing units having Electricity as their Water Heating Fuel, we determine that Mobile Homes with a Heating Fuel of Electricity located in CA and having a Water Heating Fuel of Electricity represent 0.06529% of the national residential housing stock.

<div id="tab:ex_whf_distr" data-source="2_ResStockStructureAndSampling.tex">

<table style="width:68%;">
<caption>Subset of Water Heating Fuel distribution</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Dependency=Geometry Building Type RECS</th>
<th style="text-align: left;">Dependency=<br />
Heating Fuel</th>
<th style="text-align: left;">Dependency=<br />
State</th>
<th style="text-align: left;">Option=<br />
Electricity</th>
<th style="text-align: left;">Option=<br />
Fuel Oil</th>
<th style="text-align: left;">Option=<br />
Natural Gas</th>
<th style="text-align: left;">Option=<br />
Other Fuel</th>
<th style="text-align: left;">Option=<br />
Propane</th>
<th style="text-align: left;">sampling<br />
_probability</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Mobile Home</td>
<td style="text-align: left;">Electricity</td>
<td style="text-align: left;">CA</td>
<td style="text-align: left;">0.7237</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0.1759</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0.1005</td>
<td style="text-align: left;">0.0009022</td>
</tr>
<tr>
<td style="text-align: left;">Multifamily with 2-4 Units</td>
<td style="text-align: left;">Electricity</td>
<td style="text-align: left;">CA</td>
<td style="text-align: left;">0.6379</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0.3621</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0.0026521</td>
</tr>
<tr>
<td style="text-align: left;">Multifamily with 5+ Units</td>
<td style="text-align: left;">Electricity</td>
<td style="text-align: left;">CA</td>
<td style="text-align: left;">0.5690</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0.4217</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0.0093</td>
<td style="text-align: left;">0.0113951</td>
</tr>
<tr>
<td style="text-align: left;">Single-Family Attached</td>
<td style="text-align: left;">Electricity</td>
<td style="text-align: left;">CA</td>
<td style="text-align: left;">0.6986</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0.2696</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0.0318</td>
<td style="text-align: left;">0.0019855</td>
</tr>
<tr>
<td style="text-align: left;">Single-Family Detached</td>
<td style="text-align: left;">Electricity</td>
<td style="text-align: left;">CA</td>
<td style="text-align: left;">0.3200</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0.6428</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">0.0372</td>
<td style="text-align: left;">0.0107185</td>
</tr>
</tbody>
</table>

</div>

