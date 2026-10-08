<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/95009.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy25osti/95009.pdf | publication_url: https://docs.nlr.gov/docs/fy25osti/95009.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/95009.md | section: 3.5 Exterior Wall Insulation | lines: 635-644 -->
## 3.5 Exterior Wall Insulation

The Exterior Wall Insulation upgrade applies extruded polystyrene (XPS) insulation to applicable building models. First, it determines the thickness of XPS required to meet the specified R-value, determined from the Zero Energy Small/Medium Office AEDG target assembly performance for each climate zone (Table 9). Second, it finds all the constructions used by exterior walls in the model, clones them, adds a layer of insulation to the cloned constructions, and then assigns the construction back to the wall. Based on the baseline, the updated wall properties may be close to the target values, but exact target values may not be achieved.

Table 9. AEDG Overall Wall Assembly Performance Characteristics by Climate Zone [11]

| ASHRAE Climate Zone     |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |
|-------------------------|-----|-----|-----|-----|-----|-----|-----|-----|
| R-Value (hr ft 2 F/Btu) |  13 |  13 |  16 |  16 |  19 |  21 |  21 |  29 |

