<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0a2f61f | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: Air-Side Economizers | lines: 567-666 -->
## Air-Side Economizers

Air-side economizers reduce HVAC cooling energy by increasing the amount of outdoor ventilation air during times when the temperature and/or enthalpy are beneficial for cooling. For example, if the outdoor air temperature is 55°F when the building needs cooling, the HVAC system can increase the amount of outdoor ventilation air being delivered to the space to satisfy some or all of the cooling requirement in place of mechanical cooling.

As described in Section “Building System Turnover and Effective Useful Life”, we assume that some building systems, including the HVAC system, are replaced over the lifespan of the building. We re-evaluate the requirement for an air-side economizer based on the energy code in force at the time of the latest HVAC system replacement. For buildings outside of CA, energy code requirements were taken from ASHRAE 90.1. For buildings inside CA, the CA energy code requirements were evaluated taken from the CA DEER MASControl3 models (Hirsch 2021), where the economizer limits and applicability were found as shown in Table “Economizer limits from MASControl3” and Table “Economizer applicability from MASControl3”.

<div id="tab:econ_lims_mascontrol3" data-source="tables/econ_lims_mascontrol3.tex">

| **Climate Zone** | **Drybulb Limit (°F)** | **Enthalpy Limit (Btu/lb)** |
|:-----------------|:-----------------------|:----------------------------|
| CZ01             | 70                     | 28                          |
| CZ02             | 73                     | 28                          |
| CZ03             | 70                     | 28                          |
| CZ04             | 73                     | 28                          |
| CZ05             | 70                     | 28                          |
| CZ06             | 71                     | 28                          |
| CZ07             | 69                     | 28                          |
| CZ08             | 71                     | 28                          |
| CZ09             | 71                     | 28                          |
| CZ10             | 73                     | 28                          |
| CZ11             | 75                     | 28                          |
| CZ12             | 75                     | 28                          |
| CZ13             | 75                     | 28                          |
| CZ14             | 75                     | 28                          |
| CZ15             | 75                     | 28                          |
| CZ16             | 75                     | 28                          |

Economizer limits from MASControl3

</div>

<div id="tab:econ_applic_mascontrol3" data-source="tables/econ_applic_mascontrol3.tex">

| **Vintage** | **Packaged DX** | **Chilled Water** | **Water Loop HP** |
|:------------|:----------------|:------------------|:------------------|
| 1975        | FALSE           | TRUE              | FALSE             |
| 1985        | FALSE           | TRUE              | FALSE             |
|  1996       | FALSE           | TRUE              | FALSE             |
| 2003        | FALSE           | TRUE              | FALSE             |
| 2007        | FALSE           | TRUE              | FALSE             |
| 2011        | FALSE           | TRUE              | FALSE             |
| 2014        | TRUE            | TRUE              | TRUE              |
| 2015        | TRUE            | TRUE              | TRUE              |
| 2017        | TRUE            | TRUE              | TRUE              |
| 2020        | TRUE            | TRUE              | TRUE              |

Economizer applicability from MASControl3

</div>

Figure “Presence of air-side economizers in the building stock.” shows the prevalence of economizers (in terms of floor area coverage and contribution to cooling energy) for different subcategories (building type and ventilation system type) of the existing building stock. The percentage of floor area where "economizer availability" is "True" includes the total building area if there is at least one economizer in the building. It does not represent the total floor area served by systems with economizers. While there are buildings that already include economizers in variable air volume (VAV) systems and roof top units (RTU) covering 40% of the total floor area and 28% of total electricity used for cooling, the remaining portion of buildings with those system types do not include economizers.

<figure id="fig:economizer_presence">
<img src="figures/economizer_presence.png" style="width:70.0%" />
<figcaption>Presence of air-side economizers in the building stock.</figcaption>
</figure>

Based on a large body of anecdotal evidence from conversations with fault-focused field engineers and a brief review of common current (Trane, Carrier, Daikin) rooftop unit product data sheets (Trane 2023), (Carrier 2023), (Daikin 2023), fixed dry bulb controls are a more common choice than differential dry bulb controls, although manufacturers also offer dual enthalpy (fixed dry bulb + fixed enthalpy) options with the addition of an enthalpy sensor. For this reason, fixed dry bulb controls are assumed for almost all building vintages and climate zones, with the exception being ASHRAE 90.1-2010 and 2013, which prohibited fixed dry bulb economizers in the warmer humid climate zones. These restrictions were lifted in ASHRAE 90.1-2016.

Figure “Economizer floor area coverage comparing ComStock (left) with CBECS 2018 (right).” shows the comparison of economizer coverage with respect to building floor area between ComStock and estimation from Commercial Buildings Energy Consumption Survey (U.S. Energy Information Administration 2018a). Because of how data is structured in CBECS, the floor area shown in these figures represents the entire floor area of the building if any economizer is present in any of the HVAC systems in the building rather than actual floor area covered by HVAC systems with an economizer. Because CBECS data only shows total building area instead of total area covered by the economizers, this comparison helps give a rough estimate of economizers.

<figure id="fig:economizer_prevalence">
<img src="figures/economizer_prevalence.png" style="width:70.0%" />
<figcaption>Economizer floor area coverage comparing ComStock (left) with CBECS 2018 (right).</figcaption>
</figure>

Economizers are well known for frequent faulty operations. There were many efforts in the past to understand fault characteristics in commercial buildings (Kim et al. 2021), (Crowe et al. 2022), (Katipamula et al. 2021), (Frank et al. 2018). While this evidence is insufficient to reflect all aspects (e.g., prevalence, incidence, intensity, and evolution described in (Kim et al. 2021)) of all faults in the commercial building stock across the country, it is possible to make simplifications for modeling certain fault types based on available data.

Figure “Economizer incorrect changeover temperature setting fault description.” shows how the first fault is modeled for buildings with economizers. Crowe et al. (Crowe et al. 2022) acquired data from AFDD venders that monitored 3,660 AHUs and 7,974 RTUs and reported 31% of all economizers were experiencing faulty operations. Shoukas et al. (Shoukas et al. 2020) received data from a clothing retailer and food chain that monitored 1,416 RTUs and reported 60% of all faults related to economizers were related to economizer not effectively reducing cooling load compared to the theoretical potential. The symptom described as "ineffective economizing" can be due to different faults: damper stuck, damper bias, sensor bias, sensor frozen, inappropriate configuration, etc. A report (Seventhwave and Center for Energy and Environment 2016) published by Minnesota Department of Commerce Division of Energy Resources monitored 41 RTUs in Minnesota that were installed in many different building types (e.g., office, restaurant, retail, hotel, etc.) and reported the actual changeover temperature setting in the economizer were not configured efficiently (average of 52°F) resulting in missed free cooling opportunity.

Based on this information focusing on different aspects of the fault, a fault measure was developed as shown in Figure “Economizer incorrect changeover temperature setting fault description.”. The figure includes a description of the fault as well as four different metrics that define the characteristics of a fault. Fault intensity (or severity) is when a fault can have a severity level. For example, if the sensor is drifting, the intensity is the difference between the true value and the biased measured value. Fault prevalence refers to the portion of systems or components with the fault among all systems or components in the sample space (e.g., 30% of all economizers have the fault). Fault incidence refers to the occurrence rate of a fault for a given system or component over for a given time period (e.g., economizer damper gets stuck once every year). Fault evolution refers to certain faults where the severity naturally changes over time. For example, sensor drift is typically a fault where the severity changes over the course of time. For the incorrect high limit setting described in Figure “Economizer incorrect changeover temperature setting fault description.”, the fault changes the changeover temperature setting of an economizer to 52°F and applies to 30% of economizers that use fixed dry-bulb control. Fault incidence and fault evolution were not modeled because these aspects are mostly irrelevant for this fault.

<figure id="fig:econ_temp_fault">
<img src="figures/econ_temp_fault.png" style="width:70.0%" />
<figcaption>Economizer incorrect changeover temperature setting fault description.</figcaption>
</figure>

Figure “Economizer incorrect changeover temperature setting fault impact on simulation results.” shows a comparison of simulated operation with and without the fault. As a result, the fault will reduce the changeover (high limit) temperature of the economizer, disabling the economizer even if the outdoor air temperature is favorable (e.g., 52-72°F), thus, losing opportunities for free cooling. The figure shows how the fault impacts the annual cooling energy, how the changepoint temperature changes with fault, and how the transient response changes.

<figure id="fig:econ_temp_fault_single_model">
<img src="figures/econ_temp_fault_single_model.png" style="width:70.0%" />
<figcaption>Economizer incorrect changeover temperature setting fault impact on simulation results.</figcaption>
</figure>

As reported by Heinemeier (Heinemeier 2014), contractors in California stated that 30-40% of economizers they have worked with were disabled with fully closed dampers. This is often caused by mechanical linkage issues between damper and actuator, where the economizer automatically reverts to the fully closed position as a safety measure. An economizer with a fully closed damper will not draw any fresh outdoor air, causing an air quality issue. Depending on the outdoor air condition (i.e., favorable or not favorable for economizing), it can either reduce or increase energy consumption. Figure “Economizer damper stuck closed fault description.” shows the description of the fault for the economizer outdoor air damper fully closed and stuck. Unlike the fault described in Figure “Economizer incorrect changeover temperature setting fault description.”, this fault has a bigger impact on air quality and energy and the incidence of the fault is important.

<figure id="fig:econ_damper_fault">
<img src="figures/econ_damper_fault.png" style="width:70.0%" />
<figcaption>Economizer damper stuck closed fault description.</figcaption>
</figure>

Figure “Economizer damper stuck closed fault impact on simulation results.” shows example simulation results for a building with and without the damper fully closed fault. The fault was imposed once during the entire April period resulting in 1.8% mechanical load increase. As mentioned previously, the energy impact of the fault can either be increased or decreased energy consumption, and Figure “Economizer damper stuck closed fault impact on simulation results.”(c) highlights the transition from negative to positive savings when the outdoor air temperature transitions from favorable to unfavorable conditions.

<figure id="fig:econ_damper_fault_single_model">
<img src="figures/econ_damper_fault_single_model.png" style="width:70.0%" />
<figcaption>Economizer damper stuck closed fault impact on simulation results.</figcaption>
</figure>

Although faults (e.g., damper fully closed) are implemented with fixed prevalence (e.g., 35%), the actual percentage of economizers being faulted (among applicable economizers) is less than the defined prevalence due to implementation limitations. For example, 35% of randomly selected buildings that include certain HVAC system types (categorized by the air system) are assigned the damper fully closed fault. However, certain portions of these air systems do not have economizers, thus, they cannot have an economizer fault. In other words, the current limitation is that the random selection of faulted economizers is not fully aligned with buildings that actually have economizers. In these cases, we are losing the opportunity for applying faults and decreasing the representation of fault prevalence in final building stock. Newer versions of California’s Title 24 energy code requires fault detection and diagnostics (FDD) for economizers which should prevent and mitigate faults. However, ComStock does not reflect the impact of FDD technology, possibly overestimating the impact of faults in buildings with newer HVAC systems in California.

