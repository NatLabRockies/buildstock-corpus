<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/87570.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/87570.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/87570.pdf | corpus_version: b5faf42 | corpus_path: upgrade_measures/measure_pdfs/87570.md | section: 5.2  Stock Site Energy Impacts | lines: 434-467 -->
## 5.2  Stock Site Energy Impacts

The HP-RTU measure with original fuel supplemental heat demonstrates 8.5% total site energy savings (396 trillion British thermal units [TBtu]) for the U.S. commercial building stock modeled in ComStock (Figure 4). The measure is applicable to about 36% of the Comstock floor area. The savings are primarily attributed to:

- 27% stock heating gas savings (226 TBtu)
- -22% stock heating electricity savings ( -43 TBtu)
- 11% stock cooling electricity savings (81 TBtu)
- 19% stock fan electricity savings (112 TBtu).

The site gas heating savings are attributed to switching gas-heated systems in the ComStock baseline to electric HP-RTU systems. This substantially reduces gas heating in these buildings, but some still rely on gas supplemental heating when the heat pump alone can't meet the entire heating demand. Note that some gas heating will remain in spaces deemed not applicable for this measure (e.g., kitchens).

Site electricity for heating exhibits net negative energy savings, with factors leading to both savings and penalties in this category. The HP-RTU measure transitions buildings from gas-fired RTUs to electric HP-RTUs, increasing stock electric heating. However, the HP-RTU measure also replaces electric resistance RTUs with higher-efficiency HP-RTUs, causing some reduction in stock electric heating. However, as mentioned, the combined impact of these two factors yields an increase in stock electricity for heating.

The cooling savings are from using a high-efficiency, variable-speed compressor in the HPRTUs, which generally exceeds the performance of the existing RTU systems. As discussed previously, many of the ComStock baseline systems are assumed to follow the required performance of older energy code years, which the new HP-RTU systems usually outperform (Figure 4).

Figure 4. Comparison of stock annual site energy consumption between the ComStock baseline and the HP-RTU measure for the electric backup heat scenario (left; 'HP RTU E Backup') and the original fuel backup measure scenario (right; 'HP RTU G Backup'). Energy consumption is categorized both by fuel type and end use.

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/87570.yaml
     source: 87570_images/image_000005_21bc3d55cb0dbb1a2c0f05dfc042b6153110e81375272b36d184e41e564c2ee6.png
     method: vision-description
     described: 2026-08-20 -->

![Two stacked column charts of annual stock site energy consumption, Baseline vs HP-RTU with electric backup and vs gas backup](87570_images/image_000005_21bc3d55cb0dbb1a2c0f05dfc042b6153110e81375272b36d184e41e564c2ee6.png)

Figure 4. Two side-by-side stacked column charts of annual stock site energy consumption (TBtu), y-axis 0 to about 4600. Left compares ComStock Baseline (total 4638) with HP RTU E Backup (4235); right compares the same Baseline (4638) with HP RTU G Backup (4242, an 8.5% / 396 TBtu reduction). Columns are segmented by end use and fuel per the legend. Legible segments (unchanged across scenarios): Interior Equipment Electricity 836.5. Changing segments include Fans Electricity 598.3 falling to about 476.4, Cooling Electricity 724.7 to about 644.0, and the heating segments, which are the only end uses that differ between the electric-backup and gas-backup variants. Shows cooling and fan efficiency drive most savings, while supplemental fuel choice only shuffles heating between gas and electricity.

Fan energy savings are from using high-efficiency, variable-speed fans in the HP-RTU systems. The high-efficiency fans require less energy to move the same amount of air, while the variablespeed fan controls allow the system to use less airflow during periods of lower loads.

Figure 4 compares two iterations of the HP-RTU measure: electric resistance supplemental heat (left) and original fuel supplemental heat (right). First, note that gas and electric heating are the only end uses that show any difference between these two scenarios. This is because the supplemental heating fuel type is the only change between scenarios, which does not impact the savings of cooling, fans, etc.

For the heating end uses, the original fuel backup HP-RTU scenario uses 10% less stock electricity heating and 6% more stock natural gas heating than the electric backup HP-RTU scenario. This behavior is expected because using gas supplemental heat instead of electric resistance will decrease electricity heating consumption but increase natural gas heating consumption. Lastly, Figure 4 shows slightly higher total site energy usage for the original fuel backup scenario. This is due to efficiency differences between gas and electric supplemental heating, where the electric supplemental heating is modeled with a COP of 1 while the gas supplemental heating is modeled with a COP of 0.8.

It is important to weigh multiple considerations when determining the preferred supplemental heating fuel type for a use case. So far, this discussion has only focused on site energy consumption, but projects also may want to consider source energy consumption, greenhouse gas emissions, energy cost, and peak demand implications to determine what is most appropriate for a particular application. Aside from energy cost implications, these factors are discussed to some extent in later sections of this report.

