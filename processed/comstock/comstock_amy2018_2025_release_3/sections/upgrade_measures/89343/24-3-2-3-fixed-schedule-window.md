<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89343.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89343.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89343.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89343.md | section: 3.2.3  Fixed Schedule Window | lines: 335-357 -->
## 3.2.3  Fixed Schedule Window

The fixed schedule option represents the most used demand flexibility strategy currently (discussed in Section 1.2) and is implemented as a comparative reference. We integrated the existing GEB measure in the OpenStudio GEB measure gem [34] to generate a daily schedule of the peak window by specifying peak window start and end time for summer and winter. The assumed peak window specifications are summarized in Table 4, which are derived from assumed peak windows by Electricity Market Module regions from EIA documentation [12]. Although the fixed schedule method has been widely used as the default control strategy in existing demand flexibility research, it has evident drawbacks when applying for daily dispatch providing the natural conflict of 'fixed' and 'flexibility,' which will be shown in Section 4.

Table 4. Assumed Fixed Peak Window by Climate Zones

| ASHRAE Climate Zone   | Summer Peak Period   | Winter Peak Period   |
|-----------------------|----------------------|----------------------|
| 2A                    | 5-8 p.m.             | 6-9 p.m.             |
| 2B                    | 4-7 p.m.             | 6-9 p.m.             |
| 3A                    | 6-9 p.m.             | 5-8 p.m.             |
| 3B                    | 5-8 p.m.             | 6-9 p.m.             |
| 3C                    | 6-9 p.m.             | 5-8 p.m.             |
| 4A                    | 1-4 p.m.             | 5-8 p.m.             |
| 4B                    | 4-7 p.m.             | 6-9 p.m.             |
| 4C                    | 4-7 p.m.             | 5-8 p.m.             |
| 5A                    | 5-8 p.m.             | 5-8 p.m.             |
| 5B                    | 4-7 p.m.             | 5-8 p.m.             |
| 5C                    | 4-7 p.m.             | 5-8 p.m.             |
| 6A                    | 3-6 p.m.             | 5-8 p.m.             |
| 6B                    | 4-7 p.m.             | 5-8 p.m.             |
| 7                     | 3-6 p.m.             | 5-8 p.m.             |

