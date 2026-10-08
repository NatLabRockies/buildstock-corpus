<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89239.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89239.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89239.pdf | corpus_version: 43ae2d4 | corpus_path: upgrade_measures/measure_pdfs/89239.md | section: 2  ComStock Baseline Approach | lines: 242-269 -->
## 2  ComStock Baseline Approach

Of the buildings represented in ComStock™, about 17% are served by hydronic HVAC systems (excluding buildings served by district thermal energy systems, which are not in the scope of this measure). These system types are listed in Table 1, along with a classification of whether the hydronic systems provide heating only, cooling only, or both heating and cooling. This measure modifies the existing HVAC system to create a system served by central water-to-water heat pumps with a ground loop serving as the source.

This measure is not intended to apply to buildings served by district energy (heating hot water or chilled water) systems, as this retrofit is intended to represent the installation of a ground heat exchanger to serve a single building's load. This measure is also not intended to apply to buildings that are heated (or cooled) only, since the resulting extreme load imbalance would negatively affect the performance of a ground heat exchanger over time [4]. However, as long as a given heating or cooling capability exists in the baseline, it will be replaced with a hydronic system in this measure. This measure sizes the ground heat exchanger in a way that seeks to avoid the potential for a significant (greater than 20%) load imbalance. Additionally, this measure does not apply to systems with hot water baseboard radiators, which are generally not suited to the reduction in supply water temperature for compatibility with water-source heat pumps currently available in the United States.

In ComStock, buildings with hydronic systems providing only cooling usually consist of an air handler or fan coil unit equipped with chilled water coils, and heating is supplied through gas or electric coils. Buildings with hydronic systems providing only heating generally have direct expansion cooling and hot water coils in radiators, fan coils, or air handling units. Systems modeled with hydronic heating and cooling use hydronic coils in air handling units, sometimes with a separate dedicated outdoor air system (DOAS). In ComStock, all hydronic heating systems are currently configured with a set point of 180°F, and hydronic cooling systems are configured with a set point of 44°F.

Table 1. Classification of Building-Level Hydronic HVAC System Types in ComStock

| System                                                                   | Hydronic System Classification   |
|--------------------------------------------------------------------------|----------------------------------|
| Variable air volume (VAV) chiller with packaged fan- powered (PFP) boxes | Cooling only                     |
| VAV air-cooled chiller with PFP boxes                                    | Cooling only                     |
| DOAS with fan coil chiller with baseboard electric                       | Cooling only                     |
| DOAS with fan coil chiller with baseboard electric                       | Cooling only                     |
| Packaged variable air volume (PVAV) with gas boiler reheat               | Heating only                     |
| Packaged single-zone air conditioner (PSZ-AC) with gas boiler            | Heating only                     |
| Packaged terminal air conditioner (PTAC) with gas boiler                 | Heating only                     |
| PVAV with gas heat with electric reheat                                  | Heating only                     |
| Baseboard gas boiler 1                                                   | Heating only                     |
| Direct evap coolers with baseboard gas boiler 1                          | Heating only                     |
| DOAS with water-source heat pumps with cooling tower and boiler          | Both                             |
| DOAS with fan coil chiller with boiler                                   | Both                             |
| DOAS with fan coil air-cooled chiller with boiler                        | Both                             |
| VAV chiller with gas boiler reheat                                       | Both                             |
| VAV air-cooled chiller with gas boiler reheat                            | Both                             |

