<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/explanations/Issue_2025_1_Electric_Panel_Capacity.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/explanations/Issue_2025_1_Electric_Panel_Capacity.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/explanations/Issue_2025_1_Electric_Panel_Capacity.html | corpus_version: resstock_amy2018_2025_release_1-v1 -->
# ResStock 2025 Release 1 Electric Panel Capacity

# Issue Report: ResStock 2025 Release 1 Electric Panel Capacity
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

## Recommendation for reevaluating panel constraints
The baseline annual results show that approximately 2% of samples have a preexisting capacity constraint and no samples have a preexisting breaker space constraint.

Preexisting capacity constraints are an artifact of the modeling process. Because panel ratings are estimated from housing characteristics rather than detailed equipment inventories with explicit nameplate ratings, some uncertainty is unavoidable. Unlike breaker space constraints, which reflect a discrete physical limit, capacity constraints can appear in the model even when no physical limit has been reached, since connected load is calculated analytically rather than measured directly. A preexisting capacity constraint may reflect a genuinely overloaded panel, but no empirical data is currently available to validate these estimates.

For measure-level results, ResStock flags a capacity constraint whenever post-upgrade occupied capacity exceeds the panel's service rating. While technically correct, this approach can obscure the incremental impact of a measure for samples that already had a preexisting constraint. To isolate the impact attributable to each measure, the ResStock team recommends the following:
- Count only samples where the post-upgrade occupied capacity increased to cause or worsen a capacity constraint relative to the pre-upgrade state OR exclude samples with a preexisting constraint unless the measure made that constraint worse.
- For more conservative estimates, apply an additional safety factor to both pre- and post-upgrade occupied capacity when comparing against the service rating. Note that ResStock does not apply any safety factor by default.
