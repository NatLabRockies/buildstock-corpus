<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96349.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96349.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96349.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: upgrade_measures/measure_pdfs/96349.md | section: 2  Applicability | lines: 232-275 -->
## 2  Applicability

Advanced air sealing upgrades are applied to dwelling units with infiltration rates greater than or equal 6 ACH50.

Attic floor insulation upgrades are applied only to dwelling units with unfinished attics (vented and unvented attic type in ResStock). Specifically, upgrades are triggered when attic floor insulation is below the following levels: less than R-49 in climate zone 1 and less than R-60 in climate zones 2 through 8.

Duct sealing applies to dwelling units with duct leakage to the outside greater than 6% or duct insulation rated below R-6. Dwelling units with 0% leakage to the and uninsulated ducts are not applicable, as these configurations typically indicate that the ducts are located entirely within conditioned spaces.

Drill-and-fill wall insulation is applicable to dwelling units with uninsulated wood stud walls.

Further details on the applicability criteria and stock saturation for each of these four upgrades can be found in the accompanying documentation (Phoung, Lou, &amp; White, 2025a) (Phoung, Lou, &amp; White, 2025b) (Lou &amp; Liu, 2025) (Brossman &amp; Lou, 2025). Table 1 summarizes the stock saturation for the upgrade package that includes all four measures. This comprehensive package is applicable to approximately 98% of the U.S. housing stock. However, most homes receive only one or some of these upgrades. Only 9.2% of homes receive all four upgrades.

Table 1. Stock Saturation for the Envelope Package Upgrades (Advanced Air Sealing + Attic Insulation + Duct Sealing and Insulation+ Drill-and-Fill Wall Insulation)

| Advanced Air Sealing Upgrade   | Attic Floor Insulation Upgrade   | Duct Sealing and Insulation Upgrade   | Drill-and-Fill Wall Insulation Upgrade   |   Stock Saturation (%) |
|--------------------------------|----------------------------------|---------------------------------------|------------------------------------------|------------------------|
| NO                             | NO                               | NO                                    | NO                                       |                    2.0 |
| NO                             | NO                               | NO                                    | YES                                      |                    0.2 |
| NO                             | NO                               | YES                                   | NO                                       |                    1.4 |
| NO                             | NO                               | YES                                   | YES                                      |                    0.1 |
| NO                             | YES                              | NO                                    | NO                                       |                    0.9 |
| NO                             | YES                              | NO                                    | YES                                      |                    0.1 |
| NO                             | YES                              | YES                                   | NO                                       |                    3.0 |
| NO                             | YES                              | YES                                   | YES                                      |                    0.2 |
| YES                            | NO                               | NO                                    | NO                                       |                   28.4 |
| YES                            | NO                               | NO                                    | YES                                      |                   11.3 |
| YES                            | NO                               | YES                                   | NO                                       |                    9.0 |
| YES                            | NO                               | YES                                   | YES                                      |                    5.0 |
| YES                            | YES                              | NO                                    | NO                                       |                    6.2 |
| YES                            | YES                              | NO                                    | YES                                      |                    4.5 |
| YES                            | YES                              | YES                                   | NO                                       |                   18.7 |
| YES                            | YES                              | YES                                   | YES                                      |                    9.2 |

When retrieving results for this measure package, here is a brief example of how to filter dwelling units that received some, or all four individual measures of the package upgrade. First, consult the enumeration dictionary for this release. The enumeration dictionary for ResStock 2025 Release 1 is available on the Open Energy Data Initiative (OEDI), and it describes the columns names and possible values for each column. The enumeration dictionary for this dataset release will be in a folder like oedi-data-lake/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2025. For this measure upgrade, the primary columns of interest are in.infiltration , in.insulation\_ceiling , in.duct\_leakage\_and\_insulation, and in.insulation\_wall . Filter these columns in your data file to the values specified to only see dwelling units and results that are applicable for each individual measure upgrade, as shown in Table 2.

Table 2. Housing Characteristics that Applicable to Individual Measure

| Upgrade Measure                | Housing Characteristics                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Advanced Air Sealing           | in.infiltration is 6 ACH50, 7 ACH50, 8 ACH50, 10 ACH50, 15 ACH50, 20 ACH50, 25 ACH50, 30 ACH50, 40 ACH50, 50 ACH50                                                                                                                                                                                                                                                                                                  |
| Attic Floor Insulation         | in.insulation_ceiling is Uninsulated, R-7, R-13, R-19, R-30, R-38 if in Climate Zone 1. in.insulation_ceiling is Uninsulated, R-7, R-13, R-19, R-30, R-38, R-49 if in Climate Zones 2 through 8                                                                                                                                                                                                                     |
| Duct Sealing and Insulation    | in.duct_leakage_and_insulation is 10% Leakage to Outside, R-4; 10% Leakage to Outside, R-6; 10% Leakage to Outside, R-8; 10% Leakage to Outside, Uninsulated; 20% Leakage to Outside, R-4; 20% Leakage to Outside, R-6; 20% Leakage to Outside, R-8; 20% Leakage to Outside, Uninsulated; 30% Leakage to Outside, R-4; 30% Leakage to Outside, R-6 30% Leakage to Outside, R-8; 30% Leakage to Outside, Uninsulated |
| Drill-and-Fill Wall Insulation | in.insulation_wall is Wood Stud, Uninsulated                                                                                                                                                                                                                                                                                                                                                                        |

