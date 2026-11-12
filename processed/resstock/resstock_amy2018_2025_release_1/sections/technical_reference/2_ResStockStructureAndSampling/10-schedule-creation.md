<!-- resstock resstock_amy2018_2025_release_1 | technical_reference | docs/technical_reference_guide/2_ResStockStructureAndSampling.tex | status: site_page | source_url: https://github.com/NatLabRockies/resstock/blob/3888e2ff0a4764eb57de65ad0d103870330eb542/docs/technical_reference_guide/2_ResStockStructureAndSampling.tex | publication_url: https://natlabrockies.github.io/ResStock.github.io/assets/trd/ResStockTechnicalReferenceGuide_2025_1.pdf | corpus_version: resstock_amy2018_2025_release_1-v1 | corpus_path: technical_reference/docs/technical_reference_guide/2_ResStockStructureAndSampling.md | section: Schedule Creation | lines: 267-386 -->
## Schedule Creation

In addition to the housing characteristic input files, occupant and energy use schedules are another major necessary building energy model input. Most ResStock schedules are also based upon survey data, but we use a different approach for generating these schedule files since they need to be temporally comprehensive (typically covering a full year with 15-minute time steps) as well as sufficiently diverse to appropriately represent the range of load shapes that occur within the housing stock as well as the aggregate total.

<div id="tab:schedules" data-source="2_ResStockStructureAndSampling.tex">

| Schedule Name | Unit | Description | Stochastic? |
|:---|:---|:---|:---|
| `ceiling_fan` | frac | Ceiling fan energy use schedule | Stochastic |
| `clothes_dryer` | frac | Clothes dryer energy use schedule | Stochastic |
| `clothes_washer` | frac | Clothes washer energy use schedule | Stochastic |
| `cooking_range` | frac | Cooking range & oven energy use schedule | Stochastic |
| `cooling_setpoint` | ° F | Thermostat cooling setpoint schedule | Non-Stochastic |
| `dishwasher` | frac | Dishwasher energy use schedule | Stochastic |
| `electric_vehicle_charging` | frac | Availability schedule for electric vehicle charging. | Stochastic |
| `electric_vehicle_discharging` | frac | Availability schedule for electric vehicle discharging. | Stochastic |
| `extra_refrigerator` | frac | Non-primary refrigerator energy use schedule | Non-Stochastic |
| `freezer` | frac | Freezer energy use schedule | Non-Stochastic |
| `fuel_loads_grill` | frac | Grill fuel load energy use schedule | Non-Stochastic |
| `fuel_loads_lighting` | frac | Lighting fuel load energy use schedule | Non-Stochastic |
| `fuel_loads_fireplace` | frac | Fireplace fuel load energy use schedule | Non-Stochastic |
| `heating_setpoint` | ° F | Thermostat heating setpoint schedule | Non-Stochastic |
| `hot_tub_pump` | frac | Hot tub pump energy use schedule | Non-Stochastic |
| `hot_tub_heater` | frac | Hot tub heater energy use schedule | Non-Stochastic |
| `hot_water_clothes_washer` | frac | Clothes washer hot water use schedule | Stochastic |
| `hot_water_dishwasher` | frac | Dishwasher hot water use schedule | Stochastic |
| `hot_water_fixtures` | frac | Fixtures (sinks, showers, baths) hot water use schedule | Stochastic |
| `lighting_interior` | frac | Interior lighting energy use schedule | Stochastic |
| `lighting_exterior` | frac | Exterior lighting energy use schedule | Non-Stochastic |
| `lighting_garage` | frac | Garage lighting energy use schedule | Stochastic |
| `occupants` | frac | Occupant heat gain schedule | Stochastic |
| `plug_loads_other` | frac | Other plug load energy use schedule | Stochastic |
| `plug_loads_tv` | frac | Television plug load energy use schedule | Stochastic |
| `plug_loads_well_pump` | frac | Well pump plug load energy use schedule | Non-Stochastic |
| `pool_heater` | frac | Pool heater energy use schedule | Non-Stochastic |
| `pool_pump` | frac | Pool pump energy use schedule | Non-Stochastic |
| `refrigerator` | frac | Primary refrigerator energy use schedule | Non-Stochastic |
| `water_heater_setpoint` | ° F | Water heater setpoint schedule | Non-Stochastic |
| `water_heater_operating_mode` | 0/1 | Heat pump water heater operating mode schedule. 0=hybrid/auto, 1=heat pump only. | Non-Stochastic |
| `vacancy` | 0/1 | Vacancy schedule. 0=occupied, 1=vacant. Automatically overrides other columns. | Non-Stochastic |

Modeled schedules in ResStock

</div>

In ResStock, schedules are used to define a variety of building system operations (Table “Modeled schedules in ResStock”). For example, the space heating and cooling system maintains the indoor air temperature according to a detailed schedule of heating and cooling setpoint temperatures. Interior lighting turns on according to occupancy, while exterior lighting is set to turn on at a specific time frame between the evening and the early morning. These schedules represent either preset equipment schedules, typical usage patterns, or the stochastic time use behaviors of all occupants living within a household. Occupant-driven schedules are typically heterogeneous to represent a diversity of behaviors and preferences. Many of the schedules capture not only the timing of use but also the intensity of use as fractional values, with diversity for every day of the year. These fractional value timeseries are then multiplied by the annual end-use energy or hot water use (calculated separately according to building simulation standards such as ANSI/RESNET/ICC 301 standard or those developed by (Hendron and Engebrecht 2010) and (Wilson et al. 2014)) to generate the respective end-use load profiles or hot water draw profiles. The schedules are modified for vacant units and vacancy periods (i.e., an occupied household goes on vacation). When a unit is unoccupied for either reason, all schedules are set to zero except for HVAC setpoint temperature schedules designed to keep pipes from freezing. See Section “Vacant Units” for more information. In ResStock, schedules are generated either using a stochastic occupancy generator (inherited from OS-HPXML) or through more simplistic defined schedules.

**Stochastic Schedules**. ResStock uses a stochastic schedule generator to produce representative and heterogeneous schedules for occupancy and a number of appliances and hot water end uses. Developed using the [American Time Use Survey (ATUS) data from 2013-2017](https://www.bls.gov/tus/), submetered appliance energy data, and a supplemental hot water model, the generator combines Markov chain and probability-sampling for schedule simulation. At a high level, the generator uses Markov chain models built from the ATUS data to produce occupant activity schedules for seven different activities: sleeping, personal hygiene, laundry, cooking, dish washing, absent, and active-at-home. These schedules are then processed and combined with appliance information to form household-level appliance and hot water schedules. For example, both clothes washer and clothes dryer events are scheduled to occur during laundry activity, whereas sink events are scheduled to occur during active-at-home activity. More details of the stochastic occupant model can be found in Chen et al. (2022).

One of the housing characteristics in ResStock is the number of occupants (see Section “Occupants” documentation). The generator starts by randomly assigning each occupant within a ResStock model to one of the four preset occupant types that roughly correspond to day-away-evening-home, day-away-evening-away, mostly-home-early-risers, mostly-home-late-risers. These preset occupant types were created by clustering the ATUS data and picking the number of clusters that provides a good balance between clustering performance and diversity of behavior. There is one Markov chain model for each occupant type and for weekday and weekend separately. Each Markov chain model is built from a cluster of respondents sharing a similar occupancy pattern and models their activity progression throughout the day using a time-inhomogeneous activity transition probability. This means what activity happens next depends on both the current activity and the time of day.

Once the appropriate Markov chain model is picked for an occupant, the schedule generation proceeds with sampling of the starting activity at midnight at the beginning of the weather year and sampling of activity at each time step based on the transition probability given the activity of the previous time step using the Markov-chain transition probability matrix. This process repeats until the full-year schedule is generated for each occupant in the household. Next, the occupant schedules are split into end uses and then merged as a household. The occupant schedules are combined for activities with shareable appliances (e.g., two or more occupants cooking at the same time is one cooking event) and aggregated for individualized activities (e.g., personal hygiene for each occupant is added together for hot water fixtures). While each occupant can only engage in one activity at a time, the activities can overlap after aggregating to the household level.

Next, the generator converts the household activity schedules into appliance power and hot water schedules. For laundry machines, dishwashers, and range ovens, the generator uses the activity schedules for onset only and samples separately for the duration and power consumption of the appliance, which comes from the 2011 Residential Building Stock Assessment Metering Study (RBSAM) by NEEA. For laundry, the dryer is modeled to start immediately after the washer. For appliance hot water, the activity schedules similarly provide the draw onset while the duration and flow rate are sampled using NREL’s Domestic Hot Water Event Schedule Generator (Hendron et al. 2010). In this way, the hot water schedule and power schedule for the clothes washer and dishwasher are only aligned in terms of the onset and not necessarily the duration. This is consistent with real hot water appliance cycles in which hot water is drawn typically at the beginning. Once an appliance cycle completes with a minimum time gap, the generator finds the next activity onset from the activity schedules and the process repeats until all appliance schedules are created.

For hot water fixtures, sink use is based on the at-home inactive portion of the occupancy schedule while the personal hygiene schedule is split between shower and bath. For lighting, plug loads, and ceiling fans, circuit-level reference schedules are used and they are modulated by the occupancy schedule. This means the modulated schedule is the same as the reference schedule at 100% occupancy and ramps down to the minimum of the reference schedule at 0%. The lighting and plug loads reference schedules are taken from Wilson et al. (2014), and the ceiling fans’ come from RBSAM.

The stochastic schedule generator produces all appliance schedules at 15-minute resolution and hot water schedules at 1-min to account for their shorter usage duration. These schedules are then aggregated to the simulation time step and then normalized so the maximum demand within a year is 1. The normalized schedules are multiplied by the annual energy or water consumption determined separately for their respective appliances to produce the end-use load profiles. A problem with this modeling approach is that the disconnect between energy calculation and schedule generation can result in unrealistic load profiles, which is especially important when looking at power consumption at shorter timescales. An end-use appliance with a large usage multiplier assigned can also be assigned a stochastic schedule with low usage, thus resulting in unusually large power draws in the simulation and vice versa. This problem is less jarring at the stock level as aggregation tends to balance and smooth out these anomalies. This is an area identified for future improvement.

**Non-Stochastic Schedules**. For non-stochastic schedules, ResStock defines various options for 24-hour setback periods (in 1-hour resolution) for HVAC heating and cooling setpoints in options_lookup. For range spot ventilation (see Section “Range Spot Vent Hour”), the schedule is generated on the fly using inputs that specify the start hour and the number of hours in operation.

There are two types of OS-HPXML schedule input: simple schedule input or detailed schedule input. Simple schedule inputs are available as weekday/weekend fractions and monthly multipliers for a variety of building characteristics. Detailed schedule inputs allow schedule values for every hour or time step of the simulation. They can be used to reflect real-world or stochastic occupancy and must consist of a full year of data, even if the simulation is part-year. The schedule inputs do not need to have the same time resolution as the simulation. They can be more or less granular than the simulation time step. When schedules are not specified, the default OS-HPXML schedules are used. Default schedules can be simple or detailed and are typically smooth, averaged, hourly, and homogeneous schedules mostly derived from Building America House Simulation Protocols ((Hendron and Engebrecht 2010), (Wilson et al. 2014)).

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-Chen2022" class="csl-entry">

Chen, Jianli, Rajendra Adhikari, Eric Wilson, et al. 2022. “Stochastic Simulation of Occupant-Driven Energy Use in a Bottom-up Residential Building Stock Model.” *Applied Energy* 325 (1): 119890. https://doi.org/<https://doi.org/10.1016/j.apenergy.2022.119890>.

</div>

<div id="ref-Hendron2010" class="csl-entry">

Hendron, Bob, Jay Burch, and Greg Barker. 2010. *<span class="nocase">Tool for Developing Realistic Hot Water Event Schedules</span>*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy10osti/47685.pdf>.

</div>

<div id="ref-bahsp_2010" class="csl-entry">

Hendron, Robert, and Cheryn Engebrecht. 2010. *Building America House Simulation Protocols*. US DOE: Office of Energy Efficiency; Renewable Energy. <https://www1.eere.energy.gov/buildings/publications/pdfs/building_america/house_simulation.pdf>.

</div>

<div id="ref-Langevin2020" class="csl-entry">

Langevin, J., J. L. Reyna, S. Ebrahimigharehbaghi, et al. 2020. “<span class="nocase">Developing a common approach for classifying building stock energy models</span>.” *Renewable and Sustainable Energy Reviews* 133 (December 2019). <https://doi.org/10.1016/j.rser.2020.110276>.

</div>

<div id="ref-RBSA" class="csl-entry">

Northwest Energy Efficiency Alliance. 2024. *2022 Residential Building Stock Assessment - Methods Report*. <https://neea.org/img/documents/2022-Residential-Building-Stock-Assessment-Methods-Report.pdf>.

</div>

<div id="ref-PUMS" class="csl-entry">

Ruggles, Steven, Sarah Flood, Ronald Goeken, Megan Schouweiler, and Matthew Sobek. 2022. *PUMS USA: Version 12.0 \[Dataset\]*. <https://doi.org/10.18128/D010.V11.0>.

</div>

<div id="ref-AHS" class="csl-entry">

U.S. Census. 2022. *American Housing Survey*. <https://www.census.gov/programs-surveys/ahs.html>.

</div>

<div id="ref-RECS2020" class="csl-entry">

U.S. Energy Information Administration. 2020. *Residential Buildings Energy Consumption Survey (RECS), 2020*. U.S. Energy Information Administration. <https://www.eia.gov/consumption/residential/data/2020/>.

</div>

<div id="ref-Wilson2014" class="csl-entry">

Wilson, E., C. Engebrecht Metzger, S. Horowitz, and R. Hendron. 2014. *2014 Building America House Simulation Protocols*. National Renewable Energy Laboratory. <https://www.nrel.gov/docs/fy14osti/60988.pdf>.

</div>

</div>
