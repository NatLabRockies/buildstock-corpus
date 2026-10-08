<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/5_outputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/5_outputs.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: fadc83e | corpus_path: technical_reference/documentation/reference_doc/5_outputs.md | section: Greenhouse Gas Emissions Reporting | lines: 130-164 -->
## Greenhouse Gas Emissions Reporting

ComStock calculates the greenhouse gas emissions from the building stock and savings from measures using both historical and projected emissions data.

### Electricity Emissions

#### eGRID Historical Emissions

Historical emissions use the CO<sub>2</sub>-equivalent total output emission rate from EPA’s Emissions and Generation Resource Integrated Database (eGRID)(U.S. Environmental Protection Agency (EPA) 2022). ComStock results include the historical emissions for 2018, 2019, 2020, and 2021 using eGRID U.S. state and eGRID subregion emissions factors. eGRID regions are similar to Cambium grid regions but not identical. Notably, eGrid separates out New York into upstate, New York City, and Long Island. Cambium uses a whole-state average, and historical emissions use the New York state average instead of the grid region for New York buildings. Historical eGrid emissions rates are an *annual* average multiplied by the total annual electricity use.

#### Cambium Projected Emissions

Projected emissions use data from NREL’s Cambium 2022 data set (Gagnon et al. 2023). Projected emissions consider both the average emissions rate (AER) and the long-run marginal emission rate (LRMER). LRMER, described in (Gagnon and Cole 2022), is an estimate of the rate of emissions that would be either induced or avoided by a long-term (i.e., more than several years) change in electrical demand. LRMER data is levelized over 15 and 30 years(Gagnon et al. 2023). ComStock results including End Use Savings Shapes round 1 results and earlier projects used emissions factors from the Cambium 2021 data (Gagnon et al. 2021),(Gagnon et al. 2022).

### On Site Fossil Fuel Emissions

Natural gas, propane, and fuel oil emissions use the emission factors in *Table 7.1.2(1) of draft National Average Emission Factors for Household Combustion Fuels* defined in *ANSI/RESNET/ICCC 301-2022 Addendum B-2022 Standard for the Calculation and Labeling of the Energy Performance of Dwelling and Sleeping Units using an Energy Rating Index*. Natural gas emissions include both combustion and pre-combustion emissions (e.g., methane leakage for natural gas).

On-Site Fossil Fuel Emissions Factors:\
Natural gas: 147.3 lb/MMBtu (228.0 kg/MWh)\
Propane: 177.8 lb/MMBtu (275.7 kg/MWh)\
Fuel oil: 195.9 lb/MMBtu (303.2 kg/MWh)\

### District Energy Emissions

District heating and cooling emissions use the emissions factors defined in the August 2024 version of the *Energy Star Portfolio Manager Technical Reference* available at <https://portfoliomanager.energystar.gov/pdf/reference/Emissions.pdf>. The district heating emissions factor is the same for both steam and hot water. The district cooling emissions factor assumes district chilled water served by electric driver chillers. The emissions factors were originally sourced from EIA data for district chilled water and the EPA voluntary reporting program for district steam and hot water. These district emissions factors do not include upstream methane leakage. There is considerable variation by location and type of district system, so you may need to scale the results by factors specific to your region or system.

On-Site Fossil Fuel Emissions Factors:\
District Cooling: 52.70 kg/MMBtu\
District Heating: 66.40 kg/MMBtu\

### Air Pollution from On Site Fossil Fuel Combustion

ComStock reports annual pollution emissions for NOx, CO, PM, SO2 from on-site combustion of natural gas, propane, and fuel oil. Emission factors are from U.S. EPA *AP-42: Compilation of Air Emissions Factors from Stationary Sources*(U.S. Environmental Protection Agency (EPA) 2024). Natural gas emissions use emissions factors from AP-42 Table 1.4-2 and particulate emissions are reported as *total* PM. Propane emissions use emissions factors from AP-42 Table 1.5-1 and particulate emissions are reported as *total* PM. Fuel oil emissions use emissions factors for No.2 fuel oil from AP-42 Table 1.3-1 and particulate emissions are reported as *filterable* PM. ComStock does not report air pollution from electricity generation, because grid emissions vary considerably by grid region and are typically located far away from the building site.

