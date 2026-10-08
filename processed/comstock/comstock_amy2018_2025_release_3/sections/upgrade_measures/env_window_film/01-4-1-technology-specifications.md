<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_window_film.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_window_film.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_window_film.html | corpus_version: 0396270 | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_window_film.md | section: 4.1.  Technology Specifications | lines: 103-282 -->
## 4.1.  Technology Specifications

It is possible to achieve a wide range of thermal and optical performances with an IGU that is composed of glass, spacer, gas, frame, and with and without window film. Because of the differences in climates across the United States, it is not desirable to drive the performance of the IGU in one direction (i.e., tradeoff is required); warmer climates with high cooling requirements may want lower SHGC to avoid overheating, while higher SHGC may be preferable to allow beneficial solar gain in colder climates. As a starting point for the target IGU performance, the performance properties from ASHRAE’s *Achieving Zero Energy: Advanced Energy Design Guide (AEDG) for Small to Medium Office Buildings* [3] are documented, as shown in Table 1.

Table 1. Overall Assembly Performance Characteristics by Climate Zone

| **Climate zone**         | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| **U-factor (Btu/hr-ft2-°F)** | 0.48  | 0.48  | 0.43  | 0.40  | 0.34  | 0.34  | 0.32  | 0.28  | 0.25  |
| **SHGC (-)**                 | 0.21  | 0.22  | 0.24  | 0.24  | 0.34  | 0.36  | 0.36  | 0.38  | 0.38  |
| **VLT/SHGC (-)**             | 1.10  | 1.10  | 1.10  | 1.10  | 1.10  | 1.10  | 1.10  | 1.10  | 1.10  |

To understand the expected performance of the total assembly, combinations of existing windows and window films are modeled using LBNL’s WINDOW (v7.8) and Optics (v6) software, shown in Figure 5. Table 2 includes (1) performance (e.g., U-factor, SHGC, and visual light transmittance [VLT]) improvements between ComStock baseline windows and windows with window films; and (2) performance comparison against AEDG targets, with respect to different climate zones. Several window film products were selected from a larger pool (shown in Figure 3) based on the emphasis on thermal performance improvements rather than visual performance improvements, as this analysis is focused on the energy savings potential.

![](media/da1e7d6f9b520c4ad0d2b13322635bb0.png)

Figure 5. Workflow of creating new glass, glazing systems, and windows with window films

Table 2. Performance Range Baseline Windows With Window Films

<!-- table recovered from media/ec67b834b3070ddae5461a3e344bc230.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_window_film.yaml
     method: vision-transcription -->

**Baseline window configuration**

| Config | Pane | Low-E | Glazing | Frame |
|---|---|---|---|---|
| 1 | single | No | Clear | Aluminum |
| 2 | single | No | Tinted/Reflective | Aluminum |
| 3 | single | No | Clear | Wood |
| 4 | single | No | Tinted/Reflective | Wood |
| 5 | Double | No | Clear | Aluminum |
| 6 | Double | No | Tinted/Reflective | Aluminum |
| 7 | Double | Yes | Clear | Aluminum |
| 8 | Double | Yes | Clear | Aluminum with thermal break |
| 9 | Double | Yes | Tinted/Reflective | Aluminum |
| 10 | Double | Yes | Tinted/Reflective | Aluminum with thermal break |
| 11 | Triple | Yes | Clear | Aluminum with thermal break |
| 12 | Triple | Yes | Tinted/Reflective | Aluminum with thermal break |

**Baseline compared to AEDG ZE (one value per configuration; the source repeats it on every film row of the configuration)**

| Config | U-factor within 10%? (CZ 1, 2, 3) | U-factor within 10%? (CZ 4, 5, 6) | U-factor within 10%? (CZ 7, 8) | SHGC within 10%? (CZ 1, 2, 3) | SHGC within 10%? (CZ 4, 5, 6) | SHGC within 10%? (CZ 7, 8) |
|---|---|---|---|---|---|---|
| 1 | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE |
| 2 | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE |
| 3 | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE |
| 4 | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE |
| 5 | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE |
| 6 | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE |
| 7 | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE |
| 8 | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| 9 | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| 10 | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| 11 | TRUE | TRUE | FALSE | FALSE | TRUE | TRUE |
| 12 | TRUE | TRUE | FALSE | TRUE | TRUE | TRUE |

**Config 1 (single pane, low-E No, Clear glazing, Aluminum frame): window film retrofit options, retrofit compared to baseline, and retrofit compared to AEDG ZE**

| Film Position | Film Product | Retrofit vs baseline U-factor | Retrofit vs baseline SHGC | U-factor within 10%? (CZ 1, 2, 3) | U-factor within 10%? (CZ 4, 5, 6) | U-factor within 10%? (CZ 7, 8) | SHGC within 10%? (CZ 1, 2, 3) | SHGC within 10%? (CZ 4, 5, 6) | SHGC within 10%? (CZ 7, 8) |
|---|---|---|---|---|---|---|---|---|---|
| Interior | Affinity 15 | 1% | 68% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Affinity 30 | 3% | 49% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Interior | Low e 20 | 18% | 67% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Low e 35 | 14% | 68% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Exterior | Prestige exterior 20 | 0% | 55% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Exterior | Prestige exterior 70 | 0% | 39% | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE |

**Config 2 (single pane, low-E No, Tinted/Reflective glazing, Aluminum frame): window film retrofit options, retrofit compared to baseline, and retrofit compared to AEDG ZE**

| Film Position | Film Product | Retrofit vs baseline U-factor | Retrofit vs baseline SHGC | U-factor within 10%? (CZ 1, 2, 3) | U-factor within 10%? (CZ 4, 5, 6) | U-factor within 10%? (CZ 7, 8) | SHGC within 10%? (CZ 1, 2, 3) | SHGC within 10%? (CZ 4, 5, 6) | SHGC within 10%? (CZ 7, 8) |
|---|---|---|---|---|---|---|---|---|---|
| Interior | Affinity 15 | 1% | 51% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Interior | Affinity 30 | 3% | 39% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Interior | Low e 20 | 18% | 55% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Interior | Low e 35 | 14% | 54% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Exterior | Prestige exterior 20 | 0% | 48% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Exterior | Prestige exterior 70 | 0% | 35% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |

**Config 3 (single pane, low-E No, Clear glazing, Wood frame): window film retrofit options, retrofit compared to baseline, and retrofit compared to AEDG ZE**

| Film Position | Film Product | Retrofit vs baseline U-factor | Retrofit vs baseline SHGC | U-factor within 10%? (CZ 1, 2, 3) | U-factor within 10%? (CZ 4, 5, 6) | U-factor within 10%? (CZ 7, 8) | SHGC within 10%? (CZ 1, 2, 3) | SHGC within 10%? (CZ 4, 5, 6) | SHGC within 10%? (CZ 7, 8) |
|---|---|---|---|---|---|---|---|---|---|
| Interior | Affinity 15 | 1% | 71% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Affinity 30 | 4% | 51% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Interior | Low e 20 | 22% | 70% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Low e 35 | 17% | 71% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Exterior | Prestige exterior 20 | 0% | 58% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Exterior | Prestige exterior 70 | 0% | 41% | FALSE | FALSE | FALSE | FALSE | FALSE | TRUE |

**Config 4 (single pane, low-E No, Tinted/Reflective glazing, Wood frame): window film retrofit options, retrofit compared to baseline, and retrofit compared to AEDG ZE**

| Film Position | Film Product | Retrofit vs baseline U-factor | Retrofit vs baseline SHGC | U-factor within 10%? (CZ 1, 2, 3) | U-factor within 10%? (CZ 4, 5, 6) | U-factor within 10%? (CZ 7, 8) | SHGC within 10%? (CZ 1, 2, 3) | SHGC within 10%? (CZ 4, 5, 6) | SHGC within 10%? (CZ 7, 8) |
|---|---|---|---|---|---|---|---|---|---|
| Interior | Affinity 15 | 1% | 54% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Affinity 30 | 4% | 41% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Interior | Low e 20 | 22% | 58% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Low e 35 | 17% | 57% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Exterior | Prestige exterior 20 | 0% | 51% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Exterior | Prestige exterior 70 | 0% | 37% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |

**Config 5 (Double pane, low-E No, Clear glazing, Aluminum frame): window film retrofit options, retrofit compared to baseline, and retrofit compared to AEDG ZE**

| Film Position | Film Product | Retrofit vs baseline U-factor | Retrofit vs baseline SHGC | U-factor within 10%? (CZ 1, 2, 3) | U-factor within 10%? (CZ 4, 5, 6) | U-factor within 10%? (CZ 7, 8) | SHGC within 10%? (CZ 1, 2, 3) | SHGC within 10%? (CZ 4, 5, 6) | SHGC within 10%? (CZ 7, 8) |
|---|---|---|---|---|---|---|---|---|---|
| Interior | Affinity 15 | 0% | 49% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Interior | Affinity 30 | 1% | 31% | FALSE | FALSE | FALSE | FALSE | FALSE | FALSE |
| Interior | Low e 20 | 8% | 50% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Interior | Low e 35 | 6% | 53% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Exterior | Prestige exterior 20 | 0% | 62% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Exterior | Prestige exterior 70 | 0% | 42% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |

**Config 6 (Double pane, low-E No, Tinted/Reflective glazing, Aluminum frame): window film retrofit options, retrofit compared to baseline, and retrofit compared to AEDG ZE**

| Film Position | Film Product | Retrofit vs baseline U-factor | Retrofit vs baseline SHGC | U-factor within 10%? (CZ 1, 2, 3) | U-factor within 10%? (CZ 4, 5, 6) | U-factor within 10%? (CZ 7, 8) | SHGC within 10%? (CZ 1, 2, 3) | SHGC within 10%? (CZ 4, 5, 6) | SHGC within 10%? (CZ 7, 8) |
|---|---|---|---|---|---|---|---|---|---|
| Interior | Affinity 15 | 0% | 44% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Interior | Affinity 30 | 1% | 29% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Interior | Low e 20 | 8% | 46% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Interior | Low e 35 | 6% | 49% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Exterior | Prestige exterior 20 | 0% | 56% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Exterior | Prestige exterior 70 | 0% | 39% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |

**Config 7 (Double pane, low-E Yes, Clear glazing, Aluminum frame): window film retrofit options, retrofit compared to baseline, and retrofit compared to AEDG ZE**

| Film Position | Film Product | Retrofit vs baseline U-factor | Retrofit vs baseline SHGC | U-factor within 10%? (CZ 1, 2, 3) | U-factor within 10%? (CZ 4, 5, 6) | U-factor within 10%? (CZ 7, 8) | SHGC within 10%? (CZ 1, 2, 3) | SHGC within 10%? (CZ 4, 5, 6) | SHGC within 10%? (CZ 7, 8) |
|---|---|---|---|---|---|---|---|---|---|
| Interior | Affinity 15 | 0% | 39% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Affinity 30 | 1% | 20% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Interior | Low e 20 | 4% | 37% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Low e 35 | 3% | 41% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Exterior | Prestige exterior 20 | 0% | 60% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Exterior | Prestige exterior 70 | 0% | 25% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |

**Config 8 (Double pane, low-E Yes, Clear glazing, Aluminum with thermal break frame): window film retrofit options, retrofit compared to baseline, and retrofit compared to AEDG ZE**

| Film Position | Film Product | Retrofit vs baseline U-factor | Retrofit vs baseline SHGC | U-factor within 10%? (CZ 1, 2, 3) | U-factor within 10%? (CZ 4, 5, 6) | U-factor within 10%? (CZ 7, 8) | SHGC within 10%? (CZ 1, 2, 3) | SHGC within 10%? (CZ 4, 5, 6) | SHGC within 10%? (CZ 7, 8) |
|---|---|---|---|---|---|---|---|---|---|
| Interior | Affinity 15 | 0% | 39% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Affinity 30 | 1% | 20% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |
| Interior | Low e 20 | 5% | 38% | TRUE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Low e 35 | 4% | 42% | TRUE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Exterior | Prestige exterior 20 | 0% | 61% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Exterior | Prestige exterior 70 | 0% | 25% | FALSE | FALSE | FALSE | FALSE | TRUE | TRUE |

**Config 9 (Double pane, low-E Yes, Tinted/Reflective glazing, Aluminum frame): window film retrofit options, retrofit compared to baseline, and retrofit compared to AEDG ZE**

| Film Position | Film Product | Retrofit vs baseline U-factor | Retrofit vs baseline SHGC | U-factor within 10%? (CZ 1, 2, 3) | U-factor within 10%? (CZ 4, 5, 6) | U-factor within 10%? (CZ 7, 8) | SHGC within 10%? (CZ 1, 2, 3) | SHGC within 10%? (CZ 4, 5, 6) | SHGC within 10%? (CZ 7, 8) |
|---|---|---|---|---|---|---|---|---|---|
| Interior | Affinity 15 | 0% | 32% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Affinity 30 | 1% | 17% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Low e 20 | 4% | 32% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Low e 35 | 3% | 35% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Exterior | Prestige exterior 20 | 0% | 53% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Exterior | Prestige exterior 70 | 0% | 22% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |

**Config 10 (Double pane, low-E Yes, Tinted/Reflective glazing, Aluminum with thermal break frame): window film retrofit options, retrofit compared to baseline, and retrofit compared to AEDG ZE**

| Film Position | Film Product | Retrofit vs baseline U-factor | Retrofit vs baseline SHGC | U-factor within 10%? (CZ 1, 2, 3) | U-factor within 10%? (CZ 4, 5, 6) | U-factor within 10%? (CZ 7, 8) | SHGC within 10%? (CZ 1, 2, 3) | SHGC within 10%? (CZ 4, 5, 6) | SHGC within 10%? (CZ 7, 8) |
|---|---|---|---|---|---|---|---|---|---|
| Interior | Affinity 15 | 0% | 34% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Affinity 30 | 1% | 17% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Low e 20 | 5% | 33% | TRUE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Interior | Low e 35 | 3% | 36% | TRUE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Exterior | Prestige exterior 20 | 0% | 55% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |
| Exterior | Prestige exterior 70 | 0% | 23% | FALSE | FALSE | FALSE | TRUE | TRUE | TRUE |

**Configs 11 and 12 (Triple pane): no window film retrofit options, so every retrofit column is n/a**

| Config | Film Position | Film Product | Retrofit vs baseline U-factor | Retrofit vs baseline SHGC | U-factor within 10%? (CZ 1, 2, 3) | U-factor within 10%? (CZ 4, 5, 6) | U-factor within 10%? (CZ 7, 8) | SHGC within 10%? (CZ 1, 2, 3) | SHGC within 10%? (CZ 4, 5, 6) | SHGC within 10%? (CZ 7, 8) |
|---|---|---|---|---|---|---|---|---|---|---|
| 11 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 12 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

As shown in the two “retrofit compared to baseline” columns in Table 2, U-factor improvements (i.e., reductions) vary from 0% to 22%, and SHGC improvements (i.e., reductions) vary from 17% to 71% when applying window films on different baseline windows. As expected, (1) relative improvements with window films are more significant on SHGC rather than on U-factor (while low-E coated window films still improve U-factor) and (2) higher SHGC improvements (colored in blue) are mostly seen in lower-performing windows (e.g., clear single pane).

The “baseline compared to AEDG ZE” and “retrofit compared to AEDG ZE” columns in Table 2 indicate whether the performances (i.e., U-factor and SHGC) of either baseline windows or windows with films are close (within 10%) to the target performance suggested by the AEDG shown in Table 1. As shown in Table 2, baseline triple pane windows are mostly (besides one or two extreme cases for U-factor and SHGC) within AEDG performance targets, thus, they do not need window films to meet thermal performance targets. Also, compared to SHGC improvements, attaching window films does not provide enough U-factor improvement to allow the retrofitted windows to meet the AEDG targets.

While many low-E coated double pane baseline windows perform well (in climate zones 4, 5, 6, 7, and 8) in terms of SHGC compared to AEDG targets, attaching a window film on the exterior side (e.g., Prestige Exterior series) of the window can still achieve significant SHGC reduction compared to the baseline windows, meeting the AEDG targets for climate zones 1, 2, and 3. While the material and labor price of exterior films can be higher than interior films and maintenance of exterior films (i.e., exposed to weather) can include additional effort, it may be a good option for hot climates with high cooling loads in terms of energy performance.

