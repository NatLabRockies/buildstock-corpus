<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/96598.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96598.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96598.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/96598.md | section: 2.3.2 Roof Insulation | lines: 399-517 -->
## 2.3.2 Roof Insulation

In the ComStock baseline, the thermal performance of roofs (R-value/U-value) is determined by the energy code assigned to the building, the climate zone, and the roof construction type. Our research indicated that more than 90% of commercial floor space has flat or shallow pitch roofs; therefore, ComStock assumes flat roofs for modeling simplicity.

For all states except California, ComStock models three roof types commonly seen in commercial construction: insulation entirely above deck (IEAD), metal building, and attic/other. In California, roof constructions are based on the DEER prototypes, and they include mass, wood-framed, and IEAD roofs. The roof construction assigned to a building is fixed based on the building type. More details can be found in the ComStock Reference Documentation [11].

As mentioned, because the EUL assumption for roofs is 200 years, the roofs in most buildings are assumed to be original. Table 5 shows the average assembly R-value by climate zone, roof construction type, and energy code template for non-California buildings. Note that metal buildings are not modeled for pre-1980 [11]. Table 6 shows the average assembly R-value by climate zone, roof construction type, and energy code template for California buildings. Note that the roof constructions in DEER are categorized by CEC climate zones.

Table 5. Baseline Roof R-Value by Roof Type, Energy Code, and Climate Zone for Non-California Buildings.

<!-- table recovered from measure_pdfs/96598.pdf p.20
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/96598.yaml
     method: pdf-text-layer
     supersedes the extractor's own table here (values 521126274c2a…):
       docling emitted this grid under the Table 6 caption and dropped the Roof Type column
       entirely, so the Attic and other / IEAD / Metal building groups ran together as 17
       undifferentiated rows -- three different assemblies sharing the same energy-code
       labels, with nothing to say which R-value belongs to which.
       As in all six grids on these pages, the markdown header row held the table's subtitle
       repeated across every column and the real climate-zone header was demoted into the body
       as a data row, so the table had no usable header. -->

**Whole Roof Assembly R-Value by ASHRAE Climate Zone (ft²*F*h/Btu)**
**Includes interior and exterior air films**

**Roof Type: Attic and other**

| Energy Code | 1A | 2A | 2B | 3A | 3B | 3C | 4A | 4B | 4C | 5A | 5B | 5C | 6A | 6B | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pre-1980 | 10 | 10 | 10 | 10 | 10 | 10 | 12 | 11 | 12 | 14 | 13 | 13 | 17 | 17 | 17 | 17 |
| 1980–2004 | 14 | 15 | 22 | 14 | 21 | 11 | 17 | 17 | 16 | 19 | 20 | 20 | 22 | 20 | 25 | 32 |
| 90.1-2004 | 29 | 29 | 29 | 29 | 29 | 29 | 29 | 29 | 29 | 29 | 29 | 29 | 37 | 37 | 37 | 37 |
| 90.1-2007 | 29 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 48 |
| 90.1-2010 | 29 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 37 | 48 |
| 90.1-2013 | 37 | 37 | 37 | 37 | 37 | 37 | 48 | 48 | 48 | 48 | 48 | 48 | 48 | 48 | 59 | 59 |

**Roof Type: IEAD**

| Energy Code | 1A | 2A | 2B | 3A | 3B | 3C | 4A | 4B | 4C | 5A | 5B | 5C | 6A | 6B | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pre-1980 | 10 | 10 | 10 | 10 | 10 | 10 | 12 | 11 | 12 | 14 | 13 | 13 | 17 | 17 | 17 | 17 |
| 1980–2004 | 14 | 15 | 22 | 14 | 21 | 11 | 17 | 17 | 16 | 19 | 20 | 20 | 22 | 20 | 25 | 32 |
| 90.1-2004 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 21 |
| 90.1-2007 | 16 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 |
| 90.1-2010 | 16 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 |
| 90.1-2013 | 21 | 26 | 26 | 26 | 26 | 26 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 31 | 36 | 36 |

**Roof Type: Metal building**

| Energy Code | 1A | 2A | 2B | 3A | 3B | 3C | 4A | 4B | 4C | 5A | 5B | 5C | 6A | 6B | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1980–2004 | 10 | 10 | 10 | 10 | 10 | 10 | 12 | 11 | 12 | 14 | 13 | 13 | 22 | 20 | 25 | 32 |
| 90.1-2004 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 20 |
| 90.1-2007 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 20 |
| 90.1-2010 | 15 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 18 | 20 | 20 | 20 | 29 |
| 90.1-2013 | 24 | 24 | 24 | 24 | 24 | 24 | 27 | 27 | 27 | 27 | 27 | 27 | 32 | 32 | 34 | 38 |

Table from [11]

Table 6. Baseline Roof U-Value by Roof Type, Energy Code, and Climate Zone for California Buildings.

<!-- table recovered from measure_pdfs/96598.pdf p.20
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/96598.yaml
     method: pdf-text-layer
     supersedes the extractor's own table here (values 1be1e582894f…):
       docling kept the Roof Type column but left it empty in all 27 rows, and in the Wood
       framed group merged the DEER 2014 and DEER 2015 rows into a single row of doubled
       values ('20 20', '26 26'), which also displaced values in the two rows above it.
       As in all six grids on these pages, the markdown header row held the table's subtitle
       repeated across every column and the real climate-zone header was demoted into the body
       as a data row, so the table had no usable header. -->

**Whole Roof Assembly R-Value by CEC Climate Zone (ft²*F*h/Btu)**
**Includes interior and exterior air films**

**Roof Type: IEAD**

| Energy Code | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DEER pre-1975 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 |
| DEER 1985 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 |
| DEER 1996 | 18 | 18 | 18 | 18 | 18 | 13 | 13 | 13 | 13 | 13 | 18 | 18 | 18 | 18 | 18 | 18 |
| DEER 2003 | 18 | 18 | 18 | 18 | 18 | 13 | 13 | 13 | 13 | 18 | 18 | 18 | 18 | 18 | 18 | 18 |
| DEER 2007 | 20 | 20 | 20 | 20 | 20 | 13 | 13 | 13 | 13 | 20 | 20 | 20 | 20 | 20 | 20 | 20 |
| DEER 2011 | 20 | 26 | 26 | 26 | 20 | 13 | 15 | 15 | 26 | 26 | 26 | 26 | 26 | 26 | 26 | 26 |
| DEER 2014 | 20 | 26 | 26 | 26 | 20 | 13 | 15 | 15 | 26 | 26 | 26 | 26 | 26 | 26 | 26 | 26 |
| DEER 2015 | 20 | 26 | 26 | 26 | 20 | 13 | 15 | 15 | 26 | 26 | 26 | 26 | 26 | 26 | 26 | 26 |
| DEER 2017 | 20 | 26 | 26 | 26 | 20 | 13 | 15 | 15 | 26 | 26 | 26 | 26 | 26 | 26 | 26 | 26 |

**Roof Type: Mass**

| Energy Code | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DEER pre-1975 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 16 |
| DEER 1985 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 |
| DEER 1996 | 18 | 18 | 18 | 18 | 18 | 13 | 13 | 13 | 13 | 13 | 18 | 18 | 18 | 18 | 18 | 18 |
| DEER 2003 | 18 | 18 | 18 | 18 | 18 | 13 | 13 | 13 | 13 | 18 | 18 | 18 | 18 | 18 | 18 | 18 |
| DEER 2007 | 20 | 20 | 20 | 20 | 20 | 13 | 13 | 13 | 13 | 20 | 20 | 20 | 20 | 20 | 20 | 20 |
| DEER 2011 | 20 | 26 | 26 | 26 | 20 | 13 | 15 | 15 | 26 | 26 | 26 | 26 | 26 | 26 | 26 | 26 |
| DEER 2014 | 20 | 26 | 26 | 26 | 20 | 13 | 15 | 15 | 26 | 26 | 26 | 26 | 26 | 26 | 26 | 26 |
| DEER 2015 | 20 | 26 | 26 | 26 | 20 | 13 | 15 | 15 | 26 | 26 | 26 | 26 | 26 | 26 | 26 | 26 |
| DEER 2017 | 20 | 26 | 26 | 26 | 20 | 13 | 15 | 15 | 26 | 26 | 26 | 26 | 26 | 26 | 26 | 26 |

**Roof Type: Wood framed**

| Energy Code | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DEER pre-1975 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 |
| DEER 1985 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 |
| DEER 1996 | 18 | 18 | 18 | 18 | 18 | 13 | 13 | 13 | 13 | 13 | 18 | 18 | 18 | 18 | 18 | 18 |
| DEER 2003 | 18 | 18 | 18 | 18 | 18 | 13 | 13 | 13 | 13 | 18 | 18 | 18 | 18 | 18 | 18 | 18 |
| DEER 2007 | 20 | 20 | 20 | 20 | 20 | 13 | 13 | 13 | 13 | 20 | 20 | 20 | 20 | 20 | 20 | 20 |
| DEER 2011 | 20 | 26 | 26 | 26 | 20 | 13 | 15 | 15 | 26 | 26 | 26 | 26 | 26 | 26 | 26 | 26 |
| DEER 2014 | 20 | 26 | 26 | 26 | 20 | 13 | 15 | 15 | 26 | 26 | 26 | 26 | 26 | 26 | 26 | 26 |
| DEER 2015 | 20 | 26 | 26 | 26 | 20 | 13 | 15 | 15 | 26 | 26 | 26 | 26 | 26 | 26 | 26 | 26 |
| DEER 2017 | 20 | 26 | 26 | 26 | 20 | 13 | 15 | 15 | 26 | 26 | 26 | 26 | 26 | 26 | 26 | 26 |

Table from [11]

