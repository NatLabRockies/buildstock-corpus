<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/5_outputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/5_outputs.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 43ae2d4 | corpus_path: technical_reference/documentation/reference_doc/5_outputs.md | section: Energy Consumption by Fuel and End Use | lines: 8-58 -->
## Energy Consumption by Fuel and End Use

ComStock provides energy consumption by fuel and end use at both an annual and time-series (typically 15-minute time steps for one year) resolution. Not all combinations of fuels and end uses are found in ComStock. The definitions below describe the fuels and end uses in detail.

ComStock provides modeled energy consumption for the following **fuels**:

- **Electricity**: This represents the electricity that is delivered to the building through the power grid and consumed on-site. How this electricity is generated depends on the generation mix found on the power grid in the region serving the building. This does not include electricity that is generated through a backup generator.

- **Natural Gas**: This represents the natural gas that is delivered to the building through the natural gas pipeline system and consumed on-site.

- **Propane**: This represents the propane that is delivered to the building in tanks and consumed on-site.

- **Fuel Oil**: This represents the liquid fuel oil that is delivered to the building, stored in tanks, and consumed on-site.

- **Other Fuel**: In some ComStock outputs, propane and fuel oil are combined and reported together as “other fuel” due to reporting limitations in the simulation engine. Where this is the case, propane and fuel oil are not reported separately to avoid double-counting.

- **District Heating**: This represents the hot water or steam that is delivered to the building through a district heating piping system and consumed on-site. The quantity of energy consumed represents only the energy extracted from the district heating system by the building; it does not represent the consumption of electricity or natural gas at the district heating plant required to provide heat to the building. In order to capture the energy consumption of the district heating plant, assumptions about distribution heat losses, pumping power, and district heating plant equipment efficiency and controls may be made.

- **District Cooling**: This represents the chilled water that is delivered to the building through a district cooling piping system and consumed on-site. The quantity of energy consumed represents only the energy extracted from the district cooling system by the building; it does not represent the consumption of electricity or natural gas at the district cooling plant required to provide chilled water to the building. In order to capture the energy consumption of the district cooling plant, assumptions about distribution heat gains, pumping power, and district cooling plant equipment efficiency and controls may be made.

ComStock provides modeled energy consumption for the following **end uses** for each applicable fuel:

- **Cooling**: This includes all energy consumed by primary cooling equipment such as chillers, direct expansion air conditioners (includes condenser fan energy), and direct expansion heat pumps in cooling mode (includes condenser fan energy). This also includes parasitic energy consumption of the equipment, such as pan heaters, defrost energy, and any energy needed to overcome modeled pipe losses.

- **Heating**: This represents all energy consumed by primary heating equipment such as boilers, furnaces, natural gas heating coils, electric resistance strip heating coils, and direct expansion heat pumps in heating mode (includes evaporator fan energy). This also includes parasitic energy consumption of the equipment, such as pilot lights, standby losses, defrost energy, and any energy needed to overcome modeled pipe losses.

- **Fans**: This includes all energy consumed by supply fans, return fans, exhaust fans, and kitchen hoods in the building. It excludes the condenser fan energy from direct expansion coils, which is captured in cooling and heating, as described above.

- **Pumps**: This includes all energy consumed by pumps for the purpose of moving hot water for heating and service water heating, chilled water for cooling, and condenser water for heat rejection.

- **Heat Recovery**: This includes the energy used to turn heat or enthalpy wheels, plus the increased fan energy associated with the increased pressure rise caused by the heat recovery wheels.

- **Heat Rejection**: This includes the energy used to run cooling towers and fluid coolers to reject heat from the condenser water loop to the air. As previously noted, condenser fans on direct expansion cooling and heating coils are included in heating and cooling.

- **Humidification**: This includes all energy used to purposely increase humidity in the building. Most buildings are assumed not to use humidification.

- **Water Systems**: This includes all energy consumed by the primary service hot water supply equipment, such as boilers and water heaters. This also includes parasitic energy consumption of the equipment, such as pilot lights, standby losses, and any energy needed to overcome modeled pipe losses.

- **Refrigeration**: This includes all energy used by large refrigeration cases and walk-ins such as those commonly found in grocery stores and large commercial kitchens. Plug-in refrigerators, such as those commonly found in the checkout areas of retail stores, are included in interior equipment.

- **Interior Lighting**: This includes all energy used to light the interior of the building, including general lighting, task lighting, accent lighting, and exit lighting.

- **Exterior Lighting**: This includes all energy used to light the exterior of the building and the surrounding area, including parking lot lighting, entryway illumination, and wall washing.

- **Interior Equipment**: This includes all energy used in the building that was not included in one of the other categories. This covers miscellaneous electric loads such as computers and monitors, large equipment such as elevators, and special-purpose equipment such as data center and IT-closet servers. This is a large and coarse bin, largely because the variety of energy-consuming devices found in buildings is large and little comprehensive data are available.

<figure id="fig:segments_typology">

<figcaption>Example ComStock Results</figcaption>
</figure>

