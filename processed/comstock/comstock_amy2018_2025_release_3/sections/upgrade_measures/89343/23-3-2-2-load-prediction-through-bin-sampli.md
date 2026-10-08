<!-- comstock comstock_amy2018_2025_release_3 | upgrade_measures | measure_pdfs/89343.pdf | status: osti_pdf | source_url: https://www.nlr.gov/docs/fy24osti/89343.pdf | publication_url: https://www.nlr.gov/docs/fy24osti/89343.pdf | corpus_version: 0396270 | corpus_path: upgrade_measures/measure_pdfs/89343.md | section: 3.2.2  Load Prediction Through Bin Sampling | lines: 285-332 -->
## 3.2.2  Load Prediction Through Bin Sampling

The objective of utilizing bin-sampling techniques in this measure is to generate predicted load profiles that carry sufficient insight into the timing, shape, and magnitude of the building's daily peak demand. This method bins 365 days in a year (e.g., Jan. 1 = bin A, Jan. 2 = bin B, Jan. 3 =

bin A, …, Dec. 31 = bin Q) using weather data based on the assumption that for an individual building with consistent schedules (lighting schedule, plug load schedule, occupancy schedule, etc.), similar weather conditions lead to similar load profiles. The binning criterion is based on weather parameters that have the most impact on the target load variations. Specifically, for cooling load prediction, this measure uses two variables for binning-daily maximum outdoor air temperature (OATmax), and hour of daily maximum outdoor air temperature (OATmaxhour). The daily maximum outdoor air temperature is selected to characterize the seasonal weather variations, and the time of the maximum outdoor air temperature is selected to characterize the daily weather variations and to capture the relationship between maximum temperature and hour of peak load. For heating load prediction, on the other hand, the daily minimum outdoor air temperature (OATmin) should be selected instead of OATmax, and, correspondingly, the hour of daily minimum outdoor air temperature (OATminhour) would take the place of OATmaxhour. The binning criteria could be flexible for different scenarios. In the example scenario, bins are determined to distribute number of days in bins as evenly or normally as possible to make bins mathematically representative while considering the practical applications; from prior knowledge, more discretization is needed for the noon to afternoon period, when most cooling peaks take place, for cooling load prediction, specifically.

Table 2 summarizes the chosen bins in detail for a specific example weather input.

Table 2. Example Bins and Number of Days in Bins

| Bins    | OATmaxhour   | 12-2 p.m.   | 2-3 p.m.   | 3-4 p.m.   | 4-5 p.m.   | 5 p.m.-11 a.m.   |
|---------|--------------|-------------|------------|------------|------------|------------------|
| OATmax  | OATmax       | 12-2 p.m.   | 2-3 p.m.   | 3-4 p.m.   | 4-5 p.m.   | 5 p.m.-11 a.m.   |
|         |              |             |            |            |            | Other            |
| >32°C   | Very hot     | 13          | 28         | 20         | 4          | 1                |
| 30-32°C | Hot          | 27          | 8          | 17         | 1          | 0                |
| 26-30°C | Mild         | 14          | 15         | 21         | 9          | 2                |
| 18-26°C | Cool         | 19          | 16         | 32         | 13         | 9                |
| <18°C   | Other        | 9           | 20         | 41         | 9          | 17               |

Given appropriate binning results, the measure draws sample days from the bins. The samples are randomly selected, and the number of samples increases as the number of candidates in a bin increases to account for representativeness of drawn samples. The numbers of samples drawn from each bin depending on the bin size are summarized in Table 3, showing the computational efficiency and potential number of bins.

Table 3. Number of Samples Versus Number of Days in Bins

| # Days in Bins   | # Samples   |
|------------------|-------------|
| 0                | 0           |
| 1                | 1-7         |
| 8-14             | 2           |
| >14              | 3           |

After drawing samples, simulations are run on the sample days, and the load profile is extracted (using hourly time intervals) from the simulation results as sample loads. If multiple single-day samples are drawn for a given bin, the sampled load profiles are averaged to generate the representative single-day load profile for the bin. Then, the representative load profile will be replicated for all the days in the bin as their predicted load. A full year load prediction is thus constructed by populating representative daily load profiles for all days based on their bins. Figure 2 shows the daily load profiles (green) corresponding to the bins in Table 2, the drawn samples (red-dashed), and the representative load profiles (orange) derived from the samples for every bin.

Figure 2. Example daily load profiles (green) in bins, the samples drawn (red-dashed), and the representative load profiles (orange) derived from the samples

<!-- figure described by overlay: comstock_comstock_amy2018_2025_release_3/upgrade_measures/measure_pdfs/89343.yaml
     source: 89343_images/image_000003_08c15327cb8c2ad9c9282d0c3853081f84b896bd8f14097250684d5badca44d2.png
     method: vision-description
     described: 2026-08-20 -->

![Grid of small-multiple daily load-profile plots by temperature bin, showing binned profiles, drawn samples, and representative profiles](89343_images/image_000003_08c15327cb8c2ad9c9282d0c3853081f84b896bd8f14097250684d5badca44d2.png)

Figure 2. Grid of small-multiple line plots (5 rows by 5 columns) of daily load profiles by weather bin. Rows are daily-maximum-OAT categories (very hot, hot, mild, cool, other) and columns are hour-of-OATmax bins (12-2PM, 2-3PM, 3-4PM, 4-5PM, other); each subplot title carries the number of days in that bin (e.g. very hot 12-2PM 13, very hot 2-3PM 28, hot 12-2PM 27, cool 3-4PM 32, other 3-4PM 41), matching Table 2. Each subplot has x-axis hour of day (0-23) and y-axis Power (kW) to about 14. Green lines are the individual daily load profiles in the bin, red-dashed lines are the randomly drawn samples, and the orange line is the representative (averaged) profile used as the predicted load. Hotter bins show higher, sharper afternoon peaks; cool and other bins are low and flat, and the representative orange profiles track the bin's shape and peak timing well.

The green load profiles represent daily simulation results throughout the year corresponding to the bin. Note that the green profiles are for illustration only, and only a few of them will be obtained (red-dashed) through simulation in the method. The red-dashed load profiles are randomly selected samples from the green profiles in each bin (the number of samples depends on the number of green profiles in the bin as described in Table 3). The orange profiles are the representative load profiles derived from averaging the selected samples (red-dashed) and will be the predictive load profiles representing the days (green) in the same bins, respectively. As shown in Figure 2, most of the representative load profiles (orange) can capture the daily load shape and peak with acceptable deviations (error of predicted peak time is less than 2 hours).

This method is used as a proxy to characterize the mean/median performance of any applicable control systems providing demand flexibility, intended to represent actual predictions that could be made using historical measured data, with introduced uncertainty.

