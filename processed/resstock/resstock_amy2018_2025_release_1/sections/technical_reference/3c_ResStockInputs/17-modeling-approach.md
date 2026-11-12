<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Modeling Approach | lines: 2452-2469 -->
## Modeling Approach

Five ResStock input files provide the options and arguments for lighting, but only two are currently in use:

- Lighting—Electric lighting: interior, exterior, and garage

- Misc Gas Lighting—Exterior natural gas lighting

- Holiday Lighting—Not used

- Lighting Interior Use—Not used

- Lighting Other Use—Not used.

ResStock models three lighting technologies: light-emitting diodes (LEDs), incandescent bulbs, and compact florescent (CFL) bulbs. The technologies are represented as a fraction of the number of light bulbs in the home covered by each technology.

Separately, outside these input files, ResStock provides schedules for lighting based on the occupancy schedule generator (Section “Schedule Creation”).

