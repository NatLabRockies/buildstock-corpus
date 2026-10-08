<!-- comstock comstock_amy2018_2025_release_3 | technical_reference | documentation/reference_doc/4_5_envelope.tex | status: site_page | source_url: https://github.com/NatLabRockies/ComStock/blob/b77c60d341c9b68c58c5d51e51b06f08f293d3cb/documentation/reference_doc/4_5_envelope.tex | publication_url: https://natlabrockies.github.io/ComStock.github.io/assets/files/comstock_reference_documentation_2025_3.pdf | corpus_version: 43ae2d4 | corpus_path: technical_reference/documentation/reference_doc/4_5_envelope.md | section: Windows | lines: 44-264 -->
## Windows

#### Window Construction Type

Data from the NFRC Commercial Fenestration Market Study was used to develop the modeling approach for windows in ComStock. This study, conducted by Guidehouse in collaboration with NFRC, characterized the national commercial window stock through data collection and analysis. Six primary data sources representing all regions of the United States were used in the study—a 2020 Guidehouse survey, NEEA CBSA, DOE Code Study, CAEUS, CBECS, and RECS. A variety of window properties were collected, including the window-to-wall ratio, number of panes, frame material, glazing type, low-E coating, gas fill, solar heat gain coefficient (SHGC), U-factor, and many others. In total, the database contained approximately 16,000 samples, each with an appropriate weighting factor based on the coverage, completeness, and fidelity of each data source. The WWR data was already incorporated into the ComStock baseline during the EULP project. Some of the other key window properties such as thermal performance were then used to create the new baseline window constructions and distributions discussed later in this section. A summary of the data sources and their associated information is shown in Table  <a href="#tab:window_data_sources" data-reference-type="ref" data-reference="tab:window_data_sources">[tab:window_data_sources]</a>.

Four window properties—number of panes, glazing type, frame material, and low-E coating—were used to create the baseline window configurations. These four parameters were selected based on which characteristics have the most impact on window performance, which have the most data available from the various data sources, and which inputs we trust from the average building owner or survey recipient. The options for each property are shown in Figure <a href="#fig:window_configurations" data-reference-type="ref" data-reference="fig:window_configurations">3</a>.

<figure id="fig:window_configurations" data-latex-placement="ht!">
<img src="figures/window_configurations.png" style="width:50.0%" />
<figcaption>Window characteristics for number of panes, glazing type, frame material, and low-E coating.</figcaption>
</figure>

Modeling every combination of these four properties would result in 36 different window configurations, which would add significant complexity to the sampling process. Instead, we selected 12 combinations to be modeled, based on which combinations are most common and most realistic. There are four single-pane, six double-pane, and two triple-pane configurations. The unrealistic/uncommon combinations that were eliminated include:

- Single pane with thermally broken aluminum frame

- Single pane with low-E coating

- Double pane with wood frame

- Triple pane with no low-E coating

- Triple pane without thermally broken aluminum frame

- Thermally broken double or triple pane without low-E coating.

The 12 remaining window configurations are shown in Table <a href="#tab:window_configurations" data-reference-type="ref" data-reference="tab:window_configurations">1</a>.

<div id="tab:window_configurations" data-source="tables/window_configurations.tex">

| **Number of Panes** | **Glazing Type** | **Frame Material** | **Low-E Coating** |
|:---|:---|:---|:---|
| Single | Clear | Aluminum | No |
| Single | Tinted/Reflective | Aluminum | No |
| Single | Clear | Wood | No |
| Single | Tinted/Reflective | Wood | No |
| Double | Clear | Aluminum | No |
| Double | Tinted/Reflective | Aluminum | No |
| Double | Clear | Aluminum | Yes |
| Double | Clear | Aluminum With Thermal Break | Yes |
| Double | Tinted/Reflective | Aluminum | Yes |
| Double | Tinted/Reflective | Aluminum With Thermal Break | Yes |
| Triple | Clear | Aluminum With Thermal Break | Yes |
| Triple | Tinted/Reflective | Aluminum With Thermal Break | Yes |

Window Configurations

</div>

We created a sampling distribution for the new window constructions for the entire country using the initial data set. Overall, single-pane windows make up approximately 54% of the stock, double-pane windows make up 46%, and triple-pane windows make up \<1%. Initially, we created distributions based on census division to incorporate geographic location into the sampling. Upon further analysis, we found that it was also necessary to incorporate the energy codes into distributions to prevent scenarios where a single-pane window was sampled for a certain location, but, according to the energy code for that location, a double-pane window was required. For this reason, we modified the sampling distribution to include two dependencies—climate_zone and energy_code_followed_during_last_window_replacement.

To generate these sampling distributions, we used the maximum U-values specified for each climate zone in each version of ASHRAE 90.1, using climate zones defined by ASHRAE 169-2006. For each combination of climate zone and energy code, the 12 window configurations were evaluated to determine which were both realistic and met code (i.e., had a U-value lower than the code maximum U-value). For the older energy codes, we made several assumptions about technology adoption to determine which window configurations were realistic:

- Low-E coating—not adopted until DOE Ref 1980-2004

- Thermally broken aluminum frame—not adopted until 90.1-2004

- Triple pane—not adopted until 90.1-2004.

Each combination of climate zone and energy code included 2-12 window configurations that met the criteria. After limiting the distributions to these configurations, we renormalized the percentages from the national distribution to 100%. This kept the percentages from the national distribution while also incorporating intelligent assumptions based on climate zone and energy code. Table  <a href="#tab:window_distribution_4A" data-reference-type="ref" data-reference="tab:window_distribution_4A">2</a> provides an example of the window configurations that were sampled for each code year in climate zone 4A.

<div id="tab:window_distribution_4A" data-source="tables/window_distribution_4A.tex">

<table>
<caption>Window Distribution Assumptions Example from Climate Zone 4A</caption>
<tbody>
<tr>
<td style="text-align: left;"><strong>Energy Code Followed During Last Windows Replacement</strong></td>
<td style="text-align: right;"><strong>Pre-1980</strong></td>
<td style="text-align: right;"><strong>1980-2004</strong></td>
<td style="text-align: right;"><strong>90.1-2004</strong></td>
<td style="text-align: right;"><strong>90.1-2007</strong></td>
<td style="text-align: right;"><strong>90.1-2010</strong></td>
<td style="text-align: right;"><strong>90.1-2013</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Allowable Assembly Maximum U-Value</strong></td>
<td style="text-align: right;">1.22</td>
<td style="text-align: right;">0.59</td>
<td style="text-align: right;">0.57</td>
<td style="text-align: right;">0.55</td>
<td style="text-align: right;">0.55</td>
<td style="text-align: right;">0.42</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Allowable Assembly Maximum SHGC</strong></td>
<td style="text-align: right;">0.54</td>
<td style="text-align: right;">0.36</td>
<td style="text-align: right;">0.39</td>
<td style="text-align: right;">0.4</td>
<td style="text-align: right;">0.4</td>
<td style="text-align: right;">0.4</td>
</tr>
<tr>
<td style="text-align: left;">Single - No LowE - Clear - Aluminum  U-1.178 SHGC-0.744</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td style="text-align: left;">Single - No LowE - Tinted/Reflective - Aluminum  U-1.178 SHGC-0.579</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td style="text-align: left;">Single - No LowE - Clear - Wood  U-0.91 SHGC-0.683</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td style="text-align: left;">Single - No LowE - Tinted/Reflective - Wood  U-0.91 SHGC-0.525</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td style="text-align: left;">Double - No LowE - Tinted/Reflective - Aluminum  U-0.749 SHGC-0.484</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td style="text-align: left;">Double - No LowE - Clear - Aluminum  U-0.746 SHGC-0.646</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td style="text-align: left;">Double - LowE - Clear - Aluminum  U-0.559 SHGC-0.386</td>
<td style="text-align: right;"></td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td style="text-align: left;">Double - LowE - Tinted/Reflective - Aluminum  U-0.557 SHGC-0.274</td>
<td style="text-align: right;"></td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td style="text-align: left;">Double - LowE - Clear - Thermally Broken Aluminum  U-0.499 SHGC-0.378</td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
</tr>
<tr>
<td style="text-align: left;">Double - LowE - Tinted/Reflective - Thermally Broken Aluminum  U-0.496 SHGC-0.266</td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
</tr>
<tr>
<td style="text-align: left;">Triple - LowE - Clear - Thermally Broken Aluminum  U-0.3 SHGC-0.328</td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
</tr>
<tr>
<td style="text-align: left;">Triple - LowE - Tinted/Reflective - Thermally Broken Aluminum  U-0.299 SHGC-0.224</td>
<td style="text-align: right;"></td>
<td style="text-align: right;"></td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
<td style="text-align: right;">X</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td colspan="6" style="text-align: left;">X = This window type meets code minimums</td>
</tr>
</tbody>
</table>

</div>

As can be seen in Table <a href="#tab:window_distribution_4A" data-reference-type="ref" data-reference="tab:window_distribution_4A">2</a>, for DOE Ref Pre-1980, the only windows that met code and are realistic are single-pane or double-pane windows with no low-E coating. For DOE Ref 1980-2004, the maximum U-value dropped significantly, such that single-pane aluminum windows no longer met code. However, double-pane low-E windows became available on the market at that time. For 90.1-2004 through 90.1-2010, code required a U-value equivalent to double-pane low-E or better, and in 90.1-2013, the code improved again, meaning that double-pane low-E with a thermal break or better was required. This type of logic was applied to all combinations of climate zone and energy code. Then, we converted the data into the distributions used in sampling.

A small adjustment was made to the final distributions because some states and localities do not follow or enforce energy codes strictly. Following the code exactly would likely overestimate window performance. Therefore, in scenarios where single-pane windows were technically below code, we assumed that 5% of all windows in the stock would still have the worst-performing single-pane windows installed. The distributions were adjusted accordingly by subtracting 5% total from the double-pane configurations and adding to the single-pane aluminum configurations. After making this manual adjustment, the new distributions had the same overall breakdown as the national distribution generated from the Guidehouse data—54% single-pane and 46% double-pane .

#### Window Thermal Performance

Once the 12 new window constructions were determined, a team from Lawrence Berkeley National Laboratory’s (LBNL’s) Windows and Daylighting Group used the WINDOW program to assign thermal performance properties to each construction. SimpleGlazing objects in EnergyPlus were chosen to represent windows to reduce complexity. This choice also simplifies the process of applying upgrades, because all fenestration objects in the baseline models use the same object type. The inputs for the SimpleGlazing object are U-factor, solar heat gain coefficient (SHGC), and visible light transmittance (VLT). For each window configuration, LBNL assigned a frame ID and window ID from the WINDOW database. They also filled in the respective U-factors, SHGCs, and VLTs, which are shown in Table <a href="#tab:window_thermal_performance" data-reference-type="ref" data-reference="tab:window_thermal_performance">[tab:window_thermal_performance]</a>.

The U-factors originally ranged from U-1.18 Btu/h·ft<sup>2</sup>·F for the worst-performing single-pane window to U-0.30 Btu/h·ft<sup>2</sup>·F for the best-performing triple-pane window. As mentioned earlier in this section, the maximum U-Factor that EnergyPlus can model with a simple glazing object is U-1.02 Btu/h·ft<sup>2</sup>·F, which is governed by the limitations of a 2D heat transfer model when interior and exterior air films are included. Therefore, we adjusted the U-factor for the first two single-pane windows to be U-1.02 Btu/h·ft<sup>2</sup>·F rather than U-1.18 Btu/h·ft<sup>2</sup>·F. This allowed these windows to be modeled in ComStock. This results in a slight overestimate of the thermal performance of single-pane windows.

