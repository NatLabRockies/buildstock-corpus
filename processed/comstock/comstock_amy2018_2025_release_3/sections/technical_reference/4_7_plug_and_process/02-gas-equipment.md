<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_7_plug_and_process.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_7_plug_and_process.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0396270 | corpus_path: technical_reference/documentation/reference_doc/4_7_plug_and_process.md | section: Gas Equipment | lines: 16-77 -->
## Gas Equipment

Gas equipment refers to any natural gas-powered interior equipment that is not used for space heating or water heating. Similar to electric equipment, there are many different types of gas equipment, so ComStock does not model each technology individually, but rather uses a gas intensity in BTU per hour per square foot. Gas kitchen equipment makes up the majority of the gas equipment modeled in ComStock. Kitchen equipment will be discussed separately in Section 4.6.5. There are only three non-kitchen space types in our models that contain non-zero gas equipment values, and the values used are shown in Table “Gas Equipment Power Density (Btu/hr*ft2)”.

<div id="tab:gas_equip" data-source="tables/gas_equip.tex">

<table>
<caption>Gas Equipment Power Density (Btu/hr*ft<sup>2</sup>)</caption>
<thead>
<tr>
<th colspan="2" style="text-align: center;"></th>
<th colspan="6" style="text-align: center;"><span><strong>Template</strong></span></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Building Type</strong></td>
<td style="text-align: left;"><strong>Space Type</strong></td>
<td style="text-align: right;"><strong>Pre-1980</strong></td>
<td style="text-align: right;"><strong>1980-2004</strong></td>
<td style="text-align: right;"><strong>90.1-2004</strong></td>
<td style="text-align: right;"><strong>90.1-2007</strong></td>
<td style="text-align: right;"><strong>90.1-2010</strong></td>
<td style="text-align: right;"><strong>90.1-2013</strong></td>
</tr>
<tr>
<td style="text-align: left;">LargeHotel</td>
<td style="text-align: left;">Laundry</td>
<td style="text-align: right;">170.0</td>
<td style="text-align: right;">170.0</td>
<td style="text-align: right;">170.0</td>
<td style="text-align: right;">170.0</td>
<td style="text-align: right;">170.0</td>
<td style="text-align: right;">170.0</td>
</tr>
<tr>
<td style="text-align: left;">Outpatient</td>
<td style="text-align: left;">OR</td>
<td style="text-align: right;">23.9</td>
<td style="text-align: right;">23.9</td>
<td style="text-align: right;">23.9</td>
<td style="text-align: right;">23.9</td>
<td style="text-align: right;">23.9</td>
<td style="text-align: right;">23.9</td>
</tr>
<tr>
<td style="text-align: left;">SmallHotel</td>
<td style="text-align: left;">Laundry</td>
<td style="text-align: right;">58.4</td>
<td style="text-align: right;">58.4</td>
<td style="text-align: right;">129.9</td>
<td style="text-align: right;">129.9</td>
<td style="text-align: right;">129.9</td>
<td style="text-align: right;">129.9</td>
</tr>
</tbody>
</table>

</div>

The space types that contain gas equipment are the laundry and operating room space types in hotels and outpatient buildings, respectively. Gas laundry equipment represents gas clothes dryers, which are common in commercial drying applications. In operating rooms, a small amount of gas equipment represents steam sterilizers or autoclaves, which are used for sterilization during surgical procedures.

