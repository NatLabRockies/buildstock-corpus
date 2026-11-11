<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96281.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96281.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96281.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96281.md | section: 2 Applicability | lines: 229-291 -->
## 2 Applicability

Both parts of this package, advanced air sealing and drill-and-fill insulation, apply to about 29% of the ResStock 2025 Release 1 baseline housing stock. Advanced air sealing alone applies to about 92%, and drill-and-fill wall insulation applies to about 30% of the existing ResStock 2025 Release 1 baseline housing stock. More information on advanced air sealing and applicability is available in the advanced air sealing documentation (Phoung, Lou and White 2025).

Table 1 shows the wall and insulation distributions of the ResStock 2025 Release 1 baseline housing stock. This measure applies only to wood stud framing with uninsulated walls.

Table 1. Framing and Insulation Type as a Percentage of the ResStock 2025 Release 1 Baseline Housing Stock

| Framing Type and Insulation Level   |   % of Baseline Housing Stock |
|-------------------------------------|-------------------------------|
| Brick, 12-in, 3-wythe, R-7          |                           2.6 |
| Brick, 12-in, 3-wythe, R-11         |                           5.5 |
| Brick, 12-in, 3-wythe, R-15         |                           1.4 |
| Brick, 12-in, 3-wythe, R-19         |                           1.5 |
| Brick, 12-in, 3-wythe, Uninsulated  |                           9.9 |
| CMU, 6-in Hollow, R-7               |                           0.4 |
| CMU, 6-in Hollow, R-11              |                           0.9 |
| CMU, 6-in Hollow, R-15              |                           0.2 |
| CMU, 6-in Hollow, R-19              |                           0.4 |
| CMU, 6-in Hollow, Uninsulated       |                           1.4 |
| Wood Stud, R-7                      |                           7.3 |
| Wood Stud, R-11                     |                          22.7 |
| Wood Stud, R-15                     |                           4.7 |
| Wood Stud, R-19                     |                          10.5 |
| Wood Stud, Uninsulated              |                          30.5 |

Table 2 summarizes the joint probability of uninsulated wood stud walls and their infiltration rates. The table represents all baseline dwelling units, or 100%, but only the uninsulated wood stud wall type is detailed with infiltration rates.

Table 2. Probability of Baseline Model Uninsulated Wood Stud Wall and Infiltration Type

| Framing and Insulation Type   | Infiltration Rate   |   % Baseline Dwelling Units |
|-------------------------------|---------------------|-----------------------------|
| Wood stud, uninsulated        | 2 ACH50             |                        0.02 |
| Wood stud, uninsulated        | 3 ACH50             |                        0.08 |
| Wood stud, uninsulated        | 4 ACH50             |                        0.16 |
| Wood stud, uninsulated        | 5 ACH50             |                        0.29 |
| Wood stud, uninsulated        | 6 ACH50             |                        0.45 |
| Wood stud, uninsulated        | 7 ACH50             |                        0.66 |
| Wood stud, uninsulated        | 8 ACH50             |                        0.87 |
| Wood stud, uninsulated        | 10 ACH50            |                        2.29 |
| Wood stud, uninsulated        | 15 ACH50            |                        7.23 |
| Wood stud, uninsulated        | 20 ACH50            |                        6.46 |
| Wood stud, uninsulated        | 25 ACH50            |                        4.56 |
| Wood stud, uninsulated        | 30 ACH50            |                        2.90 |
| Wood stud, uninsulated        | 40 ACH50            |                        2.88 |
| Wood stud, uninsulated        | 50 ACH50            |                        1.72 |

In total, about 29% of the ResStock 2025 Release 1 baseline housing stock could receive the full package of advanced air sealing with drill-and-fill wall insulation. As a result, the findings are heavily influenced by the advanced air sealing alone, which applies to 92% of the ResStock 2025 Release 1 baseline dwelling units.

When reviewing results for this upgrade, here is a brief example of how to filter for dwelling units that received only advanced air sealing, only drill-and-fill wall insulation, or both parts of the upgrade in the baseline housing stock.

First, consult the enumeration dictionary for this release 4 , which describes the column names and possible values for each column. For this measure upgrade, the primary columns of interest are in.infiltration and in.insulation\_wall. To see the applicable dwelling units only, filter these columns to the following values.

4 https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-buildingstock/2025/resstock\_amy2018\_release\_1/enumeration\_dictionary.tsv

Table 3. Relevant Column Names and Values for Specific Portions of This Upgrade

| Measure Scenario                                             | in.infiltration value                                                                           | in.insulation_wall value                     | ResStock 2025 Release 1 baseline applicability   |
|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------|--------------------------------------------------|
| Advanced air sealing only                                    | 6 ACH50, 7 ACH50, 8 ACH50, 10 ACH50, 15 ACH50, 20 ACH50, 25 ACH50, 30 ACH50, 40 ACH50, 50 ACH50 | All values except for Wood Stud, Uninsulated | 92.2%                                            |
| Drill-and-fill insulation only                               | 1 ACH50, 2 ACH50, 3 ACH50, 4 ACH50, 5 ACH50                                                     | Wood Stud, Uninsulated                       | 30.02%                                           |
| Advanced air sealing and drill- and-fill insulation together | 6 ACH50, 7 ACH50, 8 ACH50, 10 ACH50, 15 ACH50, 20 ACH50, 25 ACH50, 30 ACH50, 40 ACH50, 50 ACH50 | Wood Stud, Uninsulated                       | 29.47%                                           |

