<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89481.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89481.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89481.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/89481.md | section: 2  ComStock Baseline Approach | lines: 252-318 -->
## 2  ComStock Baseline Approach

There are a few features of the ComStock baseline that are especially impactful to this study. First is the prevalence of HVAC system types in the ComStock baseline that are applicable to the HP-RTU with energy recovery retrofit. This determines which and how many models the retrofit scenario is applied to, which impacts the magnitude of stock impact. The HVAC system type distributions used in ComStock are derived from CBECS 2012 microdata [1], and vary by census region and building type [15]. System type applicability is discussed further in Section 3.1.

The state of the existing RTUs in ComStock is another impactful feature that will determine the performance of the HVAC systems being replaced, which will drive the relative savings of implementing the HP-RTU with energy recovery upgrade scenario. The state of the existing RTUs in ComStock is based on a combination of when the buildings were built and how the equipment has been updated over time. This is described in detail in the ComStock Documentation report by the National Renewable Energy Laboratory (NREL) [15]. Equipment performance is assumed to meet the energy code requirements in force at the time and place of installation. For this reason, most of the existing RTUs are modeled as constant air volume with single-speed compressors. This impacts the results in this analysis because energy savings are calculated by comparing the energy performance of the ComStock baseline models to an updated version of the ComStock baseline that uses the proposed HP-RTUs.

The outdoor airflow rate of an RTU can impact energy usage considerably since outdoor ventilation air needs to be properly conditioned before being discharged into the building. Outdoor air rates also influence the impact of heat/energy recovery systems since the goal is to reduce ventilation loads. Buildings with higher outdoor airflow rates have higher potential for energy savings through heat/energy recovery systems. Distributions of building average annual outdoor air fraction and design outdoor airflow rates from ComStock are shown in Figure 2, by building type. Design outdoor airflow rates in ComStock align to the governing energy code standard for each model [15]. Outdoor air fractions are a function of the outdoor airflow rate and supply airflow rate. Large variations are shown by building type due to differences among these factors.

Figure 2 . Average annual outdoor air fraction (left) and design outdoor airflow rate (right) by ComStock building type for buildings served by RTUs

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89481.yaml
     source: 89481_images/image_000003_d81eb68cacb1e88a3eb4e10eae409d5a7f8f6fdefc56df6a27ceddc81d765ee5.png
     method: vision-description
     described: 2026-08-20 -->

![Paired box-and-whisker charts of average annual outdoor air fraction and design outdoor airflow rate by ComStock building type for RTU-served buildings](89481_images/image_000003_d81eb68cacb1e88a3eb4e10eae409d5a7f8f6fdefc56df6a27ceddc81d765ee5.png)

Figure 2 shows distributions of two ventilation characteristics for ComStock buildings served by rooftop units, broken out by building type as box-and-whisker plots. The left panel plots average annual outdoor air fraction on a 0.0 to 1.0 axis; the right panel plots design outdoor airflow rate in m3/s per m2 on a 0 to about 0.005 axis. Building types listed top to bottom are FullServiceRestaurant, QuickServiceRestaurant, SecondarySchool, PrimarySchool, RetailStripmall, RetailStandalone, Hospital, Outpatient, MediumOffice, LargeOffice, SmallOffice, and Warehouse. The two restaurant types sit farthest to the right in both panels, with the highest and widest outdoor air fractions and the largest design outdoor airflow rates; the two school types are next. Offices and Warehouse cluster at the low end, Warehouse showing the smallest values of any type. The wide variation by building type reflects differences in design outdoor airflow rate and supply airflow rate; design outdoor airflow rates in ComStock follow the governing energy code for each model, and annual outdoor air fractions are additionally affected by economizer operation. Because heat and energy recovery works by reducing ventilation loads, building types with higher outdoor airflow rates have the highest savings potential from this measure.

Note that annual outdoor air fractions will be impacted by economizer operation, where applicable.

The governing energy code for the ComStock baseline is shown as a percentage of applicable floor area in Figure 3. Applicable floor area for this analysis includes ComStock buildings with 'PSZ-AC with gas coil' and 'PSZ-AC with electric coil' HVAC system types (where PSZ-AC stands for packaged single-zone air conditioner). Most ComStock baseline RTUs follow energy code requirements from the early 2000s. Other energy efficiency features, such as demand control ventilation, energy recovery, and economizer control, are only applied to baseline ComStock RTUs if required by the in-force energy code for the particular model. The ComStock workflow checks the necessary characteristics of each RTU to determine whether the feature is required. Similarly, heating, cooling, and fan efficiencies are set based on the in-force code year. For models with the 'PSZ-AC with electric coil' HVAC system type, the ComStock baseline will use electric resistance coils with a coefficient of performance (COP) of 1. For models with the 'PSZ-AC with gas coil' HVAC system type, the ComStock baseline will generally use a gas furnace efficiency of around 80%.

Figure 3. ComStock baseline in-force energy code followed as a percentage of applicable floor area. Applicable floor area includes ComStock buildings with 'PSZ-AC with gas coil' and 'PSZAC with electric coil' HVAC system types.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89481.yaml
     source: 89481_images/image_000004_e4c9d74ea3a06f588c7a64258b1a5eebda0fe4565b60616f4191e9e6b36ae035.png
     method: vision-description
     described: 2026-08-20 -->

![Horizontal bar chart of ComStock baseline in-force energy code as a percentage of applicable RTU-served stock floor area, from DOE Ref Pre-1980 through DEER 2017](89481_images/image_000004_e4c9d74ea3a06f588c7a64258b1a5eebda0fe4565b60616f4191e9e6b36ae035.png)

Figure 3 gives the in-force energy code followed by ComStock baseline models as a percent of applicable floor area, where applicable floor area covers buildings with 'PSZ-AC with gas coil' and 'PSZ-AC with electric coil' HVAC system types. The x-axis reads '% of Stock Floor Area Served by Applicable RTUs' and runs 0% to 50%. Fifteen labeled bars, top to bottom: ComStock DOE Ref Pre-1980 0.07%, DOE Ref 1980-2004 46.50%, 90.1-2004 9.10%, 90.1-2007 19.52%, 90.1-2010 5.85%, 90.1-2013 4.28%, DEER Pre-1975 0.07%, DEER 1985 0.86%, DEER 1996 2.38%, DEER 2003 2.66%, DEER 2007 2.93%, DEER 2011 2.14%, DEER 2014 0.75%, DEER 2015 1.52%, and DEER 2017 1.38%. These sum to 100.01%, so the values are shares of the applicable RTU stock rather than of total ComStock floor area. Most applicable baseline RTUs therefore follow energy code requirements from the early 2000s or earlier, which is why they are modeled as constant air volume with single-speed compressors, using gas furnace efficiency near 80% or electric resistance coils at COP 1. DEER denotes the Database for Energy Efficiency Resources, representing California models following Title 24.

DEER stands for Database for Energy Efficiency Resources which represents building characteristics for California models following Title 24.

The ComStock baseline includes energy recovery in RTUs only when required by the governing energy code standard, which will impact the stock savings impact of including energy recovery with the new HP-RTUs. Replacing an existing RTU that already includes energy recovery may not show as high of relative energy savings versus replacing an existing RTU that does not have energy recovery. More information about the ComStock baseline heat/energy recovery systems can be found in the ComStock Documentation [15].

Lastly, the benefits of heat/energy recovery systems depend on routing exhaust air through the heat exchanger. As discussed, some amount of the exhaust air in buildings may not be routed back to the central exhaust or heat exchanger, either due to duct leakage or separate exhaust fans. ComStock includes exhaust fans in some space types, summarized in Table 1. Note that some prominent building types, such as small/medium/large office, warehouse, and retail, do not currently include any zone exhaust, so all exhaust air is assumed to return to the AHUs and become available for heat/energy recovery benefits, when applicable. Furthermore, ComStock models do not currently include duct leakage. These factors may overestimate the amount of exhaust air available for heat/energy recovery in ComStock models.

Table 1. Building and Space Types in ComStock Modeled With Zone Exhaust Fans

| Building Type            | Space Type                        |
|--------------------------|-----------------------------------|
| Full-Service Restaurant  | Kitchen                           |
| Hospital                 | Kitchen                           |
| Large Hotel              | Kitchen                           |
| Outpatient               | Anesthesia                        |
| Outpatient               | MRI                               |
| Outpatient               | MRI Control                       |
| Outpatient               | Soil Work                         |
| Outpatient               | Toilet                            |
| Primary School           | Restroom                          |
| Primary School           | Kitchen                           |
| Primary School           | Kitchen                           |
| Quick-Service Restaurant | Kitchen                           |
| Secondary School         | Restroom                          |
| Secondary School         | Kitchen                           |
| Small Hotel              | Public Restroom                   |
| No Zone Exhaust Fans     | No Zone Exhaust Fans              |
| Retail                   | None                              |
| Retail Strip Mall        | None (except those with kitchens) |
| Small Office             | None                              |
| Medium Office            | None                              |
| Large Office             | None                              |
| Warehouse                | None                              |

