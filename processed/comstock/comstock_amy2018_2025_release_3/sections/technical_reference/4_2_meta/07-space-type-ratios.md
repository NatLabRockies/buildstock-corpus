<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_2_meta.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_2_meta.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: b5faf42 | corpus_path: technical_reference/documentation/reference_doc/4_2_meta.md | section: Space Type Ratios | lines: 154-174 -->
## Space Type Ratios

A space type refers to a portion of a building that has a distinct usage, purpose, occupancy schedule, thermostat set point, etc. Most buildings have multiple space types. For example, schools typically have classrooms, hallways, restrooms, cafeterias, etc. In ComStock, each building type is assumed to have a fixed ratio of various space types relative to the total building floor area. For buildings outside of California, the space type ratios were largely taken from the DOE commercial reference building models (Deru et al. 2011b). For buildings in California, the space type ratios were largely taken from the DEER prototype models (California Public Utilities Commission 2021). There are certain building types that have altered ratios or are a mix of building types. For example in ComStock, warehouses include both unconditioned storage facilities and light manufacturing. Warehouse building subtypes alter the ratio of bulk storage. Retail strip mall buildings have different ratios of restaurant space types, with the default being 20%. Two examples of space type ratios are shown in Table “Space Type Ratio Example”. See Table “Space Type Ratios” for the space type ratios for all building types.

<div id="tab:space_type_ratios" data-source="tables/space_type_ratios.tex">

| **Building Type** | **Building Subtype**    | **Space Type**      | **Ratio** |
|:------------------|:------------------------|:--------------------|:---------:|
| Warehouse         | warehouse_default       | Bulk                |    66%    |
| Warehouse         | warehouse_default       | Fine                |    29%    |
| Warehouse         | warehouse_default       | Office              |    5%     |
| Retail Strip Mall | strip_mall_restaurant20 | Strip mall - type 1 |    20%    |
| Retail Strip Mall | strip_mall_restaurant20 | Strip mall - type 2 |    20%    |
| Retail Strip Mall | strip_mall_restaurant20 | Strip mall - type 3 |    40%    |
| Retail Strip Mall | strip_mall_restaurant20 | Dining              |    15%    |
| Retail Strip Mall | strip_mall_restaurant20 | Kitchen             |    5%     |

Space Type Ratio Example

</div>

