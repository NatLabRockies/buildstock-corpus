<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0396270 | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: HVAC System Types Probability Distributions | lines: 48-165 -->
## HVAC System Types Probability Distributions

Each ComStock model is assigned a comprehensive HVAC system type. The full list of ComStock HVAC system types is shown in Table “Fuel Type Category for ComStock HVAC System Types”. HVAC system types are assigned to ComStock models through sampling informed by representative probability distributions. These probability distributions depend on building type, census division, and heating fuel type. For example, the distributions provide the fraction of gas-heated retail buildings in the West North Central Census Division that use each HVAC system type from Table “Fuel Type Category for ComStock HVAC System Types”. The probability distributions are derived from CBECS 2012 microdata, which include data on building type, census division, heating fuel type, and HVAC system type.

<div id="tab:hvac_system_heating_fuel_categories" data-source="tables/hvac_system_heating_fuel_categories.tex">

| **HVAC System Type** | **Heating Fuel Category** |
|:---|:---|
| Packaged variable air volume (PVAV) with gas heat with electric reheat | Electricity |
| DOAS with fan coil district chilled water with district hot water | District_Heating |
| Variable air volume (VAV) district chilled water with district hot water reheat | District_Heating |
| PSZ-AC with gas coil | Fuel |
| VAV chiller with PFP boxes | Electricity |
| VAV chiller with gas boiler reheat | Fuel |
| VAV air-cooled chiller with gas boiler reheat | Fuel |
| Packaged terminal air conditioner (PTAC) with electric coil | Electricity |
| PSZ-AC with gas boiler | Fuel |
| VAV air-cooled chiller with district hot water reheat | District_Heating |
| Residential AC with residential forced air furnace | Fuel |
| PSZ-AC with electric coil | Electricity |
| VAV air-cooled chiller with parallel fan-powered (PFP) boxes | Electricity |
| Packaged terminal heat pump (PTHP) | Electricity |
| PVAV with gas boiler reheat | Fuel |
| PVAV with PFP boxes | Electricity |
| VAV chiller with district hot water reheat | District_Heating |
| DOAS with fan coil air-cooled chiller with boiler | Fuel |
| DOAS with fan coil chiller with boiler | Fuel |
| DOAS with variable refrigerant flow (VRF) | Electricity |
| Residential forced air furnace | Fuel |
| DOAS with water source heat pumps with ground source heat pump | Electricity |
| DOAS with water source heat pumps cooling tower with boiler | Electricity |
| Direct evap coolers with forced air furnace | Fuel |
| VAV district chilled water with PFP boxes | Electricity |
| PVAV with district hot water reheat | District_Heating |
| DOAS with fan coil chiller with district hot water | District_Heating |
| Direct evap coolers with baseboard gas boiler | Fuel |
| PTAC with gas boiler | Fuel |
| Packaged single-zone air conditioner (PSZ-AC) with district hot water | District_Heating |
| Packaged single-zone heat pump (PSZ-HP) | Electricity |
| Gas unit heaters | Fuel |
| DOAS with fan coil chiller with baseboard electric | Electricity |
| PSZ-AC district chilled water with district hot water | District_Heating |
| Direct evap coolers with baseboard electric | Electricity |
| VAV district chilled water with gas boiler reheat | Fuel |
| Baseboard electric | Electricity |
| DOAS with fan coil air-cooled chiller with district hot water | District_Heating |
| PSZ-AC district chilled water with electric coil | Electricity |
| DOAS with fan coil district chilled water with boiler | Fuel |
| PTAC with gas coil | Fuel |
| DOAS with fan coil district chilled water with baseboard electric | Electricity |
| Baseboard gas boiler | Fuel |
| PTAC with baseboard district hot water | District_Heating |
| DOAS with fan coil air-cooled chiller with baseboard electric | Electricity |

Fuel Type Category for ComStock HVAC System Types

</div>

### CBECS HVAC System Type Analysis

To derive probability distributions of HVAC system types from the CBECS data, we first assigned one of the comprehensive ComStock HVAC system types shown in Table “Fuel Type Category for ComStock HVAC System Types” to the CBECS microdata samples. Historically, this analysis was based solely on the CBECS 2012 data set; however, our updated methodology now integrates data from both the CBECS 2012 and CBECS 2018 data sets. To combine these data sources, we apply a weighted average based on the number of samples from each data set to ensure appropriate representation.

CBECS includes questions regarding the primary HVAC system type of the building; however, it also contains dozens of additional questions about HVAC system components, fuel types, and technologies. In several cases, these responses may conflict with one another, making it difficult to derive a deterministic HVAC system type for the CBECS building samples. Interpretation of the numerous HVAC characteristics into a complete HVAC system type needed for energy modeling involves user discretion and judgment. On multiple occasions, the combinations of survey responses related to the HVAC system were questionable, incomplete, or conflicting based on engineering judgment. This could be due to the survey respondent lacking information about the nuances of the building’s HVAC system, the survey respondent skipping relevant questions, or the building having multiple system types, perhaps due to various activities in the building or retrofits and expansions over time. Any of these issues could create a combination of equipment for a CBECS sample that would be difficult to translate into a single, comprehensive HVAC system type without firsthand knowledge of the building. Thus, reliably discerning an HVAC system type from the survey questions can be challenging for some of the CBECS samples and requires some degree of assumption.

Based on survey responses, some CBECS samples appear to utilize multiple types of HVAC systems. For example, one sample responded affirmatively to having a chiller, packaged terminal air conditioners (PTACs), heat pumps, and a swamp cooler. However, there is no indication as to the fraction of the building serving each system type in the survey. Additionally, ComStock is not trying to model buildings with several HVAC system types. To address this, we needed to determine prioritization rules when multiple system types for a single CBECS sample appeared to be prevalent. To achieve this, we grouped systems into the following four categories: VAVs, single-zone RTU, DOAS with zone terminal units (e.g., DOAS with heat pumps, VRF), and miscellaneous single-zone equipment.

There were several cases where the assigned HVAC system for a CBECS sample was unlikely given the size and type of the building. For example, only a small percentage of small office buildings would be expected to use large, multi-zone VAV systems. Similarly, only a small percentage of very large office buildings would be expected to use single-zone RTUs or zone terminal equipment with no DOAS. To address this, we introduced "size bins" to our distributions to ensure system types were correctly assigned based on building size. These size bins were incorporated into the sampling methodology, described in Section chap:3_sampling, to further refine system type assignments and improve the alignment between system types and building characteristics. Additional heating-only system types were assigned to building zones whose thermostat setpoints (see “Thermostat Set Points”) described heating-only operation. This primarily affected warehouse buildings in California, representing approximately 13% of the total stock warehouse floor area, which moved from the primary system type to heating-only gas unit heaters or electric baseboard systems, depending on primary heating fuel source.

Overall, we produced 1,162 probability distributions from the combined CBECS 2012 and 2018 HVAC analysis, with dependencies based on building type, size bin, heating fuel, and census region. These distributions are used with the ComStock sampling process, described in Section chap:3_sampling, which ensures that HVAC system types are applied to the correct proportion of models. The prevalence of each HVAC system type in ComStock for all building types is shown in Figure “Prevalence of ComStock HVAC system types by total stock floor area; all building types.” through Figure “Prevalence of ComStock HVAC system types by total stock floor area; warehouses.”.

| **ComStock System Type** | **full service restaurant** | **hospital** | **large hotel** | **large office** | **medium office** | **outpatient** | **primary school** | **quick service restaurant** | **retail** | **secondary school** | **small hotel** | **small office** | **strip mall** | **warehouse** |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| Baseboard electric | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.5 | 0 | 0 | 0 | 0 | 0.6 |
| Baseboard gas boiler | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOAS with VRF | 0 | 0 | 0.4 | 0.8 | 1.7 | 1.3 | 0.3 | 0 | 0 | 0 | 0 | 1.5 | 0 | 0.3 |
| DOAS with fan coil air-cooled chiller with baseboard electric | 0 | 0 | 0.1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOAS with fan coil air-cooled chiller with boiler | 0 | 0.2 | 2.7 | 0.3 | 0 | 0.5 | 0.9 | 0 | 0 | 1.9 | 0 | 0 | 0 | 0 |
| DOAS with fan coil air-cooled chiller with district hot water | 0 | 0.1 | 0 | 1.1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOAS with fan coil chiller with baseboard electric | 0 | 0 | 0.6 | 0.1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOAS with fan coil chiller with boiler | 0 | 0.5 | 6.2 | 0.4 | 2.8 | 0 | 0.2 | 0 | 0 | 0.5 | 0.8 | 0.4 | 0 | 0 |
| DOAS with fan coil chiller with district hot water | 0 | 0 | 1.3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOAS with fan coil district chilled water with baseboard electric | 0 | 0 | 0.1 | 0 | 0 | 0 | 0 | 0 | 0 | 1.6 | 0 | 0 | 0 | 0 |
| DOAS with fan coil district chilled water with boiler | 0 | 0 | 1.8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOAS with fan coil district chilled water with district hot water | 0.1 | 0 | 0.5 | 0.1 | 0.1 | 0 | 0 | 0 | 0 | 0.2 | 0 | 0 | 0 | 0 |
| DOAS with water source heat pumps cooling tower with boiler | 0 | 0.7 | 8 | 5.3 | 1.8 | 0.4 | 3.1 | 0 | 0 | 3.1 | 3 | 0.3 | 0.1 | 0 |
| DOAS with water source heat pumps with ground source heat pump | 0 | 0 | 6.3 | 1.1 | 0 | 0.6 | 2.1 | 0 | 0 | 4.8 | 0 | 1.2 | 0 | 0 |
| Direct evap coolers with baseboard electric | 0.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.6 | 0 | 0 | 0 | 0.6 | 0 |
| Direct evap coolers with baseboard gas boiler | 0 | 0 | 0 | 0 | 0 | 1.2 | 0.4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Direct evap coolers with forced air furnace | 0.9 | 0 | 0 | 0 | 0.8 | 0 | 0 | 1.3 | 1.6 | 1.4 | 0 | 0.3 | 0.6 | 0.5 |
| Gas unit heaters | 0.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.3 | 0 | 2.7 |
| PSZ-AC district chilled water with district hot water | 0.6 | 0 | 0 | 0 | 0.5 | 0 | 0 | 0 | 0 | 1.3 | 0 | 0 | 0 | 0 |
| PSZ-AC district chilled water with electric coil | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 5.9 | 0 | 0.4 | 0 | 0 |
| PSZ-AC with district hot water | 0 | 0 | 0 | 0.3 | 1.3 | 0.3 | 0.2 | 0 | 0.5 | 0.6 | 0 | 0 | 0 | 0.1 |
| PSZ-AC with electric coil | 25.4 | 4.3 | 0 | 3.3 | 15.7 | 22.4 | 16.6 | 44.1 | 19.4 | 11.5 | 0 | 24.6 | 32.3 | 27.2 |
| PSZ-AC with gas boiler | 3.1 | 6.4 | 0 | 3.3 | 9.1 | 4.3 | 9.4 | 2.7 | 1.5 | 4.7 | 0 | 3 | 0.2 | 1.5 |
| PSZ-AC with gas coil | 47.2 | 0 | 0 | 3.5 | 15.2 | 39.6 | 23.1 | 41.6 | 41 | 6.6 | 0 | 40.3 | 46.3 | 36.2 |
| PSZ-HP | 0 | 0 | 0 | 0 | 1.5 | 0.2 | 0 | 0 | 0 | 0 | 0 | 0 | 2.6 | 0 |
| PTAC with baseboard district hot water | 0 | 0.1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| PTAC with electric coil | 0.9 | 2.9 | 30.9 | 0 | 0.3 | 3.8 | 0.4 | 1.8 | 1 | 0 | 27.5 | 2.6 | 1.1 | 0.7 |
| PTAC with gas boiler | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5.8 | 0 | 0 | 0 |
| PTAC with gas coil | 0 | 0 | 0.6 | 0 | 0 | 0 | 0 | 0 | 0.6 | 0 | 0 | 0.6 | 0.6 | 0 |
| PTHP | 0 | 0 | 27.6 | 0 | 0 | 0 | 0 | 4.5 | 13.2 | 10.1 | 43.2 | 12.3 | 2.2 | 9.1 |
| PVAV with PFP boxes | 1 | 0.1 | 0 | 7.6 | 6.2 | 6.1 | 5.8 | 0 | 1.7 | 1.9 | 0 | 1.1 | 2 | 1.4 |
| PVAV with district hot water reheat | 0 | 2.9 | 0 | 4.7 | 0.2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| PVAV with gas boiler reheat | 1.6 | 3 | 0 | 9.5 | 12.3 | 3.9 | 9.1 | 0 | 2.6 | 5.8 | 0 | 0.7 | 1.6 | 1.4 |
| PVAV with gas heat with electric reheat | 0.5 | 1.7 | 0 | 5.3 | 11 | 2.1 | 4.4 | 0 | 1.7 | 3.8 | 0 | 1.9 | 8 | 2.6 |
| Residential AC with residential forced air furnace | 16.8 | 0 | 13.1 | 0.3 | 4.8 | 7 | 8.7 | 2.9 | 12 | 8.9 | 17.6 | 8.1 | 1.4 | 8.9 |
| Residential forced air furnace | 0 | 0 | 0 | 0 | 0 | 0 | 0.1 | 1.1 | 1.9 | 4.7 | 2 | 0.1 | 0 | 6.6 |
| VAV air-cooled chiller with PFP boxes | 0.5 | 0.3 | 0 | 1.8 | 0.1 | 1.5 | 1.5 | 0 | 0 | 0.9 | 0 | 0 | 0 | 0 |
| VAV air-cooled chiller with district hot water reheat | 0 | 3.3 | 0 | 0.3 | 0.9 | 0.1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| VAV air-cooled chiller with gas boiler reheat | 0 | 25.3 | 0 | 4.5 | 4.4 | 0.9 | 5.4 | 0 | 0 | 13.1 | 0 | 0 | 0 | 0.1 |
| VAV chiller with PFP boxes | 0 | 3.4 | 0 | 11.4 | 3.1 | 1.9 | 0 | 0 | 0 | 0.2 | 0 | 0 | 0.5 | 0 |
| VAV chiller with district hot water reheat | 0 | 1.9 | 0 | 5.3 | 0 | 0.2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| VAV chiller with gas boiler reheat | 0 | 35.2 | 0 | 19.1 | 2.7 | 1.1 | 3.7 | 0 | 0 | 5.4 | 0 | 0.2 | 0 | 0.1 |
| VAV district chilled water with PFP boxes | 0.3 | 0 | 0 | 0 | 1.1 | 0 | 0.7 | 0 | 0 | 0.7 | 0 | 0 | 0 | 0 |
| VAV district chilled water with district hot water reheat | 0.2 | 7.7 | 0 | 10 | 2.5 | 0.1 | 0 | 0 | 0 | 0.2 | 0 | 0.1 | 0 | 0 |
| VAV district chilled water with gas boiler reheat | 0 | 0.3 | 0 | 0.3 | 0.1 | 0.8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

