<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89042.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy25osti/89042.pdf | publication_url: https://www.nlr.gov/docs/fy25osti/89042.pdf | corpus_version: 0a2f61f | corpus_path: upgrade_measures/measure_pdfs/89042.md | section: 3.2.1.1  Gathering Public Performance Data and Selecting Relevant Data | lines: 331-357 -->
## 3.2.1.1  Gathering Public Performance Data and Selecting Relevant Data

Table 1 shows a summary of some HP-RTU products relevant to this study that can be researched online by searching for standard efficiency products claimed by manufacturers. Key highlights from the table include the following.

- We have focused on products that manufacturers claim as standard efficiency.
- These products have common/prevalent characteristics. We define a standard efficiency product as follows:
- o Direct drive supply fan
- o Two stages of heat pump cooling
- o Single-stage heat pump heating (i.e., all compressors running at the same time)
- o Heat pump minimum lockout temperature of 0°F (-17.8°C)
- o Backup electric resistance heating
- o Backup heating runs at the same time as heat pump heating
- o Heat pump heating locking out below minimum operating temperature
- o For units with capacity of 5 tons and below, seasonal energy efficiency rating of 14 and heating seasonal performance factor of 8
- o For units with capacity of 6 tons and above, integrated energy efficiency ratio between 10.8 and 14.1 and COP at 47°F (8.3°C) between 3.2 and 3.5.
- Some of these products (and their performance data) that can be scraped from the internet do not meet the latest federal minimum efficiency requirements [3]. Thus, we decided to only include products that meet the minimum requirements when generating the new performance maps.
- While the minimum lockout temperature for heat pump heating is well-described in coldclimate heat pump product manuals, these standard efficiency products rarely provide this information. We decided to set the minimum heat pump lockout temperature to 0°F (-18°C) based on default settings from a couple of products, shown in Table 1.
- No single product provides all the required performance maps for EnergyPlus implementation:

- o Other than Carrier's and Lennox's manuals, all the other product manuals only provide performance maps for fully staged performances (e.g., capacity and input power) and do not provide separate performance maps for lower stage cooling.
- o One of the Carrier products is named as a standard efficiency product. However, this product includes advanced fan technology, making the overall efficiency higher than the other products.
- o Carrier products do not provide performance maps for the input power (i.e., metric for deriving the operating COP) depending on different operating conditions.
- o Unlike other products, Lennox's performance maps provide heating performance with fixed indoor temperature (70°F [21°C]) only.
- There are cases where some of these products have a variable frequency drive fan, dual fuel (i.e., gas backup heating) option, three or more cooling stages, two stages of heat pump heating, no backup heating as default purchase setting, etc. However, we are defining the standard efficiency to reflect the most common and prevalent options.
- Smaller units (e.g., capacity less than 6 tons) tend to have a single-stage compressor. To simplify performance maps between small and large units, to apply consistent performance across units, and to reflect the relatively more common type, we chose to model two-stage heat pump cooling for all units.
- The capacity and airflow differences between low and high stage cooling are derived from the manufacturers' performance data, as shown in Table 2. Thus, after the overall (i.e., high stage) capacity and airflow are determined based on design load and sizing algorithm in EnergyPlus, the low stage rated cooling capacity and airflow are calculated and implemented by multiplying 50% and 59%, respectively, to the high stage cooling capacity and airflow. As the relevant low stage airflow information (corresponding to the high stage or rated airflow) is not available in manufacturer manuals, some assumptions were made. Because ASHRAE 90.1-2022 [4] suggests that the low speed fan be operated at no more than 66% of the full speed, we assumed 66% of the rated airflow to be the low stage airflow for calculating the corresponding capacity at low stage. While this was applied for Lennox products, 66% of the rated airflows of Carrier products were beyond the airflow range reported in performance tables. Thus, based on engineering judgement, the middle airflows from the range provided in the tables were chosen where the ratio of low stage airflow to high stage airflow varied between 50% and 60% for Carrier products [5], [6], [7], [8]. These are all depicted in Table 2.

