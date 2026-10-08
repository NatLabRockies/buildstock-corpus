<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89126.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/89126.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/89126.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/89126.md | section: 3.2.1 Applicability | lines: 355-371 -->
## 3.2.1 Applicability

The HP-RTU measure is applicable to ComStock models with gas furnace RTUs ('PSZ-AC with gas coil') or electric resistance RTUs ('PSZ-AC with electric coil'), two of the most common HVAC system types in the ComStock baseline (Figure 2). ComStock HVAC distributions are informed by the 2012 Commercial Buildings Energy Consumption Survey. The methodology for interpreting Commercial Buildings Energy Consumption Survey data to create HVAC probability distributions for ComStock is discussed in the ComStock documentation [2]. The measure is not applicable to space types that directly serve kitchens, spaces that are unconditioned, or RTUs with outdoor air ratios above 65% (due to an EnergyPlus bug with cycling operation). This upgrade is applicable to about 34% of the ComStock floor area.

Figure 2. ComStock HVAC system type prevalence by stock floor area (HVAC systems with &lt;1% floor area prevalence not shown)

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89126.yaml
     source: 89126_images/image_000003_8e7aa4ad6b4eb1b89fa305071954f9bc10aacac65dc06b75eb0e4ff9b93e3f21.png
     method: vision-description
     described: 2026-08-20 -->

![Two-panel horizontal bar chart of ComStock HVAC system type prevalence by stock floor area](89126_images/image_000003_8e7aa4ad6b4eb1b89fa305071954f9bc10aacac65dc06b75eb0e4ff9b93e3f21.png)

Figure 2. Two-panel horizontal bar chart of ComStock HVAC system type prevalence (HVAC systems with <1% floor area prevalence not shown). Left panel: Stock Floor Area (ft2); right panel: Percent of Stock Floor Area. Rows by HVAC system type, largest first: PSZ-AC with gas coil 16.49B ft2 / 29.59%, PVAV with gas boiler reheat 5.418 / 10.08%, PSZ-AC with electric coil 5.418 / 9.70%, PVAV with gas heat with electric reheat 3.428 / 6.14%, PVAV with PFP boxes 3.098 / 5.54%, residential AC with residential forced air furnace 2.458 / 4.40%, PSZ-HP 2.068 / 3.70%, PTAC with electric coil 1.788 / 3.20%, PTHP 1.388 / 2.49%, VAV chiller with PFP boxes 1.488 / 2.66%, plus smaller DOAS and water-source-heat-pump systems. Establishes that packaged single-zone gas/electric rooftop units dominate the applicable stock. (Dense small labels -- flag exact values for QA.)

PTHP stands for packaged terminal heat pump, PTAC stands for packaged terminal air conditioner, PVAV stands for packaged variable air volume, DOAS stands for dedicated outdoor air system, and PFP stands for parallel fanpower.

