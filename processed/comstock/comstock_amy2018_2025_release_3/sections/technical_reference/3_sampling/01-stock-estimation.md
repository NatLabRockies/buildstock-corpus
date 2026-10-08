<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/3_sampling.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/3_sampling.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: b5faf42 | corpus_path: technical_reference/documentation/reference_doc/3_sampling.md | section: Stock Estimation | lines: 6-272 -->
## Stock Estimation

Any estimate of the energy consumption of the U.S. commercial building stock relies heavily on an estimate of how much floor area of each type of building exists in each part of the country. As shown by CBECS (U.S. Energy Information Administration 2018) and others, energy consumption of commercial buildings predominantly scales with floor area, not with building count. An accurate estimate of building floor area is therefore a critical input into any stock modeling tool focused on energy or energy-related metrics.

A secondary issue is the type of building associated with each floor area. Although accurately estimating the total floor area of commercial buildings is necessary, it is not sufficient, as building type also has an impact on energy use intensity (EUI), measured in units of energy use per square foot per year. As an example, a large office with a data center would be expected to have a dramatically higher electric load per square foot than an unconditioned warehouse.

The goal of the stock estimation process is to identify the type, floor area, and location of buildings across the United States. This task is complicated by a number of factors, including data sources that are inconsistent across the United States. However, floor area estimation is central to ensuring that ComStock is accurate for its intended use cases. ComStock takes a three step approach towards achieving an accurate estimate. To begin, national data sources are assembled to present overlapping (and often conflicting) reports of the U.S. commercial building stock. Second, the buildings reported by the various data sources are assigned a consistent set of type descriptors—e.g., large office or secondary school. Finally, the various data sets are amalgamated to create a final, consistent data set that is used in the sampling process.

### Data Sources

ComStock’s stock estimation is assembled using several data sources. The primary data sources are CoStar, a commercial building real estate intelligence broker, and Homeland Infrastructure Foundation-Level Data (HIFLD), a Department of Homeland Security database that provides cross-agency information on critical infrastructure assets across the United States. Both of these data sets, due to their business-/mission-driven use cases, tend to have very high accuracy for the buildings they represent. However, the major downside of both data sources is that the buildings they do not collect data on are not represented in any manner. While this is challenging, it is easier to adjust/correct for this sparsity than to use other data sets in which buildings are incorrectly and inconsistently represented.

CoStar is a “leading provider of commercial real estate data and marketplace listing platforms. Its data offerings contain in-depth analytical information on over five million commercial real estate properties related to various subsections, including office, retail, multifamily, healthcare, industrial, self-storage, and data centers” (CoStar 2020). CoStar’s data is driven by commercial leases and commercial sales data, and is updated with millions of dollars’ worth of research per year. CoStar’s data set is not always complete, both in terms of geography and building type. For example, building types that are rarely bought and sold, such as schools and major hospital complexes, are less likely to be represented in CoStar’s database.

HIFLD is a set of data tables assembled by the U.S. Department of Homeland Security to support critical infrastructure awareness, disaster recovery, and various other uses. Their databases include information on critical infrastructure facilities such as refineries and military bases, but also include information on schools (which are often used as disaster assistance centers) and hospitals. This is particularly useful, as these are two of the key building types that are less likely to be represented in CoStar. Although the schools data set provided by HIFLD always provides information on the number of students enrolled in a given school (which is used as a proxy to determine the floor area of the school when not otherwise available), the hospital table fails to report the number of beds in a given hospital (which is likewise used to scale floor area) in approximately half the states in the United States. In these cases, data from states that do report this information is generalized and used to infer the floor area in states without data.

Although both of these data sets provide excellent coverage of buildings they consider, they do not provide full and complete coverage of commercial buildings across the United States. Of particular note, using these two data sources results in an estimate of U.S. commercial buildings that differs from that published by CBECS. The ComStock team, after significant discussion, has decided to treat the CBECS estimate of the floor area of each building type as a truth data set. Following the sampling of the CoStar and HIFLD data sets, the CBECS estimates are used to “true up” the numbers on a national basis. As a result, ComStock’s floor area estimates match CBECS’ by building type on a national basis. Although other truth data sources were considered, CBECS’ centrality to all commercial energy use estimation made it the obvious and consistent choice for estimating the U.S. commercial building stock’s energy use.

### Building Type Assignments

Building type definitions frequently do not match across data sources. This is particularly noticeable in the case of CoStar, CBECS, and DOE prototype buildings data sources. The DOE prototype building models, discussed further in Section “Building Type”, defines specific combinations of space types as “building types,” which are then used by ComStock. The building types represented by the DOE prototype building models were decided on during the development of their precursors, the DOE reference building models (Deru et al. 2011). As such, “translating” building types across data sources introduces a layer of complexity.

ComStock maps the building type definitions from each data source to a specific building type from the DOE prototype buildings to maximize consistency. While these mappings are imperfect, they represent the best efforts of the ComStock team to capture the unique energy-related characteristics of different building types within the modeling framework created and used by DOE over the last 15 years. Table “Building Type Mapping Across Data Sources” shows the mapping from the CoStar building types and HIFLD tables to the DOE prototype buildings, and from the DOE prototype buildings to CBECS’ Principal Building Activity Plus.

<div id="tab:building_types" data-source="tables/building_type_cross_datasets.tex">

<table>
<caption>Building Type Mapping Across Data Sources</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>CoStar Building Type</strong></th>
<th style="text-align: left;"><strong>HIFLD Table</strong></th>
<th style="text-align: left;"><strong>DOE Prototype and ComStock Building Type</strong></th>
<th style="text-align: left;"><strong>CBECS Principle Building Activity Plus</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Retail: Bar</td>
<td rowspan="2" style="text-align: left;">Not applicable</td>
<td rowspan="2" style="text-align: left;">Full service restaurant</td>
<td style="text-align: left;">Restaurant/cafeteria</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Retail: Restaurant</td>
<td style="text-align: left;">Bar/pub/lounge</td>
</tr>
<tr>
<td style="text-align: left;">Not applicable</td>
<td style="text-align: left;">Healthcare: Hospitals</td>
<td style="text-align: left;">Hospital</td>
<td style="text-align: left;">Hospital/inpatient health</td>
</tr>
<tr>
<td style="text-align: left;">Hospitality: Hotel</td>
<td rowspan="12" style="text-align: left;">Not applicable</td>
<td rowspan="2" style="text-align: left;">Large hotel</td>
<td rowspan="2" style="text-align: left;">Hotel</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Hospitality: Hotel casino</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Office: Industrial live/work unit</td>
<td rowspan="6" style="text-align: left;">Office</td>
<td style="text-align: left;">Administrative/professional office</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Office: Office live/work unit</td>
<td style="text-align: left;">Bank/other financial</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Office: Office/residential</td>
<td style="text-align: left;">Government office</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Retail: Bank</td>
<td style="text-align: left;">Medical office (non-diagnostic)</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Flex</td>
<td rowspan="2" style="text-align: left;">Other office</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Office: Service</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Health care: Rehabilitation center</td>
<td rowspan="4" style="text-align: left;">Outpatient</td>
<td rowspan="2" style="text-align: left;">Medical office (diagnostic)</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Health care: Skilled nursing facility</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Office: Medical</td>
<td rowspan="2" style="text-align: left;">Clinic/other outpatient health</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Health care</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">Not applicable</td>
<td style="text-align: left;">Education: Public schools</td>
<td rowspan="2" style="text-align: left;">Primary/secondary school</td>
<td style="text-align: left;">Elementary/middle school</td>
</tr>
<tr>
<td style="text-align: left;">Education: Private schools</td>
<td style="text-align: left;">High school</td>
</tr>
<tr>
<td style="text-align: left;">Retail: Fast food</td>
<td rowspan="25" style="text-align: left;">Not applicable</td>
<td rowspan="2" style="text-align: left;">Quick service restaurant</td>
<td rowspan="2" style="text-align: left;">Fast food</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> General retail: Fast rood</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Retail: Department store</td>
<td rowspan="4" style="text-align: left;">Retail</td>
<td rowspan="2" style="text-align: left;">Retail store</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Retail: Freestanding</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Retail: Garden center</td>
<td rowspan="2" style="text-align: left;">Other retail</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> General retail: Freestanding</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Hospitality: Motel</td>
<td rowspan="2" style="text-align: left;">Small hotel</td>
<td rowspan="2" style="text-align: left;">Motel or inn</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Hospitality</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Flex: Showroom</td>
<td rowspan="7" style="text-align: left;">Strip mall</td>
<td rowspan="7" style="text-align: left;">Strip shopping mall</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Retail: Storefront</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Retail: Storefront retail/office</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Retail: Storefront retail/residential</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Specialty: Post office</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Retail</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> General retail</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Flex: Light distribution</td>
<td rowspan="9" style="text-align: left;">Warehouse</td>
<td rowspan="3" style="text-align: left;">Distribution/shipping center</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Flex: Light manufacturing</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Industrial: Distribution</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Industrial: Service</td>
<td rowspan="3" style="text-align: left;">Nonrefrigerated warehouse</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Industrial: Showroom</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Industrial: Truck terminal</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Industrial: Warehouse</td>
<td rowspan="3" style="text-align: left;">Self-storage</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Specialty: Airplane hangar</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Specialty: Self-storage</td>
</tr>
<tr>
<td style="text-align: left;">Retail: Supermarket</td>
<td style="text-align: left;">Grocery</td>
<td style="text-align: left;">Grocery store</td>
</tr>
</tbody>
</table>

</div>

It is important to note that only one of either the CoStar or HIFLD data is used to represent each type of DOE prototype building—that is, no building type is pulled from both data sets. This ensures that any errors that exist in either data set are independently corrected by the CBECS normalization. According to CBECS’ estimation, the amalgamation of these three data sets accounts for 63% of the energy use and 63% of the floor area of commercial buildings in the United States. The remaining 37% of energy use not represented is due to several CBECS building types that are not included in ComStock yet such as mixed-use office and religious worship. Figure “CBECS Principal Buildings Activity Plus building types not covered by ComStock on an energy use basis.” shows the building types not represented in the ComStock model, on a CBECS Principal Building Activity Plus basis, and their relative contribution to the commercial building energy use in the United States. As can be seen in the figure, mixed-use offices represent the largest un-modeled building classification by energy use, followed by recreation, other, religious worship, nursing home/assisted living, and social/meeting buildings. Although these building types all consume energy, the ComStock team does not have sufficient information to make a reasonable estimate of their energy use, either annually or on a time-series basis, using the approach discussed in Section “Space Type Ratios”.

<figure id="fig:types_not_represented">
<img src="figures/cbecs_2018_comstock_coverage.png" />
<figcaption>CBECS Principal Buildings Activity Plus building types not covered by ComStock on an energy use basis.</figcaption>
</figure>

DOE prototype building type is used to represent a significant amount of the U.S. building stock but is also not used in many cases due to concerns regarding its accurate representation of specific building sub-types. The following list discusses each building type, and what buildings it does and does not represent, as understood by ComStock’s developers.

Full Service Restaurant
Both sit-down restaurants and bars are included in this category, as both typically require significant cooking and sanitation equipment for their operation.

Grocery Store
Grocery stores, also commonly referred to as supermarkets, are buildings whose primary purpose is the sale of food and dry goods rather than general merchandise. This category includes facilities that feature extensive refrigerated and frozen storage, fresh produce, and prepared foods, typically supported by substantial lighting, heating, ventilation, and refrigeration equipment loads. Convenience stores, small specialty food shops, and general merchandise retailers that include grocery sections are not represented by this category.

Hospital
Hospitals, wherever possible, are disambiguated from outpatient clinics through the existence of around-the-clock medical facilities. This is not possible in many states, in which case the differentiation is based on available CoStar data.

Large Hotel
Large hotels are differentiated from small hotels on the basis of conference or casino spaces. Hotels that have major facilities for conferences, events, or gambling are classified as large hotels.

Offices
Offices are divided up into three subsets: small, medium, and large. Each type of office is based on the thresholds used by American Society of Heating, Refrigerating and Air-Conditioning Engineers (ASHRAE) Appendix G (ASHRAE 2010), which include both size and number of stories. In the case of large offices, there are additional probability distributions that determine what percent (if any) of the office is a data center.

Outpatient
Outpatient facilities, as represented in ComStock, include non-hospital medical centers, rehabilitation centers, and medical offices.

Primary School
The primary school type is used to represent all schools that do not include secondary or post-secondary education, i.e., grades 9 and beyond. Schools that provide education for pre-secondary to post-secondary students (e.g., grades 5-12) are classified as secondary schools. This grouping means that any daycare facilities classified as schools by HIFLD are included as primary schools, unless the facilities also support secondary students.

Quick Service Restaurant
Quick service restaurants consist entirely of fast food restaurants.

Retail
This category predominantly features large national retailers, excluding grocery stores. This includes big box stores, garden centers, department stores, and any other freestanding retailers that do not include a significant grocery section.

Secondary School
Secondary schools incorporate all schools that offer instruction to pupils in grades 9-12. No post-secondary institutions (e.g., community colleges and universities) are represented by ComStock unless they fall into another building type defined herein.

Small Hotel
Small hotels encompass all hotels that do not have significant spaces for conferences, meetings, or gambling.

Strip Mall
Strip malls encompass all multi-tenant retail buildings, as well as single-tenant buildings that are not classified as large retailers, such as post offices, showrooms, etc. These buildings have additional probability distributions that determine how much of the building floor area (if any) is a restaurant. This is critically important, as restaurants have a far higher EUI and as a result can cause strip malls to have far higher energy uses than would otherwise be expected in a stand alone retail building.

Warehouse
Warehouses are perhaps the most differentiated building type in the commercial building stock. They are represented in ComStock as a conjunction of office spaces and high-bay spaces. This building type is used to model distribution centers, light manufacturing, and some showroom and truck terminal spaces, as well as airplane hangars, service depots, and self-storage centers. The spaces encompass a large number of functions; however, it is difficult to differentiate these spaces when examining national databases of building stock characteristics. This makes further disambiguation of these buildings impossible without additional data sources.

### Data Amalgamation for Sampling

The data from CoStar and HIFLD were converted from individual building data points to probability distributions for geographic areas due to data retention clauses.

The ComStock team tagged all individual buildings with a climate zone and a county to convert the county-level locations of buildings within the United States into a probability distribution. From this data, one distribution was created: the likelihood of a building in the United States being located in a given climate zone. In this distribution, there is a much higher likelihood of being located in a heavily populated climate zone (like 4A, which includes much of NJ, DC, MD, DE, VA, etc.) than a sparsely populated climate zone (like 8, which includes only part of AK). Next, for each climate zone, another distribution was created: the likelihood of a building being located in each county within that climate zone. In these distributions, there is a much higher likelihood of being located in a heavily populated county than a sparsely populated county. These two sets of distributions allow any ComStock sample to be assigned a climate zone and a county prior to any additional characteristics being calculated.

The next characteristic to be described as a probability distribution was the building type. Based on the combined CoStar and HIFLD data sets, the likelihood of a building being of a specific building type was calculated for each county in the United States. In some cases, the county in question had an insufficient number of buildings in CoStar and HIFLD to create a realistic distribution. In these cases, the county was instead assigned a distribution of building types based on all the buildings in the state. This is not frequently required for building type, but is more common for floor area, vintage, and number of stories (discussed next).

Probability distributions for three additional characteristics were created using the HIFLD and CoStar data sets: floor area, vintage, and number of stories. CoStar’s database has excellent coverage of floor area of a building as a function of county and building type, good coverage of vintage (the year the building was constructed), and reasonable coverage of the number of stories. HIFLD, on the other hand, has good information on vintage, but not on floor area or the number of stories. For floor area, inferences were based on the number of students enrolled (for schools) and the number of beds (for hospitals). Where information on the number of beds was missing, the aggregate distribution for the United States was used to infer the floor area. The number of stories was estimated based on the inferred floor area for each hospital/school. These estimates, as well as the estimates provided by the CoStar data, were used to create distributions for each building type’s characteristics on a county basis. There were several cases in which one or more characteristics could not be accurately estimated for a building type/county pair. In these cases, the aforementioned approach of using the state-level distribution was employed.

The approach employed is mathematically accurate. However, the downside to using building count when creating probability distributions is that a high sample count is required to ensure that less common but highly impactful buildings, such as buildings over one million square feet, are well represented. For example, if a county contains 100 retail stores with a floor area of 1,000 square feet each (for a total of 100,000 square feet) and one retail store (perhaps a mall) of one million square feet, the large retail store would be expected to use roughly ten times (1,000,000 square feet/ 100,000 square feet) the energy of all of the smaller retail stores put together. With the current count-based approach, around 100 samples would need to be generated from this distribution to ensure that the one million square foot retail store was represented in the model. Although the impacts of this are minimal at a higher geographic level, it is a known weakness of the current approach.

