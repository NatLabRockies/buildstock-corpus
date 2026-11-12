<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Vacant Units | lines: 3410-3447 -->
## Vacant Units

ResStock models just over 12% of housing units as vacant nationally, reflecting the data in PUMS 2019. In PUMS, a housing unit is considered vacant if it is not occupied at the time of the survey. This includes housing units being prepared for rent or sale, units rented or sold but not yet occupied, or units for seasonal, occasional, or migratory use. The portion of housing units that are vacant is dependent on the building type and PUMA (i.e., location). While the vacancy saturation includes samples that are only vacant part time, ResStock models all vacant units as vacant for an entire calendar year.

In most cases ResStock models vacant units using the same characteristic distributions as occupied units. For example, RECS, where all of the respondents are unit occupants, does not have unoccupied units included in its survey. Tenure is a dependency in many of the appliance characteristics derived from RECS. In those characteristics distributions, Tenure=Not Available is analogous to vacant units and their distributions are based on the full dataset (i.e., the occupied units regardless of tenure). The distribution of Geometry Floor Area, however, which comes from 2017-2019 American Housing Survey, has a real distinction between renter-occupied, owner-occupied, and vacant units, as the survey records both tenure and vacancy information.

The differences between our modeling of occupied units and vacant units are currently confined to these areas: heating setpoint, schedule-driven loads and ceiling fans, PV, and demographics.

Vacant units are set to have a heating setpoint characteristic of 55° F, intended as a “don’t freeze the pipes” approach. Vacancy status is not in the dependency tree for the heating setpoint offset characteristics, so many vacant housing units are modeled with heating setpoint offsets from that 55° F.

Reflecting a lack of occupants, vacant units are modeled without any schedule-driven appliance usage. This results in no energy consumption for the following end uses across all fuels:

- Ceiling fan (albeit through a different mechanism)

- Clothes dryer

- Clothes washer

- Dishwasher

- Fireplace

- Grill

- Lighting (all types)

- Mechanical ventilation

- Well pump

- Plug loads

- Range/oven

- TVs.

There are also no PV systems modeled for vacant units. Because vacant units have no associated household—no set of people that live in them—their *occupants* characteristic is 0 and they do not have household-based characteristics such as *income* or *tenure*. All other characteristics, modeling approaches, and end uses are independent of vacancy status; that is, if the housing unit had the same characteristics and was occupied, it would have the same results.

