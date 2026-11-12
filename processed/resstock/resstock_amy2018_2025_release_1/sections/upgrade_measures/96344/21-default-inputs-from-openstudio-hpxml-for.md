<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96344.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96344.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96344.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: upgrade_measures/measure_pdfs/96344.md | section: Default Inputs From OpenStudio-HPXML for the Duct Sealing and Insulation Upgrades | lines: 216-241 -->
## Default Inputs From OpenStudio-HPXML for the Duct Sealing and Insulation Upgrades

The ResStock inputs in the table above are sent to OS-HPXML. Any values not specified by ResStock are calculated using the defaults in the BuildResidentialHPXML OpenStudio measure. See the OS-HPXML Air Distribution documentation for the available HPXML schema elements, default values, and constraints.

Table 3. HPXML Default Values for the Duct Sealing and Insulation Upgrades

<!-- table recovered from measure_pdfs/96344.pdf p.14
     overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/96344.yaml
     method: extracted grid, with the split Notes cells rejoined (compared with the page render and text layer)
     supersedes the extractor's own table here (values 5cd58c8c258b…):
       The Notes column has two merged cells, each covering two rows: one note for the two buried-insulation-level rows and one for the two fraction-rectangular rows. The extractor cut each note in the middle of a sentence and put the first half on one row and the second half on the next, so neither row carried a readable note ('...Fully buried ducts' / 'have insulation that just covers...'). Every other cell was right. Each note is rejoined from the extractor's own two halves and repeated on both rows it covers. -->

**Table 3, part 1 of 2**

| HPXML Default Variable | Value | Units | Notes |
|---|---|---|---|
| ducts_supply_buried_insulation_level | Not buried | - | An option to indicate whether the supply and return ducts are buried in, e.g., attic loose-fill insulation. Partially buried ducts have insulation that does not cover the top of the ducts. Fully buried ducts have insulation that just covers the top of the ducts. Deeply buried ducts have insulation that extends above the top of the ducts. See the Building America Solution Center for more information. |
| ducts_return_buried_insulation_level | Not buried | - | An option to indicate whether the supply and return ducts are buried in, e.g., attic loose-fill insulation. Partially buried ducts have insulation that does not cover the top of the ducts. Fully buried ducts have insulation that just covers the top of the ducts. Deeply buried ducts have insulation that extends above the top of the ducts. See the Building America Solution Center for more information. |
| ducts_supply_fraction_rectangular | 0.25 | - | The fraction of supply and return ducts that are rectangular (as opposed to round); this affects the duct effective R-value used for modeling. A value of 1.0 means DuctShape is 'rectangular' and 0.0 means DuctShape is 'round' or 'oval.' |

**Table 3, part 2 of 2**

| HPXML Default Variable | Value | Units | Notes |
|---|---|---|---|
| ducts_return_fraction_rectangular | 1.0 | - | The fraction of supply and return ducts that are rectangular (as opposed to round); this affects the duct effective R-value used for modeling. A value of 1.0 means DuctShape is 'rectangular' and 0.0 means DuctShape is 'round' or 'oval.' |

