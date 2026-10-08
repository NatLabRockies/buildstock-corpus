<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: fadc83e | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: Refrigeration | lines: 2085-2293 -->
## Refrigeration

In ComStock, refrigeration systems refer to the refrigerated cases and walk-ins found in commercial kitchens, grocery stores, and other food service spaces. Small plug-in refrigerators are included in plug and process loads, as described in Section <a href="#sec:plug_and_process_loads" data-reference-type="ref" data-reference="sec:plug_and_process_loads">[sec:plug_and_process_loads]</a>. Refrigeration is modeled in building types where it is a major end use (primary and secondary schools, restaurants, hotels, hospitals, and grocery stores).

### Walk-ins and Case Scaling

Earlier versions of ComStock used fixed-size walk-in coolers and freezers for each building kitchen zone. This has been replaced with a scaling approach: refrigeration equipment is now sized according to the floor area of the associated space type (such as kitchens, stock rooms, or grocery sales areas). Rather than applying fixed case or walk-in sizes, ComStock uses reference space types to establish a ratio of refrigerated area or case length to total floor area. For example, a reference space type might assume 20,000 ft$`^2`$ of grocery sales area with 400 ft of refrigerated cases; this ratio of case type to floor area is then scaled to the actual space type floor area in the model. This scaling approach is consistent with the best available data sources and has been validated through in-person site visits performed by NREL staff, providing confidence that modeled refrigeration capacities align with real-world practice.

### Technology Level Assignment

Refrigeration systems are now characterized by probabilistic assignment of technology levels: *old*, *new*, and *advanced*. These levels represent distributions of baseline efficiency as a function of both building vintage and building size. Technology levels influence compressor efficiency, case lighting, fan motors, and defrost cycles. This approach allows ComStock to capture variability in stock performance, from legacy systems to modern ENERGY STAR<sup>®</sup>-like equipment (U.S. Department of Energy 2009; U.S. Environmental Protection Agency 2001).

The assignment of technology levels draws from three TSVs:

- *include_refrigeration_technology_level.tsv* flags buildings with refrigeration.

- *year_bin_of_last_refrigeration_replacement.tsv* assigns the year range of the last major equipment replacement, based on survival curves (see Section <a href="#sec:refrigeration_survival" data-reference-type="ref" data-reference="sec:refrigeration_survival">[sec:refrigeration_survival]</a>).

- *refrigeration_technology_level.tsv* probabilistically assigns equipment efficiency distributions based on year built, replacement year, and building size.

Figure <a href="#fig:refrigeration_tech_distribution" data-reference-type="ref" data-reference="fig:refrigeration_tech_distribution">17</a> illustrates the resulting distribution of refrigeration technology levels by building size and year of last replacement.

### Efficiency Distributions

Efficiency distributions for refrigeration equipment are derived from DOE Technical Support Documents, ENERGY STAR<sup>®</sup> archives, ASHRAE research, and utility/laboratory studies (U.S. Department of Energy 2009; Fricke and Becker 2010; California Energy Commission 2006). Historical data show a clear trend of improvement:

- Pre-1990 equipment had very high energy intensities (e.g., 0.3-0.4 kWh/ft$`^3`$/day for reach-in refrigerators, 2.5-3.0 kWh/ft/day for open vertical cases).

- 1990s equipment introduced modest improvements (better insulation, new refrigerants), but performance was still poor by modern standards.

- Early 2000s saw the introduction of ENERGY STAR<sup>®</sup> criteria and California Title 20 standards, driving significant efficiency gains in reach-ins, freezers, and merchandisers.

- By the late 2000s, most new commercial refrigeration equipment met or exceeded federal standards, with widespread adoption of LED case lighting, ECM fan motors, anti-sweat heater controls, and night covers.

These historical shipment distributions were mapped to *old*, *new*, and *advanced* efficiency levels using Oak Ridge National Laboratory (ORNL) performance data embedded in OpenStudio Standards. In practice, ComStock samples from these distributions to assign performance characteristics to each refrigeration system. Approximate efficiency values by technology level are summarized in Table <a href="#tab:refrigeration_efficiency_levels" data-reference-type="ref" data-reference="tab:refrigeration_efficiency_levels">19</a>. This ensures the resulting stock reflects both legacy equipment and the adoption of modern efficiency measures over time.

<div class="threeparttable">

<div id="tab:refrigeration_efficiency_levels">

| **Equipment Category** | **Old (Legacy / Pre-Standard)** | **New (Standard-Era Baseline)** | **Advanced (High Efficiency / ENERGY STAR)** |
|:---|:---|:---|:---|
| Reach-in Refrigerators (solid/glass door) | 0.30-0.40 kWh/ft$`^3`$/day | 0.20-0.30 kWh/ft$`^3`$/day | 0.15-0.20 kWh/ft$`^3`$/day |
| Reach-in Freezers | 0.50-0.60 kWh/ft$`^3`$/day | 0.40-0.50 kWh/ft$`^3`$/day | 0.30-0.40 kWh/ft$`^3`$/day |
| Vertical Open Display Cases (medium-temp) | 2.3-3.0 kWh/ft/day | 1.8-2.3 kWh/ft/day | 1.2-1.6 kWh/ft/day |
| Horizontal/Coffin Freezers (low-temp) | 2.0-2.5 kWh/ft/day | 1.5-2.0 kWh/ft/day | 1.0-1.4 kWh/ft/day |
| Walk-in Coolers (8$`\times`$<!-- -->8 typical) | 0.07-0.09 kWh/ft$`^3`$/day | 0.05-0.07 kWh/ft$`^3`$/day | 0.03-0.05 kWh/ft$`^3`$/day |
| Walk-in Freezers (8$`\times`$<!-- -->8 typical) | 0.14-0.18 kWh/ft$`^3`$/day | 0.11-0.14 kWh/ft$`^3`$/day | 0.08-0.11 kWh/ft$`^3`$/day |

Approximate efficiency levels for refrigeration equipment categories (illustrative ranges).

</div>

<div class="tablenotes">

Values represent typical daily energy use intensities under standard test conditions, used to define the “Old,” “New,” and “Advanced” technology levels applied in ComStock. Ranges are derived from DOE Technical Support Documents, ENERGY STAR<sup>®</sup> criteria, and ASHRAE/utility research studies, and mapped to OpenStudio Standards performance data.

</div>

</div>

### System Types and Controls

Refrigeration configurations also vary by building type and size. Large grocery stores almost universally use centralized compressor rack systems serving dozens of cases and walk-ins, while small-format stores rely on self-contained units (U.S. Energy Information Administration 2018b). Efficiency technologies such as floating head pressure control, variable-speed compressors, adaptive defrost, and LED case lighting are incorporated in proportion to their historical and present-day adoption levels. For example:

- Floating head pressure control was common by the late 1990s and is standard in modern racks.

- Variable-speed compressors and VFD-controlled condenser fans are now standard in new systems.

- Adaptive defrost and anti-sweat heater controls are widely adopted in newer or retrofitted equipment.

- Medium-temperature case doors, once rare, are now installed in roughly half of all modern supermarkets, reflecting a major retrofit trend.

### Summary

In summary, ComStock’s refrigeration modeling now:

- Scales walk-in and case sizes based on space type floor area, validated against site visits and data sources;

- Applies survival-based replacement schedules to reflect realistic equipment lifetimes (Section <a href="#sec:refrigeration_survival" data-reference-type="ref" data-reference="sec:refrigeration_survival">[sec:refrigeration_survival]</a>);

- Assigns technology levels probabilistically, capturing distributions of baseline efficiency by vintage and size, based on DOE shipment data mapped to OpenStudio Standards performance levels;

- Incorporates adoption of modern refrigeration efficiency measures and retrofit trends.

This methodology ensures that ComStock refrigeration energy use better reflects the diversity of U.S. commercial building stock, including both legacy equipment and advanced technologies.

<figure id="fig:refrigeration_tech_distribution">
<img src="figures/refrigeration_tech_distribution.png" style="width:90.0%" />
<figcaption>Distribution of refrigeration technology levels (old, new, advanced) by building size and year of last replacement. Based on DOE shipment data mapped to OpenStudio Standards performance levels.</figcaption>
</figure>

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-ashrae_62.1_2004" class="csl-entry">

ASHRAE. 2004. *Ventilation for Acceptable Indoor Air Quality*. <a href="https://ashrae.iwrapper.com/ASHRAE_PREVIEW_ONLY_STANDARDS/STD_62.1_2019" class="uri">Https://ashrae.iwrapper.com/ASHRAE_PREVIEW_ONLY_STANDARDS/STD_62.1_2019</a>.

</div>

<div id="ref-CEC_Title20" class="csl-entry">

California Energy Commission. 2006. *Appliance Efficiency Regulations (Title 20)*. California Energy Commission. <https://www.energy.ca.gov/rules-and-regulations/appliance-efficiency-regulations>.

</div>

<div id="ref-unocc_hvac_paper" class="csl-entry">

CaraDonna, Chris, and Kelsea Dombrovski. 2022. “Air Handling Unit Shutdowns During Scheduled Unoccupied Hours: US Commercial Building Stock Prevalence and Energy Impact.” *ASME Journal of Engineering for Sustainable Buildings and Cities* 3 (4). <https://doi.org/10.1115/1.4055887>.

</div>

<div id="ref-carrier_economiser" class="csl-entry">

Carrier. 2023. *Carrier Economizer*.

</div>

<div id="ref-osti_1889192" class="csl-entry">

Crowe, Eliot, Yimin Chen, Jessica Granderson, et al. 2022. “What We Learned from Analyzing 18 Million Rows of Commercial Buildings’ HVAC Fault Data.” *2022 Summer Study on Energy Efficiency in Buildings*, August. <https://www.osti.gov/biblio/1889192>.

</div>

<div id="ref-daikin_rebel" class="csl-entry">

Daikin. 2023. *Rebel Commercial Packaged Rooftop Systems*.

</div>

<div id="ref-osti_1457127" class="csl-entry">

Frank, Stephen M, Janghyun Kim, Jie Cai, and James E. Braun. 2018. *Common Faults and Their Prioritization in Small Commercial Buildings: February 2017 - December 2017*. National Renewable Energy Laboratory. <https://doi.org/10.2172/1457127>.

</div>

<div id="ref-Fricke2010" class="csl-entry">

Fricke, Brian, and B. Becker. 2010. “Energy Use of Doored and Open Vertical Refrigerated Display Cases.” *ASHRAE Journal*, 44-52.

</div>

<div id="ref-heinemeier2014free" class="csl-entry">

Heinemeier, Kristin. 2014. “Free Cooling: At What Cost?” *ACEEE Summer Study Energy Efficiency Build*.

</div>

<div id="ref-mascontrol3" class="csl-entry">

Hirsch, J. J. 2021. *MasControl 3*. <https://cedars.sound-data.com/deer-resources/tools/mas-control/>.

</div>

<div id="ref-osti_1829706" class="csl-entry">

Katipamula, Srinivas, Ronald M. Underhill, Nicholas EP Fernandez, Woohyun Kim, Robert G. Lutes, and Danny J. Taasevigen. 2021. “Prevalence of Typical Operational Problems and Energy Savings Opportunities in u.s. Commercial Buildings.” *Energy and Buildings* 253 (December). <https://doi.org/10.1016/j.enbuild.2021.111544>.

</div>

<div id="ref-doi_10_1080_23744731_2021_1898243" class="csl-entry">

Kim, Janghyun, Trenbath Kim, Jessica Granderson, et al. 2021. “Research Challenges and Directions in HVAC Fault Prevalence.” *Science and Technology for the Built Environment* 27 (5): 624-40. <https://doi.org/10.1080/23744731.2021.1898243>.

</div>

<div id="ref-seventhwave_rtu" class="csl-entry">

Seventhwave and Center for Energy and Environment. 2016. *Commercial Roof-Top Units in Minnesota: Characteristics and Energy Performance*. Minnesota Department of Commerce Division of Energy Resources. <https://slipstreaminc.org/research/commercial-roof-top-units-minnesota-characteristics-and-energy-performance>.

</div>

<div id="ref-osti_1665808" class="csl-entry">

Shoukas, Greg, Marcus Bianchi, and Michael Deru. 2020. *Analysis of Fault Data Collected from Automated Fault Detection and Diagnostic Products for Packaged Rooftop Units*. National Renewable Energy Laboratory. <https://doi.org/10.2172/1665808>.

</div>

<div id="ref-trane_foundation" class="csl-entry">

Trane. 2023. *Packaged Rooftop Air Conditioners Foundation*.

</div>

<div id="ref-DOE_TSD_2009" class="csl-entry">

U.S. Department of Energy. 2009. *Energy Conservation Standards for Refrigerated Beverage Vending Machines: Technical Support Document*. U.S. Department of Energy. <https://www.energy.gov/eere/buildings/appliance-and-equipment-standards-program>.

</div>

<div id="ref-eia2018cbecs" class="csl-entry">

U.S. Energy Information Administration. 2018a. *2018 Commercial Building Energy Consumption Survey (CBECS)*. Https://www.eia.gov/consumption/commercial/data/2018/.

</div>

<div id="ref-EIA_FoodSales2018" class="csl-entry">

U.S. Energy Information Administration. 2018b. *Commercial Buildings Energy Consumption Survey (CBECS): Food Sales*. U.S. Energy Information Administration. <https://www.eia.gov/consumption/commercial>.

</div>

<div id="ref-ENERGYSTAR_Refrigeration" class="csl-entry">

U.S. Environmental Protection Agency. 2001. *ENERGY STAR Program Requirements for Commercial Refrigerators and Freezers*. U.S. Environmental Protection Agency; U.S. Department of Energy. <https://www.energystar.gov>.

</div>

</div>
