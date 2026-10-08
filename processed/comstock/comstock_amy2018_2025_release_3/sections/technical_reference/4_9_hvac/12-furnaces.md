<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0a2f61f | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: Furnaces | lines: 667-842 -->
## Furnaces

Furnaces are used in a variety of HVAC equipment for space heating through the direct combustion of a fuel. For ComStock models, the fuel type can be natural gas, propane, or fuel oil. The following ComStock system types use furnaces: direct evaporative coolers with forced air furnace, gas unit heaters, PSZ-AC with gas coil, PTAC with gas coil, residential AC with residential forced air furnace, and residential forced air furnace.

### Furnace Efficiencies

Furnaces in ComStock are all assumed to be standard, non-condensing types at this time. Rated efficiency assignments are a function of capacity and in-force HVAC template code. The furnace efficiency assignments are summarized in Table “Furnace Efficiency by Capacity and Code Year”.

### Furnace Performance Modifiers

Furnaces in ComStock do not use any performance curves, so there is no change in efficiency or capacity as a function of temperature or part load ratio, and therefore no cycling losses. Furthermore, no parasitic fuel losses are included in ComStock furnace models.

<div id="tab:furnace_eff_assignments" data-source="tables/furnace_eff_table.tex">

<table>
<caption>Furnace Efficiency by Capacity and Code Year</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Template</strong></th>
<th style="text-align: left;"><strong>Minimum Capacity (Btu/hr)</strong></th>
<th style="text-align: left;"><strong>Maximum Capacity (Btu/hr)</strong></th>
<th style="text-align: left;"><strong>Minimum Annual Fuel Utilization Efficiency (AFUE)</strong></th>
<th style="text-align: left;"><strong>Minimum Thermal Efficiency (%)</strong></th>
<th style="text-align: left;"><strong>Minimum Combustion Efficiency (%)</strong></th>
<th style="text-align: left;"><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Pre-1980</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">249,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">Pre-1980</td>
<td style="text-align: left;">250,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">Pre-1980</td>
<td style="text-align: left;">250,000,000</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">1980-2004</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">299,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">1980-2004</td>
<td style="text-align: left;">300,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">90.1-2004</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">224,999</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
<td rowspan="10" style="text-align: left;">Table 6.8.1E page 49</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2004</td>
<td style="text-align: left;">225,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2007</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">224,999</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2007</td>
<td style="text-align: left;">225,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">0.8</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2010</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">224,999</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2010</td>
<td style="text-align: left;">225,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2013</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">224,999</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2013</td>
<td style="text-align: left;">225,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2016</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">224,999</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2016</td>
<td style="text-align: left;">225,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">90.1-2019</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">224,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.81</td>
<td style="text-align: left;">-</td>
<td rowspan="2" style="text-align: left;">Table 6.8.1-6 for &gt;225 kBtu/hr; Table F-4 for &lt;225 kBtu/hr</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-6</span> 90.1-2019</td>
<td style="text-align: left;">225,000</td>
<td style="text-align: left;">249,999,999</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">0.8</td>
<td style="text-align: left;">-</td>
</tr>
</tbody>
</table>

</div>

