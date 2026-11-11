<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/99818.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/99818.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/99818.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/99818.md | section: 2  Applicability | lines: 232-266 -->
## 2  Applicability

The light air sealing upgrade is applied to dwelling units with infiltration rates greater than or equal to 10 ACH50.

The attic floor insulation upgrade is applied only to dwelling units with unfinished attics (vented and unvented attic types in ResStock). Specifically, the upgrade is applied when attic floor insulation is below R-49 in climate zone 1 and below R-60 in climate zones 2 through 8.

Duct sealing applies to dwelling units with duct leakage to the outside greater than 6% or duct insulation rated below R-6. Dwelling units with 0% leakage to the outside and uninsulated ducts are not applicable, as these configurations typically indicate that the ducts are located entirely within conditioned spaces (Lou and Liu 2026).

Further details on the applicability criteria and residential building stock saturation for each of these three measures can be found in the accompanying documentation (Brossman, White and Phoung 2026) (Phoung, Lou and White 2026) (Lou and Liu 2026).

Table 1 summarizes the stock saturation for the upgrade package that includes all three measures. This comprehensive package is applicable to approximately 92.5% of the U.S. housing stock. However, most dwelling units receive only one or some of these upgrades. Only 22.9% of dwelling units receive all three upgrades.

Table 1. Stock Saturation for the Envelope Package Upgrades (Light Air Sealing + Attic Insulation + Duct Sealing and Insulation)

| Light Air Sealing Upgrade   | Attic Floor Insulation Upgrade   | Duct Sealing and Insulation Upgrade   |   Stock Saturation (%) |
|-----------------------------|----------------------------------|---------------------------------------|------------------------|
| NO                          | NO                               | NO                                    |                    7.5 |
| NO                          | NO                               | YES                                   |                    4.0 |
| NO                          | YES                              | NO                                    |                    2.6 |
| NO                          | YES                              | YES                                   |                    8.2 |
| YES                         | NO                               | NO                                    |                   34.2 |
| YES                         | NO                               | YES                                   |                   11.4 |
| YES                         | YES                              | NO                                    |                    9.2 |
| YES                         | YES                              | YES                                   |                   22.9 |

When reviewing results for this measure package, here is a brief example of how to filter dwelling units that received some or all three individual measures of the upgrade package. First, consult the enumeration dictionary for this release. The enumeration dictionary for ResStock 2025 Release 1 is available on the Open Energy Data Initiative (OEDI) and describes the column names and possible values for each column. The enumeration dictionary for 2018 weather of this dataset release resides here: https://oedidata-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-usbuilding-stock/2025/resstock\_amy2018\_release\_1/enumeration\_dictionary.tsv. For this measure upgrade, the primary columns of interest are in.infiltration , in.insulation\_ceiling , and in.duct\_leakage\_and\_insulation , and in.ASHRAE Iecc Climate Zone 2004 . Filter these columns in your data file to the values specified in Table 2, in addition to filtering applicability to 'True' to view only the dwelling units and results applicable to each individual measure upgrade.

Table 2. Housing Characteristics That Are Applicable to Individual Measures

| Upgrade Measure             | Housing Characteristics                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Light Air Sealing           | in.infiltration is 10 ACH50, 15 ACH50, 20 ACH50, 25 ACH50, 30 ACH50, 40 ACH50, 50 ACH50                                                                                                                                                                                                                                                                                                                              |
| Attic Floor Insulation      | in.insulation_ceiling is Uninsulated, R-7, R-13, R-19, R-30, R-38 if the dwelling unit is in climate zone 1. in.insulation_ceiling is Uninsulated, R-7, R-13, R-19, R-30, R-38, R-49 if the dwelling unit is in climate zones 2 through 8.                                                                                                                                                                           |
| Duct Sealing and Insulation | in.duct_leakage_and_insulation is 10% Leakage to Outside, R-4; 10% Leakage to Outside, R-6; 10% Leakage to Outside, R-8; 10% Leakage to Outside, Uninsulated; 20% Leakage to Outside, R-4; 20% Leakage to Outside, R-6; 20% Leakage to Outside, R-8; 20% Leakage to Outside, Uninsulated; 30% Leakage to Outside, R-4; 30% Leakage to Outside, R-6; 30% Leakage to Outside, R-8; 30% Leakage to Outside, Uninsulated |

