<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/hvac_doas_mshp.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/hvac_doas_mshp.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/hvac_doas_mshp.html | corpus_version: 0a2f61f | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/hvac_doas_mshp.md | section: DOAS with Mini Split Heat Pumps | lines: 2-77 -->
# DOAS with Mini Split Heat Pumps

Authors: Chris CaraDonna and Andrew Parker

# Executive Summary

Building on the successfully completed effort to calibrate and validate the U.S. Department of Energy's ResStock™ and ComStock™ models over the past three years, the objective of this work is to produce national data sets that empower analysts working for federal, state, utility, city, and manufacturer stakeholders to answer a broad range of analysis questions.

The goal of this work is to develop energy efficiency and demand flexibility end-use load shapes (electricity, gas, propane, or fuel oil) that cover a majority of the high-impact, market-ready (or nearly market-ready) measures. "Measures" refers to energy efficiency variables that can be applied to buildings during modeling.

An *end-use savings shape* is the difference in energy consumption between a baseline building and a building with an energy efficiency or demand flexibility measure applied. It results in a timeseries profile that is broken down by end use and fuel (electricity or on-site gas, propane, or fuel oil use) at each timestep.

ComStock is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States. The baseline model intends to represent the U.S. commercial building stock as it existed in 2018. The methodology and results of the baseline model are discussed in the final technical report of the [End-Use Load Profiles](https://www.nlr.gov/buildings/end-use-load-profiles.html)
project.

This documentation focuses on a single end-use savings shape measure---dedicated outdoor air units with high-efficiency mini split heat pumps.

This measure replaces gas-fired and electric resistance rooftop units
(RTUs) in small commercial buildings (under 20,000 square feet) with high-efficiency (\~30 seasonal energy efficiency ratio; 14 heating seasonal performance factor), variable speed mini split heat pumps (MSHPs) and a dedicated outdoor air unit (DOAS) system with an energy recovery ventilator (ERV) or heat recovery ventilator (HRV). ERVs are used for drier climate zones, whereas HRVs are used for humid climate zones. The DOAS system uses the existing ductwork from the replaced RTU. This measure is applicable to 11% of the ComStock floor area.

The DOAS MSHP measure demonstrates 3.9% total site energy savings (169
TBtu) for the U.S. commercial building stock modeled in ComStock (Figure
10). The savings are primarily attributed to:

-   18% (81 TBtu) gas heating site energy savings

-   2% (6 TBtu) electricity heating site energy savings

-   6% (39 TBtu) electricity cooling site energy savings

-   8.7% (52 kBtu) fan electricity site energy savings.

# Acknowledgments

The authors would like to acknowledge the valuable guidance and input provided by Shanti Pless and the ComStock team, particularly Andrew Parker and Edwin Lee.

# 1.  Introduction

This documentation covers the "Dedicated Outdoor Air Unit (DOAS) With High-Efficiency Mini Split Heat Pump (MSHP)" upgrade methodology and briefly discusses key results. Results can be accessed on the ComStock™ data lake at "[end-use-load-profiles-for-us-building-stock](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F)" or via the Data Viewer at [comstock.nlr.gov.](https://comstock.nlr.gov/datasets)

| **Measure Title**      | DOAS With High-Efficiency Mini Split Heat Pump                                                                                                                                                                                                                                                                                                                         |
| **Measure Definition** | This measure replaces gas-fired and electric resistance rooftop units (RTUs) with high-efficiency (~30 seasonal energy efficiency ratio; 14 heating seasonal performance factor), variable speed MSHPs and a DOAS system with an energy recovery ventilator (ERV) or heat recovery ventilator (HRV). The DOAS system uses the existing ductwork from the replaced RTU. |
| **Applicability**      | Small commercial buildings (<20,000 square feet) that contain gas-fired or electric resistance RTUs.                                                                                                                                                                                                                                                                   |
| **Not Applicable**     | Buildings greater than 20,000 square feet or those that do not contain gas-fired or electric resistance RTUs. Also not applicable to kitchen spaces.                                                                                                                                                                                                                   |
| **Release**            | 2023 Release 1: 2023/comstock_amy2018_release_1/                                                                                                                                                                                                                                                                                                                       |

# 2.  Technology Summary

Small commercial buildings with rooftop units (RTUs) can achieve a relatively straightforward electrification pathway using MSHPs coupled with an energy recovery ventilator (ERV) or heat recovery ventilator (HRV) DOAS for outdoor air ventilation \[1\]. The DOAS is necessary to satisfy commercial building ASHRAE-62.1 outdoor air requirements and can be conveniently retrofitted to work with the existing ductwork from the existing RTU. The ERV or HRV feature on the DOAS can reduce the energy required to precondition the outdoor ventilation air before discharging it to the space. Meanwhile, the MSHPs can be added to throughout the building for space conditioning.

Some MSHPs on the market can achieve fairly high efficiencies, with seasonal energy efficiency ratios (SEERs) exceeding 30 and heating seasonal performance factors (HSPFs) exceeding 14 in some cases \[2\]. The higher SEER and HSPF values are often associated with premium units that include variable speed compressors and high-efficiency, multi-speed, electronically commuted motors. Some of these units are capable of operating at temperatures as low as −15°F, which can make them an attractive consideration for colder climates, and they often come equipped with integrated compressor defrost operation to avoid ice buildup on the outdoor unit \[2\]. Depending on the methodology used to size the MSHPs, the heating design temperature for the location, and the capacity maintenance of the specific MSHP for the heating design temperature, backup heating may be required. Ductless MSHPs do not always have a built-in backup heating system, so the backup heating may need to come in the form of a separate system, such as electric baseboard heating. MSHPs are common in residential applications due to their relatively small capacities, but they can be used in some smaller commercial applications as well \[1\]. Ductless MSHPs can often be retrofitted into buildings with minimal space implications due to their lack of need for ductwork.

Commercial buildings generally require outdoor air ventilation when the building is occupied \[3\]. DOASs use dedicated equipment to provide the required ventilation air to the spaces throughout a building, and they are available for a wide range of airflow sizes \[1\]. This air will generally be preconditioned to avoid discharging air that is too humid or of an uncomfortable temperature directly to spaces, regardless of whether or not the spaces have other heating, ventilating, and air conditioning (HVAC) systems for space conditioning \[1\]. ERVs or HRVs can be used to precondition the outdoor ventilation air with the building's exhaust air via a heat exchanger. HRVs generally provide sensible energy recovery, often through a plate and frame heat exchanger, whereas ERVs can provide both sensible and latent heat exchange, often through an enthalpy wheel. Because ERVs offer latent energy exchange, they can be more attractive in humid locations where users may be looking to dehumidify the incoming outdoor air. The Northwest Energy Efficiency Alliance (NEEA) defines a classification of "Very High Efficiency DOAS," which includes a minimum sensible effectiveness requirement for the heat exchanger systems of 82% \[1\]. Lastly, some climates may require additional heating or cooling in the DOAS beyond what the ERV or HRV can provide to ensure adequate temperature and humidity of the discharged air \[1\]. Areas with high humidity may need additional cooling to ensure proper humidity of the air discharged to spaces, whereas areas with very cold temperatures may require a heating element to ensure sufficient temperature \[1\].

This study offers an alternative pathway to electrification beyond replacing existing RTUs with a heat pump RTU. Either pathway can be realistic for many buildings, and the choice may come down to product availability, technology preferences, cost, and building-specific constraints.

# 3.  ComStock Baseline Approach

The ComStock baseline includes the distribution of HVAC systems shown in Figure 1. The DOAS-MSHP measure is applicable to the ComStock "PSZ-AC with gas coil" (where PSZ-AC stands for packaged single-zone air conditioner) and "PSZ-AC with electric coil" system types, which compose \~45% of the ComStock baseline by floor area. The ComStock baseline HVAC system distributions were derived using Commercial Buildings Energy Consumption Survey (CBECS) 2012 microdata \[4\] coupled with county-level fuel-type distribution data from ResStock™. This methodology is discussed in depth in the ComStock documentation \[5\]. Because the DOAS-MSHP measure is primarily intended for small commercial buildings, only ComStock models under 20,000 square feet will be applicable.

![Graphical user interface, application, table Description automatically generated](./media/14116cd5-ae4c-4abe-9b1b-04be8ac4c705.png)

Figure 1. ComStock HVAC system prevalence by percentage of total floor area

The state of the ComStock baseline model will serve as the point of comparison for calculating stock energy savings and therefore will influence the results of this analysis. The ComStock documentation discusses the baseline methodology in detail \[5\], but this report summarizes a few key points.

The ComStock baseline RTU performance is determined for each RTU based on the build year for a building model coupled with how the equipment has been updated over time. The energy performance is set based on the energy code in force at the time and location of the last HVAC retrofit for the building. For this reason, most RTUs in the ComStock baseline are modeled as constant air volume systems with single-speed compressors. The energy codes in force for the applicable ComStock baseline models with RTUs are shown as a percentage of floor area in Figure 2. These in-force energy codes are used to determine key parameters such as efficiencies, fan power, and energy efficiency features (demand control ventilation, economizers, energy recovery, etc.).

![Graphical user interface, application, table, Excel Description automatically generated](./media/fde6237b-0bc8-45c0-b8cc-9dcf87d266a1.png)

Figure 2. ComStock baseline energy code year followed as a function of percent floor area for applicable RTUs

# 4.  Modeling Approach

This measure replaces existing gas-fired or electric RTUs in the ComStock baseline with a DOAS MSHP system. All operating schedules from the baseline systems are transferred to the new systems, as this measure preserves hours of operation. Design outdoor airflow rates and schedules are also maintained. The existing RTU is converted to a DOAS, modified to supply only conditioned constant volume outdoor ventilation air and to have an ERV. The MSHPs are added to each applicable thermal zone. The MSHPs are modeled as four-stage multi-speed objects with performance curves based on lab test data from MSHPs. The units are modeled with very high performance and are intended to represent variable speed MSHPs with \>30 SEER and \>13 HSPF. The MSHPs are decoupled from the DOAS system and therefore operate using a cycling control scheme where they only turn on to maintain zone thermostat set points. The DOAS operates continuously with design ventilation air and follows the same schedule as the replaced baseline RTUs. Note that the economizer and demand control ventilation functionality that may be prevalent in the baseline models are not transferred to the DOAS system.

