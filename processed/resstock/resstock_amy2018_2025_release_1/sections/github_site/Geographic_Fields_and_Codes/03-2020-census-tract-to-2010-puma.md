<!-- resstock resstock_amy2018_2025_release_1 | github_site | docs/resources/explanations/Geographic_Fields_and_Codes.md | status: site_page | source_url: https://github.com/NatLabRockies/ResStock.github.io/blob/696c020d696137830ddae75abbfb477ae7af8eaa/docs/resources/explanations/Geographic_Fields_and_Codes.md | publication_url: https://natlabrockies.github.io/ResStock.github.io/docs/resources/explanations/Geographic_Fields_and_Codes.html | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: github_site/docs/resources/explanations/Geographic_Fields_and_Codes.md | section: 2020 Census Tract to 2010 PUMA | lines: 40-82 -->
## 2020 Census Tract to 2010 PUMA
Background: Your community has given you the 2020 Census Tract for Research Road, an area right outside of NLR’s campus in Golden, Colorado. They have given you 08059010100. We have to convert that to a 2010 PUMA code for many ResStock resources.

### Example 1: Approximation
**Step 1:** Open [this website](https://www.census.gov/library/visualizations/2021/geo/demographicmapviewer.html). Click "Colorado" and zoom into the area for Research Road in Golden, CO.

**Step 2:** Click on the light blue area that includes Research Road; the area is called Applewood. Zoom out to get a better idea of the area.

**Step 3:** In a new tab, open [this website](https://usa.ipums.org/usa/volii/pumas20.shtml#web-map). Type in "Research Road" and zoom out so the area covered approximately matches the area highlighted in Step 2.

**Step 4:** Eyeball the census tract covered in Step 2 and overlap that with the map in Step 3 to identify the 2020 PUMA value (the blue number in the region that includes Research Road).

**Step 5:** Click on the 2020 PUMAs value in the step 3 website, 00702 in this example.

**Step 6:** Click to the right within the 2020 PUMA pop-up, and then you will see the 2010 PUMA pop-up. Click within the cell and you will see the 2010 PUMA value of 00818.

**Step 7:** Turn this information into a PUMA fit for ResStock. Combine the **State FIP**, <ins>an additional 0</ins>, and then the *2010 PUMA value*. For this example, it would be **08**<ins>0</ins>*00818*. Now you have the 2010 PUMA value!

### Example 2: Exact
**Step 1:** Open the [Explanation of the 2020 Census Tract to 2010 Census Tract Relationship File](https://www2.census.gov/geo/pdfs/maps-data/data/rel2020/tract/explanation_tab20_tract20_tract10.pdf). Then, go to the [Relationship Files](https://www.census.gov/geographies/reference-files/time-series/geo/relationship-files.2020.html#tract), and scroll down to the Census Tract Relationship Files and in the State-level 2020 Census Tract to 2010 Census Tract Relationship Files, choose Colorado.

**Step 2:** Search the text files that pops up for your 2020 Census Tract Number: 08059010100. Make sure the field that matches is the second one in the line, because that corresponds with the GEOID_TRACT_20 field, which we want.

**Step 3:** In this example, there are two lines that have a GEOID_TRACT_20 field that match our 2020 Census Tract. We need to figure out which one is the right one.

**Step 4:** Go to [2010 Census Tract Reference Maps](https://www.census.gov/geographies/reference-maps/2010/geo/2010-census-tract-maps.html), click Colorado, and go down to the county for this community. We know it is Jefferson County.

**Step 5:** Open each map and see if our location, Research Road in Golden, is on there. For our area it was on file DC10CT_C08059_001.pdf file.

**Step 6:** Scroll in on the map until you can find your location, and write down the census tract number which on this map is the bolded red text. In this case, it is 101.

**Step 7:** Go back to the file in Step 3. Remember, the 2020 Census Tract value 08059010100 came up twice in the 2020 column, so we need to figure out the 2010 column.

**Step 8:** Looking at the two matching rows, one row has the words Census Tract 1010 in the NAMELSAD_TRACT_10 column, which we know from Step 6 is the right census tract for 2010. We now know this is the right row.

**Step 9:** Look at the GEOID_TRACT_10 column for that row, and that is our 2010 Census Tract Number. In this example it is, 08059010100. Now we convert that to a 2010 PUMA value.

**Step 10:** Go to the [Census Tract to PUMA Relationship Files](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/pumas.html#:~:text=Census%20Tract%20to%20PUMA%20Relationship,building%20block%20of%20PUMA%20geography), and choose the 2010 Census Tract to 2010 PUMA Relationship File and open it.

**Step 11:** Search the 2010 PUMA with commas separated. 08059010100 turns into 08,059,010100. When you search for the 08,059,010100 it matches one line, and the values after the 2010 Census Tract are 00818 which is the five-digit PUMA code.

**Step 12:** Turn this information into a PUMA fit for ResStock. Combine the **State FIP**, <ins>an additional 0</ins>, and then the *2010 PUMA value*. For this example, it would be **08**<ins>0</ins>*00818*. Now you have the 2010 PUMA value!

