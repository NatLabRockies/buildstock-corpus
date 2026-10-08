<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89481.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89481.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89481.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89481.md | section: 3.1  Applicability | lines: 323-364 -->
## 3.1  Applicability

The HP-RTU measure is applicable to ComStock models with either gas furnace RTUs ('PSZAC with gas coil') or electric resistance RTUs ('PSZ-AC with electric coil'). This accounts for about 33.3% of the ComStock floor area (Figure 4). ComStock HVAC distributions are informed by the 2012 CBECS. The methodology for interpreting CBECS data to create HVAC probability distributions for ComStock is discussed in the ComStock Documentation [15]. The measure is not applicable to space types that directly serve kitchens, spaces that are unconditioned, or RTUs with outdoor air ratios above 65% (due to an EnergyPlus ®  bug with cycling operation).

Figure 4. ComStock HVAC system type prevalence by stock floor area . Orange represents the portion of the stock applicable to the HP-RTU measure, while blue shows non-applicable portions of the stock.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89481.yaml
     source: 89481_images/image_000005_420b8817e66f06921195251d4dcb330fedbfb37d9bb431a2bf88c553cab99d7b.png
     method: vision-description
     described: 2026-08-20 -->

![Three-panel bar chart of ComStock HVAC system type prevalence by stock floor area, floor area percentage, and model count, with the two applicable PSZ-AC types highlighted](89481_images/image_000005_420b8817e66f06921195251d4dcb330fedbfb37d9bb431a2bf88c553cab99d7b.png)

Figure 4 ranks ComStock HVAC system types by prevalence, with three side-by-side panels: absolute stock floor area (0 to about 40 billion ft2), percent of stock floor area (0% to about 30%), and percent of model count (0% to about 40%). Bars are colored by an 'Applicability Add Heat Pump Rtu' flag, orange for True and blue for False. The applicable orange types are 'PSZ-AC with gas coil', by a wide margin the largest single system type in the stock, and 'PSZ-AC with electric coil'; together they account for about 33.3% of ComStock floor area. Non-applicable blue types, in descending order, include PVAV with gas boiler reheat, VAV chiller with gas boiler reheat, PVAV with gas heat coils and electric reheat, VAV air-cooled chiller with gas boiler reheat, residential AC with residential forced air furnace, PVAV with PFP boxes, PSZ-HP, PTAC with electric coil, PSZ-AC with gas boiler, PTHP, VAV chiller with PFP boxes, several DOAS variants, and a residual 'All Others' bar under 1% of floor area. PSZ stands for packaged single zone, PVAV for packaged variable air volume, DOAS for dedicated outdoor air system, and PFP for parallel fan power.

PTHP stands for packaged terminal heat pump, PTAC stands for packaged terminal air conditioner, PVAV stands for packaged variable air volume, DOAS stands for dedicated outdoor air system, and PFP stands for parallel fan power.

For this study, heat/energy recovery is included in all the new HP-RTUs except for those serving food service building types. Although there is evidence to suggest that exhaust air recovery can be applied to kitchen exhaust hoods, there are additional considerations that need to be factored in to meaningfully model the application, and these are beyond the scope of this study. The only exception to this would be existing RTUs that already included energy recovery in the baseline; in these instances, a new energy recovery system is added.

Table 2 compares the stock floor area served by RTUs with heat or energy recovery for the ComStock baseline and the HP-RTU with heat/energy recovery scenarios. The baseline only includes heat/energy recovery where required by the local governing energy code at the time of last HVAC replacement. The HP-RTU scenario adds heat/energy recovery when the applicability criteria of both the HP-RTU system and the heat/energy recovery system discussed in this section are met.

Note that in most cases, there is a large increase in heat/energy recovery as a result of combining heat/energy recovery with the HP-RTU scenario. Food service building types do not show additional heat/energy recovery since they deemed not applicable for this study. Also note that we do not see 100% floor area covered by a recovery system for any building type. This is because some of the floor area is served by systems not applicable to the HP-RTU measure, and therefore they do not receive heat/energy recovery. For example, warehouses have substantial area served by unit heaters. Other cases include the prevalence of food service in some models, or outdoor air ratios that are too high.

Table 2. Fraction of Stock Floor Area Served by Heat or Energy Recovery Systems for the ComStock Baseline and the HP -RTU with Heat/Energy Recovery Scenarios

Table only includes buildings served by RTUs.

| Building Type          | Baseline   | HP-RTU With Heat/Energy Recovery   |
|------------------------|------------|------------------------------------|
| FullServiceRestaurant  | 4%         | 4%                                 |
| Hospital               | 0%         | 93%                                |
| LargeOffice            | 5%         | 74%                                |
| MediumOffice           | 0%         | 75%                                |
| Outpatient             | 0%         | 71%                                |
| PrimarySchool          | 4%         | 68%                                |
| QuickServiceRestaurant | 1%         | 1%                                 |
| RetailStandalone       | 2%         | 97%                                |
| RetailStripmall        | 2%         | 80%                                |
| SecondarySchool        | 8%         | 57%                                |
| SmallOffice            | 0%         | 94%                                |
| Warehouse              | 0%         | 28%                                |

