<!-- comstock comstock_amy2018_2025_release_3 | github_site | docs/faq.md | status: site_page | source_url: https://github.com/NatLabRockies/ComStock.github.io/blob/bacf551bc5d2f595d2b3c41a57de0beea23ec6be/docs/faq.md | publication_url: https://natlabrockies.github.io/ComStock.github.io/docs/faq.html | corpus_version: 0a2f61f | corpus_path: github_site/docs/faq.md | section: Datasets and Data Access | lines: 70-210 -->
## Datasets and Data Access
<ul class="jk_accordion">
  <li class="acc" id="faq-dataset-access-section"><input id="faq-dataset-access" type="checkbox" /><label for="faq-dataset-access">How do I access the dataset?</label>
    <div class="show">
      <p>There are several access platforms available to access ComStock and ResStock datasets. See the <a href="docs/data.md">ComStock Data page</a> and <a href="https://natlabrockies.github.io/ResStock.github.io/docs/data.html">ResStock Data page</a> for more detail about dataset access and links to the public datasets.</p>
    </div>
  </li>

  <li class="acc" id="faq-data-dictionary-section"><input id="faq-data-dictionary" type="checkbox" /><label for="faq-data-dictionary">Are descriptions available for the end-use categories and fields available for filtering?</label>
    <div class="show">
      <p>Descriptions of each of the building characteristics and the end-use categories can be found in the “data_dictionary.tsv” file. Descriptions of the values used in those filters can be found in the “enumeration_dictionary.tsv”. Both files can be downloaded from the OEDI Data Lake and are unique to each dataset release. Use the correct data dictionary for the relevant dataset. They can be opened with Excel or a text editor.</p>
      <p>Links to the OEDI Data Lake for each dataset release can be found on the <a href="docs/data.md">ComStock Data page</a> and <a href="https://natlabrockies.github.io/ResStock.github.io/docs/data.html">ResStock Data page</a>.</p>
    </div>
  </li>

  <li class="acc" id="faq-units-section"><input id="faq-units" type="checkbox" /><label for="faq-units">What are the data units?</label>
    <div class="show">
      <p>ComStock and ResStock data have multiple units. For annual results data downloaded from the Open Energy Data Initiative (OEDI) data lake, units can be found in the "data_dictionary.tsv" file. Some fields will also have the units in the column header at the end of the name (e.g., "out.electricity.total.jan.energy_consumption..<b>kwh</b>"). Timeseries energy consumption data on OEDI are provided in kWh. Natural gas, fuel oil, and propane are output in kwh--this is intentional though unconventional.</p>
      <p>The Data Viewer provides energy data in metric units, visible in the y-axis label. Depending on the scale of energy being shown, the metric prefix will automatically adjust (T for tera, G for giga, M for mega, etc.).</p>
      <p>For Tableau dashboards, use the relevant column headers or the graph axis to see the units.</p>
    </div>
  </li>

  <li class="acc" id="faq-timezone-section"><input id="faq-timezone" type="checkbox" /><label for="faq-timezone">What is the timezone of the timestamps?</label>
    <div class="show">
      <p>The timestamps of all load profiles have been converted to Eastern Standard Time, to prevent issues when aggregating across time zones.</p>
      <p>The underlying modeling was conducted using local standard time for each location, with occupant schedules adjusted for daylight savings as applicable. All EnergyPlus timeseries outputs were converted from local standard time to Eastern Standard Time for publication in the web Data Viewer, Data Viewer exports, timeseries aggregates, and individual timeseries parquet files. In converting from local Standard Time to Eastern Standard Time, if necessary the last few hours of each dataset were moved to the beginning of the timeseries. For example, the first two hours of data from Colorado in Eastern Standard Time (Jan 1, midnight to 2 AM) were originally modeled as the last two hours of the year in Mountain Standard Time (Dec 31, 10 PM to midnight) using the corresponding weather. For leap years (e.g., 2012), the two hours come from Dec 30 rather than Dec 31. Please see <i>How are leap years modeled?</i> FAQ for more info.</p>
    </div>
  </li>

  <li class="acc" id="faq-timestamp-section"><input id="faq-timestamp" type="checkbox" /><label for="faq-timestamp">Does the timestamp represent the beginning, middle, or end of each 15-minute interval?</label>
    <div class="show">
      <p>The timestamp indicates the end of each 15-minute interval. So "12:15" represents the energy use between 12:00 and 12:15.</p>
    </div>
  </li>

  <li class="acc" id="faq-timeseries-agg-weights-section"><input id="faq-timeseries-agg-weights" type="checkbox" /><label for="faq-timeseries-agg-weights">Do the timeseries aggregates have the sample weighting factors applied?</label>
    <div class="show">
      <p>Yes. The aggregates represent the total relevant building stock with all relevant weights applied (e.g., all small office buildings in the state of Colorado), not just the sum of the model results.</p>
    </div>
  </li>

  <li class="acc" id="faq-cec-climate-zones-section"><input id="faq-cec-climate-zones" type="checkbox" /><label for="faq-cec-climate-zones">Are there load profiles available for the 16 California Climate Zones?</label>
    <div class="show">
      <p>ComStock includes commercial buildings in California, and the datasets provide California Energy Commission (CEC) climate zones in the field “in.cec_climate_zone” in the metadata_and_annual_results and metadata_and_annual_results_aggregates files on the OEDI data lake.</p>
      <p>There are a few known issues with California models in ComStock. Please see the "<a href="docs/resources/explanations/california_known_issues.md">California Models Known Issues</a>" explanation for more information.</p>
    </div>
  </li>

  <li class="acc" id="faq-geographic-fields-section"><input id="faq-geographic-fields" type="checkbox" /><label for="faq-geographic-fields">What do the codes used to describe "county_id" and other geographic fields mean?</label>
    <div class="show">
      <p>ComStock and ResStock use the National Historical GIS (NHGIS) GISJOIN standard codes for county, census PUMA, and census tract, which are based on Federal Information Processing System (FIPS) codes. The datasets use the 2010 version of the GISJOIN codes--2020 are not available at this time. For more information about the geospatial fields available in the datasets, see <a href="docs/resources/explanations/reference_geographic_codes.md">this explanation for ComStock</a>, and <a href="https://natlabrockies.github.io/ResStock.github.io/docs/resources/explanations/Geographic_Fields_and_Codes.html">this explanation for ResStock.</a></p>
      <p>In most ComStock and ResStock datasets, county name is available in addition to the GISJOIN county code. For both tools, the column in the metadata_and_annual_results files on OEDI is called "in.county_name."
      </p>
    </div>
  </li>

  <li class="acc" id="faq-measure-docs-section"><input id="faq-measure-docs" type="checkbox" /><label for="faq-measure-docs">Where can I find documentation on what technologies are available in the upgrade measures?</label>
    <div class="show">
      <p>See the <a href="docs/upgrade_measures/upgrade_measures.md">Upgrade Measures</a> page for a complete list of available upgrade measures and packages in ComStock datasets, including a link to their documentation, and in which dataset release the measure was first included.</p>
    </div>
  </li>

  <li class="acc" id="faq-epw-section"><input id="faq-epw" type="checkbox" /><label for="faq-epw">Are weather data files available in EPW format?</label>
    <div class="show">
      <p>Weather data used for the modeling have been provided in .csv format for regression modeling, forecasting, or other analyses. The TMY3 weather files in EnergyPlus input format (EPW) can be downloaded from the <a href="https://data.nlr.gov/submissions/156">NLR Data Catalog</a>, with filenames that correspond to county IDs in the ResStock and ComStock metadata. EPW format weather files for 2018 or other actual meteorological years (AMY) have not been publicly released. These files can be purchased from private sector vendors. See <a href="https://energyplus.net/weather/simulation">here</a> for a list of providers.
      </p>
    </div>
  </li>

  <li class="acc" id="faq-idf-osm-section"><input id="faq-idf-osm" type="checkbox" /><label for="faq-idf-osm">Are the EnergyPlus model input files (.idf) or OpenStudio (.osm) files available?</label>
    <div class="show">
      <p>OpenStudio model input files (.osm) are available in the dataset on the OEDI data lake in the "building_energy_models" directory. Files are named by the building ID ("bldg_id").  The EnergyPlus model input files are not available.</p>
    </div>
  </li>

  <li class="acc" id="faq-api-section"><input id="faq-api" type="checkbox" /><label for="faq-api">Is there an API to access data without downloading locally?</label>
    <div class="show">
      <p>Currently, there is no API. However, we have posted a <a href="https://www.youtube.com/watch?v=qSR1MFpSiro&list=PLmIn8Hncs7bEYCZiHaoPSovoBrRGR-tRS&index=4">tutorial example</a> showing how to load the datasets into cloud services such as Amazon Web Services (AWS) so the data can be queried by analytic tools like Athena.</p>
      <p>Example notebooks and SQL queries are also available on the "<a href="docs/resources/how_to_guides/example_scripts.md">Access ComStock datasets programmatically</a>" page, and more will be added as we develop them. The queries and example notebooks are a good starting point for accessing ResStock programmatically, too.</p>
    </div>
  </li>

  <li class="acc" id="faq-timeseries-for-bldg-id-section"><input id="faq-timeseries-for-bldg-id" type="checkbox" /><label for="faq-timeseries-for-bldg-id">How do I access the timeseries data for a specific building model?</label>
    <div class="show">
      <p>To download a few results by IDs, you can use a manual approach. First use the metadata_and_annual_results to find the IDs you want to access. Then, note the download URL for any easy-to-access ID and edit it to reflect the ID you want.</p>
      <p> For example, right clicking on the first ID under ResStock dataset 2022.1.1, AMY 2018, upgrade 02, and choosing “copy link” provides this URL: <a href="https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/resstock_amy2018_release_1.1/timeseries_individual_buildings/by_state/upgrade=2/state=WA/100025-2.parquet">https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2022/resstock_amy2018_release_1.1/timeseries_individual_buildings/by_state/upgrade=2/state=WA/100025-2.parquet</a>. To access ID 813 instead of 100025, change the “100025-2” to “813-2” in the URL, and paste it into a web browser. That will download the data for ID 813.</p>
    </div>
  </li>

  <li class="acc" id="faq-parquet-section"><input id="faq-parquet" type="checkbox" /><label for="faq-parquet">What software can I use to open the .parquet files?</label>
    <div class="show">
      <p>Parquet files can be read using programming languages such as Python, using the pyarrow package. For other options, see <a href="https://arrow.apache.org/docs/index.html">here</a>. There are a few third-party graphical tools for viewing parquet files, but we have not tested them and the third-party support is limited.</p>
      <p>See below for example Python code to convert parquet file to csv.
        <pre><code>
        import pandas as pd
        import os
        folder_path = 'C:/Users/username/Documents/EUSS/Results’
        file_name = '813-2'
        suffix = '.parquet'
        file = pd.read_parquet(os.path.join(folder_path, file_name+suffix))
        new_suffix = '.csv'
        file.to_csv(os.path.join(folder_path, file_name+new_suffix), index=False)
        </code></pre>
      </p>
    </div>
  </li>

  <li class="acc" id="faq-bldg-ids-section"><input id="faq-bldg-ids" type="checkbox" /><label for="faq-bldg-ids">I am trying to match buildings between releases. Why do the building IDs not match between them?</label>
    <div class="show">
      <p>The building IDs and exact building characteristics between releases will not match because we re-sample our input characteristic distributions for every release. However, you can filter the building models using building characteristics to identify similar samples between releases. For instance, using building type, size, location, and wall construction type to identify similar models. The fields with the prefix “in.” show the available model inputs that you can use to do the comparison. You can see a complete list and description of available fields in the “data_dictionary.tsv” file on the OEDI Data Lake. Links to the datasets on OEDI are in the "Published Datasets" section of the <a href="docs/data.md">ComStock Data page</a> and <a href="https://natlabrockies.github.io/ResStock.github.io/docs/data.html">ResStock data page</a>.</p>
    </div>
  </li>

  <li class="acc" id="faq-aws-access-section"><input id="faq-aws-access" type="checkbox" /><label for="faq-aws-access">How can I use AWS Athena to query ComStock and ResStock datasets?</label>
    <div class="show">
      <p>Sample queries showing how to create prompts for different ComStock questions are available in the “<a href="docs/resources/how_to_guides/aws_athena_queries.md">AWS Athena Queries</a>” how-to guide. These examples can be easily adapted to ResStock datasets.</p>
      <p>A <a href="https://www.youtube.com/watch?v=qSR1MFpSiro">training video</a> on how to load ComStock and ResStock data into AWS Athena is also available.</p>
    </div>
  </li>

  <li class="acc" id="faq-agg-timeseries-section"><input id="faq-agg-timeseries" type="checkbox" /><label for="faq-agg-timeseries">What pre-aggregated timeseries data are available on the Open Energy Data Initiative (OEDI) data lake?</label>
    <div class="show">
      <p>Pre-aggregated timeseries data are available in the "timeseries_aggregates" directory on OEDI and are provided for multiple geographic levels:</p>
      <ul>
        <li>ASHRAE/IECC climate zone</li>
        <li>Building America climate zone</li>
        <li>ISO/RTO region</li>
        <li>State</li>
        <li>PUMA</li>
        <li>County</li>
      </ul>
      <p>The data are further disaggregated into separate files by building type.</p>
      <p>These files provide aggregate, weighted, subhourly end-use energy data by fuel type for all ComStock models that meet the specified criteria. For example, the file <b>up0-co-fullservicerestaurant</b> contains aggregate end use load profiles for all full-service restaurants in Colorado.</p>
      <p>Each file also includes "models_used" and "floor_area" columns, which indicate the number of ComStock models represented and the associated weighted floor area, respectively.</p>

    </div>
  </li>

</ul>

