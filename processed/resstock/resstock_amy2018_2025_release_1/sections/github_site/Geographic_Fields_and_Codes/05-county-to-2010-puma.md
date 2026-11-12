<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/explanations/Geographic_Fields_and_Codes.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/explanations/Geographic_Fields_and_Codes.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/explanations/Geographic_Fields_and_Codes.html | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: github_site/docs/resources/explanations/Geographic_Fields_and_Codes.md | section: County to 2010 PUMA | lines: 92-106 -->
## County to 2010 PUMA
Background: The community says they want to analyze Jefferson County, the county where NLR’s Golden, Colorado, campus is located.

**Step 1:** Make sure that county name has not undergone any changes by pulling up the [Changes to Counties](https://www.census.gov/programs-surveys/geography/technical-documentation/county-changes.2000.html#list-tab-957819518) website. Best to go from present day, 2020s, back to 2000, to make sure the county name has not changed in recent history. We see that Jefferson County is one that underwent changes back in 2001.

**Step 2:** Because Jefferson County has not undergone any changes since 2001, we can look at the 2010 maps.

**Step 3:** Go to the [2010 Census Public Use Microdata Area (PUMA) Reference Maps](https://www.census.gov/geographies/reference-maps/2010/geo/2010-pumas.html), and choose Colorado.

**Step 4:** Search for the word Jefferson to easily highlight the state and the PUMA values that Jefferson County covers.

**Step 5:** Record the values, they are written as two state numbers or FIP code, an additional zero, and then five PUMA numbers. For example, for the value 08000801, the PUMA value would be 00801. Looking at the list, the PUMAs that Jefferson County includes are: 00801, 00804, 00805, 00817, 00818, 00819, 00820, and 00821. These are the 2010 PUMAs for Jefferson County.

**Step 6:** Turn this information into a PUMA fit for ResStock. Combine the **State FIP**, <ins>an additional 0</ins>, and then the *2010 PUMA value*. The codes turn into 08000801, 08000804, 08000805, 08000817, 08000818, 08000819, 08000820, and 08000821.

