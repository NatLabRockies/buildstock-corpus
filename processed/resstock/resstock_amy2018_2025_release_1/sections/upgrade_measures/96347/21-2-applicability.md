<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96347.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96347.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96347.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96347.md | section: 2  Applicability | lines: 171-204 -->
## 2  Applicability

Advanced air sealing upgrades are applied to dwelling units with infiltration rates greater than or equal to 6 ACH50.

Attic floor insulation upgrades are applied only to dwelling units with unfinished attics (vented and unvented attic types in ResStock). Specifically, upgrades are triggered when attic floor insulation is below the following levels: less than R-49 in climate zone 1 and less than R-60 in climate zones 2 through 8.

Duct sealing applies to dwelling units with duct leakage to the outside greater than 6% or duct insulation rated below R-6. Dwelling units with 0% leakage to the outside and uninsulated ducts are not applicable, as these configurations typically indicate that the ducts are located entirely within conditioned spaces.

Further details on the applicability criteria and stock saturation for each of these three measures can be found in the accompanying documentation (Phoung, Lou, &amp; White, 2025a) (Phoung, Lou, &amp; White, 2025b) (Lou &amp; Liu, 2025). Table 1 summarizes the stock saturation for the upgrade package that includes all three measures. This comprehensive package is applicable to approximately 97.9% of the U.S. housing stock. However, most homes receive only one or some of these upgrades. Only 27.8% of homes receive all three upgrades.

Table 1. Stock Saturation for the Envelope Package Upgrades (Advanced Air Sealing + Attic Insulation + Duct Sealing and Insulation)

| Advanced Air Sealing Upgrade   | Attic Floor Insulation Upgrade   | Duct Sealing and Insulation Upgrade   |   Stock Saturation (%) |
|--------------------------------|----------------------------------|---------------------------------------|------------------------|
| NO                             | NO                               | NO                                    |                    2.1 |
| NO                             | NO                               | YES                                   |                    1.5 |
| NO                             | YES                              | NO                                    |                    1.0 |
| NO                             | YES                              | YES                                   |                    3.1 |
| YES                            | NO                               | NO                                    |                   39.7 |
| YES                            | NO                               | YES                                   |                   14.0 |
| YES                            | YES                              | NO                                    |                   10.7 |
| YES                            | YES                              | YES                                   |                   27.8 |

When reviewing results for this measure package, here is a brief example of how to filter dwelling units that received some or all three individual measures of the package upgrade. First, consult the enumeration dictionary for this release. The enumeration dictionary for ResStock 2025 Release 1 is available on OEDI and describes the column names and possible values for each column. The enumeration dictionary for this dataset release will be in a folder like oedidata-lake/nlr-pds-building-stock/end-use-load-profiles-for-us-building-stock/2025. For this measure upgrade, the primary columns of interest are in.infiltration , in.insulation\_ceiling , and in.duct\_leakage\_and\_insulation . Filter these columns in your data file to the values specified in Table 2 to view only the dwelling units and results applicable to each individual measure upgrade.

Table 2. Housing Characteristics That Are Applicable to Individual Measures

Upgrade Measure

| Advanced Air Sealing        | in.infiltration is 6 ACH50, 7 ACH50, 8 ACH50, 10 ACH50, 15 ACH50, 20 ACH50, 25 ACH50, 30 ACH50, 40 ACH50, 50 ACH50                                                                                                                                                                                                                                                                                                   |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Attic Floor Insulation      | in.insulation_ceiling is Uninsulated, R-7, R-13, R-19, R-30, R-38 if the dwelling unit is in climate zone 1. in.insulation_ceiling is Uninsulated, R-7, R-13, R-19, R- 30, R-38, R-49 if the dwelling unit is in climate zones 2 through 8.                                                                                                                                                                          |
| Duct Sealing and Insulation | in.duct_leakage_and_insulation is 10% Leakage to Outside, R-4; 10% Leakage to Outside, R-6; 10% Leakage to Outside, R-8; 10% Leakage to Outside, Uninsulated; 20% Leakage to Outside, R-4; 20% Leakage to Outside, R-6; 20% Leakage to Outside, R-8; 20% Leakage to Outside, Uninsulated; 30% Leakage to Outside, R-4; 30% Leakage to Outside, R-6; 30% Leakage to Outside, R-8; 30% Leakage to Outside, Uninsulated |

