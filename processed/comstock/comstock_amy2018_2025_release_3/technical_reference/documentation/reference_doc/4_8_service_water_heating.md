<!-- comstock 2025-3 | technical_reference | documentation/reference_doc/4_8_service_water_heating.tex -->
# Service Water Heating

Service water heating (SWH) includes all water heating usage other than space heating and process requirements. This includes general water heating for uses such as sink faucets and showers, but also building-type-specific uses like commercial dish washing and laundry. This section describes how SWH equipment, fuel type, and usage is incorporated into ComStock models.

## Service Water Heating Fuel Type

It would be logical to assume that the SWH system in a building would use the same fuel as the space heating system. An examination of the CBECS 2012 data (U.S. Energy Information Administration 2012) shows that this is the most common case, but it is not always true. In particular, it appears that building types that have large SWH loads, such as hotels and hospitals, are much more likely to use natural gas for SWH, regardless of what their space heating fuel is, presumably because of fuel cost differences. In contrast, building types with low SWH loads are more likely to use electricity for SWH, presumably because of the ease and cost of running wiring compared to installing natural gas piping.

To represent this variability, we used the CBECS 2012 data to create a distribution of SWH fuels for each combination of space heating fuel and building type. The resulting distribution of floor area served by various SWH fuels is shown in Figure <a href="#fig:swh_fuel_dist" data-reference-type="ref" data-reference="fig:swh_fuel_dist">1</a>. As described in Section <a href="#sec:HVAC_System_Type_Heating_Fuel_Type" data-reference-type="ref" data-reference="sec:HVAC_System_Type_Heating_Fuel_Type">[sec:HVAC_System_Type_Heating_Fuel_Type]</a>, the prevalence of different space heating fuel varies considerably by county. Because the service water heating fuel depends on the space heating fuel, the probabilities at a stock level are heavily skewed toward the more common space heating fuels, as shown in Figure <a href="#fig:swh_fuel_area" data-reference-type="ref" data-reference="fig:swh_fuel_area">2</a>.

<figure id="fig:swh_fuel_dist" data-latex-placement="ht!">
<img src="figures/swh_fuel_dist.png" />
<figcaption>Area-weighted distribution of service water heating fuel by space heating fuel and building type.</figcaption>
</figure>

<figure id="fig:swh_fuel_area" data-latex-placement="ht!">
<img src="figures/swh_fuel_area.png" />
<figcaption>Floor area served by each service water heating fuel by space heating fuel and building type.</figcaption>
</figure>

## Service Water Heating System Type

Service water heaters in ComStock models are all storage tank style, and are either fuel combustion (natural gas, fuel oil, or propane) or electric resistance, as discussed in Section <a href="#sec:SWH_Fuel_Type" data-reference-type="ref" data-reference="sec:SWH_Fuel_Type">1.1</a>. Service water heaters with district heating as the fuel type receive hot water from off-site; therefore, these models do not include an on-site water heater. ComStock does not currently model instantaneous water heaters or heat pump water heaters. A single water heater is used to meet the demands of the entire building, unless a booster water loop is used, in which case a separate water heater system will be modeled for the boost loop. Booster loops are included for buildings with kitchen space types. These booster water heaters increase the temperature for some portion of the water for uses that need higher temperatures such as dishwashing. See Section <a href="#sec:space_type_ratios" data-reference-type="ref" data-reference="sec:space_type_ratios">[sec:space_type_ratios]</a> for details on the space type ratios for each building type. In space types with booster water heaters, 60% of peak flow is assigned to the booster water heater, and the remaining 40% is assigned to the standard water heater.

The design temperature of standard water heaters in ComStock is 140°F with a 3.6°F deadband temperature difference allowance. Booster water heaters for kitchens have a target temperature of 180°F; this assumption comes from the DOE prototype models to account for dishwashing in kitchens. The ambient air temperature for tank heat loss is assumed to be 72°F. No parasitic losses or part load performance modifiers are included at this time.

## Service Water Heating Efficiencies

ComStock water heater efficiencies follow the requirements of ASHRAE-90.1. ComStock currently only models non-condensing units, so water heaters with a combustion fuel source are all roughly 80% efficient, whereas electric resistance water heaters are roughly 100% efficient. The efficiency parameters used to calculate the exact water heater efficiencies are summarized in Table <a href="#tab:water_heater_eff" data-reference-type="ref" data-reference="tab:water_heater_eff">[tab:water_heater_eff]</a> based on SWH template, SWH fuel type, and SWH heater capacity.

## Service Water Heating Usage and Schedules

SWH usage for a given time step is based on a design peak gal/min flow rate multiplied by a usage fraction schedule. For example, if a given model has a design SWH flow rate of 10 gal/min, and the schedule value for the time step is 0.5, the SWH flow rate for the time step will be 5 gal/min. The flow rate values in ComStock come from the DOE prototype/reference building models, and are summarized in Tables <a href="#tab:swh_flow_rates_p1" data-reference-type="ref" data-reference="tab:swh_flow_rates_p1">[tab:swh_flow_rates_p1]</a> through <a href="#tab:swh_flow_rates_p3" data-reference-type="ref" data-reference="tab:swh_flow_rates_p3">[tab:swh_flow_rates_p3]</a>.

In ComStock, the design flow rates are specified at the space type level. Then, these rates are aggregated to form a building-level design flow rate. The exception to this is SWH loads for kitchens, which are grouped into their own separate water heater system. These design flow rates are then multiplied by the usage fraction schedules, which specify the fraction of the design flow rate drawn for each time step. The usage fraction schedules in ComStock are derived from the DOE prototype/reference Buildings, and are summarized for each building type in Figures <a href="#fig:swh_sched_fsr" data-reference-type="ref" data-reference="fig:swh_sched_fsr">[fig:swh_sched_fsr]</a> through  <a href="#fig:swh_sched_strip_mall" data-reference-type="ref" data-reference="fig:swh_sched_strip_mall">[fig:swh_sched_strip_mall]</a>. The default schedule assignments for each space type and vintage are shown in Tables <a href="#tab:swh_flow_rates_p1" data-reference-type="ref" data-reference="tab:swh_flow_rates_p1">[tab:swh_flow_rates_p1]</a> through  <a href="#tab:swh_flow_rates_p3" data-reference-type="ref" data-reference="tab:swh_flow_rates_p3">[tab:swh_flow_rates_p3]</a>. However, these schedules are modified according to the hours of operation of the building, as described in Section <a href="#sec:hoo" data-reference-type="ref" data-reference="sec:hoo">[sec:hoo]</a>.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-eia2012cbecs" class="csl-entry">

U.S. Energy Information Administration. 2012. *2012 Commercial Building Energy Consumption Survey (CBECS)*. Http://www.eia.doe.gov/emeu/cbecs/.

</div>

</div>
