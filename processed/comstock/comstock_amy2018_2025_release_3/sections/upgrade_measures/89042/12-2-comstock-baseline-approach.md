<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89042.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/89042.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/89042.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/89042.md | section: 2  ComStock Baseline Approach | lines: 283-301 -->
## 2  ComStock Baseline Approach

The characteristics of existing RTUs in ComStock, the U.S. Department of Energy's commercial building stock model, are based on a combination of when the buildings were built and how the HVAC equipment has been assumed to have been updated over time. This is described in detail in the ComStock Documentation report [2]. HVAC equipment performance is assumed to meet the energy code requirements in force at the time and place of installation. For this reason, most of the existing RTUs are modeled as constant air volume with single-speed compressors with either gas or electric resistance backup heating.

The in-force energy code for the ComStock baseline is shown as a percentage of applicable floor area in Figure 1. Applicable floor area for this analysis includes ComStock buildings with 'PSZAC with gas coil' and 'PSZ-AC with electric coil' HVAC system types (where PSZ-AC stands for packaged single-zone air conditioner). Most ComStock baseline RTUs follow energy code requirements from the early 2000s. Other energy efficiency features, such as demand control ventilation, energy recovery, and economizer control, are only applied to baseline ComStock RTUs if required by the in-force energy code. The ComStock workflow checks the necessary characteristics of each RTU to determine whether the feature is required. Similarly, heating, cooling, and fan efficiencies are set based on the in-force code year. For models with the 'PSZAC with electric coil' HVAC system type, the ComStock baseline will use electric resistance coils that have an efficiency of 1. For models with the 'PSZ-AC with gas coil' HVAC system type, the ComStock baseline will generally use a gas furnace efficiency of around 80%.

Figure 1. ComStock baseline in-force energy code followed as a percentage of applicable floor area

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89042.yaml
     source: 89042_images/image_000002_411673573e02b632281ba7e6317f0a36d8a1b173d4da1e5efcc6eaf703414291.png
     method: vision-description
     described: 2026-08-22 -->

![Bar chart of ComStock baseline in-force energy code by percent of applicable stock floor area](89042_images/image_000002_411673573e02b632281ba7e6317f0a36d8a1b173d4da1e5efcc6eaf703414291.png)

Figure 1: horizontal bar chart of the ComStock baseline in-force energy code, x-axis percent of stock floor area from 0 to 50 percent, one bar per DOE Reference and DEER vintage. DOE Ref 1980-2004 dominates at 47.57 percent, followed by 90.1-2007 at 19.67 percent and 90.1-2004 at 9.18 percent; every DEER vintage sits below 2.3 percent. Section 2 explains the code mapping.

Applicable floor area includes ComStock buildings with 'PSZ-AC with gas coil' and 'PSZ-AC with electric coil' HVAC system types. DEER stands for Database for Energy Efficiency Resources, which represents building characteristics for California models following Title 24.

