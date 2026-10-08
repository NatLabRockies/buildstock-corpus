<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/96598.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96598.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96598.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/96598.md | section: 3.2.4  Roof Insulation Upgrade Methodology | lines: 894-984 -->
## 3.2.4  Roof Insulation Upgrade Methodology

This measure upgrades the roof insulation for each building to the assigned code in force for the state where the building is located. The R-value of the roof assembly will be upgraded to the new R-value for the assigned code, which can be found in Table 12 (non-California) and Table 13 (California). If the roof insulation of a building is already at the desired code level, no changes will be made.

Note that these tables contain some duplicative information to the tables in Section 2.3.2; however, Table 12 does not include the pre-1980 and 1980-2004 templates, but it does include the 90.1-2016 and 90.1-2019 templates. This is because in the upgrade scenario, the building's current code template will be set to a template ranging from 90.1-2004 to 90.1-2019, depending on what state it is in. In Table 13, only the DEER 2020 template is shown because all California buildings will be set to this code level in the upgrade scenario. The data for 90.1-2016, 90.12019, and DEER 2020 are derived from the openstudio-standards database [23], as these templates are not represented in the baseline of ComStock (and therefore not included in the ComStock Reference Documentation [11]).

Table 12. Upgrade Roof R-Value by Roof Type, Energy Code, and Climate Zone for Non-California Buildings.

<!-- table recovered from measure_pdfs/96598.pdf p.32
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/96598.yaml
     method: pdf-text-layer
     supersedes the extractor's own table here (values 709463b76410…):
       docling emitted this grid under the Table 13 caption and dropped the Roof Type column
       entirely, so the Attic and other / IEAD / Metal building groups ran together as 18
       undifferentiated rows.
       As in all six grids on these pages, the markdown header row held the table's subtitle
       repeated across every column and the real climate-zone header was demoted into the body
       as a data row, so the table had no usable header. -->

**Whole Roof Assembly R-Value by ASHRAE Climate Zone (ft²*F*h/Btu)**
**Includes interior and exterior air films**

**Roof Type: Attic and other**

| Energy Code | 1A | 2A | 2B | 3A | 3B | 3C | 4A | 4B | 4C | 5A | 5B | 5C | 6A | 6B | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 90.1-2004 | 29 | 29 | 29 | 29 | 29 | 29 | 29 | 29 | 29 | 29 | 29 | 29 | 37 | 37 | 37 | 37 |
| 90.1-2007 | 29 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 48 |
| 90.1-2010 | 29 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 48 |
| 90.1-2013 | 37 | 37 | 37 | 37 | 37 | 37 | 48 | 48 | 48 | 48 | 48 | 48 | 48 | 48 | 59 | 59 |
| 90.1-2016 | 37 | 37 | 37 | 37 | 37 | 37 | 48 | 48 | 48 | 48 | 48 | 48 | 48 | 48 | 59 | 59 |
| 90.1-2019 | 37 | 37 | 37 | 37 | 37 | 37 | 48 | 48 | 48 | 48 | 48 | 48 | 48 | 48 | 59 | 59 |

**Roof Type: IEAD**

| Energy Code | 1A | 2A | 2B | 3A | 3B | 3C | 4A | 4B | 4C | 5A | 5B | 5C | 6A | 6B | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 90.1-2004 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 21 |
| 90.1-2007 | 16 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 |
| 90.1-2010 | 16 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 |
| 90.1-2013 | 21 | 26 | 26 | 26 | 26 | 26 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 36 | 36 |
| 90.1-2016 | 21 | 26 | 26 | 26 | 26 | 26 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 36 | 36 |
| 90.1-2019 | 21 | 26 | 26 | 26 | 26 | 26 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 36 | 36 |

**Roof Type: Metal building**

| Energy Code | 1A | 2A | 2B | 3A | 3B | 3C | 4A | 4B | 4C | 5A | 5B | 5C | 6A | 6B | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 90.1-2004 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 20 |
| 90.1-2007 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 20 |
| 90.1-2010 | 15 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 20 | 20 | 20 | 29 |
| 90.1-2013 | 24 | 24 | 24 | 24 | 24 | 24 | 27 | 27 | 27 | 27 | 27 | 27 | 32 | 32 | 34 | 38 |
| 90.1-2016 | 24 | 24 | 24 | 24 | 24 | 24 | 27 | 27 | 27 | 27 | 27 | 27 | 32 | 32 | 34 | 38 |
| 90.1-2019 | 24 | 24 | 24 | 24 | 24 | 24 | 27 | 27 | 27 | 27 | 27 | 27 | 32 | 32 | 34 | 38 |

<!-- text repaired by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/96598.yaml
     docling promoted this one-line source note to a level-2 heading. Because the
     chunker is heading-aware, that filed 30 of this document's chunks under a
     section named 'Data from [11], [23]' instead of '3.2.4 Roof Insulation
     Upgrade Methodology' -- and replaced the breadcrumb rather than nesting under
     it, so the section those chunks belong to was not recoverable from them. The
     line is restored to the prose it is in the source. A corpus-wide scan found
     this to be the only citation note promoted to a heading in the release. -->

Data from [11], [23]

Table 13. Upgrade Roof R-Value by Roof Type, Energy Code, and Climate Zone for California Buildings.

<!-- table recovered from measure_pdfs/96598.pdf p.32
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/96598.yaml
     method: pdf-text-layer
     supersedes the extractor's own table here (values 694ffd87c89e…):
       docling merged the '10' and '11' CEC zone labels into one cell and left the next cell
       empty, so from that point on the zone labels sat one column to the right of the
       values they label: the figures for zones 12 through 16 read as belonging to zones 11
       through 15. The values themselves are correct.
       As in all six grids on these pages, the markdown header row held the table's subtitle
       repeated across every column and the real climate-zone header was demoted into the body
       as a data row, so the table had no usable header. -->

**Whole Roof Assembly R-Value by CEC Climate Zone (ft²*F*h/Btu)**
**Includes interior and exterior air films**

| Roof Type | Energy Code | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IEAD | DEER 2020 | 25 | 29 | 29 | 29 | 26 | 15 | 20 | 20 | 29 | 29 | 29 | 29 | 29 | 29 | 29 | 29 |
| Mass | DEER 2020 | 25 | 29 | 29 | 29 | 26 | 15 | 20 | 20 | 29 | 29 | 29 | 29 | 29 | 29 | 29 | 29 |
| Wood framed | DEER 2020 | 25 | 29 | 29 | 29 | 26 | 15 | 20 | 20 | 29 | 29 | 29 | 29 | 29 | 29 | 29 | 29 |

Data from [23]

