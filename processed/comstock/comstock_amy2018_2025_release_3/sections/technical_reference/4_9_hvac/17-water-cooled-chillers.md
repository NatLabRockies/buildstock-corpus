<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_9_hvac.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_9_hvac.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 0a2f61f | corpus_path: technical_reference/documentation/reference_doc/4_9_hvac.md | section: Water-Cooled Chillers | lines: 1731-2003 -->
## Water-Cooled Chillers

Water-cooled chillers (WCCs) provide chilled water for building cooling systems and use a water-cooled condenser for heat rejection. Therefore, a condenser water loop is required for WCCs, generally conditioned by a boiler and cooling tower. The following ComStock HVAC types use WCCs: DOAS with fan coil chiller with baseboard electric, DOAS with fan coil chiller with boiler, DOAS with fan coil chiller with district hot water, DOAS with fan coil chiller with baseboard electric, VAV chiller with PFP boxes, VAV chiller with district hot water reheat, and VAV chiller with gas boiler reheat.

### Water-Cooled Chiller Rated Performance

WCCs are assigned full load and part load efficiencies based on the HVAC code template for the model and the capacity. These assignments are summarized in Table “Water-Cooled Chiller Efficiency and Performance Curve Assignment”. These values mirror those found in ASHRAE-90.1 (or those used in the DOE reference buildings for the pre-1980 template).

<div id="tab:wcc_eff" data-source="tables/wcc_eff.tex">

<table>
<caption>Water-Cooled Chiller Efficiency and Performance Curve Assignment</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Model Template</strong></th>
<th style="text-align: left;"><strong>Compressor Type</strong></th>
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
<td rowspan="32" style="text-align: left;">Rotary Screw</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.852</td>
<td style="text-align: left;">-</td>
<td rowspan="9" style="text-align: left;">ChlrWtrPosDispPathAAllQRatiofTchwsTcwsSI</td>
<td rowspan="9" style="text-align: left;">ChlrWtrPosDispPathAAllEIRRatio_fTchwsTcwsSI</td>
<td rowspan="32" style="text-align: left;">ChlrWtrPosDispPathAAllEIRRatio_fQRatio</td>
<td rowspan="3" style="text-align: left;">From DOE Reference Buildings</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Pre-1980</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.782</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> Pre-1980</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.688</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 1980-2004</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.926</td>
<td style="text-align: left;">0.902</td>
<td rowspan="3" style="text-align: left;">From 90.1-1989</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 1980-2004</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.837</td>
<td style="text-align: left;">0.782</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 1980-2004</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.676</td>
<td style="text-align: left;">0.664</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2004</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.79</td>
<td style="text-align: left;">0.676</td>
<td rowspan="3" style="text-align: left;">Path A Efficiencies</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2004</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.718</td>
<td style="text-align: left;">0.628</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2004</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.639</td>
<td style="text-align: left;">0.572</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2007</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">74.99</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.63</td>
<td rowspan="8" style="text-align: left;">WaterCooled_PositiveDisplacement_Chiller_LT150_2010_PathA_CAPFT</td>
<td rowspan="8" style="text-align: left;">WaterCooled_PositiveDisplacement_Chiller_LT150_2010_PathA_EIRFT</td>
<td rowspan="8" style="text-align: left;">Path A Minimum Efficiencies</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2007</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.775</td>
<td style="text-align: left;">0.615</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2007</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.68</td>
<td style="text-align: left;">0.58</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2007</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.62</td>
<td style="text-align: left;">0.54</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2010</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">74.99</td>
<td style="text-align: left;">0.78</td>
<td style="text-align: left;">0.63</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2010</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.775</td>
<td style="text-align: left;">0.615</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2010</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.68</td>
<td style="text-align: left;">0.58</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2010</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.62</td>
<td style="text-align: left;">0.54</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2013</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">74.99</td>
<td style="text-align: left;">0.75</td>
<td style="text-align: left;">0.6</td>
<td rowspan="15" style="text-align: left;">ChlrWtrPosDispPathAAllQRatiofTchwsTcwsSI</td>
<td rowspan="15" style="text-align: left;">ChlrWtrPosDispPathAAllEIRRatiofTchwsTcwsSI</td>
<td rowspan="15" style="text-align: left;">Path A Efficiencies</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2013</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.72</td>
<td style="text-align: left;">0.56</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2013</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.66</td>
<td style="text-align: left;">0.54</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2013</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">599.99</td>
<td style="text-align: left;">0.61</td>
<td style="text-align: left;">0.52</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2013</td>
<td style="text-align: left;">600</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.56</td>
<td style="text-align: left;">0.5</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2016</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">74.99</td>
<td style="text-align: left;">0.75</td>
<td style="text-align: left;">0.6</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2016</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.72</td>
<td style="text-align: left;">0.56</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2016</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.66</td>
<td style="text-align: left;">0.54</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2016</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">599.99</td>
<td style="text-align: left;">0.61</td>
<td style="text-align: left;">0.52</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2016</td>
<td style="text-align: left;">600</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.56</td>
<td style="text-align: left;">0.5</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2019</td>
<td style="text-align: left;">0</td>
<td style="text-align: left;">74.99</td>
<td style="text-align: left;">0.75</td>
<td style="text-align: left;">0.6</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2019</td>
<td style="text-align: left;">75</td>
<td style="text-align: left;">149.99</td>
<td style="text-align: left;">0.72</td>
<td style="text-align: left;">0.56</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2019</td>
<td style="text-align: left;">150</td>
<td style="text-align: left;">299.99</td>
<td style="text-align: left;">0.66</td>
<td style="text-align: left;">0.54</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2019</td>
<td style="text-align: left;">300</td>
<td style="text-align: left;">599.99</td>
<td style="text-align: left;">0.61</td>
<td style="text-align: left;">0.52</td>
</tr>
<tr>
<td style="text-align: left;"><span>1-1</span> 90.1-2019</td>
<td style="text-align: left;">600</td>
<td style="text-align: left;">no max</td>
<td style="text-align: left;">0.56</td>
<td style="text-align: left;">0.5</td>
</tr>
</tbody>
</table>

</div>

### Water-Cooled Chiller Performance Modifiers

WCCs have been shown to vary capacity and efficiency at different operating conditions. ComStock uses three curve types to model the variation in performance: capacity as a function of temperature (CAPFT) modifier, EIR as a function of temperature (EIRFT) modifier, and EIR as a function of part load ratio (EIRFPLR) modifier. For each time step, the EIR modifier function outputs are multiplied by the WCC’s rated EIR (except for the PLR curve output, which is divided). This provides the realized EIR for the time step. Similarly, the CAPFT modifier function output is multiplied by the WCC’s nominal capacity every time step to get the actual available capacity for that time step. The curve assignments are summarized in Table“Water-Cooled Chiller Efficiency and Performance Curve Assignment”, and the coefficients are shown in Table “Water-Cooled Chiller Performance Curves”. Furthermore, the performance curves are illustrated in Figure “Energy input ratio modifier as a function of water-cooled chiller part load ratio.” (EIRFPLR for all chillers), Figure“Performance curves for ``WaterCooled PositiveDisplacement Chiller LT150 2010 Modifiers'' WCC.”, and Figure“``ChlrAirRecip'' modifier performance curves; capacity as a function of temperature and EIR as a function of temperature. Independent variables beyond the curve limits will use the bound of the curve limit during simulation.”.

