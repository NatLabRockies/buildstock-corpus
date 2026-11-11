<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/94463.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/94463.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/94463.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/94463.md | section: Electric Vehicle Stock Characterization | lines: 213-249 -->
## Electric Vehicle Stock Characterization

Included in the baseline ResStock inputs are probability distributions that describe the likelihood of EV-related attributes being assigned to dwelling units. These EV-related inputs are part of ResStock's broader stock characterization process, which defines detailed building, occupant, and technology characteristics for the U.S. residential building stock (see Section 3 Reyna et al. [2025] for more detail). EV input distributions are sampled to produce EV ownership profiles for each building model. The baseline of ResStock assigns each dwelling unit a value for EV ownership, the at-home charging fraction, the vehicle type that provides the battery capacity and efficiency, and the VMT per year. If a dwelling unit has an EV, an EV charger is applied, and its power draw is determined based on the charger level. Plug-in hybrid electric vehicles are not currently modeled in ResStock.

The ResStock EV implementation draws data from the TEMPO ™  model (Muratori et al. 2021), EIA RECS 2020 (U.S. EIA 2020), the National Household Travel Survey (Federal Highway Administration 2022), vehicle registration data from Experian 1 , the No Place Like Home study (Ge et al. 2021), and the Autonomie model 2 . The distributions of these options reflect 2023 saturation levels of EV technology and operation in the United States, ensuring that EV-related measures capture expected diversity 3 . All dwelling units are sampled with percentage of vehicle charge at home, a vehicle type, and the VMT. These options are only relevant in the baseline for dwelling units with an EV but are used to define vehicle and driving characteristics for dwelling units that adopt an EV in this measure. Table 1 describes the ResStock characteristics, or dependencies, that influence the distribution of EV-related options. The dependencies shown directly influence the EV inputs, but the dependencies themselves also have upstream inputs, which have an indirect influence on EV characteristics.

[1  For more information, visit https://www.experian.com/automotive/auto-vehicle-data.](https://www.experian.com/automotive/auto-vehicle-data)

[2  For more information, visit https://www.anl.gov/taps/autonomie-vehicle-system-simulation-tool.](https://www.anl.gov/taps/autonomie-vehicle-system-simulation-tool)

3 More information can be found in Section 3 of Speake et al. (2025)

Table 1. Baseline EV ResStock Input Distribution Files and the Dependencies That Inform Option Distributions

| ResStock Input File        | Dependencies                                                                  |
|----------------------------|-------------------------------------------------------------------------------|
| Electric Vehicle Ownership | Public Use Microdata Area, federal poverty level (FPL), building type, tenure |
| Electric Vehicle Charger   | EV ownership, FPL, building type, tenure                                      |
| Electric Vehicle Battery   | None                                                                          |
| Annual Miles Driven        | None                                                                          |
| Home Charging Fraction     | FPL, building type                                                            |

Upstream dependencies are important for accurately reflecting the probabilities of EV ownership and operation across households. Figure 2 illustrates how these dependencies shape the baseline distributions for 'EV Ownership,' highlighting the significant variation that can occur across regions, housing characteristics, and demographics. California has a relatively high rate of EV adoption and diversity in housing characteristics and demographics, which makes underlying trends easier to observe and interpret. We see a strong correlation between higher EV ownership rates and urban areas, home ownership, and single-family detached housing.

Figure 2. The percentage of EV ownership among households at the 400% FPL for different building types and tenures. Maps are disaggregated by Public Use Microdata Area in California.

<!-- figure described by overlay: resstock_resstock_amy2018_2025_release_1/upgrade_measures/measure_pdfs/94463.yaml
     source: 94463_images/image_000003_3ea357076c14b5d489fa921bd50c9b1f6e143d4af5ed52e71b646ab95283ec7c.png
     method: vision-description
     described: 2026-11-11 -->

![Four maps of California shaded by household electric vehicle ownership, by building type and tenure](94463_images/image_000003_3ea357076c14b5d489fa921bd50c9b1f6e143d4af5ed52e71b646ab95283ec7c.png)

Figure 2: four maps of California divided into Public Use Microdata Areas, one each for single-family detached owners, single-family detached renters, multifamily 5+ units owners and multifamily 5+ units renters. Areas are shaded by household battery EV share on a scale from 0.23% to 19.24%. The owner map for single-family detached homes is the darkest, mostly in coastal and urban areas; the other three are near the low end throughout.

SFD = single-family detached; MF 5units+ = multi-family 5+ units; BEV = battery electric vehicle

