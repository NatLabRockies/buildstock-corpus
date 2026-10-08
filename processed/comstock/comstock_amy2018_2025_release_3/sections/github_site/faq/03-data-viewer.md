<!-- comstock comstock_amy2018_2025_release_3 | github_site | docs/faq.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/faq.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/faq.html | corpus_version: 267e3ea | corpus_path: github_site/docs/faq.md | section: Data Viewer | lines: 211-278 -->
## Data Viewer
<ul class="jk_accordion">

  <li class="acc" id="faq-data-viewer-section"><input id="faq-data-viewer" type="checkbox" /><label for="faq-data-viewer">What is the Data Viewer?</label>
    <div class="show">
      <p>The Data Viewer is a web-based visualization platform that allows users to easily filter, aggregate, view, and download ComStock end-use energy data in a web browser.</p>
      <p>Links to Data Viewer visualizations for each dataset release are on the <a href="docs/data.md">Data page</a>.</p>
      <p>For Data Viewer trainings, visit the <a href="https://www.youtube.com/playlist?list=PLmIn8Hncs7bEYCZiHaoPSovoBrRGR-tRS">NLR’s Building Stock Analysis YouTube channel</a>.</p>
    </div>
  </li>

  <li class="acc" id="faq-sum-avg-def-section"><input id="faq-sum-avg-def" type="checkbox" /><label for="faq-sum-avg-def">In the Data Viewer, what does "sum" or "average" mean?</label>
    <div class="show">
      <p>The "sum" aggregation is the total energy consumption for all buildings that meet the filter criteria across all the occurrences of the given time step within the selected month(s). For example, in a day timeseries range for a specific state for the month of July, the 7-7:15 AM hour time step shows the sum of all energy consumption statewide between 7-7:15 AM in July, from buildings that meet the filter criteria. The "sum" view has fewer uses than the "average" view. The "average" aggregation is the total energy consumption for all buildings that meet the filter criteria, averaged across all the occurrences of the given time step within the selected month(s).</p>
      <p>For example, in a day timeseries range for a specific state for the month of July, the 7-7:15 AM hour time step shows the average statewide energy consumption between 7-7:15 AM in July, from buildings that meet the filter criteria. The "average" aggregation provides a view of the average day of total energy consumption in the state. This is the more logical view for most use cases. Note that while each time step within a day or a year has the same number of occurrences within each dataset, each time step for a week does not - some days of the week occur more times than others in each year or month range (except for February).
      </p>
    </div>
  </li>

  <li class="acc" id="faq-peak-day-def-section"><input id="faq-peak-day-def" type="checkbox" /><label for="faq-peak-day-def">In the Data Viewer, how are the peak day and min peak day defined?</label>
    <div class="show">
      <p>The peak day is the day with the highest single-hour (peak) energy consumption within the selected months.</p>
      <p>The min peak day is the day with the lowest single-hour energy consumption within the selected months.</p>
    </div>
  </li>

  <li class="acc" id="faq-slow-load-section"><input id="faq-slow-load" type="checkbox" /><label for="faq-slow-load">Why is the time series data sometimes slow to load after I click the update button?</label>
    <div class="show">
      <p>We query data in real time to produce the time series graphs you see on the webpage, and this can involve scanning terabytes (TB) of data. Running a baseline-only query for California, Texas, New York, or Illinois takes around a minute, while running a query for a state like Colorado or Massachusetts takes about 10-20 seconds. However, if the graphs have previously been generated we have the data cached and can typically load the data in a few seconds. That's why the load time varies.</p>
    </div>
  </li>

  <li class="acc" id="faq-explore-timeseries-section"><input id="faq-explore-timeseries" type="checkbox" /><label for="faq-explore-timeseries">Why can’t I click on “Explore Timeseries”?</label>
    <div class="show">
      <p>The “Explore Timeseries” option is available once a specific geography (e.g. state or PUMA region) is selected.</p>
    </div>
  </li>

  <li class="acc" id="faq-end-use-view-section"><input id="faq-end-use-view" type="checkbox" /><label for="faq-end-use-view">How do I see a profile for just one, or just a few, end uses?</label>
    <div class="show">
      <p>Clicking on the end uses in the legend will highlight the end use in the visualization.</p>
    </div>
  </li>

  <li class="acc" id="faq-agg-locations-section"><input id="faq-agg-locations" type="checkbox" /><label for="faq-agg-locations">Can I aggregate over multiple locations?</label>
    <div class="show">
      <p>The viewer allows aggregations of up to six locations (states or PUMAs, depending on the dataset). When viewing a single location, choose the “+ More Locations” option, add up to five additional locations, and choose “Update Search”.</p>
      <p>Additionally, sums of more than six locations can be created manually by downloading sums of up to six locations and summing further on your local computer.</p>
      <p>TMY3 weather is not aligned between locations. This does not affect our recommendations for working with annual data. However, if your application requires timeseries data and therefore would benefit from aligned weather, we recommend either using an AMY dataset, or filtering by weather station and summing only within a single weather station’s PUMAs.</p>
    </div>
  </li>

  <li class="acc" id="faq-filter-characteristics-section"><input id="faq-filter-characteristics" type="checkbox" /><label for="faq-filter-characteristics">How can I filter the data based on building characteristics?</label>
    <div class="show">
      <p>The "+ Filter" button enables users to filter the data by characteristics, such as vintage, floor area, and building type. This feature also enables aggregations of locations, including by PUMA and county.</p>
      <p>See our <a href="https://www.youtube.com/watch?v=1hzT7MGsAC8&list=PLmIn8Hncs7bEYCZiHaoPSovoBrRGR-tRS&index=14">YouTube training video</a> on the Data Viewer, around 3:50, to learn how to add multiple filters.</p>
    </div>
  </li>

  <li class="acc" id="faq-view-characteristics-section"><input id="faq-view-characteristics" type="checkbox" /><label for="faq-view-characteristics">How can I see the building characteristics associated with an aggregate load profile from the data viewer?</label>
    <div class="show">
      <p>The building characteristics are available on the Open Energy Data Initiative (OEDI) data lake. Visit the <a href="docs/data.md">Data page</a> for links to the OEDI pages for each dataset. In the "metadata_and_annual_results_aggregate" directory on OEDI, navigate to the national file: metadata_and_annual_results_aggregates > national > full > csv > baseline_agg.csv.gz. Download the file, unzip it and open in Microsoft Excel. Use the filters applied on the Data Viewer to filter the spreadsheet.</p>
      <p>Note that the national file is an “aggregate,” meaning that the data in the file is consolidated by merging duplicate building models within a geography (in this case state), so each building ID appears only once with a combined weight. Columns that cannot be meaningfully aggregated from the tract level—such as Cambium grid region and CEJST designation—are excluded from the resulting low-resolution, “aggregate” files. For more information about the updated OEDI file structure as a result of the new sampling method, please see the "<a href="docs/resources/explanations/new_sampling_method.md">New ComStock Sampling Method</a>" explanation.</p>
    </div>
  </li>

</ul>

