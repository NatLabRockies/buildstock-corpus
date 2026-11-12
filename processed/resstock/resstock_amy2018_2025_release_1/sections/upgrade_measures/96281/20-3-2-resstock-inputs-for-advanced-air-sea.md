<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96281.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96281.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96281.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96281.md | section: 3.2  ResStock Inputs for Advanced Air Sealing with Drill-and-Fill Wall Insulation | lines: 302-355 -->
## 3.2  ResStock Inputs for Advanced Air Sealing with Drill-and-Fill Wall Insulation

Building characteristics are assigned in ResStock and then translated into more detailed OS-HPXML arguments that describe a ResStock parameter. The drill-and-fill wall insulation measure leverages the 'Insulation Wall' ResStock option that assigns wall assembly R-values and wall types in OS-HPXML. As of ResStock 2024 Release 2, there are 15 different baseline insulation wall options (Reyna, Fontanini and Present, et al. 2024). The ResStock argument definitions set in the Insulation Wall characteristic are reproduced in Table 4, originally from the ResStock Technical Reference Documentation, v3.3.0 Table 46, which details the assumptions for ResStock 2024 (Reyna, Fontanini and Present, et al. 2024). Advanced air sealing arguments are provided in the measure documentation (Phoung, Lou and White 2025).

5  https://github.com/NatLabRockies/resstock/tree/v3.2.0-2024.2/resources/hpxml-measures

Table 4. OS-HPXML Arguments Assigned with the ResStock 'Insulation Wall' Option Argument Values for Drill-and-Fill Wall Insulation

<!-- table recovered from measure_pdfs/96281.pdf p.18
     overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/96281.yaml
     method: extracted grid, with one unit rewritten as a fraction (compared with the page render)
     supersedes the extractor's own table here (values b2abb8a4f516…):
       The Units cell of wall_assembly_r is printed as a stacked fraction, h-ft²-R over Btu. The extractor flattened it to 'h-ft 2 -R Btu', which loses the fraction bar and the superscript and does not read as a unit. It is written 'h-ft²-R/Btu'. Every other cell is the extractor's own; a line-break space in 'R-value' is removed. -->

| OS-HPXML Argument | Required | Units | Type | Choices | Description |
|---|---|---|---|---|---|
| wall_type | true | - | Choice | WoodStud, ConcreteMasonryUnit, DoubleWoodStud, InsulatedConcreteForms, LogWall, StructuredInsulatedPanel, SolidConcrete, SteelFrame, Stone, StrawBale, StructuralBrick | The type of walls |
| wall_assembly_r | true | h-ft²-R/Btu | - | Double | Assembly R-value of the walls |

Advanced air sealing arguments can be found in the advanced air sealing documentation (Phoung, Lou and White 2025).

Table 5 describes variables changed in the EnergyPlus model due to the application of drill-and-fill wall insulation with advanced air sealing. The HVAC-related arguments are modified because of different HVAC capacities, not specifically to model advanced air sealing or drill-and-fill wall insulation. This is not an exhaustive list, and the arguments that change depend on the individual building energy model. The variable values are model dependent, therefore only the names, units, and descriptions are provided.

Table 5. Idf File Argument Changes as a Result of Advanced Air Sealing with Drill-and-Fill Wall Insulation

<!-- table recovered from measure_pdfs/96281.pdf p.18
     overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/96281.yaml
     method: extracted grids joined under one header, with units rewritten as fractions (compared with the page renders)
     supersedes the extractor's own table here (values f1b4f65a84ca…):
     and its continuation grid(s) (values e49a82211d26…):
       The table runs over two pages and was extracted as two grids, each with the header row. Its units are printed as stacked fractions with superscripts (W over m-K, m³ over s, W over K, cm²), and the argument names carry the same superscripts ({cm²}, {m³/s}). The extractor flattened them to 'W m-K', 'm 3 s', 'W K', 'cm 2', '{cm 2 }' and '{m 3 /s}', which do not read as units. They are written 'W/m-K', 'm³/s', 'W/K', 'cm²', '{cm²}' and '{m³/s}'. Every other cell is the extractor's own, the 13 rows joined under the one header. -->

| IDF File Argument | Units | Description |
|---|---|---|
| c | - | Converts the flow coefficient based on ASHRAE principles |
| Conductivity | W/m-K | Conductivity of the wall stud and cavity |
| Effective Air Leakage Area {cm²} | cm² | Area where air can escape |
| Maximum Air Flow Rate {m³/s} | m³/s | Maximum air flow rate through a duct |
| Design Supply Air Flow Rate {m³/s} | m³/s | Design condition for the air flow rate for the air-source heat pump |
| Cooling Supply Air Flow Rate {m³/s} | m³/s | Cooling design condition for the air flow rate for the air-source heat pump |
| Design Maximum Air Flow Rate {m³/s} | m³/s | Maximum air flow rate for the air-source heat pump fan |
| Speed Flow Fraction 1 | - | Flow fraction for the fan speed (Big Ladder Software n.d.) |
| Speed Electric Power Fraction 1 | - | Electric power fraction for the fan speed (Big Ladder Software n.d.) |
| Heating Design Capacity {W} | W | The heating design capacity of the baseboard heating system if present |
| U-Factor Times Area Value {W/K} | W/K | Heat transfer through the baseboard heating wall if present |
| Maximum Water Flow Rate {m³/s} | m³/s | The maximum water flow rate of the baseboard heating system if present |
| Nominal Capacity {W} | W | Capacity of the hot water boiler if present |

OS-HPXML models wood stud walls using an overall wall assembly R-value. 6  The wall assembly includes layers such as drywall, sheathing, the stud and cavity layer, and others. The assembly's R -value determines the final wall construction set to match the ResStock assembly R-value.

When the wall assembly changes, various HVAC variables are affected. These variables depend on the HVAC system type, as shown in Table 5, which covers changes for heat pumps, boilers, and furnaces.

6 For an in-depth explanation on wood stud depth and R-value calculations, see the ResStock resource page: https://NatLabRockies.github.io/ResStock.github.io/docs/resources/explanations/Wood\_Stud\_Depth.html

