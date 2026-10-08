<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89130.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89130.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89130.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/89130.md | section: 1.1.1.3  Griddles | lines: 343-395 -->
## 1.1.1.3  Griddles

The two main types of griddles are standard griddles (flat, one-sided plate) and double-sided griddles (like a panini press). Standard griddles, as the name suggests, are more common and will be assumed for modeling.

Figure 3. Typical commercial one-sided standard griddle [8]

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89130.yaml
     source: 89130_images/image_000009_e7c7e5c91310ee625312971c87acf6030452cb8e3a910927a20bbb3cd41fda1d.png
     method: vision-description
     described: 2026-08-21 -->

![Photograph of a typical commercial one-sided standard flat griddle with three burner knobs](89130_images/image_000009_e7c7e5c91310ee625312971c87acf6030452cb8e3a910927a20bbb3cd41fda1d.png)

Figure 3: product photograph of a typical commercial one-sided standard griddle - a flat stainless steel cooking plate with a rear splash guard, a front grease trough and three burner control knobs. Reproduced from reference 8. Tables 5 and 6 give griddle rated input power and commercially available specifications.

Table 5 shows the same four sources used previously and their assumptions for rated input power for gas and electric griddles. ASHRAE specifies that their values represent a flat, 3-foot griddle, but we can safely assume that all of them refer to standard, flat griddles.

Table 5. Comparison of Griddle Rated Input Power from Four Sources

| Source                           | Gas (Btu/h)   | Electric (Btu/h)   |
|----------------------------------|---------------|--------------------|
| 2015 DOE Report [8]              | 70,000        | 40,946             |
| FSTC 2002 [9]                    | 40,000-80,000 | 25,000-60,000      |
| ASHRAE 2017 [6]                  | 90,000        | 58,400             |
| PG&E Production Test Kitchen [7] | 60,000        | 42,000             |

All sources are generally in the same range for gas and electric power. To verify, Table 6 shows some commercially available standard griddles for comparison.

Table 6. Specifications of Commercially Available Gas and Electric Griddles [10]

<!-- table recovered from 89130_images/image_000010_43e419a0d42312f3d5a62393120964e4c2da2a3eaf317d9a9b308689930b2e2e.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89130.yaml
     method: pdf-text-layer (values) + vision-transcription (product names) -->

| Image | Cooking Performance Group GM-CPG-36-NL 36" Gas Countertop Griddle with | Avantco Chef Series CAG-48-MG 48" Countertop Gas Griddle with Manual Controls |
|---|---|---|
| Fuel | Gas | Gas |
| Rated Input (Btu/h) | 90,000 | 120,000 |

| Image | Vulcan HEG36E 36" Electric Countertop Griddle with Snap-Action Thermostatic | Cooking Performance Group G-CPG-48-M 48" Electric Countertop Griddle - 12,000W |
|---|---|---|
| Fuel | Electric | Electric |
| Rated Input (kW) | 16.2 | 12 |
| Rated Input (Btu/h) | 55,200 | 41,000 |

Two product names are cut off mid-phrase in the source and are transcribed as printed. Each header cell also carries a product photograph and a fuel or voltage badge ("NATURAL GAS", "208 VOLTS", "208/240 VOLTS"); neither is transcribed.

The power levels of the griddles shown above align with our sources. The rated input values for the two 36-inch models match very closely to ASHRAE, so we can once again feel confident and use the rated input values from ASHRAE as our assumptions in the model. Therefore, our gas and electric griddles are modeled as 90,000 Btu/h and 58,400 Btu/h, respectively.

The ENERGY STAR Product Finder [14] does not report cooking efficiency for griddles, but it does give idle energy use per square foot. Three products for each fuel type were selected, and the average idle energy per square foot was calculated. For gas, the average was 2492 Btu/h/ft 2 , and for electric, the average was 869 Btu/h/ft 2 , meaning the idle conditions of the electric griddle are 65% more efficient than the gas griddle. The rated power values selected of 90,000 Btu/h and 58,400 Btu/h represent an electric griddle that is 35% more efficient than its gas counterpart, based on their rated conditions. This is a more conservative assumption than the ENERGY

STAR idle power/ft 2 values suggest, but the ENERGY STAR products do not report rated power conditions. Therefore, it is difficult to conclude whether the rated power and idle power efficiency differences can be extrapolated. Without additional data to compare, we will leave our rated power assumptions as is.

