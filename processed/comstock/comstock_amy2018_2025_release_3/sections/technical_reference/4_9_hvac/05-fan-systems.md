<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0a2f61f | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: Fan Systems | lines: 226-324 -->
## Fan Systems

Fans are used in all ComStock HVAC systems except those that rely on radiant heat transfer, such as baseboards. Fans induce pressure in the air stream of HVAC equipment, producing the airflow needed for space conditioning and/or outdoor air ventilation.

### Fan Power

Fan power determines the amount of energy it takes a fan system to provide a certain amount of airflow. The fan power requirements of each HVAC system are a function of the total pressure drop of the air stream that the fan system will need to overcome (e.g., from filters, coils, air ducts) as well as the efficiency of the fan blades and fan motor.

Fan power in ComStock is determined by ASHRAE-90.1 code requirements. ASHRAE-90.1 determines fan power primarily based on the system type. Constant air volume, variable air volume, and unitary zone equipment are all assigned different fan power allowances.

For implementation in ComStock, fan power is determined based on the static pressure of the air delivery system, the efficiencies of the fan/motor system, and the airflow of the system. The static pressure is based on the HVAC system type and the maximum airflow of the system, as shown in Table “Fan Pressure Rise and Efficiency”. The fan motor efficiencies are a function of the motor size and HVAC code year, as shown in Table “Motor Efficiency for Fans and Pumps”.

The addition of energy recovery ventilators (ERVs) in HVAC air loops can add additional static pressure to the air system and therefore result in a higher fan power requirement. ComStock accounts for this additional fan power in the ERV wheel power rather than the fan itself; this allows for improved accuracy during ERV bypass modes (where the airflow bypasses the additional static pressure of the ERV system). See Section “Air-Side Energy Recovery” for more information on ComStock ERV systems.

<div id="tab:fan_power" data-source="tables/fan_power.tex">

<table>
<caption>Fan Pressure Rise and Efficiency</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Fan Type</strong></th>
<th style="text-align: left;"><strong>Max Airflow (cfm)</strong></th>
<th style="text-align: left;"><strong>Pressure Rise (in. H<span class="math inline"><sub>2</sub></span>O)</strong></th>
<th style="text-align: left;"><strong>Fan Power Minimum Flow Fraction</strong></th>
<th style="text-align: left;"><strong>Fan Impeller Efficiency</strong></th>
<th style="text-align: left;"><strong>Motor Efficiency</strong></th>
<th style="text-align: left;"><strong>Total Fan Efficiency</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3" style="text-align: left;"><strong>Constant Volume and DOAS</strong></td>
<td style="text-align: left;">&lt;7,437</td>
<td style="text-align: left;">2.5</td>
<td rowspan="3" style="text-align: left;">1</td>
<td rowspan="6" style="text-align: left;">0.65</td>
<td rowspan="9" style="text-align: left;">See motor efficiency lookup table</td>
<td rowspan="9" style="text-align: left;">(Fan Impeller Eff.) X (Motor Eff.)</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">≥</span>7,537 and &lt;20,000</td>
<td style="text-align: left;">4.46</td>
</tr>
<tr>
<td style="text-align: left;"><span class="math inline">≥</span>20,000</td>
<td style="text-align: left;">4.09</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-4</span></td>
<td style="text-align: left;">&lt;4,648</td>
<td style="text-align: left;">4</td>
<td rowspan="3" style="text-align: left;">0.25</td>
</tr>
<tr>
<td style="text-align: left;"><span>2-3</span></td>
<td style="text-align: left;"><span class="math inline">≥</span>4,648 and &lt;20,000</td>
<td style="text-align: left;">6.32</td>
</tr>
<tr>
<td style="text-align: left;"><span>2-3</span></td>
<td style="text-align: left;"><span class="math inline">≥</span>20,000</td>
<td style="text-align: left;">5.58</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-5</span> <strong>PTAC/PTHP, WSHP, VRF</strong></td>
<td style="text-align: left;">&gt;0</td>
<td style="text-align: left;">1.33</td>
<td style="text-align: left;">1</td>
<td rowspan="3" style="text-align: left;">0.55</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-4</span> <strong>Four Pipe Fan Coil</strong></td>
<td style="text-align: left;">&gt;0</td>
<td style="text-align: left;">1.09</td>
<td style="text-align: left;">1</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-4</span> <strong>Unit Heater</strong></td>
<td style="text-align: left;">&gt;0</td>
<td style="text-align: left;">0.2</td>
<td style="text-align: left;">1</td>
</tr>
</tbody>
</table>

</div>

### Fan Controls

This section describes the operation of fan systems during the hours a building is occupied. Details on the operation of fan systems during unoccupied hours are described in Section “Unoccupied Air Handling Unit Operation”.

#### HVAC Systems Providing Outdoor Air

As required by ASHRAE-90.1, HVAC systems in commercial buildings must constantly provide the minimum design outdoor air flow rates when the building is occupied. HVAC systems in ComStock follow this control requirement. For constant volume systems, the fan system will run continuously at design airflow during occupied hours. For VAV systems, the fan system will run continuously between the minimum and maximum airflow of the system during occupied hours, always ensuring that the total system airflow meets the airflow needs of every zone.

#### HVAC Systems Not Providing Outdoor Air

Systems that do not directly provide outdoor air, such as zone-level unitary systems coupled with a DOAS, do not need to run fans continuously. Therefore, these systems are controlled to cycle the fan system on only when required to maintain zone thermostat set points. Otherwise, the fans are allowed to turn off. This is also the control logic for any residential-style system in ComStock that does not provide outdoor air.

