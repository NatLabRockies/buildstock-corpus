<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/98223.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/98223.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/98223.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/98223.md | section: 3.1  Applicability | lines: 225-251 -->
## 3.1  Applicability

In this study, the term 'applicability' refers to when and where an upgrade is implemented across the building stock. For example, if a baseline building model already includes an energyefficient system (as is sometimes the case in ComStock), we avoid replacing it with an upgrade that performs equally or worse. Therefore, 'applicability' defines the specific conditions under which an upgrade is applied to an existing building model.

For this upgrade, the first step is to determine whether the building model includes any waterbased systems that use pumps. These systems may be associated with space heating (e.g., using boilers), space cooling (e.g., using chillers), or service water heating (e.g., water heaters). However, the primary focus of this upgrade is on space heating and cooling systems.

Once it is confirmed that space heating and cooling water systems are present in the existing building model, the measure identifies all pumps associated with those systems. Regardless of whether the existing pumps are constant speed or variable speed, the upgrade attempts to replace all of them according to the specifications outlined in Section 3.2.

However, if the existing pump specifications (e.g., motor efficiency) are already better than those defined by this upgrade, no replacement will be made for those pumps. For detailed information on the pump specifications used in this upgrade, refer to Section 3.2.

Again, the variable-speed pump measure applies to ComStock models that utilize water-based systems for space heating or cooling, representing approximately 31% of the total ComStock floor area (Figure 3). The distribution of HVAC system types in ComStock is based on data from the 2012 and 2018 CBECS. The methodology used to interpret CBECS data and develop HVAC probability distributions for ComStock is detailed in the ComStock Documentation report [6]. As illustrated in Figure 3 (note the logarithmic scale on the x -axis), the applicable HVAC systems include components such as chillers, boilers, and district heating and cooling systems.

Figure 3. ComStock HVAC system type prevalence by stock floor area .

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/98223.yaml
     source: 98223_images/image_000004_0064d17d0dbb6131120a5ddae2eab0af730dbedab0d749577d0a217cf4cf2c65.png
     method: vision-description
     described: 2026-08-20 -->

![Figure 3: horizontal bar chart of ComStock HVAC system type prevalence as a percent of total stock floor area, with 24 labeled bars coloured by whether the variable-speed pump measure is applicable](98223_images/image_000004_0064d17d0dbb6131120a5ddae2eab0af730dbedab0d749577d0a217cf4cf2c65.png)

Figure 3 of the ComStock Variable-Speed Pumps measure documentation. Twenty-four horizontal bars, one per HVAC system type, are plotted against 'Percent of total stock floor area [%]' and coloured by a legend headed Applicability, False in blue and True in orange. Every bar but one carries a printed data label. The non-applicable types are PSZ-AC with gas coil 29.46, PSZ-AC with electric coil 13.69, PVAV with PFP boxes 8.25, PVAV with gas heat with electric reheat 4.08, Residential AC with forced air furnace 3.67, PTAC with electric coil 3.34, PTHP 3.25, PSZ-HP 2.73 and PTAC with gas coil 0.56. The applicable types are PVAV with gas boiler reheat 8.15, VAV chiller with gas boiler reheat 7.17, VAV air-cooled chiller with gas boiler reheat 3.17, VAV chiller with PFP boxes 2.48, VAV district chilled water with district hot water reheat 1.99, PSZ-AC with gas boiler 1.64, PTAC with gas boiler (label missing, measured about 1.3), DOAS with WSHP with ground source heat pump 1.19, VAV chiller with district hot water reheat 0.86, DOAS with WSHP cooling tower with boiler 0.85, four DOAS-with-fan-coil variants at 0.81, 0.61, 0.36 and 0.11, and a residual bar for HVAC types below 0.1% at 0.23. The applicable bars total about 31 percent, as Section 3.1 states.

PSZ-AC = packaged single-zone air conditioner; PTHP = packaged terminal heat pump; PFP = parallel fan power; PTAC = packaged terminal air conditioner; VAV = variable air volume; PVAV = packaged variable air volume; DOAS = dedicated outdoor air system

In real-world applications, variable-speed pumps are often used in both the primary and secondary loops of chilled water and hot water systems to maximize energy efficiency and operational flexibility. While ASHRAE 90.1 appendix G typically assumes a constant-flow primary loop paired with a variable-flow secondary loop for chilled water systems, and often constant-flow configurations for hot water systems, modern designs are increasingly adopting fully variable-flow configurations for both. This shift reduces pumping energy, enhances equipment performance, and maintains optimal temperature differentials across a wide range of load conditions. Additionally, dynamic control strategies such as differential pressure reset and supply temperature reset further improve system responsiveness and lower operating costs. Accordingly, this study explores the use of fully variable-flow pumps in both chilled water and hot water systems.

