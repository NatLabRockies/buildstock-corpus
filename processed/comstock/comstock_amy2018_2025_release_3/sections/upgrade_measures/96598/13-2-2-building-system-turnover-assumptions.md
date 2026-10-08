<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/96598.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96598.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96598.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/96598.md | section: 2.2  Building System Turnover Assumptions | lines: 287-303 -->
## 2.2  Building System Turnover Assumptions

The original, or as-built, energy code assigned to a building in ComStock directly informs the performance of the building systems, such as HVAC efficiency or insulation levels. The as-built code in the model can be updated for different building systems based on equipment turnover and effective useful life (EUL) assumptions. We assume that all major building systems are installed when the building is constructed and that they are replaced periodically over the lifespan of the building. This process modifies the energy code associated with that building system, and therefore the system could be upgraded to a more efficient system if the energy code at the time of replacement is better than the as-built energy code. The metric commonly used by industry to describe the lifespan of a building system or a piece of equipment is the EUL. In real buildings, replacements might be made because of equipment failure, building remodeling, or energy efficiency upgrades. In the ComStock model, we make informed assumptions regarding how often building systems are replaced; the assumptions are based on a combination of internal research and the California Public Utilities Commission DEER model [16]. Although the EUL of different systems can vary across the country, the DEER studies were found to be the best available. Table 2 details the EUL assumptions in ComStock. For more details about this methodology, see the ComStock Reference Documentation [11].

Table 2. EUL of Major Commercial Building Systems in ComStock

| Major Building System                       |   EUL (Years) |
|---------------------------------------------|---------------|
| Envelope-wall insulation                    |           200 |
| Envelope-roof insulation                    |           200 |
| Envelope-windows                            |            70 |
| Exterior lighting                           |            15 |
| Interior lighting                           |            10 |
| HVAC                                        |            20 |
| Service water heating                       |            15 |
| Interior equipment (plug-and-process loads) |            15 |

