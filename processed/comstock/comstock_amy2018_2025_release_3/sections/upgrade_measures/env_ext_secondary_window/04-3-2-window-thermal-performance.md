<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | docs/upgrade_measures/env_ext_secondary_window.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/upgrade_measures/env_ext_secondary_window.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/upgrade_measures/env_ext_secondary_window.html | corpus_version: fadc83e | corpus_path: upgrade_measures/unpublished_docs/upgrade_measures/env_ext_secondary_window.md | section: 3.2  Window Thermal Performance | lines: 179-423 -->
## 3.2  Window Thermal Performance

Once the 12 new window constructions were determined, a team from LBNL's Windows and Daylighting Group used the WINDOW program to assign thermal performance properties to each construction. SimpleGlazing objects in EnergyPlus™ were chosen to represent windows to reduce complexity. This choice also simplifies the process of applying upgrades, because all fenestration objects in the baseline models use the same object type. The inputs for the SimpleGlazing object are U-factor, SHGC, and VLT. For each window configuration, LBNL assigned a frame ID and window ID from the WINDOW database. They also filled in the respective U-factors, SHGCs, and VLTs, which are shown in Table 5.

Table 5. Window Thermal Performance

<!-- table recovered from ./media/fd012e1d-53a4-4b03-b432-a24f61cb469e.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_ext_secondary_window.yaml
     method: vision-transcription -->

| Number of Panes | Glazing Type | Frame Material | Low-E Coating | Frame ID | WINDOW ID | U-Factor IP (Btu/h-ft2-F) | SHGC | VLT |
|---|---|---|---|---|---|---|---|---|
| Single | Clear | Aluminum | No | 5 | 2000 | 1.178 | 0.744 | 0.754 |
| Single | Tinted/Reflective | Aluminum | No | 5 | 2001 | 1.178 | 0.579 | 0.455 |
| Single | Clear | Wood | No | 9 | 2002 | 0.910 | 0.683 | 0.723 |
| Single | Tinted/Reflective | Wood | No | 9 | 2003 | 0.910 | 0.525 | 0.436 |
| Double | Clear | Aluminum | No | 5 | 2004 | 0.746 | 0.646 | 0.671 |
| Double | Tinted/Reflective | Aluminum | No | 5 | 2005 | 0.749 | 0.484 | 0.411 |
| Double | Clear | Aluminum | Yes | 5 | 2006 | 0.559 | 0.386 | 0.591 |
| Double | Clear | Aluminum With Thermal Break | Yes | 7 | 2007 | 0.499 | 0.378 | 0.591 |
| Double | Tinted/Reflective | Aluminum | Yes | 5 | 2008 | 0.557 | 0.274 | 0.359 |
| Double | Tinted/Reflective | Aluminum With Thermal Break | Yes | 7 | 2009 | 0.496 | 0.266 | 0.359 |
| Triple | Clear | Aluminum With Thermal Break | Yes | 8 | 2010 | 0.300 | 0.328 | 0.527 |
| Triple | Tinted/Reflective | Aluminum With Thermal Break | Yes | 8 | 2011 | 0.299 | 0.224 | 0.320 |

The U-factors originally ranged from U-1.18 (Btu/hr-ft2-°F) for the worst-performing single-pane window to U-0.30 (Btu/hr-ft2-°F) for the best-performing triple-pane window. As mentioned earlier in this section, the maximum U-factor that EnergyPlus can model with a simple glazing object is U-1.02 (Btu/hr-ft2-°F), which is governed by the limitations of a 2D heat transfer model when interior and exterior air films are included. Therefore, we adjusted the U-factor for the first two single-pane windows to be U-1.02 (Btu/hr-ft2-°F) rather than U-1.18 (Btu/hr-ft2-°F). This allowed these windows to be modeled in ComStock. This results in a slight overestimate of the thermal performance of single-pane windows.

# 4.  Modeling Approach

There are many different window configurations available from manufacturers, and multiple performance levels have been observed in the field. Therefore, it is possible to achieve a range of thermal and optical characteristics for the glazing portion of the window assembly. Because of the differences in climate across the United States, it is not desirable to have a single performance value; warmer climates with lower heating requirements may want lower SHGC to avoid overheating, while higher SHGC may be preferable to allow beneficial solar gain in colder climates. In practice, building orientation, local shading, visual comfort, and external appearance may drive decisions to use windows with different performance characteristics on different parts of a single building.

The achievable thermal performance of the overall assembly is a different matter, as it is limited in most configurations by the thermal performance of the existing framing. Even in the frame-within-reveal configuration, the thermal conductivity of the existing sill/jamb/reveal material is important. Based on our understanding of the commercial building window stock, the frame-within-frame configuration would be the most common retrofit application. The major downside to this configuration, also discussed in some of the case studies, is that any thermal bridge through the existing window frame significantly impacts the overall assembly performance.

As starting point for target assembly performance, the values from the ASHRAE *Achieving Zero Energy---Advanced Energy Design Guide (AEDG) for Small to Medium Office Buildings* \[5\] were reviewed, as shown in Table 6. The biggest challenge in achieving these performance criteria using secondary windows would likely be the thermal bridging through the existing frame.

Table 6. Overall Assembly Performance Characteristics by Climate Zone

|                         | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** |
|-------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
|**U-factor (Btu/h-ft2-°F)** | 0.48  | 0.48  | 0.43  | 0.40  | 0.34  | 0.34  | 0.32  | 0.28  | 0.25  |
| **SHGC**                    | 0.21  | 0.22  | 0.24  | 0.24  | 0.34  | 0.36  | 0.36  | 0.38  | 0.38  |
| **VT/SHGC**                 | 1.10  | 1.10  | 1.10  | 1.10  | 1.10  | 1.10  | 1.10  | 1.10  | 1.10  |

To understand the expected performance of the total assembly, a range of combinations of existing window and secondary windows was modeled using the LBNL WINDOW software. As illustrated in Figure 3, a modeling simplification was made to exclude the effects of the secondary window frame, because in the frame-within-frame configuration, heat transfer would likely be dominated by the existing frame.

![Chart Description automatically generated with low confidence](./media/360d2138-c38d-4404-9644-d10d2efcde44.png)

Figure 3. Modeling simplification for frame-within-frame secondary window systems

Adding double-pane secondary windows to existing single-pane windows achieved a significant improvement in thermal and optical performance. Adding double-pane secondary windows to existing double-pane windows had diminishing returns over adding single-pane secondary windows because the achievable assembly performance was limited by the thermal bridging in the window frames. Ultimately, the combinations of existing windows and secondary windows shown in Table 7 is proposed. As expected, a comparison of the achieved performance values to the AEDG recommendations (see Table 8) shows that the overall thermal performance levels are still below the recommended values, largely driven by the limited performance of the existing window frame.

Table 7. Proposed Combinations for Performance of Existing Window Plus Secondary Window Combinations by Climate Zone

<!-- table recovered from ./media/00e9bd9d-633e-459e-9841-231c488010c5.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_ext_secondary_window.yaml
     method: vision-transcription -->

**Existing window (one value per ID; the source merges these across all three climate zone bands)**

| ID | Pane | Glazing | Frame | Low-e | U-Factor (IP) (Btu/hr*ft2*F) | R-value (IP) (hr*ft2*F/Btu) | SHGC | VLT |
|---|---|---|---|---|---|---|---|---|
| 1 | Single | Clear | Aluminum | No | 1.18 | 0.85 | 0.74 | 0.75 |
| 2 | Single | Tinted/Reflective | Aluminum | No | 1.18 | 0.85 | 0.58 | 0.46 |
| 3 | Single | Clear | Wood | No | 0.91 | 1.10 | 0.68 | 0.72 |
| 4 | Single | Tinted/Reflective | Wood | No | 0.91 | 1.10 | 0.53 | 0.44 |
| 5 | Double | Clear | Aluminum | No | 0.75 | 1.34 | 0.65 | 0.67 |
| 6 | Double | Tinted/Reflective | Aluminum | No | 0.75 | 1.34 | 0.48 | 0.41 |
| 7 | Double | Clear | Aluminum | Yes | 0.56 | 1.79 | 0.39 | 0.59 |
| 8 | Double | Clear | Aluminum with thermal break | Yes | 0.50 | 2.00 | 0.38 | 0.59 |
| 9 | Double | Tinted/Reflective | Aluminum | Yes | 0.56 | 1.80 | 0.27 | 0.36 |
| 10 | Double | Tinted/Reflective | Aluminum with thermal break | Yes | 0.50 | 2.02 | 0.27 | 0.36 |
| 11 | Triple | Clear | Aluminum with thermal break | Yes | 0.30 | 3.33 | 0.33 | 0.53 |
| 12 | Triple | Tinted/Reflective | Aluminum with thermal break | Yes | 0.30 | 3.34 | 0.22 | 0.32 |

**Secondary window (climate zones 1-8 = one value the source merged across every zone band)**

| ID | Climate Zones | Applicable? | Pane | Glazing | Frame | Low-e |
|---|---|---|---|---|---|---|
| 1 | 1-8 | TRUE | Double | Tinted/Reflective | Aluminum with thermal break | Yes |
| 2 | 1-8 | TRUE | Double | Clear | Aluminum with thermal break | Yes |
| 3 | 1-8 | TRUE | Double | Tinted/Reflective | Aluminum with thermal break | Yes |
| 4 | 1-8 | TRUE | Double | Clear | Aluminum with thermal break | Yes |
| 5 | 1-8 | TRUE | Single | Tinted/Reflective | Aluminum with thermal break | Yes |
| 6 | 1-8 | TRUE | Single | Clear | Aluminum with thermal break | Yes |
| 7 | 1, 2, 3 | TRUE | Single | Tinted/Reflective | Aluminum with thermal break | No |
| 7 | 4, 5, 6 | TRUE | Single | Clear | Aluminum with thermal break | No |
| 7 | 7, 8 | TRUE | Single | Clear | Aluminum with thermal break | No |
| 8 | 1, 2, 3 | TRUE | Single | Tinted/Reflective | Aluminum with thermal break | No |
| 8 | 4, 5, 6 | TRUE | Single | Clear | Aluminum with thermal break | No |
| 8 | 7, 8 | TRUE | Single | Clear | Aluminum with thermal break | No |
| 9 | 1-8 | TRUE | Single | Clear | Aluminum with thermal break | No |
| 10 | 1-8 | TRUE | Single | Clear | Aluminum with thermal break | No |
| 11 | 1-8 | FALSE | No secondary window applied |  |  |  |
| 12 | 1-8 | FALSE | No secondary window applied |  |  |  |

**Total assembly performance with secondary window added (blank for IDs 11 and 12, which have no secondary window applied)**

| ID | Climate Zones | U-Factor (IP) (Btu/hr*ft2*F) | R-value (IP) (hr*ft2*F/Btu) | SHGC | VLT |
|---|---|---|---|---|---|
| 1 | 1-8 | 0.61 | 1.63 | 0.54 | 0.47 |
| 2 | 1-8 | 0.61 | 1.63 | 0.43 | 0.37 |
| 3 | 1-8 | 0.37 | 2.70 | 0.49 | 0.45 |
| 4 | 1-8 | 0.37 | 2.70 | 0.38 | 0.36 |
| 5 | 1-8 | 0.61 | 1.64 | 0.54 | 0.36 |
| 6 | 1-8 | 0.61 | 1.64 | 0.42 | 0.37 |
| 7 | 1, 2, 3 | 0.50 | 1.98 | 0.35 | 0.32 |
| 7 | 4, 5, 6 | 0.50 | 1.98 | 0.35 | 0.32 |
| 7 | 7, 8 | 0.50 | 1.98 | 0.36 | 0.53 |
| 8 | 1, 2, 3 | 0.44 | 2.25 | 0.34 | 0.32 |
| 8 | 4, 5, 6 | 0.44 | 2.25 | 0.35 | 0.53 |
| 8 | 7, 8 | 0.44 | 2.25 | 0.35 | 0.53 |
| 9 | 1-8 | 0.50 | 1.99 | 0.25 | 0.32 |
| 10 | 1-8 | 0.44 | 2.26 | 0.24 | 0.32 |
| 11 | 1-8 |  |  |  |  |
| 12 | 1-8 |  |  |  |  |

**Performance change of the total assembly against the existing window (blank for IDs 11 and 12)**

| ID | Climate Zones | R-value (%) | SHGC (%) | VLT (%) |
|---|---|---|---|---|
| 1 | 1-8 | 92% | -27% | -38% |
| 2 | 1-8 | 92% | -26% | -18% |
| 3 | 1-8 | 146% | -28% | -38% |
| 4 | 1-8 | 146% | -28% | -18% |
| 5 | 1-8 | 23% | -17% | -46% |
| 6 | 1-8 | 23% | -13% | -11% |
| 7 | 1, 2, 3 | 11% | -10% | -46% |
| 7 | 4, 5, 6 | 11% | -10% | -46% |
| 7 | 7, 8 | 11% | -8% | -11% |
| 8 | 1, 2, 3 | 12% | -10% | -46% |
| 8 | 4, 5, 6 | 12% | -8% | -11% |
| 8 | 7, 8 | 12% | -8% | -11% |
| 9 | 1-8 | 11% | -8% | -11% |
| 10 | 1-8 | 12% | -8% | -11% |
| 11 | 1-8 |  |  |  |
| 12 | 1-8 |  |  |  |

Table 8. Comparison of Existing Window Plus Secondary Window Combinations to ASHRAE *Small and Medium Office Zero Energy AEDG* Performance Targets by Climate Zone

<!-- table recovered from ./media/0f54f116-2001-4833-b8ba-bff84c446d15.png
     overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/docs/upgrade_measures/env_ext_secondary_window.yaml
     method: vision-transcription -->

**Existing window**

| ID | Pane | Glazing | Frame | Low-e |
|---|---|---|---|---|
| 1 | Single | Clear | Aluminum | No |
| 2 | Single | Tinted/Reflective | Aluminum | No |
| 3 | Single | Clear | Wood | No |
| 4 | Single | Tinted/Reflective | Wood | No |
| 5 | Double | Clear | Aluminum | No |
| 6 | Double | Tinted/Reflective | Aluminum | No |
| 7 | Double | Clear | Aluminum | Yes |
| 8 | Double | Clear | Aluminum with thermal break | Yes |
| 9 | Double | Tinted/Reflective | Aluminum | Yes |
| 10 | Double | Tinted/Reflective | Aluminum with thermal break | Yes |
| 11 | Triple | Clear | Aluminum with thermal break | Yes |
| 12 | Triple | Tinted/Reflective | Aluminum with thermal break | Yes |

**Secondary window (climate zones 1-8 = one value the source merged across every zone band)**

| ID | Climate Zones | Pane | Glazing | Frame | Low-e |
|---|---|---|---|---|---|
| 1 | 1-8 | Double | Tinted/Reflective | Aluminum with thermal break | Yes |
| 2 | 1-8 | Double | Clear | Aluminum with thermal break | Yes |
| 3 | 1-8 | Double | Tinted/Reflective | Aluminum with thermal break | Yes |
| 4 | 1-8 | Double | Clear | Aluminum with thermal break | Yes |
| 5 | 1-8 | Single | Tinted/Reflective | Aluminum with thermal break | Yes |
| 6 | 1-8 | Single | Clear | Aluminum with thermal break | Yes |
| 7 | 1, 2, 3 | Single | Tinted/Reflective | Aluminum with thermal break | No |
| 7 | 4, 5, 6 | Single | Clear | Aluminum with thermal break | No |
| 7 | 7, 8 | Single | Clear | Aluminum with thermal break | No |
| 8 | 1, 2, 3 | Single | Tinted/Reflective | Aluminum with thermal break | No |
| 8 | 4, 5, 6 | Single | Clear | Aluminum with thermal break | No |
| 8 | 7, 8 | Single | Clear | Aluminum with thermal break | No |
| 9 | 1-8 | Single | Clear | Aluminum with thermal break | No |
| 10 | 1-8 | Single | Clear | Aluminum with thermal break | No |
| 11 | 1-8 | No secondary window applied |  |  |  |
| 12 | 1-8 | No secondary window applied |  |  |  |

**Total assembly performance with secondary window added (climate zones 1-8 = one value the source merged across every zone band)**

| ID | Climate Zones | U-Factor (IP) (Btu/hr*ft2*F) | R-value (IP) (hr*ft2*F/Btu) | SHGC | VLT |
|---|---|---|---|---|---|
| 1 | 1-8 | 0.61 | 1.63 | 0.54 | 0.47 |
| 2 | 1-8 | 0.61 | 1.63 | 0.43 | 0.37 |
| 3 | 1-8 | 0.37 | 2.70 | 0.49 | 0.45 |
| 4 | 1-8 | 0.37 | 2.70 | 0.38 | 0.36 |
| 5 | 1-8 | 0.61 | 1.64 | 0.54 | 0.36 |
| 6 | 1-8 | 0.61 | 1.64 | 0.42 | 0.37 |
| 7 | 1, 2, 3 | 0.50 | 1.98 | 0.35 | 0.32 |
| 7 | 4, 5, 6 | 0.50 | 1.98 | 0.35 | 0.32 |
| 7 | 7, 8 | 0.50 | 1.98 | 0.36 | 0.53 |
| 8 | 1, 2, 3 | 0.44 | 2.25 | 0.34 | 0.32 |
| 8 | 4, 5, 6 | 0.44 | 2.25 | 0.35 | 0.53 |
| 8 | 7, 8 | 0.44 | 2.25 | 0.35 | 0.53 |
| 9 | 1-8 | 0.50 | 1.99 | 0.25 | 0.32 |
| 10 | 1-8 | 0.44 | 2.26 | 0.24 | 0.32 |

**AEDG recommendation (average of recommendation for included climate zones)**

| Climate Zones | U-Factor (IP) (Btu/hr*ft2*F) | R-value (IP) (hr*ft2*F/Btu) | SHGC |
|---|---|---|---|
| 1, 2, 3 | 0.44 | 2.27 | 0.23 |
| 4, 5, 6 | 0.33 | 3.03 | 0.35 |
| 7, 8 | 0.27 | 3.70 | 0.38 |

**Comparison to AEDG (difference from the recommendation above; IDs 11 and 12 have no secondary window applied)**

| ID | R-value diff (zones 1, 2, 3) | R-value diff (zones 4, 5, 6) | R-value diff (zones 7, 8) | SHGC diff (zones 1, 2, 3) | SHGC diff (zones 4, 5, 6) | SHGC diff (zones 7, 8) |
|---|---|---|---|---|---|---|
| 1 | -28% | -46% | -56% | 136% | 55% | 43% |
| 2 | -28% | -46% | -56% | 85% | 22% | 12% |
| 3 | 19% | -11% | -27% | 113% | 40% | 29% |
| 4 | 19% | -11% | -27% | 65% | 8% | 0% |
| 5 | -28% | -46% | -56% | 134% | 54% | 42% |
| 6 | -28% | -46% | -56% | 83% | 20% | 11% |
| 7 | -13% | -35% | -47% | 51% | -1% | -8% |
| 8 | -1% | -26% | -39% | 51% | -1% | -8% |
| 9 | -13% | -34% | -46% | 10% | -28% | -34% |
| 10 | -1% | -26% | -39% | 6% | -30% | -36% |

# 5.  Applicability

The current stock has 12 different window configurations. Figure 4 shows the breakdown of windows by total floor area. In total, single-pane windows represent about 53% of the floor area, double-pane 47%, and triple pane \<1%.

![Timeline Description automatically generated](./media/9ee2ecf1-33ec-44f7-8d95-3db062766207.png)

Figure 4. Percent stock floor area by window type

The secondary window measure is applicable to all buildings that currently have single- or double-pane windows, which is nearly 100% of the stock. The very small fraction of buildings that already have triple-pane windows will not receive this upgrade.

# 6.  Output Variables

Table 9 includes the output variable that is calculated in ComStock. This variable is important in terms of understanding the differences between buildings with and without the secondary window system measure applied. Additionally, this output variable can be used for understanding the economics (e.g., return of investment) of the upgrade if cost information (i.e., material, labor, and maintenance cost for technology implementation) is available.

Table 9. Output Variables Calculated From the Measure Application

| **Variable Name**               | **Description**                                                          |
|---------------------------------|--------------------------------------------------------------------------|
| Area of secondary windows added | Area of windows in the model to which secondary windows were added (ft2) |

# 7.  Results

