<!-- comstock comstock_amy2018_2025_release_3 | github_site | docs/faq.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/faq.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/faq.html | corpus_version: b5faf42 | corpus_path: github_site/docs/faq.md | section: ComStock Essentials | lines: 8-69 -->
## ComStock Essentials
<ul class="jk_accordion">

  <li class="acc" id="faq-simulated-section"><input id="faq-simulated" type="checkbox" /><label for="faq-simulated">Are these load profiles measured or simulated?</label>
    <div class="show">
      <p>The profiles are simulated using the ResStock and ComStock modeling tools, which have been validated and informed by the best available data against an array of empirical datasets. ResStock and ComStock use the EnergyPlus simulation engine. The validation results and uncertainty for quantities of interest are presented in the <a href="https://www.nlr.gov/docs/fy22osti/80889.pdf">End-Use Load Profiles final report.</a></p>
      <p>ResStock generally simulates 550,000 individual building energy models, and ComStock simulates 150,000 building energy models.</p>
    </div>
  </li>

  <li class="acc" id="faq-building-types-section"><input id="faq-building-types" type="checkbox" /><label for="faq-building-types">What building types does ComStock model?</label>
    <div class="show">
      <p>ComStock models 15 commercial building types. Compared to the Commercial Building Energy Consumption Survey (CBECS) 2018 estimation, ComStock datasets account for 63% of both the energy use and floor area of commercial buildings in the United States. The ComStock development team is actively working on adding more building types to the model. See the explanation titled "<a href="docs/resources/explanations/building_types_not_included.md">Building Types Not Included in ComStock</a>" for more detail.</p>
    </div>
  </li>

  <li class="acc" id="faq-year-section"><input id="faq-year" type="checkbox" /><label for="faq-year">What year does the baseline stock represent?</label>
    <div class="show">
      <p>The ComStock and ResStock datasets represent, as closely as possible, the 2018 U.S. commercial and residential building stock characteristics. The energy consumption results depend on the weather data used in the simulations. When modeled with AMY2018 weather, the datasets represent energy use for the year 2018. When TMY3 weather is used, they represent typical or average energy consumption under typical climate conditions.</p>
      <p>Emissions and utility bills in the ComStock and ResStock datasets use input data from a several years, depending on the dataset release. See the <a href="docs/resources/resources.md#references">ComStock reference documentation</a> or <a href="https://docs.nlr.gov/docs/fy25osti/91621.pdf">ResStock reference documentation</a> for more details.</p>
    </div>
  </li>

  <li class="acc" id="faq-credible-section"><input id="faq-credible" type="checkbox" /><label for="faq-credible">Are ComStock and ResStock credible?</label>
    <div class="show">
       <p>Yes. The models underwent extensive calibration as part of the End Use Load Profiles (EULP) project where we compared model load profiles to AMI data from around the country, and updated baseline model schedules, power densities, among other things using various data sources. Reference the <a href="https://www.nlr.gov/docs/fy22osti/80889.pdf">final report</a> for more details. The EULP project concluded in 2021.</p>
      <p>For every baseline update and upgrade measures since EULP, ComStock compares energy consumption and EUI to available data sources, such as CBECS and EIA. These comparisons are available on the OEDI Data Lake for each dataset. You can find links to OEDI in the Published Datasets section of the <a href="docs/data.md">Data page</a>.</p>
      <p>For details about how to determine whether the models are appropriate for a specific analysis, reference the explanation titled "<a href="docs/resources/explanations/comstock_calibration.md">Considerations for ComStock Calibration, Validation, and Uncertainty</a>."</p>
    </div>
  </li>

  <li class="acc" id="faq-dataset-release-section"><input id="faq-dataset-release" type="checkbox" /><label for="faq-dataset-release">Which dataset release should I use? And can I compare upgrades from different dataset releases?</label>
    <div class="show">
      <p>ComStock publishes datasets on a regular basis, and we recommend using the latest release. See the <a href="docs/data.md">Data page</a> for a list of available datasets and access links.</p>
      <p>It is not necessary to compare upgrades across ComStock dataset releases because all datasets include both new upgrade measures and all measures from previous releases, as well as any improvements made to the baseline model.  Information about upgrade measures included in dataset releases can be found on the <a href="docs/upgrade_measures/upgrade_measures.md">Upgrade Measures page</a>. Baseline model improvements are captured in the release change log on our <a href="https://github.com/NatLabRockies/ComStock">public GitHub repository</a>. Note that we re-sample our input characteristic distributions for every release and as a result, the building IDs between releases will not match.</p>
    </div>
  </li>

  <li class="acc" id="faq-weights-section"><input id="faq-weights" type="checkbox" /><label for="faq-weights">What are weights in ComStock and how are they used?</label>
    <div class="show">
      <p>Weights in ComStock represent the number of real buildings in the U.S. building stock that a ComStock model represents. Weights are determined using national floor area by building type from CBECS. Use the weights by multiplying the energy consumption column by the weight for the model. Some results columns already have the weight applied. These have the word “weighted” in the name. See the explanation titled "<a href="docs/resources/explanations/sampling_and_weighting.md">Sampling and Weighting in ComStock</a>" for more information.</p>
    </div>
  </li>

  <li class="acc" id="faq-sample-count-section"><input id="faq-sample-count" type="checkbox" /><label for="faq-sample-count">How many profiles or models should be used for an analysis, and how does the number used affect uncertainty of results?</label>
    <div class="show">
      <p>The minimum sample count required for a given geography in ComStock is a function of the number of commercial buildings present in that area, as well as the quality of available input data for the ComStock model. To ensure statistical robustness in your analysis using ComStock, you may need additional building models depending on the specificity of your segmentation. A good rule of thumb is to include at least six models per segment (e.g., building type, sub-type, size, vintage, or operation hours). For example, if you’re analyzing small office buildings open more than 18 hours a day, make sure you have at least six such models.</p>
      <p>Also, cross-check ComStock’s building representation with external sources (like Google Maps or local datasets) to ensure the dataset reflects your target geography. For more detail, see the explanation titled "<a href="docs/resources/explanations/sample_size_considerations.md">Sample Size Considerations</a>"</p>
      <p>Queries in sparsely populated areas or with filters applied may have relatively few samples available. In these cases, samples from nearby locations can be grouped to increase the sample size. See the tutorial titled "<a href="docs/resources/tutorials/local_segmentation_study.md">Perform an analysis by blending ComStock and local data</a>" for an example of incorporating local floor area estimates to improve representation of ComStock data at specific geographic resolutions.</p>
      <p>Users should estimate standard error for metrics of interest using the standard deviation divided by the square root of the number of samples (i.e., profiles or models). See Section 5.1.3 in the <a href="https://www.nlr.gov/docs/fy22osti/80889.pdf">End-Use Load Profiles methodology report</a> for a discussion on uncertainty calculations.
      </p>
    </div>
  </li>

  <li class="acc" id="faq-citation-section"><input id="faq-citation" type="checkbox" /><label for="faq-citation">How should I cite the datasets?</label>
    <div class="show">
      <p>ComStock and ResStock can be cited according to the suggestions <a href="docs/citation.md">here for ComStock</a> and <a href="https://natlabrockies.github.io/ResStock.github.io/docs/citation_data_attribution.html"> here for ResStock</a>.</p>
    </div>
  </li>

</ul>

