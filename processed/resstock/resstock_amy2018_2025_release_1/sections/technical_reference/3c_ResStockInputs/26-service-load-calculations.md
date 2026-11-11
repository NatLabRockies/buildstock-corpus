<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/3c_ResStockInputs.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/3c_ResStockInputs.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1-pre | corpus_path: technical_reference/docs/technical_reference_guide/3c_ResStockInputs.md | section: Service Load Calculations | lines: 3219-3297 -->
## Service Load Calculations

The service and feeder load calculation refers to a type of load calculation used to size the service entrance wires (between the utility poles and the meter or service disconnect) or the feeder wires (between panels, such as those between a building’s main panel and subpanel in each apartment unit) according to Section 220 of the National Electrical Code (NEC). This calculation also applies to the sizing of panels to ensure electrical safety. The NEC updates every three years, and the adoption of NEC varies by municipality. Instead of capturing every NEC version currently in practice, which is impractical, we implemented the load calculations per the latest NEC release, 2023, which represents the best practice adoptable. For 2023, the service load calculation is different for new constructions and existing buildings undergoing an upgrade. Two methods are available for existing buildings, and both are implemented in ResStock: load-based and metered-based. The calculated loads (W) represent the total occuied load from installed electrical equipment and are converted to total occupied capacity (A) by dividing by 240V, the panel voltage. The occupied capacity is compared with the panel service rating to calculate headroom capacity and assess NEC compliance.

### Load-based Method

The service rating of the panel is generally not the sum of individual branch circuit ratings because not all equipment is expected to be operating at full load simultaneously. Instead, there is some diversity in the loads expected to make up the coincidence peak, even at a worst-case scenario. Following this idea, NEC Section 220.83 provides guidance on estimating this peak from the bottom-up to assess whether a panel has sufficient capacity to serve new loads. Table “Summary of load-based method per 2023 NEC 220.83” below summarizes the load-based method, and the assumptions made in ResStock to perform this calculation.

<div id="tab:panel_load_method" data-source="3c_ResStockInputs.tex">

<table>
<caption>Summary of load-based method per 2023 NEC 220.83</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Load Type</strong></th>
<th style="text-align: left;"><strong>Load Amount</strong></th>
<th style="text-align: left;"><strong>ResStock Assumptions</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">General lighting / receptacle load</td>
<td style="text-align: left;">3 W/sqft</td>
<td style="text-align: left;">Uses conditioned floor area</td>
</tr>
<tr>
<td style="text-align: left;">Kitchen small appliance circuits</td>
<td style="text-align: left;">Min two branches at 1500 W each</td>
<td style="text-align: left;">Two branches per dwelling unit</td>
</tr>
<tr>
<td style="text-align: left;">Laundry circuits</td>
<td style="text-align: left;">Min one branch at 1500 W</td>
<td style="text-align: left;">One branch per dwelling unit</td>
</tr>
<tr>
<td style="text-align: left;">Major electric loads</td>
<td style="text-align: left;"><p>Nameplate rating of:</p>
<ul>
<li><p>HVAC (larger of heating and cooling)</p></li>
<li><p>Water heaters</p></li>
<li><p>Clothes dryers (not already on laundry circuits)</p></li>
<li><p>Cooking ranges/ovens</p></li>
<li><p>All other appliances that are "fastened in place, permanently connected, or located to be on a specific circuit"</p></li>
</ul></td>
<td style="text-align: left;"><p>All other appliances include:</p>
<ul>
<li><p>Hot tub/spa</p></li>
<li><p>Pool heaters and pumps</p></li>
<li><p>Well pumps</p></li>
<li><p>Electric vehicle supply equipment (EVSE)</p></li>
<li><p>Dishwashers</p></li>
<li><p>Spot ventilations</p></li>
<li><p>Selected plug loads: microwaves, garbage disposal, garage doors</p></li>
<li><p>Low-power (120V) appliances: water heaters, cooktops (not yet modeled)</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;">Demand factors and summation</td>
<td style="text-align: left;"><p>Demand factors apply to both existing and new loads, depends on whether new HVAC is being installed:</p>
<ul>
<li><p>(a) If not adding new HVAC, take the first 8 kVA of all loads at 100% and remainder loads at 40%.</p></li>
<li><p>(b) If adding new HVAC, take HVAC load at 100%, first 8 kVA of all other loads at 100%, and remainder loads at 40%.</p></li>
</ul></td>
<td style="text-align: left;">Total occupied capacity in the baseline is calculated using (a)</td>
</tr>
</tbody>
</table>

</div>

Of note, we accounted for selected plug loads in the load-based calculation that we do not explicitly model in terms of energy for which plug loads is a single end use category. We assumed all dwelling units have a microwave, 52% homes have a garage disposal (per AHS 2013), and one garage door opener for homes with an attached garage. Additionally, the demand factors applied to sum up the loads vary depending on whether new HVAC load is being introduced by an upgrade. If all or part of the HVAC load is considered new, a more conservative approach (part (b)) is taken by taking the HVAC load (maximum of either heating or cooling) at 100% instead of lumping it with all other loads to undergo adjustment by demand tiers. For the baseline load calculation, the total occupied load is calculated using part (a) as no new load is introduced yet.

### Meter-based Method

The second method, metered-based, is a top-down approach by using the metered electricity peak of the preceding year to baseline the existing loading of the panel. Per NEC section 220.87, the total capacity needed for an upgrade is calculated as 1.25 of the baseline peak electricity plus any new loads at 100%. In ResStock, the annual electricity peak is used in place of the metered data and the new loads that are counted are the same as those outlined in the load-based method.

For a given upgrade, the load-based method is generally more conservative than the metered-based at estimating the number of homes with a panel capacity constraint. However, this may not be the case for homes that have high equipment utilization factors or setpoints that drive up HVAC use. Additionally, as the metered-based method does not account for the removal of any legacy loads, the method may be more conservative for certain upgrade scenarios. For example, for a home that is upgrading an electric boiler to a heat pump with integrated heat strip, the heating load is being counted twice, from the incumbent equipment as part of the annual electric peak and the new equipment.

