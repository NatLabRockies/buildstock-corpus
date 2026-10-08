<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86103.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86103.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/86103.md | section: 3  ComStock Baseline Approach | lines: 347-367 -->
## 3  ComStock Baseline Approach

The state (e.g., type, efficiency, configuration) of the existing HVAC systems in ComStock is based on a combination of the year a building was built and how the equipment has been updated over time. Equipment performance is assumed to meet the energy code requirements at the time and location of installation. Other energy efficiency features such as demand control ventilation, energy recovery, and economizer control are only applied to baseline HVAC system if required by the energy code for the particular model. The ComStock workflow checks the necessary characteristics of each HVAC system to determine if a feature is required. Similarly, heating, cooling, and fan efficiencies are set based on the presiding code year.

Figure 5 shows the distribution of different HVAC system types in these baseline models. Packaged single zone (PSZ) units cover a large amount of floor area and consume a large amount of site energy. Variable air volume (VAV) systems, either packaged VAV (PVAV in Figure 5) or built-up VAV (VAV in Figure 5), are the next most prevalent system type in the building stock. More details around HVAC system distribution and modeling are included in the ComStock Reference Documentation [17].

Figure 5. Distribution of different HVAC system types in baseline models

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86103.yaml
     source: 86103_images/image_000011_b5bf994bf136d2bfe2015ff7cc2256ccc6a7952d7ce4b1f861e3044bf5611e0a.png
     method: vision-description
     described: 2026-08-22 -->

![Figure 5: baseline floor area and site energy by building type, stacked by HVAC system type](86103_images/image_000011_b5bf994bf136d2bfe2015ff7cc2256ccc6a7952d7ce4b1f861e3044bf5611e0a.png)

Figure 5: paired horizontal stacked bar charts of ComStock baseline floor area (% of total) and total site energy (TBtu) by building type, stacked by HVAC system type - PSZ-AC, PVAV, VAV, PTAC, PSZ-HP, PTHP, DOAS with VRF, DOAS with others, residential and other. PSZ and VAV systems dominate both measures while DOAS with VRF is a very small slice. A side panel lists the baseline VRF+DOAS assumptions. See Section 3.

As shown in Figure 5, VRF DOAS systems exist in a very small portion of the baseline models. As mentioned previously, the distribution of baseline buildings with VRF DOAS is based on the HVAC system type distribution estimated from CBECS 2012. Also, the specification and performance of the VRF DOAS in the baseline models reflect requirements based on the energy code in force during the most recent HVAC update. Some of these specifications are also highlighted in Figure 5.

One of the outcomes of this upgrade implementation is to determine reasonable buildings and HVAC systems that could be retrofitted with a VRF DOAS; therefore, understanding the distribution of potential HVAC systems is important. More details regarding the applicability criteria for the upgrade can be found in Section 4.1.

