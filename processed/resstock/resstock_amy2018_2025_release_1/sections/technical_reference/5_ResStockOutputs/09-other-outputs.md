<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/5_ResStockOutputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/5_ResStockOutputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/5_ResStockOutputs.md | section: Other Outputs | lines: 482-534 -->
## Other Outputs

The ResStock workflow can optionally output any variable available in EnergyPlus. We regularly use this capability for a variety of purposes, including modeling improvement and validation, debugging, special purpose variables for specific projects, and additional variables to publish as part of public datasets.

Table “Other ResStock results output field names, units, and descriptions” shows a list of output variables that are not covered in other headings in this section but that we have typically included in many of our recent public datasets, where they begin with “out.x.”

<div id="tab:other_outputs" data-source="5_ResStockOutputs.tex">

| **Field Name** | **Units** | **Field Description** |
|:---|:---|:---|
| out.cooling_unavailable_period |  | Cooling unavailable period. |
| out.electricity.summer.peak.kw | kW | Maximum power value in Jun/Jul/Aug |
| out.electricity.winter.peak.kw | kW | Maximum power value in Dec/Jan/Feb |
| out.heating_unavailable_period |  | Heating unavailable period. |
| out.hot_water.clothes_washer.gal | gal | Hot water consumed by clothes washer |
| out.hot_water.dishwasher.gal | gal | Hot water consumed by dishwasher |
| out.hot_water.distribution_waste.gal | gal | Hot water consumed by water distribution system (water remaining in the pipe) |
| out.hot_water.fixtures.gal | gal | Hot water consumed by showers, sinks, and baths |
| out.params.size_water_heater_gal | gal | Size of water heater |
| out.load.cooling.energy_delivered.kbtu | kbtu | Total energy delivered by cooling system includes HVAC distribution losses |
| out.load.cooling.peak.kbtu_hr | kbtu/hr | Maximum cooling load delivered by cooling system includes HVAC distribution losses |
| out.load.heating.energy_delivered.kbtu | kbtu | Total energy delivered by heating system includes HVAC distribution losses |
| out.load.heating.peak.kbtu_hr | kbtu/hr | Maximum heating energy delivered by heating system includes HVAC distribution losses over a 60 min time period |
| out.load.hot_water.energy_delivered.kbtu | kbtu | Total energy delivered by hot water system includes contributions by desuperheaters or solar thermal systems |
| out.unmet_hours.cooling.hour | hr | Number of hours where the cooling setpoint is not maintained |
| out.unmet_hours.heating.hour | hr | Number of hours where the heating setpoint is not maintained |
| weight | n/a | the number of housing units the sample represents |

Other ResStock results output field names, units, and descriptions

</div>

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-Gagnon2025" class="csl-entry">

Gagnon, Pieter, {Pedro Andres} {Sanchez Perez}, Julian Florez, James Morris, Marck {Llerena Velasquez}, and Jordan Eisenman. 2025. *Cambium 2024 Scenario Descriptions and Documentation*. Other. <https://doi.org/10.2172/2558937>.

</div>

<div id="ref-RESNET2022" class="csl-entry">

Network, Residential Energy Services. 2022. *PDS-01, BSR/RESNET/ICC 301-2022 Addendum b, CO2 Index.* <https://www.resnet.us/wp-content/uploads/FS_301-2022AdndmB_v.2-1.pdf>.

</div>

<div id="ref-Present2024" class="csl-entry">

Present, E., P. R. White, C. Harris, et al. 2024. *ResStock Dataset 2024.1 Documentation*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy24osti/88109.pdf>.

</div>

</div>
