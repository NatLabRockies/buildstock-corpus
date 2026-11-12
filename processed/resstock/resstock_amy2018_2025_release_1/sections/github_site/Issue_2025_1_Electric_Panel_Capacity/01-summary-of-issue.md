<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/explanations/Issue_2025_1_Electric_Panel_Capacity.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/explanations/Issue_2025_1_Electric_Panel_Capacity.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/explanations/Issue_2025_1_Electric_Panel_Capacity.html | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: github_site/docs/resources/explanations/Issue_2025_1_Electric_Panel_Capacity.md | section: Summary of Issue | lines: 5-27 -->
## Summary of Issue
Electric panel results are new in the ResStock 2025 Release 1 dataset. After the dataset release, the ResStock team found an error in the electric panel results for a few of the measures in the ResStock 2025 Release 1 AMY2018 and AMY2012 datasets.

In short, the NEC load-based calculation treats new HVAC loads more conservatively than existing HVAC loads. Some of the upgraded measures’ HVAC loads are being counted as new loads when they should not be (e.g., the like-for-like replacement of a central AC is counted as a new load when it should not). This causes electric panel capacity constraints to increase in some measures when the electric panel capacity should actually decrease because the new upgraded load is more efficient than the baseline load. This issue currently impacts the following three measures only in the ResStock 2025 Release 1 dataset:
- Natural Gas Furnace 95% AFUE (applicable to 75% of the stock)
- Propane Furnace 95% AFUE or Fuel Oil Furnace 88% AFUE (applicable to 6% of the stock)
- Reference Space Heating and Air Conditioning Upgrade Circa 2025 (applicable to 75% of the stock)

This issue applies only to samples that have been upgraded in each measure, when the column **applicability** has a value of "True".

This issue impacts the following annual result columns:
- out.params.panel_load_total_load.2023_nec_existing_dwelling_load_based..w
- out.params.panel_load_occupied_capacity.2023_nec_existing_dwelling_load_based..a
- out.params.panel_load_headroom_capacity.2023_nec_existing_dwelling_load_based..a
- out.params.panel_load_total_load_savings.2023_nec_existing_dwelling_load_based..w
- out.params.panel_load_occupied_capacity_savings.2023_nec_existing_dwelling_load_based..a
- out.params.panel_constraint_capacity.2023_nec_existing_dwelling_load_based
- out.params.panel_constraint_overall.2023_nec_existing_dwelling_load_based

The electric panel space calculations are not impacted at all. This issue is only relevant for any capacity-related results.

**Until this issue is resolved in a future dataset release, the ResStock team recommends avoiding these columns for these like-for-like replacement measures.** These measures replace existing equipment with more efficient equivalents rather than adding new electric loads, and therefore should not trigger any panel constraints.

