<!-- comstock comstock_amy2018_2025_release_3 | github_site | docs/resources/explanations/combining_measure_results.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/resources/explanations/combining_measure_results.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/resources/explanations/combining_measure_results.html | corpus_version: fadc83e | corpus_path: github_site/docs/resources/explanations/combining_measure_results.md | section: Example from 2023 Release 2: HVAC and Lighting | lines: 15-68 -->
## Example from 2023 Release 2: HVAC and Lighting
The “HVAC and Envelope” example concerns two upgrade technologies that directly impact HVAC needs of a building, so it’s more obvious why the individual savings results cannot be added together since there is interaction between the building envelope composition and the HVAC system. However, the same is true for upgrades that don’t directly concern HVAC or thermal envelope. For example, the energy savings from the [LED Lighting](https://www.nlr.gov/docs/fy24osti/86100.pdf) measure from that same data release also should not be added to the Heat Pump RTU upgrade because lighting also impacts the heat balance of the building. Lighting systems in buildings give off heat, and the amount of heat depends on the lighting technology. For example, LED lighting gives off notably less heat than other commercial building lighting technologies such as incandescent, fluorescent, or halogen fixtures. For the LED lighting upgrade, the new LED lighting system gives off less heat than the previously installed technology. This causes a decrease in cooling loads and an increase in heating loads that will need to be addressed by the new Heat Pump RTU HVAC system. Understanding the joint impact of the LED Lighting and the Heat Pump RTU upgrade requires a new model run with these upgrades together as a package to appropriately model the interactive effects between the measures.

In ComStock 2023 Release 2, these two upgrades were in fact run together as a package: [Package 2: LED Lighting + HP RTU or HP Boilers](https://www.nlr.gov/docs/fy24osti/86601.pdf). Because of this, we can examine the error that would occur if we tried to add the individual savings from the LED Lighting and Heat Pump RTU measures together instead of running them as a package. We pull three individual modeled buildings from ComStock 2023 Release 2 as examples (see table, below). Note that models with the package applied have either the Heat Pump RTU _or_ Heat Pump Boiler measures applied, not both. For the three models in this example, the Heat Pump RTU measure was applied with the LED Lighting measure. For each model, we assess the annual site energy savings (*out.site_energy.total.energy_savings*) from each upgrade—the individual Heat Pump RTU and LED Lighting measures, and with the package. We can then compare the savings results from adding the individual measures with the package run. In this example, errors range from -10.4% to 15.1%.

<p style="text-align: center;"><b>Energy Savings by ComStock 2023 Release 2 Upgrade</b></p>

<table>
    <tr>
        <td rowspan="2"><b>Building ID</b></td>
        <td rowspan="2"><b>Building Type</b></td>
        <td rowspan="2"><b>State</b></td>
        <td style="text-align: center" colspan="5"><b>Annual Site Energy Savings (kWh)</b></td>
    </tr>
    <tr>
        <td><b>1. Heat Pump RTU – only</b></td>
        <td><b>10. LED Lighting – only</b></td>
        <td><b>17. Package 2, LED + HP RTU or HP Boiler</b></td>
        <td><b>Sum Upgrades 1 + 10</b></td>
        <td><b>% Error</b></td>
    </tr>
    <tr>
        <td>62841</td>
        <td>Strip Mall</td>
        <td>CO</td>
        <td>114,644</td>
        <td>47,778</td>
        <td>181,364</td>
        <td>162,422</td>
        <td>-10.40%</td>
    </tr>
    <tr>
        <td>93569</td>
        <td>Medium Office</td>
        <td>FL</td>
        <td>584,830</td>
        <td>71,372</td>
        <td>569,650</td>
        <td>656,202</td>
        <td>15.10%</td>
    </tr>
    <tr>
        <td>205619</td>
        <td>Full-Service Restaurant</td>
        <td>NY</td>
        <td>40,492</td>
        <td>10,317</td>
        <td>55,694</td>
        <td>50,809</td>
        <td>-8.80%</td>
    </tr>
</table>

This same logic can be extrapolated to nearly any energy-consuming equipment in the building such as water heating systems, cooking equipment, electronics, and other internal loads. Upgrade measures that do not directly involve HVAC equipment can yield misleading results due to interactions between the upgrades, such as an interior lighting technology upgrade paired with lighting controls. Additionally, consumption of energy typically gives off some sort of heat that impacts heating and cooling loads. In extremely rare circumstances, energy savings from a piece of electric equipment which gives off minimal heat might be able to be added to another upgrade measure as a rough approximation of energy impacts, but no upgrade measures have been run in ComStock to-date that would qualify for that exemption.
