<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_6_lighting.tex -->
# Lighting

## Interior Lighting

Interior lighting follows a technology baseline approach, meaning that energy consumed by lighting is set by an assumed distribution of a particular lighting technology (e.g., T8 or linear LEDs), rather than following a lighting power density (LPD) allowance defined in a specific energy code version. The technology baseline approach recognizes that buildings typically do not use their full lighting power allowance. It also explicitly labels lighting technology and subsystems in the energy model for granular energy efficiency measure analysis.

Two components specify interior lighting: the lighting power density and the interior lighting schedule. The lighting power density is determined by the distribution of lighting technologies in the stock, the lighting technology properties, and the space type properties. The lighting schedule is determined by a default lighting schedule by space type, occupancy hour adjustments, and magnitude variability.

### Determining Lighting Power

The technology baseline approach follows a similar process to how the ASHRAE 90.1 lighting subcommittee determines the LPD allowance for a given space type in ASHRAE 90.1. In the lighting subcommittee model (LSM), there are four kinds of lighting systems that together contribute to a target horizontal illuminance:

LPD = General Lighting + Task Lighting + Supplemental Lighting + Wall Wash Lighting\
``` math
\begin{align}
\label{lsm_lpd_eqn}
LPD = \frac{\% LS_{1} \cdot fc}{RSDD \cdot TF_{1}} + \frac{\% LS_{2} \cdot fc}{RSDD \cdot TF_{2}} + \frac{\% LS_{3} \cdot fc}{RSDD \cdot TF_{3}} + \frac{\% LS_{4} \cdot fc}{RSDD \cdot TF_{4}}
\end{align}
```
where:\

- **%LS<sub>i</sub>** is the percent of the target horizontal illuminance value met by a specific lighting system\

- **fc** is the target horizontal illuminance value in lumens per ft<sup>2</sup>\

- **RSDD** is room surface dirt depreciation, an estimate of how much surface dirt reduces light from reaching the horizontal plane\

- **TF<sub>i</sub>** is the total lighting factor, where TF = source luminous efficacy \* coefficient of utilization \* lighting loss factor (LFF)\

- **Source luminous efficacy** is the lighting technology efficacy in lumens per watt\

- **Coefficient of utilization** is a term that captures how much lighting from the luminaire reaches the horizontal plane\

- **LLF** is the lighting loss factor, where LLF = luminaire dirt depreciation (LDD) \* lamp lumen depreciation (LLD)\

Values for all these terms are specified in the LSM. The LSM is exact, using a specific lighting product, room geometry, distribution of lighting systems, and other properties to determine the lighting power density allowance for a given space type. ComStock differs from the LSM in several important ways.

First, ComStock generalizes lighting technology (e.g., T8 linear fluorescent luminaires for general lighting) rather than modeling a specific lighting product. Source efficacy, lighting loss properties, and radiant fractions are tied to lighting technology. Source efficacy values come from (Buccitelli et al. 2017) for older lighting technologies and (Yamada et al. 2019) for LEDs. Radiant heat gain fractions come from (Fisher and Chantrasrisalai 2006) for older lighting technologies and (Liu et al. 2016) for LEDs.

Second, lighting technologies are broken out into lighting generations depending on the most common space lighting technology in that generation, as general lighting accounts for most ($`\sim`$<!-- -->80%–90%) of total lighting. High bay is treated as general lighting, and the lighting measure uses the general high bay technology for rooms with height $`\ge`$<!-- -->20 ft. Lighting generations 4-8 are all LED, with improving efficacy over time. Lighting generations and their technologies are detailed in Table <a href="#tab:int_light_gens" data-reference-type="ref" data-reference="tab:int_light_gens">1</a>, and lighting technology properties are detailed in Table <a href="#tab:int_light_techs_all" data-reference-type="ref" data-reference="tab:int_light_techs_all">[tab:int_light_techs_all]</a>.

Third, the coefficient of utilization depends on both the luminaire properties and the room geometry, which complicates the calculation in the LSM. The ComStock model associates the coefficient of utilization entirely with room propertiesthat are independent of lighting technology. ComStock further assumes that rooms of the same space type have similar enough properties that they can use the same coefficient of utilization. To retain some of the variation from the luminaire properties, each kind of lighting system has a different coefficient of utilization for each space type.

Table <a href="#tab:int_light_space_types" data-reference-type="ref" data-reference="tab:int_light_space_types">[tab:int_light_space_types]</a> in Appendix <a href="#appendix:a" data-reference-type="ref" data-reference="appendix:a">[appendix:a]</a> details the target horizontal illuminance value, the fraction of the target illuminance met by the kind of lighting system, and the lighting system coefficient of utilization for each lighting space type. Lighting space types are defined in 90.1 and are determined based on a mapping of openstudio-standards space types to prototype lighting space types.

Fourth, the LSM assumes a high fraction of non-general lighting systems for certain space types. For example, half of the illuminance in retail sales spaces is from supplemental and wall wash lighting systems. In older lighting generations, there is a significant difference in source efficacy between general and non-general lighting systems. In lighting generation 2, general lighting assumes T8 linear fluorescent lamps at 94 lumens per watt, and supplemental and wall wash lighting assume halogens at 15 lumens per watt. For retail spaces using the LSM values, that means half the lighting comes from lighting technologies roughly 6 times less efficient than the general lighting technology. Although this may be appropriate for setting a code lighting allowance, most retail spaces meet a much greater percentage of their illuminance from more efficient general lighting technologies. ComStock adjusts the lighting system fractions for commonly used space types so that around 80%–90% of lighting comes from the general lighting system. These changes are reflected in Table <a href="#tab:int_light_space_types" data-reference-type="ref" data-reference="tab:int_light_space_types">[tab:int_light_space_types]</a> in Appendix <a href="#appendix:a" data-reference-type="ref" data-reference="appendix:a">[appendix:a]</a>.

Lastly, the LSM offers a generous allowance for lighting power density to account for the lighting loss factor over time. Including lighting losses and depreciation can result in a lighting power density  40% higher than when these terms are ignored. This resulted in unreasonably high installed lighting power densities; thus, ComStock assumes that most existing lighting systems were not designed to account for depreciation over time, and therefore excludes lighting loss and depreciation terms from the lighting power calculation.

With these changes, the LPD calculation simplifies to:
``` math
\begin{align}
\label{comstock_lpd_eqn}
LPD = \frac{\% LS_{1} \cdot fc}{\text{efficacy} \cdot CU_{1}} + \frac{\% LS_{2} \cdot fc}{\text{efficacy} \cdot CU_{2}} + \frac{\% LS_{3} \cdot fc}{\text{efficacy} \cdot CU_{3}} + \frac{\% LS_{4} \cdot fc}{\text{efficacy} \cdot CU_{4}}
\end{align}
```

where:\

- **%LS<sub>i</sub>** is the percent of the target horizontal illuminance value met by a specific lighting system\

- **fc** is the target horizontal illuminance value in lumens per ft<sup>2</sup>\

- **Efficacy** is the source luminous efficacy of the lighting technology in lumens per watt\

- **CU** is the coefficient of utilization, a term that captures how much lighting from the luminaire reaches the horizontal plane.\

The resulting LPDs are shown in Figure <a href="#fig:interior_lighting_lpd" data-reference-type="ref" data-reference="fig:interior_lighting_lpd">1</a>.

<div id="tab:int_light_gens">

| **Lighting Generation** | **General Lighting Technology** | **General Lighting (High Bay) Technology** | **Task Lighting Technology** | **Supplemental Lighting Technology** | **Wall Wash Lighting Technology** |
|:---|:---|:---|:---|:---|:---|
|  |  |  |  |  |  |
| Gen 1 | T12 Linear Fluorescent | HID Mercury Vapor | Incandescent A-Shape | Incandescent Decorative | Incandescent Decorative |
| Gen 2 | T8 Linear Fluorescent | HID Metal Halide | Halogen A-Shape | Halogen Decorative | Halogen Decorative |
| Gen 3 | T5 Linear Fluorescent | HID Metal Halide | Compact Fluorescent Screw | Compact Fluorescent Pin | Compact Fluorescent Pin |
| Gen 4-8 | LED Linear | LED High Bay Luminaire | LED General Purpose | LED Decorative | LED Directional |

Interior Lighting Generations and Technologies

</div>

<figure id="fig:interior_lighting_lpd">
<img src="figures/interior_lighting_lpd.png" style="width:100.0%" />
<figcaption>Average interior lighting power density by building type and lighting generation.</figcaption>
</figure>

### Distribution of Lighting Technologies

Lighting generations were assigned to each building model during sampling based on the year of, and energy code in force during, the last interior lighting replacement. Probability distributions were generated first by using an approximate start and end year for when each technology generation was being installed in commercial buildings (Table <a href="#tab:ltg_gen_year" data-reference-type="ref" data-reference="tab:ltg_gen_year">[tab:ltg_gen_year]</a>). A Gaussian distribution was generated for each lighting generation using these start and end years, and the resulting distribution for each year of last interior lighting replacement was normalized to create 0-1 probabilities. The probability distributions were duplicated for each energy code in force and were further modified to ensure they were realistic (i.e., generation 1 was not installed in a ComStock 90.1-2013 building). This was done using a cutoff generation for each energy code in force (Table <a href="#tab:ltg_cutoff_gen" data-reference-type="ref" data-reference="tab:ltg_cutoff_gen">2</a>). Each of the lighting generations were also assigned an arbitrary weight to scale the distributions. This was done to represent realistic installation trends. For example, although the installation years of generation 2 (T8s) and generation 3 (T5s) overlapped, generation 2 (T8s) was more popular. T5s were not that much more efficient than T8s compared to the difference between T8s and T12s, and T5s cost more. Furthermore, T5s have different bi-pin geometry compared to T8s and T12s, meaning replacing T8s or T12s with T5s requires changing fixtures in addition to lamp costs. For those reasons, generation 2 (T8s) are a greater portion of the stock than generation 3 (T5s).

<div id="tab:ltg_cutoff_gen">

| **Energy Code in Force**   | **Cutoff Generation** |
|:---------------------------|:----------------------|
| ComStock DOE Ref Pre-1980  | gen1_t12_incandescent |
| ComStock DOE Ref 1980-2004 | gen1_t12_incandescent |
| ComStock 90.1-2004         | gen1_t12_incandescent |
| ComStock 90.1-2007         | gen2_t8_halogen       |
| ComStock 90.1-2010         | gen2_t8_halogen       |
| ComStock 90.1-2013         | gen2_t8_halogen       |
| ComStock 90.1-2016         | gen3_t5_cfl           |
| ComStock 90.1-2019         | gen4_led              |
| ComStock DEER Pre-1975     | gen1_t12_incandescent |
| ComStock DEER 1985         | gen1_t12_incandescent |
| ComStock DEER 1996         | gen1_t12_incandescent |
| ComStock DEER 2003         | gen1_t12_incandescent |
| ComStock DEER 2007         | gen2_t8_halogen       |
| ComStock DEER 2011         | gen2_t8_halogen       |
| ComStock DEER 2014         | gen3_t5_cfl           |
| ComStock DEER 2015         | gen3_t5_cfl           |
| ComStock DEER 2017         | gen4_led              |
| ComStock DEER 2020         | gen4_led              |

Interior Lighting Generation Cutoff by Energy Code

</div>

Finally, an additional level of diversity was added to the process. Small commercial buildings (\<50,000 ft$`^2`$) tend to retrofit their lighting technology less frequently than large commercial buildings (\>50,000 ft$`^2`$) (Cadmus Group 2019). To capture this, we changed the interior lighting lifespan values so that large buildings updated their lighting every seven years on average and small buildings updated their lighting every 13 years. These time spans average to 10 years, which matches the median EUL interior lighting used previously.

The distributions were validated against data from the 2015 Lighting Market Characterization Study (Buccitelli et al. 2017) and the 2019 Solid State Lighting Report (Yamada et al. 2019). ComStock sampling results from 2017 and 2020 simulation years were compared against the data from these two studies from the same years, which is referred to as “truth” data in this document. The comparison results for 2017 and 2020 simulation years, as well as the data from the two reports for 2015, 2025, 2030, and 2035, are shown in Figure <a href="#fig:ltg_compare_dist" data-reference-type="ref" data-reference="fig:ltg_compare_dist">2</a>.

<figure id="fig:ltg_compare_dist" data-latex-placement="b!">
<img src="figures/ltg_truth_vs_sampling.png" style="width:80.0%" />
<figcaption>“Truth” lighting generation distribution data from <span class="citation" data-cites="doe2015lmc">(Buccitelli et al. 2017)</span> and <span class="citation" data-cites="doe2019ssl">(Yamada et al. 2019)</span>, and comparison of 2017 and 2020 ComStock sampling results.</figcaption>
</figure>

Simulation years 2017 and 2020 were the focus of validation because they represent the range of simulation years typically run for ComStock. Additionally, for a given iteration of the lighting generation distributions, the comparison results were inconsistent across simulation years. For example, for a set of lighting generation distributions that showed close comparisons for 2017 and 2020, years 2025-2035 were significantly different compared to the other future projections. With improvements to the script that produces the distributions, close comparisons across all simulation years should be feasible.

Table <a href="#tab:ltg_gen_tsv" data-reference-type="ref" data-reference="tab:ltg_gen_tsv">[tab:ltg_gen_tsv]</a> provides a snapshot of the final probability distributions, which show a gradual shift to higher generations as the year of the last interior lighting replacement increases. For this code year (ComStock 90.1-2013), generation 1 lighting technologies would likely not be installed. This is reflected in the distributions, as the minimum lighting generation installed is at least generation 2. The relative popularity of each generation is also apparent in the distributions: generation 2 has a much higher probability of being installed in any year than generation 3, a less popular technology set.

There are two primary areas for improvement for this process:

- The first is in the initial Gaussian distributions. Although there is good data about when the lighting generations were first installed and when they finally lost popularity, information about when the generations peaked in their install popularity is not available. The current method assumes that the peak is at the midpoint of the start and end year. This is most likely incorrect. If data on the peak year of each generation could be collected, this would improve the distribution generation process.

- The second improvement area is the final weighting process. The weights are currently determined using a guess-and-check method. Further improvements to the distribution script would make this method more robust (e.g., using an optimization algorithm).

Figure <a href="#fig:ltg_size_dist" data-reference-type="ref" data-reference="fig:ltg_size_dist">3</a> shows the breakdown of lighting generation distribution (by count) by building size for 2018, the year the current ComStock data set represents the United States building stock. Small buildings are under 50,000 ft$`^2`$ and are assumed to have slower retrofit frequency than larger buildings (\>50,000 ft$`^2`$). The data trend matches this assumption, as there is a larger percentage of smaller building models that have generation 1 and 2 lighting technologies.

Figure <a href="#fig:ltg_btype_dist" data-reference-type="ref" data-reference="fig:ltg_btype_dist">4</a> provides a breakdown of lighting generation distributions by building type. There is not huge variation among the building types. However, building types that are typically smaller (quick service restaurants, small offices, strip malls) lag behind the other building types in terms of lighting technology. This is consistent with the data in Figure <a href="#fig:ltg_size_dist" data-reference-type="ref" data-reference="fig:ltg_size_dist">3</a>.

<figure id="fig:ltg_size_dist" data-latex-placement="ht!">
<img src="figures/ltg_size_dist.png" style="width:80.0%" />
<figcaption>Fraction of installed lighting generations by building size (count-based distribution).</figcaption>
</figure>

<figure id="fig:ltg_btype_dist" data-latex-placement="ht!">
<img src="figures/ltg_btype_dist.png" style="width:90.0%" />
<figcaption>Fraction of installed lighting generation by building type (count-based distribution).</figcaption>
</figure>

### Default Interior Lighting Schedules

Default interior lighting schedules come from the openstudio-standards DOE prototype building models (Deru et al. 2011). The End-Use Load Profiles project derived new default lighting schedules for restaurant, retail, education, office, and warehouse buildings, detailed in Section 3.3.1 of the EULP report: “Interior Lighting Schedules” (Wilson et al. 2022). A full list of default ComStock schedules is available as a [schedules .json file](https://github.com/NREL/openstudio-standards/blob/master/lib/openstudio-standards/standards/ashrae_90_1/ashrae_90_1_2013/comstock_ashrae_90_1_2013/data/ashrae_90_1.schedules.json) on the openstudio-standards GitHub repository.

Additional changes to default schedules include:

- The peak lighting value in the end-use data derived hourly schedule for office spaces is now 0.85 instead of the original  0.5.

- Quick service restaurants and kitchens use the FoodService_Restaurant BLDG_LIGHT_EndUseData schedule rather than the prototype schedule.

- All large hotel guest room lighting schedules use HotelLarge BLDG_LIGHT_GUESTROOM_SCH_2013.

- All small hotel guest rooms follow the same default lighting schedule, with the midday lighting fraction changed from the prototype schedule value of  0.3 to 0.15. Vacant guest rooms use an always off lighting schedule.

Interior lighting schedules are adjusted to correspond with the building’s operating hours, as described in Section <a href="#sec:hoo" data-reference-type="ref" data-reference="sec:hoo">[sec:hoo]</a>.

### Interior Lighting Schedule Magnitude Variability

Section 3.3.4 in the End-Use Load Profiles project report, “Interior Lighting Schedule Magnitude Variability” (Wilson et al. 2022), details the derivation of base-to-peak values applied to the default lighting schedules.

Figure <a href="#fig:ltg_bpr" data-reference-type="ref" data-reference="fig:ltg_bpr">5</a> shows the distribution of base-to-peak ratios (BPRs) in the stock by building type for weekdays and weekends. Note that this methodology was not applied to hospital, outpatient, small and large hotel, and warehouse building types, due to a lack of data.

<figure id="fig:ltg_bpr">
<img src="figures/ltg_sch_bpr.png" style="width:90.0%" />
<figcaption>Weekday and weekend lighting base-to-peak ratios by building type. Base-to-peak ratio is on the x-axis, and fraction of the stock is on the y-axis.</figcaption>
</figure>

<figure id="fig:interior_lighting_eflh">
<img src="figures/interior_lighting_eflh.png" style="width:100.0%" />
<figcaption>Average interior lighting equivalent full load hours by building type.</figcaption>
</figure>

## Exterior Lighting

Exterior lighting is all outdoor lighting at the building site, including lighting for parking, walkways, doorways, canopies, building facades, signage, and landscaping.

### Parking Area Lighting

Parking area lighting accounts for the majority of exterior lighting in the stock (Buccitelli et al. 2017). Parking lighting is calculated as the parking area times the installed lighting power per unit of parking area. Parking area is based on the estimated number of parking spots per student for schools, per unit for hotels, per bed for hospitals, and per building floor area for all other building types. Parking spots are assumed to be 405 ft$`^2`$. Table <a href="#tab:parking" data-reference-type="ref" data-reference="tab:parking">[tab:parking]</a> details these assumptions.

Lighting power for a given parking area is determined from the 2015 U.S. Lighting Market Characterization report, which assumes an average of 216 Watts (W) per parking lighting system, or 0.0410 W/ft<sup>2</sup> (per equation <a href="#ext_light_eqn" data-reference-type="ref" data-reference="ext_light_eqn">[ext_light_eqn]</a>). Base parking lighting power allowance values for each vintage were reduced by a calculated factor such that the building-count weighted parking lighting power density came out to the 0.0410 W/ft<sup>2</sup> target. Note that this calculation is from 2015, so it overestimates the amount of exterior lighting in the stock, which has been changing over to use LEDs. The values for each vintage are shown in Table <a href="#tab:exterior_lighting_power" data-reference-type="ref" data-reference="tab:exterior_lighting_power">[tab:exterior_lighting_power]</a>.

``` math
\begin{align}
\label{ext_light_eqn}
LPD = \left(\frac{216\,W}{\text{lighting system}}\right) \cdot \left(\frac{1\,\text{lighting system}}{13\,\text{parking spots}}\right) \cdot \left(\frac{1\,\text{parking spot}}{405\,\text{ft}^2}\right) = 0.0410\,W/\text{ft}^2
\end{align}
```

### Other Exterior Lighting

Non-parking exterior lighting is determined by the exterior lighting allowance specified in ASHRAE 90.1 for exterior lighting zone 3 (All Other Areas). Length and area estimates are determined from the values in Table <a href="#tab:entryways" data-reference-type="ref" data-reference="tab:entryways">[tab:entryways]</a>. The building facade area is calculated from the model as the ground floor exterior wall area. The lighting power allowance is matched to the 90.1 code for each vintage. The exterior lighting power allowances are shown in Table <a href="#tab:exterior_lighting_power" data-reference-type="ref" data-reference="tab:exterior_lighting_power">[tab:exterior_lighting_power]</a>. Note that although 90.1 includes exterior lighting, the only forms of exterior lighting included in ComStock are parking areas, building facades, main entry doors, other doors, drive through windows, entry canopies, and emergency canopies. Notably, ComStock does not include lighting for exterior signage.

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
