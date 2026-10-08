<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89128.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89128.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89128.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/89128.md | section: 2.3 Economizers | lines: 398-427 -->
## 2.3 Economizers

ComStock baseline building models include HVAC systems with or without economizers, and configurations (e.g., control type and high limit) of economizers vary depending on different building parameters (e.g., climate zone). These decisions related to economizer configurations are determined by the requirements of the energy code that was in force when the HVAC system was last updated.

Figure 2 shows the prevalence of economizers (in terms of floor area coverage and contribution to cooling energy) for different subcategories (building type and ventilation system type) of the existing building stock. To note, the percentage of floor area shown as true for the 'economizer availability' represents the total building area if there is at least one economizer available in the building; thus, it does not mean the actual floor area coverage by the economizers. While there are buildings that already include economizers in variable air volume (VAV) systems and roof top units (RTU) covering 40% of the total floor area and 28% of total electricity used for cooling, the remaining portion of buildings for those system types does not leverage economizers in the baseline. HVAC system types such as packaged terminal units, dedicated outdoor air systems (DOAS), or residential systems without ventilation are not the target of this upgrade. More detailed information of the upgrade applicability is described in Section 3.3.2.

Figure 2. Contribution of ventilation system types on energy

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89128.yaml
     source: 89128_images/image_000008_e37227dcba9a955501f57e8a1b56c57865e8b0b12f2f5a710a4128d96c74e310.png
     method: vision-description
     described: 2026-08-21 -->

![Two-panel bar chart of economizer availability by building type and ventilation system type](89128_images/image_000008_e37227dcba9a955501f57e8a1b56c57865e8b0b12f2f5a710a4128d96c74e310.png)

Figure 2: two side-by-side bar panels grouped by building type and then ventilation system type - percent of total floor area on the left, electricity used for cooling in TBtu on the right - with orange marking economizer availability true and gray false. The central multi-zone VAV RTU and central single-zone RTU rows carry most of the orange; zone terminal, DOAS and residential rows almost none. Section 2.3 quantifies the coverage.

Figure 3 shows the comparison of economizer coverage with respect to building floor area between ComStock and estimation from Commercial Buildings Energy Consumption Survey [3]. Again, because of how data are structured in CBECS, the floor area coverage shown in these figures is representing the entire floor area of the building if any economizer is present in any of the HVAC systems in the building, rather than actual floor area coverage by HVAC systems with economizers. Because CBECS data only shows total building area instead of total area covered by the economizers, this comparison is mostly to understand the ballpark estimation of economizers.

Figure 3. Economizer floor area coverage between ComStock and CBECS 2018

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89128.yaml
     source: 89128_images/image_000009_255ee20822a7c111e639786023809199c7e30d2ea0fbceb59ed92834578e7ba3.png
     method: vision-description
     described: 2026-08-21 -->

![Two stacked bar panels comparing economizer floor area coverage in ComStock and CBECS 2018](89128_images/image_000009_255ee20822a7c111e639786023809199c7e30d2ea0fbceb59ed92834578e7ba3.png)

Figure 3: two stacked bar panels of percent of floor area by building type - panel (a) coverage in ComStock, panel (b) coverage in CBECS 2018 - with yes and no segments labeled in place and CBECS adding a null category. Hospital and LargeHotel show the highest yes shares in both sources. Section 2.3 cautions that both counts are whole-building area.

