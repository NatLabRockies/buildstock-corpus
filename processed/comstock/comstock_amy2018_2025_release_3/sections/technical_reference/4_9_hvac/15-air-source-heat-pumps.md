<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: b5faf42 | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: Air-Source Heat Pumps | lines: 1117-1570 -->
## Air-Source Heat Pumps

Air-source heat pumps (ASHPs) provide electric heating using a reverse vapor compression cycle. This generally provides a higher COP option for electric heating compared to standard electric resistance electric heating. In most cases, ASHPs use the same air-cooled DX system for both DX heating and DX cooling. ASHPs can be split system, packaged units, or through-the-wall packaged terminal heat pumps (PTHP). The following ComStock HVAC systems types use ASHPs: packaged single zone heat pump (PSZ-HP) and PTHP.

ASHP sizing is often based on the design cooling requirements. Because the DX cooling and heating use the same compressor system, the capacities for each are coupled. ASHPs generally have a minimum operating temperature, below which the DX heating is disabled due to lack of capacity and efficiency. To remedy this, backup heating is often included in colder climates, and for any system where the design heating load is higher than the design cooling load. ComStock ASHP sizing follows this methodology: ASHPs are sized to meet the design cooling load, and backup electric heating is added to the system to meet the design heating load when the available DX heating capacity is unavailable or insufficient. The minimum temperature for compressor operation for ComStock heat pump systems is 17°F PTHP and 10°F for PSZ-HP.

<div id="tab:ashp_eff" data-source="tables/ashp_eff.tex">

<table>
<caption>Air-Source Heat Pump Efficiency and Performance Curve Assignment</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Template</strong></th>
<th style="text-align: left;"><strong>Cooling Type</strong></th>
<th style="text-align: left;"><strong>Subcategory</strong></th>
<th style="text-align: left;"><strong>Minimum Capacity (Btu/hr)</strong></th>
<th style="text-align: left;"><strong>Maximum Capacity (Btu/hr)</strong></th>
<th style="text-align: left;"><strong>HSPF</strong></th>
<th style="text-align: left;"><strong>Min COP</strong></th>
<th style="text-align: left;"><strong>PTHP_COP_Coefficient_1</strong></th>
<th style="text-align: left;"><strong>PTHP_COP_Coefficient_2</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5" style="text-align: left;"><strong>Pre-1980 Through 1980-2004</strong></td>
<td style="text-align: left;">AirCooled, ThroughWall</td>
<td style="text-align: left;">Split System</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">6.8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">6.6</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">65,000</td>
<td style="text-align: left;">134,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">135,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">2.9</td>
<td style="text-align: left;">0.026</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;"><strong>90.1-2004</strong></td>
<td style="text-align: left;">AirCooled, ThroughWall</td>
<td style="text-align: left;">Split System</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">6.8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled, ThroughWall</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">6.6</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">65,000</td>
<td style="text-align: left;">134,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">135,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;">0.026</td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;"><strong>90.1-2007</strong></td>
<td style="text-align: left;">ThroughWall</td>
<td style="text-align: left;">Split System</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">29,999</td>
<td style="text-align: left;">7.1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Split System, Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">7.7</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">ThroughWall</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">29,999</td>
<td style="text-align: left;">7</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">65,000</td>
<td style="text-align: left;">134,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">135,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.1</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;">0.026</td>
</tr>
<tr>
<td rowspan="5" style="text-align: left;"><strong>90.1-2010</strong></td>
<td style="text-align: left;">ThroughWall</td>
<td style="text-align: left;">Split System, Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">29,999</td>
<td style="text-align: left;">7.4</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Split System, Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">7.7</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">65,000</td>
<td style="text-align: left;">134,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">135,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;">0.026</td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;"><strong>90.1-2013</strong></td>
<td style="text-align: left;">ThroughWall</td>
<td style="text-align: left;">Split System, Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">29,999</td>
<td style="text-align: left;">7.4</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Split System</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">8.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">65,000</td>
<td style="text-align: left;">134,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">135,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.7</td>
<td style="text-align: left;">0.052</td>
</tr>
<tr>
<td rowspan="6" style="text-align: left;"><strong>90.1-2016</strong></td>
<td style="text-align: left;">ThroughWall</td>
<td style="text-align: left;">Split System, Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">29,999</td>
<td style="text-align: left;">7.4</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Split System</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">8.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">65,000</td>
<td style="text-align: left;">134,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">135,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.7</td>
<td style="text-align: left;">0.052</td>
</tr>
<tr>
<td rowspan="8" style="text-align: left;"><strong>90.1-2019</strong></td>
<td style="text-align: left;">ThroughWall</td>
<td style="text-align: left;">Split System, Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">29,999</td>
<td style="text-align: left;">7.4</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Split System</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">8.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">64,999</td>
<td style="text-align: left;">8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">65,000</td>
<td style="text-align: left;">134,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">Single Package</td>
<td style="text-align: left;">135,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.2</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">6,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.3</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">6,999</td>
<td style="text-align: left;">14,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">3.7</td>
<td style="text-align: left;">0.052</td>
</tr>
<tr>
<td style="text-align: left;">AirCooled</td>
<td style="text-align: left;">PTHP</td>
<td style="text-align: left;">14,999</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">2.9</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

</div>

### ASHP Rated Performance

ASHPs in ComStock are assigned efficiencies based on ASHRAE-90.1. The assigned efficiencies are based on the template code year, the unit capacity, and the unit type. These assignments are summarized in Table “Air-Source Heat Pump Efficiency and Performance Curve Assignment”.

### ASHP Performance Modifiers

Similar to DX cooling equipment, the performance of ASHP equipment changes based on different operating conditions. The curve assignments are shown in Table “Air-Source Heat Pump Performance Curves”. ComStock ASHP equipment uses five performance modifier curves to model this behavior. Energy input ratio (EIR) as a function of part load ratio (PLR) describes how the equipment efficiency varies at different load fractions, where the nominal EIR is divided by the output of this curve to account for equipment cycling losses (Figure “Air-source heat pump EIR ratio as a function of part load ratio.”). EIR as a function of temperature describes how the equipment efficiency varies based on outdoor air dry bulb temperature (Figure “Air-source heat pump COP ratio as a function of outdoor air dry bulb temperature.”). Figure “Air-source heat pump COP ratio as a function of outdoor air dry bulb temperature.” illustrates the capacity loss of ASHPs at lower outdoor air temperatures. EIR as a function of airflow describes how the equipment efficiency varies as a function of the supply airflow fraction (Figure “Air-source heat pump EIR ratio as a function of airflow fraction.”). Capacity as a function of temperature describes how the equipment available capacity varies as a function of outdoor air dry bulb temperature (Figure “Air-source heat pump capacity as a function of airflow ratio.”). Lastly, capacity as a function of airflow describes how the equipment EIR ratio varies as a function of the supply airflow fraction (Figure “Air-source heat pump capacity as a function of airflow ratio.”). The outputs of the EIR modifiers are multiplied against the nominal EIR at every time step (except for the PLR curve output, which is divided), which provides the effective EIR at each time step. Meanwhile, the outputs of the two capacity modifiers are multiplied against the nominal capacity at every time step, yielding the effective available capacity for the time step. The curves described here are primarily derived from the DOE prototype/reference building models.

