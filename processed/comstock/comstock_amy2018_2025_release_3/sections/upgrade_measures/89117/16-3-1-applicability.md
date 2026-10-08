<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89117.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89117.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89117.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/89117.md | section: 3.1  Applicability | lines: 308-340 -->
## 3.1  Applicability

This measure will be applied to all packaged single-zone systems modeled in ComStock, which is about 45% of the weighted floor area. Figure 1 shows the prevalence of HVAC system types in ComStock.

Equipment for conditioning spaces dominated by process loads, such as data centers, is not a good candidate for a VFD retrofit due to the consistent loads. The data center space type present in ComStock, as part of a large office building, is not served by a packaged single-zone system, so this consideration does not affect measure applicability in this case (Parker, 2023).

The DCV component of this measure will not be applied to space types for which DCV is not appropriate, corresponding to the following space types represented in ComStock:

- Kitchens
- Dining
- Laboratories
- Healthcare patient spaces
- Corridors and stairwells
- Mechanical rooms
- High exhaust spaces, such as restrooms and locker rooms.

Healthcare patient spaces must provide a consistent level of ventilation at a prescribed level to ensure patient safety. Kitchens also require a consistent level of ventilation for safe operation, and kitchens often draw transfer air from adjacent dining spaces. Energy code guidance recommends that laboratory spaces in hospitals not have DCV applied.

This measure is also not intended to be applied to dedicated outdoor air units, as incorporating variable-speed fan control in such a unit would likely involve DCV, which is addressed as a separate option. Fan-coil units can, in some instances, be retrofitted for VAV operation, but are not considered in the scope of this measure due to the different conditions involved in assessing their suitability for retrofit. 5

5 Several companies make retrofit kits to install electronically commutated motors in fan coil units, which can facilitate variable-speed fan operation. These include AirRevive, Unilux Solutions, and IEC's EnviroKit (International Environmental (IEC), 2023), (Unilux Suite Solutions, 2021), (AirRevive, N.D.)).

Figure 1. Prevalence of HVAC system types in ComStock

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89117.yaml
     source: 89117_images/image_000005_8e578cbdafac3f6dcf6deca6356f5cd2dbcc5b0474cb4cc58647ccd87aae8f9c.png
     method: vision-description
     described: 2026-08-21 -->

![Three-panel horizontal bar chart of ComStock HVAC system type prevalence by percent of stock floor area, absolute stock floor area and model count, led by PSZ-AC with gas coil at 27.65%.](89117_images/image_000005_8e578cbdafac3f6dcf6deca6356f5cd2dbcc5b0474cb4cc58647ccd87aae8f9c.png)

Three side-by-side panels share the same 18 HVAC system type rows under the header "in.hvac_system_type (group)". The panels are "% of Stock Floor Area" (0% to 40%), "Stock Floor Area" (0B to 30B) and "Model Count" (0% to 40%). Data labels alternate between rows, so no single panel labels every row. Printed percentages of stock floor area: PSZ-AC with gas coil 27.65; PVAV with gas boiler reheat 9.82; VAV chiller with gas boiler reheat 7.10; VAV air-cooled chiller with gas boiler reheat 5.07; PVAV with PFP boxes 4.08; PTAC with electric coil 3.16; PTHP 2.28; DOAS with water source heat pumps cooling tower 1.96; DOAS with fan coil chiller with boiler 1.23; All others (<1% Area) 8.60. Printed stock floor areas include PSZ-AC with gas coil 16,744,407,702 ft2, PSZ-AC with electric coil 5,134,140,479 and PVAV with gas heat with electric reheat 3,369,888,394, implying a total stock of about 60.6 billion ft2. Dividing the unlabelled floor areas by that total gives PSZ-AC with electric coil about 8.5% and PSZ-AC with gas boiler about 2.5%; the three PSZ-AC rows therefore total 38.6%, the share the measure is applicable to.

