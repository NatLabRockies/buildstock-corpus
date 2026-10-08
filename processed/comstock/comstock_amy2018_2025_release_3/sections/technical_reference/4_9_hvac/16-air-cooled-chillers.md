<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: b5faf42 | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: Air-Cooled Chillers | lines: 1571-1730 -->
## Air-Cooled Chillers

Air-cooled chillers (ACCs) provide chilled water for building cooling systems and use an air-cooled condenser for heat rejection. Therefore, no condenser water loop is required for ACCs. The following ComStock HVAC types use ACCs: DOAS with fan coil air-cooled chiller with baseboard electric, DOAS with fan coil air-cooled chiller with boiler, DOAS with fan coil air-cooled chiller with district hot water, DOAS with fan coil chiller with baseboard electric, VAV air-cooled chiller with PFP boxes, VAV air-cooled chiller with district hot water reheat, and VAV air-cooled chiller with gas boiler reheat.

### Air-Cooled Chiller Rated Performance

ACCs are assigned full load and part load efficiencies based on the HVAC code template for the model and the capacity. These assignments are summarized in Table “Air-Cooled Chiller Efficiency and Performance Curve Assignment”. These values mirror those found in ASHRAE-90.1 (or those used in the DOE reference buildings for the pre-1980 template).

<div id="tab:acc_efficiencies" data-source="tables/air_cooled_chiller_eff_table.tex">

<table>
<caption>Air-Cooled Chiller Efficiency and Performance Curve Assignment</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Model Template</strong></th>
<th style="text-align: left;"><strong>Minimum Capacity (Tons)</strong></th>
<th style="text-align: left;"><strong>Maximum Capacity (Tons)</strong></th>
<th style="text-align: left;"><strong>Minimum Full Load Efficiency (kW/ton)</strong></th>
<th style="text-align: left;"><strong>Minimum Integrated Part Load Value (kW/ton)</strong></th>
<th style="text-align: left;"><strong>Capacity Function of Temperature (Schedule Name)</strong></th>
<th style="text-align: left;"><strong>EIR Function of Temperature (Schedule Name)</strong></th>
<th style="text-align: left;"><strong>EIR Function of PLR (Schedule Name)</strong></th>
<th style="text-align: left;"><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Pre-1980</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">1.303</td>
<td style="text-align: left;">-</td>
<td rowspan="4" style="text-align: left;">ChlrAir_RecipQRatio_fTchwsToadbSI</td>
<td rowspan="4" style="text-align: left;">ChlrAir_RecipEIRRatio_fTchwsToadbSI</td>
<td rowspan="4" style="text-align: left;">ChlrAir_RecipEIRRatio_fQRatio</td>
<td style="text-align: left;">From 90.1-1989</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> Pre-1980</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">1.332</td>
<td style="text-align: left;">-</td>
<td rowspan="3" style="text-align: left;">From DOE Reference Buildings</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> Pre-1980</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.332</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 1980-2004</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.407</td>
<td style="text-align: left;">1.407</td>
</tr>
<tr>
<td style="text-align: left;">90.1-2004</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.256</td>
<td style="text-align: left;">1.153</td>
<td rowspan="4" style="text-align: left;">AirCooled_Chiller_2010_PathA_CAPFT</td>
<td rowspan="4" style="text-align: left;">AirCooled_Chiller_2010_PathA_EIRFT</td>
<td rowspan="4" style="text-align: left;">AirCooled_Chiller_AllCapacities_2004_2010_EIRFPLR</td>
<td rowspan="4" style="text-align: left;">From 90.1-2004 Table 6.8.1A</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2007</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.29</td>
<td style="text-align: left;">1.164</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2010</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">1.255</td>
<td style="text-align: left;">0.941</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2010</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.255</td>
<td style="text-align: left;">0.941</td>
</tr>
<tr>
<td style="text-align: left;">90.1-2013</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">1.25</td>
<td style="text-align: left;">0.96</td>
<td rowspan="8" style="text-align: left;">ChlrAir_ScrollQRatio_fTchwsToadbSI</td>
<td rowspan="8" style="text-align: left;">ChlrAir_ScrollEIRRatio_fTchwsToadbSI</td>
<td rowspan="8" style="text-align: left;">ChlrAir_ScrollEIRRatio_fQRatio</td>
<td rowspan="8" style="text-align: left;">Path A Efficiencies</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2013</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.25</td>
<td style="text-align: left;">0.94</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2013</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">1.188</td>
<td style="text-align: left;">0.876</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2013</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.188</td>
<td style="text-align: left;">0.857</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2016</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">1.188</td>
<td style="text-align: left;">0.876</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2016</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.188</td>
<td style="text-align: left;">0.857</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2019</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">1.188</td>
<td style="text-align: left;">0.876</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> 90.1-2019</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">1.188</td>
<td style="text-align: left;">0.857</td>
</tr>
</tbody>
</table>

</div>

### Air-Cooled Chiller Performance Modifiers

ACCs vary in capacity and efficiency under different operating conditions. ComStock uses three curve types to model the variation in performance: capacity as a function of temperature (CAPFT) modifier, EIR as a function of temperature (EIRFT) modifier, and EIR as a function of part load ratio (EIRFPLR) modifier. For each time step, the EIR modifier function outputs are multiplied by the ACC’s rated EIR (except for the PLR curve output, which is divided). This provides the realized EIR for the time step. Similarly, the CAPFT modifier function output is multiplied by the ACC’s nominal capacity every time step to get the actual available capacity for that time step. The curve assignments are summarized in Table “Air-Cooled Chiller Efficiency and Performance Curve Assignment”, and the curve parameters are specified in Table “Air-Cooled Chiller Performance Curves”. The curves are also illustrated in Figure “Air-cooled chiller EIR as a function of part load ratio performance curves. Independent variables beyond the curve limits will use the bound of the curve limit during simulation.”, Figure “``AirCooledChiller2010PathA'' modifier performance curves; capacity as a function of temperature and EIR as a function of temperature. Independent variables beyond the curve limits will use the bound of the curve limit during simulation.”, and Figure “``ChlrAirRecip'' modifier performance curves; capacity as a function of temperature and EIR as a function of temperature. Independent variables beyond the curve limits will use the bound of the curve limit during simulation.”.

