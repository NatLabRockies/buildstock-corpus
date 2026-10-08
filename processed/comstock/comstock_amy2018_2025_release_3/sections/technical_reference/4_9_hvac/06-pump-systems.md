<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 267e3ea | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: Pump Systems | lines: 325-396 -->
## Pump Systems

Pumps are used to induce flow in building hydronic loops. This includes heating water loops, cooling water loops, condenser water loops, and ground-source heat pump water loops.

### Pump Power

Pump power is a function of the pressure head of the hydronic loop and the pump efficiency. The pressure heads in ComStock hydronic systems are set to reflect the baseline requirements specified in ASHRAE-90.1, noting that each hydronic loop type has its own specifications. The pressure heads used for the various ComStock hydronic loop types are specified in Table <a href="#tab:pumps" data-reference-type="ref" data-reference="tab:pumps">5</a>. Primary-only pump configurations use a single hydronic loop system between the boilers/chillers and the heating/cooling coils for space conditioning. A primary-secondary system uses a primary loop for circulating water between the boilers/chillers, and a secondary loop for supplying the the plant fluid to the heating/cooling coils. Pump motor efficiencies are derived using the same motor efficiency lookup tables used for fans (Table <a href="#tab:fan_motor_efficiencies" data-reference-type="ref" data-reference="tab:fan_motor_efficiencies">[tab:fan_motor_efficiencies]</a>).

### Pump Controls

All pumps in ComStock are set to use intermittent controls, meaning that they can cycle off when there is no load present in the loop. Constant volume pumps are controlled to ride the pump curve, as specified by ASHRAE-90.1, whereas variable speed pumps can adjust their speed to modulate flow as needed. Variable speed pumps all have a minimum flow ratio of 0% in ComStock. This value is likely too low and underestimates pumping energy, as most pump systems can only reduce flow as low as 30%–50% in order to maintain proper operation of chillers, boilers, etc. The assignment methodology for variable speed pumps is specified in Table <a href="#tab:pumps" data-reference-type="ref" data-reference="tab:pumps">5</a>.

<div id="tab:pumps">

<table>
<caption>Pump Configuration and Pressure Rise for Hydronic Loops</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Loop Type</strong></th>
<th style="text-align: left;"><strong>Pump Configuration</strong></th>
<th style="text-align: left;"><strong>Primary Pump Head (ft w.c.)</strong></th>
<th style="text-align: left;"><strong>Secondary Pump Head (ft w.c.)</strong></th>
<th style="text-align: left;"><strong>VFD Pump?</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Hot Water Loop</strong></td>
<td rowspan="2" style="text-align: left;">Primary-only</td>
<td rowspan="2" style="text-align: left;">60</td>
<td rowspan="2" style="text-align: left;">-</td>
<td rowspan="2" style="text-align: left;">Variable speed when building area &gt;120,000 ft<span class="math inline"><sup>2</sup></span></td>
</tr>
<tr>
<td style="text-align: left;"><strong>District Heating Loop</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Water-Cooled Chiller Loop</strong></td>
<td style="text-align: left;">Constant-primary, variable-secondary</td>
<td style="text-align: left;">15</td>
<td style="text-align: left;">45</td>
<td style="text-align: left;">Secondary pump always variable speed</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Air-Cooled Chiller Loop</strong></td>
<td rowspan="2" style="text-align: left;">Primary-only</td>
<td rowspan="2" style="text-align: left;">60</td>
<td rowspan="2" style="text-align: left;">-</td>
<td rowspan="2" style="text-align: left;">Variable speed when cooling capacity &gt;300 tons</td>
</tr>
<tr>
<td style="text-align: left;"><strong>District Cooling Loop</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Condenser Water Loop</strong></td>
<td style="text-align: left;">Primary-only</td>
<td style="text-align: left;">50</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">Always constant speed</td>
</tr>
<tr>
<td style="text-align: left;"><strong>GSHP Condenser Water Loop</strong></td>
<td style="text-align: left;">Primary-only</td>
<td style="text-align: left;">60</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">Always constant speed</td>
</tr>
</tbody>
</table>

</div>

