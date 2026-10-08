<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: b5faf42 | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: Boilers | lines: 843-1104 -->
## Boilers

Boilers create hot water for heating in buildings. The following ComStock HVAC types use boilers for heating: baseboard gas boiler, DOAS with fan coil air-cooled chiller with boiler, DOAS with fan coil chiller with boiler, DOAS with fan coil district chilled water with boiler, DOAS with water source heat pumps cooling tower with boiler, direct evaporative coolers with baseboard gas boiler, PSZ-AC with gas boiler, PTAC with gas boiler, PVAV with gas boiler reheat, VAV air-cooled chiller with gas boiler reheat, VAV chiller with gas boiler reheat, and VAV district chilled water with gas boiler reheat.

### Boiler Efficiencies

At this time, boiler systems in ComStock are all gas-fired (or other combustible fuels) storage tank non-condensing units. A single boiler is used to meet the hot water load for the entire building. Rated efficiency assignments are a function of the HVAC code year and boiler capacity, mirroring the requirements of ASHRAE-90.1, and are summarized in Table “Boiler Efficiency and Performance Curve Assignment”.

### Boiler Part Load Efficiencies

Boiler efficiency at different part load conditions is modeled through an assigned efficiency as a function of a part load ratio (PLR) cubic curve. The output of this curve is multiplied by the full load rated efficiency, providing the effective efficiency of the boiler for each time step. The performance curve assignments for different boiler scenarios are summarized in Table “Boiler Efficiency and Performance Curve Assignment”. The curve features are shown in Table “Boiler Performance Curves”, and the curves are illustrated in Figure “Boiler part load performance curves.”.

Table “Boiler Efficiency and Performance Curve Assignment” shows the older DOE reference building templates using a constant efficiency curve for the boiler (“Boiler Constant Efficiency Curve”). Therefore, these boilers do not currently have efficiency modifications at different part load conditions. This likely underestimates cycling losses that boilers experience at lower PLRs, and may underestimate their gas usage. The 90.1 templates for 2004 through 2010 exclusively use a performance curve for boilers with no turndown controls (“Boiler With No Minimum Turndown”). This provides some efficiency loss, as PLR is reduced. For 90.1-2013 and beyond, performance curves for boilers with minimum turndowns (“Boiler With Minimum Turndown”) are added for larger boiler systems. This provides a slight performance improvement compared to boilers with no minimum turndown. All three curves are illustrated in Figure “Boiler part load performance curves.”.

### Boiler Controls

ComStock boilers use 180°F hot water loops with flow that leaves the set point modulated, meaning the boiler model internally varies the flow rate so that the temperature leaving the boiler matches a set point. The delta T of the loop is 20°F.

<div id="tab:boiler_eff_table" data-source="tables/boiler_efficiency_table.tex">

<table>
<caption>Boiler Efficiency and Performance Curve Assignment</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Template</strong></th>
<th style="text-align: left;"><strong>Minimum Capacity (Btu/hr)</strong></th>
<th style="text-align: left;"><strong>Maximum Capacity (Btu/hr)</strong></th>
<th style="text-align: left;"><strong>Minimum Annual Fuel Utilization Efficiency (AFUE)</strong></th>
<th style="text-align: left;"><strong>Minimum Thermal Efficiency (%)</strong></th>
<th style="text-align: left;"><strong>Minimum Combustion Efficiency (%)</strong></th>
<th style="text-align: left;"><strong>Efficiency Function of Part Load Ratio (EFFFPLR)</strong></th>
<th style="text-align: left;"><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Pre-1980</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.73</td>
<td style="text-align: left;"></td>
<td rowspan="5" style="text-align: left;">Boiler Constant Efficiency Curve</td>
<td rowspan="3" style="text-align: left;">From DOE Reference Buildings</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> Pre-1980</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.74</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> Pre-1980</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.76</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 1980-2004</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">From 90.1-1989</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 1980-2004</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
</tr>
<tr>
<td style="text-align: left;">90.1-2004</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td rowspan="11" style="text-align: left;">Boiler with No Minimum Turndown</td>
<td rowspan="3" style="text-align: left;">From 90.1-2004</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2004</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.75</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2004</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2007</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td rowspan="3" style="text-align: left;">From 90.1-2007</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2007</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2007</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.82</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2010</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td rowspan="3" style="text-align: left;">From 90.1-2010</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2010</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2010</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.82</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2013</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">0.82</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td rowspan="8" style="text-align: left;">From 90.1-2013</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2013</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-7</span> 90.1-2013</td>
<td style="text-align: left;">1,000,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Boiler with Minimum Turndown</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2013</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.82</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-7</span> 90.1-2016</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">0.82</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Boiler with No Minimum Turndown</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2016</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-7</span> 90.1-2016</td>
<td style="text-align: left;">1,000,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Boiler with Minimum Turndown</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2016</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.82</td>
</tr>
<tr>
<td style="text-align: left;">90.1-2019</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">0.84</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Boiler with No Minimum Turndown</td>
<td rowspan="4" style="text-align: left;">From 90.1-2019</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2019</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><span>1-7</span> 90.1-2019</td>
<td style="text-align: left;">1,000,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;"></td>
<td rowspan="2" style="text-align: left;">Boiler with Minimum Turndown</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2019</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.82</td>
</tr>
</tbody>
</table>

</div>

