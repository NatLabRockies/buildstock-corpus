<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_8_service_water_heating.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_8_service_water_heating.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0a2f61f | corpus_path: technical_reference/documentation/reference_doc/4_8_service_water_heating.md | section: Service Water Heating Usage and Schedules | lines: 32-46 -->
## Service Water Heating Usage and Schedules

SWH usage for a given time step is based on a design peak gal/min flow rate multiplied by a usage fraction schedule. For example, if a given model has a design SWH flow rate of 10 gal/min, and the schedule value for the time step is 0.5, the SWH flow rate for the time step will be 5 gal/min. The flow rate values in ComStock come from the DOE prototype/reference building models, and are summarized in Tables “Service Water Heating Flow Rate and Schedule Assignments Based on Template, Building Type, and Space Type (Part 1 of 3)” through “Service Water Heating Flow Rate and Schedule Assignments Based on Template, Building Type, and Space Type (part 3 of 3)”.

In ComStock, the design flow rates are specified at the space type level. Then, these rates are aggregated to form a building-level design flow rate. The exception to this is SWH loads for kitchens, which are grouped into their own separate water heater system. These design flow rates are then multiplied by the usage fraction schedules, which specify the fraction of the design flow rate drawn for each time step. The usage fraction schedules in ComStock are derived from the DOE prototype/reference Buildings, and are summarized for each building type in Figures “SWH heating usage schedule for full service restaurants.” through  “SWH heating usage schedule for strip mall.”. The default schedule assignments for each space type and vintage are shown in Tables “Service Water Heating Flow Rate and Schedule Assignments Based on Template, Building Type, and Space Type (Part 1 of 3)” through  “Service Water Heating Flow Rate and Schedule Assignments Based on Template, Building Type, and Space Type (part 3 of 3)”. However, these schedules are modified according to the hours of operation of the building, as described in Section “Hours of Operation and Occupancy”.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-eia2012cbecs" class="csl-entry">

U.S. Energy Information Administration. 2012. *2012 Commercial Building Energy Consumption Survey (CBECS)*. Http://www.eia.doe.gov/emeu/cbecs/.

</div>

</div>
