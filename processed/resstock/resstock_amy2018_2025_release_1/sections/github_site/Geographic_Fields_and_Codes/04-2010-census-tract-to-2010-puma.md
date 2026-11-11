<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/explanations/Geographic_Fields_and_Codes.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/explanations/Geographic_Fields_and_Codes.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/explanations/Geographic_Fields_and_Codes.html | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: github_site/docs/resources/explanations/Geographic_Fields_and_Codes.md | section: 2010 Census Tract to 2010 PUMA | lines: 83-91 -->
## 2010 Census Tract to 2010 PUMA
Background: The community gives you the 2010 census tract value for Research Road, right outside of NLR’s Golden, Colorado campus. They give you 08059010100.

**Step 1:** Go to the [Census Tract to PUMA Relationship Files](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/pumas.html#:~:text=Census%20Tract%20to%20PUMA%20Relationship,building%20block%20of%20PUMA%20geography), and choose the 2010 Census Tract to 2010 PUMA Relationship File and open it.

**Step 2:** Search the 2010 PUMA with commas separated. 08059010100 turns into 08,059,010100. When you search for the 08,059,010100 it matches one line, and the values after the 2010 Census Tract are 00818 which is the 5 digit PUMA code.

**Step 3:** Turn this information into a PUMA fit for ResStock. Combine the **State FIP**, <ins>an additional 0</ins>, and then the *2010 PUMA value*. For this example, it would be **08**<ins>0</ins>*00818*. Now you have the 2010 PUMA value!

