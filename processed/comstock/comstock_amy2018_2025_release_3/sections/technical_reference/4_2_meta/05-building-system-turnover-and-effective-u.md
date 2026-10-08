<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_2_meta.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_2_meta.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: b5faf42 | corpus_path: technical_reference/documentation/reference_doc/4_2_meta.md | section: Building System Turnover and Effective Useful Life | lines: 63-129 -->
## Building System Turnover and Effective Useful Life

We assume that all major building systems are installed when the building is constructed, and that they are replaced periodically over the lifespan of the building. Replacements may be made because of equipment failure, building remodeling, energy efficiency upgrades, etc. To model the turnover of building systems, it is necessary to understand how often these building systems are replaced, which determines how long they last in the building stock. The metric commonly used by the energy efficiency community to describe the lifespan of a measure is effective useful life (EUL). The California Public Utilities Commission defines EUL as “an estimate of the median number of years that the measures installed under the program are still in place and operable” (California Public Utilities Commission 2020). In the reliability community, EUL is typically referred to as “median time to failure” (Texas Instruments 2021), whereas ASHRAE uses the term “median service life” (Abramson et al. 2006).

For ComStock, the primary source of EULs is the California Public Utilities Commission (CPUC) Database of Energy Efficiency Resources (DEER) (California Public Utilities Commission 2021). Previous work on EULs indicates that there is wide variation in the quality of national EUL data, but it also indicates that the studies performed in DEER are generally the best available (Skumatz 2012). The values in DEER were cross-referenced against the lifetimes used in the EIA NEMS Commercial Demand Module (U.S. Energy Information Administration 2017a) and the ASHRAE Service Life and Maintenance Cost Database (ASHRAE 2021). Table “Effective Useful Life of Major Commercial Building Systems” shows the EULs assumed for different building systems in ComStock.

<div id="tab:effective_useful_life" data-source="tables/effective_useful_life.tex">

| **Major Building System** | **EUL (Years**) | **Notes** |
|:---|:---|:---|
| Envelope—Wall Insulation | 200 | This value was based on engineering judgment. DEER EULs are capped at 20 years, per CPUC policy. NEMS does not appear to model wall turnover separate from whole-building replacement. |
| Envelope—Roof Insulation | 200 | This value was based on engineering judgment. DEER EULs are capped at 20 years, per CPUC policy. NEMS does not appear to model roof turnover separate from whole-building replacement. |
| Envelope—Windows | 70 | Based on a reliability analysis of windows from the 2014 Commercial Building Stock Assessment from the Pacific Northwest. DEER uses an EUL of 20 years for window replacement, as the DEER EULs are capped at 20 years, per CPUC policy. |
| Exterior Lighting | 15 | This closely matches the highest EUL in DEER for outdoor lighting (16 years). NEMS does not break out exterior lighting, but all NEMS commercial lighting technology types have a 10-year EUL. |
| Interior Lighting | 10 | This is in line with the EULs in DEER for interior lighting, and matches the 10-year EUL for all commercial lighting technologies in NEMS. |
| HVAC | 20 | The highest EUL in DEER for HVAC is 20 years. For rooftop air conditioners, which serve by far the largest portion of the building stock, NEMS uses a 21-year EUL. NEMS HVAC EULs range from 9.5 years for window AC units up to 30 years for some boilers. ASHRAE (2021) includes 33 packaged DX rooftop units with a mean lifetime of 21 years, and appears to be the source of some NEMS HVAC lifetimes. |
| Service Water Heating (SWH) | 15 | The highest SWH EUL in DEER is 20 years for a tankless water heater. Most tank-based SWH equipment in DEER has an EUL of 15 years or less. NEMS non-solar SWH equipment EULs range from 10 to 15 years. ASHRAE (2021) includes 5 gas-fired water heaters with a mean lifetime of 15 years, and 36 electric water heaters with a mean lifetime of 10 years. |
| Interior Equipment (Plug and Process Loads) | 15 | This value was based on engineering judgment and is meant to represent an average over all types of plug and process loads. If plug and process loads are addressed in future iterations, splitting the plug and process loads into information technology (IT) equipment and other equipment will be investigated, as IT equipment typically has a higher turnover rate than other process loads, such as hospital equipment or commercial kitchen equipment. NEMS includes commercial kitchen equipment with an EUL of 12 years, commercial ice machines with an EUL of 8 years, commercial vending machines with an EUL of 13.5 years, and commercial refrigeration equipment with an EUL of 10 years. |

Effective Useful Life of Major Commercial Building Systems

</div>

### Building Envelope

For the building envelope (windows, wall insulation, and roof insulation), the DEER database was not informative, because the maximum EUL is capped at 20 years, per CPUC policy. Because of this, we sought out other sources of envelope lifetime information.

#### Windows

As part of the DOE-funded Advanced Building Construction initiative, a team collected information on windows from a variety of commercial building surveys, including a new survey of buildings built since roughly 2010. Unfortunately, while most of the surveys did ask about windows, only one survey had enough information to perform a reliability analysis (because windows are long-lived). This survey was the 2014 Commercial Building Stock Analysis (Navigant Consulting 2014), which covers the Pacific Northwest. This survey included information on the age of the building, whether the windows had ever been replaced (and if so, an estimate of the year of replacement), and a weighting factor to describe how each sample fit into the whole building population. From these data, we performed a reliability analysis. Figure “Reliability analysis for windows in commercial buildings, from 2014 CBSA neea2014cbsa.” shows the estimated survival curve. As indicated by the black cross mark on the figure, the EUL estimate for windows is 70 years. However, the maximum lifespan extends to more than 400 years. In practice, this indicates that windows on some buildings will never be replaced.

<figure id="fig:comWindowSurvivalCurve">
<img src="figures/window_survival_curve.png" style="width:60.0%" />
<figcaption>Reliability analysis for windows in commercial buildings, from 2014 CBSA <span class="citation" data-cites="neea2014cbsa">(Navigant Consulting 2014)</span>.</figcaption>
</figure>

#### Walls and Roofs

None of the data sources we identified included information on EULs for walls and roofs, or, more specifically, the insulation on these surfaces. DEER EULs are capped at 20 years, per CPUC policy. NEMS does not appear to model wall turnover separately from whole-building replacement. Based on engineering judgment, we selected an EUL of 200 years to indicate that for most buildings, the wall and roof insulation will not be replaced before the building is demolished.

### Distribution of Lifespans

The EUL estimates in Figure “Reliability analysis for windows in commercial buildings, from 2014 CBSA neea2014cbsa.” represent the median lifespan for a given building system. However, not all systems will fail and be replaced after exactly that amount of time. To represent this diversity of failure rates we use a distribution.

The simplest approach would be to use a normal distribution centered on the EUL. However, studies of reliability data show that this is not a good assumption; instead, these studies often use a Weibull distribution to represent lifetimes. To check whether a Weibull distribution accurately represented the lifetimes of building equipment, we performed a reliability analysis on data from the ASHRAE Service Life and Maintenance Cost Database (ASHRAE 2021). This analysis was performed following the methodology described in an ASHRAE journal article (Hiller 2000), and was implemented using the reliability package (Reid 2020) in Python. Four categories of equipment with a reasonable number of entries were investigated: air handling units, boilers, chillers, and air source DX equipment (all types of each available in the database).

<figure id="fig:hvac_survival_curves" data-latex-placement="ht!">
<img src="figures/ashrae_equip_lifespans2.png" />
<figcaption>Survival curves and derived lifespan probability density functions for commercial HVAC equipment.</figcaption>
</figure>

As shown in Figure “Survival curves and derived lifespan probability density functions for commercial HVAC equipment.”, Weibull distributions are a good fit for several categories of HVAC equipment failure data. Although the ASHRAE database includes data for many different types of HVAC equipment, it was not selected as the primary source for deriving EULs for ComStock due to the limitations and biases in the database described by its creators (Abramson et al. 2006). Instead, we decided to use the EUL sources described in Table “Effective Useful Life of Major Commercial Building Systems” and develop Weibull curve parameters around these EULs. The selected parameters are shown in Table “Commercial Equipment Lifetime Weibull Distribution Parameters”. For the 70-year EUL, the parameters came from the window reliability analysis. For the 10-, 15-, and 20-year EULs, the only constraint was to match the EUL definition: 50% of the equipment would still be operable at the EUL. A minimum lifespan of 60% of the EUL was selected with the assumption that although individual components of a system might fail, it is unlikely that products on the market routinely fail at a whole-building scale in only a few years. The 200-year EUL parameters were selected to represent no failure for the life of the building.

<div id="tab:eul_distributions" data-source="tables/eul_distributions.tex">

| **EUL** | **Shape (beta)** | **Scale (alpha)** | **Shift (gamma)** |
|:-------:|:----------------:|:------------------|:------------------|
|   10    |       1.6        | EUL / 2 = 5       | EUL \* 0.6 = 6    |
|   15    |       1.6        | EUL / 2 = 7.5     | EUL \* 0.6 = 9    |
|   20    |       1.6        | EUL / 2 = 10      | EUL \* 0.6 = 12   |
|   70    |       1.3        | 91                | 0                 |
|   200   |       1.0        | 1                 | 200               |

Commercial Equipment Lifetime Weibull Distribution Parameters

</div>

