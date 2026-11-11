<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96739.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96739.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96739.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96739.md | section: 2  Applicability | lines: 207-232 -->
## 2  Applicability

The attic floor insulation upgrade logic is based on a threshold approach, where homes are eligible for retrofit if their existing attic insulation R-value is below the IECC 2021recommended level for their respective climate zone (Table 2). However, a minimum threshold is set such that the existing R-value must be at least R-10 values lower than the maximum recommended level to qualify for the upgrade. This constraint is applied to avoid inefficient retrofits with marginal benefit, since adding insulation to already well-insulated attics provides diminishing returns in energy savings and may not be cost-effective. Target R-values are assigned by climate zone using DOE-recommended R-values in Table 2 as guidance. Table 3 shows R-values that are typically achieved through retrofits from previous empirical studies. The following logics are applied to existing units:

1. Units have existing attics (automatically exclude multifamily units and mobile homes).
2. Existing attics have an R-value at least R-10 lower than targeted attic insulation level specified for their climate zone in Table 2.
3. Use the upper bound of recommended attic insulation by climate zone in Table 2 to simulate the highest energy savings scenario.

Note that in Table 2 and Table 3, the highest bound of R-value range is used in the simulations to represent the most energy-efficient scenarios. Previous studies are referenced to demonstrate that these R-values are reasonable as an upper bound. But, in some cases, our simulations test higher R-values than are typically installed. To determine eligibility for an upgrade, the existing attic must be at least 10 ft²·°F·hr/Btu (R-value) below the target for its climate zone. For example, a unit with existing R-29 won't get upgraded to R-30 because the marginal benefit of adding 1 Rvalue is negligible. The R-10  below target rule ensures that upgrades are applied only where they provide meaningful savings. Also, by including only dwellings with attics, this will automatically only include single-family units because ResStock only models attics for singlefamily units, whereas multifamily models do not include attics. Figure 1 and Figure 2 show the distribution of baseline insulation level by vintage and climate zone, respectively.

Table 4. Summarized application logic for attic floor insulation for unfinished attics

| Attic Type                                  | Climate Zone        | Insulation Ceiling                              | Target Insulation Ceiling   | Stock Saturation   |
|---------------------------------------------|---------------------|-------------------------------------------------|-----------------------------|--------------------|
| Vented Attic, unvented attic                | 1                   | Uninsulated, R-7, R- 13, R-19, R-30, R-38       | R-49                        | 0.6%               |
| Vented Attic, unvented attic                | 2, 3, 4, 5, 6, 7, 8 | Uninsulated, R-7, R- 13, R-19, R-30, R-38, R-49 | R-60                        | 42.3%              |
| None, finished attic, or cathedral ceilings | All                 | All                                             | N/A                         | 57.1%              |

Figure 1. Distribution of baseline insulation (R-value) by vintage

![Image](96739_images/image_000002_91c9a8ed13074cbecc7e1794b4a545230145c12e70a8f9a795e36ff99dd8d55e.png)

Figure 2. Distribution of baseline insulation by climate zone

![Image](96739_images/image_000003_aaeebb418e9862b88f53b8bbc2353ecf9cf2df5fc24331b8982a244442912a27.png)

