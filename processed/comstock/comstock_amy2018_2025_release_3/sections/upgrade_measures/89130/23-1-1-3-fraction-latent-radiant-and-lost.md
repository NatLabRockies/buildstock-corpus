<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89130.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89130.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89130.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/89130.md | section: 1.1.3 Fraction Latent, Radiant, and Lost | lines: 572-582 -->
## 1.1.3 Fraction Latent, Radiant, and Lost

Gas and electric equipment release heat differently, which affects zone heating and cooling loads. This heat is divided into four fractions that must add up to one: fraction convective, fraction latent, fraction radiant, and fraction lost. As defined by the EnergyPlus ®  Input Output Reference Documentation [18]:

- Fraction latent: the amount of latent heat given off by electric equipment in a zone
- Fraction radiant: the amount of long-wave radiant heat being given off by electric equipment in a zone
- Fraction lost: the amount of 'lost' heat being given off by electric equipment in a zone (in this case, this refers to heat that is vented to the atmosphere through the hood)
- Fraction convective: the amount of heat from electric equipment transferred by convection to the zone air.

The user defines the fractions latent, radiant, and lost in the model, and then the fraction convective can be calculated as follows:

