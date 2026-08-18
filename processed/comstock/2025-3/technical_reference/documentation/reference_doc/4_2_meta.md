<!-- comstock 2025-3 | technical_reference | documentation/reference_doc/4_2_meta.tex -->
# Location, Type, Age, Space Programming, Energy Code, and Change Over Time

## Location

ComStock has four levels of location granularity for its building models: ASHRAE Standard 169 - 2006 climate zone, census division, state, and county. During sampling, each model is first assigned a climate zone, then a county, then a state and census division. The climate zone and county probability distributions come from the CoStar and HIFLD data provided by the Homeland Security Infrastructure Program (HSIP) on a building count basis. The state and census division are assigned using a lookup table that is based on the model’s sampled county. The location metadata impacts numerous characteristics in the model, such as weather file, building type, building geometry characteristics (e.g., number of stories and rentable area), and energy code applicability. Table <a href="#tab:census_division_models_table" data-reference-type="ref" data-reference="tab:census_division_models_table">1</a> shows the number of models used in each census division.

Additional location metadata is joined to the *buildstock.csv* for use in parsing ComStock results. This includes data such as [Public Use Microdata Area](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/pumas.html) (PUMA), [Building America climate zone](https://www.energy.gov/eere/buildings/building-america-climate-specific-guidance), [independent system operator (ISO) region](https://isorto.org/), and [ReEDS balancing area](https://www.nrel.gov/analysis/reeds). This location metadata is joined on the [census tract](https://www2.census.gov/geo/pdfs/education/CensusTracts.pdf) level. Census tracts are assigned to the *buildstock.csv* using the CoStar and HSIP data. These location fields also include building cluster ID and name. Developed by DOE and NREL, these 88 geographic clusters allow for localized building stock analyses and are the basis for the U.S. Building Stock Segmentation Series. For more details about these clusters and their development, reference the [Building Stock Segmentation Cluster Development](https://www.nrel.gov/docs/fy23osti/84648.pdf) technical report.

<div id="tab:census_division_models_table">

| **Census Division** | **Count** | **Percentage** |
|:-------------------:|:---------:|:--------------:|
| East North Central  |   54122   |     15.46%     |
| East South Central  |   19882   |     5.68%      |
|    Mid-Atlantic     |   44976   |     12.85%     |
|      Mountain       |   24258   |     6.93%      |
|     New England     |   16791   |     4.80%      |
|       Pacific       |   54799   |     15.66%     |
|   South Atlantic    |   72616   |     20.75%     |
| West North Central  |   20910   |     5.97%      |
| West South Central  |   41646   |     11.90%     |

Distribution of ComStock Models in Each Census Division

</div>

## Building Type

The building types used by ComStock were originally defined by the DOE reference buildings, which were extended to create the prototype buildings. These building type definitions represent buildings by drawing on the applicable building code sets. Both the reference buildings and the prototype buildings have historically been used by building code organizations, include the ASHRAE 90.1 committee, to understand the potential impact of various code updates on newly constructed buildings.

Each building type is predominantly defined by a space type breakdown. For a given square footage of a ComStock building type, the fraction of the square footage of space type A (open office) vs. B (closed office) will remain the same as what they are in the DOE prototype models with two exceptions. Although these definitions are useful in the analysis of energy codes, there are several cases where they fail to provide the variability required for ComStock to provide a useful representation of the U.S. commercial building stock. There are two building types are currently represented with additional variability in space programming - large office and strip malls.

Large Offices
Currently, large offices have variable data-center loads in ComStock. This aligns with study data obtained through the [End-Use Load Profiles](https://www.nrel.gov/docs/fy22osti/80889.pdf) (EULP) project that was used to calibrate ComStock. This results in a higher degree of EUI variability within the large office building type than would be expected with only a change in space programming, given the high energy intensity of the data center space type.

Strip Malls
Strip malls often contain one or more restaurants. Strip malls with restaurants often have significantly higher EUIs than restaurant-free strip malls, which are the only kind represented by the reference and prototype models. To address the significant lack of diversity and variability in strip mall EUIs, the End-Use Load Profiles project added a variable restaurant component to strip mall models in ComStock. This results in a more realistic distribution of loads by end use across the strip mall segment.

## Vintage

Vintage, as previously discussed in the sampling section <a href="#Characteristic Estimation" data-reference-type="ref" data-reference="Characteristic Estimation">[Characteristic Estimation]</a>, is a key component of ascertaining the age and associated efficiency of building components. Vintage is determined based on information from either CoStar or HIFLD. However, in many cases, the vintage must be inferred due to a lack of available data on a county or state basis. When there is insufficient data on a county basis, state data are used, and in the few cases (typically in relation to hospitals) where state data are unavailable, national data are used.

Commercial buildings are complex in that each subsystem of the building—except perhaps walls—is expected to be replaced or updated at least once during the life of the building, without the building being reconstructed from the ground up. As such, it is critical to understand the year in which a building was first constructed in order to estimate the age (and the associated minimum energy code) as a function of the vintage. The latest year of intervention is calculated for each building component as a function of the vintage, and each of these are passed to an energy code lookup to determine which, if any, energy codes were in force.

Finally, it is important to note that vintage is especially important for recent construction. Buildings built within the last decade are unlikely to have significantly different or updated systems compared to those used at the time of construction. As a result, these buildings are a unique stock segment and have potential for cost-effective impact in the commercial building stock.

## Energy Code

#### Energy Code Adoption

Some states have a statewide code, while others have codes that are determined at the city or county level. For ComStock, the adoption of an energy code is assumed to be a function of year and state. For states with no statewide code, ComStock selects the code covering the biggest cities in the state. Where a state code was not a derivative of the ASHRAE 90.1 series of codes, the most similar versions of ASHRAE 90.1 were used for that state. The exception to this is California, where the Title 24 series of codes, as represented in DEER (California Public Utilities Commission 2021), was used because this series of codes was known to be significantly different from ASHRAE 90.1. Most of the information used to develop the code adoption history was taken from the Building Codes Assistance Project (Building Codes Assistance Project 2021). Much of the building stock was constructed before energy codes were widespread. For this time period, the “energy code” is described as either “DOE Ref Pre-1980,” whose assumptions are drawn from (Deru et al. 2011a), or “DOE Ref 1980-2004,” whose assumptions are a combination of ASHRAE 90.1-1989 and (Deru et al. 2011a). Details on the specific assumptions for each energy code are described in more detail throughout this document. The code adoption history assumptions are shown in Figure <a href="#fig:energy_code" data-reference-type="ref" data-reference="fig:energy_code">1</a>.

<figure id="fig:energy_code">
<img src="figures/energy_code.png" />
<figcaption>Adoption of energy codes by state over time.</figcaption>
</figure>

#### Energy Code Compliance

For this discussion, energy code compliance is defined as the extent to which a building constructed to comply with a certain energy code meets the requirements of that code. For example, a building built to comply with ASHRAE 90.1-2010 may meet all envelope requirements but fail to meet some HVAC control requirements. Unfortunately, there is little information available on commercial energy code compliance at a national level, and the information that does exist is not detailed. The status of this information is described in a detailed report (U.S. Energy Information Administration 2017b) generated for EIA’s NEMS modeling effort. What we do know, both from this information and anecdotally, is that commercial energy compliance is imperfect. Some buildings and building systems exceed code, and others lag behind. Because of the data limitations, we assume that all building systems meet the requirements of the energy code that was in force in their location when the building was originally constructed and as the building systems were replaced over time. As data on major building systems become available we hope to move away from this code-compliance-based framework toward a model driven by distributions of known building characteristics.

## Building System Turnover and Effective Useful Life

We assume that all major building systems are installed when the building is constructed, and that they are replaced periodically over the lifespan of the building. Replacements may be made because of equipment failure, building remodeling, energy efficiency upgrades, etc. To model the turnover of building systems, it is necessary to understand how often these building systems are replaced, which determines how long they last in the building stock. The metric commonly used by the energy efficiency community to describe the lifespan of a measure is effective useful life (EUL). The California Public Utilities Commission defines EUL as “an estimate of the median number of years that the measures installed under the program are still in place and operable” (California Public Utilities Commission 2020). In the reliability community, EUL is typically referred to as “median time to failure” (Texas Instruments 2021), whereas ASHRAE uses the term “median service life” (Abramson et al. 2006).

For ComStock, the primary source of EULs is the California Public Utilities Commission (CPUC) Database of Energy Efficiency Resources (DEER) (California Public Utilities Commission 2021). Previous work on EULs indicates that there is wide variation in the quality of national EUL data, but it also indicates that the studies performed in DEER are generally the best available (Skumatz 2012). The values in DEER were cross-referenced against the lifetimes used in the EIA NEMS Commercial Demand Module (U.S. Energy Information Administration 2017a) and the ASHRAE Service Life and Maintenance Cost Database (ASHRAE 2021). Table <a href="#tab:effective_useful_life" data-reference-type="ref" data-reference="tab:effective_useful_life">2</a> shows the EULs assumed for different building systems in ComStock.

<div id="tab:effective_useful_life">

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

As part of the DOE-funded Advanced Building Construction initiative, a team collected information on windows from a variety of commercial building surveys, including a new survey of buildings built since roughly 2010. Unfortunately, while most of the surveys did ask about windows, only one survey had enough information to perform a reliability analysis (because windows are long-lived). This survey was the 2014 Commercial Building Stock Analysis (Navigant Consulting 2014), which covers the Pacific Northwest. This survey included information on the age of the building, whether the windows had ever been replaced (and if so, an estimate of the year of replacement), and a weighting factor to describe how each sample fit into the whole building population. From these data, we performed a reliability analysis. Figure <a href="#fig:comWindowSurvivalCurve" data-reference-type="ref" data-reference="fig:comWindowSurvivalCurve">2</a> shows the estimated survival curve. As indicated by the black cross mark on the figure, the EUL estimate for windows is 70 years. However, the maximum lifespan extends to more than 400 years. In practice, this indicates that windows on some buildings will never be replaced.

<figure id="fig:comWindowSurvivalCurve">
<img src="figures/window_survival_curve.png" style="width:60.0%" />
<figcaption>Reliability analysis for windows in commercial buildings, from 2014 CBSA <span class="citation" data-cites="neea2014cbsa">(Navigant Consulting 2014)</span>.</figcaption>
</figure>

#### Walls and Roofs

None of the data sources we identified included information on EULs for walls and roofs, or, more specifically, the insulation on these surfaces. DEER EULs are capped at 20 years, per CPUC policy. NEMS does not appear to model wall turnover separately from whole-building replacement. Based on engineering judgment, we selected an EUL of 200 years to indicate that for most buildings, the wall and roof insulation will not be replaced before the building is demolished.

### Distribution of Lifespans

The EUL estimates in Figure <a href="#fig:comWindowSurvivalCurve" data-reference-type="ref" data-reference="fig:comWindowSurvivalCurve">2</a> represent the median lifespan for a given building system. However, not all systems will fail and be replaced after exactly that amount of time. To represent this diversity of failure rates we use a distribution.

The simplest approach would be to use a normal distribution centered on the EUL. However, studies of reliability data show that this is not a good assumption; instead, these studies often use a Weibull distribution to represent lifetimes. To check whether a Weibull distribution accurately represented the lifetimes of building equipment, we performed a reliability analysis on data from the ASHRAE Service Life and Maintenance Cost Database (ASHRAE 2021). This analysis was performed following the methodology described in an ASHRAE journal article (Hiller 2000), and was implemented using the reliability package (Reid 2020) in Python. Four categories of equipment with a reasonable number of entries were investigated: air handling units, boilers, chillers, and air source DX equipment (all types of each available in the database).

<figure id="fig:hvac_survival_curves" data-latex-placement="ht!">
<img src="figures/ashrae_equip_lifespans2.png" />
<figcaption>Survival curves and derived lifespan probability density functions for commercial HVAC equipment.</figcaption>
</figure>

As shown in Figure <a href="#fig:hvac_survival_curves" data-reference-type="ref" data-reference="fig:hvac_survival_curves">3</a>, Weibull distributions are a good fit for several categories of HVAC equipment failure data. Although the ASHRAE database includes data for many different types of HVAC equipment, it was not selected as the primary source for deriving EULs for ComStock due to the limitations and biases in the database described by its creators (Abramson et al. 2006). Instead, we decided to use the EUL sources described in Table <a href="#tab:effective_useful_life" data-reference-type="ref" data-reference="tab:effective_useful_life">2</a> and develop Weibull curve parameters around these EULs. The selected parameters are shown in Table <a href="#tab:eul_distributions" data-reference-type="ref" data-reference="tab:eul_distributions">3</a>. For the 70-year EUL, the parameters came from the window reliability analysis. For the 10-, 15-, and 20-year EULs, the only constraint was to match the EUL definition: 50% of the equipment would still be operable at the EUL. A minimum lifespan of 60% of the EUL was selected with the assumption that although individual components of a system might fail, it is unlikely that products on the market routinely fail at a whole-building scale in only a few years. The 200-year EUL parameters were selected to represent no failure for the life of the building.

<div id="tab:eul_distributions">

| **EUL** | **Shape (beta)** | **Scale (alpha)** | **Shift (gamma)** |
|:-------:|:----------------:|:------------------|:------------------|
|   10    |       1.6        | EUL / 2 = 5       | EUL \* 0.6 = 6    |
|   15    |       1.6        | EUL / 2 = 7.5     | EUL \* 0.6 = 9    |
|   20    |       1.6        | EUL / 2 = 10      | EUL \* 0.6 = 12   |
|   70    |       1.3        | 91                | 0                 |
|   200   |       1.0        | 1                 | 200               |

Commercial Equipment Lifetime Weibull Distribution Parameters

</div>

## Commercial Refrigeration Equipment

<figure id="fig:refrigeration_survival_curves" data-latex-placement="ht!">
<img src="figures/refrigeration_survival_curves_combined.png" />
<figcaption>Weibull survival curves for commercial refrigeration equipment in large and small/medium grocery buildings.</figcaption>
</figure>

We represent commercial refrigeration equipment lifetimes using Weibull survival functions fit to effective useful lives (EULs) informed by the U.S. Department of Energy’s *Commercial Refrigeration Equipment* Technical Support Document (U.S. Department of Energy 2024). Consistent with the TSD’s market framing and industry practices, we differentiate between large grocery buildings (often owned or operated by national chains) and medium/small grocery buildings (more often independently owned).

For large groceries, we assume earlier replacement decisions driven by risk management, reliability requirements, and chain-wide retrofit programs that standardize fleets. We therefore assign a shorter EUL of 10 years. For medium and small groceries, where equipment is commonly retained until failure or when repair costs become prohibitive, we assign a longer EUL of 15 years. These assumptions align with the ownership and operations context underlying DOE’s CRE analyses and shipments modeling (U.S. Department of Energy 2024).

We parameterize shifted-Weibull survival functions such that (i) 50% survival occurs at the EUL (our operational definition of EUL), and (ii) a minimum lifespan threshold of roughly 60% of the EUL avoids unrealistic early whole-system failures. The resulting parameters are listed in Table <a href="#tab:refrigeration_eul_distributions" data-reference-type="ref" data-reference="tab:refrigeration_eul_distributions">4</a>. These distributions produce the combined survival curves shown in Figure <a href="#fig:refrigeration_survival_curves" data-reference-type="ref" data-reference="fig:refrigeration_survival_curves">4</a> and are used to schedule replacements and retirements in ComStock’s stock-turnover logic.

<div id="tab:refrigeration_eul_distributions">

| **EUL** | **Shape (beta)** | **Scale (alpha)** | **Shift (gamma)** |
|:-------:|:----------------:|:------------------|:------------------|
|   10    |      6.995       | 10.691            | 1.0               |
|   15    |      7.343       | 21.300            | 1.0               |

Commercial Refrigeration Equipment Weibull Distribution Parameters

</div>

## Space Type Ratios

A space type refers to a portion of a building that has a distinct usage, purpose, occupancy schedule, thermostat set point, etc. Most buildings have multiple space types. For example, schools typically have classrooms, hallways, restrooms, cafeterias, etc. In ComStock, each building type is assumed to have a fixed ratio of various space types relative to the total building floor area. For buildings outside of California, the space type ratios were largely taken from the DOE commercial reference building models (Deru et al. 2011b). For buildings in California, the space type ratios were largely taken from the DEER prototype models (California Public Utilities Commission 2021). There are certain building types that have altered ratios or are a mix of building types. For example in ComStock, warehouses include both unconditioned storage facilities and light manufacturing. Warehouse building subtypes alter the ratio of bulk storage. Retail strip mall buildings have different ratios of restaurant space types, with the default being 20%. Two examples of space type ratios are shown in Table <a href="#tab:space_type_ratios" data-reference-type="ref" data-reference="tab:space_type_ratios">5</a>. See Table <a href="#tab:space_type_ratios_all" data-reference-type="ref" data-reference="tab:space_type_ratios_all">[tab:space_type_ratios_all]</a> for the space type ratios for all building types.

<div id="tab:space_type_ratios">

| **Building Type** | **Building Subtype**    | **Space Type**      | **Ratio** |
|:------------------|:------------------------|:--------------------|:---------:|
| Warehouse         | warehouse_default       | Bulk                |    66%    |
| Warehouse         | warehouse_default       | Fine                |    29%    |
| Warehouse         | warehouse_default       | Office              |    5%     |
| Retail Strip Mall | strip_mall_restaurant20 | Strip mall - type 1 |    20%    |
| Retail Strip Mall | strip_mall_restaurant20 | Strip mall - type 2 |    20%    |
| Retail Strip Mall | strip_mall_restaurant20 | Strip mall - type 3 |    40%    |
| Retail Strip Mall | strip_mall_restaurant20 | Dining              |    15%    |
| Retail Strip Mall | strip_mall_restaurant20 | Kitchen             |    5%     |

Space Type Ratio Example

</div>

## Weather Data

ComStock can be run with two different types of weather data: typical meteorological year (TMY3) and actual meteorological year (AMY). AMY data is the data measured during a specific year, taken from weather stations such as those at airports. Because these data are from a particular calendar year, weather patterns that span large areas, such as nationwide heat waves, are captured in the data across multiple locations. Therefore, these weather patterns are captured in the outputs of ComStock. This is important for use cases where coordinated weather patterns influence loads, such as peak load impacts for bulk power grid planning. TMY3 data, in contrast, take the “most typical” weather for each calendar month from a 30-year historical record and stitch these months together to form a complete year. The advantage of this method is that the weather data is less influenced by an extremely hot or cold year. However, this approach does not capture wide-area weather patterns, as the month of data used varies from location to location. For a more in-depth discussion of AMY and TMY3 weather data, see (Wilson et al. 2022).

For geographic granularity, ComStock currently uses one weather file for each county in the United States. For counties with no weather data available (generally sparsely populated rural areas), data from the nearest weather station in the same climate zone are used. See (Wilson et al. 2022) for a more in-depth discussion of the weather data sources, cleaning process, and assignment assumptions.

## Soil Properties

Soil thermal conductivity and undisturbed ground temperature are location-dependent properties that are required in the ComStock model by several goethermal heat pump upgrade measures. Therefore, these properties are part of the ComStock sampling workflow and are stored as additionl properties in the building models, which can then be used by downstream measures. Soil thermal conductivity distributions by climate zone were dervied from a dataset produced by the Southern Methodist University Geothermal Lab, and are shown in Table <a href="#fig:soil_conductivity" data-reference-type="ref" data-reference="fig:soil_conductivity">[fig:soil_conductivity]</a> ((Dedman College of Humanities and Sciences; Roy M Huffington Department of Earth Sciences 2023)). The soil thermal conductivity values range from 0.5 to 2.6 W/m-K. Average undisturbed ground temperatures by climate zone were derived from a 2014 Oklahoma State University study and are shown in Table <a href="#tab:undisturbed_ground_temp" data-reference-type="ref" data-reference="tab:undisturbed_ground_temp">[tab:undisturbed_ground_temp]</a> ((Xing 2014)).

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-ashrae_reliability_db_article" class="csl-entry">

Abramson, Barry, Lung-Sing Wong, and David L. Herman. 2006. “Service Life Data from an Interactive Web-Based Owning and Operating Cost Database.” *ASHRAE Transactions* 112 (1): 81-92.

</div>

<div id="ref-ashrae_reliability_db" class="csl-entry">

ASHRAE. 2021. *ASHRAE Owning and Operating Cost Database*. Http://weblegacy.ashrae.org/publicdatabase/summary.asp.

</div>

<div id="ref-building_codes_assistance" class="csl-entry">

Building Codes Assistance Project. 2021. *Code Status Maps: Commercial Energy Code Adoption*. Http://bcapcodes.org/code-status/.

</div>

<div id="ref-cpuc_ee_manual" class="csl-entry">

California Public Utilities Commission. 2020. *Energy Efficiency Policy Manual Version 6 for Post-2018 Programs*. California Public Utilities Commission. <https://www.cpuc.ca.gov/-/media/cpuc-website/files/legacyfiles/e/6442465683-eepolicymanualrevised-march-20-2020-b.pdf>.

</div>

<div id="ref-cpuc_deer" class="csl-entry">

California Public Utilities Commission. 2021. *Database for Energy Efficient Resources*. <a href="http://deeresources.com/" class="uri">Http://deeresources.com/</a>.

</div>

<div id="ref-smu_soil_conductivity" class="csl-entry">

Dedman College of Humanities and Sciences; Roy M Huffington Department of Earth Sciences. 2023. “SMU Geothermal Lab \| Data and Maps \| Temperature Maps.” <https://www.smu.edu/dedman/academics/departments/earth-sciences/research/geothermallab/datamaps/temperaturemaps>.

</div>

<div id="ref-doe_reference_buildings" class="csl-entry">

Deru, M, K Field, D Studer, et al. 2011a. *U.s. Department of Energy Commercial Reference Building Models of the National Building Stock*. National Renewable Energy Laboratory. <https://doi.org/10.2172/1009264>.

</div>

<div id="ref-deru_2011" class="csl-entry">

Deru, M, K Field, D Studer, et al. 2011b. *U.s. Department of Energy Commercial Reference Building Models of the National Building Stock*. NREL/TP-5500-46861. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy11osti/46861.pdf>.

</div>

<div id="ref-determine_equip_life" class="csl-entry">

Hiller, Carl. 2000. “Determining Equipment Service Life.” *ASHRAE Journal* 42 (August): 48-50+52.

</div>

<div id="ref-neea2014cbsa" class="csl-entry">

Navigant Consulting. 2014. *2014 Commercial Building Stock Assessment: Final Report*. <a href="https://neea.org/resources/2014-cbsa-final-report" class="uri">Https://neea.org/resources/2014-cbsa-final-report</a>.

</div>

<div id="ref-matthew_reid_2020_3938000" class="csl-entry">

Reid, Matthew. 2020. *MatthewReid854/Reliability: V0.5.1*. Version v0.5.1. <https://doi.org/10.5281/zenodo.3938000>.

</div>

<div id="ref-what_makes_good_eul" class="csl-entry">

Skumatz, Lisa A. 2012. “What Makes a Good EUL? Analysis of Existing Estimates and Implications for New Protocols for Estimated Useful Lifetimes (EULs).” *2012 International Energy Program Evaluation Conference, Rome, Italy*. <https://energy-evaluation.org/wp-content/uploads/2019/06/2012-iepec-skumatz-eul-v5-revised.pdf>.

</div>

<div id="ref-ti_reliability_website" class="csl-entry">

Texas Instruments. 2021. *Reliability Terminology*. <https://www.ti.com/support-quality/reliability/reliability-terminology.html>.

</div>

<div id="ref-doe_cre_tsd" class="csl-entry">

U.S. Department of Energy. 2024. *Technical Support Document: Energy Efficiency Program for Consumer Products and Commercial and Industrial Equipment: Commercial Refrigeration Equipment*. Office of Energy Efficiency; Renewable Energy, Building Technologies Program. <https://www.regulations.gov/document/EERE-2017-BT-STD-0007-0118>.

</div>

<div id="ref-nems_com_demand_module" class="csl-entry">

U.S. Energy Information Administration. 2017a. *Commercial Demand Module of the National Energy Modeling System: Model Documentation*. U.S. Energy Information Administration. <https://www.eia.gov/outlooks/aeo/nems/documentation/commercial/pdf/m066(2017).pdf>.

</div>

<div id="ref-icf_com_code_compliance_status" class="csl-entry">

U.S. Energy Information Administration. 2017b. *Residential and Commercial Sector Energy Code Adoption and Compliance Rates*. U.S. Energy Information Administration. <https://www.eia.gov/analysis/studies/rescomm/adoptcomprates/pdf/adoption_compliance.pdf>.

</div>

<div id="ref-eulp_final_report" class="csl-entry">

Wilson, Eric J. H., Andrew Parker, Anthony Fontanini, et al. 2022. *End-Use Load Profiles for the u.s. Building Stock: Methodology and Results of Model Calibration, Validation, and Uncertainty Quantification*. National Renewable Energy Laboratory. <https://doi.org/10.2172/1854582>.

</div>

<div id="ref-xing2014" class="csl-entry">

Xing, L. 2014. “Estimations of Undisturbed Ground Temperatures Using Numerical and Analytical Modeling.” PhD thesis, Oklahoma State University.

</div>

</div>
