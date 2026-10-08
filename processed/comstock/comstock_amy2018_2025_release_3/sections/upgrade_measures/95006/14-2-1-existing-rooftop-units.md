<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95006.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95006.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95006.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/95006.md | section: 2.1  Existing Rooftop Units | lines: 289-307 -->
## 2.1  Existing Rooftop Units

The state of the existing RTUs in ComStock is based on a combination of when the buildings were built and how the equipment has been updated over time, which is described in detail in the ComStock Reference Documentation: Version 1 report by the National Renewable Energy Laboratory [2]. Equipment performance is assumed to meet the energy code requirements in force at the time and place of installation. For this reason, most of the existing RTUs are modeled as constant air volume with single-speed compressors. This assumption is influential to the results in this analysis because energy savings will be calculated by comparing the energy performance of the ComStock baseline models to an updated version of the ComStock models that use the proposed HP-RTUs.

The in-force energy code for the ComStock baseline is shown as a percentage of applicable floor area in Figure 1. Applicable floor area for this analysis includes ComStock buildings with 'PSZAC with gas coil' and 'PSZ-AC with electric coil' HVAC system types (where PSZ-AC stands for packaged single-zone air conditioner). Most ComStock baseline RTUs follow energy code requirements from the early 2000s. Other energy efficiency features such as demand control ventilation, energy recovery, and economizer control are only applied to baseline ComStock RTUs if required by the in-force energy code for the particular model. The ComStock workflow checks the necessary characteristics of each RTU to determine if the feature is required. Similarly, heating, cooling, and fan efficiencies are set based on the in-force code year. For models with the 'PSZ-AC with electric coil' HVAC system type, the ComStock baseline will use electric resistance coils with a COP of 1. For models with the 'PSZ-AC with gas coil' HVAC system type, the ComStock baseline will use a gas furnace efficiency of generally around 80%.

Figure 1. Percentage of ComStock floor area by HVAC energy code followed during last HVAC replacement.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/95006.yaml
     source: 95006_images/image_000002_62b53b34a76777ce2c0efcb371eadb12e04a97989fc714ca357f7b48a9953b37.png
     method: vision-description
     described: 2026-08-20 -->

![Horizontal bar chart of percentage of ComStock floor area by HVAC energy code followed during last HVAC replacement](95006_images/image_000002_62b53b34a76777ce2c0efcb371eadb12e04a97989fc714ca357f7b48a9953b37.png)

Figure 1. Horizontal bar chart of the percentage of ComStock stock floor area by the HVAC energy code followed during the last HVAC replacement, x-axis % of Stock Floor Area 0% to about 46%. Bars from top: ComStock DOE Ref Pre-1980 0%, DOE Ref 1980-2004 46% (by far the largest), 90.1-2004 9%, 90.1-2007 19%, 90.1-2010 6%, 90.1-2013 5%, DEER Pre-1975 0%, DEER 1985 1%, DEER 1996 3%, DEER 2003 3%, DEER 2007 3%, DEER 2011 2%, DEER 2014 1%, DEER 2015 2%, and DEER 2017 1%. Shows most stock floor area follows older DOE Reference 1980-2004 or 90.1-2007 vintages.

Applicable floor area includes ComStock buildings with 'PSZ-AC with gas coil' and 'PSZ-AC with electric coil' HVAC system types. DEER stands for Database for Energy Efficiency Resources, which represents building characteristics for California models following Title 24.

