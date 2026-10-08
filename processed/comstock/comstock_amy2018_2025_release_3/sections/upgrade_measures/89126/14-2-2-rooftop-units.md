<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89126.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/89126.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/89126.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/89126.md | section: 2.2 Rooftop Units | lines: 283-301 -->
## 2.2 Rooftop Units

The state of the existing RTUs in ComStock is based on a combination of when the buildings were built and how the equipment has been updated over time, described in detail in the ComStock Reference Documentation report by the National Renewable Energy Laboratory [2]. Equipment performance is assumed to meet the energy code requirements in force at the time and place of installation. For this reason, most of the existing RTUs are modeled as constant air volume with single-speed compressors. This is influential to the results in this analysis because energy savings will be calculated by comparing the energy performance of the ComStock baseline models to an updated version of the ComStock models that use the proposed HP-RTUs.

The in-force energy code for the ComStock baseline is shown as a percentage of applicable floor area in Figure 1. Applicable floor area for this analysis includes ComStock buildings with 'PSZAC with gas coil' and 'PSZ-AC with electric coil' HVAC system types (where PSZ-AC stands for packaged single-zone air conditioner). Most ComStock baseline RTUs follow energy code requirements from the early 2000s. Other energy efficiency features such as demand control ventilation, energy recovery, and economizer control are only applied to baseline ComStock RTUs if required by the in-force energy code for the model. The ComStock workflow checks the necessary characteristics of each RTU to determine whether the feature is required. Similarly, heating, cooling, and fan efficiencies are set based on the in-force code year. For models with the 'PSZ-AC with electric coil' HVAC system type, the ComStock baseline will use electric resistance coils with a coefficient of performance (COP) of 1. For models with the 'PSZ-AC with gas coil' HVAC system type, the ComStock baseline will use a gas furnace efficiency of generally around 80%.

Figure 1. ComStock baseline in-force energy code followed as a percentage of applicable floor area

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89126.yaml
     source: 89126_images/image_000002_1245f7ee4ca34ab09ef9ec75a8aa3ccf27c534dc168902fdfb9f647b1a8314f5.png
     method: vision-description
     described: 2026-08-20 -->

![Horizontal bar chart of ComStock baseline in-force energy code followed as a percent of applicable floor area](89126_images/image_000002_1245f7ee4ca34ab09ef9ec75a8aa3ccf27c534dc168902fdfb9f647b1a8314f5.png)

Figure 1. Horizontal bar chart of the ComStock baseline in-force energy code, as a percent of applicable floor area served by applicable RTUs, x-axis 0 to about 50%. Bars by code vintage: ComStock DOE Ref Pre-1980 0.07%, DOE Ref 1980-2004 46.50% (by far the largest), 90.1-2004 9.10%, 90.1-2007 19.52%, 90.1-2010 5.85%, 90.1-2013 4.28%, DEER Pre-1975 0.07%, DEER 1985 0.86%, DEER 1996 2.38%, DEER 2003 2.66%, DEER 2007 2.93%, DEER 2011 2.14%, DEER 2014 0.75%, DEER 2015 1.52%, and DEER 2017 1.38%. Shows the applicable stock is dominated by older DOE Reference 1980-2004 and 90.1-2007 vintage construction.

Applicable floor area includes ComStock buildings with 'PSZ-AC with gas coil' and 'PSZ-AC with electric coil' HVAC system types.

