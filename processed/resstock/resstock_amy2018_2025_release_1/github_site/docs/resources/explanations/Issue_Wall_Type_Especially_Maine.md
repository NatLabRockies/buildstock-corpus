<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/explanations/Issue_Wall_Type_Especially_Maine.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/explanations/Issue_Wall_Type_Especially_Maine.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/explanations/Issue_Wall_Type_Especially_Maine.html | corpus_version: resstock_amy2018_2025_release_1-v1 -->
# Wall Type Issue, Especially in Maine

# Issue Report: Wall Type Issue, Especially in Maine
## Summary of Issue
The Geometry Wall Type characteristic is incorrect in the state of Maine due to inconsistencies in the county tax assessor data that this characteristic is based on in the ResStock™ model.

## Status
Current. Preliminary investigation completed. Detailed investigation pending. No fix implemented to date.

## Details
ResStock™ uses a nationally compiled county tax assessor dataset to create its characteristic distributions for the wall type characteristic. The current ResStock datasets, built upon this compiled county tax assessor data, show that Maine’s single-family detached housing stock has a wall type distribution of approximately 10% wood framed, 12% brick, and 78% concrete (CMU). This is the lowest portion of wood-framed construction for any state in the ResStock 2024 Release 2 dataset. The trends are similarly unexpected for other building types.

Several users, both inside and outside of NLR, notified the ResStock team that the Geometry Wall Type characteristic results did not look as expected in the state of Maine. The ResStock team confirmed these findings, noting in particular that the wall type results were inconsistent with Vermont, which has a similar housing stock. The team also confirmed with local building researchers in Maine that the results were inconsistent with their knowledge of the local housing stock.

The ResStock team spot-checked the wall type information from compiled county tax assessor data using Zillow photographs, and found considerable mislabeling of wall type. Zillow, which also imports data from county tax assessors, had the same mislabeling of wall type data as our compiled tax assessor source. Therefore, we identified the source of the error as the Maine portion of this dataset of tax assessor data that serves as the key data source for ResStock’s *Geometry Wall Type* characteristic. Similar problems have not been observed in other states, but a comprehensive investigation has not been completed.

## Impacts
The investigation into the full extent of the wall type data source inaccuracies and the extent of their impacts is not yet complete. Based on our preliminary checks, we believe the functional impacts are confined to the *wall type* and *wall exterior finish* characteristics. There is also a minimal impact on the *insulation wall* characteristic because the *insulation wall* characteristic is not dependent on the wall type, but the option names include the wall type. We believe that all published ResStock datasets are impacted.

There are downstream impacts of these functional impacts including upgrade applicability in several datasets. For example, some of the ResStock datasets have insulation measures that are only applied to wood-frame walls, and therefore would apply to fewer dwelling units in Maine than without this error. We currently do not believe there are significant impacts to energy consumption, emissions, or energy bill results in baseline or in cases where upgrades are applied.

## Recommendation
Users interested in the distribution of wall type or wall exterior finish in Maine should for now use ResStock results from nearby states, especially Vermont and New Hampshire. Users interested in the results of measures whose applicability depends on the wall type field should either re-weight the Maine results using wall type distributions from nearby states, or use the results from nearby states directly.
