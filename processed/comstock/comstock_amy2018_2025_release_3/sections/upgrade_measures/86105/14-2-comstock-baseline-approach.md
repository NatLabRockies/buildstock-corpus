<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86105.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86105.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86105.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/86105.md | section: 2  ComStock Baseline Approach | lines: 197-230 -->
## 2  ComStock Baseline Approach

ComStock baseline building models include HVAC systems with or without economizers, and configurations  (e.g.,  control  type  and  high  limit)  of  economizers  vary  depending  on  different building parameters (e.g., climate zone). These decisions related to economizer configurations are determined by the requirements of the energy code that was in force when the HVAC system was last updated.

Figure 2 shows the prevalence of economizers (in terms of floor area coverage and contribution to cooling  energy)  for  different  subcategories  (building  type  and  ventilation  system  type)  of  the existing building stock. To note, the percentage of floor area shown as True for the 'economizer availability' represents the total building area if there is at least one economizer available in the building, thus it does not mean the actual floor area coverage by the economizers. While there are buildings that already include economizers in variable air volume (VAV) systems and rooftop units (RTU) covering 40% of the total floor area and 28% of total electricity used for cooling, the remaining portion of buildings for those system types does not leverage economizers at all in the baseline models. HVAC system types such as packaged terminal units and residential systems without ventilation and dedicated outdoor air systems (DOAS) are not the target of this upgrade. More detailed information on the upgrade applicability is described in Section 4.1.

Figure 2. Contribution of ventilation system types on energy

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86105.yaml
     source: 86105_images/image_000008_be1da3dc6635f353bf7febae838270b114506eba031a77c30c0c462a3e8ab1f6.png
     method: vision-description
     described: 2026-08-21 -->

![Two-panel horizontal stacked bar chart of economizer prevalence in the ComStock baseline, showing percent of total floor area and electricity used for cooling in TBtu, split into with-economizer and without-economizer shares for thirteen combinations of building category and ventilation system type.](86105_images/image_000008_be1da3dc6635f353bf7febae838270b114506eba031a77c30c0c462a3e8ab1f6.png)

Figure 2 (Section 2, ComStock Baseline Approach) shows how economizers are distributed across the ComStock baseline. Two panels share a row axis: the left panel is "% of total floor area" on a 0-100% scale, the right is "Electricity used for cooling [TBtu]" on a 0-100 scale. The legend "Economizer availability" distinguishes a dark "without economizer" segment from a light "with economizer" segment. Rows are building category crossed with ventilation system type: Mercantile, Office, Education, Healthcare, Food Service and Warehouse and Storage each appear twice (Central Multi-zone VAV RTU and Central Single-zone RTU), and Lodging appears once (Central Single-zone RTU), for thirteen rows. Note that each floor-area bar sums to 100% within its own row, so the panel shows the economizer share of each segment, not each segment's share of the stock. Multi-zone VAV rows generally show a larger with-economizer share than their single-zone counterparts, and Lodging shows the smallest. No values are printed on either panel; the body text gives the aggregate as VAV and RTU buildings that already have economizers covering 40% of total floor area and 28% of total electricity used for cooling.

Figure 3 shows the comparison of economizer coverage with respect to building floor area between ComStock and estimation from the Commercial Buildings Energy Consumption Survey (CBECS, 2018). Again, because of how data is structured in CBECS, the floor area coverage shown in these figures is representing the entire floor area of the building if any economizer is present in any of the HVAC systems in the building rather than actual floor area coverage by HVAC systems with economizers. Because CBECS data only shows total building area instead of total area covered by economizers, this comparison is mostly to understand the ballpark estimation of economizer coverage.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/86105.yaml
     source: 86105_images/image_000009_995c7f6d12a9c00251dff248c817f1eb9759beb37eb41ce2ac8c56870d2a345d.png
     method: vision-description
     described: 2026-08-21 -->

![Two-panel horizontal stacked bar chart comparing economizer floor-area coverage by building type in ComStock against CBECS 2018, with every percentage labelled and each row summing to 100%.](86105_images/image_000009_995c7f6d12a9c00251dff248c817f1eb9759beb37eb41ce2ac8c56870d2a345d.png)

Figure 3 (Section 2) compares economizer coverage by building type between ComStock and CBECS 2018. Both panels plot "% of total floor area" from 0 to 100% and every segment is labelled, with each row summing to exactly 100.00. Panel (a), "Coverage in ComStock for each building type", has a YES/NO legend: FullServiceRestaurant 40.28/59.72, Hospital 56.50/43.50, LargeHotel 24.63/75.37, LargeOffice 50.15/49.85, MediumOffice 47.52/52.48, Outpatient 44.37/55.63, PrimarySchool 48.75/51.25, QuickServiceRestaurant 12.90/87.10, RetailStandalone 42.72/57.28, RetailStripmall 41.64/58.36, SecondarySchool 51.96/48.04, SmallHotel 2.85/97.15, SmallOffice 18.29/81.71, Warehouse 33.58/66.42. Panel (b), "Coverage in CBECS 2018", adds a Null category; its Yes values are FullServiceRestaurant 31.69, Hospital 87.69, LargeHotel 39.20, LargeOffice 70.66, MediumOffice 54.49, Outpatient 47.62, PrimarySchool 53.63, QuickServiceRestaurant 19.89, RetailStandalone 17.80, RetailStripmall 40.73, SecondarySchool 55.73, SmallHotel 2.29, SmallOffice 19.12, Warehouse 14.01. CBECS reports much higher coverage for hospitals and large offices and much lower coverage for standalone retail. Panel (b)'s legend title is misprinted "Economizer Availabillity".

(a) Coverage in ComStock for each building type

(b) Coverage in CBECS 2018 for each building type

Figure 3. Economizer floor area coverage between ComStock and CBECS (2018)

