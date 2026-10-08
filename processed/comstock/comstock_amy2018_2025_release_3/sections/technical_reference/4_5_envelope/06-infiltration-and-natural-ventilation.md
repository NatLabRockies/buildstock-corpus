<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_5_envelope.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_5_envelope.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0396270 | corpus_path: technical_reference/documentation/reference_doc/4_5_envelope.md | section: Infiltration and Natural Ventilation | lines: 315-448 -->
## Infiltration and Natural Ventilation

### Infiltration

Infiltration in ComStock uses the same model as EnergyPlus (*EnergyPlus, Version 00* 2017), detailed in equation energyplus_infiltration_eqn.

``` math
\begin{align}
\label{energyplus_infiltration_eqn}
Infiltration = I_{design} * F_{schedule} * [A + B * |(T_{zone} - T_{odb})| + C * WindSpeed + D * WindSpeed^2]
\end{align}
```

where:\

- **I<sub>design</sub>** is the design infiltration flow rate, in m<sup>3</sup> per s per m<sup>2</sup> exterior surface area\

- **F<sub>schedule</sub>** is a fractional schedule, usually tied to HVAC system operation\

- **A** is the coefficient for constant infiltration\

- **B** is the coefficient for temperature difference driven infiltration\

- **T<sub>zone</sub>** is the zone air temperature, in degrees Celsius\

- **T<sub>odb</sub>** is the outdoor dry bulb temperature, in degrees Celsius\

- **C** and **D** are linear and quadratic coefficients for wind driven infiltration\

- **WindSpeed** is the local windspeed, in m per s.\

The selection of the design infiltration rate is somewhat arbitrary, as it depends on the assumed natural pressure at typical conditions. The coefficients need to be paired with an assumed natural pressure.

### Infiltration Rates

Infiltration rates are calculated from measured airtightness data from (Emmerich and Persily 2014). There are significant differences in building airtightness due to differences in wall construction, shown in Figure 6 of the NIST reference. Airtightness does not vary significantly by building type or vintage. Airtightness does depend on size, but this is inherently captured by larger buildings having smaller surface area to volume ratios. Air barriers greatly reduce leakiness, but they are rare in existing buildings, and only recently have been required in some jurisdictions. Airtightness of buildings in ComStock follow lognormal distributions with airtightness means by wall construction type matched to those in (Emmerich and Persily 2014), shown in Figure “6-sided airtightness distributions by wall construction type. Distributions are lognormal, with means matched to means by wall construction type in nist_infiltration_data.”. Airtightness values are measured at 75 Pa and are 6-sided, meaning the infiltration is normalized by total building exterior surface area including wall, roof, and ground surfaces.

The design infiltration rate is calculated from the airtightness value assuming a 4 Pa design pressure, shown in “Infiltration Rates”
``` math
\begin{align}
\label{airtightness_to_design_infiltration}
I_{\text{design}} = \text{airtightness} \cdot \left(\frac{1\ \text{hr}}{3600\ \text{s}}\right) \cdot \left(\frac{5\ \text{sided area}}{6\ \text{sided area}}\right) \cdot \left(\frac{4.0\ \text{Pa}}{75.0\ \text{Pa}}\right)^{0.65}
\end{align}
```
where:\

- **airtightness** is the measured airtightness at 75 Pa in m<sup>3</sup> per hr per m<sup>2</sup> 6-sided exterior surface area\

- **I<sub>design</sub>** is the design infiltration rate at 4 Pa in m<sup>3</sup> per s per m<sup>2</sup> 5-sided exterior surface area\

<figure id="fig:airtightness_by_wall_construction_type">
<img src="figures/airtightness_by_wall_construction_type.png" style="width:90.0%" />
<figcaption>6-sided airtightness distributions by wall construction type. Distributions are lognormal, with means matched to means by wall construction type in <span class="citation" data-cites="nist_infiltration_data">(Emmerich and Persily 2014)</span>.</figcaption>
</figure>

### Infiltration Coefficients

NIST derived coefficients by building CONTAM models of all of the DOE prototype buildings, as explained in (Ng et al. 2021). The coefficients assume a 4 Pa design pressure. The coefficients include A, B, and D terms, with C being 0. Coefficients are by building type, with separate coefficients for whether the HVAC system is on or off. The NIST report includes separate coefficients for buildings with air barriers, but ComStock does not assume buildings have air barriers.

NIST did not model all DOE prototype buildings, and does not include HVAC system off coefficients for some buildings if the prototype was modeled as always on. ComStock building types not available in the NIST data use coefficients for either the Office or Retail building types. If off coefficients are not available, the building uses the on coefficients instead.

### Natural Ventilation

Natural ventilation is not modeled in ComStock because it is not common in the building stock.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-ashrae_901_2010" class="csl-entry">

ASHRAE. 2010. *Standard 90.1-2010 (i-p Edition) Energy Standard for Buildings Except Low-Rise Residential Buildings*. ASHRAE.

</div>

<div id="ref-ashrae_901_2022" class="csl-entry">

ASHRAE. 2022. *Standard 90.1-2022 (i-p Edition) Energy Standard for Buildings Except Low-Rise Residential Buildings*. ASHRAE.

</div>

<div id="ref-tbd_gem" class="csl-entry">

Bourgeois, Denis, and Dan Macumber. 2024. *Thermal Bridging and Derating, Version 3.4.2*. <https://github.com/rd2/tbd>.

</div>

<div id="ref-old_vintage_office_study" class="csl-entry">

Briggs, R S, D B Belzer, and D B Crawley. 1987. *Analysis and Categorization of the Office Building Stock. Topical Report, February-September 1987*. Pacific Northwest Lab. <https://www.osti.gov/biblio/6795134>.

</div>

<div id="ref-cpuc_deer" class="csl-entry">

California Public Utilities Commission. 2021. *Database for Energy Efficient Resources*. <a href="http://deeresources.com/" class="uri">Http://deeresources.com/</a>.

</div>

<div id="ref-doe_reference_buildings" class="csl-entry">

Deru, M, K Field, D Studer, et al. 2011. *U.s. Department of Energy Commercial Reference Building Models of the National Building Stock*. National Renewable Energy Laboratory. <https://doi.org/10.2172/1009264>.

</div>

<div id="ref-nist_infiltration_data" class="csl-entry">

Emmerich, Steven J, and Andrew K Persily. 2014. “Analysis of u.s. Commercial Building Envelope Air Leakage Database to Support Sustainable Building Design.” *International Journal of Ventilation* 12 (4): 331-44. <https://doi.org/10.1080/14733315.2014.11684027>.

</div>

<div id="ref-energy_plus" class="csl-entry">

*EnergyPlus, Version 00*. 2017. <https://www.osti.gov/biblio/1395882>.

</div>

<div id="ref-lightbox_smartparcels_2021" class="csl-entry">

LightBox. 2021. *SmartParcels Database*. LightBox.

</div>

<div id="ref-nist_infiltration_correlations" class="csl-entry">

Ng, Lisa C., W. Stuart Dols, and Steven J. Emmerich. 2021. “Evaluating Potential Benefits of Air Barriers in Commercial Buildings Using NIST Infiltration Correlations in EnergyPlus.” *Building and Environment* 196: 107783. https://doi.org/<https://doi.org/10.1016/j.buildenv.2021.107783>.

</div>

<div id="ref-eia2012cbecs" class="csl-entry">

U.S. Energy Information Administration. 2012. *2012 Commercial Building Energy Consumption Survey (CBECS)*. Http://www.eia.doe.gov/emeu/cbecs/.

</div>

</div>
