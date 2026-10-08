<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/87570.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/87570.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/87570.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/87570.md | section: 3.1  Applicability | lines: 304-320 -->
## 3.1  Applicability

The HP-RTU measure is applicable to ComStock models with either gas furnace RTUs ('PSZAC with gas coil') or electric resistance RTUs ('PSZ-AC with electric coil'). This accounts for about 36% of the ComStock floor area (Figure 2). ComStock HVAC distributions are informed by the 2012 CBECS. The methodology for interpreting CBECS data to create HVAC probability distributions for ComStock is discussed in the ComStock documentation [3]. The measure is not applicable to space types that directly serve kitchens, spaces that are unconditioned, or RTUs with outdoor air ratios above 65% (due to an EnergyPlus ®  bug with cycling operation).

Figure 2. ComStock HVAC system type prevalence by stock floor area .

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/87570.yaml
     source: 87570_images/image_000003_42a1b06c9dff87f535dd65e0dc844f9fcaedb1ed74b4a1d10fd1d5085c19d495.png
     method: vision-description
     described: 2026-08-20 -->

![Horizontal bar chart of ComStock HVAC system type prevalence by stock floor area, floor area, and model count](87570_images/image_000003_42a1b06c9dff87f535dd65e0dc844f9fcaedb1ed74b4a1d10fd1d5085c19d495.png)

Figure 2. Horizontal bar chart of ComStock HVAC system type prevalence, with three value columns per system type: % of Stock Floor Area, Stock Floor Area (ft2), and Model Count. PSZ-AC with gas coil is the most common (27.65% of stock floor area, 14,744,407,702 ft2, 40.45% of models) followed by PSZ-AC with electric coil (9.82% / 5,134,140,479 / 12.81%). Other types include PVAV with gas boiler reheat (7.10%), PVAV with gas heat with electric reheat (5.07%), VAV air-cooled chiller with gas boiler reheat, PTHP, PTAC, PSZ-HP, and a long tail; 'All others (<1% area)' sums to 8.60%. The two applicable PSZ-AC types together make up roughly 36% of stock floor area.

PTHP stands for packaged terminal heat pump, PTAC stands for packaged terminal air conditioner, PVAV stands for packaged variable air volume, DOAS stands for dedicated outdoor air system, and PFP stands for parallel fan-power.

