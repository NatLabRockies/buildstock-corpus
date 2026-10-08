<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/96598.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96598.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96598.pdf | corpus_version: fadc83e | corpus_path: upgrade_measures/measure_pdfs/96598.md | section: 2.3.3  Windows | lines: 518-559 -->
## 2.3.3  Windows

Unlike walls and roofs, which are simply modeled to meet the R-value or U-value required by the building's energy code, windows in the ComStock baseline are modeled based on marketrepresentative product distributions, reflecting the realistic performance characteristics of actual window technologies rather than idealized code-minimum values. ComStock models 12 different window assemblies, whose properties are based on commercially available products, as described in a collaborative study by Lawrence Berkeley National Laboratory and the National Laboratory of the Rockies (previously National Renewable Energy Laboratory) [18]. Window performance in ComStock is defined by three metrics: U-value, SHGC, and visible light transmittance (VLT). The 12 window constructions modeled in ComStock, along with their performance characteristics, are shown in Table 7 [11].

Table 7. Window Constructions and Associated Performance Characteristics Modeled in ComStock.

Content of table derived from [11]

| Panes   | Glazing Type      | Frame Material              | Low-e Coating   |   U-Value IP (Btu/h-ft 2 -F) |   U-Value SI (W/m 2 -K) |   SHGC |   VLT |
|---------|-------------------|-----------------------------|-----------------|------------------------------|-------------------------|--------|-------|
| Single  | Clear             | Aluminum                    | No              |                         1.01 |                   6.689 |  0.744 | 0.754 |
| Single  | Tinted/reflective | Aluminum                    | No              |                         1.01 |                   6.689 |  0.579 | 0.455 |
| Single  | Clear             | Wood                        | No              |                         0.91 |                   5.167 |  0.683 | 0.723 |
| Single  | Tinted/reflective | Wood                        | No              |                         0.91 |                   5.167 |  0.525 | 0.436 |
| Double  | Clear             | Aluminum                    | No              |                        0.746 |                   4.236 |  0.646 | 0.671 |
| Double  | Tinted/reflective | Aluminum                    | No              |                        0.749 |                   4.253 |  0.484 | 0.411 |
| Double  | Clear             | Aluminum                    | Yes             |                        0.559 |                   3.174 |  0.386 | 0.591 |
| Double  | Clear             | Aluminum with thermal break | Yes             |                        0.499 |                   2.833 |  0.378 | 0.591 |
| Double  | Tinted/reflective | Aluminum                    | Yes             |                        0.557 |                   3.163 |  0.274 | 0.359 |
| Double  | Tinted/reflective | Aluminum with thermal break | Yes             |                        0.496 |                   2.816 |  0.266 | 0.359 |
| Triple  | Clear             | Aluminum with thermal break | Yes             |                          0.3 |                   1.703 |  0.328 | 0.527 |
| Triple  | Tinted/reflective | Aluminum with thermal break | Yes             |                        0.299 |                   1.698 |  0.224 |  0.32 |

These window constructions and performance characteristics were developed after thorough analysis of several commercial building window databases that characterize existing installations. WINDOW modeling software was used to set the U-value, SHGC, and VLT associated with each window construction [19]. More details about this methodology can be found in the ComStock Reference Documentation [11] and the commercial window market report study [18].

The prevalence of each window construction was determined to be dependent on the climate zone and the energy code of the building. Again, ComStock assumes a 70-year lifespan for windows, so some of the oldest buildings in the stock might assume that the window energy code template was updated since construction; however, most buildings are still modeled with their original windows.

Building energy codes such as ASHRAE 90.1 define a maximum U-value and a maximum SHGC as the window performance characteristics for code compliance. For each combination of climate zone and energy code, we determined which window constructions most closely complied with code. (For example, although triple-pane windows technically comply with all energy code templates based on U-value and SHGC, it is not realistic to assume that buildings used triple-pane windows to align with pre-2004 energy code requirements.) Each combination of climate and energy code included anywhere from 2-12 window constructions that met those criteria. A probability distribution (based on the data on existing installations) was incorporated in the sampling to assign a window construction to each model.

Figure 3 shows the breakdown for floor area by window construction type for each climate zone. In general, the warmer climate zones have a larger prevalence of single-pane windows than the colder climates. This is based on the datasets of existing window installations as well as energy code requirements, which typically become more aggressive in colder climate zones. As of the ComStock 2025 Release 2 dataset [20], 49% of the baseline stock received single-pane windows, 51% received double-pane windows, and less than 1% received triple-pane windows. See the ComStock Reference Documentation for more information [11].

Figure 3. Breakdown of window construction by Climate Zone in the ComStock baseline. Data from ComStock 2025 Release 2 [20]

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/96598.yaml
     source: 96598_images/image_000004_e9fca371fb9cb26cf40c812bc8d64a88c12d29d901c72aacac3fff9d0bb6d82d.png
     method: vision-description
     described: 2026-08-21 -->

![Stacked bar chart of percent of square footage by window construction type for each climate zone](96598_images/image_000004_e9fca371fb9cb26cf40c812bc8d64a88c12d29d901c72aacac3fff9d0bb6d82d.png)

Figure 3: 100% stacked horizontal bar chart of the percent of ComStock square footage by window construction type, one row per climate zone, x-axis 0 to 100%, with a 12-entry legend from triple-pane low-e to single-pane clear. Warmer zones carry more single-pane glazing. Section 2.3.3 reports 49% single-pane, 51% double-pane and under 1% triple-pane stock-wide; Table 7 gives the assembly properties.

