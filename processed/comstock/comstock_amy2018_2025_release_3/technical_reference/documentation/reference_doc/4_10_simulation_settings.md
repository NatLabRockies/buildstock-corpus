<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_10_simulation_settings.tex -->
# Simulation Settings

## EnergyPlus Simulation Settings

The EnergyPlus simulation settings are a crucial part of any run because they set the length of the run, the calendar year, the number of time steps, and a number of other inputs. A list of all the simulation settings used in ComStock and their descriptions is shown in Table <a href="#tab:simulation_settings" data-reference-type="ref" data-reference="tab:simulation_settings">1</a>.

<div id="tab:simulation_settings">

<table>
<caption>EnergyPlus Simulation Settings</caption>
<thead>
<tr>
<th style="text-align: left;"><strong>Simulation Setting</strong></th>
<th style="text-align: left;"><strong>Input</strong></th>
<th style="text-align: left;"><strong>Input Explanation</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Number of time steps per hour used by EnergyPlus for heat transfer and load calculations</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;">ComStock uses four time steps per hour for all EnergyPlus simulations, unless otherwise specified. This creates a 15-minute time step.</td>
</tr>
<tr>
<td style="text-align: left;">Enable daylight saving time</td>
<td style="text-align: left;">TRUE</td>
<td style="text-align: left;">EnergyPlus automatically interprets schedules as being in local time, and therefore shifts with daylight saving time. In the individual model output time series data, the timestamp is reported out in local time, Daylight Standard Time, and Coordinated Universal Time (UTC). In ComStock, the time series results for all buildings are all converted to Eastern Standard Time (EST) for publication. For buildings whose local time is not EST, the last few hours of the data set are moved to the beginning of the time series to ensure a full year of data.</td>
</tr>
<tr>
<td style="text-align: left;">Start of daylight saving time</td>
<td style="text-align: left;">Second Sunday in March</td>
<td rowspan="2" style="text-align: left;">Daylight saving time (DST) in the United States starts on the second Sunday in March and ends on the first Sunday in November. The current schedule was introduced in 2007 and follows the Energy Policy Act of 2005.</td>
</tr>
<tr>
<td style="text-align: left;">End of daylight saving time</td>
<td style="text-align: left;">First Sunday in November</td>
</tr>
<tr>
<td style="text-align: left;">Calendar year of simulation</td>
<td style="text-align: left;">Varies</td>
<td style="text-align: left;">The calendar year varies based on the year intended to be simulated. The calendar year should match the year of the weather file being used for simulation.</td>
</tr>
<tr>
<td style="text-align: left;">January 1 day of week</td>
<td style="text-align: left;">Varies</td>
<td style="text-align: left;">The day of the week on January 1 for the calendar year being simulated.</td>
</tr>
<tr>
<td style="text-align: left;">Beginning month of simulation</td>
<td style="text-align: left;">1</td>
<td rowspan="2" style="text-align: left;">These four parameters specify the length of the simulation. The default is a one-year, 8,760-hour simulation, starting on January 1 and ending on December 31. If the calendar year of simulation is a leap year, the end of the simulation period will be input as December 30 instead of December 31 to ensure 8,760 hours of simulation results. In years with February 29, December 31 will not be included in the simulation. These settings can also be adjusted if only a partial year simulation is necessary.</td>
</tr>
<tr>
<td style="text-align: left;">Beginning day of simulation</td>
<td style="text-align: left;">1</td>
</tr>
<tr>
<td style="text-align: left;">End month of simulation</td>
<td style="text-align: left;">12</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">End day of simulation</td>
<td style="text-align: left;">31</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

</div>
