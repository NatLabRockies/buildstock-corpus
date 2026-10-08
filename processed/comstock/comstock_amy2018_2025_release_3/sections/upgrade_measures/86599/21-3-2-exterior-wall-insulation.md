<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/86599.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/86599.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/86599.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/86599.md | section: 3.2 Exterior Wall Insulation | lines: 387-396 -->
## 3.2 Exterior Wall Insulation

The Exterior Wall Insulation upgrade applies extruded polystyrene (XPS) insulation to applicable building models. First, it determines the thickness of XPS required to meet the specified R-value, determined from the Zero Energy Small/Medium Office AEDG target assembly performance for each climate zone (Table 5). Second, it finds all the constructions used by exterior walls in the model, clones them, adds a layer of insulation to the cloned constructions, and then assigns the construction back to the wall. Based on the baseline, the updated wall properties may be close to the target values, but exact target values may not be achieved.

Table 5. AEDG Overall Wall Assembly Performance Characteristics by Climate Zone [3]

| ASHRAE Climate Zone     |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |
|-------------------------|-----|-----|-----|-----|-----|-----|-----|-----|
| R-Value (hr ft 2 F/Btu) |  13 |  13 |  16 |  16 |  19 |  21 |  21 |  29 |

