<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 43ae2d4 | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: Cooling Towers | lines: 2004-2074 -->
## Cooling Towers

Cooling towers are an HVAC component used to reject heat from a condenser water loop. The following ComStock HVAC system types use cooling towers: DOAS with fan coil chiller with baseboard electric, DOAS with fan coil chiller with boiler, DOAS with fan coil chiller with district hot water, DOAS with water source heat pumps cooling tower with boiler, VAV chiller with PFP boxes, VAV chiller with district hot water reheat, and VAV chiller with gas boiler reheat.

The cooling tower assumptions used in ComStock are primarily code-driven and are summarized in Table <a href="#tab:cooling_towers_table" data-reference-type="ref" data-reference="tab:cooling_towers_table">18</a>.

<div id="tab:cooling_towers_table" data-source="tables/cooling_towers_table.tex">

<table>
<caption>Cooling Tower Efficiency</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Model Template</strong></th>
<th style="text-align: left;"><strong>Equipment Type</strong></th>
<th style="text-align: left;"><strong>Fan Type</strong></th>
<th style="text-align: left;"><strong>Fan Type</strong></th>
<th style="text-align: left;"><strong>Minimum Air Flow Rate Ratio</strong></th>
<th style="text-align: left;"><strong>Design Inlet Wet Bulb Temperature (°F)</strong></th>
<th style="text-align: left;"><strong>Design Entering Water Temperature (°F)</strong></th>
<th style="text-align: left;"><strong>Design Leaving Water Temperature (°F)</strong></th>
<th style="text-align: left;"><strong>Minimum Performance (gpm/hp)</strong></th>
<th style="text-align: left;"><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Pre-1980</td>
<td rowspan="8" style="text-align: left;">Open Cooling Tower</td>
<td rowspan="8" style="text-align: left;">Propeller or Axial</td>
<td rowspan="8" style="text-align: left;">VFD</td>
<td rowspan="8" style="text-align: left;">0.2</td>
<td rowspan="8" style="text-align: left;">76</td>
<td rowspan="8" style="text-align: left;">95</td>
<td rowspan="8" style="text-align: left;">85</td>
<td rowspan="5" style="text-align: left;">38.2</td>
<td style="text-align: left;">From 90.1-2004 Table 6.8.1G</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 1980-2004</td>
<td style="text-align: left;">From 90.1-2004 Table 6.8.1G</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2004</td>
<td style="text-align: left;">From 90.1-2004 Table 6.8.1G</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2007</td>
<td style="text-align: left;">From 90.1-2007 Table 6.8.1G</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2010</td>
<td style="text-align: left;">From 90.1-2010 Table 6.8.1 G</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2013</td>
<td rowspan="3" style="text-align: left;">40.2</td>
<td style="text-align: left;">From 90.1-2013 Table 6.8.1-7</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2016</td>
<td style="text-align: left;">From 90.1-2016 Table 6.8.1-7</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2019</td>
<td style="text-align: left;">From 90.1-2019 Table 6.8.1-7</td>
</tr>
</tbody>
</table>

</div>

