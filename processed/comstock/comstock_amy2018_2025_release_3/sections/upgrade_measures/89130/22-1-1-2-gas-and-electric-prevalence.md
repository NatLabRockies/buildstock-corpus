<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89130.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89130.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89130.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/89130.md | section: 1.1.2 Gas and Electric Prevalence | lines: 553-571 -->
## 1.1.2 Gas and Electric Prevalence

We assume that the baseline model already has some prevalence of electric cooking equipment. To determine the breakdown, we used percentages from a 2015 DOE study [8]. This study used data from a 1993 study called 'Characterization of Commercial Appliances,' which estimated market saturation of gas and electric cooking equipment. These numbers were then extrapolated to the present day using scaling factors based on CBECS and other sources. While these numbers may not be perfect, in the absence of a more recent study on the prevalence of gas and electric cooking equipment, we use the assumptions from Table 13.

Table 13. Prevalence of Gas and Electric Equipment by Appliance [8]

| Appliance   |   Total Installed Base (thousands) |   Gas Installed Base (thousands) |   Electric Installed Base (thousands) |   Gas Percentage |   Electric Percentage |
|-------------|------------------------------------|----------------------------------|---------------------------------------|------------------|-----------------------|
| Broilers    |                                380 |                              346 |                                    34 |               91 |                     9 |
| Fryers      |                              1,857 |                            1,077 |                                   780 |               58 |                    42 |
| Griddles    |                                893 |                              447 |                                   447 |               50 |                    50 |
| Ovens       |                              1,604 |                              882 |                                   722 |               55 |                    45 |
| Ranges      |                                725 |                              660 |                                    65 |               91 |                     9 |
| Steamers    |                                272 |                               90 |                                   182 |               33 |                    67 |

The percentages of gas and electric equipment from Table 13 were incorporated into the ComStock baseline model through ComStock's sampling processes [17]. For each type of equipment, a building is assigned either the gas or electric version of the appliance, and the rated input power and heat gain fractions are assigned in the model. Buildings in the baseline can have a mixture of gas and electric appliances.

In addition to the fuel type, the sampling process also determines the quantity of each appliance, which is based on the building type and kitchen square footage. Section 2 describes how this was done in more detail, and the ComStock Reference Documentation provides the full explanation of this methodology [17].

