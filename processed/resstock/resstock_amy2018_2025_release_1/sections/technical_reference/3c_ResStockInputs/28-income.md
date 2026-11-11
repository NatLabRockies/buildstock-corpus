<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Income | lines: 3370-3397 -->
## Income

The ACS reports both household and family incomes in continuous values, which are then binned in ResStock. Income in ResStock represents the household income, or the total income of all household members age 15 or higher standardized to 2019 dollars. From income a variety of secondary income parameters are derived. Income RECS2015 and Income RECS2020 are binned variations that align with the reported bins from RECS 2015 and 2020, respectively. Federal poverty level (FPL) standardizes the household income according to the 2019 U.S. federal poverty guidelines, which vary based on household size and differ for the contiguous United States, Hawaii, and Alaska. Table “2019 federal poverty guidelines (aspe_2019_fpl)” shows the poverty lines by household size for the lower 48 states including D.C., for Hawaii, and for Alaska.

<div id="tab:fpl" data-source="3c_ResStockInputs.tex">

|        Household size        | Contiguous U.S. |  Hawaii  |  Alaska  |
|:----------------------------:|:---------------:|:--------:|:--------:|
|              1               |    \$12,490     | \$14,380 | \$15,600 |
|              2               |    \$16,910     | \$19,460 | \$21,130 |
|              3               |    \$21,330     | \$24,540 | \$26,660 |
|              4               |    \$25,750     | \$29,620 | \$32,190 |
|              5               |    \$30,170     | \$34,700 | \$37,720 |
|              6               |    \$34,590     | \$39,780 | \$43,250 |
|              7               |    \$39,010     | \$44,860 | \$48,780 |
|              8               |    \$43,430     | \$49,940 | \$54,310 |
| Per additional person over 8 |     \$4,420     | \$5,080  | \$5,530  |

2019 federal poverty guidelines ((Assistant Secretary For Planning and Evaluation n.d.a))

</div>

Per Table “2019 federal poverty guidelines (aspe_2019_fpl)”, the poverty line is \$25,750 for a household of four in the contiguous U.S. A household of the same size making \$40,000 per year in Colorado is therefore at 150%–200% of FPL (40,000/25,750\*100% = 155%). However, that exact household would be considered 100%–150% of FPL if living in Hawaii instead (40,000/29,620\*100% = 135%). FPL is used to determine eligibility for several federal assistance programs, including Low-Income Home Energy Assistance Program (LIHEAP) and Weatherization Assistance for Low-Income Persons ((Assistant Secretary For Planning and Evaluation n.d.b)).

Similar to FPL, Area Median Income in ResStock is household income standardized as a percentage of the [2019 Income Limits](https://www.huduser.gov/portal/datasets/il.html#data_2019), which are annually updated by HUD. The Income Limits are means-testing metrics intended to determine financial assistance eligibility, such as Section 8 housing, based on family income ((Department of Housing and Urban Development 2019)). Since ResStock does not model multiple families sharing a single housing unit, household income is treated the same as family income, and household income is used to calculate percent Area Median Income instead. Like FPL, the income limits vary by family size. But unlike FPL, they adjust for local housing costs and vary by county subdivisions. Generally, 0%–80% Area Median Income is regarded as Low-to-Moderate Income and the threshold for receiving most types of financial assistance. Sometimes 80%–150% Area Median Income households are eligible for partial financial assistance, such as in Section 50122 of the Inflation Reduction Act ((U.S. Congress 2022)) for home electrification rebates.

State Metro Median Income (SMMI) is a variant of Area Median Income. As the name suggests, SMMI standardizes the household income based on 2019 Income Limits set at the state level while differentiating between metropolitan and non-metropolitan areas. This metric is created primarily for the integration of socio-demographically differentiated time-use schedules from the American Time Use Survey, which tags respondents by state and metro status.

