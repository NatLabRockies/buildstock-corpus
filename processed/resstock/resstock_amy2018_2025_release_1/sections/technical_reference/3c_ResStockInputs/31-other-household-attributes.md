<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Other Household Attributes | lines: 3448-3900 -->
## Other Household Attributes

Occupants is the household size or the number of residents living together in a housing unit. Occupant is zero for vacant units and 10+ is modeled as 11. This assumption is used when converting household income to FPL, Area Median Income, or SMMI. Tenure defines whether a housing unit is renter- or owner-occupied. A unit occupied without rent payment is considered renter-occupied under the assumption that the occupants cannot easily update the property without the ownership. “Household Has Tribal Persons” is derived from the person samples to indicate whether a household has at least one person identified as American Indian or from one of the American Tribes. These household characteristics are either zero or not available for vacant units.

The details of each household characteristics are found in the next section.

### Income

#### Description

Income of the household occupying the housing unit.

#### Distribution Data Sources

- 2019 5-year PUMS from the University of Minnesota.

#### Direct Conditional Dependencies

- Geometry Building Type RECS

- PUMA

- Tenure

- Vintage ACS.

#### Options

The Income options are a set of income bins ranging from 10,000 to 199,999. The two end bins are \<10,000 and 200,000+. This characteristic has no ResStock arguments. Instead, it is used to construct other income characteristics and influences the distribution of housing characteristics as an indirect dependency.

#### Distribution Assumptions

- In ACS, Income and Tenure are reported for occupied units only. Because we assume vacant units share the same Tenure distribution as occupied units, by extension, we assume this Income distribution applies to all units regardless of Vacancy Status. For reference, 57445 / 140160 rows have sampling_probability \>= 1/550,000.[^7] Of those rows, 2961 (5%) were replaced due to low samples in the following process: Where sample counts are less than 10 (79145 / 140160 relevant rows), the Census Division by PUMA Metro Status average distribution has been inserted first (76864), followed by Census Division by ‘Metro’/‘Non-metro’ average distribution (1187), followed by Census Region by PUMA Metro Status average distribution (282), followed by Census Region by ‘Metro’/‘Non-metro’ average distribution (112).

### Income RECS2015

#### Description

Income of the household occupying the housing unit that are aligned with the 2015 U.S. Energy Information Administration Residential Energy Consumption Survey.

#### Distribution Data Sources

- 2019 5-year PUMS from the University of Minnesota.

#### Direct Conditional Dependencies

- Income.

#### Options

The Income RECS2015 option are bins mapped from the Income characteristic to align with the RECS 2015 income bins. The characteristic does not set any ResStock arguments.

#### Distribution Assumptions

- The income in 2019 USD are consolidated to align with those of RECS 2015 without inflation adjustment.

### Income RECS2020

#### Description

Income of the household occupying the housing unit that are aligned with the 2020 U.S. Energy Information Administration Residential Energy Consumption Survey.

#### Distribution Data Sources

- 2019 5-year PUMS from the University of Minnesota.

#### Direct Conditional Dependencies

- Income.

#### Options

The Income RECS2020 options are bins mapped from the Income characteristic to align with the RECS 2020 income bins. The characteristic does not set any ResStock arguments.

#### Distribution Assumptions

- The income in 2019 USD are consolidated to align with those of RECS 2020 without inflation adjustment.

### Federal Poverty Level

#### Description

Income as a percent of the federal poverty line of the household occupying the housing unit.

#### Distribution Data Sources

- Income from 2019 5-year PUMS from the University of Minnesota.

- 2019 federal poverty guidelines from [Office of the Assistant Secretary for Planning and Evaluation within the U.S. Department of Health and Human Services](https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines/prior-hhs-poverty-guidelines-federal-register-references/2019-poverty-guidelines).

#### Direct Conditional Dependencies

- Income

- Occupants.

#### Options

The Federal Poverty Level options are the following bins: %0-100%, 100%–150%, 150%–200%, 200%–300%, 300%–400%, and 400%+. The Not Available option is for vacant units. The Federal Poverty Level options do not set any ResStock arguments.

#### Distribution Assumptions

- Percent Federal Poverty Level is calculated using annual household income in 2019 USD (continuous, not binned) from 2019 5-year PUMS data and 2019 Federal Poverty Lines for contiguous U.S., where the FPL threshold for 1-occupant household is \$12,490 and \$4,420 for every additional person in the household.

### Area Median Income

#### Description

Income as a percent of area median income of the household occupying the housing unit.

#### Distribution Data Sources

- Income from 2019 5-year PUMS from the University of Minnesota.

- Area Median Income definitions based on [2019 Income Limits from HUD](https://www.huduser.gov/portal/datasets/il.html#data_2019).

#### Direct Conditional Dependencies

- Income

- Occupants

- PUMA.

#### Options

The Area Median Income options are the following bins: 0%–30%, 30%–60%, 60%–80%, 80%–100%, 100%–120%, 120%–150%, and 150+%. The Not Available option is for vacant units. The Area Median Income options do not set any ResStock arguments.

#### Distribution Assumptions

1.  Percent Area Median Income is calculated using annual household income in 2019 USD (continuous, not binned) from 2019 5-year PUMS data and 2019 income limits from HUD. These limits adjust for household size AND local housing costs (i.e., fair market rents). Income limits reported at county subdivisions are consolidated to County using a [crosswalk](https://mcdc.missouri.edu/applications/geocorr2014.html) generated from Missouri Census Data Center’s geocorr (2014), which has 2010 ACS housing unit count.

2.  For the 478 counties available in PUMS (60%), the county-level income limits are used. For all others (40%), PUMA-level income limits are used, which are converted from county-level using 2010 ACS housing unit count.

### State Metro Median Income

#### Description

State Metro Median Income of the household occupying the housing unit. This is different from State Median Income in that the Income Limits are differentiated by metro and nonmetro regions of the state.

#### Distribution Data Sources

- Income from 2019 5-year PUMS from the University of Minnesota.

- Income Limits derived from 2019 5-year PUMS from the University of Minnesota and 2019 median income by state and metro/nonmetro area from HUD.

#### Direct Conditional Dependencies

- Area Median Income

- County Metro Status

- State.

#### Options

The State Metro Median Income options are the following bins: 0%–30%, 30%–60%, 60%–80%, 80%–100%, 100%–120%, 120%–150%, and 150+%. The Not Available option is for vacant units. The State Metro Median Income options do not set any ResStock arguments.

#### Distribution Assumptions

- Percent State Metro Median Income is calculated using annual household income in 2019 USD (continuous, not binned) from 2019 5-year PUMS data and 2019 median income by state and metro/nonmetro area from HUD. A County Metro Status-differentiated Income Limits table is derived from the median income table by adjusting for household size, which is consistent with the method of generating state income limits by HUD.

### Occupants

#### Description

The number of occupants living in the housing unit.

#### Distribution Data Sources

- 2019 5-year PUMS from the University of Minnesota.

#### Direct Conditional Dependencies

- Bedrooms

- Census Division

- Geometry Building Type RECS

- Income RECS2015

- PUMA Metro Status

- Tenure.

#### Options

The Occupants options range from 0 to 10+ for the the ResStock baseline baseline (Table “The ResStock arguments set in the Occupants characteristic”). This characteristic assigns value to `geometry_unit_num_occupants` accordingly, with `geometry_unit_num_occupants`=11 for Occupants=10+. Occupants=0 corresponds to vacant units. `general_water_use_usage_multiplier` is auto-calculated from occupants.

<div id="table:hc_arg_def_occupants" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `geometry_unit_num_occupants` | false | \# | Double |  | The number of occupants in the unit. If not provided, an *asset* calculation is performed assuming standard occupancy, in which various end-use defaults (e.g., plug loads, appliances, and hot water usage) are calculated based on Number of Bedrooms and Conditioned Floor Area per ANSI/RESNET/ICC 301-2019. If provided, an *operational* calculation is instead performed in which the end-use defaults are adjusted using the relationship between Number of Bedrooms and Number of Occupants from RECS 2015. |
| `general_water_use_usage_multiplier` | false |  | Double | auto | Multiplier on internal gains from general water use (floor mopping, shower evaporation, water films on showers, tubs & sinks surfaces, plant watering, etc.) that can reflect, e.g., high/low usage occupants. |

The ResStock arguments set in the Occupants characteristic

</div>

#### Distribution Assumptions

- Option=10+ has a (weighted) representative value of 11. In ACS, Income, Tenure, and Occupants are reported for occupied units only. Because we assume vacant units share the same Income and Tenure distributions as occupied units, by extension, we assume this Occupants distribution applies to all units regardless of Vacancy Status. Where sample counts are less than 10 (6,243 / 18,000 rows), the Census Region average distribution has been inserted first (2,593), followed by national average distribution (2,678), followed by national + ‘MF’/‘SF’ average distribution (252), followed by national + ‘MF’/‘SF’ + ‘Metro’/‘Non-metro’ average distribution (315), followed by national + ‘MF’/‘SF’ + ‘Metro’/‘Non-metro’ + Vacancy Status average distribution (657).

### Vacancy Status

#### Description

The vacancy status (occupied or vacant) of the housing unit.

#### Distribution Data Sources

- 2019 5-year PUMS from the University of Minnesota.

#### Direct Conditional Dependencies

- Geometry Building Type RECS

- PUMA.

#### Options

The Vacancy Status options are either Occupied or Vacant. The options assign the vacancy periods through the `schedules_vacancy_periods` ResStock argument (Table “The ResStock arguments set in the Vacancy Status characteristic”). Vacant units are assumed to be vacant for the full calendar year.

<div id="table:hc_opt_vacancy" data-source="3c_ResStockInputs.tex">

| Option name | `schedules_vacancy_periods` |
|:------------|:----------------------------|
| Occupied    |                             |
| Vacant      | Jan 1–Dec 31                |

The ResStock arguments set in the Vacancy Status characteristic

</div>

The argument definition of the arguments set in the Vacancy Status characteristic can be found in Table “The ResStock arguments set in the Vacancy Status characteristic”.

<div id="table:hc_arg_def_vacancy" data-source="3c_ResStockInputs.tex">

| Name | Required | Units | Type | Choices | Description |
|:---|:---|:---|:---|:---|:---|
| `schedules_vacancy_periods` | false |  | String |  | Specifies the vacancy periods. Enter a date like “Dec 15–Jan 15.” Optionally, can enter hour of the day like “Dec 15 2–Jan 15 20” (start hour can be 0 through 23 and end hour can be 1 through 24). If multiple periods, use a comma-separated list. |

The ResStock arguments set in the Vacancy Status characteristic

</div>

#### Distribution Assumptions

- Where sample counts are less than 10 (434 / 11,680 rows), the State average distribution has been inserted. ‘Mobile Home’ does not exist in D.C. and is replaced by ‘Single-Family Detached.’

### Tenure

#### Description

The tenancy (owner or renter) of the household occupying the housing unit.

#### Distribution Data Sources

- 2019 5-year PUMS from the University of Minnesota.

#### Direct Conditional Dependencies

- Geometry Building Type RECS

- PUMA

- Vacancy Status.

#### Options

The Tenure options are Owner, Renter, and Not Available. The not applicable option is for vacant units.

#### Distribution Assumptions

- In ACS, Tenure is reported for occupied units only. By excluding Vacancy Status as a dependency, we assume vacant units share the same Tenure distribution as occupied units. Where sample counts are less than 10 (464 / 11,680 rows), the Census Division by PUMA Metro Status average distribution has been inserted. ‘Mobile Home’ does not exist in D.C. and is replaced by ‘Single-Family Detached.’

### Household Has Tribal Persons

#### Description

The household occupying the housing unit has at least one Tribal person in the household.

#### Distribution Data Sources

- 2019 5-year PUMS from the University of Minnesota.

#### Direct Conditional Dependencies

- Federal Poverty Level

- Geometry Building Type RECS

- PUMA.

#### Options

The Household Has Tribal Persons options are Yes, No, and Not Available. The Not Available option is for Vacant Units.

#### Distribution Assumptions

- 2,188 / 2,336 PUMA has \<10 samples and are falling back to state -level aggregated values. D.C. Mobile Homes do not exist and are replaced with Single-Family Detached.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-AUTONOMIE" class="csl-entry">

Argonne National Laboratory. 2025. *Autonomie*. <https://vms.taps.anl.gov/tools/autonomie/full_version/>.

</div>

<div id="ref-aspe_2019_fpl" class="csl-entry">

Assistant Secretary For Planning and Evaluation. n.d.a. *Office of the Assistant Secretary for Planning and Evaluation: 2019 Poverty Guidelines*. <https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines/prior-hhs-poverty-guidelines-federal-register-references/2019-poverty-guidelines>.

</div>

<div id="ref-aspe_fpl_use" class="csl-entry">

Assistant Secretary For Planning and Evaluation. n.d.b. *Office of the Assistant Secretary for Planning and Evaluation: Frequently Asked Questions Related to the Poverty Guidelines and Poverty*. <https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines/frequently-asked-questions-related-poverty-guidelines-poverty>.

</div>

<div id="ref-LBNLTTS2019" class="csl-entry">

Barbose, Galen, and Niam Darghouth. 2019. *<span class="nocase">Tracking the Sun: Pricing and Design Trends for Distributed Photovoltaic Systems in the United States</span>*. Lawrence Berkeley National Laboratory. <https://live-lbl-eta-publications.pantheonsite.io/sites/default/files/tracking_the_sun_2019_report.pdf>.

</div>

<div id="ref-hud2019_inc_lim_method" class="csl-entry">

Department of Housing and Urban Development. 2019. *Department of Housing and Urban Development: Methodology for Determining Section 8 Income Limits*. <https://www.huduser.gov/portal/datasets/il//il19/IncomeLimitsMethodology-FY19.pdf>.

</div>

<div id="ref-pvwatts_doc" class="csl-entry">

Dobos, Aron. 2014. *PVWatts Version 5 Manual*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy14osti/62641.pdf>.

</div>

<div id="ref-drehobl2020_energy_burden" class="csl-entry">

Drehobl, Ariel, Lauren Ross, and Roxana Ayala. 2020. “How High Are Household Energy Burdens? An Assessment of National and Metropolitan Energy Burden Across the United States.” *ACEEE*. <https://www.aceee.org/sites/default/files/pdfs/u2006.pdf>.

</div>

<div id="ref-EXPERIAN2023" class="csl-entry">

Experian. 2023. *Auto Registration Database*. [https://www.experian.com/automotive/auto-vehicle-data ](https://www.experian.com/automotive/auto-vehicle-data ).

</div>

<div id="ref-NHTS2017" class="csl-entry">

Federal Highway Administration. 2017. *2017 National Household Travel Survey*.

</div>

<div id="ref-NHTS2022" class="csl-entry">

Federal Highway Administration. 2022. *2022 National Household Travel Survey*.

</div>

<div id="ref-NPLH2021" class="csl-entry">

Ge, Yanbo, Christina Simeone, Andrew Duvall, and Eric Wood. 2021. *There’s No Place Like Home: Residential Parking, Electrical Access, and Implications for the Future of Electric Vehicle Charging Infrastructure*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy22osti/81065.pdf>.

</div>

<div id="ref-bahsp_2010" class="csl-entry">

Hendron, Robert, and Cheryn Engebrecht. 2010. *Building America House Simulation Protocols*. US DOE: Office of Energy Efficiency; Renewable Energy. <https://www1.eere.energy.gov/buildings/publications/pdfs/building_america/house_simulation.pdf>.

</div>

<div id="ref-ansi_resnet_301_2019" class="csl-entry">

International Code Council. 2019. *2019 ANSI/RESNET/ICC 2301 Standard for the Calculation and Labeling of the Energy Performance of Dwelling and Sleeping Units Using an Energy Rating Index*. International Code Council. <https://codes.iccsafe.org/content/RESNET3012019P1>.

</div>

<div id="ref-tank_model_parameters" class="csl-entry">

Maguire, Jeff, and David Roberts. 2020. “Deriving SimulationParameters for Storage-Type Water Heaters Using Ratings Data Produced from the Uniform Energy Factor Test Procedure.” *Building Performance Analysis Conference & SimBuild*. <https://www.nrel.gov/docs/fy21osti/71633.pdf>.

</div>

<div id="ref-MURATORI2021102967" class="csl-entry">

Muratori, Matteo, Paige Jadun, Brian Bush, et al. 2021. “Exploring the Future Energy-Mobility Nexus: The Transportation Energy & Mobility Pathway Options (TEMPO) Model.” *Transportation Research Part D: Transport and Environment* 98: 102967. https://doi.org/<https://doi.org/10.1016/j.trd.2021.102967>.

</div>

<div id="ref-RBSA" class="csl-entry">

Northwest Energy Efficiency Alliance. 2024. *2022 Residential Building Stock Assessment - Methods Report*. <https://neea.org/img/documents/2022-Residential-Building-Stock-Assessment-Methods-Report.pdf>.

</div>

<div id="ref-AHS" class="csl-entry">

U.S. Census. 2022. *American Housing Survey*. <https://www.census.gov/programs-surveys/ahs.html>.

</div>

<div id="ref-2022IRA" class="csl-entry">

U.S. Congress. 2022. *Inflation Reduction Act of 2022, Pub. L. No. 117-169, §50122.* <https://www.congress.gov/bill/117th-congress/house-bill/5376/text>.

</div>

<div id="ref-RECS2020" class="csl-entry">

U.S. Energy Information Administration. 2020. *Residential Buildings Energy Consumption Survey (RECS), 2020*. U.S. Energy Information Administration. <https://www.eia.gov/consumption/residential/data/2020/>.

</div>

<div id="ref-Wilson2014" class="csl-entry">

Wilson, E., C. Engebrecht Metzger, S. Horowitz, and R. Hendron. 2014. *2014 Building America House Simulation Protocols*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy14osti/60988.pdf>.

</div>

<div id="ref-WoodsMackenzie2020" class="csl-entry">

Woods Mackenzie. 2020. *<span class="nocase">Solar PV module technology market report 2020</span>*. <https://www.woodmac.com/reports/power-markets-solar-pv-module-technology-market-report-2020-443274/>.

</div>

<div id="ref-YIP2023" class="csl-entry">

Yip, Arthur, Christopher Hoehne, Paige Jadun, Catherine Ledna, Elaine Hale, and Matteo Muratori. 2023. *Highly Resolved Projections of Passenger Electric Vehicle Charging Loads for the Contiguous United States: Results from and Methods Behind Bottom-up Simulations of County-Specific Household Electric Vehicle Charging Load (Hourly 8760) Profiles Projected Through 2050 for Differentiated Household and Vehicle Types*. National Renewable Energy Laboratory (NREL), Golden, CO (United States). <https://doi.org/10.2172/1984452>.

</div>

</div>

[^1]: The 80% average multiplier resulted in a lower than expected water usage and is addressed in a later version of ResStock.

[^2]: For more information, see http://hes-documentation.lbl.gov/.

[^3]: For more information, see http://hes-documentation.lbl.gov/.

[^4]: ResStock currently does not account for hand washing of dishes in hot water in cases where no dishwasher is present.

[^5]: https://www.nrel.gov/transportation/tempo-model.html

[^6]: Autonomie is the source of TEMPO’s inputs about electric vehicle characteristics for both current day and future scenarios

[^7]: 550,000 is the typical sample size for ResStock, indicating that these rows are likely to get sampled.
