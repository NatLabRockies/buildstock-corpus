<!-- comstock comstock_amy2018_2025_release_3 | github_site | docs/faq.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/faq.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/faq.html | corpus_version: 0a2f61f | corpus_path: github_site/docs/faq.md | section: Modeling Methods, Assumptions and Documentation | lines: 298-371 -->
## Modeling Methods, Assumptions and Documentation
<ul class="jk_accordion">

  <li class="acc" id="faq-ref-section"><input id="faq-ref" type="checkbox" /><label for="faq-ref">Where can I find information about ComStock modeling methodology and assumptions?</label>
    <div class="show">
      <p>ComStock reference documentation is available in the <a href="docs/resources/resources.md#references">References section</a> of the <a href="docs/resources/resources.md">Resources page</a>. We publish an updated version with every dataset release that includes changes to the ComStock model.</p>
    </div>
  </li>

  <li class="acc" id="faq-costs-section"><input id="faq-costs" type="checkbox" /><label for="faq-costs">Are costs modeled?</label>
    <div class="show">
      <p>As of the 2024 Release 1, ComStock includes utility cost data using current electricity rates from the Utility Rate Database (URDB), matched by utility ID, demand, and usage. Annual utility bills are reported as the min, max, mean, and median of all applicable rates for each model. Natural gas, propane, and fuel oil prices are based on volumetric pricing due to limited rate data, using EIA price and heat content data. See the <a href="docs/resources/resources.md#references">ComStock reference documentation</a> for details.</p>
      <p>ComStock does not calculate first costs (i.e., upgrade or measure costs). However, many ComStock output variables can be used to estimate first cost. See the explanation titled "<a href="docs/resources/explanations/costing_analysis.md">Using ComStock to Analyze Cost</a>" for more detail about cost assessments, including a discussion of output variables that can be used to estimate first costs.</p>
    </div>
  </li>

  <li class="acc" id="faq-pv-section"><input id="faq-pv" type="checkbox" /><label for="faq-pv">Does ComStock model rooftop solar PV?</label>
    <div class="show">
      <p>ComStock does not currently model rooftop solar PV in the baseline. However, starting with ComStock 2025 Release 1, upgrade measures are available that model rooftop solar PV additions to buildings. See the <a href="docs/upgrade_measures/upgrade_measures.md"> Upgrade Measures</a> page for more information.</p>
    </div>
  </li>

  <li class="acc" id="faq-ev-section"><input id="faq-ev" type="checkbox" /><label for="faq-ev">Are there electric vehicle (EV) charging profiles in the dataset?</label>
    <div class="show">
      <p>No, ComStock does not currently model EV charging in the dataset. For modeling aggregate EV load profiles for a city or state, we suggest using <a href="https://afdc.energy.gov/evi-pro-lite/load-profile">EVI-Pro Lite</a>. Measured charging profile data for individual homes can be found in the <a href="https://neea.org/data/nw-end-use-load-research-project/energy-metering-study-data">NEEA HEMS data</a> and <a href="https://www.pecanstreet.org/dataport/">Pecan Street Dataport</a>. Email us at <a href="mailto:ComStock@nlr.gov">ComStock@nlr.gov</a> if you have suggestions for other EV charging data sources.</p>
    </div>
  </li>

  <li class="acc" id="faq-water-heater-section"><input id="faq-water-heater" type="checkbox" /><label for="faq-water-heater">Are there water heater upgrade measures available?</label>
    <div class="show">
      <p>We have not published a service water heating measure due to current water draw profiles in our baseline models. The energy consumed by heat pump water heaters (HPWHs), especially, is sensitive to how quickly the water in the tank is consumed. More specifically, how to design and size a HPWH system greatly relies on realistic water draw profiles to correctly capture when the heat pump heating and, especially, backup heating elements are triggered.</p>
      <p>If you are aware of water draw profile data, please let email us at <a href="mailto:ComStock@nlr.gov">ComStock@nlr.gov</a>! We are in search of 15-min to hourly water draw profiles for commercial buildings of various types and square footage.</p>
    </div>
  </li>

  <li class="acc" id="faq-data-centers-section"><input id="faq-data-centers" type="checkbox" /><label for="faq-data-centers">Does ComStock model data centers?</label>
    <div class="show">
      <p>We do not currently model data centers as a building type in ComStock. Some large office buildings include data center loads, but these do not capture the characteristics, performance, HVAC system, etc. of standalone data centers and we do not recommend extrapolating results from these models.</p>
    </div>
  </li>

  <li class="acc" id="faq-leap-year-section"><input id="faq-leap-year" type="checkbox" /><label for="faq-leap-year">How are leap years modeled?</label>
    <div class="show">
      <p>ComStock public dataset releases include AMY2012 weather, which is a leap year, and AMY2018 and TMY3 weather years, neither of which are leap years.</p>
      <p>The default simulation runs for one year, covering 8,760 hours from January 1 to December 31. For ComStock dataset releases using AMY2012 weather, the simulation period is adjusted to maintain exactly 8,760 hours: it starts on January 1, includes February 29, and ends on December 30 instead of December 31.</p>
      <p>For more detail, please see the <a href="docs/resources/resources.md#references">ComStock reference documentation</a>.</p>
    </div>
  </li>

  <li class="acc" id="faq-multifamily-section"><input id="faq-multifamily" type="checkbox" /><label for="faq-multifamily">How are multifamily common areas modeled?</label>
    <div class="show">
      <p>The residential housing units in multifamily buildings are modeled in ResStock and are not in ComStock.  All energy consumption specific to the housing unit is included in the modeled results, such as lighting, appliances, window air conditioners, and HVAC and water heaters that serve a single housing unit.</p>
      <p>HVAC and water heating that serves multiple housing units are also included, with energy consumption allocated to the unit served and with adjustment factors applied to account for the energy consumption differences of shared equipment. These adjustment factors are set by OpenStudio-HPXML and from ANSI/RESNET 301.</p>
      <p>Electric vehicle charging energy consumption from common areas is also included in ResStock results, allocated directly to the unit that is associated with each electric vehicle.</p>
      <p>All other energy that provides services to common areas in multifamily buildings is not included in either ResStock or ComStock. Examples of this would include common area lighting, common laundry facilities, pools, and hot tubs, and elevators.</p>
    </div>
  </li>

  <li class="acc" id="faq-walls-section"><input id="faq-walls" type="checkbox" /><label for="faq-walls">How are wall cavity R-values determined?</label>
    <div class="show">
      <p>In ComStock models, wall R-values are based on building energy code requirements by climate zone and construction type (mass, metal building, steel-framed, wood-framed) and account for both interior and exterior air films.</p>
      <p>See the <a href="docs/resources/resources.md#references">ComStock reference documentation</a> for more information.</p>
    </div>
  </li>

  <li class="acc" id="faq-census-section"><input id="faq-census" type="checkbox" /><label for="faq-census">What year of U.S. Census geography (e.g., counties, PUMAs) do ComStock and ResStock use?</label>
    <div class="show">
      <p>ComStock and ResStock datasets reflect the 2010 National Historical GIS (NHGIS) GISJOIN standard codes for counties, PUMAs, and Census Tracts. Some model input data sources use 2020 Census geographies, and these are translated to 2010 before being integrated into the ComStock and ResStock workflows. However, 2020 geographic codes are not currently available in the ComStock and ResStock datasets.</p>
      <p>For more information about geographic fields and codes used in the models, please refer to the <a href="docs/resources/explanations/reference_geographic_codes.md">ComStock</a> and <a href="https://natlabrockies.github.io/ResStock.github.io/docs/resources/explanations/Geographic_Fields_and_Codes.html">ResStock</a> user resources.
      </p>
    </div>
  </li>

</ul>
