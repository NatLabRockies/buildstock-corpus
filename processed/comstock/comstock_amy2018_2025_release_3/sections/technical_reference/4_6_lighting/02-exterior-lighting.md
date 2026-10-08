<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_6_lighting.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_6_lighting.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0396270 | corpus_path: technical_reference/documentation/reference_doc/4_6_lighting.md | section: Exterior Lighting | lines: 186-251 -->
## Exterior Lighting

Exterior lighting is all outdoor lighting at the building site, including lighting for parking, walkways, doorways, canopies, building facades, signage, and landscaping.

### Parking Area Lighting

Parking area lighting accounts for the majority of exterior lighting in the stock (Buccitelli et al. 2017). Parking lighting is calculated as the parking area times the installed lighting power per unit of parking area. Parking area is based on the estimated number of parking spots per student for schools, per unit for hotels, per bed for hospitals, and per building floor area for all other building types. Parking spots are assumed to be 405 ft$`^2`$. Table “Parking; Values From osti_1015277 Table 4.17” details these assumptions.

Lighting power for a given parking area is determined from the 2015 U.S. Lighting Market Characterization report, which assumes an average of 216 Watts (W) per parking lighting system, or 0.0410 W/ft<sup>2</sup> (per equation ext_light_eqn). Base parking lighting power allowance values for each vintage were reduced by a calculated factor such that the building-count weighted parking lighting power density came out to the 0.0410 W/ft<sup>2</sup> target. Note that this calculation is from 2015, so it overestimates the amount of exterior lighting in the stock, which has been changing over to use LEDs. The values for each vintage are shown in Table “Exterior Lighting Power”.

``` math
\begin{align}
\label{ext_light_eqn}
LPD = \left(\frac{216\,W}{\text{lighting system}}\right) \cdot \left(\frac{1\,\text{lighting system}}{13\,\text{parking spots}}\right) \cdot \left(\frac{1\,\text{parking spot}}{405\,\text{ft}^2}\right) = 0.0410\,W/\text{ft}^2
\end{align}
```

### Other Exterior Lighting

Non-parking exterior lighting is determined by the exterior lighting allowance specified in ASHRAE 90.1 for exterior lighting zone 3 (All Other Areas). Length and area estimates are determined from the values in Table “Entryways; Values From osti_1015277 Table 4.18”. The building facade area is calculated from the model as the ground floor exterior wall area. The lighting power allowance is matched to the 90.1 code for each vintage. The exterior lighting power allowances are shown in Table “Exterior Lighting Power”. Note that although 90.1 includes exterior lighting, the only forms of exterior lighting included in ComStock are parking areas, building facades, main entry doors, other doors, drive through windows, entry canopies, and emergency canopies. Notably, ComStock does not include lighting for exterior signage.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-doe2015lmc" class="csl-entry">

Buccitelli, Nicole, Clay Elliott, Seth Schober, and Mary Yamada. 2017. *2015 u.s. Lighting Market Characterization*. U.S. Department of Energy.

</div>

<div id="ref-neea2019cbsa" class="csl-entry">

Cadmus Group. 2019. *Commercial Building Stock Assessment 4 (2019) Final Report*. Northwest Energy Efficiency Alliance.

</div>

<div id="ref-deru_2011" class="csl-entry">

Deru, M, K Field, D Studer, et al. 2011. *U.s. Department of Energy Commercial Reference Building Models of the National Building Stock*. NREL/TP-5500-46861. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy11osti/46861.pdf>.

</div>

<div id="ref-ashrae_rp1282" class="csl-entry">

Fisher, D., and C. Chantrasrisalai. 2006. *Lighting Heat Gain Distribution in Buildings*. ASHRAE.

</div>

<div id="ref-ashrae_rp1681" class="csl-entry">

Liu, Ran, Xiaohui Zhou, Scott Lochhead, Zhikun Zhong, and Cuong Van Huynh. 2016. *Low Energy LED LIghting Heat Distribution in Buildings*. ASHRAE.

</div>

<div id="ref-eulp_final_report" class="csl-entry">

Wilson, Eric J. H., Andrew Parker, Anthony Fontanini, et al. 2022. *End-Use Load Profiles for the u.s. Building Stock: Methodology and Results of Model Calibration, Validation, and Uncertainty Quantification*. National Renewable Energy Laboratory. <https://doi.org/10.2172/1854582>.

</div>

<div id="ref-doe2019ssl" class="csl-entry">

Yamada, Mary, Julie Penning, Seth Schober, Kyung Lee, and Clay Elliott. 2019. *Energy Savings Forecast of Solid-State Lighting in General Illumination Applications*. U.S. Department of Energy.

</div>

</div>
