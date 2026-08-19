<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex -->
# Heating, Ventilating, Air Conditioning, and Refrigeration

## HVAC System Heating Fuel Type

Commercial HVAC equipment can use various heating fuel types, with the most common being natural gas, electricity, propane, fuel oil, and district heating. To reflect the variability of heating fuels in the real building stock, the ComStock workflow creates probability distributions of heating fuel types per building type at the county level. These distributions are used to assign a heating fuel type to each ComStock building model during the sampling process.

The probability distributions are informed by two data sources. First, there are the CBECS 2012 microdata, which include data on heating fuel(s), building type, and census division for the surveyed buildings. This data can be used to produce probability distributions for heating fuel by building type at the census division level. However, several data sources suggest notable variation within census divisions, which indicates that increased granularity may be needed (beyond what CBECS can provide). The heating fuel type probability distributions used in ResStock—which provides data for residential buildings at the county level—were used to add granularity. However, initial comparisons showed discrepancies between the ResStock data and the CBECS data, which is likely due to inherent differences between residential and commercial buildings. This indicated that the ResStock data should not be used directly. To rectify this, the county-level ResStock data were scaled to align with the CBECS data. This preserved the county-level variation in fuel type prevalence provided by the ResStock data, while also preserving the census division totals provided by the CBECS commercial data. District heating values were not available in the ResStock data, so the per-building-type CBECS values were used for all counties in a given census division.

In some cases, filtering down to a specific region and building type in the CBECS data yields very few samples. This can lead to unreliable conclusions for a region. To mitigate this, we took a blended approach, where some fraction of the CBECS region fuel type percentage comes from the regional samples only, and some fraction comes from the national sample for the building type. If more than 15 samples exist for a given building type and region, then 100% of the fuel type prevalence comes from that specific region. (The threshold of 15 samples was selected baced on engineering judgment to balance process reliability and regional variability.) If there are fewer than 15 samples, the number of samples divided by 15 will be the fraction used for the region, and the remainder will use the national numbers. For example, if a region has only 12 office samples, 80% (12/15) of the effective CBECS regional value will come from the CBECS region, and the other 20% will come from the national CBECS value for the building type. This will cause region/building type combinations with lower sample sizes to have a stronger inheritance of the national characteristics than the regional characteristics when we lack sufficient evidence to support this level of detail.

Some commercial building HVAC systems use multiple fuel types. For example, a VAV system with a gas furnace in the air handling unit and electric resistance coils in the reheat boxes, or a gas furnace DOAS with variable refrigerant flow (VRF) heat pumps serving the zones. This can complicate the categorization of these systems into a single primary fuel type. To address this, we determine the primary heating fuel type for the mixed fuel systems. The primary heating fuel is the heating fuel expected to carry the majority of the heating load. For example, the previously mentioned example of a VAV system with gas heat at the air handler and electric reheat would be classified as an electric-heated system, since the majority of heating for multizone VAV systems usually comes from the reheat. A full list of ComStock HVAC systems and their fuel type categories are shown in Table <a href="#tab:hvac_system_heating_fuel_categories" data-reference-type="ref" data-reference="tab:hvac_system_heating_fuel_categories">1</a>. Further detail on model HVAC system assignment methodology can be found in Section <a href="#sec:HVAC_System_Type" data-reference-type="ref" data-reference="sec:HVAC_System_Type">1.2</a>.

Figure <a href="#fig:fuel_cbecs_v_cstock" data-reference-type="ref" data-reference="fig:fuel_cbecs_v_cstock">1</a> compares the prevalence of heating fuel type by stock floor area for CBECS 2012 and ComStock, by building type. In most cases, ComStock closely aligns to the CBECS 2012 values. However, there are some differences between the two sources due to randomness in the sampling process and from the use of other data sources to achieve county-level granularity in fuel type prevalence. The largest difference is in small hotels where ComStock shows 87% of the floor area using electric heating while CBECS suggest 74%, an absolute difference of 12%.

<figure id="fig:fuel_cbecs_v_cstock">
<img src="figures/cbecs_comstock_fuel_type_comparison.png" style="width:110.0%" />
<figcaption>Comparison of heating fuel type prevalence by floor area between CBECS 2012 and ComStock.</figcaption>
</figure>

The county-level prevalences of different heating fuel types are shown in Figure <a href="#fig:map_naturalgas" data-reference-type="ref" data-reference="fig:map_naturalgas">2</a> (natural gas), Figure <a href="#fig:map_electricity" data-reference-type="ref" data-reference="fig:map_electricity">3</a> (electricity), Figure <a href="#fig:map_fueloil" data-reference-type="ref" data-reference="fig:map_fueloil">4</a> (fuel oil), Figure <a href="#fig:map_propane" data-reference-type="ref" data-reference="fig:map_propane">5</a> (propane), and Figure <a href="#fig:map_district" data-reference-type="ref" data-reference="fig:map_district">6</a> (district heating).

<figure id="fig:map_naturalgas">
<img src="figures/map_naturalgas.png" style="width:80.0%" />
<figcaption>Fraction of ComStock models using natural gas heating per county.</figcaption>
</figure>

<figure id="fig:map_electricity">
<img src="figures/map_electricity.png" style="width:80.0%" />
<figcaption>Fraction of ComStock models using electric heating per county.</figcaption>
</figure>

<figure id="fig:map_fueloil">
<img src="figures/map_fueloil.png" style="width:80.0%" />
<figcaption>Fraction of ComStock models using fuel oil heating per county.</figcaption>
</figure>

<figure id="fig:map_propane">
<img src="figures/map_propane.png" style="width:80.0%" />
<figcaption>Fraction of ComStock models using propane heating per county.</figcaption>
</figure>

<figure id="fig:map_district">
<img src="figures/map_districtheating.png" style="width:80.0%" />
<figcaption>Fraction of ComStock models using district heating per county.</figcaption>
</figure>

## HVAC System Types Probability Distributions

Each ComStock model is assigned a comprehensive HVAC system type. The full list of ComStock HVAC system types is shown in Table <a href="#tab:hvac_system_heating_fuel_categories" data-reference-type="ref" data-reference="tab:hvac_system_heating_fuel_categories">1</a>. HVAC system types are assigned to ComStock models through sampling informed by representative probability distributions. These probability distributions depend on building type, census division, and heating fuel type. For example, the distributions provide the fraction of gas-heated retail buildings in the West North Central Census Division that use each HVAC system type from Table <a href="#tab:hvac_system_heating_fuel_categories" data-reference-type="ref" data-reference="tab:hvac_system_heating_fuel_categories">1</a>. The probability distributions are derived from CBECS 2012 microdata, which include data on building type, census division, heating fuel type, and HVAC system type.

<div id="tab:hvac_system_heating_fuel_categories">

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

To derive probability distributions of HVAC system types from the CBECS data, we first assigned one of the comprehensive ComStock HVAC system types shown in Table <a href="#tab:hvac_system_heating_fuel_categories" data-reference-type="ref" data-reference="tab:hvac_system_heating_fuel_categories">1</a> to the CBECS microdata samples. Historically, this analysis was based solely on the CBECS 2012 data set; however, our updated methodology now integrates data from both the CBECS 2012 and CBECS 2018 data sets. To combine these data sources, we apply a weighted average based on the number of samples from each data set to ensure appropriate representation.

CBECS includes questions regarding the primary HVAC system type of the building; however, it also contains dozens of additional questions about HVAC system components, fuel types, and technologies. In several cases, these responses may conflict with one another, making it difficult to derive a deterministic HVAC system type for the CBECS building samples. Interpretation of the numerous HVAC characteristics into a complete HVAC system type needed for energy modeling involves user discretion and judgment. On multiple occasions, the combinations of survey responses related to the HVAC system were questionable, incomplete, or conflicting based on engineering judgment. This could be due to the survey respondent lacking information about the nuances of the building’s HVAC system, the survey respondent skipping relevant questions, or the building having multiple system types, perhaps due to various activities in the building or retrofits and expansions over time. Any of these issues could create a combination of equipment for a CBECS sample that would be difficult to translate into a single, comprehensive HVAC system type without firsthand knowledge of the building. Thus, reliably discerning an HVAC system type from the survey questions can be challenging for some of the CBECS samples and requires some degree of assumption.

Based on survey responses, some CBECS samples appear to utilize multiple types of HVAC systems. For example, one sample responded affirmatively to having a chiller, packaged terminal air conditioners (PTACs), heat pumps, and a swamp cooler. However, there is no indication as to the fraction of the building serving each system type in the survey. Additionally, ComStock is not trying to model buildings with several HVAC system types. To address this, we needed to determine prioritization rules when multiple system types for a single CBECS sample appeared to be prevalent. To achieve this, we grouped systems into the following four categories: VAVs, single-zone RTU, DOAS with zone terminal units (e.g., DOAS with heat pumps, VRF), and miscellaneous single-zone equipment.

There were several cases where the assigned HVAC system for a CBECS sample was unlikely given the size and type of the building. For example, only a small percentage of small office buildings would be expected to use large, multi-zone VAV systems. Similarly, only a small percentage of very large office buildings would be expected to use single-zone RTUs or zone terminal equipment with no DOAS. To address this, we introduced "size bins" to our distributions to ensure system types were correctly assigned based on building size. These size bins were incorporated into the sampling methodology, described in Section <a href="#chap:3_sampling" data-reference-type="ref" data-reference="chap:3_sampling">[chap:3_sampling]</a>, to further refine system type assignments and improve the alignment between system types and building characteristics. Additional heating-only system types were assigned to building zones whose thermostat setpoints (see <a href="#section:therm_setpoints" data-reference-type="ref" data-reference="section:therm_setpoints">1.7</a>) described heating-only operation. This primarily affected warehouse buildings in California, representing approximately 13% of the total stock warehouse floor area, which moved from the primary system type to heating-only gas unit heaters or electric baseboard systems, depending on primary heating fuel source.

Overall, we produced 1,162 probability distributions from the combined CBECS 2012 and 2018 HVAC analysis, with dependencies based on building type, size bin, heating fuel, and census region. These distributions are used with the ComStock sampling process, described in Section <a href="#chap:3_sampling" data-reference-type="ref" data-reference="chap:3_sampling">[chap:3_sampling]</a>, which ensures that HVAC system types are applied to the correct proportion of models. The prevalence of each HVAC system type in ComStock for all building types is shown in Figure <a href="#fig:hvac_sys_type_prevalence" data-reference-type="ref" data-reference="fig:hvac_sys_type_prevalence">[fig:hvac_sys_type_prevalence]</a> through Figure <a href="#fig:hvac_sys_type_prevalence_warehouse" data-reference-type="ref" data-reference="fig:hvac_sys_type_prevalence_warehouse">[fig:hvac_sys_type_prevalence_warehouse]</a>.

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

## HVAC System Sizing

HVAC system design sizing is determined from several EnergyPlus design day sizing runs. Equipment capacity is hardsized, meaning it is explicitly set in the model. Design day conditions come from the same weather location as the weather file. Design days include the annual heating 99.6% drybulb temperature, annual cooling 0.4% drybulb temperature, annual cooling 0.4% wetbulb temperature for cooling towers and evaporative coolers, and monthly 0.4% drybulb temperature for August, September, and October to account for buildings with solar-gain driven cooling load maximums.

Per ASHRAE 90.1 Appendix G, HVAC systems are oversized by 15% for cooling and 25% for heating. Note that sizing results for a model will be impacted by several control properties specific to the model, such as supply air temperature control, thermostat set points, and outdoor ventilation rates, which are described in later sections.

## Outdoor Air Ventilation Rates

Commercial buildings require outdoor ventilation air when the building is occupied. The design outdoor air rate for a system is the minimum amount of outdoor air the system must supply while the building is occupied. The amount of outdoor air required for an HVAC system is calculated by the combined needs of the space type(s) served by a system.

ComStock design outdoor air ventilation rates follow the requirements set forth by ASHRAE Standard 62.1: Ventilation for Acceptable Indoor Air Quality (non-California models), or by DEER (California models). Both of these sources dictate the minimum design outdoor air flow rate by space type. The minimum outdoor air requirements for each space type are composed of a flow rate per person, a flow rate per area, and in some cases, an exhaust rate. Combined, these components determine the design outdoor air requirement for each space and its respective HVAC system. Table <a href="#tab:outdoor_air_table" data-reference-type="ref" data-reference="tab:outdoor_air_table">2</a> and Table <a href="#tab:outdoor_air_table_deer" data-reference-type="ref" data-reference="tab:outdoor_air_table_deer">3</a> show the average design outdoor air flow rate per area (cfm/m<sup>2</sup>) for non-California models and California models, respectively. These averages are influenced by the number of buildings of each type and their vintage. Both methods are heavily influenced by the space type composition of the model; ComStock models assume space type ratios for building types, with some building types having variation in the space type ratios. ComStock space types are described further in Section <a href="#sec:space_type_ratios" data-reference-type="ref" data-reference="sec:space_type_ratios">[sec:space_type_ratios]</a>.

Some ComStock HVAC system types are residential style systems (denoted “residential” in Table <a href="#tab:hvac_system_heating_fuel_categories" data-reference-type="ref" data-reference="tab:hvac_system_heating_fuel_categories">1</a>). These systems do not include ventilation air and are an exception to the aforementioned ASHRAE-62.1 outdoor air methodology. Although commercial buildings all require outdoor ventilation air per code, some commercial buildings in the stock use residential systems without outdoor air. This is reflected in ComStock through the use of these residential system types. ComStock’s HVAC system selection methodology is described further in Section <a href="#sec:HVAC_System_Type" data-reference-type="ref" data-reference="sec:HVAC_System_Type">1.2</a>.

<div id="tab:outdoor_air_table">

| **Building Type** | **Pre-1980 (cfm/sf)** | **1980-2004 (cfm/sf)** | **90.1-2004 (cfm/sf)** | **90.1-2007 (cfm/sf)** | **90.1-2010 (cfm/sf)** | **90.1-2013 (cfm/sf)** |
|:---|:---|:---|:---|:---|:---|:---|
| **FullServiceRestaurant** | 1.103 | 1.103 | 1.107 | 1.048 | 1.067 | 1.077 |
| **Hospital** | \- | 0.258 | 0.254 | 0.258 | 0.258 | 0.258 |
| **LargeHotel** | 0.240 | 0.240 | 0.240 | 0.224 | 0.234 | 0.226 |
| **LargeOffice** | 0.098 | 0.098 | 0.098 | 0.098 | 0.098 | 0.098 |
| **MediumOffice** | 0.100 | 0.100 | 0.100 | 0.098 | 0.098 | 0.098 |
| **Outpatient** | 0.215 | 0.215 | 0.223 | 0.215 | 0.215 | 0.215 |
| **PrimarySchool** | 0.376 | 0.376 | 0.378 | 0.374 | 0.374 | 0.374 |
| **QuickServiceRestaurant** | 0.935 | 0.935 | 0.935 | 0.849 | 0.884 | 0.886 |
| **RetailStandalone** | 0.276 | 0.276 | 0.276 | 0.268 | 0.270 | 0.270 |
| **RetailStripmall** | 0.449 | 0.461 | 0.461 | 0.449 | 0.451 | 0.453 |
| **SecondarySchool** | 0.547 | 0.547 | 0.547 | 0.543 | 0.542 | 0.542 |
| **SmallHotel** | \- | \- | 0.138 | 0.100 | 0.100 | 0.100 |
| **SmallOffice** | 0.100 | 0.100 | 0.100 | 0.100 | 0.098 | 0.098 |
| **Warehouse** | 0.049 | 0.049 | 0.049 | 0.051 | 0.051 | 0.051 |

Design Outdoor Air Rates by Building Type and HVAC Code Template for Buildings Outside California

</div>

<div id="tab:outdoor_air_table_deer">

| **Building Type** | **DEER Pre-1975 (cfm/sf)** | **DEER 1985 (cfm/sf)** | **DEER 1996 (cfm/sf)** | **DEER 2003 (cfm/sf)** | **DEER 2007 (cfm/sf)** | **DEER 2011 (cfm/sf)** | **DEER 2014 (cfm/sf)** | **DEER 2015 (cfm/sf)** | **DEER 2017 (cfm/sf)** |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| **FullServiceRestaurant** | 0.540 | 0.540 | 0.540 | 0.540 | 0.540 | 0.540 | 0.540 | 0.540 | 0.540 |
| **Hospital** | \- | 0.152 | 0.152 | 0.152 | 0.152 | 0.152 | 0.152 | 0.152 | \- |
| **LargeHotel** | 0.000 | 0.104 | 0.104 | 0.104 | 0.104 | 0.104 | 0.104 | 0.104 | 0.104 |
| **LargeOffice** | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 |
| **MediumOffice** | \- | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 |
| **Outpatient** | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 | 0.108 |
| **PrimarySchool** | \- | 0.447 | 0.447 | 0.447 | 0.447 | 0.447 | 0.447 | 0.447 | 0.447 |
| **QuickServiceRestaurant** | 0.439 | 0.439 | 0.439 | 0.439 | 0.439 | 0.439 | 0.439 | 0.439 | 0.439 |
| **RetailStandalone** | 0.268 | 0.268 | 0.268 | 0.268 | 0.268 | 0.268 | 0.268 | 0.268 | 0.268 |
| **RetailStripmall** | 0.327 | 0.323 | 0.323 | 0.323 | 0.323 | 0.323 | 0.325 | 0.323 | 0.323 |
| **SecondarySchool** | 0.433 | 0.433 | 0.433 | 0.433 | 0.433 | 0.433 | 0.433 | 0.433 | 0.433 |
| **SmallHotel** | 0.069 | 0.069 | 0.069 | 0.069 | 0.069 | 0.069 | 0.069 | 0.069 | 0.069 |
| **SmallOffice** | 0.077 | 0.077 | 0.077 | 0.077 | 0.077 | 0.077 | 0.077 | 0.077 | 0.077 |
| **Warehouse** | 0.150 | 0.150 | 0.150 | 0.150 | 0.150 | 0.150 | 0.150 | 0.150 | 0.150 |

Design Outdoor Air Rates by Building Type and HVAC Code Template for Buildings Inside California

</div>

## Fan Systems

Fans are used in all ComStock HVAC systems except those that rely on radiant heat transfer, such as baseboards. Fans induce pressure in the air stream of HVAC equipment, producing the airflow needed for space conditioning and/or outdoor air ventilation.

### Fan Power

Fan power determines the amount of energy it takes a fan system to provide a certain amount of airflow. The fan power requirements of each HVAC system are a function of the total pressure drop of the air stream that the fan system will need to overcome (e.g., from filters, coils, air ducts) as well as the efficiency of the fan blades and fan motor.

Fan power in ComStock is determined by ASHRAE-90.1 code requirements. ASHRAE-90.1 determines fan power primarily based on the system type. Constant air volume, variable air volume, and unitary zone equipment are all assigned different fan power allowances.

For implementation in ComStock, fan power is determined based on the static pressure of the air delivery system, the efficiencies of the fan/motor system, and the airflow of the system. The static pressure is based on the HVAC system type and the maximum airflow of the system, as shown in Table <a href="#tab:fan_power" data-reference-type="ref" data-reference="tab:fan_power">4</a>. The fan motor efficiencies are a function of the motor size and HVAC code year, as shown in Table <a href="#tab:fan_motor_efficiencies" data-reference-type="ref" data-reference="tab:fan_motor_efficiencies">[tab:fan_motor_efficiencies]</a>.

The addition of energy recovery ventilators (ERVs) in HVAC air loops can add additional static pressure to the air system and therefore result in a higher fan power requirement. ComStock accounts for this additional fan power in the ERV wheel power rather than the fan itself; this allows for improved accuracy during ERV bypass modes (where the airflow bypasses the additional static pressure of the ERV system). See Section <a href="#sec:erv" data-reference-type="ref" data-reference="sec:erv">1.10</a> for more information on ComStock ERV systems.

<div id="tab:fan_power">

<table>
<caption>Fan Pressure Rise and Efficiency</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Fan Type</strong></th>
<th style="text-align: left;"><strong>Max Airflow (cfm)</strong></th>
<th style="text-align: left;"><strong>Pressure Rise (in. H<span class="math inline"><sub>2</sub></span>O)</strong></th>
<th style="text-align: left;"><strong>Fan Power Minimum Flow Fraction</strong></th>
<th style="text-align: left;"><strong>Fan Impeller Efficiency</strong></th>
<th style="text-align: left;"><strong>Motor Efficiency</strong></th>
<th style="text-align: left;"><strong>Total Fan Efficiency</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3" style="text-align: left;"><strong>Constant Volume and DOAS</strong></td>
<td style="text-align: left;">&lt;7,437</td>
<td style="text-align: left;">2.5</td>
<td rowspan="3" style="text-align: left;">1</td>
<td rowspan="6" style="text-align: left;">0.65</td>
<td rowspan="9" style="text-align: left;">See motor efficiency lookup table</td>
<td rowspan="9" style="text-align: left;">(Fan Impeller Eff.) X (Motor Eff.)</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">≥</span>7,537 and &lt;20,000</td>
<td style="text-align: left;">4.46</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">≥</span>20,000</td>
<td style="text-align: left;">4.09</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-4</span></td>
<td style="text-align: left;">&lt;4,648</td>
<td style="text-align: left;">4</td>
<td rowspan="3" style="text-align: left;">0.25</td>
</tr>
<tr>
<td style="text-align: left;"><span>2-3</span></td>
<td style="text-align: left;"><span class="math inline">≥</span>4,648 and &lt;20,000</td>
<td style="text-align: left;">6.32</td>
</tr>
<tr>
<td style="text-align: left;"><span>2-3</span></td>
<td style="text-align: left;"><span class="math inline">≥</span>20,000</td>
<td style="text-align: left;">5.58</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> <strong>PTAC/PTHP, WSHP, VRF</strong></td>
<td style="text-align: left;">&gt;0</td>
<td style="text-align: left;">1.33</td>
<td style="text-align: left;">1</td>
<td rowspan="3" style="text-align: left;">0.55</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-4</span> <strong>Four Pipe Fan Coil</strong></td>
<td style="text-align: left;">&gt;0</td>
<td style="text-align: left;">1.09</td>
<td style="text-align: left;">1</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-4</span> <strong>Unit Heater</strong></td>
<td style="text-align: left;">&gt;0</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">1</td>
</tr>
</tbody>
</table>

</div>

### Fan Controls

This section describes the operation of fan systems during the hours a building is occupied. Details on the operation of fan systems during unoccupied hours are described in Section <a href="#sec:unoccupied_ahu_operation" data-reference-type="ref" data-reference="sec:unoccupied_ahu_operation">1.8</a>.

#### HVAC Systems Providing Outdoor Air

As required by ASHRAE-90.1, HVAC systems in commercial buildings must constantly provide the minimum design outdoor air flow rates when the building is occupied. HVAC systems in ComStock follow this control requirement. For constant volume systems, the fan system will run continuously at design airflow during occupied hours. For VAV systems, the fan system will run continuously between the minimum and maximum airflow of the system during occupied hours, always ensuring that the total system airflow meets the airflow needs of every zone.

#### HVAC Systems Not Providing Outdoor Air

Systems that do not directly provide outdoor air, such as zone-level unitary systems coupled with a DOAS, do not need to run fans continuously. Therefore, these systems are controlled to cycle the fan system on only when required to maintain zone thermostat set points. Otherwise, the fans are allowed to turn off. This is also the control logic for any residential-style system in ComStock that does not provide outdoor air.

## Pump Systems

Pumps are used to induce flow in building hydronic loops. This includes heating water loops, cooling water loops, condenser water loops, and ground-source heat pump water loops.

### Pump Power

Pump power is a function of the pressure head of the hydronic loop and the pump efficiency. The pressure heads in ComStock hydronic systems are set to reflect the baseline requirements specified in ASHRAE-90.1, noting that each hydronic loop type has its own specifications. The pressure heads used for the various ComStock hydronic loop types are specified in Table <a href="#tab:pumps" data-reference-type="ref" data-reference="tab:pumps">5</a>. Primary-only pump configurations use a single hydronic loop system between the boilers/chillers and the heating/cooling coils for space conditioning. A primary-secondary system uses a primary loop for circulating water between the boilers/chillers, and a secondary loop for supplying the the plant fluid to the heating/cooling coils. Pump motor efficiencies are derived using the same motor efficiency lookup tables used for fans (Table <a href="#tab:fan_motor_efficiencies" data-reference-type="ref" data-reference="tab:fan_motor_efficiencies">[tab:fan_motor_efficiencies]</a>).

### Pump Controls

All pumps in ComStock are set to use intermittent controls, meaning that they can cycle off when there is no load present in the loop. Constant volume pumps are controlled to ride the pump curve, as specified by ASHRAE-90.1, whereas variable speed pumps can adjust their speed to modulate flow as needed. Variable speed pumps all have a minimum flow ratio of 0% in ComStock. This value is likely too low and underestimates pumping energy, as most pump systems can only reduce flow as low as 30%–50% in order to maintain proper operation of chillers, boilers, etc. The assignment methodology for variable speed pumps is specified in Table <a href="#tab:pumps" data-reference-type="ref" data-reference="tab:pumps">5</a>.

<div id="tab:pumps">

<table>
<caption>Pump Configuration and Pressure Rise for Hydronic Loops</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Loop Type</strong></th>
<th style="text-align: left;"><strong>Pump Configuration</strong></th>
<th style="text-align: left;"><strong>Primary Pump Head (ft w.c.)</strong></th>
<th style="text-align: left;"><strong>Secondary Pump Head (ft w.c.)</strong></th>
<th style="text-align: left;"><strong>VFD Pump?</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Hot Water Loop</strong></td>
<td rowspan="2" style="text-align: left;">Primary-only</td>
<td rowspan="2" style="text-align: left;">60</td>
<td rowspan="2" style="text-align: left;">-</td>
<td rowspan="2" style="text-align: left;">Variable speed when building area &gt;120,000 ft<span class="math inline"><sup>2</sup></span></td>
</tr>
<tr>
<td style="text-align: left;"><strong>District Heating Loop</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Water-Cooled Chiller Loop</strong></td>
<td style="text-align: left;">Constant-primary, variable-secondary</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">45</td>
<td style="text-align: left;">Secondary pump always variable speed</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Air-Cooled Chiller Loop</strong></td>
<td rowspan="2" style="text-align: left;">Primary-only</td>
<td rowspan="2" style="text-align: left;">60</td>
<td rowspan="2" style="text-align: left;">-</td>
<td rowspan="2" style="text-align: left;">Variable speed when cooling capacity &gt;300 tons</td>
</tr>
<tr>
<td style="text-align: left;"><strong>District Cooling Loop</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Condenser Water Loop</strong></td>
<td style="text-align: left;">Primary-only</td>
<td style="text-align: left;">50</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">Always constant speed</td>
</tr>
<tr>
<td style="text-align: left;"><strong>GSHP Condenser Water Loop</strong></td>
<td style="text-align: left;">Primary-only</td>
<td style="text-align: left;">60</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">Always constant speed</td>
</tr>
</tbody>
</table>

</div>

## Thermostat Set Points

Thermostat set points, both heating and cooling, dictate the target indoor temperature range for the HVAC system to satisfy. The cooling thermostat set point will set the upper temperature limit, whereas the heating thermostat set point will set the lower temperature limit.

Thermostat set points are implemented in ComStock through square-wave schedules. Each model is assigned a set point temperature, which is the temperature the HVAC system must maintain during occupied hours, and a setback temperature, which is the temperature the HVAC system must maintain during unoccupied hours (note that some models have no setback temperature). The set point and setback temperatures used in the models are described later in this section. The timing of the set point and setback temperatures align with the building occupancy schedules discussed in Section <a href="#sec:hoo" data-reference-type="ref" data-reference="sec:hoo">[sec:hoo]</a>.

### Thermostat Set Points Informed by Building Automation System Data

This section outlines the ComStock thermostat set point assignment methodology for the following building types: full service restaurant, large office, medium office, primary school, quick service restaurant, retail standalone, retail strip mall, secondary school, and small office.

All ComStock building types, excluding hospitals, outpatient, warehouses, and hotels, utilize building automation system (BAS) data to inform distributions of thermostat set points. The methodology behind this approach is described in this section. The intent is to include heating and cooling thermostat set point variability between ComStock models to reflect the thermostat set point variability between real buildings. For example, some offices could be expected to set their heating thermostat to 72°F, whereas others might set it to 70°F. The ComStock methodology allows this variation to exist in the models.

Building automation data from three industry-provided private data sources with over 3,700 buildings were used to derive the distributions of thermostat set points that are used to assign set points to the applicable ComStock models. Table <a href="#tab:bas_thermostat_count_by_btype" data-reference-type="ref" data-reference="tab:bas_thermostat_count_by_btype">6</a> shows the counts of buildings with thermostat data available in the data set by building type. The data set includes the time series heating and cooling set points that were used to determine the occupied heating and cooling set points for each building. In turn, these were used to create probability distributions of thermostat set points by building type when aggregating across the data set. For building types with less than 25 samples in the data set, the distribution for all building types was used, as smaller sample sizes cannot reliably be extrapolated to represent a population. The resulting heating and cooling probability distributions, per applicable building type, are shown in Figure <a href="#fig:htg_therm_setpoints" data-reference-type="ref" data-reference="fig:htg_therm_setpoints">7</a> and Figure <a href="#fig:clg_therm_setpoints" data-reference-type="ref" data-reference="fig:clg_therm_setpoints">8</a>, respectively. Note that some outliers exist in the data set at very low prevalence, such as offices with heating set points of 61°F. These outliers are incorporated into ComStock models at a similar low prevalence to reflect the wide diversity of commercial buildings.

<div id="tab:bas_thermostat_count_by_btype">

| **Building Type**       | **Building Count** |
|:------------------------|:-------------------|
| Food Service/Restaurant | 1,817              |
| Mercantile Retail       | 1,692              |
| Food Sales/Grocery      | 164                |
| Office                  | 31                 |
| School                  | 16                 |
| Warehouse               | 4                  |
| Hotel                   | 4                  |
| Hospital                | 2                  |
| Outpatient              | 2                  |

Building Counts With Thermostat Data by Building Type

</div>

<figure id="fig:htg_therm_setpoints">
<img src="figures/heating_setpoints.png" style="width:100.0%" />
<figcaption>Heating thermostat set point (Fahrenheit) distributions per building type.</figcaption>
</figure>

<figure id="fig:clg_therm_setpoints">
<img src="figures/cooling_setpoints.png" style="width:100.0%" />
<figcaption>Cooling thermostat set point (Fahrenheit) distributions per building type.</figcaption>
</figure>

### Unoccupied Thermostat Setbacks

An unoccupied thermostat setback defines the difference in the temperature set point from the occupied thermostat set point, for either heating or cooling, which is used during periods where the building is unoccupied. For example, an office might have an occupied heating set point of 71°F, but an unoccupied thermostat setback of 6°F for when the building is unoccupied, resulting in an unoccupied thermostat set point of 65°F (71°F - 6°F). This setback would be expected to save HVAC energy by relaxing the temperature requirements when there are no occupants in the building. This section describes ComStock’s methodology for assigning unoccupied thermostat setback prevalence, as well as the setback temperature delta, for both heating and cooling.

The prevalence of thermostat setbacks in ComStock models is determined by building type using CBECS 2012. Each building type has some fraction of buildings with a thermostat setback, and some fraction without. The CBECS survey does not provide details on thermostat set point and setback temperatures, but it does provide survey responses as to whether heating and cooling setbacks are used, and whether these setbacks are manual. The survey responses are summarized by building type in Figure <a href="#fig:cbecs_therm_setback_summary" data-reference-type="ref" data-reference="fig:cbecs_therm_setback_summary">[fig:cbecs_therm_setback_summary]</a>. However, it seems likely that many respondents who claim to implement manual setbacks do not reliably do so; we made a conservative assumption that only 20% of manual setbacks would be counted as reliably practicing thermostat setbacks (manually adjusting the thermostat every night before leaving and every morning upon entering). The fraction of ComStock models that include thermostat setbacks is shown in Table <a href="#tab:thermostat_setback_prev" data-reference-type="ref" data-reference="tab:thermostat_setback_prev">7</a>. Note that the timing of the thermostat setbacks coincides with the assigned hours of operation for a specific model, the methodology for which is described in Section <a href="#sec:hoo" data-reference-type="ref" data-reference="sec:hoo">[sec:hoo]</a>.

<div id="tab:thermostat_setback_prev">

| **Building Type**      | **Fraction of Models With Thermostat Setback** |
|:-----------------------|:-----------------------------------------------|
| FullServiceRestaurant  | 0.57                                           |
| Grocery                | 0.63                                           |
| LargeOffice            | 0.77                                           |
| MediumOffice           | 0.76                                           |
| PrimarySchool          | 0.9                                            |
| QuickServiceRestaurant | 0.46                                           |
| RetailStandalone       | 0.63                                           |
| RetailStripmall        | 0.9                                            |
| SecondarySchool        | 0.95                                           |
| SmallOffice            | 0.77                                           |
| Warehouse              | 0.56                                           |

Fraction of ComStock Buildings With Thermostat Setbacks by Building Type

</div>

### Unoccupied Thermostat Setbacks Informed by Building Automation System Data

The method for determining the magnitude of the temperature setback for buildings with unoccupied temperature setbacks is described in this section. This methodology is used for the following building types: full service restaurant, large office, medium office, primary school, quick service restaurant, retail standalone, retail strip mall, secondary school, small office, and warehouse. In warehouse buildings, this methodology only applies to the office space type within the building.

The magnitudes of the temperature setbacks are determined using the same data sets and methods described in Section <a href="#section:therm_setpoints_bas" data-reference-type="ref" data-reference="section:therm_setpoints_bas">1.7.1</a> for thermostat set points; probability distributions are created for each building type. The relationship between the thermostat set points and the delta setbacks is shown in Figure <a href="#fig:therm_setpoint_setback" data-reference-type="ref" data-reference="fig:therm_setpoint_setback">[fig:therm_setpoint_setback]</a>. The resulting heating and cooling thermostat delta setback temperature probability distributions, for each applicable building type, are shown in Figure <a href="#fig:therm_heating_setback" data-reference-type="ref" data-reference="fig:therm_heating_setback">9</a> and Figure <a href="#fig:therm_cooling_setback" data-reference-type="ref" data-reference="fig:therm_cooling_setback">10</a>, respectively.

<figure id="fig:therm_heating_setback">
<img src="figures/heating_setbacks.png" style="width:100.0%" />
<figcaption>Thermostat heating setback delta temperature probability distributions per building type.</figcaption>
</figure>

<figure id="fig:therm_cooling_setback">
<img src="figures/cooling_setbacks.png" style="width:100.0%" />
<figcaption>Thermostat cooling setback delta temperature probability distributions per building type.</figcaption>
</figure>

### Thermostat Setpoints Not Informed by Building Automation System Data

The following ComStock building types do not infer thermostat setpoints from the BAS data, and therefore each have there own methodology previously described in this section: Hospitals, Outpatient, Warehouses, Small Hotels, and Large Hotels.

#### Warehouses

Heating thermostat setpoints for warehouse storage spaces are adjusted from the DOE/DEER prototype model defaults in order to better calibrate warehouse energy consumption to the CBECS truth data set, informed by CBECS 2018 (U.S. Energy Information Administration 2018a) responses to the “Percent Heated” and “Percent Cooled” questions as well as engineering judgement. The default DOE prototype setpoint value of 45°F (50°F for buildings built after 2004) was increased, and the default DEER prototype setpoint value of 70°F was decreased, both to a new heating setpoint of 61°F. Cooling thermostat setpoints remained unchanged, except for California (DEER prototype) warehousees, which are modeled as heated-only.

## Unoccupied Air Handling Unit Operation

Commercial buildings require constant design outdoor air ventilation rates when the building is occupied per ASHRAE-90.1. For air handling units (AHUs), the outdoor air is generally mixed with the supply air. This requires constant supply fan operation to maintain the outdoor air requirements established by ASHRAE-62.1 (ASHRAE 2004). However, AHUs do not need to provide outdoor ventilation air when the building is unoccupied. Therefore, ASHRAE-90.1 requires outdoor air dampers to close when the building is unoccupied, and to only cycle on supply fans as needed to maintain thermostat set points. This control scheme can have a large impact on energy usage, and data suggests that not all buildings implement these controls in their AHU systems. This section discusses ComStock’s methodology for including the prevalence of different unoccupied AHU control schemes observed in real buildings, which follows the methodology used in (CaraDonna and Dombrovski 2022).

An industry-provided BAS data set of over 5,700 AHUs was used to inform the prevalence of three unoccupied AHU operation modes. The data set includes time series (hourly) BAS variables for “Occupied Status” (describes whether the AHU was in an occupied mode for that hour), “Fan Status” (describes whether the fan was used for that hour), and “Ventilation Status” (describes whether outdoor ventilation air was used for that hour). Counts of AHUs and buildings by building type in the data set are shown in Table <a href="#tab:unnoc_ahu_data_counts" data-reference-type="ref" data-reference="tab:unnoc_ahu_data_counts">8</a>, and the three unoccupied AHU shutdown control schemes are summarized in Table <a href="#tab:unnoc_ahu_schemes" data-reference-type="ref" data-reference="tab:unnoc_ahu_schemes">9</a>.

The data set suggests that 27% of AHUs use scheme 1 (least efficient), 50% of AHUs use scheme 2 (more efficient), and 23% of AHUs use scheme 3 (most efficient; ASHRAE-90.1 required). The prevalence of the AHU unoccupied control schemes by building type is shown in Table <a href="#tab:unnoc_ahu_scheme_prev" data-reference-type="ref" data-reference="tab:unnoc_ahu_scheme_prev">[tab:unnoc_ahu_scheme_prev]</a>. These probability distributions are used in ComStock sampling to set the fraction of buildings utilizing the discussed control schemes, by building type, for models that use AHU-based HVAC systems. Non-AHU HVAC system types are not applicable to this methodology, nor are building types not listed in Table <a href="#tab:unnoc_ahu_scheme_prev" data-reference-type="ref" data-reference="tab:unnoc_ahu_scheme_prev">[tab:unnoc_ahu_scheme_prev]</a>. Note that building types with less than 25 buildings in the BAS data set (Table <a href="#tab:unnoc_ahu_data_counts" data-reference-type="ref" data-reference="tab:unnoc_ahu_data_counts">8</a>) use the “All Types” distribution of the data set at large, as fewer than 25 samples cannot reliably be used to represent a population.

The following building types are not included in the unnocupied air handling unit operation workflow, and utilize default scheduling only: small hotels, large hotels, outpatient, hospitals, primary schools, and secondary schools. The building types may be integrated into this workflow in the future as more data becomes available.

<div id="tab:unnoc_ahu_data_counts">

| **Building Type** | **Site Count** | **AHU Count** |
|:------------------|:---------------|:--------------|
| **All Types**     | 843            | 5,706         |
| **Retail**        | 541            | 3,300         |
| **Unknown**       | 164            | 1,391         |
| **Office**        | 43             | 466           |
| **Restaurant**    | 39             | 155           |
| **Grocery**       | 35             | 212           |
| **Hotel**         | 6              | 46            |
| **Education**     | 6              | 29            |
| **Warehouse**     | 5              | 94            |
| **Healthcare**    | 4              | 13            |

Site and AHU Counts of Time Series BAS Data per Building Type

</div>

<div id="tab:unnoc_ahu_schemes">

| **Scheme Name** | **Unoccupied Control Scheme Description** | **Expected Efficiency** | **Occupied Status** | **Fan Status** | **Ventilation Status** |
|:---|:---|:---|:---|:---|:---|
| **Scheme 1** | Scheduled on, running | Least Efficient | Active | Active | Active |
| **Scheme 2** | Scheduled off, fan cycles with ventilation to maintain thermostat setpoints | More Efficient | Inactive | Active | Active |
| **Scheme 3** | Scheduled off, fan cycles without ventilation to maintain thermostat setpoints | Most Efficient | Inactive | Active | Inactive |

AHU Operating Mode Schemes Used During Scheduled Unoccupied Times

</div>

## Demand Control Ventilation

Demand control ventilation (DCV) acts to reduce outdoor air ventilation during periods of detected low occupancy. Occupancy levels are generally detected through the use of CO<sub>2</sub> sensors located directly in the space or within the HVAC system.

DCV is included in ComStock models when required by the governing ASHRAE-90.1 energy code for the specific spaces/systems in the model. ComStock gathers the necessary criteria for determining DCV requirements and includes DCV functionality only if the space/system requires it. The requirement criteria for DCV include space floor area, space design occupant density, system economizer prevalence, system design outdoor air flow rate, and system energy recovery prevalence. The 90.1 code year for a model is based on the year of the model’s last major HVAC replacement. Code year assignment and system turnover assumptions are described further in Section <a href="#sec:system_turnover_and_eul" data-reference-type="ref" data-reference="sec:system_turnover_and_eul">[sec:system_turnover_and_eul]</a>. A summary of the floor area served by a system with DCV is shown in Table <a href="#tab:dcv_prev" data-reference-type="ref" data-reference="tab:dcv_prev">[tab:dcv_prev]</a>. Note that DCV is not required by ASHRAE 90.1 when an HVAC system has an ERV. One important observation from these data is that no office buildings include DCV. This is because office buildings are currently modeled using a single, blended space type that is a fractional mix of open offices, enclosed offices, conference rooms, etc. The occupancy density of this blended space does not exceed the DCV thresholds in ASHRAE 90.1. This leads to unrealistically low (0%) DCV in office buildings. Another important observation is that DCV is not modeled in any of the buildings in California (which use the DEER data set), although this does not align with the newer versions of Title 24. DCV is expected to be implemented in California buildings in the near future.

## Air-Side Energy Recovery

Energy recovery ventilators (ERVs) in AHUs reduce energy consumption by pre-conditioning the incoming outdoor air using the system exhaust air, which reduces the heating and cooling energy required to condition the air. Energy recovery is especially effective in systems serving spaces with high outdoor air ventilation loads.

ERVs are included in ComStock model HVAC systems only when required by the governing energy code for the specific system. This determination is made using OpenStudio-Standards, where the necessary ComStock model properties are gathered to determine whether an ERV is required for each system. These properties include the climate zone, percent outdoor air, and design supply airflow rate, aligning with ASHRAE-90.1 Table 6.5.6.1 for the respective energy code year followed. A summary of the floor area served by systems with energy recovery is shown in Table <a href="#tab:energy_recovery_prev" data-reference-type="ref" data-reference="tab:energy_recovery_prev">10</a>.

<div id="tab:energy_recovery_prev">

| **Building Type** | **Pre-1980** | **1980-2004** | **90.1-2004** | **90.1-2007** | **90.1-2010** | **90.1-2013** | **DEER All Years** |
|:---|:---|:---|:---|:---|:---|:---|:---|
| FullServiceRestaurant | 0 | 0 | 0.051 | 0.027 | 0.347 | 0.392 | 0 |
| Hospital | 0 | 0 | 0.457 | 0.442 | 0.613 | 0.871 | 0 |
| LargeHotel | 0 | 0 | 0.109 | 0.09 | 0.267 | 0.245 | 0 |
| LargeOffice | 0 | 0 | 0.028 | 0.035 | 0.139 | 0.519 | 0 |
| MediumOffice | 0 | 0 | 0.007 | 0.016 | 0.093 | 0.306 | 0 |
| Outpatient | 0 | 0 | 0.087 | 0.078 | 0.095 | 0.246 | 0 |
| PrimarySchool | 0 | 0 | 0.376 | 0.41 | 0.597 | 0.639 | 0 |
| QuickServiceRestaurant | 0 | 0 | 0 | 0 | 0.088 | 0.063 | 0 |
| RetailStandalone | 0 | 0 | 0.027 | 0.022 | 0.029 | 0.306 | 0 |
| RetailStripmall | 0 | 0 | 0.115 | 0.111 | 0.191 | 0.435 | 0 |
| SecondarySchool | 0 | 0 | 0.540 | 0.530 | 0.675 | 0.725 | 0 |
| SmallHotel | 0 | 0 | 0.186 | 0 | 0.092 | 0 | 0 |
| SmallOffice | 0 | 0 | 0 | 0 | 0.044 | 0.050 | 0 |
| Warehouse | 0 | 0 | 0.065 | 0.053 | 0.069 | 0.083 | 0 |

Fraction of Floor Area Served by HVAC Systems With Energy Recovery by Building Type and Code Year

</div>

An enthalpy wheel ERV system (rotary) is added to the HVAC systems in ComStock models where an ERV is determined to be required. The effectiveness of the system is 50% for all conditions, aligning with the requirements of ASHRAE-90.1. Economizer lockout and supply air bypass for temperature control are included. The defrost type is exhaust only, which temporarily bypasses the supply side of the heat exchanger to allow warmer exhaust air to remove frost uninhibited when needed.

## Air-Side Economizers

Air-side economizers reduce HVAC cooling energy by increasing the amount of outdoor ventilation air during times when the temperature and/or enthalpy are beneficial for cooling. For example, if the outdoor air temperature is 55°F when the building needs cooling, the HVAC system can increase the amount of outdoor ventilation air being delivered to the space to satisfy some or all of the cooling requirement in place of mechanical cooling.

As described in Section <a href="#sec:system_turnover_and_eul" data-reference-type="ref" data-reference="sec:system_turnover_and_eul">[sec:system_turnover_and_eul]</a>, we assume that some building systems, including the HVAC system, are replaced over the lifespan of the building. We re-evaluate the requirement for an air-side economizer based on the energy code in force at the time of the latest HVAC system replacement. For buildings outside of CA, energy code requirements were taken from ASHRAE 90.1. For buildings inside CA, the CA energy code requirements were evaluated taken from the CA DEER MASControl3 models (Hirsch 2021), where the economizer limits and applicability were found as shown in Table <a href="#tab:econ_lims_mascontrol3" data-reference-type="ref" data-reference="tab:econ_lims_mascontrol3">11</a> and Table <a href="#tab:econ_applic_mascontrol3" data-reference-type="ref" data-reference="tab:econ_applic_mascontrol3">12</a>.

<div id="tab:econ_lims_mascontrol3">

| **Climate Zone** | **Drybulb Limit (°F)** | **Enthalpy Limit (Btu/lb)** |
|:-----------------|:-----------------------|:----------------------------|
| CZ01             | 70                     | 28                          |
| CZ02             | 73                     | 28                          |
| CZ03             | 70                     | 28                          |
| CZ04             | 73                     | 28                          |
| CZ05             | 70                     | 28                          |
| CZ06             | 71                     | 28                          |
| CZ07             | 69                     | 28                          |
| CZ08             | 71                     | 28                          |
| CZ09             | 71                     | 28                          |
| CZ10             | 73                     | 28                          |
| CZ11             | 75                     | 28                          |
| CZ12             | 75                     | 28                          |
| CZ13             | 75                     | 28                          |
| CZ14             | 75                     | 28                          |
| CZ15             | 75                     | 28                          |
| CZ16             | 75                     | 28                          |

Economizer limits from MASControl3

</div>

<div id="tab:econ_applic_mascontrol3">

| **Vintage** | **Packaged DX** | **Chilled Water** | **Water Loop HP** |
|:------------|:----------------|:------------------|:------------------|
| 1975        | FALSE           | TRUE              | FALSE             |
| 1985        | FALSE           | TRUE              | FALSE             |
|  1996       | FALSE           | TRUE              | FALSE             |
| 2003        | FALSE           | TRUE              | FALSE             |
| 2007        | FALSE           | TRUE              | FALSE             |
| 2011        | FALSE           | TRUE              | FALSE             |
| 2014        | TRUE            | TRUE              | TRUE              |
| 2015        | TRUE            | TRUE              | TRUE              |
| 2017        | TRUE            | TRUE              | TRUE              |
| 2020        | TRUE            | TRUE              | TRUE              |

Economizer applicability from MASControl3

</div>

Figure <a href="#fig:economizer_presence" data-reference-type="ref" data-reference="fig:economizer_presence">11</a> shows the prevalence of economizers (in terms of floor area coverage and contribution to cooling energy) for different subcategories (building type and ventilation system type) of the existing building stock. The percentage of floor area where "economizer availability" is "True" includes the total building area if there is at least one economizer in the building. It does not represent the total floor area served by systems with economizers. While there are buildings that already include economizers in variable air volume (VAV) systems and roof top units (RTU) covering 40% of the total floor area and 28% of total electricity used for cooling, the remaining portion of buildings with those system types do not include economizers.

<figure id="fig:economizer_presence">
<img src="figures/economizer_presence.png" style="width:70.0%" />
<figcaption>Presence of air-side economizers in the building stock.</figcaption>
</figure>

Based on a large body of anecdotal evidence from conversations with fault-focused field engineers and a brief review of common current (Trane, Carrier, Daikin) rooftop unit product data sheets (Trane 2023), (Carrier 2023), (Daikin 2023), fixed dry bulb controls are a more common choice than differential dry bulb controls, although manufacturers also offer dual enthalpy (fixed dry bulb + fixed enthalpy) options with the addition of an enthalpy sensor. For this reason, fixed dry bulb controls are assumed for almost all building vintages and climate zones, with the exception being ASHRAE 90.1-2010 and 2013, which prohibited fixed dry bulb economizers in the warmer humid climate zones. These restrictions were lifted in ASHRAE 90.1-2016.

Figure <a href="#fig:economizer_prevalence" data-reference-type="ref" data-reference="fig:economizer_prevalence">12</a> shows the comparison of economizer coverage with respect to building floor area between ComStock and estimation from Commercial Buildings Energy Consumption Survey (U.S. Energy Information Administration 2018a). Because of how data is structured in CBECS, the floor area shown in these figures represents the entire floor area of the building if any economizer is present in any of the HVAC systems in the building rather than actual floor area covered by HVAC systems with an economizer. Because CBECS data only shows total building area instead of total area covered by the economizers, this comparison helps give a rough estimate of economizers.

<figure id="fig:economizer_prevalence">
<img src="figures/economizer_prevalence.png" style="width:70.0%" />
<figcaption>Economizer floor area coverage comparing ComStock (left) with CBECS 2018 (right).</figcaption>
</figure>

Economizers are well known for frequent faulty operations. There were many efforts in the past to understand fault characteristics in commercial buildings (Kim et al. 2021), (Crowe et al. 2022), (Katipamula et al. 2021), (Frank et al. 2018). While this evidence is insufficient to reflect all aspects (e.g., prevalence, incidence, intensity, and evolution described in (Kim et al. 2021)) of all faults in the commercial building stock across the country, it is possible to make simplifications for modeling certain fault types based on available data.

Figure <a href="#fig:econ_temp_fault" data-reference-type="ref" data-reference="fig:econ_temp_fault">13</a> shows how the first fault is modeled for buildings with economizers. Crowe et al. (Crowe et al. 2022) acquired data from AFDD venders that monitored 3,660 AHUs and 7,974 RTUs and reported 31% of all economizers were experiencing faulty operations. Shoukas et al. (Shoukas et al. 2020) received data from a clothing retailer and food chain that monitored 1,416 RTUs and reported 60% of all faults related to economizers were related to economizer not effectively reducing cooling load compared to the theoretical potential. The symptom described as "ineffective economizing" can be due to different faults: damper stuck, damper bias, sensor bias, sensor frozen, inappropriate configuration, etc. A report (Seventhwave and Center for Energy and Environment 2016) published by Minnesota Department of Commerce Division of Energy Resources monitored 41 RTUs in Minnesota that were installed in many different building types (e.g., office, restaurant, retail, hotel, etc.) and reported the actual changeover temperature setting in the economizer were not configured efficiently (average of 52°F) resulting in missed free cooling opportunity.

Based on this information focusing on different aspects of the fault, a fault measure was developed as shown in Figure <a href="#fig:econ_temp_fault" data-reference-type="ref" data-reference="fig:econ_temp_fault">13</a>. The figure includes a description of the fault as well as four different metrics that define the characteristics of a fault. Fault intensity (or severity) is when a fault can have a severity level. For example, if the sensor is drifting, the intensity is the difference between the true value and the biased measured value. Fault prevalence refers to the portion of systems or components with the fault among all systems or components in the sample space (e.g., 30% of all economizers have the fault). Fault incidence refers to the occurrence rate of a fault for a given system or component over for a given time period (e.g., economizer damper gets stuck once every year). Fault evolution refers to certain faults where the severity naturally changes over time. For example, sensor drift is typically a fault where the severity changes over the course of time. For the incorrect high limit setting described in Figure <a href="#fig:econ_temp_fault" data-reference-type="ref" data-reference="fig:econ_temp_fault">13</a>, the fault changes the changeover temperature setting of an economizer to 52°F and applies to 30% of economizers that use fixed dry-bulb control. Fault incidence and fault evolution were not modeled because these aspects are mostly irrelevant for this fault.

<figure id="fig:econ_temp_fault">
<img src="figures/econ_temp_fault.png" style="width:70.0%" />
<figcaption>Economizer incorrect changeover temperature setting fault description.</figcaption>
</figure>

Figure <a href="#fig:econ_temp_fault_single_model" data-reference-type="ref" data-reference="fig:econ_temp_fault_single_model">14</a> shows a comparison of simulated operation with and without the fault. As a result, the fault will reduce the changeover (high limit) temperature of the economizer, disabling the economizer even if the outdoor air temperature is favorable (e.g., 52-72°F), thus, losing opportunities for free cooling. The figure shows how the fault impacts the annual cooling energy, how the changepoint temperature changes with fault, and how the transient response changes.

<figure id="fig:econ_temp_fault_single_model">
<img src="figures/econ_temp_fault_single_model.png" style="width:70.0%" />
<figcaption>Economizer incorrect changeover temperature setting fault impact on simulation results.</figcaption>
</figure>

As reported by Heinemeier (Heinemeier 2014), contractors in California stated that 30-40% of economizers they have worked with were disabled with fully closed dampers. This is often caused by mechanical linkage issues between damper and actuator, where the economizer automatically reverts to the fully closed position as a safety measure. An economizer with a fully closed damper will not draw any fresh outdoor air, causing an air quality issue. Depending on the outdoor air condition (i.e., favorable or not favorable for economizing), it can either reduce or increase energy consumption. Figure <a href="#fig:econ_damper_fault" data-reference-type="ref" data-reference="fig:econ_damper_fault">15</a> shows the description of the fault for the economizer outdoor air damper fully closed and stuck. Unlike the fault described in Figure <a href="#fig:econ_temp_fault" data-reference-type="ref" data-reference="fig:econ_temp_fault">13</a>, this fault has a bigger impact on air quality and energy and the incidence of the fault is important.

<figure id="fig:econ_damper_fault">
<img src="figures/econ_damper_fault.png" style="width:70.0%" />
<figcaption>Economizer damper stuck closed fault description.</figcaption>
</figure>

Figure <a href="#fig:econ_damper_fault_single_model" data-reference-type="ref" data-reference="fig:econ_damper_fault_single_model">16</a> shows example simulation results for a building with and without the damper fully closed fault. The fault was imposed once during the entire April period resulting in 1.8% mechanical load increase. As mentioned previously, the energy impact of the fault can either be increased or decreased energy consumption, and Figure <a href="#fig:econ_damper_fault_single_model" data-reference-type="ref" data-reference="fig:econ_damper_fault_single_model">16</a>(c) highlights the transition from negative to positive savings when the outdoor air temperature transitions from favorable to unfavorable conditions.

<figure id="fig:econ_damper_fault_single_model">
<img src="figures/econ_damper_fault_single_model.png" style="width:70.0%" />
<figcaption>Economizer damper stuck closed fault impact on simulation results.</figcaption>
</figure>

Although faults (e.g., damper fully closed) are implemented with fixed prevalence (e.g., 35%), the actual percentage of economizers being faulted (among applicable economizers) is less than the defined prevalence due to implementation limitations. For example, 35% of randomly selected buildings that include certain HVAC system types (categorized by the air system) are assigned the damper fully closed fault. However, certain portions of these air systems do not have economizers, thus, they cannot have an economizer fault. In other words, the current limitation is that the random selection of faulted economizers is not fully aligned with buildings that actually have economizers. In these cases, we are losing the opportunity for applying faults and decreasing the representation of fault prevalence in final building stock. Newer versions of California’s Title 24 energy code requires fault detection and diagnostics (FDD) for economizers which should prevent and mitigate faults. However, ComStock does not reflect the impact of FDD technology, possibly overestimating the impact of faults in buildings with newer HVAC systems in California.

## Furnaces

Furnaces are used in a variety of HVAC equipment for space heating through the direct combustion of a fuel. For ComStock models, the fuel type can be natural gas, propane, or fuel oil. The following ComStock system types use furnaces: direct evaporative coolers with forced air furnace, gas unit heaters, PSZ-AC with gas coil, PTAC with gas coil, residential AC with residential forced air furnace, and residential forced air furnace.

### Furnace Efficiencies

Furnaces in ComStock are all assumed to be standard, non-condensing types at this time. Rated efficiency assignments are a function of capacity and in-force HVAC template code. The furnace efficiency assignments are summarized in Table <a href="#tab:furnace_eff_assignments" data-reference-type="ref" data-reference="tab:furnace_eff_assignments">13</a>.

### Furnace Performance Modifiers

Furnaces in ComStock do not use any performance curves, so there is no change in efficiency or capacity as a function of temperature or part load ratio, and therefore no cycling losses. Furthermore, no parasitic fuel losses are included in ComStock furnace models.

<div id="tab:furnace_eff_assignments">

<table>
<caption>Furnace Efficiency by Capacity and Code Year</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Template</strong></th>
<th style="text-align: left;"><strong>Minimum Capacity (Btu/hr)</strong></th>
<th style="text-align: left;"><strong>Maximum Capacity (Btu/hr)</strong></th>
<th style="text-align: left;"><strong>Minimum Annual Fuel Utilization Efficiency (AFUE)</strong></th>
<th style="text-align: left;"><strong>Minimum Thermal Efficiency (%)</strong></th>
<th style="text-align: left;"><strong>Minimum Combustion Efficiency (%)</strong></th>
<th style="text-align: left;"><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Pre-1980</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">249,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">Pre-1980</td>
<td style="text-align: left;">250,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">Pre-1980</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">1980-2004</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">1980-2004</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">90.1-2004</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">224,999</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
<td rowspan="10" style="text-align: left;">Table 6.8.1E page 49</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2004</td>
<td style="text-align: left;">225,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2007</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">224,999</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2007</td>
<td style="text-align: left;">225,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2010</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">224,999</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2010</td>
<td style="text-align: left;">225,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2013</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">224,999</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2013</td>
<td style="text-align: left;">225,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2016</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">224,999</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2016</td>
<td style="text-align: left;">225,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">90.1-2019</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">224,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: left;">-</td>
<td rowspan="2" style="text-align: left;">Table 6.8.1-6 for &gt;225 kBtu/hr; Table F-4 for &lt;225 kBtu/hr</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2019</td>
<td style="text-align: left;">225,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
</tbody>
</table>

</div>

## Boilers

Boilers create hot water for heating in buildings. The following ComStock HVAC types use boilers for heating: baseboard gas boiler, DOAS with fan coil air-cooled chiller with boiler, DOAS with fan coil chiller with boiler, DOAS with fan coil district chilled water with boiler, DOAS with water source heat pumps cooling tower with boiler, direct evaporative coolers with baseboard gas boiler, PSZ-AC with gas boiler, PTAC with gas boiler, PVAV with gas boiler reheat, VAV air-cooled chiller with gas boiler reheat, VAV chiller with gas boiler reheat, and VAV district chilled water with gas boiler reheat.

### Boiler Efficiencies

At this time, boiler systems in ComStock are all gas-fired (or other combustible fuels) storage tank non-condensing units. A single boiler is used to meet the hot water load for the entire building. Rated efficiency assignments are a function of the HVAC code year and boiler capacity, mirroring the requirements of ASHRAE-90.1, and are summarized in Table <a href="#tab:boiler_eff_table" data-reference-type="ref" data-reference="tab:boiler_eff_table">14</a>.

### Boiler Part Load Efficiencies

Boiler efficiency at different part load conditions is modeled through an assigned efficiency as a function of a part load ratio (PLR) cubic curve. The output of this curve is multiplied by the full load rated efficiency, providing the effective efficiency of the boiler for each time step. The performance curve assignments for different boiler scenarios are summarized in Table <a href="#tab:boiler_eff_table" data-reference-type="ref" data-reference="tab:boiler_eff_table">14</a>. The curve features are shown in Table <a href="#tab:boiler_plr_curve_table" data-reference-type="ref" data-reference="tab:boiler_plr_curve_table">[tab:boiler_plr_curve_table]</a>, and the curves are illustrated in Figure <a href="#fig:blr_plr_curves" data-reference-type="ref" data-reference="fig:blr_plr_curves">[fig:blr_plr_curves]</a>.

Table <a href="#tab:boiler_eff_table" data-reference-type="ref" data-reference="tab:boiler_eff_table">14</a> shows the older DOE reference building templates using a constant efficiency curve for the boiler (“Boiler Constant Efficiency Curve”). Therefore, these boilers do not currently have efficiency modifications at different part load conditions. This likely underestimates cycling losses that boilers experience at lower PLRs, and may underestimate their gas usage. The 90.1 templates for 2004 through 2010 exclusively use a performance curve for boilers with no turndown controls (“Boiler With No Minimum Turndown”). This provides some efficiency loss, as PLR is reduced. For 90.1-2013 and beyond, performance curves for boilers with minimum turndowns (“Boiler With Minimum Turndown”) are added for larger boiler systems. This provides a slight performance improvement compared to boilers with no minimum turndown. All three curves are illustrated in Figure <a href="#fig:blr_plr_curves" data-reference-type="ref" data-reference="fig:blr_plr_curves">[fig:blr_plr_curves]</a>.

### Boiler Controls

ComStock boilers use 180°F hot water loops with flow that leaves the set point modulated, meaning the boiler model internally varies the flow rate so that the temperature leaving the boiler matches a set point. The delta T of the loop is 20°F.

<div id="tab:boiler_eff_table">

<table>
<caption>Boiler Efficiency and Performance Curve Assignment</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Template</strong></th>
<th style="text-align: left;"><strong>Minimum Capacity (Btu/hr)</strong></th>
<th style="text-align: left;"><strong>Maximum Capacity (Btu/hr)</strong></th>
<th style="text-align: left;"><strong>Minimum Annual Fuel Utilization Efficiency (AFUE)</strong></th>
<th style="text-align: left;"><strong>Minimum Thermal Efficiency (%)</strong></th>
<th style="text-align: left;"><strong>Minimum Combustion Efficiency (%)</strong></th>
<th style="text-align: left;"><strong>Efficiency Function of Part Load Ratio (EFFFPLR)</strong></th>
<th style="text-align: left;"><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Pre-1980</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.73</td>
<td style="text-align: left;"></td>
<td rowspan="5" style="text-align: left;">Boiler Constant Efficiency Curve</td>
<td rowspan="3" style="text-align: left;">From DOE Reference Buildings</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> Pre-1980</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.74</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> Pre-1980</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.76</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 1980-2004</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">From 90.1-1989</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 1980-2004</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
</tr>
<tr>
<td style="text-align: left;">90.1-2004</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td rowspan="11" style="text-align: left;">Boiler with No Minimum Turndown</td>
<td rowspan="3" style="text-align: left;">From 90.1-2004</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2004</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.75</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2004</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2007</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td rowspan="3" style="text-align: left;">From 90.1-2007</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2007</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2007</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.82</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2010</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td rowspan="3" style="text-align: left;">From 90.1-2010</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2010</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2010</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.82</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2013</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">0.82</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td rowspan="8" style="text-align: left;">From 90.1-2013</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2013</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-7</span> 90.1-2013</td>
<td style="text-align: left;">1,000,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Boiler with Minimum Turndown</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2013</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.82</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-7</span> 90.1-2016</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">0.82</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Boiler with No Minimum Turndown</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2016</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-7</span> 90.1-2016</td>
<td style="text-align: left;">1,000,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Boiler with Minimum Turndown</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2016</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.82</td>
</tr>
<tr>
<td style="text-align: left;">90.1-2019</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">0.84</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Boiler with No Minimum Turndown</td>
<td rowspan="4" style="text-align: left;">From 90.1-2019</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2019</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-7</span> 90.1-2019</td>
<td style="text-align: left;">1,000,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Boiler with Minimum Turndown</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2019</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.82</td>
</tr>
</tbody>
</table>

</div>

## Direct Expansion Cooling

Standard air-cooled direct expansion (DX) cooling is the most prevalent cooling equipment type in commercial buildings. The following ComStock HVAC system types use DX cooling: PSZ-AC with district hot water, PSZ-AC with electric coil, PSZ-AC with gas boiler, PSZ-AC with gas coil, PSZ-HP, PTAC with baseboard district hot water, PTAC with electric coil, PTAC with gas boiler, PTAC with gas coil, PTHP, PVAV with PFP boxes, PVAV with district hot water reheat, PVAV with gas boiler reheat, PVAV with gas heat with electric reheat, and residential AC with residential forced air furnace.

### DX Cooling Rated Performance

DX cooling systems are assigned full load and part load efficiencies based on the HVAC code template for the model and the capacity. These assignments are summarized in Table<a href="#tab:unitary_dx_efficiencies" data-reference-type="ref" data-reference="tab:unitary_dx_efficiencies">[tab:unitary_dx_efficiencies]</a> (unitary DX) and Table<a href="#tab:ptac_efficiencies" data-reference-type="ref" data-reference="tab:ptac_efficiencies">[tab:ptac_efficiencies]</a> (PTAC). These values mirror those found in ASHRAE-90.1 (or those used in the DOE reference buildings for the pre-1980 template).

### DX Cooling Performance Modifiers

The performance of DX cooling equipment changes based on operating conditions. ComStock DX cooling equipment uses five performance modifier curves to model this behavior. Energy input ratio (EIR) as a function of part load ratio (PLR) describes how the equipment efficiency varies at different load fractions, accounting for equipment cycling (Figure <a href="#fig:dx_eirfplr" data-reference-type="ref" data-reference="fig:dx_eirfplr">[fig:dx_eirfplr]</a>). EIR as a function of temperature describes how the equipment efficiency varies based on both the outdoor air dry bulb temperature and the wet bulb temperature of the air entering the cooling coil (Figure <a href="#fig:dx_eirft" data-reference-type="ref" data-reference="fig:dx_eirft">[fig:dx_eirft]</a>). EIR as a function of airflow describes how the equipment efficiency varies as a function of the supply airflow fraction (Figure <a href="#fig:dx_eirff" data-reference-type="ref" data-reference="fig:dx_eirff">[fig:dx_eirff]</a>). Capacity as a function of temperature describes how the equipment available capacity varies as a function of both the outdoor air dry bulb temperature and the wet bulb temperature of the air entering the cooling coil (Figure <a href="#fig:dx_capft" data-reference-type="ref" data-reference="fig:dx_capft">[fig:dx_capft]</a>). Lastly, capacity as a function of airflow describes how the equipment available capacity varies as a function of the supply airflow fraction (Figure <a href="#fig:dx_capff" data-reference-type="ref" data-reference="fig:dx_capff">[fig:dx_capff]</a>). The outputs of the EIR modifiers are multiplied against the nominal EIR at every time step (except for the PLR modifier, which is divided), which provides the effective EIR at each time step. Meanwhile, the outputs of the two capacity modifiers are multiplied against the nominal capacity at every time step, yielding the effective available capacity for the time step.

## Air-Source Heat Pumps

Air-source heat pumps (ASHPs) provide electric heating using a reverse vapor compression cycle. This generally provides a higher COP option for electric heating compared to standard electric resistance electric heating. In most cases, ASHPs use the same air-cooled DX system for both DX heating and DX cooling. ASHPs can be split system, packaged units, or through-the-wall packaged terminal heat pumps (PTHP). The following ComStock HVAC systems types use ASHPs: packaged single zone heat pump (PSZ-HP) and PTHP.

ASHP sizing is often based on the design cooling requirements. Because the DX cooling and heating use the same compressor system, the capacities for each are coupled. ASHPs generally have a minimum operating temperature, below which the DX heating is disabled due to lack of capacity and efficiency. To remedy this, backup heating is often included in colder climates, and for any system where the design heating load is higher than the design cooling load. ComStock ASHP sizing follows this methodology: ASHPs are sized to meet the design cooling load, and backup electric heating is added to the system to meet the design heating load when the available DX heating capacity is unavailable or insufficient. The minimum temperature for compressor operation for ComStock heat pump systems is 17°F PTHP and 10°F for PSZ-HP.

<div id="tab:ashp_eff">

<table>
<caption>Air-Source Heat Pump Efficiency and Performance Curve Assignment</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Template</strong></th>
<th style="text-align: left;"><strong>Cooling Type</strong></th>
<th style="text-align: left;"><strong>Subcategory</strong></th>
<th style="text-align: left;"><strong>Minimum Capacity (Btu/hr)</strong></th>
<th style="text-align: left;"><strong>Maximum Capacity (Btu/hr)</strong></th>
<th style="text-align: left;"><strong>HSPF</strong></th>
<th style="text-align: left;"><strong>Min COP</strong></th>
<th style="text-align: left;"><strong>PTHP_COP_Coefficient_1</strong></th>
<th style="text-align: left;"><strong>PTHP_COP_Coefficient_2</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5" style="text-align: left;"><strong>Pre-1980 Through 1980-2004</strong></td>
<td style="text-align: left;">AirCooled, ThroughWall</td>
<td style="text-align: left;">Split System</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">6.8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">6.6</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">65,000</td>
<td style="text-align: left;">134,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">135,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">2.9</td>
<td style="text-align: left;">0.026</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;"><strong>90.1-2004</strong></td>
<td style="text-align: left;">AirCooled, ThroughWall</td>
<td style="text-align: left;">Split System</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">6.8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled, ThroughWall</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">6.6</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">65,000</td>
<td style="text-align: left;">134,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">135,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;">0.026</td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;"><strong>90.1-2007</strong></td>
<td style="text-align: left;">ThroughWall</td>
<td style="text-align: left;">Split System</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">29,999</td>
<td style="text-align: left;">7.1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Split System, Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">7.7</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">ThroughWall</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">29,999</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">65,000</td>
<td style="text-align: left;">134,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">135,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;">0.026</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;"><strong>90.1-2010</strong></td>
<td style="text-align: left;">ThroughWall</td>
<td style="text-align: left;">Split System, Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">29,999</td>
<td style="text-align: left;">7.4</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Split System, Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">7.7</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">65,000</td>
<td style="text-align: left;">134,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">135,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;">0.026</td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;"><strong>90.1-2013</strong></td>
<td style="text-align: left;">ThroughWall</td>
<td style="text-align: left;">Split System, Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">29,999</td>
<td style="text-align: left;">7.4</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Split System</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">8.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">65,000</td>
<td style="text-align: left;">134,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">135,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.7</td>
<td style="text-align: left;">0.052</td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;"><strong>90.1-2016</strong></td>
<td style="text-align: left;">ThroughWall</td>
<td style="text-align: left;">Split System, Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">29,999</td>
<td style="text-align: left;">7.4</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Split System</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">8.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">65,000</td>
<td style="text-align: left;">134,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">135,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.7</td>
<td style="text-align: left;">0.052</td>
</tr>
<tr>
<td rowspan="8" style="text-align: left;"><strong>90.1-2019</strong></td>
<td style="text-align: left;">ThroughWall</td>
<td style="text-align: left;">Split System, Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">29,999</td>
<td style="text-align: left;">7.4</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Split System</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">8.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">65,000</td>
<td style="text-align: left;">134,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">135,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">6,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">6,999</td>
<td style="text-align: left;">14,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.7</td>
<td style="text-align: left;">0.052</td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">14,999</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">2.9</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

</div>

### ASHP Rated Performance

ASHPs in ComStock are assigned efficiencies based on ASHRAE-90.1. The assigned efficiencies are based on the template code year, the unit capacity, and the unit type. These assignments are summarized in Table <a href="#tab:ashp_eff" data-reference-type="ref" data-reference="tab:ashp_eff">15</a>.

### ASHP Performance Modifiers

Similar to DX cooling equipment, the performance of ASHP equipment changes based on different operating conditions. The curve assignments are shown in Table <a href="#tab:ashp_curves" data-reference-type="ref" data-reference="tab:ashp_curves">[tab:ashp_curves]</a>. ComStock ASHP equipment uses five performance modifier curves to model this behavior. Energy input ratio (EIR) as a function of part load ratio (PLR) describes how the equipment efficiency varies at different load fractions, where the nominal EIR is divided by the output of this curve to account for equipment cycling losses (Figure <a href="#fig:ashp_eirfplr" data-reference-type="ref" data-reference="fig:ashp_eirfplr">[fig:ashp_eirfplr]</a>). EIR as a function of temperature describes how the equipment efficiency varies based on outdoor air dry bulb temperature (Figure <a href="#fig:ashp_eirft" data-reference-type="ref" data-reference="fig:ashp_eirft">[fig:ashp_eirft]</a>). Figure <a href="#fig:ashp_eirft" data-reference-type="ref" data-reference="fig:ashp_eirft">[fig:ashp_eirft]</a> illustrates the capacity loss of ASHPs at lower outdoor air temperatures. EIR as a function of airflow describes how the equipment efficiency varies as a function of the supply airflow fraction (Figure <a href="#fig:ashp_eirff" data-reference-type="ref" data-reference="fig:ashp_eirff">[fig:ashp_eirff]</a>). Capacity as a function of temperature describes how the equipment available capacity varies as a function of outdoor air dry bulb temperature (Figure <a href="#fig:ashp_capff" data-reference-type="ref" data-reference="fig:ashp_capff">[fig:ashp_capff]</a>). Lastly, capacity as a function of airflow describes how the equipment EIR ratio varies as a function of the supply airflow fraction (Figure <a href="#fig:ashp_capff" data-reference-type="ref" data-reference="fig:ashp_capff">[fig:ashp_capff]</a>). The outputs of the EIR modifiers are multiplied against the nominal EIR at every time step (except for the PLR curve output, which is divided), which provides the effective EIR at each time step. Meanwhile, the outputs of the two capacity modifiers are multiplied against the nominal capacity at every time step, yielding the effective available capacity for the time step. The curves described here are primarily derived from the DOE prototype/reference building models.

## Air-Cooled Chillers

Air-cooled chillers (ACCs) provide chilled water for building cooling systems and use an air-cooled condenser for heat rejection. Therefore, no condenser water loop is required for ACCs. The following ComStock HVAC types use ACCs: DOAS with fan coil air-cooled chiller with baseboard electric, DOAS with fan coil air-cooled chiller with boiler, DOAS with fan coil air-cooled chiller with district hot water, DOAS with fan coil chiller with baseboard electric, VAV air-cooled chiller with PFP boxes, VAV air-cooled chiller with district hot water reheat, and VAV air-cooled chiller with gas boiler reheat.

### Air-Cooled Chiller Rated Performance

ACCs are assigned full load and part load efficiencies based on the HVAC code template for the model and the capacity. These assignments are summarized in Table <a href="#tab:acc_efficiencies" data-reference-type="ref" data-reference="tab:acc_efficiencies">16</a>. These values mirror those found in ASHRAE-90.1 (or those used in the DOE reference buildings for the pre-1980 template).

<div id="tab:acc_efficiencies">

<table>
<caption>Air-Cooled Chiller Efficiency and Performance Curve Assignment</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Model Template</strong></th>
<th style="text-align: left;"><strong>Minimum Capacity (Tons)</strong></th>
<th style="text-align: left;"><strong>Maximum Capacity (Tons)</strong></th>
<th style="text-align: left;"><strong>Minimum Full Load Efficiency (kW/ton)</strong></th>
<th style="text-align: left;"><strong>Minimum Integrated Part Load Value (kW/ton)</strong></th>
<th style="text-align: left;"><strong>Capacity Function of Temperature (Schedule Name)</strong></th>
<th style="text-align: left;"><strong>EIR Function of Temperature (Schedule Name)</strong></th>
<th style="text-align: left;"><strong>EIR Function of PLR (Schedule Name)</strong></th>
<th style="text-align: left;"><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Pre-1980</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">1.303</td>
<td style="text-align: left;">-</td>
<td rowspan="4" style="text-align: left;">ChlrAir_RecipQRatio_fTchwsToadbSI</td>
<td rowspan="4" style="text-align: left;">ChlrAir_RecipEIRRatio_fTchwsToadbSI</td>
<td rowspan="4" style="text-align: left;">ChlrAir_RecipEIRRatio_fQRatio</td>
<td style="text-align: left;">From 90.1-1989</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> Pre-1980</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">1.332</td>
<td style="text-align: left;">-</td>
<td rowspan="3" style="text-align: left;">From DOE Reference Buildings</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> Pre-1980</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.332</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 1980-2004</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.407</td>
<td style="text-align: left;">1.407</td>
</tr>
<tr>
<td style="text-align: left;">90.1-2004</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.256</td>
<td style="text-align: left;">1.153</td>
<td rowspan="4" style="text-align: left;">AirCooled_Chiller_2010_PathA_CAPFT</td>
<td rowspan="4" style="text-align: left;">AirCooled_Chiller_2010_PathA_EIRFT</td>
<td rowspan="4" style="text-align: left;">AirCooled_Chiller_AllCapacities_2004_2010_EIRFPLR</td>
<td rowspan="4" style="text-align: left;">From 90.1-2004 Table 6.8.1A</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2007</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.29</td>
<td style="text-align: left;">1.164</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2010</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">1.255</td>
<td style="text-align: left;">0.941</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2010</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.255</td>
<td style="text-align: left;">0.941</td>
</tr>
<tr>
<td style="text-align: left;">90.1-2013</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">1.25</td>
<td style="text-align: left;">0.96</td>
<td rowspan="8" style="text-align: left;">ChlrAir_ScrollQRatio_fTchwsToadbSI</td>
<td rowspan="8" style="text-align: left;">ChlrAir_ScrollEIRRatio_fTchwsToadbSI</td>
<td rowspan="8" style="text-align: left;">ChlrAir_ScrollEIRRatio_fQRatio</td>
<td rowspan="8" style="text-align: left;">Path A Efficiencies</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2013</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.25</td>
<td style="text-align: left;">0.94</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2013</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">1.188</td>
<td style="text-align: left;">0.876</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2013</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.188</td>
<td style="text-align: left;">0.857</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2016</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">1.188</td>
<td style="text-align: left;">0.876</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2016</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.188</td>
<td style="text-align: left;">0.857</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2019</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">1.188</td>
<td style="text-align: left;">0.876</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2019</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.188</td>
<td style="text-align: left;">0.857</td>
</tr>
</tbody>
</table>

</div>

### Air-Cooled Chiller Performance Modifiers

ACCs vary in capacity and efficiency under different operating conditions. ComStock uses three curve types to model the variation in performance: capacity as a function of temperature (CAPFT) modifier, EIR as a function of temperature (EIRFT) modifier, and EIR as a function of part load ratio (EIRFPLR) modifier. For each time step, the EIR modifier function outputs are multiplied by the ACC’s rated EIR (except for the PLR curve output, which is divided). This provides the realized EIR for the time step. Similarly, the CAPFT modifier function output is multiplied by the ACC’s nominal capacity every time step to get the actual available capacity for that time step. The curve assignments are summarized in Table <a href="#tab:acc_efficiencies" data-reference-type="ref" data-reference="tab:acc_efficiencies">16</a>, and the curve parameters are specified in Table <a href="#tab:acc_perf_curves" data-reference-type="ref" data-reference="tab:acc_perf_curves">[tab:acc_perf_curves]</a>. The curves are also illustrated in Figure <a href="#fig:acc_eir_curves" data-reference-type="ref" data-reference="fig:acc_eir_curves">[fig:acc_eir_curves]</a>, Figure <a href="#fig:AirCooledChiller2010PathA_funct_curves" data-reference-type="ref" data-reference="fig:AirCooledChiller2010PathA_funct_curves">[fig:AirCooledChiller2010PathA_funct_curves]</a>, and Figure <a href="#fig:ChlrAirRecipQRatio_curves" data-reference-type="ref" data-reference="fig:ChlrAirRecipQRatio_curves">[fig:ChlrAirRecipQRatio_curves]</a>.

## Water-Cooled Chillers

Water-cooled chillers (WCCs) provide chilled water for building cooling systems and use a water-cooled condenser for heat rejection. Therefore, a condenser water loop is required for WCCs, generally conditioned by a boiler and cooling tower. The following ComStock HVAC types use WCCs: DOAS with fan coil chiller with baseboard electric, DOAS with fan coil chiller with boiler, DOAS with fan coil chiller with district hot water, DOAS with fan coil chiller with baseboard electric, VAV chiller with PFP boxes, VAV chiller with district hot water reheat, and VAV chiller with gas boiler reheat.

### Water-Cooled Chiller Rated Performance

WCCs are assigned full load and part load efficiencies based on the HVAC code template for the model and the capacity. These assignments are summarized in Table <a href="#tab:wcc_eff" data-reference-type="ref" data-reference="tab:wcc_eff">17</a>. These values mirror those found in ASHRAE-90.1 (or those used in the DOE reference buildings for the pre-1980 template).

<div id="tab:wcc_eff">

<table>
<caption>Water-Cooled Chiller Efficiency and Performance Curve Assignment</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Model Template</strong></th>
<th style="text-align: left;"><strong>Compressor Type</strong></th>
<th style="text-align: left;"><strong>Minimum Capacity (Tons)</strong></th>
<th style="text-align: left;"><strong>Maximum Capacity (Tons)</strong></th>
<th style="text-align: left;"><strong>Minimum Full Load Efficiency (kW/ton)</strong></th>
<th style="text-align: left;"><strong>Minimum Integrated Part Load Value (kW/ton)</strong></th>
<th style="text-align: left;"><strong>Capacity Function of Temperature (Schedule Name)</strong></th>
<th style="text-align: left;"><strong>EIR Function of Temperature (Schedule Name)</strong></th>
<th style="text-align: left;"><strong>EIR Function of PLR (Schedule Name)</strong></th>
<th style="text-align: left;"><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Pre-1980</td>
<td rowspan="32" style="text-align: left;">Rotary Screw</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.852</td>
<td style="text-align: left;">-</td>
<td rowspan="9" style="text-align: left;">ChlrWtrPosDispPathAAllQRatiofTchwsTcwsSI</td>
<td rowspan="9" style="text-align: left;">ChlrWtrPosDispPathAAllEIRRatio_fTchwsTcwsSI</td>
<td rowspan="32" style="text-align: left;">ChlrWtrPosDispPathAAllEIRRatio_fQRatio</td>
<td rowspan="3" style="text-align: left;">From DOE Reference Buildings</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Pre-1980</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.782</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Pre-1980</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.688</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 1980-2004</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.926</td>
<td style="text-align: left;">0.902</td>
<td rowspan="3" style="text-align: left;">From 90.1-1989</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 1980-2004</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.837</td>
<td style="text-align: left;">0.782</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 1980-2004</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.676</td>
<td style="text-align: left;">0.664</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2004</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.79</td>
<td style="text-align: left;">0.676</td>
<td rowspan="3" style="text-align: left;">Path A Efficiencies</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2004</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.718</td>
<td style="text-align: left;">0.628</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2004</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.639</td>
<td style="text-align: left;">0.572</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2007</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">74.99</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.63</td>
<td rowspan="8" style="text-align: left;">WaterCooled_PositiveDisplacement_Chiller_LT150_2010_PathA_CAPFT</td>
<td rowspan="8" style="text-align: left;">WaterCooled_PositiveDisplacement_Chiller_LT150_2010_PathA_EIRFT</td>
<td rowspan="8" style="text-align: left;">Path A Minimum Efficiencies</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2007</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.775</td>
<td style="text-align: left;">0.615</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2007</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.68</td>
<td style="text-align: left;">0.58</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2007</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.62</td>
<td style="text-align: left;">0.54</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2010</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">74.99</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.63</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2010</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.775</td>
<td style="text-align: left;">0.615</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2010</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.68</td>
<td style="text-align: left;">0.58</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2010</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.62</td>
<td style="text-align: left;">0.54</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2013</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">74.99</td>
<td style="text-align: left;">0.75</td>
<td style="text-align: left;">0.6</td>
<td rowspan="15" style="text-align: left;">ChlrWtrPosDispPathAAllQRatiofTchwsTcwsSI</td>
<td rowspan="15" style="text-align: left;">ChlrWtrPosDispPathAAllEIRRatiofTchwsTcwsSI</td>
<td rowspan="15" style="text-align: left;">Path A Efficiencies</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2013</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.72</td>
<td style="text-align: left;">0.56</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2013</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.66</td>
<td style="text-align: left;">0.54</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2013</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">599.99</td>
<td style="text-align: left;">0.61</td>
<td style="text-align: left;">0.52</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2013</td>
<td style="text-align: left;">600</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.56</td>
<td style="text-align: left;">0.5</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2016</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">74.99</td>
<td style="text-align: left;">0.75</td>
<td style="text-align: left;">0.6</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2016</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.72</td>
<td style="text-align: left;">0.56</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2016</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.66</td>
<td style="text-align: left;">0.54</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2016</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">599.99</td>
<td style="text-align: left;">0.61</td>
<td style="text-align: left;">0.52</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2016</td>
<td style="text-align: left;">600</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.56</td>
<td style="text-align: left;">0.5</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2019</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">74.99</td>
<td style="text-align: left;">0.75</td>
<td style="text-align: left;">0.6</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2019</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.72</td>
<td style="text-align: left;">0.56</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2019</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.66</td>
<td style="text-align: left;">0.54</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2019</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">599.99</td>
<td style="text-align: left;">0.61</td>
<td style="text-align: left;">0.52</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2019</td>
<td style="text-align: left;">600</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.56</td>
<td style="text-align: left;">0.5</td>
</tr>
</tbody>
</table>

</div>

### Water-Cooled Chiller Performance Modifiers

WCCs have been shown to vary capacity and efficiency at different operating conditions. ComStock uses three curve types to model the variation in performance: capacity as a function of temperature (CAPFT) modifier, EIR as a function of temperature (EIRFT) modifier, and EIR as a function of part load ratio (EIRFPLR) modifier. For each time step, the EIR modifier function outputs are multiplied by the WCC’s rated EIR (except for the PLR curve output, which is divided). This provides the realized EIR for the time step. Similarly, the CAPFT modifier function output is multiplied by the WCC’s nominal capacity every time step to get the actual available capacity for that time step. The curve assignments are summarized in Table<a href="#tab:wcc_eff" data-reference-type="ref" data-reference="tab:wcc_eff">17</a>, and the coefficients are shown in Table <a href="#tab:wcc_perf_curves" data-reference-type="ref" data-reference="tab:wcc_perf_curves">[tab:wcc_perf_curves]</a>. Furthermore, the performance curves are illustrated in Figure <a href="#fig:wcc_plr" data-reference-type="ref" data-reference="fig:wcc_plr">[fig:wcc_plr]</a> (EIRFPLR for all chillers), Figure<a href="#fig:wcc_WaterCooled_PositiveDisplacement_Chiller_LT150_2010_Modifiers" data-reference-type="ref" data-reference="fig:wcc_WaterCooled_PositiveDisplacement_Chiller_LT150_2010_Modifiers">[fig:wcc_WaterCooled_PositiveDisplacement_Chiller_LT150_2010_Modifiers]</a>, and Figure<a href="#fig:ChlrAirRecipQRatio_curves" data-reference-type="ref" data-reference="fig:ChlrAirRecipQRatio_curves">[fig:ChlrAirRecipQRatio_curves]</a>.

## Cooling Towers

Cooling towers are an HVAC component used to reject heat from a condenser water loop. The following ComStock HVAC system types use cooling towers: DOAS with fan coil chiller with baseboard electric, DOAS with fan coil chiller with boiler, DOAS with fan coil chiller with district hot water, DOAS with water source heat pumps cooling tower with boiler, VAV chiller with PFP boxes, VAV chiller with district hot water reheat, and VAV chiller with gas boiler reheat.

The cooling tower assumptions used in ComStock are primarily code-driven and are summarized in Table <a href="#tab:cooling_towers_table" data-reference-type="ref" data-reference="tab:cooling_towers_table">18</a>.

<div id="tab:cooling_towers_table">

<table>
<caption>Cooling Tower Efficiency</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Model Template</strong></th>
<th style="text-align: left;"><strong>Equipment Type</strong></th>
<th style="text-align: left;"><strong>Fan Type</strong></th>
<th style="text-align: left;"><strong>Fan Type</strong></th>
<th style="text-align: left;"><strong>Minimum Air Flow Rate Ratio</strong></th>
<th style="text-align: left;"><strong>Design Inlet Wet Bulb Temperature (°F)</strong></th>
<th style="text-align: left;"><strong>Design Entering Water Temperature (°F)</strong></th>
<th style="text-align: left;"><strong>Design Leaving Water Temperature (°F)</strong></th>
<th style="text-align: left;"><strong>Minimum Performance (gpm/hp)</strong></th>
<th style="text-align: left;"><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Pre-1980</td>
<td rowspan="8" style="text-align: left;">Open Cooling Tower</td>
<td rowspan="8" style="text-align: left;">Propeller or Axial</td>
<td rowspan="8" style="text-align: left;">VFD</td>
<td rowspan="8" style="text-align: left;">0.2</td>
<td rowspan="8" style="text-align: left;">76</td>
<td rowspan="8" style="text-align: left;">95</td>
<td rowspan="8" style="text-align: left;">85</td>
<td rowspan="5" style="text-align: left;">38.2</td>
<td style="text-align: left;">From 90.1-2004 Table 6.8.1G</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 1980-2004</td>
<td style="text-align: left;">From 90.1-2004 Table 6.8.1G</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2004</td>
<td style="text-align: left;">From 90.1-2004 Table 6.8.1G</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2007</td>
<td style="text-align: left;">From 90.1-2007 Table 6.8.1G</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2010</td>
<td style="text-align: left;">From 90.1-2010 Table 6.8.1 G</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2013</td>
<td rowspan="3" style="text-align: left;">40.2</td>
<td style="text-align: left;">From 90.1-2013 Table 6.8.1-7</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2016</td>
<td style="text-align: left;">From 90.1-2016 Table 6.8.1-7</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2019</td>
<td style="text-align: left;">From 90.1-2019 Table 6.8.1-7</td>
</tr>
</tbody>
</table>

</div>

## Water-Source Heat Pumps

Water-source heat pumps (WSHPs) are an HVAC system type that uses water-to-air heat pumps for space conditioning. These differ from ASHPs in that the condenser side of the heat pumps use water from a condenser water loop as the heat source/sink instead of air. The following ComStock HVAC system type(s) use WSHPs: DOAS with water source heat pumps cooling tower with boiler.

## Ground-Source Heat Pumps

Ground-source heat pumps (GSHPs) are WSHP systems that use the ground as the heat sink for the condenser water loop. The temperature of the ground is fairly constant throughout the year, which makes the ground an effective heat sink for the refrigeration cycle. The following ComStock HVAC system type uses GSHPs: DOAS with water source heat pumps with ground source heat pump.

The GSHP model in ComStock uses the “Plant Component Temperature Source” with energy management system (EMS) controls to represent the temperature behavior of the ground condenser water loop. The EMS predicts the exit temperature of the ground loop based on the inlet temperature of the loop, where the exit temperature will directly impact the efficiency and capacity of the heat pump system. A warmer exit temperature will generally be beneficial for heating, whereas a colder exit temperature will generally be beneficial for cooling. The exit temperature in ComStock is predicted by a linear interpolation that assumes a +12°F delta temperature at the lowest expected inlet loop temperature of 30°F (42°F loop exit temperature), and a -12°F delta temperature at the highest expected inlet loop temperature of 90°F (78°F loop exit temperature), while ramping linearly in between. The relationship between the inlet loop temperature and the outlet loop temperature is illustrated in Figure <a href="#fig:gshp_loop_temps" data-reference-type="ref" data-reference="fig:gshp_loop_temps">[fig:gshp_loop_temps]</a>. Note that there is no change in the loop temperature at 60°F, as this approach results in a constant ground temperature assumption of 60°F.

## Refrigeration

In ComStock, refrigeration systems refer to the refrigerated cases and walk-ins found in commercial kitchens, grocery stores, and other food service spaces. Small plug-in refrigerators are included in plug and process loads, as described in Section <a href="#sec:plug_and_process_loads" data-reference-type="ref" data-reference="sec:plug_and_process_loads">[sec:plug_and_process_loads]</a>. Refrigeration is modeled in building types where it is a major end use (primary and secondary schools, restaurants, hotels, hospitals, and grocery stores).

### Walk-ins and Case Scaling

Earlier versions of ComStock used fixed-size walk-in coolers and freezers for each building kitchen zone. This has been replaced with a scaling approach: refrigeration equipment is now sized according to the floor area of the associated space type (such as kitchens, stock rooms, or grocery sales areas). Rather than applying fixed case or walk-in sizes, ComStock uses reference space types to establish a ratio of refrigerated area or case length to total floor area. For example, a reference space type might assume 20,000 ft$`^2`$ of grocery sales area with 400 ft of refrigerated cases; this ratio of case type to floor area is then scaled to the actual space type floor area in the model. This scaling approach is consistent with the best available data sources and has been validated through in-person site visits performed by NREL staff, providing confidence that modeled refrigeration capacities align with real-world practice.

### Technology Level Assignment

Refrigeration systems are now characterized by probabilistic assignment of technology levels: *old*, *new*, and *advanced*. These levels represent distributions of baseline efficiency as a function of both building vintage and building size. Technology levels influence compressor efficiency, case lighting, fan motors, and defrost cycles. This approach allows ComStock to capture variability in stock performance, from legacy systems to modern ENERGY STAR<sup>®</sup>-like equipment (U.S. Department of Energy 2009; U.S. Environmental Protection Agency 2001).

The assignment of technology levels draws from three TSVs:

- *include_refrigeration_technology_level.tsv* flags buildings with refrigeration.

- *year_bin_of_last_refrigeration_replacement.tsv* assigns the year range of the last major equipment replacement, based on survival curves (see Section <a href="#sec:refrigeration_survival" data-reference-type="ref" data-reference="sec:refrigeration_survival">[sec:refrigeration_survival]</a>).

- *refrigeration_technology_level.tsv* probabilistically assigns equipment efficiency distributions based on year built, replacement year, and building size.

Figure <a href="#fig:refrigeration_tech_distribution" data-reference-type="ref" data-reference="fig:refrigeration_tech_distribution">17</a> illustrates the resulting distribution of refrigeration technology levels by building size and year of last replacement.

### Efficiency Distributions

Efficiency distributions for refrigeration equipment are derived from DOE Technical Support Documents, ENERGY STAR<sup>®</sup> archives, ASHRAE research, and utility/laboratory studies (U.S. Department of Energy 2009; Fricke and Becker 2010; California Energy Commission 2006). Historical data show a clear trend of improvement:

- Pre-1990 equipment had very high energy intensities (e.g., 0.3-0.4 kWh/ft$`^3`$/day for reach-in refrigerators, 2.5-3.0 kWh/ft/day for open vertical cases).

- 1990s equipment introduced modest improvements (better insulation, new refrigerants), but performance was still poor by modern standards.

- Early 2000s saw the introduction of ENERGY STAR<sup>®</sup> criteria and California Title 20 standards, driving significant efficiency gains in reach-ins, freezers, and merchandisers.

- By the late 2000s, most new commercial refrigeration equipment met or exceeded federal standards, with widespread adoption of LED case lighting, ECM fan motors, anti-sweat heater controls, and night covers.

These historical shipment distributions were mapped to *old*, *new*, and *advanced* efficiency levels using Oak Ridge National Laboratory (ORNL) performance data embedded in OpenStudio Standards. In practice, ComStock samples from these distributions to assign performance characteristics to each refrigeration system. Approximate efficiency values by technology level are summarized in Table <a href="#tab:refrigeration_efficiency_levels" data-reference-type="ref" data-reference="tab:refrigeration_efficiency_levels">19</a>. This ensures the resulting stock reflects both legacy equipment and the adoption of modern efficiency measures over time.

<div class="threeparttable">

<div id="tab:refrigeration_efficiency_levels">

| **Equipment Category** | **Old (Legacy / Pre-Standard)** | **New (Standard-Era Baseline)** | **Advanced (High Efficiency / ENERGY STAR)** |
|:---|:---|:---|:---|
| Reach-in Refrigerators (solid/glass door) | 0.30-0.40 kWh/ft$`^3`$/day | 0.20-0.30 kWh/ft$`^3`$/day | 0.15-0.20 kWh/ft$`^3`$/day |
| Reach-in Freezers | 0.50-0.60 kWh/ft$`^3`$/day | 0.40-0.50 kWh/ft$`^3`$/day | 0.30-0.40 kWh/ft$`^3`$/day |
| Vertical Open Display Cases (medium-temp) | 2.3-3.0 kWh/ft/day | 1.8-2.3 kWh/ft/day | 1.2-1.6 kWh/ft/day |
| Horizontal/Coffin Freezers (low-temp) | 2.0-2.5 kWh/ft/day | 1.5-2.0 kWh/ft/day | 1.0-1.4 kWh/ft/day |
| Walk-in Coolers (8$`\times`$<!-- -->8 typical) | 0.07-0.09 kWh/ft$`^3`$/day | 0.05-0.07 kWh/ft$`^3`$/day | 0.03-0.05 kWh/ft$`^3`$/day |
| Walk-in Freezers (8$`\times`$<!-- -->8 typical) | 0.14-0.18 kWh/ft$`^3`$/day | 0.11-0.14 kWh/ft$`^3`$/day | 0.08-0.11 kWh/ft$`^3`$/day |

Approximate efficiency levels for refrigeration equipment categories (illustrative ranges).

</div>

<div class="tablenotes">

Values represent typical daily energy use intensities under standard test conditions, used to define the “Old,” “New,” and “Advanced” technology levels applied in ComStock. Ranges are derived from DOE Technical Support Documents, ENERGY STAR<sup>®</sup> criteria, and ASHRAE/utility research studies, and mapped to OpenStudio Standards performance data.

</div>

</div>

### System Types and Controls

Refrigeration configurations also vary by building type and size. Large grocery stores almost universally use centralized compressor rack systems serving dozens of cases and walk-ins, while small-format stores rely on self-contained units (U.S. Energy Information Administration 2018b). Efficiency technologies such as floating head pressure control, variable-speed compressors, adaptive defrost, and LED case lighting are incorporated in proportion to their historical and present-day adoption levels. For example:

- Floating head pressure control was common by the late 1990s and is standard in modern racks.

- Variable-speed compressors and VFD-controlled condenser fans are now standard in new systems.

- Adaptive defrost and anti-sweat heater controls are widely adopted in newer or retrofitted equipment.

- Medium-temperature case doors, once rare, are now installed in roughly half of all modern supermarkets, reflecting a major retrofit trend.

### Summary

In summary, ComStock’s refrigeration modeling now:

- Scales walk-in and case sizes based on space type floor area, validated against site visits and data sources;

- Applies survival-based replacement schedules to reflect realistic equipment lifetimes (Section <a href="#sec:refrigeration_survival" data-reference-type="ref" data-reference="sec:refrigeration_survival">[sec:refrigeration_survival]</a>);

- Assigns technology levels probabilistically, capturing distributions of baseline efficiency by vintage and size, based on DOE shipment data mapped to OpenStudio Standards performance levels;

- Incorporates adoption of modern refrigeration efficiency measures and retrofit trends.

This methodology ensures that ComStock refrigeration energy use better reflects the diversity of U.S. commercial building stock, including both legacy equipment and advanced technologies.

<figure id="fig:refrigeration_tech_distribution">
<img src="figures/refrigeration_tech_distribution.png" style="width:90.0%" />
<figcaption>Distribution of refrigeration technology levels (old, new, advanced) by building size and year of last replacement. Based on DOE shipment data mapped to OpenStudio Standards performance levels.</figcaption>
</figure>

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-ashrae_62.1_2004" class="csl-entry">

ASHRAE. 2004. *Ventilation for Acceptable Indoor Air Quality*. <a href="https://ashrae.iwrapper.com/ASHRAE_PREVIEW_ONLY_STANDARDS/STD_62.1_2019" class="uri">Https://ashrae.iwrapper.com/ASHRAE_PREVIEW_ONLY_STANDARDS/STD_62.1_2019</a>.

</div>

<div id="ref-CEC_Title20" class="csl-entry">

California Energy Commission. 2006. *Appliance Efficiency Regulations (Title 20)*. California Energy Commission. <https://www.energy.ca.gov/rules-and-regulations/appliance-efficiency-regulations>.

</div>

<div id="ref-unocc_hvac_paper" class="csl-entry">

CaraDonna, Chris, and Kelsea Dombrovski. 2022. “Air Handling Unit Shutdowns During Scheduled Unoccupied Hours: US Commercial Building Stock Prevalence and Energy Impact.” *ASME Journal of Engineering for Sustainable Buildings and Cities* 3 (4). <https://doi.org/10.1115/1.4055887>.

</div>

<div id="ref-carrier_economiser" class="csl-entry">

Carrier. 2023. *Carrier Economizer*.

</div>

<div id="ref-osti_1889192" class="csl-entry">

Crowe, Eliot, Yimin Chen, Jessica Granderson, et al. 2022. “What We Learned from Analyzing 18 Million Rows of Commercial Buildings’ HVAC Fault Data.” *2022 Summer Study on Energy Efficiency in Buildings*, August. <https://www.osti.gov/biblio/1889192>.

</div>

<div id="ref-daikin_rebel" class="csl-entry">

Daikin. 2023. *Rebel Commercial Packaged Rooftop Systems*.

</div>

<div id="ref-osti_1457127" class="csl-entry">

Frank, Stephen M, Janghyun Kim, Jie Cai, and James E. Braun. 2018. *Common Faults and Their Prioritization in Small Commercial Buildings: February 2017 - December 2017*. National Renewable Energy Laboratory. <https://doi.org/10.2172/1457127>.

</div>

<div id="ref-Fricke2010" class="csl-entry">

Fricke, Brian, and B. Becker. 2010. “Energy Use of Doored and Open Vertical Refrigerated Display Cases.” *ASHRAE Journal*, 44-52.

</div>

<div id="ref-heinemeier2014free" class="csl-entry">

Heinemeier, Kristin. 2014. “Free Cooling: At What Cost?” *ACEEE Summer Study Energy Efficiency Build*.

</div>

<div id="ref-mascontrol3" class="csl-entry">

Hirsch, J. J. 2021. *MasControl 3*. <https://cedars.sound-data.com/deer-resources/tools/mas-control/>.

</div>

<div id="ref-osti_1829706" class="csl-entry">

Katipamula, Srinivas, Ronald M. Underhill, Nicholas EP Fernandez, Woohyun Kim, Robert G. Lutes, and Danny J. Taasevigen. 2021. “Prevalence of Typical Operational Problems and Energy Savings Opportunities in u.s. Commercial Buildings.” *Energy and Buildings* 253 (December). <https://doi.org/10.1016/j.enbuild.2021.111544>.

</div>

<div id="ref-doi_10_1080_23744731_2021_1898243" class="csl-entry">

Kim, Janghyun, Trenbath Kim, Jessica Granderson, et al. 2021. “Research Challenges and Directions in HVAC Fault Prevalence.” *Science and Technology for the Built Environment* 27 (5): 624-40. <https://doi.org/10.1080/23744731.2021.1898243>.

</div>

<div id="ref-seventhwave_rtu" class="csl-entry">

Seventhwave and Center for Energy and Environment. 2016. *Commercial Roof-Top Units in Minnesota: Characteristics and Energy Performance*. Minnesota Department of Commerce Division of Energy Resources. <https://slipstreaminc.org/research/commercial-roof-top-units-minnesota-characteristics-and-energy-performance>.

</div>

<div id="ref-osti_1665808" class="csl-entry">

Shoukas, Greg, Marcus Bianchi, and Michael Deru. 2020. *Analysis of Fault Data Collected from Automated Fault Detection and Diagnostic Products for Packaged Rooftop Units*. National Renewable Energy Laboratory. <https://doi.org/10.2172/1665808>.

</div>

<div id="ref-trane_foundation" class="csl-entry">

Trane. 2023. *Packaged Rooftop Air Conditioners Foundation*.

</div>

<div id="ref-DOE_TSD_2009" class="csl-entry">

U.S. Department of Energy. 2009. *Energy Conservation Standards for Refrigerated Beverage Vending Machines: Technical Support Document*. U.S. Department of Energy. <https://www.energy.gov/eere/buildings/appliance-and-equipment-standards-program>.

</div>

<div id="ref-eia2018cbecs" class="csl-entry">

U.S. Energy Information Administration. 2018a. *2018 Commercial Building Energy Consumption Survey (CBECS)*. Https://www.eia.gov/consumption/commercial/data/2018/.

</div>

<div id="ref-EIA_FoodSales2018" class="csl-entry">

U.S. Energy Information Administration. 2018b. *Commercial Buildings Energy Consumption Survey (CBECS): Food Sales*. U.S. Energy Information Administration. <https://www.eia.gov/consumption/commercial>.

</div>

<div id="ref-ENERGYSTAR_Refrigeration" class="csl-entry">

U.S. Environmental Protection Agency. 2001. *ENERGY STAR Program Requirements for Commercial Refrigerators and Freezers*. U.S. Environmental Protection Agency; U.S. Department of Energy. <https://www.energystar.gov>.

</div>

</div>
