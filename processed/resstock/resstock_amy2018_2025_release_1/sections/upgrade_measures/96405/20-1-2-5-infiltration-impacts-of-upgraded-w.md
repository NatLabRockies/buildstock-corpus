<!-- resstock resstock_amy2018_2025_release_1 | upgrade_measures | measure_pdfs/96405.pdf | status: osti_pdf | source_url: https://docs.nlr.gov/docs/fy26osti/96405.pdf | publication_url: https://docs.nlr.gov/docs/fy26osti/96405.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: upgrade_measures/measure_pdfs/96405.md | section: 1.2.5 Infiltration Impacts of Upgraded Windows | lines: 286-327 -->
## 1.2.5 Infiltration Impacts of Upgraded Windows

As described in most window manufacturer literature, and as indicated by the presence of an air leakage requirement in the ENERGY STAR V7 performance characteristics, air leakage through and around windows plays a role in their energy performance. Unfortunately, literature quantifying this impact using measured data is limited. A 2003 paper (Ian Ridley, 2003) developed a simple model of the reduction that could be expected from replacing windows in the UK and concluded: 'A review of existing data suggests that replacing old leaky windows with modern sealed windows will reduce the background infiltration rate by the order of 0.1 air changes per hour (ach) to 0.3 ach. The actual value being dependent on the number of windows being replaced, the volume of the house and the leakiness of the old windows.' The values given in the paper are at natural pressure. Using the calculations from that paper, this equates to a reduction of 2-6 air changes per hour at 50 pascals (ACH50), which is a common way to describe infiltration levels.

In the ResStock baseline models, infiltration is specified as whole-dwelling ACH50. This input is dependent on climate zone, floor area, and vintage. The mean infiltration rate is generally higher in smaller, older homes in warmer climates. The mean infiltration rate ranges from around 20 ACH50 in older homes to 10 ACH50 in newer homes. There is no explicit relationship between infiltration and window type. However, there is an explicit relationship between window type and dwelling vintage. The resulting correlation is that older homes tend to have both lower-performance windows and higher infiltration. Table 5 shows the mean infiltration rates for dwellings with different window types.

Table 5. Baseline Infiltration Rate by Window Type

M-Gain stands for medium heat gain; L-Gain stands for low heat gain

| Baseline Window Type                                |   Mean Infiltration Rate (ACH50) |
|-----------------------------------------------------|----------------------------------|
| Single, Clear, Metal                                |                             19.7 |
| Single, Clear, Non-Metal                            |                             20.7 |
| Single, Clear, Metal, Exterior Clear Storm          |                             19.3 |
| Single, Clear, Non-Metal, Exterior Clear Storm      |                             20.5 |
| Double, Clear, Metal, Air                           |                             16.9 |
| Double, Clear, Metal, Air, Exterior Clear Storm     |                             16.8 |
| Double, Clear, Non-Metal, Air                       |                             17.1 |
| Double, Low-E, Non-Metal, Air, M-Gain               |                             15.7 |
| Double, Clear, Non-Metal, Air, Exterior Clear Storm |                             16.7 |
| Triple, Low-E, Non-Metal, Air, L-Gain               |                             16.3 |

Dwellings with single pane windows have a mean infiltration rate of 20 ACH50. Assuming these windows are older and leakier, applying the upper end 6 ACH50 reduction results in roughly a 30% decrease in infiltration from new windows. Dwellings with double or triple pane windows have a mean infiltration rate of around 16 ACH 50. Assuming these windows are newer and less leaky due to better materials and less exposure to time, home settling, etc., applying the lower end 2 ACH50 reduction results in roughly a 13% decrease in infiltration from new windows. Given the limited information available in the literature, these percentage reductions are assumed to apply to all dwellings with a given window type, as summarized in Table 6.

Table 6. Infiltration Rate Reduction From ENERGY STAR V7 Windows by Baseline Window Type

| Baseline Window Type                                |   Infiltration Rate Reduction (%) |
|-----------------------------------------------------|-----------------------------------|
| Single, Clear, Metal                                |                                30 |
| Single, Clear, Non-Metal                            |                                30 |
| Single, Clear, Metal, Exterior Clear Storm          |                                30 |
| Single, Clear, Non-Metal, Exterior Clear Storm      |                                30 |
| Double, Clear, Metal, Air                           |                                13 |
| Double, Clear, Metal, Air, Exterior Clear Storm     |                                13 |
| Double, Clear, Non-Metal, Air                       |                                13 |
| Double, Low-E, Non-Metal, Air, M-Gain               |                                13 |
| Double, Clear, Non-Metal, Air, Exterior Clear Storm |                                13 |
| Triple, Low-E, Non-Metal, Air, L-Gain               |                                13 |

A previous analysis (Elaina Present, 2024) came to a similar conclusion of applying a 30% reduction in infiltration to dwellings where single pane windows are replaced, and a 10% reduction in infiltration to dwellings where double or triple pane windows are replaced. The authors of that publication described that the numbers were based primarily on conversations with subject matter experts rather than calculations.

