<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86602.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86602.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86602.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/86602.md | section: 2.5 Rooftop Units | lines: 468-486 -->
## 2.5 Rooftop Units

The state of the existing RTUs in ComStock is based on a combination of when the buildings were built and how the equipment has been updated over time, described in detail in the 'ComStock Documentation' report by the National Renewable Energy Laboratory [3]. Equipment performance is assumed to meet the energy code requirements in force at the time and place of installation. For this reason, most of the existing RTUs are modeled as constant air volume with single-speed compressors. This is influential to the results in this analysis because energy savings will be calculated by comparing the energy performance of the ComStock baseline models to an updated version of the ComStock models that use the proposed HP-RTUs.

The in-force energy code for the ComStock baseline is shown as a percentage of applicable floor area in Figure 1. Applicable floor area for this analysis includes ComStock buildings with 'PSZAC with gas coil' and 'PSZ-AC with electric coil' HVAC system types (where PSZ-AC stands for packaged single-zone air conditioner). Most ComStock baseline RTUs follow energy code requirements from the early 2000s. Other energy efficiency features such as demand control ventilation, energy recovery, and economizer control are only applied to baseline ComStock RTUs if required by the in-force energy code for the particular model. The ComStock workflow checks the necessary characteristics of each RTU to determine if the feature is required. Similarly, heating, cooling, and fan efficiencies are set based on the in-force code year. For models with the 'PSZ-AC with electric coil' HVAC system type, the ComStock baseline will use electric resistance coils with a coefficient of performance (COP) of 1. For models with the

'PSZ-AC with gas coil' HVAC system type, the ComStock baseline will use a gas furnace efficiency of generally around 80%.

Figure 1. ComStock baseline in-force energy code followed as a percentage of applicable floor area. Applicable floor area includes ComStock buildings with 'PSZ-AC with gas coil' and 'PSZAC with electric coil' HVAC system types.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86602.yaml
     source: 86602_images/image_000005_316aa0fda323fd01d3a71d36b1079b91a8e91cb41194ac780efb9c2fa661ffc4.png
     method: vision-description
     described: 2026-08-21 -->

![Bar chart of percent of stock floor area served by applicable RTUs, by baseline in-force energy code](86602_images/image_000005_316aa0fda323fd01d3a71d36b1079b91a8e91cb41194ac780efb9c2fa661ffc4.png)

Figure 1: horizontal bar chart of the percent of stock floor area served by applicable RTUs, one row per baseline in-force energy code from ComStock DOE Ref Pre-1980 through DEER 2017, x-axis 0 to 50% with printed labels. DOE Ref 1980-2004 dominates at 46.50%, followed by 90.1-2007 at 19.52% and 90.1-2004 at 9.10%; every DEER row is 2.93% or less. Applicability covers PSZ-AC gas- and electric-coil systems only.

